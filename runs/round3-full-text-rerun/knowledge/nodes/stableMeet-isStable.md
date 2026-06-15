---
id: stableMeet-isStable
title: stableMeet_isStable
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - stableMeet_isStable
uses:
  - IsStable
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - prefM_strict
  - prefW_strict
  - meetMan_mem_women
  - meetMan_le_left
  - meetMan_le_right
---

# stableMeet_isStable

## Lean type

```lean
theorem stableMeet_isStable : Matching.IsStable (MatchingMarket.ofEquivData w m) (stableMeet μ ν hμ hν)
```

## Dependencies

- IsStable
- IsPositiveAffineOf.symm
- Indifferent.symm
- prefM_strict
- prefW_strict
- meetMan_mem_women
- meetMan_le_left
- meetMan_le_right
