---
id: eliminateAllCycles-acyclic
title: eliminateAllCycles_acyclic
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - eliminateAllCycles_acyclic
uses:
  - Valuation
  - Allocation
  - hasEnvyCycle
  - eliminateAllCycles_unfold
  - rotateBundles_paretoDomCount_lt
---

# eliminateAllCycles_acyclic

## Lean type

```lean
lemma eliminateAllCycles_acyclic (v : Valuation N G) (A : Allocation N G) : ¬ hasEnvyCycle v (eliminateAllCycles v A)
```

## Dependencies

- Valuation
- Allocation
- hasEnvyCycle
- eliminateAllCycles_unfold
- rotateBundles_paretoDomCount_lt
