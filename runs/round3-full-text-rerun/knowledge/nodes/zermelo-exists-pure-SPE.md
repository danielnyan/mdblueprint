---
id: zermelo-exists-pure-SPE
title: zermelo_exists_pure_SPE
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - zermelo_exists_pure_SPE
uses:
  - Strategy
  - IsSubgamePerfectOn
  - Kuhn_exists_SPE_on
---

# zermelo_exists_pure_SPE

## Lean type

```lean
theorem zermelo_exists_pure_SPE (g : GameTree (Fin 2) ℚ) : ∃ σ : Strategy (Fin 2) ℚ, IsSubgamePerfectOn σ g
```

## Dependencies

- Strategy
- IsSubgamePerfectOn
- Kuhn_exists_SPE_on
