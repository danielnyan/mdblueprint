---
id: isEnvyCycle
title: isEnvyCycle
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - isEnvyCycle
uses:
  - Valuation
  - Allocation
---

# isEnvyCycle

## Lean type

```lean
def isEnvyCycle (v : Valuation N G) (A : Allocation N G) (l : List N) : Prop
```

## Dependencies

- Valuation
- Allocation
