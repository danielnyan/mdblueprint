---
id: toGenericCardinalInstance
title: toGenericCardinalInstance
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Instance
  declarations:
    - toGenericCardinalInstance
uses:
---

# toGenericCardinalInstance

## Lean type

```lean
def toGenericCardinalInstance {N G : Type*} [Fintype N] [DecidableEq G] (I : AdditiveInstance N G) : SocialChoice.FairDivision.CardinalInstance N (Finset G) (Finset G)
```

## Dependencies

- none
