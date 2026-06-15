---
id: rps-uniform-completely-mixed
title: rps_uniform_completely_mixed
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.RockPaperScissors
  declarations:
    - rps_uniform_completely_mixed
uses:
  - IsCompletelyMixedProfile
  - uniformProfile
---

# rps_uniform_completely_mixed

## Lean type

```lean
theorem rps_uniform_completely_mixed : IsCompletelyMixedProfile RPS uniformProfile
```

## Dependencies

- IsCompletelyMixedProfile
- uniformProfile
