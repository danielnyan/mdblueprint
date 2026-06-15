---
id: prefM-strict
title: prefM_strict
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - prefM_strict
uses:
---

# prefM_strict

## Lean type

```lean
lemma prefM_strict {i a b : Fin n} : strict ((MatchingMarket.ofEquivData w m).prefM i).rel (some a) (some b) ↔ (w.prefs i).idxOf a < (w.prefs i).idxOf b
```

## Dependencies

- none
