---
id: BallotPrefers-total-of-ne
title: BallotPrefers.total_of_ne
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - BallotPrefers.total_of_ne
uses:
  - BallotPrefers
  - ballotLT
---

# BallotPrefers.total_of_ne

## Lean type

```lean
theorem BallotPrefers.total_of_ne (r : LinearOrder A) {a b : A} (hne : a ≠ b) : BallotPrefers r a b ∨ BallotPrefers r b a
```

## Dependencies

- BallotPrefers
- ballotLT
