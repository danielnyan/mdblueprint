---
id: strom-piece-empty-iff
title: strom_piece_empty_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.Existence
  declarations:
    - strom_piece_empty_iff
uses:
  - Profile.ext
---

# strom_piece_empty_iff

## Lean type

```lean
lemma strom_piece_empty_iff (x : Fin n → ℝ) (hx : x ∈ stdSimplex ℝ (Fin n)) (i : Fin n) : strom_piece n x i = ∅ ↔ x i = 0
```

## Dependencies

- Profile.ext
