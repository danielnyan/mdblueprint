---
id: mechanism-payment-of-allocation-ne-some
title: mechanism_payment_of_allocation_ne_some
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.ReserveVickrey
  declarations:
    - mechanism_payment_of_allocation_ne_some
uses:
  - Allocation
---

# mechanism_payment_of_allocation_ne_some

## Lean type

```lean
lemma mechanism_payment_of_allocation_ne_some {reserve : U} {b : I → U} {i : I} (halloc : allocation reserve b ≠ some i) : (mechanism reserve).paymentRule b i = 0
```

## Dependencies

- Allocation
