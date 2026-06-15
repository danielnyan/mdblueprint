---
id: nash-iff-degenerate-ce
title: nash_iff_degenerate_ce
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.CorrelatedEq
  declarations:
    - nash_iff_degenerate_ce
uses:
  - Profile
  - IsNashEquilibrium
  - IsDegenerateCorrelatedEq
---

# nash_iff_degenerate_ce

## Lean type

```lean
theorem nash_iff_degenerate_ce (G : StrategicGame N U) (σ : G.Profile) : IsNashEquilibrium G σ ↔ IsDegenerateCorrelatedEq G σ
```

## Dependencies

- Profile
- IsNashEquilibrium
- IsDegenerateCorrelatedEq
