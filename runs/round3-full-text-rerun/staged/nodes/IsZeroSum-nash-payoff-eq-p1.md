---
id: IsZeroSum-nash-payoff-eq-p1
title: IsZeroSum.nash_payoff_eq_p1
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.Basic
  declarations:
    - IsZeroSum.nash_payoff_eq_p1
uses:
  - IsZeroSum
  - Profile
  - IsNashEquilibrium
  - IsConstantSum.neg
  - IsZeroSum.neg
  - IsConstantSum.nash_payoff_eq
  - IsZeroSum.nash_payoff_eq
---

# IsZeroSum.nash_payoff_eq_p1

## Lean type

```lean
theorem IsZeroSum.nash_payoff_eq_p1 (hzs : IsZeroSum G) {σ τ : G.Profile} (hσ : IsNashEquilibrium G σ) (hτ : IsNashEquilibrium G τ) : G.payoff σ 1 = G.payoff τ 1
```

## Dependencies

- IsZeroSum
- Profile
- IsNashEquilibrium
- IsConstantSum.neg
- IsZeroSum.neg
- IsConstantSum.nash_payoff_eq
- IsZeroSum.nash_payoff_eq
