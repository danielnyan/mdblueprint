---
id: candidateChoice-has-ne
title: candidateChoice_has_ne
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CandidateChoice
  declarations:
    - candidateChoice_has_ne
uses:
  - Strategy
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
  - IsNashEquilibrium
  - candidateChoiceGame
  - Kuhn_exists_NE
---

# candidateChoice_has_ne

## Lean type

```lean
theorem candidateChoice_has_ne : ∃ σ : Strategy Player ℚ, IsNashEquilibrium σ candidateChoiceGame
```

## Dependencies

- Strategy
- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
- IsNashEquilibrium
- candidateChoiceGame
- Kuhn_exists_NE
