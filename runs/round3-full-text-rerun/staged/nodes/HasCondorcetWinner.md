---
id: HasCondorcetWinner
title: HasCondorcetWinner
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - HasCondorcetWinner
uses:
  - Profile
  - CondorcetWinner
---

# HasCondorcetWinner

## Lean type

```lean
def HasCondorcetWinner [Fintype N] [Fintype A] (P : Profile N A) : Prop
```

## Dependencies

- Profile
- CondorcetWinner
