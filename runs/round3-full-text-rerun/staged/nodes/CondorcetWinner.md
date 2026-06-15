---
id: CondorcetWinner
title: CondorcetWinner
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - CondorcetWinner
uses:
  - Profile
  - MajorityPrefers
---

# CondorcetWinner

## Lean type

```lean
def CondorcetWinner [Fintype N] [Fintype A] (P : Profile N A) (a : A) : Prop
```

## Dependencies

- Profile
- MajorityPrefers
