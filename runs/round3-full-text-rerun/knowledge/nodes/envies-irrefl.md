---
id: envies-irrefl
title: envies_irrefl
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - envies_irrefl
uses:
  - Valuation
  - Allocation
---

# envies_irrefl

## Lean type

```lean
lemma envies_irrefl (v : Valuation N G) (A : Allocation N G) (i : N) : ¬ envies v A i i
```

## Dependencies

- Valuation
- Allocation
