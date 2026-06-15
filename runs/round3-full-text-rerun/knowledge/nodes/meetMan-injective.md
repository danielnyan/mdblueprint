---
id: meetMan-injective
title: meetMan_injective
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.Lattice
  declarations:
    - meetMan_injective
uses:
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - meetMan_mem_women
  - meetMan_worse_left
  - meetMan_worse_right
  - pref_list_mem
---

# meetMan_injective

## Lean type

```lean
lemma meetMan_injective : Function.Injective (meetMan μ ν hμ hν)
```

## Dependencies

- IsPositiveAffineOf.symm
- Indifferent.symm
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- meetMan_mem_women
- meetMan_worse_left
- meetMan_worse_right
- pref_list_mem
