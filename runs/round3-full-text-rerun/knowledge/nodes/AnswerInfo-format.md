---
id: AnswerInfo-format
title: AnswerInfo.format
kind: theorem
status: staged
lean:
  module: EconCSLib.OpenProblem.Util.Answer
  declarations:
    - AnswerInfo.format
uses:
  - answerElab
  - stdSimplex.pure
  - Lottery.pure
---

# AnswerInfo.format

## Lean type

```lean
def AnswerInfo.format (a : AnswerInfo) : Elab.Term.TermElabM MessageData
```

## Dependencies

- answerElab
- stdSimplex.pure
- Lottery.pure
