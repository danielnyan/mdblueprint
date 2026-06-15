---
id: lp-weak-complementarity-col
title: lp_weak_complementarity_col
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearProgramming.StrongComplementarity
  declarations:
    - lp_weak_complementarity_col
uses:
  - DualFeasible
---

# lp_weak_complementarity_col

## Lean type

```lean
theorem lp_weak_complementarity_col (A : I → Fin n → 𝕜) (b : I → 𝕜) (c : Fin n → 𝕜) {x : Fin n → 𝕜} (hxA : ∀ i, b i ≤ ∑ j, A i j * x j) (hxnn : ∀ j, 0 ≤ x j) {u : I → 𝕜} (hu_du : DualFeasible A c u) (h_match : ∑ j, c j * x j = ∑ i, u i * b i) : ∀ j, (c j - ∑ i, u i * A i j) * x j = 0
```

## Dependencies

- DualFeasible
