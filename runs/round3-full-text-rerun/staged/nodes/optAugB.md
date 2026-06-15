---
id: optAugB
title: optAugB
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearProgramming.StrongComplementarity
  declarations:
    - optAugB
uses:
  - OptAugRow
  - optAugA
---

# optAugB

## Lean type

```lean
def optAugB (b : I → 𝕜) (v : 𝕜) : OptAugRow I n → 𝕜 | Sum.inl (Sum.inl i) => b i | Sum.inl (Sum.inr _) => 0 | Sum.inr () => -v @[simp] theorem optAugA_inl_inl (A : I → Fin n → 𝕜) (c : Fin n → 𝕜) (i : I) (j : Fin n) : optAugA A c (Sum.inl (Sum.inl i)) j = A i j
```

## Dependencies

- OptAugRow
- optAugA
