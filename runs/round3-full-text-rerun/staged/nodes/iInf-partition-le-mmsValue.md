---
id: iInf-partition-le-mmsValue
title: iInf_partition_le_mmsValue
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.MMS
  declarations:
    - iInf_partition_le_mmsValue
uses:
  - Valuation
  - Allocation
  - lamB.aux.bddAbove
  - lam.aux.bddAbove
---

# iInf_partition_le_mmsValue

## Lean type

```lean
lemma iInf_partition_le_mmsValue (v : Valuation N G) (allGoods : Finset G) (i : N) (B : Allocation N G) (hB : IsAllocation allGoods B) (hbdd : BddAbove (Set.range fun X : {A : Allocation N G // IsAllocation allGoods A} => iInf fun j : N => v.val i (X.val j))) : iInf (fun j : N => v.val i (B j)) ≤ mmsValue v allGoods i
```

## Dependencies

- Valuation
- Allocation
- lamB.aux.bddAbove
- lam.aux.bddAbove
