---
id: wsum-smul
title: wsum_smul
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - wsum_smul
uses:
---

# wsum_smul

## Lean type

```lean
theorem wsum_smul (x : stdSimplex 𝕜 I) (c : 𝕜) (f : I → 𝕜) : wsum x (c • f) = c * wsum x f
```

## Dependencies

- none
