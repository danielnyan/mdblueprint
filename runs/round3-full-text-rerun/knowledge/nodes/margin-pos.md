---
id: margin-pos
title: margin_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - margin_pos
uses:
  - Profile
---

# margin_pos

## Lean type

```lean
def margin_pos [Fintype N] [Fintype A] (P : Profile N A) (a b : A) : Prop
```

## Dependencies

- Profile
