---
id: rowRatio-continuous
title: rowRatio.continuous
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - rowRatio.continuous
uses:
  - IsPositive
  - colRatio.continuous
  - lamB.aux.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - wsum_continuous
  - By_pos
---

# rowRatio.continuous

## Lean type

```lean
theorem rowRatio.continuous {A B : I → J → ℝ} (hB : IsPositive B) (i : I) : Continuous (fun y : stdSimplex ℝ J => rowRatio A B y i)
```

## Dependencies

- IsPositive
- colRatio.continuous
- lamB.aux.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- wsum_continuous
- By_pos
