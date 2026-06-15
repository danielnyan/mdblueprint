---
id: matchW-partner
title: matchW_partner
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - matchW_partner
uses:
  - StableMatching
  - pref_list_mem
  - Profile.ext
  - stableJoin_isStable
  - stableMeet_isStable
  - joinWoman_le_left
  - joinWoman_le_right
  - joinWoman_eq_or
  - stableMeet_ge_left
  - stableMeet_ge_right
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - meetEquiv_symm_eq_or
  - gs_bijective
  - galeShapley_isStable
---

# matchW_partner

## Lean type

```lean
lemma matchW_partner (μ : StableMatching w m) (j : Fin n) : μ.1.matchW j = some (μ.partner j)
```

## Dependencies

- StableMatching
- pref_list_mem
- Profile.ext
- stableJoin_isStable
- stableMeet_isStable
- joinWoman_le_left
- joinWoman_le_right
- joinWoman_eq_or
- stableMeet_ge_left
- stableMeet_ge_right
- IsPositiveAffineOf.symm
- Indifferent.symm
- meetEquiv_symm_eq_or
- gs_bijective
- galeShapley_isStable
