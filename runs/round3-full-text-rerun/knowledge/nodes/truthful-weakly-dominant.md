---
id: truthful-weakly-dominant
title: truthful_weakly_dominant
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Vickrey
  declarations:
    - truthful_weakly_dominant
uses:
  - IsStrictlyDominant.isWeaklyDominant
  - IsWeaklyDominant
  - valuation_is_dominant
  - Allocation
  - IsStrictlyDominant.isWeaklyDominant
  - IsWeaklyDominant
  - valuation_is_dominant
---

# truthful_weakly_dominant

## Lean type

```lean
theorem truthful_weakly_dominant (v : I → U) (i : I) : IsWeaklyDominant (game v) i (v i)
```

## Dependencies

- IsStrictlyDominant.isWeaklyDominant
- IsWeaklyDominant
- valuation_is_dominant
- Allocation
- IsStrictlyDominant.isWeaklyDominant
- IsWeaklyDominant
- valuation_is_dominant
