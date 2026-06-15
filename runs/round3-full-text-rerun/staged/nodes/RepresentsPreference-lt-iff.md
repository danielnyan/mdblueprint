---
id: RepresentsPreference-lt-iff
title: RepresentsPreference.lt_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Preference
  declarations:
    - RepresentsPreference.lt_iff
uses:
---

# RepresentsPreference.lt_iff

## Lean type

```lean
theorem RepresentsPreference.lt_iff [Preorder A] [Preorder V] {u : A → V} (h : RepresentsPreference u) (a b : A) : a < b ↔ u a < u b
```

## Dependencies

- none
