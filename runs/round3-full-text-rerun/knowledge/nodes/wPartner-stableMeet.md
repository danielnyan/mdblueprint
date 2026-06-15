---
id: wPartner-stableMeet
title: wPartner_stableMeet
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - wPartner_stableMeet
uses:
  - stableMeet_isStable
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# wPartner_stableMeet

## Lean type

```lean
lemma wPartner_stableMeet (j : Fin n) : wPartner (stableMeet μ ν hμ hν) (stableMeet_isStable μ ν hμ hν) j = (meetEquiv μ ν hμ hν).symm j
```

## Dependencies

- stableMeet_isStable
- IsPositiveAffineOf.symm
- Indifferent.symm
