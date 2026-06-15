---
id: IsZeroSum-nash-payoff-eq
title: IsZeroSum.nash_payoff_eq
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.Basic
  declarations:
    - IsZeroSum.nash_payoff_eq
uses:
  - IsZeroSum
  - Profile
  - IsNashEquilibrium
  - IsConstantSum.neg
  - IsZeroSum.neg
---

# IsZeroSum.nash_payoff_eq

## Lean type

```lean
theorem IsZeroSum.nash_payoff_eq (hzs : IsZeroSum G) {σ τ : G.Profile} (hσ : IsNashEquilibrium G σ) (hτ : IsNashEquilibrium G τ) : G.payoff σ 0 = G.payoff τ 0
```

## Dependencies

- IsZeroSum
- Profile
- IsNashEquilibrium
- IsConstantSum.neg
- IsZeroSum.neg
