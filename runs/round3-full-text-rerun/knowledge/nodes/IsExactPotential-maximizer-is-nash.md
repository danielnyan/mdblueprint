---
id: IsExactPotential-maximizer-is-nash
title: IsExactPotential.maximizer_is_nash
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.PotentialGame
  declarations:
    - IsExactPotential.maximizer_is_nash
uses:
  - Profile
  - IsExactPotential
  - IsNashEquilibrium
---

# IsExactPotential.maximizer_is_nash

## Lean type

```lean
theorem IsExactPotential.maximizer_is_nash {Φ : G.Profile → U} (hΦ : IsExactPotential G Φ) {σ : G.Profile} (hmax : ∀ τ : G.Profile, Φ σ ≥ Φ τ) : IsNashEquilibrium G σ
```

## Dependencies

- Profile
- IsExactPotential
- IsNashEquilibrium
