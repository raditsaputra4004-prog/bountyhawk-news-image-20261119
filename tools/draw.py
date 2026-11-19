#!/usr/bin/env python3
"""Draw the 19 November 2026 world-news front page.

Renders entry.png (1024x1024) from the researched facts below with Pillow
and DejaVu fonts only. Every word on the page is exact text from this file,
so nothing can come out garbled. Run: python3 tools/draw.py
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
MARGIN = 28
CONTENT_W = W - 2 * MARGIN

PAPER = (247, 243, 234)
INK = (26, 26, 26)
SOFT_INK = (74, 74, 74)
RULE = (169, 30, 34)
NAVY = (31, 42, 68)
GOLD = (176, 124, 22)

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    """Greedy word wrap by pixel width; returns a list of lines."""
    lines = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        if not words:
            lines.append("")
            continue
        current = words[0]
        for word in words[1:]:
            trial = current + " " + word
            if draw.textlength(trial, font=fnt) <= max_width:
                current = trial
            else:
                lines.append(current)
                current = word
        lines.append(current)
    return lines


def fit(draw, text, fnt, max_width, max_lines):
    """Wrap text to at most max_lines lines, ellipsising the last one."""
    lines = wrap(draw, text, fnt, max_width)
    if len(lines) <= max_lines:
        return lines
    lines = lines[:max_lines]
    while lines and draw.textlength(lines[-1] + " …", font=fnt) > max_width:
        lines[-1] = lines[-1].rsplit(" ", 1)[0]
    lines[-1] += " …"
    return lines


def draw_card(draw, box, kicker, colour, headline, body,
              head_size=27, body_size=20, head_lines=2, body_lines=3):
    """One story card: coloured top bar, kicker, headline, body text."""
    x0, y0, x1, y1 = box
    draw.rectangle([x0, y0, x1, y1], fill=(255, 255, 255),
                   outline=(198, 190, 174), width=1)
    draw.rectangle([x0, y0, x1, y0 + 5], fill=colour)
    pad = 16
    cx = x0 + pad
    cw = x1 - x0 - 2 * pad
    y = y0 + 18
    kf = font(SANS_BOLD, 19)
    draw.text((cx, y), kicker, font=kf, fill=colour)
    y += 30
    hf = font(SANS_BOLD, head_size)
    for line in fit(draw, headline, hf, cw, head_lines):
        draw.text((cx, y), line, font=hf, fill=INK)
        y += head_size + 6
    y += 4
    bf = font(SANS, body_size)
    for line in fit(draw, body, bf, cw, body_lines):
        draw.text((cx, y), line, font=bf, fill=SOFT_INK)
        y += body_size + 6
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead.
    mast = font(SERIF_BOLD, 42)
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=mast)
    d.text(((W - tw) / 2, 24), title, font=mast, fill=INK)
    date_f = font(SANS_BOLD, 31)
    date = "Thursday 19 November 2026"
    dw = d.textlength(date, font=date_f)
    d.text(((W - dw) / 2, 76), date, font=date_f, fill=RULE)
    d.line([(MARGIN, 120), (W - MARGIN, 120)], fill=INK, width=2)
    d.line([(MARGIN, 125), (W - MARGIN, 125)], fill=INK, width=1)

    # Lead story: the Shenzhen trilateral summit.
    lead = (MARGIN, 138, W - MARGIN, 350)
    d.rectangle(lead, fill=(255, 255, 255),
                outline=(198, 190, 174), width=1)
    d.rectangle([MARGIN, 138, MARGIN + 8, 350], fill=RULE)
    x = MARGIN + 26
    cw = W - MARGIN - x - 18
    y = 152
    kf = font(SANS_BOLD, 20)
    d.text((x, y), "DIPLOMACY  ·  SHENZHEN", font=kf, fill=RULE)
    y += 32
    hf = font(SANS_BOLD, 34)
    for line in fit(d, "Trump, Xi and Putin hold first three-way summit",
                    hf, cw, 2):
        d.text((x, y), line, font=hf, fill=INK)
        y += 40
    y += 2
    bf = font(SANS, 20)
    body = ("The leaders of the US, China and Russia meet at the APEC forum "
            "and issue a four-point “Declaration Towards Peace”: UN reform, "
            "more refined oil, a narrower ICC reach and talks on nuclear "
            "risk. No deal on Ukraine or Iran.")
    for line in fit(d, body, bf, cw, 3):
        d.text((x, y), line, font=bf, fill=SOFT_INK)
        y += 26

    # Four stories in a two-by-two grid.
    col_w = (CONTENT_W - 16) // 2
    grid = [
        ("JUSTICE  ·  THE HAGUE", NAVY,
         "World court: Myanmar committed genocide",
         "The ICJ rules 9–6 that Myanmar’s 2017 Rohingya crackdown was "
         "genocide, the first such finding against a state. It orders "
         "reparations."),
        ("MARKETS  ·  NEW YORK", GOLD,
         "Anthropic’s $107bn debut, the biggest IPO ever",
         "The AI firm behind Claude prices shares at $83, raising $81.3bn "
         "— the largest IPO ever. Shares debut on the Nasdaq today."),
        ("WEATHER  ·  INDIA", (21, 101, 124),
         "Cyclone Akvan: nearly 50,000 evacuated",
         "Odisha evacuates coastal districts as severe Cyclone Akvan "
         "nears India — the third storm in a month. Landfall due Friday "
         "noon."),
        ("CONFLICT  ·  UKRAINE", RULE,
         "Kerch Bridge hit for a third time in four days",
         "An overnight strike halts rail traffic on the bridge to Crimea, "
         "days after attacks brought down part of its road span. No "
         "casualties reported."),
    ]
    gx = [MARGIN, MARGIN + col_w + 16]
    gy = [362, 562]
    for i, (kicker, colour, head, body) in enumerate(grid):
        box = (gx[i % 2], gy[i // 2],
               gx[i % 2] + col_w, gy[i // 2] + 190)
        draw_card(d, box, kicker, colour, head, body, body_size=18)

    # Wide climate card.
    wide = (MARGIN, 764, W - MARGIN, 900)
    draw_card(d, wide, "CLIMATE  ·  COP31", (46, 110, 58),
              "Climate talks split on fossil fuels",
              "COP31 enters its final stage with negotiators divided over "
              "whether the deal calls for a “transition away” from fossil "
              "fuels or a stronger phaseout.",
              head_size=26, body_size=20, head_lines=1, body_lines=2)

    # Footer ticker.
    tick = (MARGIN, 912, W - MARGIN, 968)
    d.rectangle(tick, fill=NAVY)
    tf = font(SANS_BOLD, 19)
    ticker = ("IAEA: North Korea expanded uranium enrichment   •   "
              "LPG tanker Gas Husky sinks off Bulgaria   •   "
              "Russian military plane crashes, killing all 19 aboard")
    ty = 920
    for line in fit(d, ticker, tf, CONTENT_W - 32, 2):
        d.text((MARGIN + 16, ty), line, font=tf, fill=(255, 255, 255))
        ty += 25

    # Source line.
    sf = font(SANS, 15)
    src = ("Sources: Reuters · AP · AFP · The Times · IMD · ICJ · Xinhua — "
           "all events reported on 19 November 2026")
    sw = d.textlength(src, font=sf)
    d.text(((W - sw) / 2, 982), src, font=sf, fill=SOFT_INK)

    img.save("entry.png", format="PNG")
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
