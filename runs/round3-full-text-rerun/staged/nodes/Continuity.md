---
id: Continuity
title: Continuity
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.VNMAxioms
  declarations:
    - Continuity
uses:
  - Lottery
  - stdSimplex.mix
  - Lottery.mix
---

# Continuity

## Lean type

```lean
def Continuity (pref : Lottery 𝕜 O → Lottery 𝕜 O → Prop) : Prop
```

## Dependencies

- Lottery
- stdSimplex.mix
- Lottery.mix
