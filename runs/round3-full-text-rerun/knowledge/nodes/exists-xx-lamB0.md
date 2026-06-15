---
id: exists-xx-lamB0
title: exists_xx_lamB0
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - exists_xx_lamB0
uses:
  - IsPositive
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - xB_pos
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
---

# exists_xx_lamB0

## Lean type

```lean
theorem exists_xx_lamB0 (A B : I → J → ℝ) (hB : IsPositive B) : ∃ xx : stdSimplex ℝ I, ∀ j, lamB0 A B * xB B xx j ≤ xA A xx j
```

## Dependencies

- IsPositive
- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- xB_pos
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
