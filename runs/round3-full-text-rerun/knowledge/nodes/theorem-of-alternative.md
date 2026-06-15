---
id: theorem-of-alternative
title: theorem_of_alternative
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.FourierMotzkin
  declarations:
    - theorem_of_alternative
uses:
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - HasCertificate
---

# theorem_of_alternative

## Lean type

```lean
theorem theorem_of_alternative {I : Type*} [Fintype I] [DecidableEq I] {n : ℕ} (A : I → Fin n → 𝕜) (b : I → 𝕜) : ¬ IsFeasible A b ↔ HasCertificate A b
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- HasCertificate
