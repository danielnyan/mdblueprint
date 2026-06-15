---
id: joinWoman-le-right
title: joinWoman_le_right
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - joinWoman_le_right
uses:
---

# joinWoman_le_right

## Lean type

```lean
lemma joinWoman_le_right (j : Fin n) : (m.prefs j).idxOf (joinWoman μ ν hμ hν j) ≤ (m.prefs j).idxOf (wPartner ν hν j)
```

## Dependencies

- none
