---
id: CondorcetConsistency
title: CondorcetConsistency
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - CondorcetConsistency
uses:
  - VotingRule
  - Profile
  - CondorcetWinner
---

# CondorcetConsistency

## Lean type

```lean
def CondorcetConsistency [Fintype N] [Fintype A] (f : VotingRule N A) : Prop
```

## Dependencies

- VotingRule
- Profile
- CondorcetWinner
