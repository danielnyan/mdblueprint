---
id: reachableSubgameAt-payoff
title: reachableSubgameAt_payoff
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Subgame
  declarations:
    - reachableSubgameAt_payoff
uses:
  - reachableSubgameAt
---

# reachableSubgameAt_payoff

## Lean type

```lean
@[simp] theorem reachableSubgameAt_payoff (G : ExtensiveGame iota U) (root : G.State) (s : (G.reachableSubgameAt root).State) (i : iota) : (G.reachableSubgameAt root).payoff s i = G.payoff s.1 i
```

## Dependencies

- reachableSubgameAt
