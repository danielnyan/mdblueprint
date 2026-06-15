---
id: RepresentsPreference-indifferent-iff
title: RepresentsPreference.indifferent_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.Foundation.Preference
  declarations:
    - RepresentsPreference.indifferent_iff
uses:
  - Indifferent
---

# RepresentsPreference.indifferent_iff

## Lean type

```lean
theorem RepresentsPreference.indifferent_iff [Preorder A] [Preorder V] {u : A → V} (h : RepresentsPreference u) (a b : A) : Indifferent a b ↔ Indifferent (u a) (u b)
```

## Dependencies

- Indifferent
