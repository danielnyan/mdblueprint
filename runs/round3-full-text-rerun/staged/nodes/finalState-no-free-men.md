---
id: finalState-no-free-men
title: finalState_no_free_men
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - finalState_no_free_men
uses:
  - isFree
  - finalState
  - initState
  - initState_injective
  - freeMenSet
  - mem_freeMenSet
---

# finalState_no_free_men

## Lean type

```lean
lemma finalState_no_free_men : ∀ i : Fin n, isFree (finalState w m) i = false
```

## Dependencies

- isFree
- finalState
- initState
- initState_injective
- freeMenSet
- mem_freeMenSet
