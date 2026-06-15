---
id: dpSolveList-supportedOn
title: dpSolveList_supportedOn
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - dpSolveList_supportedOn
uses:
  - supportedOn
  - dpSolveList
  - natBinarySocialWelfare
---

# dpSolveList_supportedOn

## Lean type

```lean
lemma dpSolveList_supportedOn (w b : I → Nat) : ∀ items capacity, supportedOn items (dpSolveList w b items capacity)
```

## Dependencies

- supportedOn
- dpSolveList
- natBinarySocialWelfare
