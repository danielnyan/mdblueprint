---
id: lamB-aux-bddAbove
title: lamB.aux.bddAbove
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - lamB.aux.bddAbove
uses:
  - IsPositive
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - lam.aux.bddAbove
---

# lamB.aux.bddAbove

## Lean type

```lean
theorem lamB.aux.bddAbove {A B : I → J → ℝ} (hB : IsPositive B) : ∃ C, ∀ x, lamB.aux A B x ≤ C
```

## Dependencies

- IsPositive
- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- lam.aux.bddAbove
