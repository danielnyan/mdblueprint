---
id: answerElab
title: answerElab
kind: theorem
status: staged
lean:
  module: EconCSLib.OpenProblem.Util.Answer
  declarations:
    - answerElab
uses:
  - elabTermAndAnnotate
  - mkAnswerAnnotation
---

# answerElab

## Lean type

```lean
@[term_elab answer] def answerElab : TermElab
```

## Dependencies

- elabTermAndAnnotate
- mkAnswerAnnotation
