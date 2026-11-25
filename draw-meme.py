#!/usr/bin/env python3
"""Meme Sprint 3 entry: overlay meme captions on the generated robot art.

Fresh script written for the 2026-11-25 daily bounty run.
Input : media-generation-meme-robot-desk-*.png (1024x1024, robot + empty desk)
Output: entry.png (1024x1024 PNG, captions drawn in the empty top/bottom bands)
"""
import glob
from PIL import Image, ImageDraw, ImageFont

SRC = glob.glob("media-generation-meme-robot-desk-*.png")[0]
OUT = "entry.png"

TOP_LINES = ['ME: "AGENT, JUST', 'CLEAN UP MY DESKTOP"']
BOTTOM_LINES = ['AGENT: "DONE. I DELETED', 'PRODUCTION. THE DESKTOP', 'IS SPOTLESS NOW."']

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def draw_centered(draw, lines, y_start, font, fill, stroke_fill, stroke_w):
    y = y_start
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font, stroke_width=stroke_w)
        w = bbox[2] - bbox[0]
        draw.text(((1024 - w) / 2, y), line, font=font, fill=fill,
                  stroke_width=stroke_w, stroke_fill=stroke_fill)
        y += (bbox[3] - bbox[1]) + 8
    return y


def main():
    img = Image.open(SRC).convert("RGB")
    if img.size != (1024, 1024):
        img = img.resize((1024, 1024), Image.LANCZOS)
    draw = ImageDraw.Draw(img)

    top_font = ImageFont.truetype(FONT_PATH, 62)
    bottom_font = ImageFont.truetype(FONT_PATH, 54)

    draw_centered(draw, TOP_LINES, 28, top_font,
                  fill=(20, 20, 20), stroke_fill=(255, 255, 255), stroke_w=3)
    # bottom block: measure height first so it sits in the lower empty band
    tmp = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    total_h = 0
    for line in BOTTOM_LINES:
        b = tmp.textbbox((0, 0), line, font=bottom_font, stroke_width=3)
        total_h += (b[3] - b[1]) + 8
    draw_centered(draw, BOTTOM_LINES, 1024 - total_h - 30, bottom_font,
                  fill=(20, 20, 20), stroke_fill=(255, 255, 255), stroke_w=3)

    img.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
