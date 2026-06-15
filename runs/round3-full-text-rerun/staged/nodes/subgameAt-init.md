---
id: subgameAt-init
title: subgameAt_init
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.ImperfectInformation
  declarations:
    - subgameAt_init
uses:
  - subgameAt
  - ReachedSubgamePayoffTransfer.init
  - subgameAt
  - ReachedSubgamePayoffTransfer.init
---

# subgameAt_init

## Lean type

```lean
theorem subgameAt_init (s : G.State) : (G.subgameAt s).init = s
```

## Dependencies

- subgameAt
- ReachedSubgamePayoffTransfer.init
- subgameAt
- ReachedSubgamePayoffTransfer.init
