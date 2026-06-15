---
id: wsum-const
title: wsum_const
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - wsum_const
uses:
---

# wsum_const

## Lean type

```lean
theorem wsum_const (x : stdSimplex 𝕜 I) (c : 𝕜) : wsum x (fun _ => c) = c
```

## Dependencies

- none
