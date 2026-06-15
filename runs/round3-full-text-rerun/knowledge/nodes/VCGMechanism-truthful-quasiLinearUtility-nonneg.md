---
id: VCGMechanism-truthful-quasiLinearUtility-nonneg
title: VCGMechanism_truthful_quasiLinearUtility_nonneg
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.VCG
  declarations:
    - VCGMechanism_truthful_quasiLinearUtility_nonneg
uses:
  - Valuation
  - quasiLinearUtility
  - valueOfAllocation
  - socialWelfare
  - welfareWithout
  - welfareWithout_le_socialWelfare_of_nonneg_i
  - efficientAllocation_isOptimal
  - socialWelfare_eq_value_add_welfareWithout
---

# VCGMechanism_truthful_quasiLinearUtility_nonneg

## Lean type

```lean
theorem VCGMechanism_truthful_quasiLinearUtility_nonneg (v : ∀ _ : I, Valuation A ℝ) (hnonneg : ∀ i : I, ∀ a : A, 0 ≤ v i a) (i : I) (r : ∀ _ : I, Valuation A ℝ) : 0 ≤ MechanismWithTransfers.quasiLinearUtility VCGTransferMechanism valueOfAllocation id id (Function.update r i (v i)) v i
```

## Dependencies

- Valuation
- quasiLinearUtility
- valueOfAllocation
- socialWelfare
- welfareWithout
- welfareWithout_le_socialWelfare_of_nonneg_i
- efficientAllocation_isOptimal
- socialWelfare_eq_value_add_welfareWithout
