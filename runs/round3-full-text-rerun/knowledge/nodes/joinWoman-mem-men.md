---
id: joinWoman-mem-men
title: joinWoman_mem_men
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - joinWoman_mem_men
uses:
  - joinWoman_eq_or
  - wPartner_eq_iff
---

# joinWoman_mem_men

## Lean type

```lean
lemma joinWoman_mem_men {j i : Fin n} (h : joinWoman μ ν hμ hν j = i) : mPartner μ hμ i = j ∨ mPartner ν hν i = j
```

## Dependencies

- joinWoman_eq_or
- wPartner_eq_iff
