---
id: wsum-le-wsum
title: wsum_le_wsum
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - wsum_le_wsum
uses:
---

# wsum_le_wsum

## Lean type

```lean
theorem wsum_le_wsum (x : stdSimplex 𝕜 I) {f g : I → 𝕜} (h : ∀ i, f i ≤ g i) : wsum x f ≤ wsum x g
```

## Dependencies

- none
