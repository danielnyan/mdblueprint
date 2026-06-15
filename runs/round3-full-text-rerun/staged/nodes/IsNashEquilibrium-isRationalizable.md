---
id: IsNashEquilibrium-isRationalizable
title: IsNashEquilibrium.isRationalizable
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.IESDS
  declarations:
    - IsNashEquilibrium.isRationalizable
uses:
  - Profile
  - IsNashEquilibrium
  - IsRationalizable
  - IsNashEquilibrium.survives
  - Survives
---

# IsNashEquilibrium.isRationalizable

## Lean type

```lean
theorem IsNashEquilibrium.isRationalizable {G : StrategicGame N U} {σ : G.Profile} (hN : IsNashEquilibrium G σ) (i : N) : G.IsRationalizable i (σ i)
```

## Dependencies

- Profile
- IsNashEquilibrium
- IsRationalizable
- IsNashEquilibrium.survives
- Survives
