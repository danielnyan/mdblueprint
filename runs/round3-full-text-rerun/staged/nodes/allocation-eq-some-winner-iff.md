---
id: allocation-eq-some-winner-iff
title: allocation_eq_some_winner_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.ReserveVickrey
  declarations:
    - allocation_eq_some_winner_iff
uses:
  - Allocation
---

# allocation_eq_some_winner_iff

## Lean type

```lean
lemma allocation_eq_some_winner_iff {reserve : U} {b : I → U} : allocation reserve b = some (SecondPrice.winner b) ↔ reserve ≤ b (SecondPrice.winner b)
```

## Dependencies

- Allocation
