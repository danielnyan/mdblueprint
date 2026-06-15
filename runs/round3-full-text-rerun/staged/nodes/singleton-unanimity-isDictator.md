---
id: singleton-unanimity-isDictator
title: singleton_unanimity_isDictator
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Decisive
  declarations:
    - singleton_unanimity_isDictator
uses:
  - SWF
  - Unanimity
  - SWF.IsDictator
---

# singleton_unanimity_isDictator

## Lean type

```lean
theorem singleton_unanimity_isDictator [Fintype N] [Fintype A] [Subsingleton N] {F : SWF N A} (h : SWF.Unanimity F) (i : N) : F.IsDictator i
```

## Dependencies

- SWF
- Unanimity
- SWF.IsDictator
