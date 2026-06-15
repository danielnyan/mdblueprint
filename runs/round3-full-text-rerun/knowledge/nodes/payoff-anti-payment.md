---
id: payoff-anti-payment
title: payoff_anti_payment
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.OrderedGroup
  declarations:
    - payoff_anti_payment
uses:
---

# payoff_anti_payment

## Lean type

```lean
theorem payoff_anti_payment {value price₁ price₂ : U} (h : price₁ ≤ price₂) : value - price₂ ≤ value - price₁
```

## Dependencies

- none
