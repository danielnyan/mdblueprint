---
id: value-optStrategy-eq
title: value_optStrategy_eq
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTreeSPE
  declarations:
    - value_optStrategy_eq
uses:
  - value_Node_eq_some_child_value
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# value_optStrategy_eq

## Lean type

```lean
theorem value_optStrategy_eq [DecidableLE U] (m : N) (h : GameTree N U) (t : List (GameTree N U)) : value (optStrategy m h t).val = value (Node m h t)
```

## Dependencies

- value_Node_eq_some_child_value
- IsPositiveAffineOf.symm
- Indifferent.symm
