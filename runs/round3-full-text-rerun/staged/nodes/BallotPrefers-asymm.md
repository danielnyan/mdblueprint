---
id: BallotPrefers-asymm
title: BallotPrefers.asymm
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - BallotPrefers.asymm
uses:
  - BallotPrefers
---

# BallotPrefers.asymm

## Lean type

```lean
theorem BallotPrefers.asymm (r : LinearOrder A) {a b : A} : BallotPrefers r a b → ¬ BallotPrefers r b a
```

## Dependencies

- BallotPrefers
