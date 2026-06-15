---
id: not-mem-paretoDomSet-of-strict
title: not_mem_paretoDomSet_of_strict
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - not_mem_paretoDomSet_of_strict
uses:
  - Valuation
  - Allocation
---

# not_mem_paretoDomSet_of_strict

## Lean type

```lean
lemma not_mem_paretoDomSet_of_strict [Fintype N] [Fintype G] (v : Valuation N G) (A A' : Allocation N G) (_hweak : ∀ i : N, v.val i (A i) ≤ v.val i (A' i)) (hstrict : ∃ j : N, v.val j (A j) < v.val j (A' j)) : A ∉ Finset.univ.filter (fun B : N → Finset G => ∀ i : N, v.val i (A' i) ≤ v.val i (B i))
```

## Dependencies

- Valuation
- Allocation
