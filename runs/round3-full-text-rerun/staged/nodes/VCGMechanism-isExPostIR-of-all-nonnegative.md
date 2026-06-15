---
id: VCGMechanism-isExPostIR-of-all-nonnegative
title: VCGMechanism_isExPostIR_of_all_nonnegative
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.VCG
  declarations:
    - VCGMechanism_isExPostIR_of_all_nonnegative
uses:
  - Valuation
  - isQuasiLinearExPostIR
  - valueOfAllocation
  - quasiLinearUtility
  - VCGMechanism_truthful_quasiLinearUtility_nonneg
---

# VCGMechanism_isExPostIR_of_all_nonnegative

## Lean type

```lean
theorem VCGMechanism_isExPostIR_of_all_nonnegative (hnonneg : ∀ v : (∀ _ : I, Valuation A ℝ), ∀ i : I, ∀ a : A, 0 ≤ v i a) : MechanismWithTransfers.isQuasiLinearExPostIR (M
```

## Dependencies

- Valuation
- isQuasiLinearExPostIR
- valueOfAllocation
- quasiLinearUtility
- VCGMechanism_truthful_quasiLinearUtility_nonneg
