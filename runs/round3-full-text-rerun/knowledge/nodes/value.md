---
id: value
title: value
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.ZeroSumGameTreeWithChance
  declarations:
    - value
uses:
---

# value

## Lean type

```lean
def value : GameTree → ℚ | Leaf r => r | Pnode p L R => match p with | .A => max L.value R.value | .B => min L.value R.value | Nnode prob L R => prob * L.value + (1 - prob) * R.value /-- **A's dominant strategy**: at each A-node, move to whichever child has the higher value; ties go left. -/
```

## Dependencies

- none
