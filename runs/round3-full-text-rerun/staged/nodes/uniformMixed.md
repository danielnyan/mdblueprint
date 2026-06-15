---
id: uniformMixed
title: uniformMixed
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.MixedStrategy
  declarations:
    - uniformMixed
uses:
  - Strategy
  - MixedStrategy
---

# uniformMixed

## Lean type

```lean
def uniformMixed {G : StrategicGame N U} {i : N} [Fintype (G.strategy i)] [Nonempty (G.strategy i)] : MixedStrategy G i
```

## Dependencies

- Strategy
- MixedStrategy
