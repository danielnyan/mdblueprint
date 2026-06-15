---
id: gsStable-greatest
title: gsStable_greatest
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - gsStable_greatest
uses:
  - StableMatching
  - gs_bijective
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - galeShapley_isProposingOptimal
  - matchW_partner
---

# gsStable_greatest

## Lean type

```lean
theorem gsStable_greatest [NeZero n] (μ : StableMatching w m) : μ ≤ gsStable w m
```

## Dependencies

- StableMatching
- gs_bijective
- IsPositiveAffineOf.symm
- Indifferent.symm
- galeShapley_isProposingOptimal
- matchW_partner
