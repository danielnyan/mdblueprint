---
id: exists-withoutAllocation
title: exists_withoutAllocation
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.VCG
  declarations:
    - exists_withoutAllocation
uses:
  - Valuation
  - welfareWithout
---

# exists_withoutAllocation

## Lean type

```lean
lemma exists_withoutAllocation (v : ∀ _ : I, Valuation A ℝ) (i : I) : ∃ a : A, ∀ b : A, welfareWithout v i b ≤ welfareWithout v i a
```

## Dependencies

- Valuation
- welfareWithout
