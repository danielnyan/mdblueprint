---
id: Bounded
title: Bounded
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.CostM
  declarations:
    - Bounded
uses:
---

# Bounded

## Lean type

```lean
def Bounded {Input Output : Type*} [LE C] (alg : Input → CostM C Output) (size : Input → ℕ) (bound : ℕ → C) : Prop
```

## Dependencies

- none
