---
id: ef-impossible-two-agents-one-good
title: ef_impossible_two_agents_one_good
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.ImpossibilityEF
  declarations:
    - ef_impossible_two_agents_one_good
uses:
  - Valuation
  - Allocation
  - IsEnvyFree
  - mem_biUnion
---

# ef_impossible_two_agents_one_good

## Lean type

```lean
theorem ef_impossible_two_agents_one_good {G : Type*} [DecidableEq G] {g : G} (v : Valuation (Fin 2) G) (h0 : v.val 0 ∅ < v.val 0 {g}) (h1 : v.val 1 ∅ < v.val 1 {g}) {A : Allocation (Fin 2) G} (hA : IsAllocation {g} A) : ¬ IsEnvyFree v A
```

## Dependencies

- Valuation
- Allocation
- IsEnvyFree
- mem_biUnion
