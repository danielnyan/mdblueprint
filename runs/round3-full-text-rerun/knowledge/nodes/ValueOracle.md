---
id: ValueOracle
title: ValueOracle
kind: theorem
status: staged
lean:
  module: EconCSLib.OpenProblem.SubmodularWelfareDemandOracle
  declarations:
    - ValueOracle
uses:
  - BundleAllocation
  - valueOfAllocation
---

# ValueOracle

## Lean type

```lean
def ValueOracle {G : Type*} [DecidableEq G] {M : Finset G} (v : SubmodularBundleValuation M) (S : BundleAllocation M) : ℝ
```

## Dependencies

- BundleAllocation
- valueOfAllocation
