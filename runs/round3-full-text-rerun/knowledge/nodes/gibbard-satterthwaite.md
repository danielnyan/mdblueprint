---
id: gibbard-satterthwaite
title: gibbard_satterthwaite
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.GibbardSatterthwaite
  declarations:
    - gibbard_satterthwaite
uses:
  - VotingRule
  - IsTotal
  - Resolute
  - Unanimity
  - ResoluteStrategyproofness
  - Dictatorial
  - muller_satterthwaite
  - strategyproof_monotonic
---

# gibbard_satterthwaite

## Lean type

```lean
theorem gibbard_satterthwaite [Fintype N] [Nonempty N] [Fintype A] [Nonempty A] (hA : Fintype.card A ≥ 3) (f : VotingRule N A) (hf_total : IsTotal f) (hf_res : Resolute f) (hU : Unanimity f) (hSP : ResoluteStrategyproofness f hf_res) : Dictatorial f
```

## Dependencies

- VotingRule
- IsTotal
- Resolute
- Unanimity
- ResoluteStrategyproofness
- Dictatorial
- muller_satterthwaite
- strategyproof_monotonic
