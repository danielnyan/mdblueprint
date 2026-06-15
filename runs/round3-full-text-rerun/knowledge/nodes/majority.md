---
id: majority
title: majority
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.BoyerMoore
  declarations:
    - majority
uses:
  - stdSimplex.pure
  - Lottery.pure
---

# majority

## Lean type

```lean
def majority : List A → CostM Cells (Option A) | [] => pure none | x :: xs => do ✓[Cells.alloc 2] do let result ← loop x 1 xs ✓[Cells.free 2] pure result where /-- Single-pass loop carrying the current candidate and counter as parameters — no allocation, no ticks. -/ loop (cand : A) (cnt : ℕ) : List A → CostM Cells (Option A) | [] => pure (some cand) | y :: ys => if y = cand then loop cand (cnt + 1) ys else if cnt = 0 then loop y 1 ys else loop cand (cnt - 1) ys /-- The loop has zero cost: it overwrites the two slots without allocating. -/
```

## Dependencies

- stdSimplex.pure
- Lottery.pure
