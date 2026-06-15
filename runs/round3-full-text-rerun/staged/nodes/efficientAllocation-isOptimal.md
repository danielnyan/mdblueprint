---
id: efficientAllocation-isOptimal
title: efficientAllocation_isOptimal
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.VCG
  declarations:
    - efficientAllocation_isOptimal
uses:
  - Valuation
  - socialWelfare
  - exists_efficientAllocation
---

# efficientAllocation_isOptimal

## Lean type

```lean
lemma efficientAllocation_isOptimal (v : ∀ _ : I, Valuation A ℝ) (a : A) : socialWelfare v a ≤ socialWelfare v (efficientAllocation v)
```

## Dependencies

- Valuation
- socialWelfare
- exists_efficientAllocation
