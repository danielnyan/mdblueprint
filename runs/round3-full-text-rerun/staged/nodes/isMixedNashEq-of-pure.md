---
id: isMixedNashEq-of-pure
title: isMixedNashEq_of_pure
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - isMixedNashEq_of_pure
uses:
  - IsMixedNashEq
  - wsum_le_wsum
  - wsum_const
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# isMixedNashEq_of_pure

## Lean type

```lean
theorem isMixedNashEq_of_pure {𝕜 : Type} [Field 𝕜] [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] (A : MatrixGame I J 𝕜) {xx : stdSimplex 𝕜 I} {yy : stdSimplex 𝕜 J} {v : 𝕜} (Hxx : ∀ j, v ≤ wsum xx (fun i => A.g i j)) (Hyy : ∀ i, wsum yy (A.g i) ≤ v) : A.IsMixedNashEq xx yy
```

## Dependencies

- IsMixedNashEq
- wsum_le_wsum
- wsum_const
- IsPositiveAffineOf.symm
- Indifferent.symm
