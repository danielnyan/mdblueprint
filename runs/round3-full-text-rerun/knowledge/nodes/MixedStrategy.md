---
id: MixedStrategy
title: MixedStrategy
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.MixedStrategy
  declarations:
    - MixedStrategy
uses:
  - Strategy
---

# MixedStrategy

## Lean type

```lean
abbrev MixedStrategy (G : StrategicGame N U) (i : N) [Fintype (G.strategy i)]
```

## Dependencies

- Strategy
