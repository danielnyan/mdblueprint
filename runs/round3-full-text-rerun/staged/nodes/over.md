---
id: over
title: over
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Decisive
  declarations:
    - over
uses:
  - Unanimity
---

# over

## Lean type

```lean
theorem over strict voting profiles. This file records the public decisive-coalition vocabulary for the strict ranked-ballot voting domain. The proof route is the standard one: 1. unanimity implies the grand coalition is decisive; 2. weak decisiveness for one ordered pair spreads to decisiveness for all pairs; 3. any decisive coalition of size at least two has a strictly smaller nonempty decisive subcoalition; 4. a minimal decisive coalition is a singleton; 5. the singleton voter is a dictator. -/ namespace SocialChoice namespace Voting variable {N A : Type*} /-- A coalition is decisive for `a` over `b` if unanimous strict support inside the coalition forces the social strict preference `a ≻ b`. -/
```

## Dependencies

- Unanimity
