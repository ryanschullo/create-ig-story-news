#!/usr/bin/env python3
"""Render the November 10 oil/Iran restraint story with same-snapshot Brent and WTI futures, actual fonts and original coin.

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
TEMPLATE = ROOT / "assets/layouts/oil-iran-pause-2026-11-10.html"
BACKGROUND = ROOT / "assets/oil-iran-pause-background-2026-11-10.png"
COIN = ROOT / "assets/moneyberg-coin-original.png"
LATO = ROOT / "assets/fonts/lato/Lato-Black.ttf"
OUTPUT = ROOT / "exports/oil-iran-pause-2026-11-10.png"
AUDIT = ROOT / "briefs/oil-iran-pause-2026-11-10-layout.json"
COIN_HASH = "4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716"
INNER = (104, 164, 961, 1536)
PROMPT_DOCUMENT = (ROOT / "assets/oil-iran-pause-background-2026-11-10.md").read_text()
GENERATION_PROMPTS = re.findall(r"```text\n(.*?)\n```", PROMPT_DOCUMENT, flags=re.DOTALL)
if not GENERATION_PROMPTS:
    GENERATION_PROMPTS = re.findall(r"## Generation prompt\n\n(.*?)(?=\n## |\Z)", PROMPT_DOCUMENT, flags=re.DOTALL)
if not GENERATION_PROMPTS or any(not prompt.strip() or prompt.strip().lower() in {"undefined", "null"} for prompt in GENERATION_PROMPTS):
    raise ValueError("All original generation and editing prompts are required")
INTEGRATION = {
    "method": "Exact original coin PNG seated inside an industrial brass recess on refinery equipment, with compatible amber light and contact shadow",
    "artwork": "Original uniformly scaled PNG; original portrait, lettering and circular rim preserved",
    "image_generation_role": "Text-free conceptual petroleum refinery, tanker and pipeline setting only",
    "topic": "Oil eases after Trump's stated restraint toward Iran; same-snapshot Brent and WTI futures with continuing Hormuz blockade context",
    "category_badge": "OIL & GAS",
    "background_credit_on_graphic": False,
    "background_provenance": "Conceptual petroleum infrastructure, not documentary evidence of an event or a quantitative market chart",
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
    with tempfile.TemporaryDirectory(prefix="moneyberg-oil-iran-pause-", dir="/tmp") as temp:
        runtime_html = Path(temp) / "oil-iran-pause-runtime.html"
        files = {
            "/runtime.html": (runtime_html, "text/html; charset=utf-8"),
            "/georgia-runtime.ttf": (georgia, "font/ttf"),
            "/assets/fonts/lato/Lato-Black.ttf": (LATO, "font/ttf"),
            "/assets/oil-iran-pause-background-2026-11-10.png": (BACKGROUND, "image/png"),
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
                return {text, panels, scene_elements, fonts:Array.from(document.fonts).map(face =>
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
                "brand": "MONEYBERG NEWS BRIEF", "category": "OIL & GAS",
                "date": "NOVEMBER 10, 2026",
                "headline-one": "OIL EASES AS",
                "headline-two": "TRUMP SIGNALS",
                "headline-three": "RESTRAINT",
                "quote-one": "Trump says military action against Iran",
                "quote-two": "is not necessary “at this point.”",
                "benchmark-scope": "CRUDE FUTURES • USD / BARREL",
                "brent-label": "BRENT", "brent-price": "$92.33",
                "brent-change": "−$0.24 / barrel",
                "wti-label": "WTI", "wti-price": "$86.50",
                "wti-change": "−$0.35 / barrel",
                "snapshot": "INTRADAY • NOV. 10, 01:02 GMT",
                "caveat-one": "The Strait of Hormuz naval",
                "caveat-two": "blockade remains in place.",
                "source": "Source: Reuters via Euronext",
            }
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
             "sources": [
                 "https://live.euronext.com/en/financial-news/oil-falls-trump-downplays-prospect-escalation-iran",
             ],
             "source_access": "Read the full Reuters report by Noel John republished by Euronext. Both futures prices and their dollar changes occur in the same sentence with the same explicit 01:02 GMT observation time. Refreshed article body matches the earlier retrieved report. Direct Reuters full-text access is not claimed.",
             "reporting_scope": {
                 "production_date": "2026-11-10",
                 "edition_date": "2026-11-10",
                 "edition_date_basis": "Reuters November 10 dateline and GMT market snapshot",
                 "source_published_utc": "2026-11-10T01:43:22Z",
                 "source_published_chicago": "2026-11-09T19:43:22-06:00",
                 "source_visible_site_clock": "Tue 10/11/2026 - 02:43; not treated as UTC or Chicago time",
                 "source_byline": "Noel John, Reuters",
                 "snapshot_label": "INTRADAY • NOV. 10, 01:02 GMT",
                 "snapshot_utc_minute_precision": "2026-11-10T01:02Z",
                 "snapshot_chicago_minute_precision": "2026-11-09T19:02-06:00",
                 "same_observation_time_for_both_benchmarks": True,
                 "not_final_settlements": True,
                 "source_publication_time_not_substituted_for_observation_time": True,
                 "currency": "USD", "unit": "per barrel",
                 "benchmarks": [
                     {"name": "Brent", "instrument": "crude oil futures", "price": 92.33, "daily_dollar_change": -0.24, "contract_month": None, "snapshot_utc": "2026-11-10T01:02Z"},
                     {"name": "WTI", "instrument": "crude oil futures", "price": 86.50, "daily_dollar_change": -0.35, "contract_month": None, "snapshot_utc": "2026-11-10T01:02Z"},
                 ],
                 "both_required_oil_benchmarks_displayed": True,
                 "contract_months_not_supplied_by_source_and_not_invented": True,
                 "percentage_changes_displayed": False,
                 "percentage_omission_reason": "The source Brent percentage does not reconcile with its reported price and dollar move. Both percentages are omitted consistently; no replacement percentage is calculated or shown.",
                 "trump_statement_is_attributed_and_temporary": True,
                 "temporary_qualifier_retained": "at this point",
                 "continuing_hormuz_naval_blockade_caveat_retained": True,
                 "no_ceasefire_peace_agreement_or_reopening_claim": True,
                 "no_chart_or_investment_advice": True,
                 "no_invented_market_signals": True,
             },
             "output_sha256": sha256(OUTPUT)}
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(f"Rendered {OUTPUT.relative_to(ROOT)} at 1080 × 1920")
    print(f"Verified {len(layout['text'])} text elements, {len(layout['panels'])} panels, and actual browser fonts.")
    print("Original coin, both oil benchmarks and common intraday timestamp verified; Georgia runtime-only; Python does not edit image pixels.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--georgia-font", type=Path, required=True)
    parser.add_argument("--background-source", type=Path)
    args = parser.parse_args()
    asyncio.run(render(args.georgia_font, args.background_source))
