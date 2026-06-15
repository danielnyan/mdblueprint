---
id: allocation-eq-some-iff
title: allocation_eq_some_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.ReserveVickrey
  declarations:
    - allocation_eq_some_iff
uses:
  - Allocation
---

# allocation_eq_some_iff

## Lean type

```lean
lemma allocation_eq_some_iff {reserve : U} {b : I → U} {i : I} : allocation reserve b = some i ↔ reserve ≤ b (SecondPrice.winner b) ∧ SecondPrice.winner b = i
```

## Dependencies

- Allocation
