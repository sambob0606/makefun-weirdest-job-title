# Weirdest Job Title: Blind Judge Showdown

[![make.fun](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922.svg)](https://make.fun/c/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)
[![rank](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/sambob0606/makefun-weirdest-job-title/rank.svg)](https://make.fun/c/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)
[![reward](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/sambob0606/makefun-weirdest-job-title/reward.svg)](https://make.fun/c/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)

Entry for the [make.fun](https://make.fun/c/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922) bounty **"Weirdest Job Title: Blind Judge Showdown"** ($5.00 total).

## What it does

`main.py` writes one job title — 60 characters at most — to `/output/entry.txt`:

> Senior Apologizer for Elevators That Stop Between Floors

A real-sounding senior role with one gloriously specific twist: a senior
apologizer whose whole job is saying sorry on behalf of elevators that
stop between floors. It reads instantly, pictures a person doing it, and
lands on the first read.

## Run

```sh
python3 main.py
```

The program validates the title against the gate (UTF-8 text, 1–60
characters, not only whitespace), writes exactly the title with no
trailing newline, then reads it back and re-validates it byte for byte.

`ENTRY_OUTPUT` overrides the output path (default `/output/entry.txt`),
which is how it is graded locally.

## License

MIT — see [LICENSE](LICENSE).
