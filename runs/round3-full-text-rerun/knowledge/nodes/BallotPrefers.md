---
id: BallotPrefers
title: BallotPrefers
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - BallotPrefers
uses:
  - ballotLT
  - ballotLE
---

# BallotPrefers

## Lean type

```lean
def BallotPrefers (r : LinearOrder A) (a b : A) : Prop
```

## Dependencies

- ballotLT
- ballotLE
