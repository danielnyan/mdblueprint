---
id: liftCoeff
title: liftCoeff
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.FourierMotzkin
  declarations:
    - liftCoeff
uses:
  - FMRowIndex
---

# liftCoeff

## Lean type

```lean
def liftCoeff (A : I → Fin (n+1) → 𝕜) (idx : FMRowIndex A) (i : I) : 𝕜
```

## Dependencies

- FMRowIndex
