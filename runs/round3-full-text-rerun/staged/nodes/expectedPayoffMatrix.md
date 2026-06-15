---
id: expectedPayoffMatrix
title: expectedPayoffMatrix
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - expectedPayoffMatrix
uses:
---

# expectedPayoffMatrix

## Lean type

```lean
def expectedPayoffMatrix (A : I → J → 𝕜) [Fintype J] (x : stdSimplex 𝕜 I) (y : stdSimplex 𝕜 J) : 𝕜
```

## Dependencies

- none
