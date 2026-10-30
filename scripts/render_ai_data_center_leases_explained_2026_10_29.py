#!/usr/bin/env python3
"""Render the AI data-center leases Story using actual fonts and original coin in a server cabinet.

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
TEMPLATE = ROOT / "assets/layouts/ai-data-center-leases-explained-2026-10-29.html"
BACKGROUND = ROOT / "assets/ai-data-center-leases-explained-background-2026-10-29.png"
COIN = ROOT / "assets/moneyberg-coin-original.png"
LATO = ROOT / "assets/fonts/lato/Lato-Black.ttf"
OUTPUT = ROOT / "exports/ai-data-center-leases-explained-2026-10-29.png"
AUDIT = ROOT / "briefs/ai-data-center-leases-explained-2026-10-29-layout.json"
COIN_HASH = "4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716"
INNER = (104, 164, 961, 1536)
GENERATION_PROMPTS = ["Create a premium text-free 9:16 vertical editorial background for a financial news Story about Wall Street investing in AI data-center buildings and collecting long-term rent. Final composition at1080x1920. Refined architectural photography: charcoal graphite, deep steel blue, subtle cyan light, cold industrial metal and a little restrained brass. View within a quiet high-end hyperscale data-center facility. The entire upper and center LEFT of the frame (x90..850,y140..1530) is a broad front-facing almost-uniform dark graphite/ink technical wall with beautiful very subtle brushed texture, spacious negative space for large ivory typography. Keep this reading area extremely dark, plain and uncluttered all the way through y1530. Along the far-right margin only, a flat front-facing steel-blue server-cabinet architectural panel runs from y780 to y1450. Into this actual cabinet panel, create one perfectly circular EMPTY brass-lined shallow mounting recess centered around x980,y1140 with diameter150px. The center is plain dark metal, no face, emblem, logo or coin artwork. The seat is physically embedded in the cabinet with realistic edge and contact shadows, facing straight on so circular proportions remain true. We will place the user's exact original Moneyberg coin directly in this recess afterward, with its whole rim above y1440, no generated substitute. At the bottom below y1550, beautiful rows of black server racks recede into depth with subtle cyan status lights and floor reflections, suggesting tangible infrastructure and energy demand rather than an abstract AI brain. Some rack edges can appear at the far right outside the news area. No people, no readable signage, no invented charts, no artificial network symbols. Do not add text, letters, numbers, words, logos, badges, portraits, watermark, borders or coins. The finished design separately uses actual Lato Black900 for the headline, data, date, category ENERGY & INFRASTRUCTURE, and the compact single-line35px MONEYBERG NEWS BRIEF; Georgia for body and sources. Authored minimums are33px alltext,35pxbody,51pxheadlines. All added news content will stay within x104..961,y164..1536. Render ONLY the photographic background, not the final news graphic.", "Edit the supplied text-free data-center background for an updated vertical 9:16 financial news graphic, final canvas1080x1920. Preserve its sophisticated graphite, steel-blue and subtle cyan palette, front-facing plain dark metal wall on the left, server cabinet on the far right and photographic server aisle below. Make ONLY these composition refinements to accommodate an additional readable explanation: extend the uninterrupted plain dark left reading wall lower, so it continues all the way through y1550 at final1080x1920 coordinates, then the receding server aisle begins below y1565 and continues to bottom1920. Keep left reading area x104–800,y164–1536 dark, even, uncluttered, no seam across that area, no distracting reflections. Keep the tall server cabinet at the far right, and keep its existing empty brass circular mounting recess, front-facing and circular, approximately x820–1035,y800–1015 in finalpixels. No coin or emblem in this empty seat; we will install the user's exact original Moneyberg coin separately so portrait and lettering are unchanged. Its full rim must be above y1440. High-quality realistic metal with original subtle lighting. The final typography will be added separately in actual Lato Black900 for headline>=51px, labels>=33px, compact one-line35px MONEYBERG NEWS BRIEF; Georgia for body>=35px, sources>=33px. Allnewscontentinside x104–961,y164–1536. New added text later will say: Wall Street’s top alternative asset managers are betting on the AI boom by owning the infrastructure behind it and locking in rent through long-term leases. Do NOT render those words or any text; output text-free background only. No letters, numbers, logo, charts or coin artwork. Only extend the plain architecture for more readable copy, retaining the photographic style of reference."]
INTEGRATION = {'method': 'Original coin seated in the front-facing server cabinet brass-lined recess with contact shading and cool illumination', 'artwork': 'Exact original PNG with uniform scale, portrait and lettering preserved', 'image_generation_role': 'Edited text-free data-center architecture to extend the plain reading wall; no generated coin or news text', 'generated_source': '/workspace/generated_images/exec-18965db3-a935-4c81-8fa7-2a6ddce85d5f.png', 'reference_background': 'assets/ai-data-center-leases-background-2026-10-29.png', 'category': 'ENERGY & INFRASTRUCTURE', 'background_credit_on_graphic': False, 'background_provenance': 'Generated generic data-center environment, not a documentary photograph of a particular manager portfolio', 'revision': 'Add user-provided Reuters opening sentence verbatim ahead of lease terms'}


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
    with tempfile.TemporaryDirectory(prefix="moneyberg-infra-explained-", dir="/tmp") as temp:
        runtime_html = Path(temp) / "infra-leases-runtime.html"
        files = {
            "/runtime.html": (runtime_html, "text/html; charset=utf-8"),
            "/georgia-runtime.ttf": (georgia, "font/ttf"),
            "/assets/fonts/lato/Lato-Black.ttf": (LATO, "font/ttf"),
            "/assets/ai-data-center-leases-explained-background-2026-10-29.png": (BACKGROUND, "image/png"),
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
                    font_family:css.fontFamily, font_weight:css.fontWeight, font_size:css.fontSize, role:element.dataset.role || "label"};
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
            if not any("ENERGY & INFRASTRUCTURE" in item["text"] for item in layout["text"]):
                raise ValueError("The required infrastructure category is missing")

            for entry in layout["text"]:
                size = float(entry["font_size"].removesuffix("px"))
                minimum = {"headline":51,"body":35}.get(entry["role"],33)
                if size < minimum:
                    raise ValueError(f"Authored text falls below the current {minimum} px role minimum: {entry['id']} ({size}px)")
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
             "minimum_authored_font_size_px": 33, "minimum_body_font_size_px":35, "minimum_headline_font_size_px":51, "font_size_minimum_verified": True,
             "renderer": "Chromium via Playwright; HTML/CSS screenshot",
             "background_sha256": sha256(BACKGROUND), "original_coin_sha256": sha256(COIN),
             "lato_black_sha256": sha256(LATO), "georgia_runtime_sha256": sha256(georgia),
             "georgia_redistributed": False, "layout": layout, "platform_fonts": platform_fonts,
             "coin_bounds": coin_bounds, "whole_coin_upper_75_percent_verified": True,
             "integration": INTEGRATION, "generation_prompts": GENERATION_PROMPTS,
             "source": "https://d2233.cms.socastsrm.com/2026/10/29/wall-streets-ai-bet-own-the-infrastructure-collect-the-rent/",
             "output_sha256": sha256(OUTPUT)}
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(f"Rendered {OUTPUT.relative_to(ROOT)} at 1080 × 1920")
    print(f"Verified {len(layout['text'])} text elements, {len(layout['panels'])} panels, and actual browser fonts.")
    print("Original coin verified in server-cabinet recess; Georgia runtime-only; Python does not edit image pixels.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--georgia-font", type=Path, required=True)
    parser.add_argument("--background-source", type=Path)
    args = parser.parse_args()
    asyncio.run(render(args.georgia_font, args.background_source))
