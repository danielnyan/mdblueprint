---
id: Survives-mono
title: Survives.mono
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.IESDS
  declarations:
    - Survives.mono
uses:
  - Strategy
  - IsNashEquilibrium.survives
  - Survives
  - IsPositiveAffineOf.refl
  - Indifferent.refl
  - IVariant.refl
  - Arena.Reachable.step
  - CPState.step
  - Survives.prev
---

# Survives.mono

## Lean type

```lean
theorem Survives.mono {G : StrategicGame N U} {m n : ℕ} (hmn : m ≤ n) {i : N} {s : G.strategy i} (h : G.Survives n i s) : G.Survives m i s
```

## Dependencies

- Strategy
- IsNashEquilibrium.survives
- Survives
- IsPositiveAffineOf.refl
- Indifferent.refl
- IVariant.refl
- Arena.Reachable.step
- CPState.step
- Survives.prev
