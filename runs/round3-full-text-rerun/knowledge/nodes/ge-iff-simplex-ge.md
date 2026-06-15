---
id: ge-iff-simplex-ge
title: ge_iff_simplex_ge
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - ge_iff_simplex_ge
uses:
  - wsum_const
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - wsum_le_wsum
  - stdSimplex.pure
  - Lottery.pure
---

# ge_iff_simplex_ge

## Lean type

```lean
theorem ge_iff_simplex_ge {f : I → 𝕜} {v : 𝕜} : (∀ i, v ≤ f i) ↔ ∀ x : stdSimplex 𝕜 I, v ≤ wsum x f
```

## Dependencies

- wsum_const
- IsPositiveAffineOf.symm
- Indifferent.symm
- wsum_le_wsum
- stdSimplex.pure
- Lottery.pure
