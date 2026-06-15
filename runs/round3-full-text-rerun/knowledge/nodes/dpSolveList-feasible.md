---
id: dpSolveList-feasible
title: dpSolveList_feasible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - dpSolveList_feasible
uses:
  - natBinaryLoad
  - dpSolveList
  - eq_false_of_supportedOn_of_not_mem
  - dpSolveList_supportedOn
  - natBinarySocialWelfare
  - natBinaryLoad_update_true_of_false
---

# dpSolveList_feasible

## Lean type

```lean
lemma dpSolveList_feasible (w b : I → Nat) : ∀ items, items.Nodup → ∀ capacity, natBinaryLoad w (dpSolveList w b items capacity) ≤ capacity
```

## Dependencies

- natBinaryLoad
- dpSolveList
- eq_false_of_supportedOn_of_not_mem
- dpSolveList_supportedOn
- natBinarySocialWelfare
- natBinaryLoad_update_true_of_false
