---
id: eliminateAllCycles-nondecreasing
title: eliminateAllCycles_nondecreasing
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - eliminateAllCycles_nondecreasing
uses:
  - Valuation
  - Allocation
  - eliminateAllCycles_unfold
  - rotateBundles_nondecreasing
  - rotateBundles_paretoDomCount_lt
---

# eliminateAllCycles_nondecreasing

## Lean type

```lean
lemma eliminateAllCycles_nondecreasing [DecidableEq G] (v : Valuation N G) (A : Allocation N G) (i : N) : v.val i (A i) ≤ v.val i (eliminateAllCycles v A i)
```

## Dependencies

- Valuation
- Allocation
- eliminateAllCycles_unfold
- rotateBundles_nondecreasing
- rotateBundles_paretoDomCount_lt
