---
id: toValuation-mono
title: toValuation_mono
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Valuation
  declarations:
    - toValuation_mono
uses:
  - toValuation
---

# toValuation_mono

## Lean type

```lean
lemma toValuation_mono [DecidableEq G] (w : AdditiveValuation N G) (hnn : ∀ (i : N) (g : G), 0 ≤ w.weight i g) (i : N) {S T : Finset G} (h : T ⊆ S) : w.toValuation.val i T ≤ w.toValuation.val i S
```

## Dependencies

- toValuation
