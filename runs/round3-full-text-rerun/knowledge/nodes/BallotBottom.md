---
id: BallotBottom
title: BallotBottom
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - BallotBottom
uses:
  - BallotPrefers
  - Profile
---

# BallotBottom

## Lean type

```lean
def BallotBottom (r : LinearOrder A) (a : A) : Prop
```

## Dependencies

- BallotPrefers
- Profile
