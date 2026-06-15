---
id: IsBehaviorNashEq-toSubgamePerfect-of-reachProb-pos
title: IsBehaviorNashEq.toSubgamePerfect_of_reachProb_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - IsBehaviorNashEq.toSubgamePerfect_of_reachProb_pos
uses:
  - isEmpty
  - BehaviorProfile
  - IsBehaviorNashEq
  - ReachedSubgamePayoffTransfer
  - IsBehaviorSubgamePerfect
  - IsBehaviorNashEq.restrictSubgame_of_reachProb_pos
---

# IsBehaviorNashEq.toSubgamePerfect_of_reachProb_pos

## Lean type

```lean
theorem IsBehaviorNashEq.toSubgamePerfect_of_reachProb_pos {G : ExtensiveGame iota Real} [DecidableEq G.State] [(s : G.State) -> Fintype (G.Action s)] [(s : G.State) -> Decidable (IsEmpty (G.Action s))] [DecidableEq iota] {beta : G.BehaviorProfile} {fuel : Nat} (hNash : IsBehaviorNashEq G beta fuel) (hreach : forall root : G.State, 0 < reachProb G beta root fuel) (hpay : forall root : G.State, ReachedSubgamePayoffTransfer G beta root fuel) : IsBehaviorSubgamePerfect G beta fuel
```

## Dependencies

- isEmpty
- BehaviorProfile
- IsBehaviorNashEq
- ReachedSubgamePayoffTransfer
- IsBehaviorSubgamePerfect
- IsBehaviorNashEq.restrictSubgame_of_reachProb_pos
