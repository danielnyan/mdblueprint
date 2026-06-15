---
id: meetMan-worse-left
title: meetMan_worse_left
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - meetMan_worse_left
uses:
  - wPartner_eq_iff
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - pref_list_mem
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - opposed_preferences_women
---

# meetMan_worse_left

## Lean type

```lean
lemma meetMan_worse_left {i j : Fin n} (hij : meetMan μ ν hμ hν i = j) (hμij : wPartner μ hμ j = i) : (m.prefs j).idxOf (wPartner ν hν j) ≤ (m.prefs j).idxOf i
```

## Dependencies

- wPartner_eq_iff
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- pref_list_mem
- IsPositiveAffineOf.symm
- Indifferent.symm
- opposed_preferences_women
