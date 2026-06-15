---
id: lamB-aux-continuous
title: lamB.aux.continuous
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - lamB.aux.continuous
uses:
  - IsPositive
  - colRatio.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
---

# lamB.aux.continuous

## Lean type

```lean
theorem lamB.aux.continuous {A B : I → J → ℝ} (hB : IsPositive B) : Continuous (lamB.aux A B)
```

## Dependencies

- IsPositive
- colRatio.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
