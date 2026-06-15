---
id: muB-aux-continuous
title: muB.aux.continuous
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - muB.aux.continuous
uses:
  - IsPositive
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - mu.aux.continuous
---

# muB.aux.continuous

## Lean type

```lean
theorem muB.aux.continuous {A B : I → J → ℝ} (hB : IsPositive B) : Continuous (muB.aux A B)
```

## Dependencies

- IsPositive
- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- mu.aux.continuous
