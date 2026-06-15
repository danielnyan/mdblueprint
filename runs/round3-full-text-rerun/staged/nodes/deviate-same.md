---
id: deviate-same
title: deviate_same
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Basic
  declarations:
    - deviate_same
uses:
  - Profile
  - BehaviorProfile
  - BehaviorStrategy
  - Profile
  - Strategy
---

# deviate_same

## Lean type

```lean
@[simp] theorem deviate_same (σ : G.Profile) (i : N) (s' : G.strategy i) : deviate σ i s' i = s'
```

## Dependencies

- Profile
- BehaviorProfile
- BehaviorStrategy
- Profile
- Strategy
