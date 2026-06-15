---
id: BundlePartitionAllocation
title: BundlePartitionAllocation
kind: theorem
status: staged
lean:
  module: EconCSLib.OpenProblem.SubmodularWelfareDemandOracle
  declarations:
    - BundlePartitionAllocation
uses:
  - BundleAllocation
---

# BundlePartitionAllocation

## Lean type

```lean
def BundlePartitionAllocation (I : Type*) {G : Type*} [DecidableEq G] (M : Finset G) : Type _
```

## Dependencies

- BundleAllocation
