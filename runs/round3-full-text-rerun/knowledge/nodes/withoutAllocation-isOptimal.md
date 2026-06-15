---
id: withoutAllocation-isOptimal
title: withoutAllocation_isOptimal
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.VCG
  declarations:
    - withoutAllocation_isOptimal
uses:
  - Valuation
  - welfareWithout
  - exists_withoutAllocation
---

# withoutAllocation_isOptimal

## Lean type

```lean
lemma withoutAllocation_isOptimal (v : ∀ _ : I, Valuation A ℝ) (i : I) (a : A) : welfareWithout v i a ≤ welfareWithout v i (withoutAllocation v i)
```

## Dependencies

- Valuation
- welfareWithout
- exists_withoutAllocation
