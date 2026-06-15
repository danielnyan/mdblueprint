---
id: common-guarantee-eq-value
title: common_guarantee_eq_value
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - common_guarantee_eq_value
uses:
  - IsPlayerIGuarantee
  - IsPlayerIIGuarantee
  - lamB.aux.bddAbove
  - lam.aux.bddAbove
  - muB.aux.bddBelow
  - mu.aux.bddBelow
  - minimax_theorem
  - value_eq_maximin
---

# common_guarantee_eq_value

## Lean type

```lean
theorem common_guarantee_eq_value (w : ℝ) (h1 : A.IsPlayerIGuarantee w) (h2 : A.IsPlayerIIGuarantee w) : w = A.value
```

## Dependencies

- IsPlayerIGuarantee
- IsPlayerIIGuarantee
- lamB.aux.bddAbove
- lam.aux.bddAbove
- muB.aux.bddBelow
- mu.aux.bddBelow
- minimax_theorem
- value_eq_maximin
