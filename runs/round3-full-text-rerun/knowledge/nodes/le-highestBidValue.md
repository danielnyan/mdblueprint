---
id: le-highestBidValue
title: le_highestBidValue
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - le_highestBidValue
uses:
---

# le_highestBidValue

## Lean type

```lean
lemma le_highestBidValue (b : I → Nat) (i : I) : b i ≤ highestBidValue b
```

## Dependencies

- none
