---
id: BundleDemandUtility
title: BundleDemandUtility
kind: theorem
status: staged
lean:
  module: EconCSLib.OpenProblem.SubmodularWelfareDemandOracle
  declarations:
    - BundleDemandUtility
uses:
  - BundlePriceVector
  - BundleAllocation
  - ValueOracle
---

# BundleDemandUtility

## Lean type

```lean
def BundleDemandUtility {G : Type*} [DecidableEq G] {M : Finset G} (v : SubmodularBundleValuation M) (p : BundlePriceVector M) (S : BundleAllocation M) : ℝ
```

## Dependencies

- BundlePriceVector
- BundleAllocation
- ValueOracle
