---
id: mechanism-payment-of-allocation-eq-some
title: mechanism_payment_of_allocation_eq_some
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.ReserveVickrey
  declarations:
    - mechanism_payment_of_allocation_eq_some
uses:
  - Allocation
---

# mechanism_payment_of_allocation_eq_some

## Lean type

```lean
lemma mechanism_payment_of_allocation_eq_some {reserve : U} {b : I → U} {i : I} (halloc : allocation reserve b = some i) : (mechanism reserve).paymentRule b i = clearingPrice reserve b
```

## Dependencies

- Allocation
