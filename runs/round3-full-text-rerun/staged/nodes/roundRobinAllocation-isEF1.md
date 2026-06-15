---
id: roundRobinAllocation-isEF1
title: roundRobinAllocation_isEF1
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.RoundRobin
  declarations:
    - roundRobinAllocation_isEF1
uses:
  - IsEFX.isEF1
  - IsEF1
  - toValuation
  - toAdditiveValuation
---

# roundRobinAllocation_isEF1

## Lean type

```lean
theorem roundRobinAllocation_isEF1 [DecidableEq G] (I : AdditiveInstance (Fin n) G) (hnn : ∀ (i : Fin n) (g : G), 0 ≤ I.weight i g) : I.IsEF1 (roundRobinAllocation I)
```

## Dependencies

- IsEFX.isEF1
- IsEF1
- toValuation
- toAdditiveValuation
