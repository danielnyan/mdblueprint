---
id: optStrategy-isSubgamePerfect
title: optStrategy_isSubgamePerfect
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTreeSPE
  declarations:
    - optStrategy_isSubgamePerfect
uses:
  - IsSubgamePerfect
  - Strategy
  - strong_induction
  - outcome_Leaf
  - Arena.Reachable.step
  - CPState.step
  - outcome_Node
  - outcome_optStrategy_eq_value
  - value_Node_ge
  - value_optStrategy_eq
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# optStrategy_isSubgamePerfect

## Lean type

```lean
theorem optStrategy_isSubgamePerfect [DecidableLE U] : IsSubgamePerfect (optStrategy : Strategy N U)
```

## Dependencies

- IsSubgamePerfect
- Strategy
- strong_induction
- outcome_Leaf
- Arena.Reachable.step
- CPState.step
- outcome_Node
- outcome_optStrategy_eq_value
- value_Node_ge
- value_optStrategy_eq
- IsPositiveAffineOf.symm
- Indifferent.symm
