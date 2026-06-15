---
id: muB-aux-bddBelow
title: muB.aux.bddBelow
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - muB.aux.bddBelow
uses:
  - IsPositive
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - mu.aux.bddBelow
---

# muB.aux.bddBelow

## Lean type

```lean
theorem muB.aux.bddBelow {A B : I → J → ℝ} (hB : IsPositive B) : ∃ C, ∀ y, C ≤ muB.aux A B y
```

## Dependencies

- IsPositive
- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- mu.aux.bddBelow
