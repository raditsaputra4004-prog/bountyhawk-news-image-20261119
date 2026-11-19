# Thursday 19 November 2026 — the world in one image

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/raditsaputra4004-prog/bountyhawk-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/raditsaputra4004-prog/bountyhawk-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Entry for make.fun [`news-image-20261119`](https://make.fun/bounty/news-image-20261119): one 1024×1024 image summing up
the world's news of Thursday 19 November 2026. Referral code `2yq7mcmp` — https://make.fun/r/2yq7mcmp

## What the image shows

Six stories, each verified against reporting of 19 November 2026
(Reuters, AP, AFP, The Times, IMD, the ICJ and others):

1. **Diplomacy** — Trump, Xi and Putin hold their first three-way summit
   in Shenzhen and issue a four-point "Declaration Towards Peace".
2. **Justice** — The ICJ rules 9–6 that Myanmar committed genocide
   against the Rohingya in 2017, the first such finding against a state.
3. **Markets** — Anthropic's $107bn debut, the biggest IPO ever, with
   shares starting to trade on the Nasdaq.
4. **Weather** — Cyclone Akvan nears India's east coast; Odisha evacuates
   coastal districts ahead of Friday's landfall.
5. **Conflict** — The Kerch Bridge is hit for a third time in four days;
   rail traffic halts.
6. **Climate** — COP31 enters its final stage, split over fossil fuels.

The footer adds three more items from the day: the IAEA on North
Korea's uranium enrichment, the LPG tanker Gas Husky sinking off
Bulgaria, and a Russian military plane crash that killed all 19 aboard.

## How it was made

`tools/draw.py` renders `entry.png` from the researched facts with
Pillow and DejaVu (no downloaded images, no AI-generated art — every
word is exact text, so nothing can come out garbled). `main.ts`
(Node, standard library only) copies `entry.png` to the output
directory, so both grader runs write identical bytes.

Run it locally:

```sh
python3 tools/draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see `LICENSE`.
