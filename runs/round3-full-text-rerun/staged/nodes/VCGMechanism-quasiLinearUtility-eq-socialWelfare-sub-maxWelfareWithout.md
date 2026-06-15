---
id: VCGMechanism-quasiLinearUtility-eq-socialWelfare-sub-maxWelfareWithout
title: VCGMechanism_quasiLinearUtility_eq_socialWelfare_sub_maxWelfareWithout
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.VCG
  declarations:
    - VCGMechanism_quasiLinearUtility_eq_socialWelfare_sub_maxWelfareWithout
uses:
  - Valuation
  - quasiLinearUtility
  - valueOfAllocation
  - socialWelfare
  - welfareWithout
  - welfareWithout_update_self
  - socialWelfare_eq_value_add_welfareWithout
---

# VCGMechanism_quasiLinearUtility_eq_socialWelfare_sub_maxWelfareWithout

## Lean type

```lean
lemma VCGMechanism_quasiLinearUtility_eq_socialWelfare_sub_maxWelfareWithout (reports trueTypes : ∀ _ : I, Valuation A ℝ) (i : I) : MechanismWithTransfers.quasiLinearUtility VCGTransferMechanism valueOfAllocation id id reports trueTypes i = socialWelfare (Function.update reports i (trueTypes i)) (efficientAllocation reports) - maxWelfareWithout reports i
```

## Dependencies

- Valuation
- quasiLinearUtility
- valueOfAllocation
- socialWelfare
- welfareWithout
- welfareWithout_update_self
- socialWelfare_eq_value_add_welfareWithout
