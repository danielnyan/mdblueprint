---
id: lcs
title: lcs
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CostM.LCS
  declarations:
    - lcs
uses:
  - Visited
  - stdSimplex.pure
  - Lottery.pure
---

# lcs

## Lean type

```lean
def lcs : List A → List A → CostM (Visited (ℕ × ℕ)) ℕ | [], ys => do CostM.tick (Visited.singleton (0, ys.length)) pure 0 | x :: xs, [] => do CostM.tick (Visited.singleton (xs.length + 1, 0)) pure 0 | x :: xs, y :: ys => if x = y then do CostM.tick (Visited.singleton (xs.length + 1, ys.length + 1)) let r ← lcs xs ys pure (r + 1) else do CostM.tick (Visited.singleton (xs.length + 1, ys.length + 1)) let r1 ← lcs xs (y :: ys) let r2 ← lcs (x :: xs) ys pure (max r1 r2) /-- Monotonicity helper: enlarging both arguments of `Finset.range` preserves the `×ˢ` containment. -/ private lemma range_prod_mono {a a' b b' : ℕ} (ha : a ≤ a') (hb : b ≤ b') : Finset.range a ×ˢ Finset.range b ⊆ Finset.range a' ×ˢ Finset.range b'
```

## Dependencies

- Visited
- stdSimplex.pure
- Lottery.pure
