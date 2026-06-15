---
id: dualAugA
title: dualAugA
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearProgramming.StrongDuality
  declarations:
    - dualAugA
uses:
  - DualAugRow
---

# dualAugA

## Lean type

```lean
def dualAugA (A : I → Fin n → 𝕜) : DualAugRow I n → Fin n → 𝕜 | Sum.inl i, j => A i j | Sum.inr j', j => if j = j' then 1 else 0 /-- Augmented RHS. -/
```

## Dependencies

- DualAugRow
