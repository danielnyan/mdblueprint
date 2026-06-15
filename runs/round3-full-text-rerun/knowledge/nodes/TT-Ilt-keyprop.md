---
id: TT-Ilt-keyprop
title: TT.Ilt_keyprop
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer
  declarations:
    - TT.Ilt_keyprop
uses:
  - TT
---

# TT.Ilt_keyprop

## Lean type

```lean
lemma TT.Ilt_keyprop (a b : TT n l) : a i < b i → a <[i] b
```

## Dependencies

- TT
