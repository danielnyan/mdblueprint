---
id: candidateChoice-has-spe
title: candidateChoice_has_spe
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CandidateChoice
  declarations:
    - candidateChoice_has_spe
uses:
  - Strategy
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
  - IsSubgamePerfect
  - Kuhn_exists_SPE
---

# candidateChoice_has_spe

## Lean type

```lean
theorem candidateChoice_has_spe : ∃ σ : Strategy Player ℚ, IsSubgamePerfect σ
```

## Dependencies

- Strategy
- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
- IsSubgamePerfect
- Kuhn_exists_SPE
