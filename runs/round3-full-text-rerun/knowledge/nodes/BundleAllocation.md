---
id: BundleAllocation
title: BundleAllocation
kind: theorem
status: staged
lean:
  module: EconCSLib.OpenProblem.SubmodularWelfareDemandOracle
  declarations:
    - BundleAllocation
uses:
  - Valuation
  - Nonnegative
---

# BundleAllocation

## Lean type

```lean
abbrev BundleAllocation {G : Type*} (M : Finset G) : Type _
```

## Dependencies

- Valuation
- Nonnegative
