---
id: hpkg-aux
title: hpkg_aux
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer
  declarations:
    - hpkg_aux
uses:
  - room_point_seq
---

# hpkg_aux

## Lean type

```lean
@[reducible] def hpkg_aux: Nonempty {(z , h) : (stdSimplex ℝ (Fin n)) × (ℕ → ℕ) | StrictMono h ∧ Filter.Tendsto ((fun l' => (room_point_seq f (g1 f l'): stdSimplex ℝ (Fin n))) ∘ h) Filter.atTop (𝓝 z) }
```

## Dependencies

- room_point_seq
