---
id: meetEquiv-symm-eq-or
title: meetEquiv_symm_eq_or
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - meetEquiv_symm_eq_or
uses:
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - meetMan_mem_women
---

# meetEquiv_symm_eq_or

## Lean type

```lean
lemma meetEquiv_symm_eq_or (j : Fin n) : (meetEquiv μ ν hμ hν).symm j = wPartner μ hμ j ∨ (meetEquiv μ ν hμ hν).symm j = wPartner ν hν j
```

## Dependencies

- IsPositiveAffineOf.symm
- Indifferent.symm
- meetMan_mem_women
