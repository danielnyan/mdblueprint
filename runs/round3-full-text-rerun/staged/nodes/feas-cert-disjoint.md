---
id: feas-cert-disjoint
title: feas_cert_disjoint
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.FourierMotzkin
  declarations:
    - feas_cert_disjoint
uses:
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - HasCertificate
  - rowEval
---

# feas_cert_disjoint

## Lean type

```lean
theorem feas_cert_disjoint {I : Type*} {n : ℕ} [Fintype I] (A : I → Fin n → 𝕜) (b : I → 𝕜) (hfeas : IsFeasible A b) (hcert : HasCertificate A b) : False
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- HasCertificate
- rowEval
