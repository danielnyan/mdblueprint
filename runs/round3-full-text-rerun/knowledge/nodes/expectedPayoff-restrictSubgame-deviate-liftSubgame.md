---
id: expectedPayoff-restrictSubgame-deviate-liftSubgame
title: expectedPayoff_restrictSubgame_deviate_liftSubgame
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - expectedPayoff_restrictSubgame_deviate_liftSubgame
uses:
  - isEmpty
  - BehaviorProfile
  - subgameAt
  - BehaviorStrategy
  - expectedPayoff
  - liftSubgame
  - restrictSubgame
  - restrictSubgame_deviate_liftSubgame
---

# expectedPayoff_restrictSubgame_deviate_liftSubgame

## Lean type

```lean
theorem expectedPayoff_restrictSubgame_deviate_liftSubgame {G : ExtensiveGame iota Real} [(s : G.State) -> Fintype (G.Action s)] [(s : G.State) -> Decidable (IsEmpty (G.Action s))] [DecidableEq iota] (beta : G.BehaviorProfile) (who : iota) {root : G.State} (beta' : (G.subgameAt root).BehaviorStrategy who) (fuel : Nat) : expectedPayoff (G.subgameAt root) ((beta.deviate who beta'.liftSubgame).restrictSubgame root) fuel who = expectedPayoff (G.subgameAt root) ((beta.restrictSubgame root).deviate who beta') fuel who
```

## Dependencies

- isEmpty
- BehaviorProfile
- subgameAt
- BehaviorStrategy
- expectedPayoff
- liftSubgame
- restrictSubgame
- restrictSubgame_deviate_liftSubgame
