---
id: DemandOracle
title: DemandOracle
kind: theorem
status: staged
lean:
  module: EconCSLib.OpenProblem.SubmodularWelfareDemandOracle
  declarations:
    - DemandOracle
uses:
  - BundlePriceVector
  - BundleAllocation
  - BundleDemandUtility
---

# DemandOracle

## Lean type

```lean
def DemandOracle {G : Type*} [DecidableEq G] {M : Finset G} (v : SubmodularBundleValuation M) (p : BundlePriceVector M) : Type _
```

## Dependencies

- BundlePriceVector
- BundleAllocation
- BundleDemandUtility
