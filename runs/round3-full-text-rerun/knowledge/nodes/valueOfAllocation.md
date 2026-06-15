---
id: valueOfAllocation
title: valueOfAllocation
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Transfer
  declarations:
    - valueOfAllocation
uses:
  - Valuation
---

# valueOfAllocation

## Lean type

```lean
def valueOfAllocation (a : A) (types : ∀ _ : I, Valuation A V) (i : I) : V
```

## Dependencies

- Valuation
