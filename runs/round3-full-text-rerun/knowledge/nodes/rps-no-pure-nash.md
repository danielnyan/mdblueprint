---
id: rps-no-pure-nash
title: rps_no_pure_nash
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.RockPaperScissors
  declarations:
    - rps_no_pure_nash
uses:
  - Profile
  - IsNashEquilibrium
---

# rps_no_pure_nash

## Lean type

```lean
theorem rps_no_pure_nash : ¬ ∃ σ : RPS.Profile, IsNashEquilibrium RPS σ
```

## Dependencies

- Profile
- IsNashEquilibrium
