---
id: deviate-of-ne
title: deviate_of_ne
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Basic
  declarations:
    - deviate_of_ne
uses:
  - Profile
  - BehaviorProfile
  - BehaviorStrategy
  - Mark.other
  - Profile
  - Strategy
---

# deviate_of_ne

## Lean type

```lean
@[simp] theorem deviate_of_ne (σ : G.Profile) (i : N) (s' : G.strategy i) {j : N} (h : j ≠ i) : deviate σ i s' j = σ j
```

## Dependencies

- Profile
- BehaviorProfile
- BehaviorStrategy
- Mark.other
- Profile
- Strategy
