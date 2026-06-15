---
id: SWF-IsDictator
title: SWF.IsDictator
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Decisive
  declarations:
    - SWF.IsDictator
uses:
  - SWF
  - IsDecisive
---

# SWF.IsDictator

## Lean type

```lean
def SWF.IsDictator [Fintype N] [Fintype A] (F : SWF N A) (i : N) : Prop
```

## Dependencies

- SWF
- IsDecisive
