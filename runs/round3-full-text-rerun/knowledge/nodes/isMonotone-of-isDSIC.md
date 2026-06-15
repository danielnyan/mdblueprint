---
id: isMonotone-of-isDSIC
title: isMonotone_of_isDSIC
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Myerson
  declarations:
    - isMonotone_of_isDSIC
uses:
  - IsDSIC
  - isDSIC
  - IsMonotone
  - toStrategicGame
  - IsStrictlyDominant.isWeaklyDominant
  - IsWeaklyDominant
  - WeaklyDominates
---

# isMonotone_of_isDSIC

## Lean type

```lean
theorem isMonotone_of_isDSIC [DecidableEq I] {M : SingleParameterMechanism I ℝ} (hdsic : M.IsDSIC) : M.IsMonotone
```

## Dependencies

- IsDSIC
- isDSIC
- IsMonotone
- toStrategicGame
- IsStrictlyDominant.isWeaklyDominant
- IsWeaklyDominant
- WeaklyDominates
