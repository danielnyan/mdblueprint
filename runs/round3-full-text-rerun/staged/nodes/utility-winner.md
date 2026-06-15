---
id: utility-winner
title: utility_winner
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Vickrey
  declarations:
    - utility_winner
uses:
  - Allocation
---

# utility_winner

## Lean type

```lean
lemma utility_winner {b : I → U} {i : I} (h : i = winner b) : utility v b i = v i - secondPrice b
```

## Dependencies

- Allocation
