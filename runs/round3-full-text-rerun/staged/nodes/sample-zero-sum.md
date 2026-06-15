---
id: sample-zero-sum
title: sample_zero_sum
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.SimpleGameTree
  declarations:
    - sample_zero_sum
uses:
  - IsZeroSum
  - zeroSumLeaf
  - Strategy
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
  - IsSubgamePerfect
  - Kuhn_exists_SPE
---

# sample_zero_sum

## Lean type

```lean
theorem sample_zero_sum : IsZeroSum sample
```

## Dependencies

- IsZeroSum
- zeroSumLeaf
- Strategy
- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
- IsSubgamePerfect
- Kuhn_exists_SPE
