#!/usr/bin/env python3
"""Render a data-led Story with the recorded chart and unredrawn logo.

The decorative background is generated separately. Chart pixels come from the
validated Matplotlib plot; probabilities are never drawn by an image model.
Georgia is a runtime font, not redistributed with this repository.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/moneyberg-matplotlib")
os.environ.setdefault("XDG_CACHE_HOME", "/tmp/moneyberg-cache")

import matplotlib

matplotlib.use("Agg")
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, Rectangle


ROOT = Path(__file__).resolve().parents[1]
WIDTH, HEIGHT, DPI = 1080, 1920, 100
LATO = ROOT / "assets/fonts/lato/Lato-Black.ttf"
CHART = ROOT / "assets/charts/polymarket-fed-october-2026-month.png"
BACKGROUND = ROOT / "assets/fed-rate-decision-background.png"
COIN = ROOT / "assets/moneyberg-coin-original.png"
OUTPUT = ROOT / "exports/polymarket-fed-decision-2026-10-28.png"
COIN_HASH = "4881cdd23eb81a8bd14be818e7b7d0b5f7a27f101402abebf42be7f07b9f5716"


def render(georgia: Path):
    if not georgia.is_file():
        raise FileNotFoundError("Provide the actual Georgia font; fallback is not allowed")
    if font_manager.FontProperties(fname=str(georgia)).get_name() != "Georgia":
        raise ValueError("The body/source font must be Georgia")
    if hashlib.sha256(COIN.read_bytes()).hexdigest() != COIN_HASH:
        raise ValueError("Original Moneyberg artwork changed")
    for font in (LATO, georgia):
        font_manager.fontManager.addfont(str(font))

    fig = plt.figure(figsize=(WIDTH / DPI, HEIGHT / DPI), dpi=DPI, facecolor="#0D2033")
    background_ax = fig.add_axes([0, 0, 1, 1], zorder=0)
    background_ax.imshow(mpimg.imread(BACKGROUND), extent=(0, WIDTH, HEIGHT, 0), aspect="auto")
    background_ax.set_xlim(0, WIDTH)
    background_ax.set_ylim(HEIGHT, 0)
    background_ax.axis("off")
    # This is a new plotted figure; no source artwork is overwritten.
    fig.patches.append(Rectangle((0, 0), 1, 1, transform=fig.transFigure,
                                 color="#071827", alpha=0.22, linewidth=0, zorder=1))

    authored = []

    def text(x, y, value, pixels, face=LATO, color="#F8F7F0"):
        prop = font_manager.FontProperties(fname=str(face), size=pixels * 72 / DPI)
        artist = fig.text(x / WIDTH, 1 - y / HEIGHT, value, ha="left", va="top",
                          fontproperties=prop, color=color, zorder=5)
        authored.append((artist, face))
        return artist

    text(130, 185, "MONEYBERG NEWS BRIEF", 30)
    fig.patches.append(Rectangle((130 / WIDTH, 1 - 233 / HEIGHT), 820 / WIDTH,
                                 2 / HEIGHT, transform=fig.transFigure,
                                 color="#A8B8C4", alpha=0.65, linewidth=0, zorder=4))
    text(130, 258, "FED DECISION  •  WEDNESDAY, OCT. 28, 2026", 26)
    text(130, 325, "Fed hold odds", 78)
    text(130, 415, "surge over a month", 78)
    text(125, 535, "93.5%", 145, color="#7CE3CF")
    text(635, 565, "NO CHANGE", 40)
    text(635, 620, "Polymarket", 28, georgia)
    text(130, 708, "From 32.5% on Sep. 25 to 93.5% on Oct. 25", 29, georgia)

    chart = mpimg.imread(CHART)
    chart_x, chart_y, chart_width = 124, 788, 830
    chart_height = chart_width * chart.shape[0] / chart.shape[1]
    panel = FancyBboxPatch((chart_x / WIDTH, 1 - (chart_y + chart_height) / HEIGHT),
                           chart_width / WIDTH, chart_height / HEIGHT,
                           boxstyle="round,pad=0.003,rounding_size=0.012",
                           transform=fig.transFigure, facecolor="#F6F8FA",
                           edgecolor="#A9C0CE", linewidth=1.1, zorder=2)
    fig.patches.append(panel)
    chart_ax = fig.add_axes([chart_x / WIDTH, 1 - (chart_y + chart_height) / HEIGHT,
                             chart_width / WIDTH, chart_height / HEIGHT], zorder=3)
    chart_ax.imshow(chart, interpolation="lanczos", aspect="equal")
    chart_ax.axis("off")

    fig.patches.append(FancyBboxPatch((124 / WIDTH, 1 - 1530 / HEIGHT),
                                      830 / WIDTH, 148 / HEIGHT,
                                      boxstyle="round,pad=0.002,rounding_size=0.008",
                                      transform=fig.transFigure, facecolor="#071827",
                                      edgecolor="none", alpha=0.82, zorder=2))
    text(130, 1390, "Market-implied probabilities, not a Fed forecast.", 28, georgia)
    text(130, 1430, "Hourly history  •  Last points: Oct. 25, 10 p.m. CDT", 25, georgia)
    text(130, 1466, "Source: Polymarket  •  Gaps reflect missing observations", 24, georgia)
    text(130, 1500, "Prices may not total 100%  •  Editorial illustration", 22, georgia)

    # Uniformly scaled original PNG annotation; no generated portrait or rim.
    coin_size, coin_x, coin_y = 238, 775, 1645
    coin_ax = fig.add_axes([coin_x / WIDTH, 1 - (coin_y + coin_size) / HEIGHT,
                            coin_size / WIDTH, coin_size / HEIGHT], zorder=3)
    coin_ax.imshow(mpimg.imread(COIN), interpolation="lanczos", alpha=0.68)
    coin_ax.axis("off")

    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    boxes = []
    inner = (104, 164, 961, 1536)
    for artist, expected_font in authored:
        box = artist.get_window_extent(renderer)
        bounds = (box.x0, HEIGHT - box.y1, box.x1, HEIGHT - box.y0)
        if bounds[0] < inner[0] or bounds[1] < inner[1] or bounds[2] > inner[2] or bounds[3] > inner[3]:
            raise ValueError(f"Authored text exceeds inner bounds: {artist.get_text()}: {bounds}")
        resolved = Path(font_manager.findfont(artist.get_fontproperties(), fallback_to_default=False)).resolve()
        if resolved != expected_font.resolve():
            raise ValueError(f"Font fallback: {artist.get_text()}")
        boxes.append({"text": artist.get_text(), "bounds": bounds,
                      "font_family": artist.get_fontproperties().get_name()})
    # Check the full data panel, including all chart axes/legend/title.
    panel_bounds = (chart_x - 4, chart_y - 6, chart_x + chart_width + 4,
                    chart_y + chart_height + 6)
    if not (inner[0] <= panel_bounds[0] and inner[1] <= panel_bounds[1]
            and panel_bounds[2] <= inner[2] and panel_bounds[3] <= inner[3]):
        raise ValueError("The source chart panel exceeds inner bounds")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=DPI, facecolor=fig.get_facecolor())
    plt.close(fig)
    audit = {"dimensions": [WIDTH, HEIGHT], "inner_bounds": inner,
             "chart_panel_bounds": panel_bounds, "authored_text": boxes,
             "chart_sha256": hashlib.sha256(CHART.read_bytes()).hexdigest(),
             "original_coin_sha256": COIN_HASH,
             "snapshot": "2026-10-25 22:00 America/Chicago"}
    audit_file = ROOT / "briefs/polymarket-fed-decision-2026-10-28-layout.json"
    audit_file.write_text(json.dumps(audit, indent=2))
    print(f"Rendered {OUTPUT} at {WIDTH} × {HEIGHT}")
    print(f"Verified {len(authored)} text items, real font files and full chart within inner bounds")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--georgia-font", type=Path, required=True)
    args = parser.parse_args()
    render(args.georgia_font)
