#!/usr/bin/env python3
"""Check the deals in src/deals.md and print them as PBN: python3 deals.py

Each deal must be four hands of 13 making 52 distinct cards.  The output feeds
a double-dummy solver, e.g. `python3 deals.py | cargo run --example solve-pbn`
in ../dds-bridge.  The HCP of W N E S go to stderr.
"""
import re
import sys

HCP = {"A": 4, "K": 3, "Q": 2, "J": 1}

for n, row in enumerate(re.findall(r"^\| ♠.*$", open("src/deals.md").read(), re.M), 1):
    hands = []
    for cell in row.strip("|").split("|"):
        suits = [re.findall(r"10|[AKQJ2-9]", s) for s in re.split(r"[♠♥♦♣]", cell)[1:]]
        assert len(suits) == 4 and sum(map(len, suits)) == 13, f"deal {n}: {cell.strip()}"
        hands.append(suits)
    cards = {(i, r) for hand in hands for i, suit in enumerate(hand) for r in suit}
    assert len(cards) == 52, f"deal {n}: duplicate card"
    w, north, e, s = (".".join("".join(suit).replace("10", "T") for suit in h) for h in hands)
    print(f'[Deal "N:{north} {e} {s} {w}"]')
    print(n, *(sum(HCP.get(r, 0) for suit in h for r in suit) for h in hands), file=sys.stderr)
