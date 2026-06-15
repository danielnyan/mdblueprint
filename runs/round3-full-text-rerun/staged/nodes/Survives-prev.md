---
id: Survives-prev
title: Survives.prev
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.IESDS
  declarations:
    - Survives.prev
uses:
  - Strategy
  - IsNashEquilibrium.survives
  - Survives
---

# Survives.prev

## Lean type

```lean
theorem Survives.prev {G : StrategicGame N U} {n : ℕ} {i : N} {s : G.strategy i} (h : G.Survives (n + 1) i s) : G.Survives n i s
```

## Dependencies

- Strategy
- IsNashEquilibrium.survives
- Survives
