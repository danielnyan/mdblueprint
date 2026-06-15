---
id: rps-dev0
title: rps_dev0
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.RockPaperScissors
  declarations:
    - rps_dev0
uses:
  - expectedPayoff
  - deviateMixed
  - uniformProfile
---

# rps_dev0

## Lean type

```lean
theorem rps_dev0 (s₀ : RPSMove) : expectedPayoff RPS (deviateMixed RPS uniformProfile 0 s₀) 0 = 0
```

## Dependencies

- expectedPayoff
- deviateMixed
- uniformProfile
