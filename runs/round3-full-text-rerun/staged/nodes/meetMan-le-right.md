---
id: meetMan-le-right
title: meetMan_le_right
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - meetMan_le_right
uses:
---

# meetMan_le_right

## Lean type

```lean
lemma meetMan_le_right (i : Fin n) : (w.prefs i).idxOf (meetMan μ ν hμ hν i) ≤ (w.prefs i).idxOf (mPartner ν hν i)
```

## Dependencies

- none
