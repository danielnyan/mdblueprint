---
id: IsAntisymmetric-diag-zero
title: IsAntisymmetric.diag_zero
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.Antisymmetric
  declarations:
    - IsAntisymmetric.diag_zero
uses:
  - IsAntisymmetric
---

# IsAntisymmetric.diag_zero

## Lean type

```lean
theorem IsAntisymmetric.diag_zero {B : I → I → ℝ} (hB : IsAntisymmetric B) (i : I) : B i i = 0
```

## Dependencies

- IsAntisymmetric
