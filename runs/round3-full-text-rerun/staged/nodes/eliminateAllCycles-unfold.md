---
id: eliminateAllCycles-unfold
title: eliminateAllCycles_unfold
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - eliminateAllCycles_unfold
uses:
  - Valuation
  - Allocation
  - hasEnvyCycle
---

# eliminateAllCycles_unfold

## Lean type

```lean
lemma eliminateAllCycles_unfold [Fintype N] [Fintype G] [DecidableEq N] (v : Valuation N G) (A : Allocation N G) : eliminateAllCycles v A = if h : hasEnvyCycle v A then eliminateAllCycles v (rotateBundles A (Classical.choose h)) else A
```

## Dependencies

- Valuation
- Allocation
- hasEnvyCycle
