---
id: top-unanimity-of-unanimity
title: top_unanimity_of_unanimity
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - top_unanimity_of_unanimity
uses:
  - VotingRule
  - IsTotal
  - Unanimity
  - Profile
  - TopRank
---

# top_unanimity_of_unanimity

## Lean type

```lean
theorem top_unanimity_of_unanimity [Nonempty A] {f : VotingRule N A} (hf : IsTotal f) (hU : Unanimity f) : ∀ (P : Profile N A) (a : A), (∀ i : N, TopRank P i a) → f P = {a}
```

## Dependencies

- VotingRule
- IsTotal
- Unanimity
- Profile
- TopRank
