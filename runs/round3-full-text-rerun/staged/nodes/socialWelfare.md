---
id: socialWelfare
title: socialWelfare
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.VCG
  declarations:
    - socialWelfare
uses:
  - Valuation
---

# socialWelfare

## Lean type

```lean
def socialWelfare (v : ∀ _ : I, Valuation A ℝ) (a : A) : ℝ
```

## Dependencies

- Valuation
