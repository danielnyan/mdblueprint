---
id: roundRobinAllocation-isAllocation
title: roundRobinAllocation_isAllocation
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.RoundRobin
  declarations:
    - roundRobinAllocation_isAllocation
uses:
---

# roundRobinAllocation_isAllocation

## Lean type

```lean
theorem roundRobinAllocation_isAllocation [DecidableEq G] (I : AdditiveInstance (Fin n) G) : IsAllocation I.allGoods (roundRobinAllocation I)
```

## Dependencies

- none
