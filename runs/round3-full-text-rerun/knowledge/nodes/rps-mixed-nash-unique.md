---
id: rps-mixed-nash-unique
title: rps_mixed_nash_unique
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.RockPaperScissors
  declarations:
    - rps_mixed_nash_unique
uses:
  - MixedProfile
  - IsMixedNashEq
  - uniformProfile
  - expectedPayoff
  - Profile.ext
---

# rps_mixed_nash_unique

## Lean type

```lean
theorem rps_mixed_nash_unique (p : MixedProfile RPS) (hN : IsMixedNashEq RPS p) : p = uniformProfile
```

## Dependencies

- MixedProfile
- IsMixedNashEq
- uniformProfile
- expectedPayoff
- Profile.ext
