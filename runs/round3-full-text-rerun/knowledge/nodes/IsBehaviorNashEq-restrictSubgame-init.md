---
id: IsBehaviorNashEq-restrictSubgame-init
title: IsBehaviorNashEq.restrictSubgame_init
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - IsBehaviorNashEq.restrictSubgame_init
uses:
  - isEmpty
  - BehaviorProfile
  - IsBehaviorNashEq
  - subgameAt
  - ReachedSubgamePayoffTransfer.init
  - restrictSubgame
  - liftSubgame
  - expectedPayoff
  - restrictSubgame_deviate_liftSubgame
---

# IsBehaviorNashEq.restrictSubgame_init

## Lean type

```lean
theorem IsBehaviorNashEq.restrictSubgame_init {G : ExtensiveGame iota Real} [(s : G.State) -> Fintype (G.Action s)] [(s : G.State) -> Decidable (IsEmpty (G.Action s))] [DecidableEq iota] {beta : G.BehaviorProfile} {fuel : Nat} (hNash : IsBehaviorNashEq G beta fuel) : IsBehaviorNashEq (G.subgameAt G.init) (beta.restrictSubgame G.init) fuel
```

## Dependencies

- isEmpty
- BehaviorProfile
- IsBehaviorNashEq
- subgameAt
- ReachedSubgamePayoffTransfer.init
- restrictSubgame
- liftSubgame
- expectedPayoff
- restrictSubgame_deviate_liftSubgame
