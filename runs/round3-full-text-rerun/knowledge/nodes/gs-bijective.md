---
id: gs-bijective
title: gs_bijective
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - gs_bijective
uses:
  - gs_injective
---

# gs_bijective

## Lean type

```lean
lemma gs_bijective : Function.Bijective (gs w m)
```

## Dependencies

- gs_injective
