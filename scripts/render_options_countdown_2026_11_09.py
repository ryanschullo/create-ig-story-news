#!/usr/bin/env python3
"""Render a reusable stock-options Instagram Story with genuinely empty countdown and link sticker spaces, actual fonts and original coin.

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
TEMPLATE = ROOT / "assets/layouts/options-countdown-2026-11-09.html"
BACKGROUND = ROOT / "assets/options-countdown-background-2026-11-09.png"
COIN = ROOT / "assets/moneyberg-coin-original.png"
LATO = ROOT / "assets/fonts/lato/Lato-Black.ttf"
OUTPUT = ROOT / "exports/options-countdown-2026-11-09.png"
AUDIT = ROOT / "briefs/options-countdown-2026-11-09-layout.json"
COIN_HASH = "4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716"
INNER = (104, 164, 961, 1536)
STICKER_INTERIORS = {
    "countdown-interior": (200, 820, 880, 1100),
    "link-interior": (240, 1210, 840, 1320),
}
GENERATION_PROMPTS = re.findall(r"```text\n(.*?)\n```", (ROOT / "assets/options-countdown-background-2026-11-09.md").read_text(), flags=re.DOTALL)
if not GENERATION_PROMPTS or any(not prompt.strip() or prompt.strip().lower() in {"undefined", "null"} for prompt in GENERATION_PROMPTS):
    raise ValueError("All original generation and editing prompts are required")
INTEGRATION = {
    "method": "Exact original coin PNG seated inside a physical brass mount in the options-themed environment, with compatible plum/teal light and contact shadow",
    "artwork": "Original uniformly scaled PNG; original portrait, lettering and circular rim preserved",
    "image_generation_role": "Text-free conceptual options-investing environment with quiet center and peripheral glass forms only",
    "topic": "Reusable stock-options Instagram Story with space for native countdown and link stickers",
    "category_badge": "OPTIONS INVESTING",
    "background_credit_on_graphic": False,
    "background_provenance": "Decorative conceptual options environment; peripheral shapes do not encode real financial data",
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
    with tempfile.TemporaryDirectory(prefix="moneyberg-options-countdown-", dir="/tmp") as temp:
        runtime_html = Path(temp) / "options-countdown-runtime.html"
        files = {
            "/runtime.html": (runtime_html, "text/html; charset=utf-8"),
            "/georgia-runtime.ttf": (georgia, "font/ttf"),
            "/assets/fonts/lato/Lato-Black.ttf": (LATO, "font/ttf"),
            "/assets/options-countdown-background-2026-11-09.png": (BACKGROUND, "image/png"),
            "/assets/moneyberg-coin-original.png": (COIN, "image/png"),
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
                    text_role:element.dataset.textRole || "label", font_family:css.fontFamily, font_weight:css.fontWeight, font_size:css.fontSize};
                });
                const panels = Array.from(document.querySelectorAll('[data-news-panel]')).map(element =>
                  ({id:element.id, bounds:rect(element.getBoundingClientRect())}));
                const scene_elements = Array.from(document.querySelectorAll('[data-scene-element]')).map(element => {
                  const css=getComputedStyle(element);
                  return {id:element.id, bounds:rect(element.getBoundingClientRect()), box_shadow:css.boxShadow, background:css.backgroundImage};
                });
                const sticker_interiors = Array.from(document.querySelectorAll('[data-sticker-interior]')).map(element => {
                  const css=getComputedStyle(element);
                  return {id:element.id, bounds:rect(element.getBoundingClientRect()),
                    child_count:element.childElementCount, text:element.textContent,
                    background_color:css.backgroundColor, background_image:css.backgroundImage,
                    border_widths:[css.borderTopWidth,css.borderRightWidth,css.borderBottomWidth,css.borderLeftWidth],
                    box_shadow:css.boxShadow, before_content:getComputedStyle(element,'::before').content,
                    after_content:getComputedStyle(element,'::after').content};
                });
                const sticker_frames = Array.from(document.querySelectorAll('[data-sticker-frame]')).map(element => {
                  const css=getComputedStyle(element);
                  return {id:element.id, interior:element.dataset.stickerFrame,
                    bounds:rect(element.getBoundingClientRect()), child_count:element.childElementCount,
                    text:element.textContent, background_color:css.backgroundColor,
                    background_image:css.backgroundImage, box_shadow:css.boxShadow,
                    border_widths:[css.borderTopWidth,css.borderRightWidth,css.borderBottomWidth,css.borderLeftWidth],
                    border_radius:css.borderRadius, before_content:getComputedStyle(element,'::before').content,
                    after_content:getComputedStyle(element,'::after').content};
                });
                const untracked_visible_text = [];
                const walker = document.createTreeWalker(document.getElementById('stage'), NodeFilter.SHOW_TEXT);
                while(walker.nextNode()) {
                  const node=walker.currentNode, parent=node.parentElement;
                  if(node.textContent.trim() && !parent.closest('[data-news-text]')) {
                    const css=getComputedStyle(parent);
                    if(css.display!=='none' && css.visibility!=='hidden' && css.opacity!=='0') untracked_visible_text.push(node.textContent.trim());
                  }
                }
                const stage_element_ids = Array.from(document.querySelectorAll('#stage *')).map(element=>element.id);
                return {text, panels, scene_elements, sticker_interiors, sticker_frames,
                  untracked_visible_text, stage_element_ids, fonts:Array.from(document.fonts).map(face =>
                  ({family:face.family, weight:face.weight, status:face.status})),
                  images:Array.from(document.images).map(image => ({id:image.id,
                    natural_width:image.naturalWidth, natural_height:image.naturalHeight,
                    object_fit:getComputedStyle(image).objectFit, clip_path:getComputedStyle(image).clipPath,
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
            for entry in layout["text"] + layout["panels"]:
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
            required = {
                "brand": "MONEYBERG NEWS BRIEF",
                "category": "OPTIONS INVESTING",
                "headline-one": "STOCK",
                "headline-two": "OPTIONS",
                "tagline": "Strategy starts with timing.",
            }
            actual_copy = {item["id"]: item["text"] for item in layout["text"]}
            for key, text in required.items():
                if actual_copy.get(key) != text:
                    raise ValueError(f"Required factual scope is missing: {key}")

            if actual_copy != required or layout["untracked_visible_text"]:
                raise ValueError("Reusable template contains extra text or placeholder copy")
            expected_stage_ids = set(required) | {
                "background", "coin-installation", "coin", "coin-contact",
                "countdown-frame", "countdown-interior", "link-frame", "link-interior",
            }
            if (set(layout["stage_element_ids"]) != expected_stage_ids
                    or len(layout["stage_element_ids"]) != len(expected_stage_ids)):
                raise ValueError("Unexpected element could add an icon or placeholder to the reusable template")

            def overlaps(a, b):
                return (a["left"] < b["right"] and a["right"] > b["left"]
                        and a["top"] < b["bottom"] and a["bottom"] > b["top"])

            if len(layout["sticker_interiors"]) != 2 or len(layout["sticker_frames"]) != 2:
                raise ValueError("Both blank sticker spaces must be present")
            for interior in layout["sticker_interiors"]:
                expected = STICKER_INTERIORS[interior["id"]]
                bounds = interior["bounds"]
                if any(abs(bounds[key] - value) > .02 for key, value in zip(("left", "top", "right", "bottom"), expected)):
                    raise ValueError(f"Reserved sticker bounds changed: {interior['id']}")
                if (interior["text"].strip() or interior["child_count"]
                        or interior["background_color"] != "rgba(0, 0, 0, 0)"
                        or interior["background_image"] != "none" or interior["box_shadow"] != "none"
                        or any(float(width.removesuffix("px")) != 0 for width in interior["border_widths"])
                        or any(interior[key] not in ("none", "normal", '""') for key in ("before_content", "after_content"))):
                    raise ValueError(f"Sticker interior is not empty and transparent: {interior['id']}")
                if (bounds["left"] < INNER[0] or bounds["top"] < INNER[1]
                        or bounds["right"] > INNER[2] or bounds["bottom"] > INNER[3]):
                    raise ValueError("Reserved sticker space exceeds content bounds")
                for element in layout["text"] + layout["scene_elements"] + [coin]:
                    if overlaps(bounds, element["bounds"]):
                        raise ValueError(f"Authored content overlaps {interior['id']}: {element['id']}")
                frame = next(item for item in layout["sticker_frames"] if item["interior"] == interior["id"])
                f = frame["bounds"]
                if (frame["text"].strip() or frame["child_count"]
                        or frame["background_color"] != "rgba(0, 0, 0, 0)"
                        or frame["background_image"] != "none" or frame["box_shadow"] != "none"
                        or any(float(width.removesuffix("px")) > 1 for width in frame["border_widths"])
                        or any(frame[key] not in ("none", "normal", '""') for key in ("before_content", "after_content"))):
                    raise ValueError("A sticker frame introduces a fill, icon, text or heavy border")
                if min(bounds["left"]-f["left"], bounds["top"]-f["top"], f["right"]-bounds["right"], f["bottom"]-bounds["bottom"]) < 16:
                    raise ValueError("Sticker outline intrudes on reserved clear space")

            for entry in layout["text"]:
                size = float(entry["font_size"].removesuffix("px"))
                if size < 33:
                    raise ValueError(f"Authored text falls below the 33 px minimum: {entry['id']} ({size}px)")
                role_minimum = {"headline": 51, "body": 35}.get(entry["text_role"], 33)
                if size < role_minimum:
                    raise ValueError(f"Text role minimum not met: {entry['id']} ({size}px < {role_minimum}px)")
            for entry in layout["text"] + layout["panels"]:
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
             "sources": [],
             "template_scope": {
                 "kind": "Reusable stock-options Instagram Story sticker template, not a news report",
                 "production_date": "2026-11-09",
                 "visible_edition_date": False,
                 "event_title_prefilled": False,
                 "countdown_rendered": False,
                 "url_rendered": False,
                 "source_attribution_rendered": False,
                 "performance_promise_rendered": False,
                 "placeholder_text_or_icons_rendered": False,
                 "authored_text_element_count": 5,
                 "source_chart_used": False,
                 "native_instagram_stickers_to_be_added_by_user": ["countdown", "link"],
             },
             "sticker_safe_areas": {
                 "countdown": {"left": 200, "top": 820, "right": 880, "bottom": 1100, "width": 680, "height": 280},
                 "link": {"left": 240, "top": 1210, "right": 840, "bottom": 1320, "width": 600, "height": 110},
                 "both_interiors_empty_and_transparent_in_dom": True,
                 "no_authored_text_images_coin_or_scene_overlays_in_interiors": True,
                 "subtle_outline_clearance_px": 16,
                 "no_placeholder_text_numbers_or_icons": True,
                 "background_visual_inspection_required_in_addition_to_dom_checks": True,
             },
             "output_sha256": sha256(OUTPUT)}
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(f"Rendered {OUTPUT.relative_to(ROOT)} at 1080 × 1920")
    print(f"Verified {len(layout['text'])} text elements, {len(layout['panels'])} panels, and actual browser fonts.")
    print("Original coin and both empty sticker spaces verified; Georgia runtime-only; Python does not edit image pixels.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--georgia-font", type=Path, required=True)
    parser.add_argument("--background-source", type=Path)
    args = parser.parse_args()
    asyncio.run(render(args.georgia_font, args.background_source))
