---
id: liftSubgame-eq-self
title: liftSubgame_eq_self
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - liftSubgame_eq_self
uses:
  - subgameAt
  - BehaviorStrategy
  - liftSubgame
---

# liftSubgame_eq_self

## Lean type

```lean
theorem liftSubgame_eq_self {G : ExtensiveGame iota U} [(s : G.State) -> Fintype (G.Action s)] {i : iota} {root : G.State} (beta : (G.subgameAt root).BehaviorStrategy i) : beta.liftSubgame = beta
```

## Dependencies

- subgameAt
- BehaviorStrategy
- liftSubgame
