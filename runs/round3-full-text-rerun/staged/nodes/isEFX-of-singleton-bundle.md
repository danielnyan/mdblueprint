---
id: isEFX-of-singleton-bundle
title: isEFX_of_singleton_bundle
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EFX
  declarations:
    - isEFX_of_singleton_bundle
uses:
  - Valuation
  - Allocation
---

# isEFX_of_singleton_bundle

## Lean type

```lean
lemma isEFX_of_singleton_bundle [DecidableEq G] (v : Valuation (Fin 2) G) (A : Allocation (Fin 2) G) (i j : Fin 2) {g : G} (hAi : A i = {g}) (h_empty_le : v.val j ∅ ≤ v.val j (A j)) : ∀ h ∈ A i, v.val j (A i \ {h}) ≤ v.val j (A j)
```

## Dependencies

- Valuation
- Allocation
