---
id: eliminateAllCycles-eq-of-acyclic
title: eliminateAllCycles_eq_of_acyclic
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - eliminateAllCycles_eq_of_acyclic
uses:
  - Valuation
  - Allocation
  - hasEnvyCycle
  - eliminateAllCycles_unfold
---

# eliminateAllCycles_eq_of_acyclic

## Lean type

```lean
lemma eliminateAllCycles_eq_of_acyclic (v : Valuation N G) (A : Allocation N G) (h : ¬ hasEnvyCycle v A) : eliminateAllCycles v A = A
```

## Dependencies

- Valuation
- Allocation
- hasEnvyCycle
- eliminateAllCycles_unfold
