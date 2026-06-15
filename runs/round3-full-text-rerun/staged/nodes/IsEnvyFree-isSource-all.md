---
id: IsEnvyFree-isSource-all
title: IsEnvyFree.isSource_all
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - IsEnvyFree.isSource_all
uses:
  - Valuation
  - Allocation
  - IsEnvyFree
  - isSource
---

# IsEnvyFree.isSource_all

## Lean type

```lean
lemma IsEnvyFree.isSource_all (v : Valuation N G) (A : Allocation N G) (hef : IsEnvyFree v A) (i : N) : isSource v A i
```

## Dependencies

- Valuation
- Allocation
- IsEnvyFree
- isSource
