---
id: dpSolveList
title: dpSolveList
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - dpSolveList
uses:
  - BinaryAllocation
  - natBinarySocialWelfare
---

# dpSolveList

## Lean type

```lean
def dpSolveList (w b : I → Nat) : List I → Nat → BinaryAllocation I | [], _ => fun _ => false | i :: is, capacity => if w i ≤ capacity then let skip
```

## Dependencies

- BinaryAllocation
- natBinarySocialWelfare
