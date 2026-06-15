---
id: ExtractsGameTree-spe-on-to-nash-at
title: ExtractsGameTree.spe_on_to_nash_at
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.FiniteArenaExtraction
  declarations:
    - ExtractsGameTree.spe_on_to_nash_at
uses:
  - Strategy
  - IsSubgamePerfectOn
  - IsNashAt
  - IsSubgamePerfectOn.toNashAt
---

# ExtractsGameTree.spe_on_to_nash_at

## Lean type

```lean
theorem ExtractsGameTree.spe_on_to_nash_at [TotalPreorder U] {s : G.State} {tree : GameTree N U} (_h : ExtractsGameTree G s tree) {σ : GameTree.Strategy N U} (hspe : GameTree.IsSubgamePerfectOn σ tree) : GameTree.IsNashAt σ tree
```

## Dependencies

- Strategy
- IsSubgamePerfectOn
- IsNashAt
- IsSubgamePerfectOn.toNashAt
