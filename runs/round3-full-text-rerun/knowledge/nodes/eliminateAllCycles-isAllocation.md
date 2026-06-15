---
id: eliminateAllCycles-isAllocation
title: eliminateAllCycles_isAllocation
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - eliminateAllCycles_isAllocation
uses:
  - Valuation
  - Allocation
  - hasEnvyCycle
  - eliminateAllCycles_unfold
  - rotateBundles_isAllocation
  - rotateBundles_paretoDomCount_lt
---

# eliminateAllCycles_isAllocation

## Lean type

```lean
lemma eliminateAllCycles_isAllocation [DecidableEq G] (v : Valuation N G) {allGoods : Finset G} {A : Allocation N G} (hA : IsAllocation allGoods A) : IsAllocation allGoods (eliminateAllCycles v A)
```

## Dependencies

- Valuation
- Allocation
- hasEnvyCycle
- eliminateAllCycles_unfold
- rotateBundles_isAllocation
- rotateBundles_paretoDomCount_lt
