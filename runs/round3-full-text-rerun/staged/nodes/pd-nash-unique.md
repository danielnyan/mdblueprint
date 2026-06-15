---
id: pd-nash-unique
title: pd_nash_unique
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.PrisonersDilemma
  declarations:
    - pd_nash_unique
uses:
  - Profile
  - PD
  - IsNashEquilibrium
---

# pd_nash_unique

## Lean type

```lean
theorem pd_nash_unique : ∀ σ : PD.Profile, IsNashEquilibrium PD σ → σ = fun _ => Defect
```

## Dependencies

- Profile
- PD
- IsNashEquilibrium
