---
id: strict-transitive
title: strict_transitive
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Preference
  declarations:
    - strict_transitive
uses:
---

# strict_transitive

## Lean type

```lean
theorem strict_transitive {A : Type*} {R : A → A → Prop} (h : Transitive R) : Transitive (strict R)
```

## Dependencies

- none
