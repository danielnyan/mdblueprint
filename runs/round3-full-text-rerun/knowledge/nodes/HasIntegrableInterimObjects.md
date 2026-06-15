---
id: HasIntegrableInterimObjects
title: HasIntegrableInterimObjects
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - HasIntegrableInterimObjects
uses:
  - HasIntegrableInterimAllocation
  - HasIntegrableInterimPayment
---

# HasIntegrableInterimObjects

## Lean type

```lean
def HasIntegrableInterimObjects (A : BayesianSingleItemAuction I) : Prop
```

## Dependencies

- HasIntegrableInterimAllocation
- HasIntegrableInterimPayment
