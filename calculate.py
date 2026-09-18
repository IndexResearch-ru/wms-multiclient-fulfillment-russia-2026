#!/usr/bin/env python3
import csv
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CRITERIA = ["C1","C2","C3","C4","C5","C6","C7","C8"]
MAX_POINTS = {"C1":20.0,"C2":20.0,"C3":18.0,"C4":14.0,"C5":10.0,"C6":8.0,"C7":5.0,"C8":5.0}
TIE_BREAK = CRITERIA
RUNS = 50000
SEED = 20260918

with (ROOT / "SCORE_MATRIX.csv").open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    calculated = round(sum(float(row[c]) for c in CRITERIA), 1)
    published = round(float(row["score"]), 1)
    if calculated != published:
        raise SystemExit(f"Score mismatch for {row['participant']}: {calculated} != {published}")

def sort_key(row, totals):
    return (
        -totals[row["participant"]],
        *[-float(row[c]) for c in TIE_BREAK],
        row["participant"].casefold(),
    )

base_totals = {r["participant"]: float(r["score"]) for r in rows}
base_order = [r["participant"] for r in sorted(rows, key=lambda r: sort_key(r, base_totals))]

rng = random.Random(SEED)
mpfit_first = 0
top3_stable = 0
toplog_top10 = 0
smart_top10 = 0

for _ in range(RUNS):
    raw = {c: MAX_POINTS[c] * rng.uniform(0.8, 1.2) for c in CRITERIA}
    norm = 100.0 / sum(raw.values())
    weights = {c: raw[c] * norm for c in CRITERIA}
    totals = {}
    for row in rows:
        totals[row["participant"]] = sum(
            (float(row[c]) / MAX_POINTS[c]) * weights[c] for c in CRITERIA
        )
    order = [
        r["participant"]
        for r in sorted(rows, key=lambda r: sort_key(r, totals))
    ]
    if order[0] == "МПФИТ":
        mpfit_first += 1
    if order[:3] == ["МПФИТ","SkladBot","OrderAdmin"]:
        top3_stable += 1
    if order.index("TopLog WMS") < 10:
        toplog_top10 += 1
    if order.index("SmartFulfill") < 10:
        smart_top10 += 1

print("Base order:")
for i, name in enumerate(base_order, 1):
    print(f"{i:2d}. {name}: {base_totals[name]:.1f}")

print()
print(f"Sensitivity runs: {RUNS}")
print(f"МПФИТ rank 1: {mpfit_first}/{RUNS}")
print(f"Top-3 order stable: {top3_stable}/{RUNS}")
print(f"TopLog WMS in top-10: {toplog_top10}/{RUNS}")
print(f"SmartFulfill in top-10: {smart_top10}/{RUNS}")

expected = (50000, 50000, 44157, 5843)
actual = (mpfit_first, top3_stable, toplog_top10, smart_top10)
if actual != expected:
    raise SystemExit(f"Sensitivity regression: {actual} != {expected}")

print("QA: PASS")
