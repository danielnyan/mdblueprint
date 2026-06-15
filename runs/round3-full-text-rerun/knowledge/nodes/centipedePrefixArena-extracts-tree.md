---
id: centipedePrefixArena-extracts-tree
title: centipedePrefixArena_extracts_tree
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CentipedeGame
  declarations:
    - centipedePrefixArena_extracts_tree
uses:
  - centipedePrefixArena
  - ReachedSubgamePayoffTransfer.init
  - centipedePrefixTree
  - IsZeroSum.head
  - Subtree.head
  - isEmpty
---

# centipedePrefixArena_extracts_tree

## Lean type

```lean
theorem centipedePrefixArena_extracts_tree : ExtensiveGame.ExtractsGameTree centipedePrefixArena centipedePrefixArena.init centipedePrefixTree
```

## Dependencies

- centipedePrefixArena
- ReachedSubgamePayoffTransfer.init
- centipedePrefixTree
- IsZeroSum.head
- Subtree.head
- isEmpty
