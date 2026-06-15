---
id: singleton-of-card-one
title: singleton_of_card_one
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.MinimaxLoomis
  declarations:
    - singleton_of_card_one
uses:
  - Profile.ext
---

# singleton_of_card_one

## Lean type

```lean
theorem singleton_of_card_one {K : Type*} [Fintype K] [DecidableEq K] (H : Fintype.card K = 1) : ∃ a : K, (Finset.univ : Finset K) = {a}
```

## Dependencies

- Profile.ext
