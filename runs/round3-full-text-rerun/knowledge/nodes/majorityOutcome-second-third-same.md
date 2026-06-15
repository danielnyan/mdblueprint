---
id: majorityOutcome-second-third-same
title: majorityOutcome_second_third_same
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CandidateChoice
  declarations:
    - majorityOutcome_second_third_same
uses:
  - majorityOutcome
---

# majorityOutcome_second_third_same

## Lean type

```lean
@[simp] theorem majorityOutcome_second_third_same (a b : Candidate) : majorityOutcome b a a = Accepted a
```

## Dependencies

- majorityOutcome
