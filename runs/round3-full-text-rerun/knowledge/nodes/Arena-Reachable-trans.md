---
id: Arena-Reachable-trans
title: Arena.Reachable.trans
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Subgame
  declarations:
    - Arena.Reachable.trans
uses:
  - IsPositiveAffineOf.refl
  - Indifferent.refl
  - IVariant.refl
  - Arena.Reachable.step
  - CPState.step
---

# Arena.Reachable.trans

## Lean type

```lean
theorem Arena.Reachable.trans {A : Arena} {s t u : A.State} (h1 : Arena.Reachable A s t) (h2 : Arena.Reachable A t u) : Arena.Reachable A s u
```

## Dependencies

- IsPositiveAffineOf.refl
- Indifferent.refl
- IVariant.refl
- Arena.Reachable.step
- CPState.step
