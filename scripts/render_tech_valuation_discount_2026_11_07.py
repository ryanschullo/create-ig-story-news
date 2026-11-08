#!/usr/bin/env python3
"""Render the November 7 technology-valuation discount news brief with complete original chart, actual fonts and original coin.

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
TEMPLATE = ROOT / "assets/layouts/tech-valuation-discount-2026-11-07.html"
BACKGROUND = ROOT / "assets/tech-valuation-discount-background-2026-11-07.png"
COIN = ROOT / "assets/moneyberg-coin-original.png"
CHART = ROOT / "assets/tech-valuation-discount-chart-original-2026-11-07.png"
CHART_HASH = "977456f33d678de498d3908cc327eba520ea6cc1a0ff58006eb83f63d9875315"
LATO = ROOT / "assets/fonts/lato/Lato-Black.ttf"
OUTPUT = ROOT / "exports/tech-valuation-discount-2026-11-07.png"
AUDIT = ROOT / "briefs/tech-valuation-discount-2026-11-07-layout.json"
COIN_HASH = "4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716"
INNER = (104, 164, 961, 1536)
GENERATION_PROMPTS = re.findall(r"```text\n(.*?)\n```", (ROOT / "assets/tech-valuation-discount-background-2026-11-07.md").read_text(), flags=re.DOTALL)
if not GENERATION_PROMPTS or any(not prompt.strip() or prompt.strip().lower() in {"undefined", "null"} for prompt in GENERATION_PROMPTS):
    raise ValueError("All original generation and editing prompts are required")
INTEGRATION = {
    "method": "Exact original coin PNG seated in a physical brass recess in a nickel column, with compatible lighting and contact shadow",
    "artwork": "Original uniformly scaled PNG; original portrait, lettering and circular rim preserved",
    "image_generation_role": "Text-free conceptual semiconductor and technology-corporate environment only",
    "topic": "S&P 500 technology-sector expected-earnings valuation relative to the broader index, with a separate historical losing-streak return study",
    "category_badge": "STOCK MARKET",
    "background_credit_on_graphic": False,
    "background_provenance": "Conceptual semiconductor environment; not documentary evidence or quantitative chart data",
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
    with tempfile.TemporaryDirectory(prefix="moneyberg-tech-valuation-", dir="/tmp") as temp:
        runtime_html = Path(temp) / "tech-valuation-runtime.html"
        files = {
            "/runtime.html": (runtime_html, "text/html; charset=utf-8"),
            "/georgia-runtime.ttf": (georgia, "font/ttf"),
            "/assets/fonts/lato/Lato-Black.ttf": (LATO, "font/ttf"),
            "/assets/tech-valuation-discount-background-2026-11-07.png": (BACKGROUND, "image/png"),
            "/assets/moneyberg-coin-original.png": (COIN, "image/png"),
            "/assets/tech-valuation-discount-chart-original-2026-11-07.png": (CHART, "image/png"),
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
    if sha256(CHART) != CHART_HASH:
        raise ValueError("The complete original source chart has changed")
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

            chart = next(image for image in layout["images"] if image["id"] == "chart")
            chart_bounds = chart["bounds"]
            if (chart["natural_width"], chart["natural_height"]) != (2400, 1350):
                raise ValueError("The full original chart did not load")
            if chart["object_fit"] != "contain" or chart["clip_path"] != "none":
                raise ValueError("Original chart may be cropped")
            if abs(chart_bounds["width"] / chart_bounds["height"] - 2400 / 1350) > .0001:
                raise ValueError("Original chart aspect ratio is distorted")
            for entry in layout["text"]:
                box=entry["bounds"]
                if (box["left"] < chart_bounds["right"] and box["right"] > chart_bounds["left"]
                        and box["top"] < chart_bounds["bottom"] and box["bottom"] > chart_bounds["top"]):
                    raise ValueError(f"Authored text overlaps original chart: {entry['id']}")

            coin = next(image for image in layout["images"] if image["id"] == "coin")
            coin_bounds = coin["bounds"]
            if (coin["natural_width"], coin["natural_height"]) != (2084, 2084):
                raise ValueError("The browser did not load the full original coin PNG")
            if (coin_bounds["top"] < 0 or coin_bounds["bottom"] > 0.75 * 1920
                    or abs(coin_bounds["width"] - coin_bounds["height"]) > 0.01):
                raise ValueError(f"Original coin violates whole-coin upper-75% or aspect rule: {coin_bounds}")
            if (coin_bounds["left"] < chart_bounds["right"] and coin_bounds["right"] > chart_bounds["left"]
                    and coin_bounds["top"] < chart_bounds["bottom"] and coin_bounds["bottom"] > chart_bounds["top"]):
                raise ValueError("Coin overlaps the original source screenshot")
            for entry in layout["text"]:
                box=entry["bounds"]
                if (box["left"] < coin_bounds["right"] and box["right"] > coin_bounds["left"]
                        and box["top"] < coin_bounds["bottom"] and box["bottom"] > coin_bounds["top"]):
                    raise ValueError(f"Coin overlaps text: {entry['id']}")
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
                "category": "STOCK MARKET",
                "date": "NOVEMBER 7, 2026",
                "headline-one": "TECH TRADES AT",
                "headline-two": "A RARE DISCOUNT",
                "context": "Expected earnings • Truist, Nov. 5 note",
                "tech-label": "S&P 500 TECH",
                "market-label": "S&P 500",
                "tech-value": "~17×",
                "market-value": "~18×",
                "discount": "First discount to the S&P 500 since 2017.",
                "chart-heading": "S&P 500 AFTER 4+ LOSING WEEKS",
                "study": "Historical study: 33 streaks since 1990.",
                "exceptions": "Dot-com bust and 2008 were exceptions.",
                "source": "Yahoo Finance • November 7, 2026",
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
             "sources": ["https://finance.yahoo.com/markets/article/tech-stocks-are-now-cheaper-than-the-sp-500-for-the-first-time-since-2017--heres-what-history-says-comes-next-chart-of-the-day-130131812.html"],
             "source_access": "Full Yahoo Finance article by Jared Blikre and its unmodified original chart. Article reports approximate S&P 500 technology-sector expected-earnings multiples from Keith Lerner's November 5 Truist note. Historical S&P 500 return figures are a separate Yahoo Finance study of losing streaks, not a study of technology valuation discounts.",
             "original_chart": {
                 "sha256": sha256(CHART),
                 "dimensions": [2400, 1350],
                 "rendered_bounds": chart_bounds,
                 "complete_image_preserved": True,
                 "retyped_or_redrawn": False,
                 "embedded_fonts_preserved": True,
                 "title": "After 4 straight losing weeks, the S&P 500 has usually done better than normal",
                 "subtitle": "Median S&P 500 return, since 1990",
                 "units": "Median subsequent S&P 500 return, percent",
                 "source_credit": "Yahoo Finance calculations. 33 streaks of four or more weekly losses since 1990.",
                 "historical_study_of_losing_streaks_not_valuation_discounts": True,
                 "median_returns_percent": {
                     "after_4_or_more_losing_weeks": {"1_month": 1.9, "3_months": 6.0, "6_months": 10.3, "1_year": 16.5},
                     "after_any_week": {"1_month": 1.2, "3_months": 3.2, "6_months": 5.7, "1_year": 11.9},
                 },
                 "sample_size": 33,
                 "sample_start_year": 1990,
                 "exceptions_disclosed": ["dot-com bust", "2008 financial crisis"],
                 "historical_returns_not_a_forecast": True,
             },
             "valuation_snapshot": {
                 "kind": "Reported approximate expected-earnings valuation comparison",
                 "article_published_utc": "2026-11-07T13:01:31Z",
                 "article_published_chicago": "2026-11-07T07:01:31-06:00",
                 "attributed_research_note_date": "2026-11-05",
                 "source_analyst": "Keith Lerner, Truist Wealth",
                 "technology_scope": "S&P 500 information-technology sector; article references XLK",
                 "technology_expected_earnings_multiple_approximate": 17,
                 "broader_sp500_expected_earnings_multiple_approximate": 18,
                 "first_relative_discount_since_year": 2017,
                 "not_all_technology_stocks_or_nasdaq": True,
                 "not_assigned_an_unverified_closing_timestamp": True,
                 "not_a_daily_market_wrap": True,
                 "chart_is_a_separate_historical_study": True,
                 "no_inference_that_valuation_discount_predicts_chart_returns": True,
             },
             "output_sha256": sha256(OUTPUT)}
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(f"Rendered {OUTPUT.relative_to(ROOT)} at 1080 × 1920")
    print(f"Verified {len(layout['text'])} text elements, {len(layout['panels'])} panels, and actual browser fonts.")
    print("Full original chart and original coin verified; Georgia runtime-only; Python does not edit image pixels.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--georgia-font", type=Path, required=True)
    parser.add_argument("--background-source", type=Path)
    args = parser.parse_args()
    asyncio.run(render(args.georgia_font, args.background_source))
