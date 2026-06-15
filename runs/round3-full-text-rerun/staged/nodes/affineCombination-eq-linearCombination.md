---
id: affineCombination-eq-linearCombination
title: affineCombination_eq_linearCombination
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - affineCombination_eq_linearCombination
uses:
---

# affineCombination_eq_linearCombination

## Lean type

```lean
@[simp] theorem affineCombination_eq_linearCombination {k V I : Type*} [Ring k] [PartialOrder k] [Fintype I] [AddCommGroup V] [Module k V] (x : stdSimplex k I) (p : I → V) : affineCombination x p = Fintype.linearCombination k p x
```

## Dependencies

- none
