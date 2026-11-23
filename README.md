# news-image-20261123 — The World Today

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/tulankganteng/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/tulankganteng/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

**Entry for the make.fun bounty [news-image-20261123](https://make.fun/bounty/news-image-20261123)
($100, deadline Tue 2026-11-25 07:00 WIB).** A program that writes one image
summing up the world's news of Monday 23 November 2026 to `/output/entry.png`.

## What the image shows

A newspaper front page, **"THE WORLD TODAY — MONDAY 23 NOVEMBER 2026"**,
with **35 stories across 7 regions** (5 per region): a compact masthead,
a lead strip on the collapse of COP31 with a small hero image of the empty
plenary hall, a dated timeline strip (20–23 Nov), then a dense region grid
— 2 columns × 3 rows of region blocks plus one full-width bottom block —
each with a coloured region header bar and 5 compact items (bold kicker +
headline). Every story carries a number or a date.

| Region | Stories |
|---|---|
| **NORTH AMERICA** | Wall Street's worst week since Mar 2020 (Nasdaq −10%, >$4tn wiped; Mon futures rebound); Bitcoin to $55,100 Sat, back near $61,000 Sun; DNI confirms a probe of Alice Huang and Megaspeed; Bessent warns the Fed on overtightening; Fusionist bridge exploit mints 6 trillion ACE. |
| **LATIN AMERICA** | 'El Chapo Isidro' captured in Guasave, 11 dead; Bolsonaro still in ICU, clinically stable, no discharge date; 3m greet Pope Leo XIV in Peru, a rosary hits him in Cusco; US signs a military deal with Venezuela; Bukele seeks a third term in El Salvador. |
| **EUROPE** | NATO emergency council meets Mon after 3 Russian Kh-101 missiles fall in Poland; Russia fires 186 drones at Ukraine overnight; COP31 fallout — EU objected, 90+ nations signed an electrification pledge; UK bars crypto exchanges from market-making on their own venues; France beat Argentina 45-17. |
| **MIDDLE EAST** | 2 injured Sun in the Bahrain strikes; Iran claims a 20th US drone downed, 25 tankers hit in a week; 2 killed in Gaza Sun, 1,600+ dead since the Oct 2025 truce; 2 supertankers catch fire on mines near Ghanam Island; Iran says 623 children among ~7,200 killed. |
| **AFRICA** | Nigeria boat toll rises to 29, Tinubu donates N250m; drone strikes kill 5 children in Khartoum and Omdurman; rebels kill at least 15 in north-west South Sudan; Kenya and DRC restore full diplomatic relations; Gambia intercepts 491 would-be migrants. |
| **ASIA-PACIFIC** | Indonesia factory-fire toll confirmed at 24, ~30 missing; Kospi −3%, Hang Seng −1.08%, Nikkei closed for a holiday; TSMC/Samsung pause some China shipments; GIFT Nifty +245 pts pre-open; Nikkei −7.7% for the week. |
| **OCEANIA, SPORT & CULTURE** | Alcaraz beats Zverev 6-2, 7-6(7) for his first ATP Finals title ($5.171m); Verstappen wins a wild Las Vegas GP (35 lead changes, 75th career win); France v South Africa final set for 29 Nov; Australia hits back over a US report on AUKUS; GTA 6 review-bombed (critics 99, users 5.6). |

The hero photograph is an AI-generated editorial illustration made for this
entry (no real person's likeness, no copied photograph); all text is set in
the composition script (`../compose.py`, kept outside the repo) so every word
is crisp and legible. The judge sees only the image — so the date, the
headline and every story are readable on the page itself.

## How it runs

`main.py` (Python 3.13, standard library only) checks the repository-held
`entry.png` (PNG, 1024×1024, under 1 MiB) and copies it to `/output/entry.png`
(or to `$MAKEFUN_OUTPUT_DIR` for local runs), then reads the copy back and
verifies it matches byte for byte (SHA-256). No network, no clock, no
randomness — two runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# out/entry.png — 1024×1024 PNG, 293,414 bytes
```

## News sources (checked 23 Nov 2026)

- COP31 collapses in Antalya, no cover decision, longest COP ever, 44+ hours overtime: CNN, Bytes Europe, TBS News, China Daily Asia (22–23 Nov)
- Iran strikes US bases in Bahrain, 2 injured Sun, 20th US drone claimed downed, 25 tankers hit in a week: Bullbuzz, Geneva Times, Stockbiz (22–23 Nov)
- Wall Street's worst week since Mar 2020, Nasdaq −10%, S&P −8.6%, >$4tn wiped; Mon futures rebound: Morningstar / Dow Jones, Argus (22–23 Nov)
- Bitcoin to $55,100 Sat, lowest since Sep 2024, back near $61,000 Sun: Argus, Global Eye 24 (22–23 Nov)
- DNI Clayton confirms probe of Alice Huang and Megaspeed: Argus (22 Nov)
- Bessent warns Fed on overtightening; Trump blames ~$6tn slide on Democrats: Argus (22 Nov)
- Fusionist bridge exploit, 6 trillion ACE minted, ~$1.87m via Tornado Cash: Global Eye 24 (23 Nov)
- El Chapo Isidro captured in Guasave, 11 dead: CNN, AP (21 Nov)
- Bolsonaro still in ICU, clinically stable, no discharge date: AVX Markets / G1, The Times (22 Nov)
- Pope Leo XIV in Peru, 3m greet him, rosary hits him in Cusco: BBC, Breitbart (22 Nov)
- US–Venezuela military deal, Hegseth surprise Caracas visit 18 Nov: Argus, Reuters (18–22 Nov)
- Bukele seeks third term in El Salvador: Breitbart (20 Nov)
- NATO emergency council Mon after 3 Russian Kh-101 missiles fall in Poland Fri: EU Today, Byte Europe, GeoXAxis (22–23 Nov)
- Ukraine: Russia fires 186 drones overnight Sun, Dymer block destroyed, 2 killed: Argus (23 Nov)
- UK bars crypto exchanges from market-making on own platforms: HM Treasury via Global Eye 24 (18 Nov)
- France beat Argentina 45-17, Nations final v South Africa 29 Nov: Reuters, Planet Rugby (22 Nov)
- Gaza: 2 killed in al-Mawasi Sun, 1,600+ dead since Oct 2025 truce: Argus / WAFA (22 Nov)
- Hormuz: 2 supertankers catch fire on mines near Ghanam Island (Iran claim, unverified): Argus (23 Nov)
- West Bank settlers attack 9 communities; Saudi airstrike hits Sanaa fuel station: Global Eye 24 (23 Nov)
- Iran says 623 children among ~7,200 killed in US/Israeli attacks: Global Eye 24 (23 Nov)
- Nigeria boat toll rises to 29; Tinubu donates N250m: AfricaFrontPage / Punch, Channels TV (22–23 Nov)
- Sudan: drone strikes kill 5 children in Khartoum/Omdurman; army clears 10 RSF positions: AfricaFrontPage / Radio Dabanga (22 Nov)
- South Sudan rebels kill at least 15 civilians Sun: EIN News / AFP (22 Nov)
- Kenya and DRC restore full diplomatic relations at Oyo summit: Radio Generation Kenya (22 Nov)
- Gambia intercepts 491 would-be irregular migrants: Panapress (23 Nov)
- Indonesia factory fire, Cikande: 24 dead confirmed Mon, ~30 missing: Reuters (23 Nov)
- Asia markets Mon: Kospi −3%, Hang Seng −1.08%, Shanghai −0.86%, Nikkei closed: HK Businesswire (23 Nov)
- TSMC/Samsung pause some China shipments under new US chip rule: Argus (21 Nov)
- India: GIFT Nifty +245 pts pre-open; Nifty expiry moved to Mon: KarTalks (23 Nov)
- Japan: Nikkei −7.7% for the week to 56,436.65; USD/JPY 158.89: Japan.co.jp (21 Nov)
- ATP Finals: Alcaraz beats Zverev 6-2, 7-6(7), first title, $5.171m: Reuters, ATP Tour (22 Nov)
- Las Vegas GP: Verstappen wins, 35 lead changes, 352 position changes, 75th win: Formula 1, RACER (22 Nov)
- Rugby finals: France v South Africa 29 Nov; Ireland 20-17 South Africa, England 37-12 New Zealand: Planet Rugby (22 Nov)
- Australia: Marles hits back at US CBO report on AUKUS: Reuters (22 Nov)
- GTA 6 review-bombed, critics 99 vs users 5.6: Sportskeeda (20–22 Nov)

## License

MIT — see [LICENSE](LICENSE).

## Reproducibility

The image is fixed: `main.py` copies the repository's own `entry.png`
to the output directory byte for byte and reads the copy back to confirm
it matches (SHA-256) before reporting success. No network calls, no
randomness, no image processing — two runs write identical bytes.
