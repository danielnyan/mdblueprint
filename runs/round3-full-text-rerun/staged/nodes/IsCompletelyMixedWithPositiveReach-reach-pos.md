---
id: IsCompletelyMixedWithPositiveReach-reach-pos
title: IsCompletelyMixedWithPositiveReach.reach_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - IsCompletelyMixedWithPositiveReach.reach_pos
uses:
  - BehaviorProfile
  - IsCompletelyMixedWithPositiveReach
  - isEmpty
  - actionProb
  - IsReachable.next
  - expectedPayoff
  - ReachedSubgamePayoffTransfer.init
---

# IsCompletelyMixedWithPositiveReach.reach_pos

## Lean type

```lean
theorem IsCompletelyMixedWithPositiveReach.reach_pos {G : ExtensiveGame iota U} [DecidableEq G.State] [(s : G.State) -> Fintype (G.Action s)] {beta : G.BehaviorProfile} {fuel : Nat} (hbeta : IsCompletelyMixedWithPositiveReach beta fuel) (root : G.State) : 0 < reachProb G beta root fuel
```

## Dependencies

- BehaviorProfile
- IsCompletelyMixedWithPositiveReach
- isEmpty
- actionProb
- IsReachable.next
- expectedPayoff
- ReachedSubgamePayoffTransfer.init
