---
id: subgameAt-infoWellFormed
title: subgameAt_infoWellFormed
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.ImperfectInformation
  declarations:
    - subgameAt_infoWellFormed
uses:
  - InfoWellFormed
  - subgameAt
  - SameMoverOnInfo
  - SameActionsOnInfo
  - NoChanceOnDecisionInfo
---

# subgameAt_infoWellFormed

## Lean type

```lean
theorem subgameAt_infoWellFormed {s : G.State} (h : G.InfoWellFormed) : (G.subgameAt s).InfoWellFormed
```

## Dependencies

- InfoWellFormed
- subgameAt
- SameMoverOnInfo
- SameActionsOnInfo
- NoChanceOnDecisionInfo
