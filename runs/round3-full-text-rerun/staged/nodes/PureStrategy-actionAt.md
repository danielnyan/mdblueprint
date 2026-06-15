---
id: PureStrategy-actionAt
title: PureStrategy.actionAt
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.ImperfectInformation
  declarations:
    - PureStrategy.actionAt
uses:
  - PureStrategy
---

# PureStrategy.actionAt

## Lean type

```lean
def PureStrategy.actionAt {i : N} (σ : G.PureStrategy i) {s : G.State} {k : G.InfoSet} (hinfo : G.info s = some k) (hmover : G.mover s = some i) : G.Action s
```

## Dependencies

- PureStrategy
