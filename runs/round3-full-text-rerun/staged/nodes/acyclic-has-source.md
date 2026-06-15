---
id: acyclic-has-source
title: acyclic_has_source
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - acyclic_has_source
uses:
  - Valuation
  - Allocation
  - hasEnvyCycle
  - isSource
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - isEnvyCycle
---

# acyclic_has_source

## Lean type

```lean
lemma acyclic_has_source [Fintype N] [Nonempty N] (v : Valuation N G) (A : Allocation N G) (hdag : ¬ hasEnvyCycle v A) : ∃ i : N, isSource v A i
```

## Dependencies

- Valuation
- Allocation
- hasEnvyCycle
- isSource
- IsPositiveAffineOf.symm
- Indifferent.symm
- isEnvyCycle
