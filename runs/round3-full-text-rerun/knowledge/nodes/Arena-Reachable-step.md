---
id: Arena-Reachable-step
title: Arena.Reachable.step
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Subgame
  declarations:
    - Arena.Reachable.step
uses:
  - CPState.step
  - IsReachable.next
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - IsPositiveAffineOf.refl
  - Indifferent.refl
  - IVariant.refl
---

# Arena.Reachable.step

## Lean type

```lean
theorem Arena.Reachable.step' {A : Arena} {s t : A.State} (h : Arena.Reachable A s t) (a : A.Action t) : Arena.Reachable A s (A.next t a)
```

## Dependencies

- CPState.step
- IsReachable.next
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- IsPositiveAffineOf.refl
- Indifferent.refl
- IVariant.refl
