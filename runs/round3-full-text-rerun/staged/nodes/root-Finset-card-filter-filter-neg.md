---
id: root-Finset-card-filter-filter-neg
title: _root_.Finset.card_filter_filter_neg
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - _root_.Finset.card_filter_filter_neg
uses:
---

# _root_.Finset.card_filter_filter_neg

## Lean type

```lean
theorem _root_.Finset.card_filter_filter_neg {X : Type*} (s : Finset X) (p : X → Prop) [DecidablePred p] : s.card = (Finset.filter p s).card + (Finset.filter (fun (a : X) => ¬p a) s).card
```

## Dependencies

- none
