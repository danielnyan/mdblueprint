---
id: dpSolveList-optimal
title: dpSolveList_optimal
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - dpSolveList_optimal
uses:
  - BinaryAllocation
  - supportedOn
  - natBinaryLoad
  - natBinarySocialWelfare
  - dpSolveList
  - supportedOn_nil_iff
  - supportedOn_update_false
  - natBinaryLoad_eq_add_of_true
  - eq_false_of_supportedOn_of_not_mem
  - dpSolveList_supportedOn
  - natBinarySocialWelfare_eq_add_of_true
  - natBinarySocialWelfare_update_true_of_false
  - supportedOn_tail_of_eq_false
---

# dpSolveList_optimal

## Lean type

```lean
lemma dpSolveList_optimal (w b : I → Nat) : ∀ (items : List I), items.Nodup → ∀ capacity {x : BinaryAllocation I}, supportedOn items x → natBinaryLoad w x ≤ capacity → natBinarySocialWelfare b x ≤ natBinarySocialWelfare b (dpSolveList w b items capacity)
```

## Dependencies

- BinaryAllocation
- supportedOn
- natBinaryLoad
- natBinarySocialWelfare
- dpSolveList
- supportedOn_nil_iff
- supportedOn_update_false
- natBinaryLoad_eq_add_of_true
- eq_false_of_supportedOn_of_not_mem
- dpSolveList_supportedOn
- natBinarySocialWelfare_eq_add_of_true
- natBinarySocialWelfare_update_true_of_false
- supportedOn_tail_of_eq_false
