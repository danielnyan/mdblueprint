---
id: joinWoman-eq-or
title: joinWoman_eq_or
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - joinWoman_eq_or
uses:
---

# joinWoman_eq_or

## Lean type

```lean
lemma joinWoman_eq_or (j : Fin n) : joinWoman μ ν hμ hν j = wPartner μ hμ j ∨ joinWoman μ ν hμ hν j = wPartner ν hν j
```

## Dependencies

- none
