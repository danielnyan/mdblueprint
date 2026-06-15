---
id: dynamicProgrammingOptimalAllocation-fractionalFeasible
title: dynamicProgrammingOptimalAllocation_fractionalFeasible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - dynamicProgrammingOptimalAllocation_fractionalFeasible
uses:
  - natAuctionData
  - fractionalFeasible
  - binaryToAllocation
  - dynamicProgrammingOptimalAllocation_feasible
  - natBinaryLoad
---

# dynamicProgrammingOptimalAllocation_fractionalFeasible

## Lean type

```lean
lemma dynamicProgrammingOptimalAllocation_fractionalFeasible (w b : I → Nat) (capacity : Nat) : (natAuctionData w capacity).fractionalFeasible (binaryToAllocation (dynamicProgrammingOptimalAllocation w b capacity))
```

## Dependencies

- natAuctionData
- fractionalFeasible
- binaryToAllocation
- dynamicProgrammingOptimalAllocation_feasible
- natBinaryLoad
