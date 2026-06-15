---
id: VCGMechanism-isDSIC
title: VCGMechanism_isDSIC
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.VCG
  declarations:
    - VCGMechanism_isDSIC
uses:
  - isQuasiLinearDSIC
  - Valuation
  - valueOfAllocation
  - IsStrictlyDominant.isWeaklyDominant
  - IsWeaklyDominant
  - WeaklyDominates
  - socialWelfare
  - efficientAllocation_isOptimal
  - quasiLinearUtility
  - VCGMechanism_quasiLinearUtility_eq_socialWelfare_sub_maxWelfareWithout
  - maxWelfareWithout_update_self
---

# VCGMechanism_isDSIC

## Lean type

```lean
theorem VCGMechanism_isDSIC : MechanismWithTransfers.isQuasiLinearDSIC (M
```

## Dependencies

- isQuasiLinearDSIC
- Valuation
- valueOfAllocation
- IsStrictlyDominant.isWeaklyDominant
- IsWeaklyDominant
- WeaklyDominates
- socialWelfare
- efficientAllocation_isOptimal
- quasiLinearUtility
- VCGMechanism_quasiLinearUtility_eq_socialWelfare_sub_maxWelfareWithout
- maxWelfareWithout_update_self
