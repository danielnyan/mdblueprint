---
id: StrictlyPreferred-irrefl
title: StrictlyPreferred.irrefl
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Preference
  declarations:
    - StrictlyPreferred.irrefl
uses:
  - StrictlyPreferred
---

# StrictlyPreferred.irrefl

## Lean type

```lean
theorem StrictlyPreferred.irrefl (a : A) : ¬ StrictlyPreferred a a
```

## Dependencies

- StrictlyPreferred
