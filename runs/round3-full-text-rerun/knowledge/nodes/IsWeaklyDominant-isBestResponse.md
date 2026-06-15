---
id: IsWeaklyDominant-isBestResponse
title: IsWeaklyDominant.isBestResponse
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Dominance
  declarations:
    - IsWeaklyDominant.isBestResponse
uses:
  - Strategy
  - IsStrictlyDominant.isWeaklyDominant
  - IsWeaklyDominant
  - Profile
  - IsBestResponse
  - deviate_self
---

# IsWeaklyDominant.isBestResponse

## Lean type

```lean
theorem IsWeaklyDominant.isBestResponse {G : StrategicGame N U} {i : N} {s : G.strategy i} (hdom : IsWeaklyDominant G i s) (σ : G.Profile) (hσ : σ i = s) : IsBestResponse G σ i
```

## Dependencies

- Strategy
- IsStrictlyDominant.isWeaklyDominant
- IsWeaklyDominant
- Profile
- IsBestResponse
- deviate_self
