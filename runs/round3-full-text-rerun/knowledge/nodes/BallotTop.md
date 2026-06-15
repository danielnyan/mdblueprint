---
id: BallotTop
title: BallotTop
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - BallotTop
uses:
  - BallotPrefers
---

# BallotTop

## Lean type

```lean
def BallotTop (r : LinearOrder A) (a : A) : Prop
```

## Dependencies

- BallotPrefers
