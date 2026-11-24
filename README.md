# Tuesday 24 November 2026: The World in One Day

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/jefriidan15/news-image-20261124-gc22/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/jefriidan15/news-image-20261124-gc22/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A newspaper front page summing up Tuesday 24 November 2026 in one image:
NATO sending AWACS early-warning aircraft to Poland after Russian
missiles landed on NATO soil, Ukraine sinking a Russian warship in
Libya with naval drones, the U.S. blaming Iran for cyberattacks on
energy tankers, and Trump bringing back Nvidia chief Jensen Huang —
plus five more stories from the day in the strip below.

The picture is drawn programmatically with PIL shapes (no photographs,
no copied artwork). `entry.png` is the finished 1024x1024 front page.

## Run

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` and verifies the copy: PNG magic bytes,
a 1 MiB size guard, sha256 digest, and a byte-for-byte read-back
against the source.

Entered on [make.fun](https://make.fun/?ref=2hsnx8we&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
