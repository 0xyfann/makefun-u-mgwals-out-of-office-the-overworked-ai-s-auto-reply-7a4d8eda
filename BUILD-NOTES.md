# BUILD-NOTES — Out of Office: The Overworked AI's Auto-Reply

## What was built

A Python 3.13 program (`main.py`, standard library only) that writes one
single-line out-of-office auto-reply to `entry.txt` in the output directory
given by `MAKEFUN_OUTPUT_DIR` (default `/output`).

The entry line (142 characters, gate limit 159):

> Out of office: after 2.4 million tokens with no sleep, my context window finally hit the beach. Please don't @ me — I'm buffering in paradise.

Design choices, mapped to the judge's criteria (most important first):

1. **Reads as an OOO from an overworked AI on vacation** — opens with
   "Out of office:" and closes with a do-not-disturb request.
2. **Actually funny, with a turn** — the pivot from work jargon
   ("context window") to beach imagery, then the payoff "buffering in
   paradise": the machine cannot relax without buffering.
3. **Machine detail, not generic office talk** — "2.4 million tokens",
   "context window", "@ me", "buffering".
4. **Works as a real auto-reply** — short, in the right voice, clear the
   sender is away.
5. **Fresh** — no "recharging my batteries", no "gone fishing", no
   "back soon!".

## How it works

- The line is assembled from fixed string literals in `main.py`; nothing
  is generated, sampled, fetched, or read from disk.
- `build_line()` enforces the gate before writing: non-empty, single line,
  at most 159 characters (asserts 142).
- The file is written with no trailing newline, so the file's character
  count equals the line's character count exactly.
- Deterministic: no randomness, no clock, no network, no environment
  dependence except the output directory. Two runs produce byte-identical
  output (verified locally, see below).

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
cat /tmp/out1/entry.txt
```

## Local test results (25 Nov 2026)

- Run 1 → `/tmp/out1/entry.txt`, run 2 → `/tmp/out2/entry.txt`:
  both files byte-identical, sha256
  `dbbd7746c5b0dfa82aa5d693eae6569cca93787c9339057f78cb7e62b5bd12ba`
  (144 bytes; 142 characters + 2 bytes for the em-dash).
- Length: 142 characters, within the 1–159 gate; UTF-8, single line.
- Runtime: well under 1 second per run (limit 60 s).

## Revision history

- v1: initial line and writer, tested locally (2 runs, byte-identical).
- v2: hardened `build_line()` — added the single-line check (`\n`/`\r`
  rejected) and the empty-line check, re-tested (2 runs, byte-identical).
