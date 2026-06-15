---
id: wPartner-eq-iff
title: wPartner_eq_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - wPartner_eq_iff
uses:
  - IsStable
---

# wPartner_eq_iff

## Lean type

```lean
lemma wPartner_eq_iff (μ : Matching (Fin n) (Fin n)) (hμ : Matching.IsStable (MatchingMarket.ofEquivData w m) μ) {i j : Fin n} : wPartner μ hμ j = i ↔ mPartner μ hμ i = j
```

## Dependencies

- IsStable
