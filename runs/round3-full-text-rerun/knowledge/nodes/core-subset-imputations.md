---
id: core-subset-imputations
title: core_subset_imputations
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.CoalitionalGame.Core
  declarations:
    - core_subset_imputations
uses:
  - Core
  - IsImputation
  - coalitionPayoff
---

# core_subset_imputations

## Lean type

```lean
theorem core_subset_imputations : G.Core ⊆ { x | G.IsImputation x }
```

## Dependencies

- Core
- IsImputation
- coalitionPayoff
