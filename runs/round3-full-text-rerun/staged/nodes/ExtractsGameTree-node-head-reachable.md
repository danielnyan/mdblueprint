---
id: ExtractsGameTree-node-head-reachable
title: ExtractsGameTree.node_head_reachable
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.FiniteArenaExtraction
  declarations:
    - ExtractsGameTree.node_head_reachable
uses:
  - IsZeroSum.head
  - Subtree.head
  - IsReachable.next
  - Arena.Reachable.step
  - CPState.step
  - IsPositiveAffineOf.refl
  - Indifferent.refl
  - IVariant.refl
---

# ExtractsGameTree.node_head_reachable

## Lean type

```lean
theorem ExtractsGameTree.node_head_reachable {s : G.State} {i : N} {headTree : GameTree N U} {tailTrees : List (GameTree N U)} (h : ExtractsGameTree G s (GameTree.Node i headTree tailTrees)) : ∃ head : G.Action s, Arena.Reachable G.toArena s (G.next s head) ∧ ExtractsGameTree G (G.next s head) headTree
```

## Dependencies

- IsZeroSum.head
- Subtree.head
- IsReachable.next
- Arena.Reachable.step
- CPState.step
- IsPositiveAffineOf.refl
- Indifferent.refl
- IVariant.refl
