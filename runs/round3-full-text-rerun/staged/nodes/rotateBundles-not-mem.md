---
id: rotateBundles-not-mem
title: rotateBundles_not_mem
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - rotateBundles_not_mem
uses:
  - Allocation
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# rotateBundles_not_mem

## Lean type

```lean
lemma rotateBundles_not_mem (A : Allocation N G) (l : List N) (i : N) (h : i ∉ l) : rotateBundles A l i = A i
```

## Dependencies

- Allocation
- IsPositiveAffineOf.symm
- Indifferent.symm
