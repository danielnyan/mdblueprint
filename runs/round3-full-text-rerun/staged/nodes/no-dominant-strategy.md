---
id: no-dominant-strategy
title: no_dominant_strategy
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.FirstPrice
  declarations:
    - no_dominant_strategy
uses:
  - IsStrictlyDominant.isWeaklyDominant
  - IsWeaklyDominant
  - utility_winner
---

# no_dominant_strategy

## Lean type

```lean
theorem no_dominant_strategy (v : I → U) (i : I) (bi : U) (ha : ∃ a : U, 0 < a) : ¬ IsWeaklyDominant (game v) i bi
```

## Dependencies

- IsStrictlyDominant.isWeaklyDominant
- IsWeaklyDominant
- utility_winner
