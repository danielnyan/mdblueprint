---
id: opposed-preferences
title: opposed_preferences
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - opposed_preferences
uses:
  - IsStable
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - pref_list_mem
  - stable_matching_perfect
---

# opposed_preferences

## Lean type

```lean
theorem opposed_preferences (μ : Matching (Fin n) (Fin n)) (hμ : Matching.IsStable (MatchingMarket.ofEquivData w m) μ) {j wj wj' m' : Fin n} (hμ_j : μ.matchW j = some wj') (hpref : (m.prefs j).idxOf wj < (m.prefs j).idxOf wj') (hμ_w : μ.matchM wj = some m') : (w.prefs wj).idxOf m' < (w.prefs wj).idxOf j
```

## Dependencies

- IsStable
- IsPositiveAffineOf.symm
- Indifferent.symm
- pref_list_mem
- stable_matching_perfect
