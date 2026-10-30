#!/usr/bin/env python3
"""Render the Alphabet stock Story with actual fonts, official Google wordmark and original Moneyberg coin.

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
TEMPLATE = ROOT / "assets/layouts/alphabet-stock-2026-10-29.html"
BACKGROUND = ROOT / "assets/alphabet-stock-background-2026-10-29.png"
COIN = ROOT / "assets/moneyberg-coin-original.png"
GOOGLE_LOGO = ROOT / "assets/logos/google-wordmark-original.png"
GOOGLE_LOGO_HASH = "262084257c2103702ef8a25705e3f8dbc1fa3823103ad7b954d54bdb77e6d89d"
LATO = ROOT / "assets/fonts/lato/Lato-Black.ttf"
OUTPUT = ROOT / "exports/alphabet-stock-2026-10-29.png"
AUDIT = ROOT / "briefs/alphabet-stock-2026-10-29-layout.json"
COIN_HASH = "4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716"
INNER = (104, 164, 961, 1536)
GENERATION_PROMPTS = ["Create a premium text-free photographic editorial background for a vertical9:16 Instagram financial news Story, final composition1080x1920, about Google parent Alphabet stock falling as investors scrutinize AI capital spending. Distinct clean bright Google-era technology aesthetic: warm porcelain white, very pale cool gray, glass, brushed silver, fine blue details and restrained small reflections of Google blue/red/yellow/green; no logos, words or letterforms. The upper80% and left82% of frame is a beautiful front-facing matte off-white technical wall with extremely subtle material texture and clear airy daylight. Precisely x104–820,y164–1536 remains plain, evenly light and unobstructed for large dark readable typesetting and Google's actual official wordmark later. No strong diagonals, patterns or shadows in that area. At far right x885–1080 an elegant flat white/silver equipment cabinet column, front facing, runs fromy800to1500. It has one perfectly circular EMPTY shallow brass-lined mounting recess centered x969,y1085 diameter180px, circle straight-on, realistic recessed edge and contact shadow, physically part of cabinet. We will install the user's actual original Moneyberg gold coin into this seat, preserving its exact portrait and lettering; DO NOT generate any coin, portrait, letters or substitute logo. Whole eventualcoinabove y1440. Below y1570, an attractive minimal photorealistic cloud-computing/AI hardware scene: neat white server racks, clear glass foreground corner, polished aluminum structures, softly glowing tiny blue indicatorlights, delicate multicolor light reflections on clean surfaces. Show material depth and a sophisticated quiet technology campus interior, no evidence of actual Google facilities. Keep all busy hardware below the news region. No red stock chart or invented numbers, no damage, no people. Final typesetting later uses real Lato Black900 for headline>=51px, labels>=33px and compactone-line35px MONEYBERG NEWS BRIEF, category AI INVESTING; actual Georgia forbody>=35px/source>=33px. Newsallinside x104–961,y164–1536. Output only text-free architectural background; no text, watermarks, logos or coinartwork.", 'Edit this background only. Extend the huge unbroken white left wall DOWN to occupy the upper82percent of the entire image; this is essential. On final1080x1920 the bottom of that plain wall must be a HORIZONTAL edge at y1570, NOT its current height near y1250. Leave the white left reading area x104–820,y164–1536 completely plain, evenly lit and unobstructed, all the way to y1536. Push/compress the entire busy server room/railing/floor scene into only the bottom18percent, y1570–1920. Do not leave hardware, ledges, shadows or reflections in the reading area. Preserve beautiful porcelainwhite/steel/paleblue aesthetic and tall equipment columnatfarright, includingexistingemptybrasscircularmountatx~950,y~840; no emblem coin or logo. No added text. The final actual Google wordmark and Moneyberg original coin will be added separately, actual Lato Black900 headline>=51px/label>=33px/compact35px single-line MONEYBERG NEWS BRIEF and Georgia body>=35px/source>=33px; allnewsx104–961,y164–1536. Output text-free scene only. Critical specific edit: plain wall extends through82%height, serverroom onlylowest18%, the small brassmountstaysupper75%.']
INTEGRATION = {'method': 'Exact original coin PNG seated in the generated white equipment cabinet brass recess, with contact shadows and light compatible with the surroundings', 'artwork': 'Original uniformly scaled PNG; portrait and rim lettering preserved, not redrawn', 'image_generation_role': 'Text-free bright generic technology/data-center architecture', 'initial_generated_source': '/workspace/generated_images/exec-c385d08c-3f80-472d-b1bf-5578ceeebce8.png', 'generated_source': '/workspace/generated_images/exec-1cb0dc80-8d94-4bea-9d72-fd109ccedb42.png', 'category': 'AI INVESTING', 'background_credit_on_graphic': False, 'background_provenance': 'Generic illustrative technology interior, not a documentary image of Google facilities', 'google_logo_source': 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'}


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
    with tempfile.TemporaryDirectory(prefix="moneyberg-alphabet-", dir="/tmp") as temp:
        runtime_html = Path(temp) / "alphabet-runtime.html"
        files = {
            "/runtime.html": (runtime_html, "text/html; charset=utf-8"),
            "/georgia-runtime.ttf": (georgia, "font/ttf"),
            "/assets/fonts/lato/Lato-Black.ttf": (LATO, "font/ttf"),
            "/assets/alphabet-stock-background-2026-10-29.png": (BACKGROUND, "image/png"),
            "/assets/moneyberg-coin-original.png": (COIN, "image/png"),
            "/assets/logos/google-wordmark-original.png": (GOOGLE_LOGO, "image/png"),
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
    if sha256(GOOGLE_LOGO) != GOOGLE_LOGO_HASH:
        raise ValueError("The official Google logo has changed")
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
                return {text, panels, scene_elements, fonts:Array.from(document.fonts).map(face =>
                  ({family:face.family, weight:face.weight, status:face.status})),
                  images:Array.from(document.images).map(image => ({id:image.id,
                    natural_width:image.naturalWidth, natural_height:image.naturalHeight,
                    bounds:rect(image.getBoundingClientRect())})),
                  document_width:document.documentElement.scrollWidth,
                  document_height:document.documentElement.scrollHeight};
            }""")

            google_logo = next(image for image in layout["images"] if image["id"] == "google-logo")
            if (google_logo["natural_width"], google_logo["natural_height"]) != (544, 184):
                raise ValueError("The official Google wordmark dimensions do not match")
            logo_box = google_logo["bounds"]
            if abs(logo_box["width"] / logo_box["height"] - 544 / 184) > 0.001:
                raise ValueError("Google logo is distorted")

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
            if not any(item["text"] == "AI INVESTING" for item in layout["text"]):
                raise ValueError("The AI INVESTING category is missing")

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
             "official_google_logo_sha256":sha256(GOOGLE_LOGO), "google_logo_bounds":logo_box,
             "lato_black_sha256": sha256(LATO), "georgia_runtime_sha256": sha256(georgia),
             "georgia_redistributed": False, "layout": layout, "platform_fonts": platform_fonts,
             "coin_bounds": coin_bounds, "whole_coin_upper_75_percent_verified": True,
             "integration": INTEGRATION, "generation_prompts": GENERATION_PROMPTS,
             "source": "https://www.cnn.com/2026/10/29/investing/alphabet-google-stock-ai",
             "output_sha256": sha256(OUTPUT)}
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(f"Rendered {OUTPUT.relative_to(ROOT)} at 1080 × 1920")
    print(f"Verified {len(layout['text'])} text elements, {len(layout['panels'])} panels, and actual browser fonts.")
    print("Original coin verified in white equipment cabinet recess; official Google logo intact; Georgia runtime-only; Python does not edit image pixels.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--georgia-font", type=Path, required=True)
    parser.add_argument("--background-source", type=Path)
    args = parser.parse_args()
    asyncio.run(render(args.georgia_font, args.background_source))
