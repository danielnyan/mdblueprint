---
id: joinWoman-injective
title: joinWoman_injective
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - joinWoman_injective
uses:
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - joinWoman_mem_men
  - joinWoman_worse_left
  - joinWoman_worse_right
  - pref_list_mem
---

# joinWoman_injective

## Lean type

```lean
lemma joinWoman_injective : Function.Injective (joinWoman μ ν hμ hν)
```

## Dependencies

- IsPositiveAffineOf.symm
- Indifferent.symm
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- joinWoman_mem_men
- joinWoman_worse_left
- joinWoman_worse_right
- pref_list_mem
