---
id: ReachedSubgamePayoffTransfer-init
title: ReachedSubgamePayoffTransfer.init
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - ReachedSubgamePayoffTransfer.init
uses:
  - isEmpty
  - BehaviorProfile
  - ReachedSubgamePayoffTransfer
  - expectedPayoff
  - restrictSubgame_deviate_liftSubgame
  - expectedPayoffFrom_restrictSubgame
---

# ReachedSubgamePayoffTransfer.init

## Lean type

```lean
theorem ReachedSubgamePayoffTransfer.init (G : ExtensiveGame iota Real) [DecidableEq G.State] [(s : G.State) -> Fintype (G.Action s)] [(s : G.State) -> Decidable (IsEmpty (G.Action s))] [DecidableEq iota] (beta : G.BehaviorProfile) (fuel : Nat) : ReachedSubgamePayoffTransfer G beta G.init fuel
```

## Dependencies

- isEmpty
- BehaviorProfile
- ReachedSubgamePayoffTransfer
- expectedPayoff
- restrictSubgame_deviate_liftSubgame
- expectedPayoffFrom_restrictSubgame
