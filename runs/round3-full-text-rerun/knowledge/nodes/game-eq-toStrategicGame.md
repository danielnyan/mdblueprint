---
id: game-eq-toStrategicGame
title: game_eq_toStrategicGame
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Vickrey
  declarations:
    - game_eq_toStrategicGame
uses:
  - toStrategicGame
  - toStrategicGame
  - toStrategicGame
---

# game_eq_toStrategicGame

## Lean type

```lean
lemma game_eq_toStrategicGame (v : I → U) : game v = mechanism.toStrategicGame (fun (w : I) (pay : I → U) (vals : I → U) (i : I) => if i = w then vals i - pay i else 0) v
```

## Dependencies

- toStrategicGame
- toStrategicGame
- toStrategicGame
