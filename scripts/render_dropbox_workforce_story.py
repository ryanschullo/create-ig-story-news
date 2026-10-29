#!/usr/bin/env python3
"""Render the Dropbox workforce Story with actual fonts and the original coin integrated in an office-panel recess.

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
TEMPLATE = ROOT / "assets/layouts/dropbox-workforce-cuts-2026-10-28.html"
BACKGROUND = ROOT / "assets/dropbox-workforce-background-2026-10-28.png"
COIN = ROOT / "assets/moneyberg-coin-original.png"
LATO = ROOT / "assets/fonts/lato/Lato-Black.ttf"
OUTPUT = ROOT / "exports/dropbox-workforce-cuts-2026-10-28.png"
AUDIT = ROOT / "briefs/dropbox-workforce-cuts-2026-10-28-layout.json"
COIN_HASH = "4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716"
INNER = (104, 164, 961, 1536)
GENERATION_PROMPTS = ['Create a sophisticated text-free editorial photographic background for a vertical 9:16 Instagram news story about Dropbox planning to cut about9% of its workforce. This is an illustrative generic modern software office, not a documentary photograph of Dropbox. Art direction: quiet editorial workplace scene, soft porcelain/off-white, matte Dropbox-like cobalt-blue architectural accents, slate steel, restrained desaturated gray. Camera faces a broad flat off-white plaster partition wall in an elegant contemporary office; diffuse cool daylight from the left, subtle realistic texture. Most of the image is calm light-toned negative space for large dark typography: at final1080x1920 coordinates x104–961,y164–1536, especially x104–820,y164–1536, keep background almost uniform warm-white and highly legible. In the far-right strip x835–1080,y790–1400, place a straight-on front-facing matte cobalt-blue vertical architectural cabinet/panel with a small circular EMPTY recessed brass mounting seat centered near x939,y995, diameter160px. It is an inset IN THE PANEL, not a detached floating badge. Dark plain flat center with subtle brass edge light and contact shadow, no coin/portrait/logo generated. We will place an original circular gold Moneyberg coin directly in that recess later, uniformly scaled, wholly above y1440 and unobstructed. Lower fifth of picture y1540–1920 reveals soft-focus empty office workstations, neat task chairs, slim monitorbacks, pale desk surfaces and faint cobalt-blue divider panels, suggesting corporate reorganization calmly. Keep recognizable workstations confined to bottom and side; no actual corporate signage. Elegant depth and editorial magazine-quality lighting, gentle geometry. No people, no dramatic collapse, no boxes or personal belongings, no fake chart. Do NOT add words, letters, numbers, logos, generated medallions, portraits, seals, headline, watermark, border or any text. Final typesetting will be added separately in actual Lato Black900 for headline/date/category/numbers and small one-line32px MONEYBERG NEWS BRIEF, and Georgia for body/sources; ALL authored text>=30px at1080x1920, body>=32headline>=48; allnewsinside x104–961,y164–1536. Render background only. Composition should feel specific to a cloud software workplace and sober employment news, not finance trading screens.']
GENERATION_PROMPTS.append('Edit this background very conservatively. Preserve the exact composition, dimensions9:16, off-white plaster wall, left windows, cobalt-blue right cabinet, circular EMPTY brass mounting recess, and its position/size exactly. Preserve the photorealistic office lighting and bottom desks/chairs. Only simplify and clear the lower-left reading zone: at final1080x1920coordinates x90–840,y1230–1550, remove the plant and lower any monitor/chair/desk silhouettes to start only below y1580, filling the cleared space seamlessly with matching off-white plaster texture. We need perfectly legible dark source and body typography at x120,y1290–1520. Do not create a rectangle overlay or edit the upper scene. Keep furniture prominent and beautiful in bottom y1590–1920. Coin mounting seat stays exactly in current position at approximatelyx987,y1012, smallcircle. Do NOT generate any lettering, words, numbers, logos, seals, coins or portraits. Final typesetting is separately actualLatoBlack900/Georgia,minimum30px alltext,headline>=48,body>=32;compactone-lineMONEYBERG NEWS BRIEF and newsinside x104–961,y164–1536;originalMoneybergcoinwillbeplacedexactlyinthepanelrecessupper75%. Background readability edit only.')
INTEGRATION = {'method': 'Exact original coin PNG seated within the blue office panel brass recess, with contact shadow, edge shading and compatible cool illumination', 'artwork': 'Original PNG uniformly scaled; portrait, lettering and circular proportions preserved', 'image_generation_role': 'Text-free illustrative office background only; no generated coin, company mark or news text', 'generated_source': '/workspace/generated_images/exec-9ae34474-accf-4dea-ab98-e6c16e649199.png', 'category': 'JOBS & EMPLOYMENT', 'background_credit_on_graphic': False, 'background_provenance': 'Generated decorative generic software office, not a documentary photograph of Dropbox premises'}


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
    """Serve only the four intended assets and ephemeral document on loopback."""
    template = TEMPLATE.read_text(encoding="utf-8")
    if "__GEORGIA_FONT_URI__" not in template or "__ASSET_BASE_URI__" not in template:
        raise ValueError("The committed template must retain its runtime placeholders")
    with tempfile.TemporaryDirectory(prefix="moneyberg-dropbox-", dir="/tmp") as temp:
        runtime_html = Path(temp) / "dropbox-runtime.html"
        files = {
            "/runtime.html": (runtime_html, "text/html; charset=utf-8"),
            "/georgia-runtime.ttf": (georgia, "font/ttf"),
            "/assets/fonts/lato/Lato-Black.ttf": (LATO, "font/ttf"),
            "/assets/dropbox-workforce-background-2026-10-28.png": (BACKGROUND, "image/png"),
            "/assets/moneyberg-coin-original.png": (COIN, "image/png"),
            "/assets/logos/dropbox-mark-original.svg": (ROOT / "assets/logos/dropbox-mark-original.svg", "image/svg+xml"),
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
                const scene_elements = Array.from(document.querySelectorAll('[data-scene-element]')).map(element => {
                  const css=getComputedStyle(element);
                  return {id:element.id, bounds:rect(element.getBoundingClientRect()), box_shadow:css.boxShadow, background:css.backgroundImage};
                });
                return {text, panels, scene_elements, fonts:Array.from(document.fonts).map(face =>
                  ({family:face.family, weight:face.weight, status:face.status})),
                  images:Array.from(document.images).map(image => ({id:image.id,
                    natural_width:image.naturalWidth, natural_height:image.naturalHeight,
                    bounds:rect(image.getBoundingClientRect())})),
                  document_width:document.documentElement.scrollWidth,
                  document_height:document.documentElement.scrollHeight};
            }""")

            coin = next(image for image in layout["images"] if image["id"] == "coin")
            coin_bounds = coin["bounds"]
            if (coin["natural_width"], coin["natural_height"]) != (2084, 2084):
                raise ValueError("The browser did not load the full original coin PNG")
            if (coin_bounds["top"] < 0 or coin_bounds["bottom"] > 0.75 * 1920
                    or abs(coin_bounds["width"] - coin_bounds["height"]) > 0.01):
                raise ValueError(f"Original coin violates whole-coin upper-75% or aspect rule: {coin_bounds}")
            for entry in layout["text"]:
                box=entry["bounds"]
                if (box["left"] < coin_bounds["right"] and box["right"] > coin_bounds["left"]
                        and box["top"] < coin_bounds["bottom"] and box["bottom"] > coin_bounds["top"]):
                    raise ValueError(f"Coin overlaps text: {entry['id']}")
            scene={entry["id"]:entry for entry in layout["scene_elements"]}
            if scene["coin-installation"]["box_shadow"] == "none" or scene["coin-contact"]["box_shadow"] == "none":
                raise ValueError("Scene integration is missing recess/contact shading")
            if any("Background:" in item["text"] for item in layout["text"]):
                raise ValueError("An unwanted background-production credit remains")
            if not any("JOBS & EMPLOYMENT" in item["text"] for item in layout["text"]):
                raise ValueError("The required employment category is missing")

            for entry in layout["text"]:
                size = float(entry["font_size"].removesuffix("px"))
                if size < 30:
                    raise ValueError(f"Authored text falls below the new 30 px minimum: {entry['id']} ({size}px)")
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
             "minimum_authored_font_size_px": 30, "font_size_minimum_verified": True,
             "renderer": "Chromium via Playwright; HTML/CSS screenshot",
             "background_sha256": sha256(BACKGROUND), "original_coin_sha256": sha256(COIN),
             "lato_black_sha256": sha256(LATO), "georgia_runtime_sha256": sha256(georgia),
             "georgia_redistributed": False, "layout": layout, "platform_fonts": platform_fonts,
             "coin_bounds": coin_bounds, "whole_coin_upper_75_percent_verified": True,
             "integration": INTEGRATION, "generation_prompts": GENERATION_PROMPTS,
             "source": "https://www.sec.gov/Archives/edgar/data/1467623/000146762326000052/dbx-20261028.htm",
             "official_dropbox_logo_sha256": sha256(ROOT / "assets/logos/dropbox-mark-original.svg"),
             "output_sha256": sha256(OUTPUT)}
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(f"Rendered {OUTPUT.relative_to(ROOT)} at 1080 × 1920")
    print(f"Verified {len(layout['text'])} text elements, {len(layout['panels'])} panels, and actual browser fonts.")
    print("Original coin verified in office-panel recess; Georgia runtime-only; Python does not edit image pixels.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--georgia-font", type=Path, required=True)
    parser.add_argument("--background-source", type=Path)
    args = parser.parse_args()
    asyncio.run(render(args.georgia_font, args.background_source))
