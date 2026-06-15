---
id: outcome-Leaf
title: outcome_Leaf
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTreeSPE
  declarations:
    - outcome_Leaf
uses:
  - Strategy
---

# outcome_Leaf

## Lean type

```lean
@[simp] theorem outcome_Leaf (σ : Strategy N U) (p : N → U) : outcome σ (Leaf p) = p
```

## Dependencies

- Strategy
