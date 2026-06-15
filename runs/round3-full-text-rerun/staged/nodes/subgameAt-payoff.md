---
id: subgameAt-payoff
title: subgameAt_payoff
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - subgameAt_payoff
uses:
  - subgameAt
---

# subgameAt_payoff

## Lean type

```lean
@[simp] theorem subgameAt_payoff (G : ExtensiveGame iota U) (s t : G.State) (i : iota) : (G.subgameAt s).payoff t i = G.payoff t i
```

## Dependencies

- subgameAt
