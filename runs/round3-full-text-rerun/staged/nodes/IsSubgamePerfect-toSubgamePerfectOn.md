---
id: IsSubgamePerfect-toSubgamePerfectOn
title: IsSubgamePerfect.toSubgamePerfectOn
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTreeNE
  declarations:
    - IsSubgamePerfect.toSubgamePerfectOn
uses:
  - Strategy
  - IsSubgamePerfect
  - IsSubgamePerfectOn
---

# IsSubgamePerfect.toSubgamePerfectOn

## Lean type

```lean
theorem IsSubgamePerfect.toSubgamePerfectOn {σ : Strategy N U} (hspe : IsSubgamePerfect σ) (g : GameTree N U) : IsSubgamePerfectOn σ g
```

## Dependencies

- Strategy
- IsSubgamePerfect
- IsSubgamePerfectOn
