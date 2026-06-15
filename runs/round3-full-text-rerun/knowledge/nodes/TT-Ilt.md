---
id: TT-Ilt
title: TT.Ilt
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer
  declarations:
    - TT.Ilt
uses:
  - TT
  - StrictlyPreferred.irrefl
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
---

# TT.Ilt

## Lean type

```lean
abbrev TT.Ilt ( x y : TT n l)
```

## Dependencies

- TT
- StrictlyPreferred.irrefl
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
