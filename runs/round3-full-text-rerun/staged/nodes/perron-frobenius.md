---
id: perron-frobenius
title: perron_frobenius
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.PerronFrobenius
  declarations:
    - perron_frobenius
uses:
  - IsPositive
  - loomis_theorem
  - By_pos
  - xB_pos
---

# perron_frobenius

## Lean type

```lean
theorem perron_frobenius (M : Fin n → Fin n → ℝ) (hM_pos : ∀ i j, 0 < M i j) : ∃ (x y : stdSimplex ℝ (Fin n)) (lam : ℝ), 0 < lam ∧ (∀ i, 0 < x.val i) ∧ (∀ i, 0 < y.val i) ∧ (∀ j, wsum x (fun i => M i j) = lam * x.val j) ∧ (∀ i, wsum y (M i) = lam * y.val i)
```

## Dependencies

- IsPositive
- loomis_theorem
- By_pos
- xB_pos
