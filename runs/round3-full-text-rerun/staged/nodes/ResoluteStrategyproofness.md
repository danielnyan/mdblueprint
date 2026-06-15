---
id: ResoluteStrategyproofness
title: ResoluteStrategyproofness
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - ResoluteStrategyproofness
uses:
  - VotingRule
  - Resolute
  - Profile
  - Prefers
---

# ResoluteStrategyproofness

## Lean type

```lean
def ResoluteStrategyproofness (f : VotingRule N A) (_hf : Resolute f) : Prop
```

## Dependencies

- VotingRule
- Resolute
- Profile
- Prefers
