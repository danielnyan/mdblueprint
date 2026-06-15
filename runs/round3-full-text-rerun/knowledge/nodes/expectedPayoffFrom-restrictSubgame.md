---
id: expectedPayoffFrom-restrictSubgame
title: expectedPayoffFrom_restrictSubgame
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - expectedPayoffFrom_restrictSubgame
uses:
  - isEmpty
  - BehaviorProfile
  - subgameAt
  - restrictSubgame
  - actionProb_restrictSubgame
  - IsReachable.next
---

# expectedPayoffFrom_restrictSubgame

## Lean type

```lean
@[simp] theorem expectedPayoffFrom_restrictSubgame {G : ExtensiveGame iota Real} [(s : G.State) -> Fintype (G.Action s)] [(s : G.State) -> Decidable (IsEmpty (G.Action s))] (beta : G.BehaviorProfile) (root start : G.State) (fuel : Nat) (who : iota) : expectedPayoffFrom (G
```

## Dependencies

- isEmpty
- BehaviorProfile
- subgameAt
- restrictSubgame
- actionProb_restrictSubgame
- IsReachable.next
