---
id: MajorityPrefers
title: MajorityPrefers
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - MajorityPrefers
uses:
  - Profile
  - margin_pos
---

# MajorityPrefers

## Lean type

```lean
def MajorityPrefers [Fintype N] [Fintype A] (P : Profile N A) (a b : A) : Prop
```

## Dependencies

- Profile
- margin_pos
