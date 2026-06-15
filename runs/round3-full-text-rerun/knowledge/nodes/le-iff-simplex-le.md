---
id: le-iff-simplex-le
title: le_iff_simplex_le
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - le_iff_simplex_le
uses:
  - wsum_le_wsum
  - wsum_const
  - stdSimplex.pure
  - Lottery.pure
---

# le_iff_simplex_le

## Lean type

```lean
theorem le_iff_simplex_le {f : I → 𝕜} {v : 𝕜} : (∀ i, f i ≤ v) ↔ ∀ x : stdSimplex 𝕜 I, wsum x f ≤ v
```

## Dependencies

- wsum_le_wsum
- wsum_const
- stdSimplex.pure
- Lottery.pure
