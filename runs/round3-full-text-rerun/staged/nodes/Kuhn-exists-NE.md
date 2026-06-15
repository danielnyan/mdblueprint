---
id: Kuhn-exists-NE
title: Kuhn_exists_NE
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTreeNE
  declarations:
    - Kuhn_exists_NE
uses:
  - Strategy
  - IsNashEquilibrium
  - Kuhn_exists_SPE
  - IsSubgamePerfect.toNE
---

# Kuhn_exists_NE

## Lean type

```lean
theorem Kuhn_exists_NE [DecidableLE U] (g : GameTree N U) : ∃ σ : Strategy N U, IsNashEquilibrium σ g
```

## Dependencies

- Strategy
- IsNashEquilibrium
- Kuhn_exists_SPE
- IsSubgamePerfect.toNE
