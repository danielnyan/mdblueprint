---
id: IsCompletelyMixed
title: IsCompletelyMixed
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.MixedStrategy
  declarations:
    - IsCompletelyMixed
uses:
  - BehaviorProfile
  - BehaviorStrategy
  - Strategy
  - MixedStrategy
---

# IsCompletelyMixed

## Lean type

```lean
def IsCompletelyMixed (G : StrategicGame N ℚ) {i : N} [Fintype (G.strategy i)] (p : MixedStrategy G i) : Prop
```

## Dependencies

- BehaviorProfile
- BehaviorStrategy
- Strategy
- MixedStrategy
