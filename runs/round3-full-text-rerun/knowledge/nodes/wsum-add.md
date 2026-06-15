---
id: wsum-add
title: wsum_add
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - wsum_add
uses:
---

# wsum_add

## Lean type

```lean
theorem wsum_add (x : stdSimplex 𝕜 I) (f g : I → 𝕜) : wsum x (f + g) = wsum x f + wsum x g
```

## Dependencies

- none
