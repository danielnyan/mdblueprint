---
id: StrategyProfile-actionAt
title: StrategyProfile.actionAt
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Strategy
  declarations:
    - StrategyProfile.actionAt
uses:
  - StrategyProfile
---

# StrategyProfile.actionAt

## Lean type

```lean
def StrategyProfile.actionAt [DecidableEq N] {G : ExtensiveGame N U} (σ : StrategyProfile G) (s : G.State) : Option (Σ i : N, G.Action s)
```

## Dependencies

- StrategyProfile
