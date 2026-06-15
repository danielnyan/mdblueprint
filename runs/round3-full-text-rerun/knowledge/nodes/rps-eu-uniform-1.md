---
id: rps-eu-uniform-1
title: rps_eu_uniform_1
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.RockPaperScissors
  declarations:
    - rps_eu_uniform_1
uses:
  - expectedPayoff
  - uniformProfile
---

# rps_eu_uniform_1

## Lean type

```lean
theorem rps_eu_uniform_1 : expectedPayoff RPS uniformProfile 1 = 0
```

## Dependencies

- expectedPayoff
- uniformProfile
