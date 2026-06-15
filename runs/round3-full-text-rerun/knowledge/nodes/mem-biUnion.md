---
id: mem-biUnion
title: mem_biUnion
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Basic
  declarations:
    - mem_biUnion
uses:
---

# mem_biUnion

## Lean type

```lean
lemma mem_biUnion (h : IsAllocation allGoods A) (g : G) (hg : g ∈ allGoods) : ∃ i : N, g ∈ A i
```

## Dependencies

- none
