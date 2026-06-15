---
id: Kuhn-exists-SPE-on
title: Kuhn_exists_SPE_on
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTreeNE
  declarations:
    - Kuhn_exists_SPE_on
uses:
  - Strategy
  - IsSubgamePerfectOn
  - Kuhn_exists_SPE
  - IsSubgamePerfect.toSubgamePerfectOn
---

# Kuhn_exists_SPE_on

## Lean type

```lean
theorem Kuhn_exists_SPE_on [DecidableLE U] (g : GameTree N U) : ∃ σ : Strategy N U, IsSubgamePerfectOn σ g
```

## Dependencies

- Strategy
- IsSubgamePerfectOn
- Kuhn_exists_SPE
- IsSubgamePerfect.toSubgamePerfectOn
