---
id: strategyproof-monotonic
title: strategyproof_monotonic
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.GibbardSatterthwaite
  declarations:
    - strategyproof_monotonic
uses:
  - VotingRule
  - Resolute
  - ResoluteStrategyproofness
  - Monotonicity
---

# strategyproof_monotonic

## Lean type

```lean
theorem strategyproof_monotonic [Fintype N] [Fintype A] (f : VotingRule N A) (hf_res : Resolute f) (hSP : ResoluteStrategyproofness f hf_res) : Monotonicity f
```

## Dependencies

- VotingRule
- Resolute
- ResoluteStrategyproofness
- Monotonicity
