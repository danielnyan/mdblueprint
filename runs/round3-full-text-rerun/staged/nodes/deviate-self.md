---
id: deviate-self
title: deviate_self
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Basic
  declarations:
    - deviate_self
uses:
  - Profile
  - Profile
---

# deviate_self

## Lean type

```lean
@[simp] theorem deviate_self (σ : G.Profile) (i : N) : deviate σ i (σ i) = σ
```

## Dependencies

- Profile
- Profile
