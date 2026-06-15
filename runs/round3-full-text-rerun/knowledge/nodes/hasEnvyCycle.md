---
id: hasEnvyCycle
title: hasEnvyCycle
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - hasEnvyCycle
uses:
  - Valuation
  - Allocation
  - isEnvyCycle
---

# hasEnvyCycle

## Lean type

```lean
def hasEnvyCycle (v : Valuation N G) (A : Allocation N G) : Prop
```

## Dependencies

- Valuation
- Allocation
- isEnvyCycle
