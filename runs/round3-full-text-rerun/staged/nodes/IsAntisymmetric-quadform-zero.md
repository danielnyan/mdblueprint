---
id: IsAntisymmetric-quadform-zero
title: IsAntisymmetric.quadform_zero
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.Antisymmetric
  declarations:
    - IsAntisymmetric.quadform_zero
uses:
  - IsAntisymmetric
---

# IsAntisymmetric.quadform_zero

## Lean type

```lean
theorem IsAntisymmetric.quadform_zero {B : I → I → ℝ} (hB : IsAntisymmetric B) (z : I → ℝ) : ∑ i, ∑ j, z i * B i j * z j = 0
```

## Dependencies

- IsAntisymmetric
