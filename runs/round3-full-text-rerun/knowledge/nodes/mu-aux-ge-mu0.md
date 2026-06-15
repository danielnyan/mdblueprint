---
id: mu-aux-ge-mu0
title: mu.aux.ge_mu0
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.MinimaxLoomis
  declarations:
    - mu.aux.ge_mu0
uses:
  - muB.aux.bddBelow
  - mu.aux.bddBelow
---

# mu.aux.ge_mu0

## Lean type

```lean
theorem mu.aux.ge_mu0 (A : I → J → ℝ) (y : stdSimplex ℝ J) : mu0 A ≤ mu.aux A y
```

## Dependencies

- muB.aux.bddBelow
- mu.aux.bddBelow
