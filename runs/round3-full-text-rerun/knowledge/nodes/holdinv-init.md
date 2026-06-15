---
id: holdinv-init
title: holdinv_init
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - holdinv_init
uses:
  - HoldInv
  - initState
---

# holdinv_init

## Lean type

```lean
lemma holdinv_init (m : Preferences n) : HoldInv m (initState n)
```

## Dependencies

- HoldInv
- initState
