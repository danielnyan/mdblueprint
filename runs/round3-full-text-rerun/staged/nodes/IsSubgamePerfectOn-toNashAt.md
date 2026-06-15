---
id: IsSubgamePerfectOn-toNashAt
title: IsSubgamePerfectOn.toNashAt
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTreeNE
  declarations:
    - IsSubgamePerfectOn.toNashAt
uses:
  - Strategy
  - IsSubgamePerfectOn
  - IsNashAt
  - Subtree.self
---

# IsSubgamePerfectOn.toNashAt

## Lean type

```lean
theorem IsSubgamePerfectOn.toNashAt {σ : Strategy N U} {g : GameTree N U} (hspe : IsSubgamePerfectOn σ g) : IsNashAt σ g
```

## Dependencies

- Strategy
- IsSubgamePerfectOn
- IsNashAt
- Subtree.self
