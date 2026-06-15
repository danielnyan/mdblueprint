---
id: isSource-not-mem-envyCycle
title: isSource_not_mem_envyCycle
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - isSource_not_mem_envyCycle
uses:
  - Valuation
  - Allocation
  - isSource
  - isEnvyCycle
  - Profile.ext
  - IsZeroSum.head
  - Subtree.head
---

# isSource_not_mem_envyCycle

## Lean type

```lean
lemma isSource_not_mem_envyCycle (v : Valuation N G) (A : Allocation N G) (i : N) (hs : isSource v A i) (l : List N) (hcyc : isEnvyCycle v A l) : i ∉ l
```

## Dependencies

- Valuation
- Allocation
- isSource
- isEnvyCycle
- Profile.ext
- IsZeroSum.head
- Subtree.head
