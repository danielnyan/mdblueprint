---
id: not-paretoImproved-self
title: not_paretoImproved_self
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Efficiency
  declarations:
    - not_paretoImproved_self
uses:
  - Allocation
---

# not_paretoImproved_self

## Lean type

```lean
lemma not_paretoImproved_self (A : Allocation N G) : ¬ (IsAllocation allGoods A ∧ (∀ i, v.val i (A i) ≤ v.val i (A i)) ∧ ∃ i, v.val i (A i) < v.val i (A i))
```

## Dependencies

- Allocation
