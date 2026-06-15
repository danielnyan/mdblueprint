---
id: IsNashAt-toSubgamePerfectOn-of-hasOnlyRootSubgames
title: IsNashAt.toSubgamePerfectOn_of_hasOnlyRootSubgames
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTreeNE
  declarations:
    - IsNashAt.toSubgamePerfectOn_of_hasOnlyRootSubgames
uses:
  - Strategy
  - IsNashAt
  - HasOnlyRootSubgames
  - IsSubgamePerfectOn
---

# IsNashAt.toSubgamePerfectOn_of_hasOnlyRootSubgames

## Lean type

```lean
theorem IsNashAt.toSubgamePerfectOn_of_hasOnlyRootSubgames {σ : Strategy N U} {g : GameTree N U} (hnash : IsNashAt σ g) (hsubgames : HasOnlyRootSubgames g) : IsSubgamePerfectOn σ g
```

## Dependencies

- Strategy
- IsNashAt
- HasOnlyRootSubgames
- IsSubgamePerfectOn
