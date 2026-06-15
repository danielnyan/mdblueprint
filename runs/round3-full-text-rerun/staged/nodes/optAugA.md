---
id: optAugA
title: optAugA
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearProgramming.StrongComplementarity
  declarations:
    - optAugA
uses:
  - OptAugRow
---

# optAugA

## Lean type

```lean
def optAugA (A : I → Fin n → 𝕜) (c : Fin n → 𝕜) : OptAugRow I n → Fin n → 𝕜 | Sum.inl (Sum.inl i), j => A i j | Sum.inl (Sum.inr j'), j => if j = j' then 1 else 0 | Sum.inr (), j => -c j /-- Optimality-augmented RHS. -/
```

## Dependencies

- OptAugRow
