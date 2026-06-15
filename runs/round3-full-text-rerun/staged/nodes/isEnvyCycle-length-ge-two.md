---
id: isEnvyCycle-length-ge-two
title: isEnvyCycle_length_ge_two
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - isEnvyCycle_length_ge_two
uses:
  - Valuation
  - Allocation
  - isEnvyCycle
---

# isEnvyCycle_length_ge_two

## Lean type

```lean
lemma isEnvyCycle_length_ge_two (v : Valuation N G) (A : Allocation N G) (l : List N) (hcyc : isEnvyCycle v A l) : 2 ≤ l.length
```

## Dependencies

- Valuation
- Allocation
- isEnvyCycle
