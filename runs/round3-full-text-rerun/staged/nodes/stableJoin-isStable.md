---
id: stableJoin-isStable
title: stableJoin_isStable
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - stableJoin_isStable
uses:
  - IsStable
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - prefM_strict
  - prefW_strict
  - joinWoman_mem_men
  - joinWoman_le_left
  - joinWoman_le_right
---

# stableJoin_isStable

## Lean type

```lean
theorem stableJoin_isStable : Matching.IsStable (MatchingMarket.ofEquivData w m) (stableJoin μ ν hμ hν)
```

## Dependencies

- IsStable
- IsPositiveAffineOf.symm
- Indifferent.symm
- prefM_strict
- prefW_strict
- joinWoman_mem_men
- joinWoman_le_left
- joinWoman_le_right
