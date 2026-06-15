---
id: holdinv-finalState
title: holdinv_finalState
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - holdinv_finalState
uses:
  - HoldInv
  - finalState
  - initState
  - holdinv_init
  - initState_injective
  - pref_list_mem
---

# holdinv_finalState

## Lean type

```lean
lemma holdinv_finalState (w m : Preferences n) : HoldInv m (finalState w m)
```

## Dependencies

- HoldInv
- finalState
- initState
- holdinv_init
- initState_injective
- pref_list_mem
