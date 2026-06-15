---
id: BundlePartitionSocialWelfare
title: BundlePartitionSocialWelfare
kind: theorem
status: staged
lean:
  module: EconCSLib.OpenProblem.SubmodularWelfareDemandOracle
  declarations:
    - BundlePartitionSocialWelfare
uses:
  - BundlePartitionAllocation
  - socialWelfare
  - BundlePartitionProfileValuation
  - Valuation
  - ValueOracle
  - BundleAllocation
  - DemandOracle
  - BundlePriceVector
  - Lottery
  - Profile
  - Lottery.expectedValue
---

# BundlePartitionSocialWelfare

## Lean type

```lean
def BundlePartitionSocialWelfare {I G : Type*} [Fintype I] [DecidableEq G] {M : Finset G} [Fintype (BundlePartitionAllocation I M)] [Nonempty (BundlePartitionAllocation I M)] (v : I → SubmodularBundleValuation M) (S : BundlePartitionAllocation I M) : ℝ
```

## Dependencies

- BundlePartitionAllocation
- socialWelfare
- BundlePartitionProfileValuation
- Valuation
- ValueOracle
- BundleAllocation
- DemandOracle
- BundlePriceVector
- Lottery
- Profile
- Lottery.expectedValue
