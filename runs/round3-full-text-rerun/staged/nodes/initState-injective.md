---
id: initState-injective
title: initState_injective
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - initState_injective
uses:
  - initState
  - isFree
  - propTarget
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - Survives.mono
  - holding_rank_mono_step
  - daStep_nc_free
  - daStep_nc_held
  - not_isFree_iff
  - pref_list_mem
  - holding_injective_step
  - freeMenSet
  - mem_freeMenSet
  - holding_rank_mono_run
  - finalState
---

# initState_injective

## Lean type

```lean
lemma initState_injective : ∀ j1 j2 : Fin n, ∀ i : Fin n, (initState n).holding j1 = some i → (initState n).holding j2 = some i → j1 = j2
```

## Dependencies

- initState
- isFree
- propTarget
- IsPositiveAffineOf.symm
- Indifferent.symm
- Survives.mono
- holding_rank_mono_step
- daStep_nc_free
- daStep_nc_held
- not_isFree_iff
- pref_list_mem
- holding_injective_step
- freeMenSet
- mem_freeMenSet
- holding_rank_mono_run
- finalState
