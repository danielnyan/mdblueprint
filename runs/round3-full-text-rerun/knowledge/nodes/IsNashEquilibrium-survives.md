---
id: IsNashEquilibrium-survives
title: IsNashEquilibrium.survives
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.IESDS
  declarations:
    - IsNashEquilibrium.survives
uses:
  - Profile
  - IsNashEquilibrium
  - Survives
  - deviate_self
---

# IsNashEquilibrium.survives

## Lean type

```lean
theorem IsNashEquilibrium.survives {G : StrategicGame N U} {σ : G.Profile} (hN : IsNashEquilibrium G σ) : ∀ (n : ℕ) (i : N), G.Survives n i (σ i)
```

## Dependencies

- Profile
- IsNashEquilibrium
- Survives
- deviate_self
