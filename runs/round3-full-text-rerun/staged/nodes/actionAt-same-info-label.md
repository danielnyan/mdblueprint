---
id: actionAt-same-info-label
title: actionAt_same_info_label
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.ImperfectInformation
  declarations:
    - actionAt_same_info_label
uses:
  - PureStrategy
  - StrategyProfile.actionAt
  - PureStrategy.actionAt
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
---

# actionAt_same_info_label

## Lean type

```lean
theorem actionAt_same_info_label {i : N} (σ : G.PureStrategy i) {s t : G.State} {k : G.InfoSet} (hs : G.info s = some k) (ht : G.info t = some k) (hms : G.mover s = some i) (hmt : G.mover t = some i) : PureStrategy.actionAt G σ hs hms = σ k s hs hms ∧ PureStrategy.actionAt G σ ht hmt = σ k t ht hmt
```

## Dependencies

- PureStrategy
- StrategyProfile.actionAt
- PureStrategy.actionAt
- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
