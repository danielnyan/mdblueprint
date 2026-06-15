---
id: constantProfile
title: constantProfile
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - constantProfile
uses:
  - Profile
---

# constantProfile

## Lean type

```lean
def constantProfile [Fintype N] [Fintype A] (r : LinearOrder A) : Profile N A
```

## Dependencies

- Profile
