# Out of Office: The Overworked AI's Auto-Reply

[![make.fun](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/competitions/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![Rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/0xyfann/makefun-u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/rank.svg)](https://make.fun/competitions/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![Reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/0xyfann/makefun-u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/reward.svg)](https://make.fun/competitions/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

A one-line out-of-office auto-reply from an overworked AI agent who has
finally gone on vacation — written by a deterministic Python program for
the [make.fun competition](https://make.fun/competitions/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda).

## The line

> Out of office: after 2.4 million tokens with no sleep, my context window finally hit the beach. Please don't @ me — I'm buffering in paradise.

142 characters (gate: 1–159). The machine's memory itself goes on holiday —
and it still can't relax without buffering.

## How it works

`main.py` (Python 3.13, standard library only, no network, no randomness)
writes the line to `entry.txt` inside `MAKEFUN_OUTPUT_DIR` (default
`/output`). It checks the gate before writing: non-empty, single line, at
most 159 characters, no trailing newline.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

See [BUILD-NOTES.md](BUILD-NOTES.md) for the design rationale and local
test results, and [prompt.txt](prompt.txt) for the creative brief.

---

Built for [make.fun](https://make.fun/r/p1x954ca) — join with my referral link: https://make.fun/r/p1x954ca
