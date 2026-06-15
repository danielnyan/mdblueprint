---
id: stable-matching-perfect
title: stable_matching_perfect
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.RuralHospitals
  declarations:
    - stable_matching_perfect
uses:
  - IsStable
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# stable_matching_perfect

## Lean type

```lean
theorem stable_matching_perfect (μ : Matching (Fin n) (Fin n)) (hμ : Matching.IsStable (MatchingMarket.ofEquivData w m) μ) : (∀ i : Fin n, (μ.matchM i).isSome) ∧ (∀ j : Fin n, (μ.matchW j).isSome)
```

## Dependencies

- IsStable
- IsPositiveAffineOf.symm
- Indifferent.symm
