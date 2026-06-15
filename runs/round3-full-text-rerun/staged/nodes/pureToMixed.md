---
id: pureToMixed
title: pureToMixed
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.MixedStrategy
  declarations:
    - pureToMixed
uses:
  - Strategy
  - MixedStrategy
---

# pureToMixed

## Lean type

```lean
def pureToMixed {G : StrategicGame N U} {i : N} [Fintype (G.strategy i)] [DecidableEq (G.strategy i)] (s₀ : G.strategy i) : MixedStrategy G i
```

## Dependencies

- Strategy
- MixedStrategy
