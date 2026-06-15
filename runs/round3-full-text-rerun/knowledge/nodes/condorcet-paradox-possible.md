---
id: condorcet-paradox-possible
title: condorcet_paradox_possible
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - condorcet_paradox_possible
uses:
  - Profile
  - HasCondorcetWinner
---

# condorcet_paradox_possible

## Lean type

```lean
theorem condorcet_paradox_possible : ∃ P : Profile (Fin 3) (Fin 3), ¬ HasCondorcetWinner P
```

## Dependencies

- Profile
- HasCondorcetWinner
