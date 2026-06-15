---
id: final-holding-injective
title: final_holding_injective
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - final_holding_injective
uses:
  - finalState
  - holding_injective_run
  - initState
  - initState_injective
---

# final_holding_injective

## Lean type

```lean
lemma final_holding_injective : ∀ j1 j2 : Fin n, ∀ i : Fin n, (finalState w m).holding j1 = some i → (finalState w m).holding j2 = some i → j1 = j2
```

## Dependencies

- finalState
- holding_injective_run
- initState
- initState_injective
