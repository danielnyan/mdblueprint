---
id: Indifferent-trans
title: Indifferent.trans
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Preference
  declarations:
    - Indifferent.trans
uses:
  - Indifferent
---

# Indifferent.trans

## Lean type

```lean
theorem Indifferent.trans {a b c : A} (h₁ : Indifferent a b) (h₂ : Indifferent b c) : Indifferent a c
```

## Dependencies

- Indifferent
