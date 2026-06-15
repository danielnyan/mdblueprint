---
id: opposed-preferences-women
title: opposed_preferences_women
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - opposed_preferences_women
uses:
  - IsStable
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - pref_list_mem
---

# opposed_preferences_women

## Lean type

```lean
theorem opposed_preferences_women (candidate : Matching (Fin n) (Fin n)) (hcandidate : Matching.IsStable (MatchingMarket.ofEquivData w m) candidate) {i mi mi' j' : Fin n} (hcandidate_i : candidate.matchM i = some mi') (hpref : (w.prefs i).idxOf mi < (w.prefs i).idxOf mi') (hcandidate_m : candidate.matchW mi = some j') : (m.prefs mi).idxOf j' < (m.prefs mi).idxOf i
```

## Dependencies

- IsStable
- IsPositiveAffineOf.symm
- Indifferent.symm
- pref_list_mem
