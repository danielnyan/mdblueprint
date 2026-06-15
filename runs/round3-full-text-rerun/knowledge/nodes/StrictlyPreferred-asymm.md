---
id: StrictlyPreferred-asymm
title: StrictlyPreferred.asymm
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Preference
  declarations:
    - StrictlyPreferred.asymm
uses:
  - StrictlyPreferred
---

# StrictlyPreferred.asymm

## Lean type

```lean
theorem StrictlyPreferred.asymm {a b : A} (h : StrictlyPreferred a b) : ¬ StrictlyPreferred b a
```

## Dependencies

- StrictlyPreferred
