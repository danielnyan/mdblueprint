---
id: exists-xx-lam0
title: exists_xx_lam0
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.MinimaxLoomis
  declarations:
    - exists_xx_lam0
uses:
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
---

# exists_xx_lam0

## Lean type

```lean
theorem exists_xx_lam0 (A : I → J → ℝ) : ∃ xx : stdSimplex ℝ I, ∀ j, lam0 A ≤ wsum xx (fun i => A i j)
```

## Dependencies

- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
