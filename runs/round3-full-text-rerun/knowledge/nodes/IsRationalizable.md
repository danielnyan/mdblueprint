---
id: IsRationalizable
title: IsRationalizable
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.IESDS
  declarations:
    - IsRationalizable
uses:
  - Strategy
  - IsNashEquilibrium.survives
  - Survives
---

# IsRationalizable

## Lean type

```lean
def IsRationalizable (G : StrategicGame N U) (i : N) (s : G.strategy i) : Prop
```

## Dependencies

- Strategy
- IsNashEquilibrium.survives
- Survives
