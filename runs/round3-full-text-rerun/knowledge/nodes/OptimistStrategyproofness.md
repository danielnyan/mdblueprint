---
id: OptimistStrategyproofness
title: OptimistStrategyproofness
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - OptimistStrategyproofness
uses:
  - VotingRule
  - Profile
  - Prefers
---

# OptimistStrategyproofness

## Lean type

```lean
def OptimistStrategyproofness (f : VotingRule N A) : Prop
```

## Dependencies

- VotingRule
- Profile
- Prefers
