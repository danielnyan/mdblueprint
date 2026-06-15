---
id: welfareWithout-update-self
title: welfareWithout_update_self
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.VCG
  declarations:
    - welfareWithout_update_self
uses:
  - Valuation
  - welfareWithout
---

# welfareWithout_update_self

## Lean type

```lean
lemma welfareWithout_update_self (v : ∀ _ : I, Valuation A ℝ) (i : I) (report : Valuation A ℝ) (a : A) : welfareWithout (Function.update v i report) i a = welfareWithout v i a
```

## Dependencies

- Valuation
- welfareWithout
