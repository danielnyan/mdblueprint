---
id: maxWelfareWithout-update-self
title: maxWelfareWithout_update_self
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.VCG
  declarations:
    - maxWelfareWithout_update_self
uses:
  - Valuation
  - welfareWithout_update_self
---

# maxWelfareWithout_update_self

## Lean type

```lean
lemma maxWelfareWithout_update_self (v : ∀ _ : I, Valuation A ℝ) (i : I) (report : Valuation A ℝ) : maxWelfareWithout (Function.update v i report) i = maxWelfareWithout v i
```

## Dependencies

- Valuation
- welfareWithout_update_self
