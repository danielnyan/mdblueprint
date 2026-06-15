---
id: keylemma-of-dominant
title: keylemma_of_dominant
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - keylemma_of_dominant
uses:
  - isDominant
  - Profile.ext
---

# keylemma_of_dominant

## Lean type

```lean
lemma keylemma_of_dominant {σ : Finset T} {C: Finset I} (h1 : IST.isDominant σ C) (h2: σ.Nonempty): σ = C.image (mini h2)
```

## Dependencies

- isDominant
- Profile.ext
