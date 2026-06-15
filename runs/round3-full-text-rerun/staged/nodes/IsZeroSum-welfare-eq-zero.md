---
id: IsZeroSum-welfare-eq-zero
title: IsZeroSum.welfare_eq_zero
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.Basic
  declarations:
    - IsZeroSum.welfare_eq_zero
uses:
  - IsZeroSum
  - Profile
---

# IsZeroSum.welfare_eq_zero

## Lean type

```lean
theorem IsZeroSum.welfare_eq_zero [AddCommMonoid U] {G : StrategicGame (Fin 2) U} (hzs : IsZeroSum G) (σ : G.Profile) : welfare G σ = 0
```

## Dependencies

- IsZeroSum
- Profile
