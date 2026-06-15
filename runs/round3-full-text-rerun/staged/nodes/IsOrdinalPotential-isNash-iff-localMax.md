---
id: IsOrdinalPotential-isNash-iff-localMax
title: IsOrdinalPotential.isNash_iff_localMax
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.PotentialGame
  declarations:
    - IsOrdinalPotential.isNash_iff_localMax
uses:
  - Profile
  - IsOrdinalPotential
  - IsNashEquilibrium
  - Strategy
---

# IsOrdinalPotential.isNash_iff_localMax

## Lean type

```lean
theorem IsOrdinalPotential.isNash_iff_localMax {Φ : G.Profile → U} (hΦ : IsOrdinalPotential G Φ) {σ : G.Profile} : IsNashEquilibrium G σ ↔ ∀ i (s' : G.strategy i), Φ σ ≥ Φ (deviate σ i s')
```

## Dependencies

- Profile
- IsOrdinalPotential
- IsNashEquilibrium
- Strategy
