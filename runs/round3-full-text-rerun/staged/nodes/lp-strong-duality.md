---
id: lp-strong-duality
title: lp_strong_duality
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearProgramming.StrongDuality
  declarations:
    - lp_strong_duality
uses:
  - PrimalFeasible
  - DualFeasible
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - dualAugA
  - dualAugB
  - isFeasible_dualAug_iff
  - farkas_lemma
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# lp_strong_duality

## Lean type

```lean
theorem lp_strong_duality (A : I → Fin n → 𝕜) (b : I → 𝕜) (c : Fin n → 𝕜) (d : 𝕜) (hP_feas : PrimalFeasible A b) (hP_bound : ∀ x : Fin n → 𝕜, (∀ i, b i ≤ ∑ j, A i j * x j) → (∀ j, 0 ≤ x j) → d ≤ ∑ j, c j * x j) : ∃ u : I → 𝕜, DualFeasible A c u ∧ d ≤ ∑ i, u i * b i
```

## Dependencies

- PrimalFeasible
- DualFeasible
- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- dualAugA
- dualAugB
- isFeasible_dualAug_iff
- farkas_lemma
- IsPositiveAffineOf.symm
- Indifferent.symm
