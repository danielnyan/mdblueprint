---
id: payoff-lt-of-price-lt
title: payoff_lt_of_price_lt
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.OrderedGroup
  declarations:
    - payoff_lt_of_price_lt
uses:
---

# payoff_lt_of_price_lt

## Lean type

```lean
theorem payoff_lt_of_price_lt {value price₁ price₂ : U} (h : price₁ < price₂) : value - price₂ < value - price₁
```

## Dependencies

- none
