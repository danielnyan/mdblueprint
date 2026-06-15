---
id: sample-zermelo-determinacy
title: sample_zermelo_determinacy
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.SimpleGameTree
  declarations:
    - sample_zermelo_determinacy
uses:
  - Strategy
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
  - IVariant
  - zermelo_determinacy
  - sample_zero_sum
---

# sample_zermelo_determinacy

## Lean type

```lean
theorem sample_zermelo_determinacy : (∀ σ' : Strategy Player ℚ, IVariant (1 : Player) optStrategy σ' → value₀ sample ≤ outcome σ' sample 0) ∧ (∀ σ' : Strategy Player ℚ, IVariant (0 : Player) optStrategy σ' → outcome σ' sample 0 ≤ value₀ sample)
```

## Dependencies

- Strategy
- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
- IVariant
- zermelo_determinacy
- sample_zero_sum
