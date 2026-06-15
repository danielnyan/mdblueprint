---
id: envyCycleAllocation-isEF1
title: envyCycleAllocation_isEF1
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - envyCycleAllocation_isEF1
uses:
  - IsEFX.isEF1
  - IsEF1
  - toValuation
  - toAdditiveValuation
---

# envyCycleAllocation_isEF1

## Lean type

```lean
theorem envyCycleAllocation_isEF1 [Fintype N] [Fintype G] [Nonempty N] [DecidableEq N] [DecidableEq G] (I : AdditiveInstance N G) (hnn : ∀ (i : N) (g : G), 0 ≤ I.weight i g) : I.IsEF1 (envyCycleAllocation I)
```

## Dependencies

- IsEFX.isEF1
- IsEF1
- toValuation
- toAdditiveValuation
