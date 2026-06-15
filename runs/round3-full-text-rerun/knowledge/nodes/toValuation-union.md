---
id: toValuation-union
title: toValuation_union
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Valuation
  declarations:
    - toValuation_union
uses:
  - toValuation
---

# toValuation_union

## Lean type

```lean
lemma toValuation_union [DecidableEq G] (w : AdditiveValuation N G) (i : N) (S T : Finset G) (h : Disjoint S T) : w.toValuation.val i (S ∪ T) = w.toValuation.val i S + w.toValuation.val i T
```

## Dependencies

- toValuation
