---
id: fm-cert-lift
title: fm_cert_lift
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.FourierMotzkin
  declarations:
    - fm_cert_lift
uses:
  - HasCertificate
  - fmA
  - fmB
  - liftCert
  - liftCert_nonneg
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - feas_cert_disjoint
  - rowEval
  - feasible_of_fm_feasible
---

# fm_cert_lift

## Lean type

```lean
theorem fm_cert_lift (A : I → Fin (n+1) → 𝕜) (b : I → 𝕜) (hred : HasCertificate (fmA A) (fmB A b)) : HasCertificate A b
```

## Dependencies

- HasCertificate
- fmA
- fmB
- liftCert
- liftCert_nonneg
- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- feas_cert_disjoint
- rowEval
- feasible_of_fm_feasible
