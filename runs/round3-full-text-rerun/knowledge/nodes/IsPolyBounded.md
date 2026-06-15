---
id: IsPolyBounded
title: IsPolyBounded
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.CostM
  declarations:
    - IsPolyBounded
uses:
  - Bounded
---

# IsPolyBounded

## Lean type

```lean
def IsPolyBounded {Input Output : Type*} (alg : Input → CostM ℕ Output) (size : Input → ℕ) : Prop
```

## Dependencies

- Bounded
