---
id: wsum-wsum-comm
title: wsum_wsum_comm
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - wsum_wsum_comm
uses:
  - Profile.ext
---

# wsum_wsum_comm

## Lean type

```lean
theorem wsum_wsum_comm {J : Type*} [Fintype J] (x : stdSimplex 𝕜 I) (y : stdSimplex 𝕜 J) (A : I → J → 𝕜) : wsum x (fun i => wsum y (A i)) = wsum y (fun j => wsum x (fun i => A i j))
```

## Dependencies

- Profile.ext
