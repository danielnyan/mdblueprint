---
id: farkas-lemma
title: farkas_lemma
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.Farkas
  declarations:
    - farkas_lemma
uses:
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - farkasAugA
  - farkasAugB
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - rowEval
  - HasCertificate
  - theorem_of_alternative
---

# farkas_lemma

## Lean type

```lean
theorem farkas_lemma (A : I → Fin n → 𝕜) (b : I → 𝕜) (c : Fin n → 𝕜) (d : 𝕜) (hS : IsFeasible A b) : (∀ x : Fin n → 𝕜, (∀ i, b i ≤ ∑ j, A i j * x j) → d ≤ ∑ j, c j * x j) ↔ (∃ u : I → 𝕜, (∀ i, 0 ≤ u i) ∧ (∀ j, ∑ i, u i * A i j = c j) ∧ d ≤ ∑ i, u i * b i)
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- farkasAugA
- farkasAugB
- IsPositiveAffineOf.symm
- Indifferent.symm
- rowEval
- HasCertificate
- theorem_of_alternative
