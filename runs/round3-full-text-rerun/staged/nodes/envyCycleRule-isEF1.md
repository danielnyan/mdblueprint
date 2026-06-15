---
id: envyCycleRule-isEF1
title: envyCycleRule_isEF1
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - envyCycleRule_isEF1
uses:
  - IsEFX.isEF1
  - IsEF1
  - envyCycleAllocation_isEF1
---

# envyCycleRule_isEF1

## Lean type

```lean
theorem envyCycleRule_isEF1 [Fintype N] [Fintype G] [Nonempty N] [DecidableEq N] [DecidableEq G] (I : AdditiveInstance N G) (hnn : ∀ (i : N) (g : G), 0 ≤ I.weight i g) : I.IsEF1 (envyCycleRule I).1
```

## Dependencies

- IsEFX.isEF1
- IsEF1
- envyCycleAllocation_isEF1
