---
id: mixed-g
title: mixed_g
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Nash
  declarations:
    - mixed_g
uses:
  - Strategy
  - Profile
---

# mixed_g

## Lean type

```lean
def mixed_g (i : N) (m : ∀ i, G.strategy i → ℝ) : ℝ
```

## Dependencies

- Strategy
- Profile
