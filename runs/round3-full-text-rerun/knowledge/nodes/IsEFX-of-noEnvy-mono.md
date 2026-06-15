---
id: IsEFX-of-noEnvy-mono
title: IsEFX.of_noEnvy_mono
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EFX
  declarations:
    - IsEFX.of_noEnvy_mono
uses:
  - Valuation
  - Allocation
  - IsEnvyFree
  - IsEFX
  - IsEnvyFree.isEFX_of_mono
---

# IsEFX.of_noEnvy_mono

## Lean type

```lean
theorem IsEFX.of_noEnvy_mono [DecidableEq G] (v : Valuation (Fin 2) G) (hmono : ∀ i S T, T ⊆ S → v.val i T ≤ v.val i S) (A : Allocation (Fin 2) G) (h : IsEnvyFree v A) : IsEFX v A
```

## Dependencies

- Valuation
- Allocation
- IsEnvyFree
- IsEFX
- IsEnvyFree.isEFX_of_mono
