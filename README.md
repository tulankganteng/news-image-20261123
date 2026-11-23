# The World Today — news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/tulankganteng/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/tulankganteng/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

This is an entry for the make.fun bounty
[news-image-20261123](https://make.fun/bounty/news-image-20261123)
($100, deadline Tuesday 2026-11-25 07:00 WIB). The task: sum up the
world's news of Monday 23 November 2026 in a single image. The entry
is a small program that writes that image to `/output/entry.png`.

## The front page

The image is laid out like a newspaper front page under the masthead
**THE WORLD TODAY — MONDAY 23 NOVEMBER 2026**. At the top, a lead
strip covers the day's biggest story — the collapse of the COP31
climate talks in Antalya, which ended with no deal — beside a small
photo of the empty plenary hall. Under it runs a dated timeline strip
for 20–23 November, so the reader can place each development in the
weekend's sequence at a glance.

Below that, the page is a dense grid of seven region blocks, five
stories in each, for 35 stories in total. Every block opens with a
coloured region header, and every story is a short bold kicker plus a
one-line headline. Each item carries a figure, a place, or a date, so
the page reads as news, not decoration.

The timeline strip itself reads, day by day:

- **20 Nov** — three Russian missiles fall in Poland.
- **21 Nov** — Iran strikes US bases in Bahrain.
- **22 Nov** — COP31 collapses with no deal; Alcaraz and Verstappen
  win their titles.
- **23 Nov** — the Indonesia factory-fire toll hits 24.

| Region | What the five stories cover |
|---|---|
| North America | Wall Street's worst week since March 2020 — Nasdaq down 10%, S&P down 8.6%, trillions wiped, futures rebounding Monday; Bitcoin dipping to about $55,100 on Saturday, its lowest since September 2024, then recovering toward $61,000; a US intelligence probe into Alice Huang and the Singapore firm Megaspeed; the Treasury Secretary warning the Fed against overtightening; a bridge exploit minting 6 trillion ACE tokens. |
| Latin America | The capture of 'El Chapo Isidro' in Guasave, with 11 dead in the operation; Jair Bolsonaro still in intensive care, clinically stable with no discharge date; three million people greeting Pope Leo XIV in Peru, where a rosary thrown from the crowd struck him in Cusco; the US signing a military deal with Venezuela; Nayib Bukele seeking a third term in El Salvador. |
| Europe | An emergency NATO council meeting on Monday after three Russian Kh-101 missiles fell in Poland; Russia firing 186 drones at Ukraine overnight; the COP31 fallout, with the EU objecting to the draft text and 90-plus nations signing an electrification pledge; the UK barring crypto exchanges from market-making on their own venues; France beating Argentina 45–17 in rugby. |
| Middle East | Two people injured in the Bahrain strikes, with Iran claiming a 20th US drone downed and 25 tankers hit in a week; two killed in Gaza on Sunday and more than 1,600 dead since the October 2025 truce; two supertankers catching fire on mines near Ghanam Island; settler attacks and a Saudi airstrike on a Sanaa fuel station; Iran saying 623 children are among nearly 7,200 killed. |
| Africa | The Bayelsa boat toll rising to 29, with President Tinubu donating N250m to victims' families; drone strikes killing five children in Khartoum and Omdurman; rebels killing at least 15 civilians in north-west South Sudan; Kenya and DR Congo restoring full diplomatic relations; Gambia intercepting 491 would-be migrants. |
| Asia-Pacific | The Indonesia factory-fire toll confirmed at 24, with around 30 still missing; Asian markets sliding — Kospi down 3%, Hang Seng down 1.08%, Nikkei closed for a holiday; TSMC and Samsung pausing some China shipments under a new US chip rule; GIFT Nifty up 245 points pre-open; the Nikkei down 7.7% for the week. |
| Oceania, Sport & Culture | Carlos Alcaraz beating Alexander Zverev 6–2, 7–6(7) for his first ATP Finals title; Max Verstappen winning a chaotic Las Vegas Grand Prix, his 75th career win; the France–South Africa rugby final set for 29 November; Australia pushing back on a US report about AUKUS; GTA 6 review-bombed, critics 99 against users 5.6. |

## How it runs

`main.py` (Python 3.13, standard library only) takes the finished
`entry.png` that ships in this repository, checks it is a genuine
1024×1024 PNG under 1 MiB, and copies it to the output directory —
`/output/entry.png` by default, or wherever `$MAKEFUN_OUTPUT_DIR`
points for local runs. It then reads the copy back and compares
SHA-256 hashes to prove the copy is byte-for-byte identical before
it reports success. There are no network calls, no clock reads, and
no randomness anywhere in the path.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# wrote out/entry.png (293414 bytes, 1024x1024 PNG, sha256 b8ce28250cfff50a...)
```

## Sources

Every story on the page was first reported between 20 and 23
November 2026. The main wires and outlets behind them are Reuters,
AP, CNN, BBC, and AFP, plus ATP and Formula 1 for the sporting
results. The two anchor facts were checked against live reporting
on 23 November: the COP31 collapse in Antalya (CNN, Reuters — no
cover decision, the longest COP on record, the first breakdown since
Copenhagen in 2009) and the market rout (Nasdaq −10% for its worst
week since March 2020; Bitcoin touching about $55,100 on Saturday).
Claims that could not be independently confirmed are marked as
claims on the page itself.

## License

MIT — see [LICENSE](LICENSE).

## Reproducibility

The image never changes: `main.py` only copies the repository's own
`entry.png` and verifies the copy. Run it twice and the two outputs
are identical, byte for byte, with the same SHA-256. Nothing in the
program depends on the time of day, the machine, or the network.
