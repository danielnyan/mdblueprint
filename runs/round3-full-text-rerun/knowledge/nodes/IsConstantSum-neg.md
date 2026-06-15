---
id: IsConstantSum-neg
title: IsConstantSum.neg
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.Basic
  declarations:
    - IsConstantSum.neg
uses:
  - IsConstantSum
  - Profile
---

# IsConstantSum.neg

## Lean type

```lean
theorem IsConstantSum.neg [AddCommGroup U] {G : StrategicGame (Fin 2) U} {c : U} (hcs : IsConstantSum G c) (σ : G.Profile) : G.payoff σ 1 = c - G.payoff σ 0
```

## Dependencies

- IsConstantSum
- Profile
