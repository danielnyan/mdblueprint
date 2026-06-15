---
id: IsBehaviorNashEq-toSubgamePerfect-of-isCompletelyMixed
title: IsBehaviorNashEq.toSubgamePerfect_of_isCompletelyMixed
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - IsBehaviorNashEq.toSubgamePerfect_of_isCompletelyMixed
uses:
  - isEmpty
  - BehaviorProfile
  - IsBehaviorNashEq
  - IsCompletelyMixedWithPositiveReach
  - ReachedSubgamePayoffTransfer
  - IsBehaviorSubgamePerfect
  - IsBehaviorNashEq.toSubgamePerfect_of_reachProb_pos
  - IsCompletelyMixedWithPositiveReach.reach_pos
---

# IsBehaviorNashEq.toSubgamePerfect_of_isCompletelyMixed

## Lean type

```lean
theorem IsBehaviorNashEq.toSubgamePerfect_of_isCompletelyMixed {G : ExtensiveGame iota Real} [DecidableEq G.State] [(s : G.State) -> Fintype (G.Action s)] [(s : G.State) -> Decidable (IsEmpty (G.Action s))] [DecidableEq iota] {beta : G.BehaviorProfile} {fuel : Nat} (hNash : IsBehaviorNashEq G beta fuel) (hbeta : BehaviorProfile.IsCompletelyMixedWithPositiveReach beta fuel) (hpay : forall root : G.State, ReachedSubgamePayoffTransfer G beta root fuel) : IsBehaviorSubgamePerfect G beta fuel
```

## Dependencies

- isEmpty
- BehaviorProfile
- IsBehaviorNashEq
- IsCompletelyMixedWithPositiveReach
- ReachedSubgamePayoffTransfer
- IsBehaviorSubgamePerfect
- IsBehaviorNashEq.toSubgamePerfect_of_reachProb_pos
- IsCompletelyMixedWithPositiveReach.reach_pos
