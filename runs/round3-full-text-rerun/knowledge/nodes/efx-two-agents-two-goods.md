---
id: efx-two-agents-two-goods
title: efx_two_agents_two_goods
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EFX
  declarations:
    - efx_two_agents_two_goods
uses:
  - Valuation
  - Allocation
  - IsEFX
  - isEFX_of_singleton_bundle
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - Profile.ext
  - toValuation
---

# efx_two_agents_two_goods

## Lean type

```lean
theorem efx_two_agents_two_goods [DecidableEq G] (v : Valuation (Fin 2) G) {g₀ g₁ : G} (h₀ : v.val 0 ∅ ≤ v.val 0 {g₀}) (h₁ : v.val 1 ∅ ≤ v.val 1 {g₁}) (A : Allocation (Fin 2) G) (hA0 : A 0 = {g₀}) (hA1 : A 1 = {g₁}) : IsEFX v A
```

## Dependencies

- Valuation
- Allocation
- IsEFX
- isEFX_of_singleton_bundle
- IsPositiveAffineOf.symm
- Indifferent.symm
- Profile.ext
- toValuation
