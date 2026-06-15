---
id: optimal
title: optimal
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.SkewSymmetric
  declarations:
    - optimal
uses:
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - theorem_of_alternative
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - rowEval
---

# optimal

## Lean type

```lean
theorem optimal [NeZero N] (S : Fin N → Fin N → 𝕜) (hS : ∀ k l, S k l = - S l k) : ∃ z : Fin N → 𝕜, (∀ k, 0 ≤ z k) ∧ (∑ k, z k = 1) ∧ (∀ l, 0 ≤ ∑ k, z k * S k l)
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- theorem_of_alternative
- IsPositiveAffineOf.symm
- Indifferent.symm
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- rowEval
