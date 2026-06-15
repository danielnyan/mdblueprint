---
id: wsum-ge-wsum
title: wsum_ge_wsum
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - wsum_ge_wsum
uses:
  - wsum_le_wsum
---

# wsum_ge_wsum

## Lean type

```lean
theorem wsum_ge_wsum (x : stdSimplex 𝕜 I) {f g : I → 𝕜} (h : ∀ i, f i ≥ g i) : wsum x f ≥ wsum x g
```

## Dependencies

- wsum_le_wsum
