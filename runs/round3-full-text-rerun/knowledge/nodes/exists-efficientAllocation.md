---
id: exists-efficientAllocation
title: exists_efficientAllocation
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.VCG
  declarations:
    - exists_efficientAllocation
uses:
  - Valuation
  - socialWelfare
---

# exists_efficientAllocation

## Lean type

```lean
lemma exists_efficientAllocation (v : ∀ _ : I, Valuation A ℝ) : ∃ a : A, ∀ b : A, socialWelfare v b ≤ socialWelfare v a
```

## Dependencies

- Valuation
- socialWelfare
