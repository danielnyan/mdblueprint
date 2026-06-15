---
id: expectedPayoffMatrix-comm
title: expectedPayoffMatrix_comm
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - expectedPayoffMatrix_comm
uses:
  - expectedPayoffMatrix
  - wsum_wsum_comm
---

# expectedPayoffMatrix_comm

## Lean type

```lean
theorem expectedPayoffMatrix_comm {J : Type*} [Fintype J] (A : I → J → 𝕜) (x : stdSimplex 𝕜 I) (y : stdSimplex 𝕜 J) : expectedPayoffMatrix A x y = y ⬝ᵥ fun j => x ⬝ᵥ fun i => A i j
```

## Dependencies

- expectedPayoffMatrix
- wsum_wsum_comm
