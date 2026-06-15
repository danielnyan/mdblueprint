---
id: ExtractsGameTree-leaf-payoff
title: ExtractsGameTree.leaf_payoff
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.FiniteArenaExtraction
  declarations:
    - ExtractsGameTree.leaf_payoff
uses:
---

# ExtractsGameTree.leaf_payoff

## Lean type

```lean
theorem ExtractsGameTree.leaf_payoff {s : G.State} {p : N → U} (h : ExtractsGameTree G s (GameTree.Leaf p)) : p = G.payoff s
```

## Dependencies

- none
