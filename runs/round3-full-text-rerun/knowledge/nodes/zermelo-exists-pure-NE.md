---
id: zermelo-exists-pure-NE
title: zermelo_exists_pure_NE
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - zermelo_exists_pure_NE
uses:
  - Strategy
  - IsNashEquilibrium
  - Kuhn_exists_NE
---

# zermelo_exists_pure_NE

## Lean type

```lean
theorem zermelo_exists_pure_NE (g : GameTree (Fin 2) ℚ) : ∃ σ : Strategy (Fin 2) ℚ, IsNashEquilibrium σ g
```

## Dependencies

- Strategy
- IsNashEquilibrium
- Kuhn_exists_NE
