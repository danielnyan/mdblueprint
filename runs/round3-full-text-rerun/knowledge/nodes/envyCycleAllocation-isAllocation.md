---
id: envyCycleAllocation-isAllocation
title: envyCycleAllocation_isAllocation
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - envyCycleAllocation_isAllocation
uses:
---

# envyCycleAllocation_isAllocation

## Lean type

```lean
theorem envyCycleAllocation_isAllocation [Fintype N] [Fintype G] [Nonempty N] [DecidableEq N] [DecidableEq G] (I : AdditiveInstance N G) : IsAllocation I.allGoods (envyCycleAllocation I)
```

## Dependencies

- none
