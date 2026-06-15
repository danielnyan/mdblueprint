---
id: colRatio-continuous
title: colRatio.continuous
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - colRatio.continuous
uses:
  - IsPositive
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - wsum_continuous
  - xB_pos
---

# colRatio.continuous

## Lean type

```lean
theorem colRatio.continuous {A B : I → J → ℝ} (hB : IsPositive B) (j : J) : Continuous (fun x : stdSimplex ℝ I => colRatio A B x j)
```

## Dependencies

- IsPositive
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- wsum_continuous
- xB_pos
