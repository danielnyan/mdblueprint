---
id: outcome-optStrategy-eq-value
title: outcome_optStrategy_eq_value
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTreeSPE
  declarations:
    - outcome_optStrategy_eq_value
uses:
  - Strategy
  - strong_induction
  - outcome_Leaf
  - value₀_Leaf
  - value_Leaf
  - Arena.Reachable.step
  - CPState.step
  - outcome_Node
  - value_optStrategy_eq
---

# outcome_optStrategy_eq_value

## Lean type

```lean
theorem outcome_optStrategy_eq_value [DecidableLE U] (g : GameTree N U) : outcome (optStrategy : Strategy N U) g = value g
```

## Dependencies

- Strategy
- strong_induction
- outcome_Leaf
- value₀_Leaf
- value_Leaf
- Arena.Reachable.step
- CPState.step
- outcome_Node
- value_optStrategy_eq
