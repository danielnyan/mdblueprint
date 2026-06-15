---
id: of-dominant
title: of_dominant
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.NashEquilibrium
  declarations:
    - of_dominant
uses:
  - Profile
  - IsStrictlyDominant.isWeaklyDominant
  - IsWeaklyDominant
  - IsNashEquilibrium
  - IsWeaklyDominant.isBestResponse
  - IsBestResponse
---

# of_dominant

## Lean type

```lean
theorem of_dominant {G : StrategicGame N U} {σ : G.Profile} (h : ∀ i : N, IsWeaklyDominant G i (σ i)) : IsNashEquilibrium G σ
```

## Dependencies

- Profile
- IsStrictlyDominant.isWeaklyDominant
- IsWeaklyDominant
- IsNashEquilibrium
- IsWeaklyDominant.isBestResponse
- IsBestResponse
