---
id: copeland-isTotal
title: copeland_isTotal
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - copeland_isTotal
uses:
  - IsTotal
  - Profile
  - MajorityPrefers
  - Profile.ext
  - Prefers
  - margin_pos
---

# copeland_isTotal

## Lean type

```lean
theorem copeland_isTotal [Fintype N] [Fintype A] [Nonempty A] : IsTotal (N
```

## Dependencies

- IsTotal
- Profile
- MajorityPrefers
- Profile.ext
- Prefers
- margin_pos
