---
id: mk-subseq
title: mk_subseq
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer
  declarations:
    - mk_subseq
uses:
---

# mk_subseq

## Lean type

```lean
def mk_subseq (f : ℕ → ℕ) (h : ∀ n, n < f n) : ℕ → ℕ | 0 => f 0 | n+1 => f (mk_subseq f h n)
```

## Dependencies

- none
