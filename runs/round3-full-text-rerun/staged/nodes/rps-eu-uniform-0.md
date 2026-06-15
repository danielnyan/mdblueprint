---
id: rps-eu-uniform-0
title: rps_eu_uniform_0
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.RockPaperScissors
  declarations:
    - rps_eu_uniform_0
uses:
  - expectedPayoff
  - uniformProfile
---

# rps_eu_uniform_0

## Lean type

```lean
theorem rps_eu_uniform_0 : expectedPayoff RPS uniformProfile 0 = 0
```

## Dependencies

- expectedPayoff
- uniformProfile
