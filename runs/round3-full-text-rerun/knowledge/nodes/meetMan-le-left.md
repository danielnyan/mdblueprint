---
id: meetMan-le-left
title: meetMan_le_left
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - meetMan_le_left
uses:
---

# meetMan_le_left

## Lean type

```lean
lemma meetMan_le_left (i : Fin n) : (w.prefs i).idxOf (meetMan μ ν hμ hν i) ≤ (w.prefs i).idxOf (mPartner μ hμ i)
```

## Dependencies

- none
