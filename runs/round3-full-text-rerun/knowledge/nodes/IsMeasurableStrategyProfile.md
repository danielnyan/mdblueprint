---
id: IsMeasurableStrategyProfile
title: IsMeasurableStrategyProfile
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.MechBayesian
  declarations:
    - IsMeasurableStrategyProfile
uses:
  - StrategyProfile
---

# IsMeasurableStrategyProfile

## Lean type

```lean
def IsMeasurableStrategyProfile [∀ i, MeasurableSpace (M i)] (σ : StrategyProfile T M) : Prop
```

## Dependencies

- StrategyProfile
