---
id: gs-injective
title: gs_injective
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - gs_injective
uses:
  - final_all_women_hold
  - final_holding_injective
---

# gs_injective

## Lean type

```lean
lemma gs_injective : Function.Injective (gs w m)
```

## Dependencies

- final_all_women_hold
- final_holding_injective
