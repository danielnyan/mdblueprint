---
id: IsConstantSum-nash-payoff-eq-p1
title: IsConstantSum.nash_payoff_eq_p1
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.Basic
  declarations:
    - IsConstantSum.nash_payoff_eq_p1
uses:
  - IsConstantSum
  - Profile
  - IsNashEquilibrium
  - IsConstantSum.nash_payoff_eq
  - IsZeroSum.nash_payoff_eq
  - Strategy
---

# IsConstantSum.nash_payoff_eq_p1

## Lean type

```lean
theorem IsConstantSum.nash_payoff_eq_p1 {c : U} (hcs : IsConstantSum G c) {σ τ : G.Profile} (hσ : IsNashEquilibrium G σ) (hτ : IsNashEquilibrium G τ) : G.payoff σ 1 = G.payoff τ 1
```

## Dependencies

- IsConstantSum
- Profile
- IsNashEquilibrium
- IsConstantSum.nash_payoff_eq
- IsZeroSum.nash_payoff_eq
- Strategy
