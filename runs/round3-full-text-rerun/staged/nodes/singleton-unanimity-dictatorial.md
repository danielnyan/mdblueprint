---
id: singleton-unanimity-dictatorial
title: singleton_unanimity_dictatorial
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Decisive
  declarations:
    - singleton_unanimity_dictatorial
uses:
  - SWF
  - Unanimity
  - Dictatorial
---

# singleton_unanimity_dictatorial

## Lean type

```lean
theorem singleton_unanimity_dictatorial [Fintype N] [Fintype A] [Subsingleton N] [Nonempty N] {F : SWF N A} (h : SWF.Unanimity F) : SWF.Dictatorial F
```

## Dependencies

- SWF
- Unanimity
- Dictatorial
