---
id: card-le-of-domiant
title: card_le_of_domiant
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - card_le_of_domiant
uses:
  - isDominant
  - keylemma_of_dominant
---

# card_le_of_domiant

## Lean type

```lean
lemma card_le_of_domiant {σ : Finset T} {C: Finset I} (h1 : IST.isDominant σ C) : σ.card ≤ C.card
```

## Dependencies

- isDominant
- keylemma_of_dominant
