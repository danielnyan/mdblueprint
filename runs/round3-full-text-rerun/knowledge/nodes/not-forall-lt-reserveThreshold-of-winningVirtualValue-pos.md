---
id: not-forall-lt-reserveThreshold-of-winningVirtualValue-pos
title: not_forall_lt_reserveThreshold_of_winningVirtualValue_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - not_forall_lt_reserveThreshold_of_winningVirtualValue_pos
uses:
  - IsReserveThreshold
  - winningVirtualValue_nonpos_of_forall_lt_reserveThreshold
---

# not_forall_lt_reserveThreshold_of_winningVirtualValue_pos

## Lean type

```lean
theorem not_forall_lt_reserveThreshold_of_winningVirtualValue_pos [Fintype I] [Nontrivial I] [LinearOrder I] (A : BayesianSingleItemAuction I) {reserve b : I → ℝ} (hreserve : ∀ i, A.IsReserveThreshold i (reserve i)) (hpos : 0 < A.winningVirtualValue b) : ¬ ∀ i, b i < reserve i
```

## Dependencies

- IsReserveThreshold
- winningVirtualValue_nonpos_of_forall_lt_reserveThreshold
