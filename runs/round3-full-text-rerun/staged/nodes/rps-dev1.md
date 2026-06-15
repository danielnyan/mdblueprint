---
id: rps-dev1
title: rps_dev1
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.RockPaperScissors
  declarations:
    - rps_dev1
uses:
  - expectedPayoff
  - deviateMixed
  - uniformProfile
---

# rps_dev1

## Lean type

```lean
theorem rps_dev1 (s₁ : RPSMove) : expectedPayoff RPS (deviateMixed RPS uniformProfile 1 s₁) 1 = 0
```

## Dependencies

- expectedPayoff
- deviateMixed
- uniformProfile
