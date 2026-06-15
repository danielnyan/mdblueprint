---
id: IsConstantSum-welfare-eq
title: IsConstantSum.welfare_eq
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.Basic
  declarations:
    - IsConstantSum.welfare_eq
uses:
  - IsConstantSum
  - Profile
---

# IsConstantSum.welfare_eq

## Lean type

```lean
theorem IsConstantSum.welfare_eq [AddCommMonoid U] {G : StrategicGame (Fin 2) U} {c : U} (hcs : IsConstantSum G c) (σ : G.Profile) : welfare G σ = c
```

## Dependencies

- IsConstantSum
- Profile
