---
id: muller-satterthwaite
title: muller_satterthwaite
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.GibbardSatterthwaite
  declarations:
    - muller_satterthwaite
uses:
  - VotingRule
  - IsTotal
  - Resolute
  - Unanimity
  - Monotonicity
  - Dictatorial
  - SWF
  - arrow_impossibility
  - Prefers
  - topChoice_topRank
  - monotonic_zProfile
---

# muller_satterthwaite

## Lean type

```lean
theorem muller_satterthwaite [Fintype N] [Nonempty N] [Fintype A] [Nonempty A] (hA : Fintype.card A ≥ 3) (f : VotingRule N A) (hf_total : IsTotal f) (hf_res : Resolute f) (hU : Unanimity f) (hM : Monotonicity f) : Dictatorial f
```

## Dependencies

- VotingRule
- IsTotal
- Resolute
- Unanimity
- Monotonicity
- Dictatorial
- SWF
- arrow_impossibility
- Prefers
- topChoice_topRank
- monotonic_zProfile
