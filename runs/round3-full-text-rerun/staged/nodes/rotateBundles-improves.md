---
id: rotateBundles-improves
title: rotateBundles_improves
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - rotateBundles_improves
uses:
  - Valuation
  - Allocation
  - isEnvyCycle
  - rotateBundles_mem
---

# rotateBundles_improves

## Lean type

```lean
lemma rotateBundles_improves (v : Valuation N G) (A : Allocation N G) (l : List N) (hcyc : isEnvyCycle v A l) (i : N) (hi : i ∈ l) : v.val i (A i) < v.val i (rotateBundles A l i)
```

## Dependencies

- Valuation
- Allocation
- isEnvyCycle
- rotateBundles_mem
