---
id: toShareInstance
title: toShareInstance
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Instance
  declarations:
    - toShareInstance
uses:
  - inducedSharePref
---

# toShareInstance

## Lean type

```lean
def toShareInstance {N G : Type*} [Fintype N] [DecidableEq G] (I : AdditiveInstance N G) : SocialChoice.FairDivision.ShareInstance N (Finset G) (Finset G)
```

## Dependencies

- inducedSharePref
