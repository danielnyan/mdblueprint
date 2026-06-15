---
id: exists-nonempty-decisive-of-size
title: exists_nonempty_decisive_of_size
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Decisive
  declarations:
    - exists_nonempty_decisive_of_size
uses:
  - SWF
  - IsDecisive
---

# exists_nonempty_decisive_of_size

## Lean type

```lean
def exists_nonempty_decisive_of_size [Fintype N] [Fintype A] (F : SWF N A) (n : Nat) : Prop
```

## Dependencies

- SWF
- IsDecisive
