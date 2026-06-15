---
id: welfareWithout
title: welfareWithout
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.VCG
  declarations:
    - welfareWithout
uses:
  - Valuation
---

# welfareWithout

## Lean type

```lean
def welfareWithout (v : ∀ _ : I, Valuation A ℝ) (i : I) (a : A) : ℝ
```

## Dependencies

- Valuation
