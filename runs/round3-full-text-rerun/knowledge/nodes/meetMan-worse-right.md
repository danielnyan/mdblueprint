---
id: meetMan-worse-right
title: meetMan_worse_right
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - meetMan_worse_right
uses:
  - wPartner_eq_iff
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - opposed_preferences_women
---

# meetMan_worse_right

## Lean type

```lean
lemma meetMan_worse_right {i j : Fin n} (hij : meetMan μ ν hμ hν i = j) (hνij : wPartner ν hν j = i) : (m.prefs j).idxOf (wPartner μ hμ j) ≤ (m.prefs j).idxOf i
```

## Dependencies

- wPartner_eq_iff
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- opposed_preferences_women
