---
id: liftCert
title: liftCert
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.FourierMotzkin
  declarations:
    - liftCert
uses:
  - FMRowIndex
  - liftCoeff
---

# liftCert

## Lean type

```lean
def liftCert (A : I → Fin (n+1) → 𝕜) (u' : FMRowIndex A → 𝕜) (i : I) : 𝕜
```

## Dependencies

- FMRowIndex
- liftCoeff
