---
id: rowEval
title: rowEval
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.FourierMotzkin
  declarations:
    - rowEval
uses:
---

# rowEval

## Lean type

```lean
def rowEval {I : Type*} {n : ℕ} [Fintype I] (A : I → Fin n → 𝕜) (i : I) (x : Fin n → 𝕜) : 𝕜
```

## Dependencies

- none
