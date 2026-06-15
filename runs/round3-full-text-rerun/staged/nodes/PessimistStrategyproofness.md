---
id: PessimistStrategyproofness
title: PessimistStrategyproofness
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - PessimistStrategyproofness
uses:
  - VotingRule
  - Profile
  - Prefers
---

# PessimistStrategyproofness

## Lean type

```lean
def PessimistStrategyproofness (f : VotingRule N A) : Prop
```

## Dependencies

- VotingRule
- Profile
- Prefers
