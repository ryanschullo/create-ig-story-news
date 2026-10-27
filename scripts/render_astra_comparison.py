#!/usr/bin/env python3
"""Lay out unchanged Story exports in a before/after browser contact sheet."""

import asyncio
import hashlib
import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

from playwright.async_api import async_playwright


ROOT = Path(__file__).resolve().parents[1]
STORIES = [
    ("Anthropic IPO", "anthropic-ipo-2026-10-26"),
    ("Microsoft buyouts", "microsoft-voluntary-buyouts-2026-10-26"),
    ("Options Investing", "retail-options-share-2026-10-26"),
]
OUTPUT = ROOT / "exports/astra-redesign-comparison-2026-10-26.png"


async def main():
    files = {"/lato.ttf": (ROOT / "assets/fonts/lato/Lato-Black.ttf", "font/ttf")}
    rows = []
    for label, suffix in [("PREVIOUS DESIGNS", "integrated"), ("NEW DESIGNS", "astra")]:
        cards = []
        for title, stem in STORIES:
            name = f"{stem}-{suffix}.png"
            path = ROOT / "exports" / name
            if not path.is_file():
                raise FileNotFoundError(path)
            files["/" + name] = (path, "image/png")
            cards.append(f'<figure><figcaption>{title}</figcaption><img src="/{name}"></figure>')
        rows.append(f'<section><h2>{label}</h2><div class="grid">{"".join(cards)}</div></section>')
    html = ("""<!doctype html><html><head><meta charset="utf-8"><style>
      @font-face{font-family:Lato;src:url('/lato.ttf');font-weight:900}
      *{box-sizing:border-box}html,body{margin:0;width:1800px;height:2320px}
      body{background:#151719;color:#f3f0ea;padding:44px 64px;font-family:Lato;font-weight:900}
      h1{font-size:34px;letter-spacing:1px;margin:0 0 24px}
      section{margin:0 0 30px}h2{font-size:22px;letter-spacing:2.2px;color:#bcbab7;margin:0 0 14px}
      .grid{display:grid;grid-template-columns:repeat(3,540px);gap:26px}
      figure{margin:0}figcaption{font-size:25px;margin:0 0 12px}
      img{display:block;width:540px;height:960px;object-fit:contain}
      </style></head><body><h1>MONEYBERG NEWS BRIEF / DESIGN COMPARISON</h1>"""
      + "".join(rows) + "</body></html>").encode()

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            resource = urlsplit(self.path).path
            if resource == "/":
                data, mime = html, "text/html; charset=utf-8"
            elif resource in files:
                path, mime = files[resource]
                data = path.read_bytes()
            else:
                self.send_error(404)
                return
            self.send_response(200)
            self.send_header("Content-Type", mime)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def log_message(self, *_args):
            pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(
                executable_path="/usr/bin/chromium", args=["--no-sandbox", "--disable-dev-shm-usage"])
            page = await browser.new_page(viewport={"width":1800, "height":2320}, device_scale_factor=1)
            await page.goto(f"http://127.0.0.1:{server.server_address[1]}/")
            await page.evaluate("""async () => {
              await document.fonts.ready;
              await Promise.all(Array.from(document.images).map(image => image.decode()));
            }""")
            sizes = await page.evaluate("""() => Array.from(document.images).map(image =>
              [image.naturalWidth,image.naturalHeight])""")
            assert sizes == [[1080,1920]] * 6, sizes
            assert await page.evaluate("document.documentElement.scrollHeight") == 2320
            await page.screenshot(path=str(OUTPUT), animations="disabled")
            await browser.close()
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
    print(json.dumps({"output":str(OUTPUT),"dimensions":[1800,2320],
                      "sha256":hashlib.sha256(OUTPUT.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    asyncio.run(main())
