---
id: utility-loser
title: utility_loser
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Vickrey
  declarations:
    - utility_loser
uses:
  - Strategy
  - Allocation
---

# utility_loser

## Lean type

```lean
lemma utility_loser {b : I → U} {i : I} (h : i ≠ winner b) : utility v b i = 0
```

## Dependencies

- Strategy
- Allocation
