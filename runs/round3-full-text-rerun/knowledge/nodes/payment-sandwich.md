---
id: payment-sandwich
title: payment_sandwich
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Myerson
  declarations:
    - payment_sandwich
uses:
  - IsDSIC
  - isDSIC
  - toStrategicGame
  - IsStrictlyDominant.isWeaklyDominant
  - IsWeaklyDominant
  - WeaklyDominates
---

# payment_sandwich

## Lean type

```lean
theorem payment_sandwich [DecidableEq I] {x p : (I → ℝ) → I → ℝ} (hdsic : ({ allocationRule
```

## Dependencies

- IsDSIC
- isDSIC
- toStrategicGame
- IsStrictlyDominant.isWeaklyDominant
- IsWeaklyDominant
- WeaklyDominates
