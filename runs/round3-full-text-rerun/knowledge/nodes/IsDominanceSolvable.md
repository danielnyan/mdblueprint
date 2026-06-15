---
id: IsDominanceSolvable
title: IsDominanceSolvable
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.IESDS
  declarations:
    - IsDominanceSolvable
uses:
  - Profile
  - IsNashEquilibrium.survives
  - Survives
---

# IsDominanceSolvable

## Lean type

```lean
def IsDominanceSolvable (G : StrategicGame N U) : Prop
```

## Dependencies

- Profile
- IsNashEquilibrium.survives
- Survives
