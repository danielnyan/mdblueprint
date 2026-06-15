---
id: muB-aux-ge-muB0
title: muB.aux.ge_muB0
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - muB.aux.ge_muB0
uses:
  - IsPositive
  - muB.aux.bddBelow
  - mu.aux.bddBelow
---

# muB.aux.ge_muB0

## Lean type

```lean
theorem muB.aux.ge_muB0 {A B : I → J → ℝ} (hB : IsPositive B) (y : stdSimplex ℝ J) : muB0 A B ≤ muB.aux A B y
```

## Dependencies

- IsPositive
- muB.aux.bddBelow
- mu.aux.bddBelow
