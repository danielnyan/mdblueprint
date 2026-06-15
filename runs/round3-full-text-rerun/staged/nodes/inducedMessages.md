---
id: inducedMessages
title: inducedMessages
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.MechBayesian
  declarations:
    - inducedMessages
uses:
  - StrategyProfile
---

# inducedMessages

## Lean type

```lean
def inducedMessages (σ : StrategyProfile T M) (t : ∀ i, T i) : ∀ i, M i
```

## Dependencies

- StrategyProfile
