---
id: dominant-coords-tend-to-zero
title: dominant_coords_tend_to_zero
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer
  declarations:
    - dominant_coords_tend_to_zero
uses:
  - room_seq
  - room_point_seq
  - pick_colorful_point
  - isDominant
  - TT
  - size_bound_out
  - TTtostdSimplex
---

# dominant_coords_tend_to_zero

## Lean type

```lean
lemma dominant_coords_tend_to_zero (f : stdSimplex ℝ (Fin n) → stdSimplex ℝ (Fin n)) (C : Finset (Fin n)) (g : ℕ ↪o ℕ) (h_const : ∀ l', (room_seq f (g l')).1.2 = C) : ∀ i ∉ C, Filter.Tendsto (fun l' => ((room_point_seq f (g l')) : stdSimplex ℝ (Fin n)).1 i) Filter.atTop (𝓝 0)
```

## Dependencies

- room_seq
- room_point_seq
- pick_colorful_point
- isDominant
- TT
- size_bound_out
- TTtostdSimplex
