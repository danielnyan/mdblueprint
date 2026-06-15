---
id: IsBehaviorNashEq-restrictSubgame-of-reachProb-pos
title: IsBehaviorNashEq.restrictSubgame_of_reachProb_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - IsBehaviorNashEq.restrictSubgame_of_reachProb_pos
uses:
  - isEmpty
  - BehaviorProfile
  - IsBehaviorNashEq
  - ReachedSubgamePayoffTransfer
  - subgameAt
  - restrictSubgame
  - liftSubgame
  - expectedPayoff
---

# IsBehaviorNashEq.restrictSubgame_of_reachProb_pos

## Lean type

```lean
theorem IsBehaviorNashEq.restrictSubgame_of_reachProb_pos {G : ExtensiveGame iota Real} [DecidableEq G.State] [(s : G.State) -> Fintype (G.Action s)] [(s : G.State) -> Decidable (IsEmpty (G.Action s))] [DecidableEq iota] {beta : G.BehaviorProfile} {root : G.State} {fuel : Nat} (hNash : IsBehaviorNashEq G beta fuel) (hreach : 0 < reachProb G beta root fuel) (hpay : ReachedSubgamePayoffTransfer G beta root fuel) : IsBehaviorNashEq (G.subgameAt root) (beta.restrictSubgame root) fuel
```

## Dependencies

- isEmpty
- BehaviorProfile
- IsBehaviorNashEq
- ReachedSubgamePayoffTransfer
- subgameAt
- restrictSubgame
- liftSubgame
- expectedPayoff
