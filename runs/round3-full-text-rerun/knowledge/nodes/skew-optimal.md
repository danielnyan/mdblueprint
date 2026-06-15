---
id: skew-optimal
title: skew_optimal
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Minimax
  declarations:
    - skew_optimal
uses:
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# skew_optimal

## Lean type

```lean
theorem skew_optimal {K : Type*} [Fintype K] [DecidableEq K] [Nonempty K] (S : K → K → 𝕜) (hS : ∀ k l, S k l = - S l k) : ∃ z : K → 𝕜, (∀ k, 0 ≤ z k) ∧ (∑ k, z k = 1) ∧ (∀ l, 0 ≤ ∑ k, z k * S k l)
```

## Dependencies

- IsPositiveAffineOf.symm
- Indifferent.symm
