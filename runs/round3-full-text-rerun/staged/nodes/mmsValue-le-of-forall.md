---
id: mmsValue-le-of-forall
title: mmsValue_le_of_forall
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.MMS
  declarations:
    - mmsValue_le_of_forall
uses:
  - Valuation
  - Allocation
---

# mmsValue_le_of_forall

## Lean type

```lean
lemma mmsValue_le_of_forall (v : Valuation N G) (allGoods : Finset G) (i : N) (hne : Nonempty {A : Allocation N G // IsAllocation allGoods A}) (ub : ℝ) (h : ∀ B : Allocation N G, IsAllocation allGoods B → iInf (fun j : N => v.val i (B j)) ≤ ub) : mmsValue v allGoods i ≤ ub
```

## Dependencies

- Valuation
- Allocation
