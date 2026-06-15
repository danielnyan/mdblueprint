---
id: outcome
title: outcome
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.ZeroSumGameTreeWithChance
  declarations:
    - outcome
uses:
  - Strategy
---

# outcome

## Lean type

```lean
def outcome (SA SB : Strategy) : GameTree → ℚ | Leaf r => r | Pnode p L R => match p with | .A => match SA L R with | .l => outcome SA SB L | .r => outcome SA SB R | .B => match SB L R with | .l => outcome SA SB L | .r => outcome SA SB R | Nnode prob L R => prob * outcome SA SB L + (1 - prob) * outcome SA SB R /-! ### Main theorem -/ /-- **Soundness of `DStrategy`**: the backward-induction value is a lower bound on the outcome A achieves by following `DStrategy`, regardless of how B plays. Formally: for every B-strategy `SB` and game tree `t`, `t.value ≤ t.outcome DStrategy SB`. -/
```

## Dependencies

- Strategy
