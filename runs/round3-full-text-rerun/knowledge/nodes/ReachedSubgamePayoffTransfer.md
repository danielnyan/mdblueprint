---
id: ReachedSubgamePayoffTransfer
title: ReachedSubgamePayoffTransfer
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - ReachedSubgamePayoffTransfer
uses:
  - isEmpty
  - BehaviorProfile
  - subgameAt
  - BehaviorStrategy
  - expectedPayoff
  - liftSubgame
  - restrictSubgame
---

# ReachedSubgamePayoffTransfer

## Lean type

```lean
def ReachedSubgamePayoffTransfer (G : ExtensiveGame iota Real) [DecidableEq G.State] [(s : G.State) -> Fintype (G.Action s)] [(s : G.State) -> Decidable (IsEmpty (G.Action s))] [DecidableEq iota] (beta : G.BehaviorProfile) (root : G.State) (fuel : Nat) : Prop
```

## Dependencies

- isEmpty
- BehaviorProfile
- subgameAt
- BehaviorStrategy
- expectedPayoff
- liftSubgame
- restrictSubgame
