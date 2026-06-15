---
id: roundRobinRule-isEF1
title: roundRobinRule_isEF1
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.RoundRobin
  declarations:
    - roundRobinRule_isEF1
uses:
  - IsEFX.isEF1
  - IsEF1
  - roundRobinAllocation_isEF1
---

# roundRobinRule_isEF1

## Lean type

```lean
theorem roundRobinRule_isEF1 [DecidableEq G] (I : AdditiveInstance (Fin n) G) (hnn : ∀ (i : Fin n) (g : G), 0 ≤ I.weight i g) : I.IsEF1 (roundRobinRule I).1
```

## Dependencies

- IsEFX.isEF1
- IsEF1
- roundRobinAllocation_isEF1
