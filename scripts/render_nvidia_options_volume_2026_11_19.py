#!/usr/bin/env python3
"""Render verified NVIDIA November18 options activity with exact fonts, official logo and original coin.

The committed HTML is a template. Its Georgia URL is populated only in a runtime
HTML file outside the repository. No font bytes are embedded in committed files,
and no pixel-editing library is used.
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import re
import shutil
import struct
import tempfile
import threading
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

from fontTools.ttLib import TTFont
from playwright.async_api import async_playwright


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "assets/layouts/nvidia-options-volume-2026-11-19.html"
BACKGROUND = ROOT / "assets/nvidia-options-volume-background-2026-11-19.png"
COIN = ROOT / "assets/moneyberg-coin-original.png"
NVIDIA_LOGO = ROOT / "assets/logos/nvidia/nvidia-logo-horiz-wht-original.png"
NVIDIA_LOGO_HASH = "b4937f65c1f3a07536507865c2947d9c65a66131f2f137c661bb41aa43fce2ca"
NVIDIA_LOGO_ART = (552, 820, 2736, 520)
LATO = ROOT / "assets/fonts/lato/Lato-Black.ttf"
OUTPUT = ROOT / "exports/nvidia-options-volume-2026-11-19.png"
AUDIT = ROOT / "briefs/nvidia-options-volume-2026-11-19-layout.json"
COIN_HASH = "4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716"
INNER = (104, 164, 961, 1536)
PROMPT_DOCUMENT = (ROOT / "assets/nvidia-options-volume-background-2026-11-19.md").read_text()
GENERATION_PROMPTS = re.findall(r"```text\n(.*?)\n```", PROMPT_DOCUMENT, flags=re.DOTALL)
if not GENERATION_PROMPTS:
    GENERATION_PROMPTS = re.findall(r"## Generation prompt\n\n(.*?)(?=\n## |\Z)", PROMPT_DOCUMENT, flags=re.DOTALL)
if not GENERATION_PROMPTS or any(not prompt.strip() or prompt.strip().lower() in {"undefined", "null"} for prompt in GENERATION_PROMPTS):
    raise ValueError("All original generation and editing prompts are required")
INTEGRATION = {
    "method": "Exact original coin PNG seated in an upper-right brass recess in a NVIDIA-green and black-glass trading workstation scene, with compatible lighting and contact shading",
    "artwork": "Original uniformly scaled PNG; original portrait, lettering and circular rim preserved",
    "image_generation_role": "Text-free conceptual professional electronic-trading workstation with NVIDIA-green edge lighting against black glass; the official logo is composited separately unchanged",
    "topic": "NVIDIA options traded 6.43 million contracts on November 18; calls were 63.77% of volume; total volume was 70.84% above the reported 30-day average",
    "category_badge": "OPTIONS INVESTING",
    "background_credit_on_graphic": False,
    "background_provenance": "Conceptual trading architecture, not an actual market-data display or evidence of future stock-market direction",
}



def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_font(path: Path, expected_family: str, expected_weight: int):
    if not path.is_file():
        raise FileNotFoundError(f"Required original font file is missing: {path}")
    with TTFont(path) as face:
        families = {record.toUnicode() for record in face["name"].names if record.nameID in (1, 16)}
        if expected_family not in families or face["OS/2"].usWeightClass != expected_weight:
            raise ValueError(f"Expected {expected_family} weight {expected_weight} at {path}")


@contextmanager
def runtime_document(georgia: Path):
    """Serve only the intended assets and ephemeral document on loopback."""
    template = TEMPLATE.read_text(encoding="utf-8")
    if "__GEORGIA_FONT_URI__" not in template or "__ASSET_BASE_URI__" not in template:
        raise ValueError("The committed template must retain its runtime placeholders")
    with tempfile.TemporaryDirectory(prefix="moneyberg-nvidia-options-", dir="/tmp") as temp:
        runtime_html = Path(temp) / "nvidia-options-runtime.html"
        files = {
            "/runtime.html": (runtime_html, "text/html; charset=utf-8"),
            "/georgia-runtime.ttf": (georgia, "font/ttf"),
            "/assets/fonts/lato/Lato-Black.ttf": (LATO, "font/ttf"),
            "/assets/nvidia-options-volume-background-2026-11-19.png": (BACKGROUND, "image/png"),
            "/assets/moneyberg-coin-original.png": (COIN, "image/png"),
            "/assets/logos/nvidia/nvidia-logo-horiz-wht-original.png": (NVIDIA_LOGO, "image/png"),
        }

        class AssetHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                resource = files.get(urlsplit(self.path).path)
                if resource is None:
                    self.send_error(404)
                    return
                path, content_type = resource
                data = path.read_bytes()
                self.send_response(200)
                self.send_header("Content-Type", content_type)
                self.send_header("Content-Length", str(len(data)))
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(data)

            def log_message(self, *_args):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), AssetHandler)
        base = f"http://127.0.0.1:{server.server_address[1]}"
        html = template.replace("__GEORGIA_FONT_URI__", base + "/georgia-runtime.ttf")
        html = html.replace("__ASSET_BASE_URI__", base + "/assets/")
        runtime_html.write_text(html, encoding="utf-8")
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            yield base + "/runtime.html"
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


async def render(georgia: Path, background_source: Path | None):
    verify_font(LATO, "Lato", 900)
    verify_font(georgia, "Georgia", 400)
    if sha256(COIN) != COIN_HASH:
        raise ValueError("The original coin master has changed")
    logo_bytes = NVIDIA_LOGO.read_bytes()
    if (sha256(NVIDIA_LOGO) != NVIDIA_LOGO_HASH
            or logo_bytes[:8] != b"\x89PNG\r\n\x1a\n"
            or struct.unpack(">II", logo_bytes[16:24]) != (3840, 2160)):
        raise ValueError("The unchanged official NVIDIA logo master has changed")
    if background_source is not None:
        if BACKGROUND.exists() and sha256(BACKGROUND) != sha256(background_source):
            raise ValueError("A different background already exists; refusing to overwrite it")
        if not BACKGROUND.exists():
            shutil.copyfile(background_source, BACKGROUND)
    if not BACKGROUND.is_file():
        raise FileNotFoundError("Supply the generated background using --background-source")

    with runtime_document(georgia) as runtime_url:
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(
                executable_path="/usr/bin/chromium", headless=True,
                args=["--no-sandbox", "--disable-dev-shm-usage"],
            )
            page = await browser.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
            await page.goto(runtime_url, wait_until="load")
            await page.evaluate("""async () => {
                await Promise.all([
                  document.fonts.load('900 35px "Moneyberg Lato Black"'),
                  document.fonts.load('400 35px "Moneyberg Georgia"')
                ]);
                await document.fonts.ready;
                await Promise.all(Array.from(document.images).map(image => image.decode()));
            }""")
            layout = await page.evaluate("""() => {
                const rect = value => ({left:value.left, top:value.top,
                  right:value.right, bottom:value.bottom, width:value.width, height:value.height});
                const text = Array.from(document.querySelectorAll('[data-news-text]')).map(element => {
                  const range = document.createRange(); range.selectNodeContents(element);
                  const css = getComputedStyle(element);
                  return {id:element.id, text:element.textContent,
                    bounds:rect(range.getBoundingClientRect()), element_bounds:rect(element.getBoundingClientRect()),
                    text_role:element.dataset.textRole || "label", font_family:css.fontFamily, font_weight:css.fontWeight, font_size:css.fontSize, color:css.color};
                });
                const panels = Array.from(document.querySelectorAll('[data-news-panel]')).map(element =>
                  ({id:element.id, bounds:rect(element.getBoundingClientRect())}));
                const illustrations = Array.from(document.querySelectorAll('[data-news-illustration]')).map(element =>
                  ({id:element.id, bounds:rect(element.getBoundingClientRect())}));
                const scene_elements = Array.from(document.querySelectorAll('[data-scene-element]')).map(element => {
                  const css=getComputedStyle(element);
                  return {id:element.id, bounds:rect(element.getBoundingClientRect()), box_shadow:css.boxShadow, background:css.backgroundImage};
                });
                return {text, panels, illustrations, scene_elements, fonts:Array.from(document.fonts).map(face =>
                  ({family:face.family, weight:face.weight, status:face.status})),
                  images:Array.from(document.images).map(image => ({id:image.id,
                    natural_width:image.naturalWidth, natural_height:image.naturalHeight,
                    object_fit:getComputedStyle(image).objectFit, clip_path:getComputedStyle(image).clipPath,
                    filter:getComputedStyle(image).filter, transform:getComputedStyle(image).transform,
                    opacity:getComputedStyle(image).opacity,
                    bounds:rect(image.getBoundingClientRect())})),
                  document_width:document.documentElement.scrollWidth,
                  document_height:document.documentElement.scrollHeight};
            }""")

            coin = next(image for image in layout["images"] if image["id"] == "coin")
            coin_bounds = coin["bounds"]
            if (coin["natural_width"], coin["natural_height"]) != (2084, 2084):
                raise ValueError("The browser did not load the full original coin PNG")
            if (coin_bounds["left"] < 0 or coin_bounds["right"] > 1080
                    or coin_bounds["top"] < 0 or coin_bounds["bottom"] > 0.75 * 1920
                    or abs(coin_bounds["width"] - coin_bounds["height"]) > 0.01):
                raise ValueError(f"Original coin violates whole-coin upper-75% or aspect rule: {coin_bounds}")
            if coin["object_fit"] != "contain" or coin["clip_path"] != "none":
                raise ValueError("Original coin may be cropped")
            logo = next(image for image in layout["images"] if image["id"] == "nvidia-logo")
            logo_viewport = next(item for item in layout["illustrations"] if item["id"] == "nvidia-logo-viewport")
            if (logo["natural_width"], logo["natural_height"]) != (3840, 2160):
                raise ValueError("The browser did not load the complete official NVIDIA logo master")
            if (logo["object_fit"] != "contain" or logo["clip_path"] != "none"
                    or logo["filter"] != "none" or logo["transform"] != "none" or logo["opacity"] != "1"):
                raise ValueError("Official NVIDIA logo pixels may be altered")
            logo_scale = logo["bounds"]["width"] / 3840
            if abs(logo["bounds"]["height"] - 2160 * logo_scale) > 0.02:
                raise ValueError("The NVIDIA logo is not uniformly scaled")
            logo_art_bounds = {
                "left": logo["bounds"]["left"] + NVIDIA_LOGO_ART[0] * logo_scale,
                "top": logo["bounds"]["top"] + NVIDIA_LOGO_ART[1] * logo_scale,
                "width": NVIDIA_LOGO_ART[2] * logo_scale,
                "height": NVIDIA_LOGO_ART[3] * logo_scale,
            }
            logo_art_bounds["right"] = logo_art_bounds["left"] + logo_art_bounds["width"]
            logo_art_bounds["bottom"] = logo_art_bounds["top"] + logo_art_bounds["height"]
            viewport = logo_viewport["bounds"]
            if (logo_art_bounds["left"] < viewport["left"]
                    or logo_art_bounds["top"] < viewport["top"]
                    or logo_art_bounds["right"] > viewport["right"]
                    or logo_art_bounds["bottom"] > viewport["bottom"]):
                raise ValueError("NVIDIA viewport crops actual artwork, not merely unused solid-black padding")
            for entry in layout["text"] + layout["panels"]:
                box = entry["bounds"]
                if (box["left"] < viewport["right"] and box["right"] > viewport["left"]
                        and box["top"] < viewport["bottom"] and box["bottom"] > viewport["top"]):
                    raise ValueError(f"Official NVIDIA logo overlaps news content: {entry['id']}")
            for entry in layout["text"] + layout["panels"] + layout["illustrations"]:
                box=entry["bounds"]
                if (box["left"] < coin_bounds["right"] and box["right"] > coin_bounds["left"]
                        and box["top"] < coin_bounds["bottom"] and box["bottom"] > coin_bounds["top"]):
                    raise ValueError(f"Coin overlaps news content: {entry['id']}")
            for i, left in enumerate(layout["text"]):
                a=left["bounds"]
                for right in layout["text"][i+1:]:
                    b=right["bounds"]
                    if a["left"] < b["right"] and a["right"] > b["left"] and a["top"] < b["bottom"] and a["bottom"] > b["top"]:
                        raise ValueError(f"Text overlaps: {left['id']} / {right['id']}")
            scene={entry["id"]:entry for entry in layout["scene_elements"]}
            if scene["coin-installation"]["box_shadow"] == "none" or scene["coin-contact"]["box_shadow"] == "none":
                raise ValueError("Scene integration is missing recess/contact shading")
            if any("Background:" in item["text"] for item in layout["text"]):
                raise ValueError("An unwanted background-production credit remains")
            required = {'brand': 'MONEYBERG NEWS BRIEF', 'category': 'OPTIONS INVESTING', 'date': 'NOVEMBER 19, 2026', 'headline': 'OPTIONS VOLUME', 'volume': '6.43M', 'volume-label': 'CONTRACTS TRADED', 'period': 'NOVEMBER 18 SESSION', 'call-value': '63.77%', 'call-label-one': 'CALL SHARE', 'call-label-two': 'OF VOLUME', 'average-value': '70.84%', 'average-label-one': 'ABOVE THE', 'average-label-two': '30-DAY AVERAGE', 'ratio-one': 'Volume was 170.84% of its', 'ratio-two': '30-day average.', 'source-one': 'Source: Moomoo • Nov. 18, 2026 activity', 'source-two': 'November 19 edition • Options trading volume'}
            actual_copy = {item["id"]: item["text"] for item in layout["text"]}
            for key, text in required.items():
                if actual_copy.get(key) != text:
                    raise ValueError(f"Required factual scope is missing: {key}")

            for entry in layout["text"]:
                size = float(entry["font_size"].removesuffix("px"))
                if size < 33:
                    raise ValueError(f"Authored text falls below the 33 px minimum: {entry['id']} ({size}px)")
                role_minimum = {"headline": 51, "body": 35}.get(entry["text_role"], 33)
                if size < role_minimum:
                    raise ValueError(f"Text role minimum not met: {entry['id']} ({size}px < {role_minimum}px)")
            for entry in layout["text"] + layout["panels"] + layout["illustrations"]:
                box = entry["bounds"]
                if (box["left"] < INNER[0] or box["top"] < INNER[1]
                        or box["right"] > INNER[2] or box["bottom"] > INNER[3]):
                    raise ValueError(f"Content exceeds required inner bounds: {entry}")
            if layout["document_width"] != 1080 or layout["document_height"] != 1920:
                raise ValueError("The HTML document overflows the canvas")

            cdp = await page.context.new_cdp_session(page)
            await cdp.send("DOM.enable")
            await cdp.send("CSS.enable")
            document = await cdp.send("DOM.getDocument")
            platform_fonts = []
            for entry in layout["text"]:
                node = await cdp.send("DOM.querySelector", {
                    "nodeId": document["root"]["nodeId"], "selector": f"#{entry['id']}"})
                actual = await cdp.send("CSS.getPlatformFontsForNode", {"nodeId": node["nodeId"]})
                expected = "Lato" if entry["font_weight"] == "900" else "Georgia"
                if (not actual["fonts"] or any(font["familyName"] != expected or not font["isCustomFont"]
                                               for font in actual["fonts"])):
                    raise ValueError(f"Browser used a substituted font for {entry['id']}: {actual}")
                platform_fonts.append({"id": entry["id"], "fonts": actual["fonts"]})
            for face in layout["fonts"]:
                if face["status"] != "loaded":
                    raise ValueError("A required font did not finish loading")

            OUTPUT.parent.mkdir(parents=True, exist_ok=True)
            await page.screenshot(path=str(OUTPUT), full_page=False, animations="disabled")
            await browser.close()

    data = OUTPUT.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n" or struct.unpack(">II", data[16:24]) != (1080, 1920):
        raise ValueError("Screenshot dimensions or format are incorrect")
    audit = {"dimensions": [1080, 1920], "inner_bounds": INNER,
             "minimum_authored_font_size_px": 33, "minimum_body_font_size_px": 35, "minimum_headline_font_size_px": 51, "font_size_minimum_verified": True,
             "renderer": "Chromium via Playwright; HTML/CSS screenshot",
             "background_sha256": sha256(BACKGROUND), "original_coin_sha256": sha256(COIN),
             "lato_black_sha256": sha256(LATO), "georgia_runtime_sha256": sha256(georgia),
             "georgia_redistributed": False, "layout": layout, "platform_fonts": platform_fonts,
             "coin_bounds": coin_bounds, "whole_coin_upper_75_percent_verified": True,
             "integration": INTEGRATION, "generation_prompts": GENERATION_PROMPTS,
             "nvidia_logo": {
                 "path": str(NVIDIA_LOGO.relative_to(ROOT)), "sha256": sha256(NVIDIA_LOGO),
                 "original_dimensions": [3840, 2160], "original_bytes": NVIDIA_LOGO.stat().st_size,
                 "original_art_bounds_xywh": NVIDIA_LOGO_ART,
                 "rendered_art_bounds": logo_art_bounds, "viewport_bounds": viewport,
                 "uniform_scale_verified": True, "only_unused_solid_black_padding_excluded": True,
                 "source_has_alpha_channel_but_is_fully_opaque": True,
                 "official_gallery": "https://nvidianews.nvidia.com/multimedia/corporate/nvidia-logos",
                 "original_asset_url": "https://iprsoftwaremedia.com/219/files/202512/nvidia-logo-horiz-wht-16x9.png?download=true",
                 "master_unchanged": True,
             },
             "source_access": "Full Moomoo report read through its public reader representation after the original site redirected to HTTP 403; original infographic downloaded unchanged and reviewed on November 19, 2026.",
             "sources": ["https://www.moomoo.com/news/post/1005082970/nvidia-options-spot-on-on-november-18th-6-43-million"],
             "reporting_scope": json.loads((ROOT / "briefs/nvidia-options-volume-2026-11-19-source.json").read_text()),
             "output_sha256": sha256(OUTPUT)}
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(f"Rendered {OUTPUT.relative_to(ROOT)} at 1080 × 1920")
    print(f"Verified {len(layout['text'])} text elements, {len(layout['panels'])} panels, and actual browser fonts.")
    print("Original coin, NVIDIA logo and November 18 options-volume scope verified; Georgia runtime-only; Python does not edit image pixels.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--georgia-font", type=Path, required=True)
    parser.add_argument("--background-source", type=Path)
    args = parser.parse_args()
    asyncio.run(render(args.georgia_font, args.background_source))
