---
id: exists-strategic-game-nash-equilibrium
title: exists_strategic_game_nash_equilibrium
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - exists_strategic_game_nash_equilibrium
uses:
  - MixedProfile
  - toStrategicGame
  - IsMixedNashEq
  - exists_mixed_nash_equilibrium
  - expectedPayoff_toStrategicGame_zero
  - deviateMixed
  - pureToMixed
  - expectedPayoff_toStrategicGame_one
---

# exists_strategic_game_nash_equilibrium

## Lean type

```lean
theorem exists_strategic_game_nash_equilibrium : ∃ p : StrategicGame.MixedProfile A.toStrategicGame, StrategicGame.IsMixedNashEq A.toStrategicGame p
```

## Dependencies

- MixedProfile
- toStrategicGame
- IsMixedNashEq
- exists_mixed_nash_equilibrium
- expectedPayoff_toStrategicGame_zero
- deviateMixed
- pureToMixed
- expectedPayoff_toStrategicGame_one
