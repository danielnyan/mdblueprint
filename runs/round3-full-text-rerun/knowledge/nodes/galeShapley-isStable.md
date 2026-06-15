---
id: galeShapley-isStable
title: galeShapley_isStable
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - galeShapley_isStable
uses:
  - IsStable
  - gs_bijective
  - IsBlocking
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - finalState
  - final_all_women_hold
  - holdinv_finalState
  - pref_list_mem
---

# galeShapley_isStable

## Lean type

```lean
theorem galeShapley_isStable : Matching.IsStable (MatchingMarket.ofEquivData w m) (Matching.ofGS (gs w m) (gs_bijective w m))
```

## Dependencies

- IsStable
- gs_bijective
- IsBlocking
- IsPositiveAffineOf.symm
- Indifferent.symm
- finalState
- final_all_women_hold
- holdinv_finalState
- pref_list_mem
