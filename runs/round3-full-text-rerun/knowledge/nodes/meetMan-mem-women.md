---
id: meetMan-mem-women
title: meetMan_mem_women
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - meetMan_mem_women
uses:
  - meetMan_eq_or
  - wPartner_eq_iff
---

# meetMan_mem_women

## Lean type

```lean
lemma meetMan_mem_women {i j : Fin n} (h : meetMan μ ν hμ hν i = j) : wPartner μ hμ j = i ∨ wPartner ν hν j = i
```

## Dependencies

- meetMan_eq_or
- wPartner_eq_iff
