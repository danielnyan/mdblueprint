---
id: final-all-women-hold
title: final_all_women_hold
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - final_all_women_hold
uses:
  - finalState
  - final_all_men_held
  - final_holding_injective
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - Pos
---

# final_all_women_hold

## Lean type

```lean
lemma final_all_women_hold : ∀ j : Fin n, ∃ i : Fin n, (finalState w m).holding j = some i
```

## Dependencies

- finalState
- final_all_men_held
- final_holding_injective
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- Pos
