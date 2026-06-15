---
id: Kuhn-exists-SPE
title: Kuhn_exists_SPE
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTreeSPE
  declarations:
    - Kuhn_exists_SPE
uses:
  - Strategy
  - IsSubgamePerfect
  - optStrategy_isSubgamePerfect
---

# Kuhn_exists_SPE

## Lean type

```lean
theorem Kuhn_exists_SPE [DecidableLE U] : ∃ σ : Strategy N U, IsSubgamePerfect σ
```

## Dependencies

- Strategy
- IsSubgamePerfect
- optStrategy_isSubgamePerfect
