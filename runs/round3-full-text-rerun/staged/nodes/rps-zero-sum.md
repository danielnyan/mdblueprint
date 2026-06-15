---
id: rps-zero-sum
title: rps_zero_sum
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.RockPaperScissors
  declarations:
    - rps_zero_sum
uses:
  - Profile
---

# rps_zero_sum

## Lean type

```lean
theorem rps_zero_sum : ∀ σ : RPS.Profile, RPS.payoff σ 0 + RPS.payoff σ 1 = 0
```

## Dependencies

- Profile
