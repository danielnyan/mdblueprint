---
id: joinWoman-worse-right
title: joinWoman_worse_right
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - joinWoman_worse_right
uses:
  - wPartner_eq_iff
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - opposed_preferences
---

# joinWoman_worse_right

## Lean type

```lean
lemma joinWoman_worse_right {j i : Fin n} (hji : joinWoman μ ν hμ hν j = i) (hνji : mPartner ν hν i = j) : (w.prefs i).idxOf (mPartner μ hμ i) ≤ (w.prefs i).idxOf j
```

## Dependencies

- wPartner_eq_iff
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- opposed_preferences
