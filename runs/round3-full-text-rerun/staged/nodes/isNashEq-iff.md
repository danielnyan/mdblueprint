---
id: isNashEq-iff
title: isNashEq_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Checker
  declarations:
    - isNashEq_iff
uses:
  - Strategy
  - Profile
  - isNashEq
  - IsNashEquilibrium
  - IsWeaklyDominant.isBestResponse
  - IsBestResponse
---

# isNashEq_iff

## Lean type

```lean
theorem isNashEq_iff [Fintype N] (G : StrategicGame N U) [∀ i, Fintype (G.strategy i)] (σ : G.Profile) : isNashEq G σ = true ↔ IsNashEquilibrium G σ
```

## Dependencies

- Strategy
- Profile
- isNashEq
- IsNashEquilibrium
- IsWeaklyDominant.isBestResponse
- IsBestResponse
