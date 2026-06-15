---
id: efx-exists-two-agents
title: efx_exists_two_agents
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EFX
  declarations:
    - efx_exists_two_agents
uses:
  - Allocation
  - IsEFX
  - toValuation
---

# efx_exists_two_agents

## Lean type

```lean
theorem efx_exists_two_agents [Fintype G] [DecidableEq G] (w : AdditiveValuation (Fin 2) G) (hnn₀ : ∀ g, 0 ≤ w.weight 0 g) (hnn₁ : ∀ g, 0 ≤ w.weight 1 g) (allGoods : Finset G) : ∃ A : Allocation (Fin 2) G, IsAllocation allGoods A ∧ IsEFX w.toValuation A
```

## Dependencies

- Allocation
- IsEFX
- toValuation
