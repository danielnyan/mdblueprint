---
id: deviate
title: deviate
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.MechBayesian
  declarations:
    - deviate
uses:
  - Profile
  - BehaviorProfile
  - BehaviorStrategy
  - Profile
  - Strategy
  - StrategyProfile
---

# deviate

## Lean type

```lean
def deviate [DecidableEq I] (σ : StrategyProfile T M) (i : I) (τ : T i → M i) : StrategyProfile T M
```

## Dependencies

- Profile
- BehaviorProfile
- BehaviorStrategy
- Profile
- Strategy
- StrategyProfile
