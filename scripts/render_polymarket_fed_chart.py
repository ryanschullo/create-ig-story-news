#!/usr/bin/env python3
"""Render the archived hourly October Fed market, without resampling its data.

Run from any directory with Python, matplotlib, and NumPy installed. The PNG is
intended as an accurately rendered chart panel within an Instagram Story, not as
the complete news graphic. Its only typeface is the bundled Lato Black master.
"""

from __future__ import annotations

import csv
import math
import os
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

os.environ.setdefault("MPLCONFIGDIR", "/tmp/moneyberg-matplotlib")
os.environ.setdefault("XDG_CACHE_HOME", "/tmp/moneyberg-cache")

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.ft2font import FT2Font
from matplotlib.text import Text


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "assets/data/polymarket-fed-october-2026/all-outcomes-hourly.csv"
FONT = ROOT / "assets/fonts/lato/Lato-Black.ttf"
OUTPUT = ROOT / "assets/charts/polymarket-fed-october-2026-month.png"
CHICAGO = ZoneInfo("America/Chicago")
BACKGROUND = "#F6F8FA"
NAVY = "#17314A"
DPI = 180
WIDTH, HEIGHT = 1800, 1250

# These are the final historical observations, not a later Gamma snapshot.
SERIES = [
    ("No change", "No change", "#168C81", 3.7, "-", 708, 93.5),
    ("25 bps increase", "25 bp hike", "#E28A19", 3.3, "-", 709, 5.5),
    ("50+ bps increase", "50+ bp hike", "#C64343", 1.9, (0, (5, 3)), 701, 0.35),
    ("25 bps decrease", "25 bp cut", "#3479BD", 1.8, (0, (3, 2)), 707, 0.15),
    ("50+ bps decrease", "50+ bp cut", "#7956A6", 1.8, (0, (1, 2)), 703, 0.05),
]


def load_series():
    grouped = defaultdict(list)
    with DATA.open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source))
    if len(rows) != 3528:
        raise ValueError(f"Expected 3,528 archived observations, received {len(rows):,}")
    if {row["outcome"] for row in rows} != {item[0] for item in SERIES}:
        raise ValueError("The archived outcome set has changed")
    for row in rows:
        grouped[row["outcome"]].append(row)

    result = {}
    for outcome, _, _, _, _, expected_count, expected_end in SERIES:
        records = sorted(grouped[outcome], key=lambda row: int(row["timestamp_unix"]))
        if len(records) != expected_count:
            raise ValueError(f"Unexpected observation count for {outcome}")
        x, y, break_count = [], [], 0
        previous = None
        for row in records:
            timestamp = int(row["timestamp_unix"])
            when = datetime.fromtimestamp(timestamp, tz=CHICAGO)
            if when != datetime.fromisoformat(row["timestamp_chicago"]):
                raise ValueError("Chicago timestamp differs from archived Unix time")
            value = float(row["probability_percent"])
            if not 0 <= value <= 100:
                raise ValueError("An archived probability is outside 0–100%")
            if not math.isclose(value, float(row["price"]) * 100, abs_tol=1e-10):
                raise ValueError("Archived price and probability disagree")
            if previous is not None and timestamp <= previous:
                raise ValueError("Duplicate or unordered archived timestamps")
            should_break = previous is not None and timestamp - previous > 5400
            if (row["break_line_before"] == "1") != should_break:
                raise ValueError("Gap flag does not match a gap exceeding 90 minutes")
            if should_break:
                # A NaN is only a path separator; no observations are invented.
                x.append(mdates.date2num(when))
                y.append(np.nan)
                break_count += 1
            x.append(mdates.date2num(when))
            y.append(value)
            previous = timestamp
        if not math.isclose(y[-1], expected_end, abs_tol=1e-9):
            raise ValueError(f"Historical endpoint changed for {outcome}")
        if records[0]["timestamp_chicago"][:10] != "2026-09-25":
            raise ValueError("Unexpected first observation date")
        if records[-1]["timestamp_chicago"][:13] != "2026-10-25T22":
            raise ValueError("Unexpected last observation hour")
        result[outcome] = (np.array(x), np.array(y), break_count)
    return result


