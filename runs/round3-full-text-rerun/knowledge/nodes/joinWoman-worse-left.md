---
id: joinWoman-worse-left
title: joinWoman_worse_left
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - joinWoman_worse_left
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
  - opposed_preferences
---

# joinWoman_worse_left

## Lean type

```lean
lemma joinWoman_worse_left {j i : Fin n} (hji : joinWoman μ ν hμ hν j = i) (hμji : mPartner μ hμ i = j) : (w.prefs i).idxOf (mPartner ν hν i) ≤ (w.prefs i).idxOf j
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
- opposed_preferences
