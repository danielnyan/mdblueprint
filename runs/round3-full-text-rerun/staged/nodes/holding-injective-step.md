---
id: holding-injective-step
title: holding_injective_step
kind: theorem
status: staged
lean:
  module: EconCSLib.MarketDesign.Matching.GaleShapley
  declarations:
    - holding_injective_step
uses:
  - isFree
  - propTarget
  - IsPositiveAffineOf.trans
  - IsPositiveAffineOf.symm
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Indifferent.symm
  - Subtree.trans
  - isFree_iff
---

# holding_injective_step

## Lean type

```lean
lemma holding_injective_step (s : DAState n) (hinj : ∀ j1 j2 : Fin n, ∀ i : Fin n, s.holding j1 = some i → s.holding j2 = some i → j1 = j2) : ∀ j1 j2 : Fin n, ∀ i : Fin n, (daStep w m s).holding j1 = some i → (daStep w m s).holding j2 = some i → j1 = j2
```

## Dependencies

- isFree
- propTarget
- IsPositiveAffineOf.trans
- IsPositiveAffineOf.symm
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Indifferent.symm
- Subtree.trans
- isFree_iff