def render():
    face = FT2Font(str(FONT))
    if face.family_name != "Lato" or face.style_name != "Black":
        raise ValueError("The bundled typeface must be Lato Black")
    font_manager.fontManager.addfont(str(FONT))
    label_font = font_manager.FontProperties(fname=str(FONT), size=22)
    if Path(font_manager.findfont(label_font, fallback_to_default=False)).resolve() != FONT.resolve():
        raise ValueError("Lato Black did not resolve to its bundled font file")
    series = load_series()

    with plt.rc_context({"svg.fonttype": "path", "text.color": NAVY}):
        fig = plt.figure(figsize=(WIDTH / DPI, HEIGHT / DPI), dpi=DPI, facecolor=BACKGROUND)
        ax = fig.add_axes([0.17, 0.325, 0.79, 0.455], facecolor=BACKGROUND)
        fig.text(0.055, 0.935, "October Fed decision: one month of odds",
                 fontsize=28, ha="left", va="top", color=NAVY)
        fig.text(0.055, 0.865, "SEP 25–OCT 25, 2026  •  CHICAGO TIME",
                 fontsize=20, ha="left", va="top", color=NAVY)

        handles = {}
        # The two main outcomes are drawn last so thin low-probability paths do
        # not obscure them. Every non-NaN coordinate is an actual archived row.
        for outcome, label, color, width, style, count, endpoint in reversed(SERIES):
            x, y, _ = series[outcome]
            line, = ax.plot(x, y, color=color, linewidth=width, linestyle=style,
                            solid_capstyle="round", label=f"{label} — {endpoint:g}%")
            ax.plot(x[-1], y[-1], "o", color=color, markersize=5, zorder=8, clip_on=False)
            handles[outcome] = line
            if np.count_nonzero(np.isfinite(y)) != count:
                raise ValueError("Rendered coordinate count differs from archived rows")

        ax.set_ylim(0, 100)
        ax.set_yticks([0, 25, 50, 75, 100])
        ax.set_ylabel("Market-implied probability (%)", fontsize=20, labelpad=18, color=NAVY)
        ax.set_xlim(datetime(2026, 9, 25, tzinfo=CHICAGO),
                    datetime(2026, 10, 25, 23, 59, 59, tzinfo=CHICAGO))
        ticks = [(9, 25), (10, 3), (10, 10), (10, 17), (10, 25)]
        ax.set_xticks([datetime(2026, month, day, tzinfo=CHICAGO) for month, day in ticks])
        ax.set_xticklabels(["Sep 25", "Oct 3", "Oct 10", "Oct 17", "Oct 25"])
        ax.tick_params(axis="both", labelsize=22, colors=NAVY, length=0, pad=12)
        ax.grid(axis="y", color="#D4DFE7", linewidth=1.1)
        ax.set_axisbelow(True)
        for side in ["top", "right"]:
            ax.spines[side].set_visible(False)
        for side in ["left", "bottom"]:
            ax.spines[side].set_color("#BAC9D6")
            ax.spines[side].set_linewidth(1.0)

        # Matplotlib fills columns first: arrange handles for a sensible row order.
        legend_order = ["No change", "50+ bps increase", "50+ bps decrease",
                        "25 bps increase", "25 bps decrease"]
        legend = fig.legend([handles[name] for name in legend_order],
                            [handles[name].get_label() for name in legend_order],
                            loc="lower center", bbox_to_anchor=(0.53, 0.035),
                            ncol=2, frameon=False, fontsize=20,
                            handlelength=2.15, columnspacing=1.5,
                            labelspacing=0.8, handletextpad=0.55, borderpad=0)

        # Pin every authored title, tick, axis, and legend to the actual font file.
        for text in fig.findobj(match=Text):
            size = text.get_fontsize()
            text.set_fontproperties(font_manager.FontProperties(fname=str(FONT), size=size))
            text.set_color(NAVY)
        fig.canvas.draw()
        renderer = fig.canvas.get_renderer()
        failures = []
        for text in fig.findobj(match=Text):
            if not text.get_visible() or not text.get_text().strip():
                continue
            box = text.get_window_extent(renderer)
            if box.x0 < 8 or box.y0 < 8 or box.x1 > WIDTH - 8 or box.y1 > HEIGHT - 8:
                failures.append(text.get_text())
            resolved = Path(font_manager.findfont(text.get_fontproperties(), fallback_to_default=False))
            if resolved.resolve() != FONT.resolve():
                raise ValueError("A text artist uses a fallback font")
        if failures:
            raise ValueError(f"Text exceeds output bounds: {failures}")
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(OUTPUT, dpi=DPI, facecolor=BACKGROUND)
        fig.savefig(OUTPUT.with_suffix(".svg"), facecolor=BACKGROUND)
        plt.close(fig)

    print(f"Rendered {OUTPUT.relative_to(ROOT)} ({WIDTH} × {HEIGHT})")
    print("Verified Lato Black file for every text artist; all text inside canvas.")
    for outcome, _, _, _, _, count, endpoint in SERIES:
        print(f"{outcome}: {count} actual points, {series[outcome][2]} explicit gaps, final {endpoint:g}%")


if __name__ == "__main__":
    render()
