---
id: fairCoin-expected-player0
title: fairCoin_expected_player0
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.StochasticGameTree
  declarations:
    - fairCoin_expected_player0
uses:
  - expectedPayoff
  - headStrategy
  - Strategy
  - fairCoinGame
---

# fairCoin_expected_player0

## Lean type

```lean
theorem fairCoin_expected_player0 : expectedPayoff (headStrategy : Strategy (Fin 2)) fairCoinGame 0 = 1 / 2
```

## Dependencies

- expectedPayoff
- headStrategy
- Strategy
- fairCoinGame
