---
id: lp-weak-duality
title: lp_weak_duality
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearProgramming.StrongDuality
  declarations:
    - lp_weak_duality
uses:
  - DualFeasible
---

# lp_weak_duality

## Lean type

```lean
theorem lp_weak_duality (A : I → Fin n → 𝕜) (b : I → 𝕜) (c : Fin n → 𝕜) {x : Fin n → 𝕜} (hxA : ∀ i, b i ≤ ∑ j, A i j * x j) (hxnn : ∀ j, 0 ≤ x j) {u : I → 𝕜} (hu_du : DualFeasible A c u) : ∑ i, u i * b i ≤ ∑ j, c j * x j
```

## Dependencies

- DualFeasible
