---
id: unanimity-univ-isDecisive
title: unanimity_univ_isDecisive
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Decisive
  declarations:
    - unanimity_univ_isDecisive
uses:
  - SWF
  - Unanimity
  - IsDecisive
---

# unanimity_univ_isDecisive

## Lean type

```lean
theorem unanimity_univ_isDecisive [Fintype N] [Fintype A] {F : SWF N A} (h : SWF.Unanimity F) : IsDecisive F Set.univ
```

## Dependencies

- SWF
- Unanimity
- IsDecisive
