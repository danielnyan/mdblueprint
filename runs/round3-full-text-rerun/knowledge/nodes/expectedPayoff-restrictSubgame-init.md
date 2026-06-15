---
id: expectedPayoff-restrictSubgame-init
title: expectedPayoff_restrictSubgame_init
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - expectedPayoff_restrictSubgame_init
uses:
  - isEmpty
  - BehaviorProfile
  - expectedPayoff
  - subgameAt
  - ReachedSubgamePayoffTransfer.init
  - restrictSubgame
---

# expectedPayoff_restrictSubgame_init

## Lean type

```lean
@[simp] theorem expectedPayoff_restrictSubgame_init {G : ExtensiveGame iota Real} [(s : G.State) -> Fintype (G.Action s)] [(s : G.State) -> Decidable (IsEmpty (G.Action s))] (beta : G.BehaviorProfile) (fuel : Nat) (who : iota) : expectedPayoff (G.subgameAt G.init) (beta.restrictSubgame G.init) fuel who = expectedPayoff G beta fuel who
```

## Dependencies

- isEmpty
- BehaviorProfile
- expectedPayoff
- subgameAt
- ReachedSubgamePayoffTransfer.init
- restrictSubgame
