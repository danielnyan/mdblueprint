---
id: Independence
title: Independence
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Utility.VNMAxioms
  declarations:
    - Independence
uses:
  - Lottery
  - stdSimplex.mix
  - Lottery.mix
---

# Independence

## Lean type

```lean
def Independence (pref : Lottery 𝕜 O → Lottery 𝕜 O → Prop) : Prop
```

## Dependencies

- Lottery
- stdSimplex.mix
- Lottery.mix
