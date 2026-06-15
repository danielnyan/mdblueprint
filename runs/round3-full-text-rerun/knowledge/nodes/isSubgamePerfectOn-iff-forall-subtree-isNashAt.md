---
id: isSubgamePerfectOn-iff-forall-subtree-isNashAt
title: isSubgamePerfectOn_iff_forall_subtree_isNashAt
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTreeNE
  declarations:
    - isSubgamePerfectOn_iff_forall_subtree_isNashAt
uses:
  - Strategy
  - IsSubgamePerfectOn
  - IsNashAt
---

# isSubgamePerfectOn_iff_forall_subtree_isNashAt

## Lean type

```lean
theorem isSubgamePerfectOn_iff_forall_subtree_isNashAt {σ : Strategy N U} {g : GameTree N U} : IsSubgamePerfectOn σ g ↔ ∀ s : GameTree N U, Subtree s g → IsNashAt σ s
```

## Dependencies

- Strategy
- IsSubgamePerfectOn
- IsNashAt
