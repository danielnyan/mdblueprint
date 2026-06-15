---
id: BallotPrefers-ballotFromInjective
title: BallotPrefers_ballotFromInjective
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - BallotPrefers_ballotFromInjective
uses:
  - BallotPrefers
  - ballotLT
---

# BallotPrefers_ballotFromInjective

## Lean type

```lean
@[simp] theorem BallotPrefers_ballotFromInjective {B : Type*} (rB : LinearOrder B) (f : A → B) (hf : Function.Injective f) (a b : A) : BallotPrefers (ballotFromInjective rB f hf) a b ↔ @LT.lt B (ballotLT rB) (f a) (f b)
```

## Dependencies

- BallotPrefers
- ballotLT
