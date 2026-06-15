---
id: self-mem-paretoDomSet
title: self_mem_paretoDomSet
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - self_mem_paretoDomSet
uses:
  - Valuation
  - Allocation
---

# self_mem_paretoDomSet

## Lean type

```lean
lemma self_mem_paretoDomSet [Fintype N] [Fintype G] (v : Valuation N G) (A : Allocation N G) : A ∈ Finset.univ.filter (fun B : N → Finset G => ∀ i : N, v.val i (A i) ≤ v.val i (B i))
```

## Dependencies

- Valuation
- Allocation
