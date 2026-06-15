---
id: congr-payoff
title: congr_payoff
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.BestResponse
  declarations:
    - congr_payoff
uses:
  - Profile
  - IsWeaklyDominant.isBestResponse
  - IsBestResponse
---

# congr_payoff

## Lean type

```lean
theorem congr_payoff (G : StrategicGame N U) (σ : G.Profile) (i : N) {payoff' : G.Profile → N → U} (h : ∀ τ : G.Profile, payoff' τ i = G.payoff τ i) : IsBestResponse G σ i ↔ IsBestResponse { G with payoff
```

## Dependencies

- Profile
- IsWeaklyDominant.isBestResponse
- IsBestResponse
