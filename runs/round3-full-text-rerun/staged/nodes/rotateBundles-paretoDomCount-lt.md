---
id: rotateBundles-paretoDomCount-lt
title: rotateBundles_paretoDomCount_lt
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - rotateBundles_paretoDomCount_lt
uses:
  - Valuation
  - Allocation
  - isEnvyCycle
  - paretoDomSet_subset
  - rotateBundles_nondecreasing
  - self_mem_paretoDomSet
  - not_mem_paretoDomSet_of_strict
  - rotateBundles_improves
  - hasEnvyCycle
---

# rotateBundles_paretoDomCount_lt

## Lean type

```lean
lemma rotateBundles_paretoDomCount_lt [Fintype N] [Fintype G] [DecidableEq N] (v : Valuation N G) (A : Allocation N G) (l : List N) (hcyc : isEnvyCycle v A l) : paretoDomCount v (rotateBundles A l) < paretoDomCount v A
```

## Dependencies

- Valuation
- Allocation
- isEnvyCycle
- paretoDomSet_subset
- rotateBundles_nondecreasing
- self_mem_paretoDomSet
- not_mem_paretoDomSet_of_strict
- rotateBundles_improves
- hasEnvyCycle
