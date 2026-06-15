---
id: HasCertificate
title: HasCertificate
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.FourierMotzkin
  declarations:
    - HasCertificate
uses:
  - IsCertificate
---

# HasCertificate

## Lean type

```lean
def HasCertificate {I : Type*} {n : ℕ} [Fintype I] (A : I → Fin n → 𝕜) (b : I → 𝕜) : Prop
```

## Dependencies

- IsCertificate
