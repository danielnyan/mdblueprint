---
id: Brouwer
title: Brouwer
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer
  declarations:
    - Brouwer
uses:
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - tendsto_diam_to_zero
  - room_point_seq
  - room_seq
  - dominant_coords_tend_to_zero
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - f_coords_ge_z_coords
  - Profile.ext
---

# Brouwer

## Lean type

```lean
theorem Brouwer (hf : Continuous f): ∃ x , f x = x
```

## Dependencies

- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- tendsto_diam_to_zero
- room_point_seq
- room_seq
- dominant_coords_tend_to_zero
- IsPositiveAffineOf.symm
- Indifferent.symm
- f_coords_ge_z_coords
- Profile.ext
