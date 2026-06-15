---
id: IsEnvyFree-isEFX-of-mono
title: IsEnvyFree.isEFX_of_mono
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Fairness
  declarations:
    - IsEnvyFree.isEFX_of_mono
uses:
  - Valuation
  - Allocation
  - IsEnvyFree
  - IsEFX
---

# IsEnvyFree.isEFX_of_mono

## Lean type

```lean
theorem IsEnvyFree.isEFX_of_mono (v : Valuation N G) (A : Allocation N G) (hmono : ∀ i S T, T ⊆ S → v.val i T ≤ v.val i S) (hef : IsEnvyFree v A) : IsEFX v A
```

## Dependencies

- Valuation
- Allocation
- IsEnvyFree
- IsEFX
