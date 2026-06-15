---
id: IsZeroSum-neg
title: IsZeroSum.neg
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.Basic
  declarations:
    - IsZeroSum.neg
uses:
  - IsConstantSum.neg
  - IsZeroSum
  - Profile
  - Strategy
---

# IsZeroSum.neg

## Lean type

```lean
theorem IsZeroSum.neg' [AddGroup U] {G : StrategicGame (Fin 2) U} (hzs : IsZeroSum G) (σ : G.Profile) : G.payoff σ 0 = - G.payoff σ 1
```

## Dependencies

- IsConstantSum.neg
- IsZeroSum
- Profile
- Strategy
