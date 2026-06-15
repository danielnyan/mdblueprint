---
id: Indifferent-symm
title: Indifferent.symm
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Preference
  declarations:
    - Indifferent.symm
uses:
  - Indifferent
---

# Indifferent.symm

## Lean type

```lean
theorem Indifferent.symm {a b : A} (h : Indifferent a b) : Indifferent b a
```

## Dependencies

- Indifferent
