---
id: IIA
title: IIA
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - IIA
uses:
  - SWF
  - Profile
  - Prefers
---

# IIA

## Lean type

```lean
def IIA (F : SWF N A) : Prop
```

## Dependencies

- SWF
- Profile
- Prefers
