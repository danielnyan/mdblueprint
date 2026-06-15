---
id: mu-aux-continuous
title: mu.aux.continuous
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.MinimaxLoomis
  declarations:
    - mu.aux.continuous
uses:
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - wsum_continuous
---

# mu.aux.continuous

## Lean type

```lean
theorem mu.aux.continuous (A : I → J → ℝ) : Continuous (mu.aux A)
```

## Dependencies

- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- wsum_continuous
