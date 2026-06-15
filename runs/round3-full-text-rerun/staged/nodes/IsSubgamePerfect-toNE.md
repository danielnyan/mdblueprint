---
id: IsSubgamePerfect-toNE
title: IsSubgamePerfect.toNE
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTreeNE
  declarations:
    - IsSubgamePerfect.toNE
uses:
  - Strategy
  - IsSubgamePerfect
  - IsNashEquilibrium
---

# IsSubgamePerfect.toNE

## Lean type

```lean
theorem IsSubgamePerfect.toNE {σ : Strategy N U} (hspe : IsSubgamePerfect σ) (g : GameTree N U) : IsNashEquilibrium σ g
```

## Dependencies

- Strategy
- IsSubgamePerfect
- IsNashEquilibrium
