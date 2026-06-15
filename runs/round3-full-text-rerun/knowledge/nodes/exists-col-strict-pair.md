---
id: exists-col-strict-pair
title: exists_col_strict_pair
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearProgramming.StrongComplementarity
  declarations:
    - exists_col_strict_pair
uses:
  - DualFeasible
  - optAugB
  - optAugA
  - optAug_feasible_iff
  - lp_weak_duality
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - farkas_lemma
  - OptAugRow
---

# exists_col_strict_pair

## Lean type

```lean
theorem exists_col_strict_pair (A : I → Fin n → 𝕜) (b : I → 𝕜) (c : Fin n → 𝕜) (v : 𝕜) {x₀ : Fin n → 𝕜} (hx₀A : ∀ i, b i ≤ ∑ j, A i j * x₀ j) (hx₀nn : ∀ j, 0 ≤ x₀ j) (hx₀_val : ∑ j, c j * x₀ j = v) {u₀ : I → 𝕜} (hu₀ : DualFeasible A c u₀) (hu₀_val : ∑ i, u₀ i * b i = v) (j₀ : Fin n) : ∃ (x : Fin n → 𝕜) (u : I → 𝕜), (∀ i, b i ≤ ∑ j, A i j * x j) ∧ (∀ j, 0 ≤ x j) ∧ DualFeasible A c u ∧ (∑ j, c j * x j = v) ∧ (∑ i, u i * b i = v) ∧ 0 < x j₀ + (c j₀ - ∑ i, u i * A i j₀)
```

## Dependencies

- DualFeasible
- optAugB
- optAugA
- optAug_feasible_iff
- lp_weak_duality
- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- farkas_lemma
- OptAugRow
