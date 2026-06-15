---
id: galeShapley-isProposingOptimal
title: galeShapley_isProposingOptimal
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Optimal
  declarations:
    - galeShapley_isProposingOptimal
uses:
  - IsStable
  - gs_bijective
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - IsAchievable
  - finalState
  - final_all_women_hold
  - pref_list_mem
  - holdinv_finalState
  - finalState_NoAchievableRejection
  - final_holding_injective
---

# galeShapley_isProposingOptimal

## Lean type

```lean
theorem galeShapley_isProposingOptimal (μ : Matching (Fin n) (Fin n)) (hμ : Matching.IsStable (MatchingMarket.ofEquivData w m) μ) : ∀ (j wj : Fin n), μ.matchW j = some wj → (m.prefs j).idxOf ((Equiv.ofBijective (gs w m) (gs_bijective w m)).symm j) ≤ (m.prefs j).idxOf wj
```

## Dependencies

- IsStable
- gs_bijective
- IsPositiveAffineOf.symm
- Indifferent.symm
- IsAchievable
- finalState
- final_all_women_hold
- pref_list_mem
- holdinv_finalState
- finalState_NoAchievableRejection
- final_holding_injective
