---
id: stableMeet-ge-left
title: stableMeet_ge_left
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - stableMeet_ge_left
uses:
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - meetMan_mem_women
  - meetMan_worse_right
---

# stableMeet_ge_left

## Lean type

```lean
lemma stableMeet_ge_left (j : Fin n) : (m.prefs j).idxOf (wPartner μ hμ j) ≤ (m.prefs j).idxOf ((meetEquiv μ ν hμ hν).symm j)
```

## Dependencies

- IsPositiveAffineOf.symm
- Indifferent.symm
- meetMan_mem_women
- meetMan_worse_right
