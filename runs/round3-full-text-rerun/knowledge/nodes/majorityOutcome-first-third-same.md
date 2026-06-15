---
id: majorityOutcome-first-third-same
title: majorityOutcome_first_third_same
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CandidateChoice
  declarations:
    - majorityOutcome_first_third_same
uses:
  - majorityOutcome
---

# majorityOutcome_first_third_same

## Lean type

```lean
@[simp] theorem majorityOutcome_first_third_same (a b : Candidate) : majorityOutcome a b a = Accepted a
```

## Dependencies

- majorityOutcome
