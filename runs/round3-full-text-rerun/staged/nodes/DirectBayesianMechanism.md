---
id: DirectBayesianMechanism
title: DirectBayesianMechanism
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.MechBayesian
  declarations:
    - DirectBayesianMechanism
uses:
---

# DirectBayesianMechanism

## Lean type

```lean
abbrev DirectBayesianMechanism (I : Type*) (T : I → Type*) [∀ i, MeasurableSpace (T i)] (O : Type*)
```

## Dependencies

- none
