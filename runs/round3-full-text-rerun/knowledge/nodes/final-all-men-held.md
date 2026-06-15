---
id: final-all-men-held
title: final_all_men_held
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - final_all_men_held
uses:
  - finalState
  - not_isFree_iff
  - finalState_no_free_men
---

# final_all_men_held

## Lean type

```lean
lemma final_all_men_held : ∀ i : Fin n, ∃ j : Fin n, (finalState w m).holding j = some i
```

## Dependencies

- finalState
- not_isFree_iff
- finalState_no_free_men
