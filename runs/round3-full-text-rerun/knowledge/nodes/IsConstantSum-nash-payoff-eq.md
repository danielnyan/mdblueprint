---
id: IsConstantSum-nash-payoff-eq
title: IsConstantSum.nash_payoff_eq
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.Basic
  declarations:
    - IsConstantSum.nash_payoff_eq
uses:
  - IsConstantSum
  - Profile
  - IsNashEquilibrium
---

# IsConstantSum.nash_payoff_eq

## Lean type

```lean
theorem IsConstantSum.nash_payoff_eq {c : U} (hcs : IsConstantSum G c) {σ τ : G.Profile} (hσ : IsNashEquilibrium G σ) (hτ : IsNashEquilibrium G τ) : G.payoff σ 0 = G.payoff τ 0
```

## Dependencies

- IsConstantSum
- Profile
- IsNashEquilibrium
