---
id: TT-Ilt-def
title: TT.Ilt_def
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer
  declarations:
    - TT.Ilt_def
uses:
  - TT
  - TT.Ilt
---

# TT.Ilt_def

## Lean type

```lean
lemma TT.Ilt_def (a b : TT n l) : (a <[i] b) ↔ TT.Ilt i a b
```

## Dependencies

- TT
- TT.Ilt
