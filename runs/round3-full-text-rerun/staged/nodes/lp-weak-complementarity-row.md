---
id: lp-weak-complementarity-row
title: lp_weak_complementarity_row
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearProgramming.StrongComplementarity
  declarations:
    - lp_weak_complementarity_row
uses:
  - DualFeasible
---

# lp_weak_complementarity_row

## Lean type

```lean
theorem lp_weak_complementarity_row (A : I → Fin n → 𝕜) (b : I → 𝕜) (c : Fin n → 𝕜) {x : Fin n → 𝕜} (hxA : ∀ i, b i ≤ ∑ j, A i j * x j) (hxnn : ∀ j, 0 ≤ x j) {u : I → 𝕜} (hu_du : DualFeasible A c u) (h_match : ∑ j, c j * x j = ∑ i, u i * b i) : ∀ i, (∑ j, A i j * x j - b i) * u i = 0
```

## Dependencies

- DualFeasible
