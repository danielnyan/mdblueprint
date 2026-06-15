---
id: IsBehaviorSubgamePerfect
title: IsBehaviorSubgamePerfect
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - IsBehaviorSubgamePerfect
uses:
  - isEmpty
  - BehaviorProfile
  - IsBehaviorNashEq
  - subgameAt
  - restrictSubgame
---

# IsBehaviorSubgamePerfect

## Lean type

```lean
def IsBehaviorSubgamePerfect (G : ExtensiveGame iota Real) [(s : G.State) -> Fintype (G.Action s)] [(s : G.State) -> Decidable (IsEmpty (G.Action s))] [DecidableEq iota] (beta : G.BehaviorProfile) (fuel : Nat) : Prop
```

## Dependencies

- isEmpty
- BehaviorProfile
- IsBehaviorNashEq
- subgameAt
- restrictSubgame
