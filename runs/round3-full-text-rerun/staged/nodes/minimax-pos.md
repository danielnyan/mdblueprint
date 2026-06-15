---
id: minimax-pos
title: minimax_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Minimax
  declarations:
    - minimax_pos
uses:
  - skew_optimal
  - symMat
  - symMat_skew
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
---

# minimax_pos

## Lean type

```lean
theorem minimax_pos (A : I → J → 𝕜) (hA : ∀ i j, 0 < A i j) : ∃ (x : I → 𝕜) (y : J → 𝕜) (v : 𝕜), (∀ i, 0 ≤ x i) ∧ (∑ i, x i = 1) ∧ (∀ j, 0 ≤ y j) ∧ (∑ j, y j = 1) ∧ (∀ j, v ≤ ∑ i, x i * A i j) ∧ (∀ i, ∑ j, A i j * y j ≤ v)
```

## Dependencies

- skew_optimal
- symMat
- symMat_skew
- IsPositiveAffineOf.symm
- Indifferent.symm
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
