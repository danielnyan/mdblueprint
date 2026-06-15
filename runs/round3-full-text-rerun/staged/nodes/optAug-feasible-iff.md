---
id: optAug-feasible-iff
title: optAug_feasible_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearProgramming.StrongComplementarity
  declarations:
    - optAug_feasible_iff
uses:
  - optAugB
  - optAugA
---

# optAug_feasible_iff

## Lean type

```lean
theorem optAug_feasible_iff (A : I → Fin n → 𝕜) (b : I → 𝕜) (c : Fin n → 𝕜) (v : 𝕜) (x : Fin n → 𝕜) : (∀ idx, optAugB b v idx ≤ ∑ j, optAugA A c idx j * x j) ↔ (∀ i, b i ≤ ∑ j, A i j * x j) ∧ (∀ j, 0 ≤ x j) ∧ (∑ j, c j * x j ≤ v)
```

## Dependencies

- optAugB
- optAugA
