---
id: f-coords-ge-z-coords
title: f_coords_ge_z_coords
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer
  declarations:
    - f_coords_ge_z_coords
uses:
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - room_point_seq
  - room_seq
  - Fcolor
  - TTtostdSimplex
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - pick_colorful_point
  - tendsto_diam_to_zero
  - Survives.mono
---

# f_coords_ge_z_coords

## Lean type

```lean
theorem f_coords_ge_z_coords (f : stdSimplex ℝ (Fin n) → stdSimplex ℝ (Fin n)) (hf : Continuous f) : ∀ i ∈ (gpkg f).1.1, (f (hpkg f).1.1).1 i ≥ ((hpkg f).1.1).1 i
```

## Dependencies

- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- room_point_seq
- room_seq
- Fcolor
- TTtostdSimplex
- IsPositiveAffineOf.symm
- Indifferent.symm
- pick_colorful_point
- tendsto_diam_to_zero
- Survives.mono
