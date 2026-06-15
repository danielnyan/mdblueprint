---
id: VCGMechanism-truthful-profile-quasiLinearUtility-nonneg
title: VCGMechanism_truthful_profile_quasiLinearUtility_nonneg
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.VCG
  declarations:
    - VCGMechanism_truthful_profile_quasiLinearUtility_nonneg
uses:
  - Valuation
  - quasiLinearUtility
  - valueOfAllocation
  - VCGMechanism_truthful_quasiLinearUtility_nonneg
---

# VCGMechanism_truthful_profile_quasiLinearUtility_nonneg

## Lean type

```lean
theorem VCGMechanism_truthful_profile_quasiLinearUtility_nonneg (v : ∀ _ : I, Valuation A ℝ) (hnonneg : ∀ i : I, ∀ a : A, 0 ≤ v i a) (i : I) : 0 ≤ MechanismWithTransfers.quasiLinearUtility VCGTransferMechanism valueOfAllocation id id v v i
```

## Dependencies

- Valuation
- quasiLinearUtility
- valueOfAllocation
- VCGMechanism_truthful_quasiLinearUtility_nonneg
