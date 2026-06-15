---
id: winningVirtualValue-nonpos-of-forall-lt-reserveThreshold
title: winningVirtualValue_nonpos_of_forall_lt_reserveThreshold
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - winningVirtualValue_nonpos_of_forall_lt_reserveThreshold
uses:
  - IsReserveThreshold
  - winningVirtualValue_nonpos_iff_forall_virtualValue_nonpos
  - virtualValue_nonpos_of_lt_isReserveThreshold
---

# winningVirtualValue_nonpos_of_forall_lt_reserveThreshold

## Lean type

```lean
theorem winningVirtualValue_nonpos_of_forall_lt_reserveThreshold [Fintype I] [Nontrivial I] [LinearOrder I] (A : BayesianSingleItemAuction I) {reserve b : I → ℝ} (hreserve : ∀ i, A.IsReserveThreshold i (reserve i)) (hb : ∀ i, b i < reserve i) : A.winningVirtualValue b ≤ 0
```

## Dependencies

- IsReserveThreshold
- winningVirtualValue_nonpos_iff_forall_virtualValue_nonpos
- virtualValue_nonpos_of_lt_isReserveThreshold
