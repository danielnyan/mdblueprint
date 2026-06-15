---
id: Finset-eq-of-mem-of-card-one
title: Finset.eq_of_mem_of_card_one
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - Finset.eq_of_mem_of_card_one
uses:
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# Finset.eq_of_mem_of_card_one

## Lean type

```lean
lemma Finset.eq_of_mem_of_card_one {X : Type*} [DecidableEq X] {s : Finset X} {a : X} (h_mem : a ∈ s) (h_card : s.card = 1) : s = {a}
```

## Dependencies

- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- IsPositiveAffineOf.symm
- Indifferent.symm
