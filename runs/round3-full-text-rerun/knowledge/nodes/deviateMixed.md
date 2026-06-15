---
id: deviateMixed
title: deviateMixed
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.MixedStrategy
  declarations:
    - deviateMixed
uses:
  - Strategy
  - MixedProfile
  - pureToMixed
---

# deviateMixed

## Lean type

```lean
def deviateMixed (G : StrategicGame N U) [∀ i, Fintype (G.strategy i)] [DecidableEq N] [∀ i, DecidableEq (G.strategy i)] (p : MixedProfile G) (who : N) (s' : G.strategy who) : MixedProfile G
```

## Dependencies

- Strategy
- MixedProfile
- pureToMixed
