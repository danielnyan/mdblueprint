---
id: prefW-strict
title: prefW_strict
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - prefW_strict
uses:
  - joinWoman_injective
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# prefW_strict

## Lean type

```lean
lemma prefW_strict {j a b : Fin n} : strict ((MatchingMarket.ofEquivData w m).prefW j).rel (some a) (some b) ↔ (m.prefs j).idxOf a < (m.prefs j).idxOf b
```

## Dependencies

- joinWoman_injective
- IsPositiveAffineOf.symm
- Indifferent.symm
