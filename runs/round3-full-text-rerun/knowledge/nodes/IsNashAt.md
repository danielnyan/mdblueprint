---
id: IsNashAt
title: IsNashAt
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTreeNE
  declarations:
    - IsNashAt
uses:
  - Strategy
  - IsNashEquilibrium
---

# IsNashAt

## Lean type

```lean
abbrev IsNashAt (σ : Strategy N U) (g : GameTree N U) : Prop
```

## Dependencies

- Strategy
- IsNashEquilibrium
