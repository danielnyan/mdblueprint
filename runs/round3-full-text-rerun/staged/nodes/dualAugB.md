---
id: dualAugB
title: dualAugB
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearProgramming.StrongDuality
  declarations:
    - dualAugB
uses:
  - DualAugRow
  - dualAugA
---

# dualAugB

## Lean type

```lean
def dualAugB (b : I → 𝕜) : DualAugRow I n → 𝕜 | Sum.inl i => b i | Sum.inr _ => 0 @[simp] theorem dualAugA_inl (A : I → Fin n → 𝕜) (i : I) (j : Fin n) : dualAugA A (Sum.inl i) j = A i j
```

## Dependencies

- DualAugRow
- dualAugA
