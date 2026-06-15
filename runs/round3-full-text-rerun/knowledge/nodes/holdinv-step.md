---
id: holdinv-step
title: holdinv_step
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - holdinv_step
uses:
  - HoldInv
  - daStep_holding
  - isFree
  - propTarget
  - not_isFree_iff
  - daStep_nc_held
  - daStep_nc_free
  - pref_list_mem
---

# holdinv_step

## Lean type

```lean
lemma holdinv_step (w m : Preferences n) (s : DAState n) (hhold : HoldInv m s) : HoldInv m (daStep w m s)
```

## Dependencies

- HoldInv
- daStep_holding
- isFree
- propTarget
- not_isFree_iff
- daStep_nc_held
- daStep_nc_free
- pref_list_mem
