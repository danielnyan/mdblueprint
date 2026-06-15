---
id: strict-nash-implies-ess
title: strict_nash_implies_ess
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ESS
  declarations:
    - strict_nash_implies_ess
uses:
  - IsESS
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# strict_nash_implies_ess

## Lean type

```lean
theorem strict_nash_implies_ess {s : S} (hstrict : ∀ t, t ≠ s → u s s > u t s) : IsESS u s
```

## Dependencies

- IsESS
- IsPositiveAffineOf.symm
- Indifferent.symm
