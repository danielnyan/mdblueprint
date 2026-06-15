---
id: envies
title: envies
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - envies
uses:
  - Valuation
  - Allocation
---

# envies

## Lean type

```lean
def envies (v : Valuation N G) (A : Allocation N G) (i j : N) : Prop
```

## Dependencies

- Valuation
- Allocation
