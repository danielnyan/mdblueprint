---
id: mechanism-payment-eq-zero-of-allocation-eq-none
title: mechanism_payment_eq_zero_of_allocation_eq_none
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.ReserveVickrey
  declarations:
    - mechanism_payment_eq_zero_of_allocation_eq_none
uses:
  - Allocation
  - mechanism_payment_of_allocation_ne_some
---

# mechanism_payment_eq_zero_of_allocation_eq_none

## Lean type

```lean
lemma mechanism_payment_eq_zero_of_allocation_eq_none {reserve : U} {b : I → U} {i : I} (halloc : allocation reserve b = none) : (mechanism reserve).paymentRule b i = 0
```

## Dependencies

- Allocation
- mechanism_payment_of_allocation_ne_some
