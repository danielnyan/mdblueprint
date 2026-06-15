---
id: paretoDomSet-subset
title: paretoDomSet_subset
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - paretoDomSet_subset
uses:
  - Valuation
  - Allocation
---

# paretoDomSet_subset

## Lean type

```lean
lemma paretoDomSet_subset [Fintype N] [Fintype G] (v : Valuation N G) (A A' : Allocation N G) (h : ∀ i : N, v.val i (A i) ≤ v.val i (A' i)) : Finset.univ.filter (fun B : N → Finset G => ∀ i : N, v.val i (A' i) ≤ v.val i (B i)) ⊆ Finset.univ.filter (fun B : N → Finset G => ∀ i : N, v.val i (A i) ≤ v.val i (B i))
```

## Dependencies

- Valuation
- Allocation
