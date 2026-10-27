#!/usr/bin/env python3
"""Render the Anthropic IPO Story in Chromium, using real local font files.

The committed HTML is a template. Its Georgia URL is populated only in a runtime
HTML file outside the repository. No font bytes are embedded in committed files,
and no pixel-editing library is used.
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
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
TEMPLATE = ROOT / "assets/layouts/anthropic-ipo-2026-10-26-astra.html"
BACKGROUND = ROOT / "assets/anthropic-ipo-background-astra.png"
COIN = ROOT / "assets/moneyberg-coin-original.png"
LOGO = ROOT / "assets/logos/anthropic-wordmark-original.svg"
LATO = ROOT / "assets/fonts/lato/Lato-Black.ttf"
OUTPUT = ROOT / "exports/anthropic-ipo-2026-10-26-astra.png"
AUDIT = ROOT / "briefs/anthropic-ipo-2026-10-26-astra-layout.json"
COIN_HASH = "4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716"
LOGO_HASH = "eb0f063a7a66a42ca0b1db7696555030d1afe80c63896a594ecdbb90e980cb7d"
INNER = (104, 164, 961, 1536)


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
    with tempfile.TemporaryDirectory(prefix="moneyberg-anthropic-", dir="/tmp") as temp:
        runtime_html = Path(temp) / "anthropic-ipo-runtime.html"
        files = {
            "/runtime.html": (runtime_html, "text/html; charset=utf-8"),
            "/georgia-runtime.ttf": (georgia, "font/ttf"),
            "/assets/fonts/lato/Lato-Black.ttf": (LATO, "font/ttf"),
            "/assets/anthropic-ipo-background-astra.png": (BACKGROUND, "image/png"),
            "/assets/moneyberg-coin-original.png": (COIN, "image/png"),
            "/assets/logos/anthropic-wordmark-original.svg": (LOGO, "image/svg+xml"),
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
    if sha256(LOGO) != LOGO_HASH:
        raise ValueError("The official Anthropic wordmark has changed")
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
                  document.fonts.load('900 32px "Moneyberg Lato Black"'),
                  document.fonts.load('400 32px "Moneyberg Georgia"')
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
                    font_family:css.fontFamily, font_weight:css.fontWeight, font_size:css.fontSize};
                });
                const panels = Array.from(document.querySelectorAll('[data-news-panel]')).map(element =>
                  ({id:element.id, bounds:rect(element.getBoundingClientRect())}));
                const news_images = Array.from(document.querySelectorAll('[data-news-image]')).map(element =>
                  ({id:element.id, bounds:rect(element.getBoundingClientRect())}));
                const scene_elements = Array.from(document.querySelectorAll('[data-scene-element]')).map(element => {
                  const css=getComputedStyle(element);
                  return {id:element.id, bounds:rect(element.getBoundingClientRect()),
                    background:css.backgroundImage, box_shadow:css.boxShadow,
                    mix_blend_mode:css.mixBlendMode, opacity:css.opacity};
                });
                const coin=document.getElementById('coin');
                const coin_css=getComputedStyle(coin);
                return {text, panels, news_images, scene_elements,
                  coin_style:{opacity:coin_css.opacity, mix_blend_mode:coin_css.mixBlendMode,
                    object_fit:coin_css.objectFit, transform:coin_css.transform}, fonts:Array.from(document.fonts).map(face =>
                  ({family:face.family, weight:face.weight, status:face.status})),
                  images:Array.from(document.images).map(image => ({id:image.id,
                    natural_width:image.naturalWidth, natural_height:image.naturalHeight,
                    bounds:rect(image.getBoundingClientRect())})),
                  document_width:document.documentElement.scrollWidth,
                  document_height:document.documentElement.scrollHeight};
            }""")

            for entry in layout["text"] + layout["panels"] + layout["news_images"]:
                box = entry["bounds"]
                if (box["left"] < INNER[0] or box["top"] < INNER[1]
                        or box["right"] > INNER[2] or box["bottom"] > INNER[3]):
                    raise ValueError(f"Content exceeds required inner bounds: {entry}")
            if layout["document_width"] != 1080 or layout["document_height"] != 1920:
                raise ValueError("The HTML document overflows the canvas")
            logo_image = next(image for image in layout["images"] if image["id"] == "anthropic-logo")
            logo_bounds = logo_image["bounds"]
            if (logo_image["natural_width"], logo_image["natural_height"]) != (570, 64):
                raise ValueError("The official wordmark must retain its original 570 × 64 dimensions")
            if abs(logo_bounds["width"] / logo_bounds["height"] - 570 / 64) > 0.005:
                raise ValueError("The official wordmark has been stretched")

            coin_image = next(image for image in layout["images"] if image["id"] == "coin")
            coin_bounds = coin_image["bounds"]
            if (coin_image["natural_width"], coin_image["natural_height"]) != (2084, 2084):
                raise ValueError("The coin must use the original square master")
            if (coin_bounds["top"] < 0 or coin_bounds["bottom"] > 1440
                    or coin_bounds["left"] < 0 or coin_bounds["right"] > 1080):
                raise ValueError("The entire coin must fit within the upper 75% of the canvas")
            if abs(coin_bounds["width"] - coin_bounds["height"]) > 0.01:
                raise ValueError("The original coin must be scaled uniformly")
            if layout["coin_style"] != {"opacity":"1", "mix_blend_mode":"multiply",
                                        "object_fit":"contain", "transform":"none"}:
                raise ValueError("Unexpected destructive coin style")
            scene = {entry["id"]:entry for entry in layout["scene_elements"]}
            for scene_id in ["coin-seat", "coin-seat-reveal", "coin-contact", "coin-surface-glaze"]:
                if scene_id not in scene:
                    raise ValueError(f"Missing scene-integration element: {scene_id}")
            socket = scene["coin-seat"]["bounds"]
            if not (socket["left"] < coin_bounds["left"] < coin_bounds["right"] < socket["right"]
                    and socket["top"] < coin_bounds["top"] < coin_bounds["bottom"] < socket["bottom"]):
                raise ValueError("Coin must sit fully inside its recessed architectural socket")
            if scene["coin-seat"]["box_shadow"] == "none" or scene["coin-contact"]["box_shadow"] == "none":
                raise ValueError("Surface integration requires contact and recess shading")
            if "Background: editorial illustration" in await page.locator("body").inner_text():
                raise ValueError("The removed production footer must not return")
            for entry in layout["text"] + layout["news_images"]:
                box=entry["bounds"]
                if (box["left"] < coin_bounds["right"] and box["right"] > coin_bounds["left"]
                        and box["top"] < coin_bounds["bottom"] and box["bottom"] > coin_bounds["top"]):
                    raise ValueError(f"Coin interferes with news content: {entry['id']}")

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
             "renderer": "Chromium via Playwright; HTML/CSS screenshot",
             "background_sha256": sha256(BACKGROUND), "original_coin_sha256": sha256(COIN),
             "background_provenance": {"tool":"image_gen.imagegen", "operation":"generate new Anthropic editorial architecture background",
                 "generated_source":"/workspace/generated_images/exec-5372fab9-fa34-451c-a1c2-8037ccff7359.png",
                 "subject":"tactile warm ivory paper, terracotta and copper AI architecture with front-facing clay pier at mid-right",
                 "contains_generated_coin":False},
             "coin_actual_bounds":coin_bounds, "coin_whole_upper_75_percent":True,
             "coin_integration_method":"Exact original PNG scaled uniformly inside a shallow bronze recess in the generated terracotta pier; multiply blending, scene-matched copper bevel and inset contact shadow with a non-destructive warm soft-light glaze. No generated coin, portrait or lettering.",
             "production_footer_removed":True,
             "original_logo_sha256": sha256(LOGO), "logo_natural_dimensions": [570, 64],
             "logo_rendered_aspect_ratio": logo_bounds["width"] / logo_bounds["height"],
             "lato_black_sha256": sha256(LATO), "georgia_runtime_sha256": sha256(georgia),
             "georgia_redistributed": False, "layout": layout, "platform_fonts": platform_fonts,
             "output_sha256": sha256(OUTPUT)}
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(f"Rendered {OUTPUT.relative_to(ROOT)} at 1080 × 1920")
    print(f"Verified {len(layout['text'])} text elements, {len(layout['panels'])} panels, and actual browser fonts.")
    print("Original 570:64 Anthropic SVG and coin preserved; Georgia remains runtime-only.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--georgia-font", type=Path, required=True)
    parser.add_argument("--background-source", type=Path)
    args = parser.parse_args()
    asyncio.run(render(args.georgia_font, args.background_source))
