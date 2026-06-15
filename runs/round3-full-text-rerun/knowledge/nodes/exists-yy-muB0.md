---
id: exists-yy-muB0
title: exists_yy_muB0
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - exists_yy_muB0
uses:
  - IsPositive
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - By_pos
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - wsum_wsum_comm
---

# exists_yy_muB0

## Lean type

```lean
theorem exists_yy_muB0 (A B : I → J → ℝ) (hB : IsPositive B) : ∃ yy : stdSimplex ℝ J, ∀ i, Ay A yy i ≤ muB0 A B * By B yy i
```

## Dependencies

- IsPositive
- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- By_pos
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- wsum_wsum_comm
