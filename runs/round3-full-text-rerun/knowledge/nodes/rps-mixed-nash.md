---
id: rps-mixed-nash
title: rps_mixed_nash
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.RockPaperScissors
  declarations:
    - rps_mixed_nash
uses:
  - IsMixedNashEq
  - uniformProfile
---

# rps_mixed_nash

## Lean type

```lean
theorem rps_mixed_nash : IsMixedNashEq RPS uniformProfile
```

## Dependencies

- IsMixedNashEq
- uniformProfile
