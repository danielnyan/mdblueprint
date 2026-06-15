---
id: stableMeet-ge-right
title: stableMeet_ge_right
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - stableMeet_ge_right
uses:
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - meetMan_mem_women
  - meetMan_worse_left
---

# stableMeet_ge_right

## Lean type

```lean
lemma stableMeet_ge_right (j : Fin n) : (m.prefs j).idxOf (wPartner ν hν j) ≤ (m.prefs j).idxOf ((meetEquiv μ ν hμ hν).symm j)
```

## Dependencies

- IsPositiveAffineOf.symm
- Indifferent.symm
- meetMan_mem_women
- meetMan_worse_left
