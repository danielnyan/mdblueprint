---
id: parity-lemma
title: parity_lemma
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - parity_lemma
uses:
---

# parity_lemma

## Lean type

```lean
lemma parity_lemma {a b c d : ℕ } (h1 : Odd a) (h2 : Even b) (h3 : Even d) (h4 : a + b = c + d ): Odd c
```

## Dependencies

- none
