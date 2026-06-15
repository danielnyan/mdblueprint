---
id: fairCoin-probs-sum-to-one
title: fairCoin_probs_sum_to_one
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.StochasticGameTree
  declarations:
    - fairCoin_probs_sum_to_one
uses:
  - ChanceProbabilitiesSumToOne
---

# fairCoin_probs_sum_to_one

## Lean type

```lean
theorem fairCoin_probs_sum_to_one : ChanceProbabilitiesSumToOne (1 / 2) (List.cons (1 / 2, StochasticGameTree.Leaf (fun i : Fin 2 => if i = 0 then 0 else 1)) List.nil)
```

## Dependencies

- ChanceProbabilitiesSumToOne
