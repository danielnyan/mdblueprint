---
id: IsCertificate
title: IsCertificate
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.FourierMotzkin
  declarations:
    - IsCertificate
uses:
---

# IsCertificate

## Lean type

```lean
def IsCertificate {I : Type*} {n : ℕ} [Fintype I] (A : I → Fin n → 𝕜) (b : I → 𝕜) (u : I → 𝕜) : Prop
```

## Dependencies

- none
