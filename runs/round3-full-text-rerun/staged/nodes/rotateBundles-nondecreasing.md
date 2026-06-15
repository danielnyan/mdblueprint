---
id: rotateBundles-nondecreasing
title: rotateBundles_nondecreasing
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - rotateBundles_nondecreasing
uses:
  - Valuation
  - Allocation
  - isEnvyCycle
  - rotateBundles_improves
  - rotateBundles_not_mem
---

# rotateBundles_nondecreasing

## Lean type

```lean
lemma rotateBundles_nondecreasing (v : Valuation N G) (A : Allocation N G) (l : List N) (hcyc : isEnvyCycle v A l) (i : N) : v.val i (A i) ≤ v.val i (rotateBundles A l i)
```

## Dependencies

- Valuation
- Allocation
- isEnvyCycle
- rotateBundles_improves
- rotateBundles_not_mem
