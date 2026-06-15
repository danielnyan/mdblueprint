---
id: StrictlyPreferred-trans
title: StrictlyPreferred.trans
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Preference
  declarations:
    - StrictlyPreferred.trans
uses:
  - StrictlyPreferred
---

# StrictlyPreferred.trans

## Lean type

```lean
theorem StrictlyPreferred.trans {a b c : A} (h₁ : StrictlyPreferred a b) (h₂ : StrictlyPreferred b c) : StrictlyPreferred a c
```

## Dependencies

- StrictlyPreferred
