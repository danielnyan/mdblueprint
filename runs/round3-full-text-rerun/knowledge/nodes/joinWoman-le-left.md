---
id: joinWoman-le-left
title: joinWoman_le_left
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - joinWoman_le_left
uses:
---

# joinWoman_le_left

## Lean type

```lean
lemma joinWoman_le_left (j : Fin n) : (m.prefs j).idxOf (joinWoman μ ν hμ hν j) ≤ (m.prefs j).idxOf (wPartner μ hμ j)
```

## Dependencies

- none
