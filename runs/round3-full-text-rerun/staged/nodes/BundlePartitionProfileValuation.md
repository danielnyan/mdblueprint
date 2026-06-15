---
id: BundlePartitionProfileValuation
title: BundlePartitionProfileValuation
kind: theorem
status: staged
lean:
  module: EconCSLib.OpenProblem.SubmodularWelfareDemandOracle
  declarations:
    - BundlePartitionProfileValuation
uses:
  - Valuation
  - BundlePartitionAllocation
---

# BundlePartitionProfileValuation

## Lean type

```lean
def BundlePartitionProfileValuation {I G : Type*} [DecidableEq G] {M : Finset G} (v : I → SubmodularBundleValuation M) (i : I) : MultipleParameterMechanism.Valuation (BundlePartitionAllocation I M) ℝ
```

## Dependencies

- Valuation
- BundlePartitionAllocation
