---
id: findSource-isSource
title: findSource_isSource
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - findSource_isSource
uses:
  - Valuation
  - Allocation
  - hasEnvyCycle
  - isSource
  - acyclic_has_source
  - eliminateAllCycles_acyclic
  - toValuation
  - isEnvyCycle
  - toFinset
  - Profile.ext
  - eliminateAllCycles_isAllocation
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - rotateBundles_mem
  - rotateBundles_not_mem
  - eliminateAllCycles_unfold
  - rotateBundles_paretoDomCount_lt
  - IsEFX.isEF1
  - IsEF1
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - eliminateAllCycles_nondecreasing
---

# findSource_isSource

## Lean type

```lean
lemma findSource_isSource [Fintype N] [Nonempty N] (v : Valuation N G) (A : Allocation N G) (hdag : ¬ hasEnvyCycle v A) : isSource v A (findSource v A hdag)
```

## Dependencies

- Valuation
- Allocation
- hasEnvyCycle
- isSource
- acyclic_has_source
- eliminateAllCycles_acyclic
- toValuation
- isEnvyCycle
- toFinset
- Profile.ext
- eliminateAllCycles_isAllocation
- IsPositiveAffineOf.symm
- Indifferent.symm
- rotateBundles_mem
- rotateBundles_not_mem
- eliminateAllCycles_unfold
- rotateBundles_paretoDomCount_lt
- IsEFX.isEF1
- IsEF1
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- eliminateAllCycles_nondecreasing
