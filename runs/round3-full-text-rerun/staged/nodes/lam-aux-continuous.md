---
id: lam-aux-continuous
title: lam.aux.continuous
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.MinimaxLoomis
  declarations:
    - lam.aux.continuous
uses:
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - wsum_continuous
---

# lam.aux.continuous

## Lean type

```lean
theorem lam.aux.continuous (A : I → J → ℝ) : Continuous (lam.aux A)
```

## Dependencies

- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- muB.aux.continuous
- mu.aux.continuous
- wsum_continuous
