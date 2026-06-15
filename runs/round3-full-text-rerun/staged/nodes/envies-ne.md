---
id: envies-ne
title: envies_ne
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - envies_ne
uses:
  - Valuation
  - Allocation
---

# envies_ne

## Lean type

```lean
lemma envies_ne (v : Valuation N G) (A : Allocation N G) {i j : N} (h : envies v A i j) : i ≠ j
```

## Dependencies

- Valuation
- Allocation
