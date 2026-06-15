# Lean Adjudication Report

- Run: `runs/refactor-countercheck/20260615T131427Z`
- Knowledge root: `../EconCSLib/docs/knowledge`
- Lean source root: `../EconCSLib`
- Inputs used:
  - `reports/refactor-report.md`
  - `dry-runs/refactor-dry-run.json`
  - `countercheck/pairs.json`
  - `countercheck/skipped.json`
  - `countercheck/summary.json`

## Factual Extraction Summary

- Countercheck pairs adjudicated: 16
- Skipped candidates: 1
- True discrepancies found: 0
- False abends found: 16
- Needs-review cases in the adjudicated set: 0
- The dominant pattern is namespace or granularity drift between authored node declarations and Lean-extracted declaration names, plus a small amount of helper-lemma leakage and topic-home divergence.
- No admitted or staged knowledge files were edited.

## Node-To-Theorem Mapping

| Node | Lean fact | Mapping note | Pair judgment |
| --- | --- | --- | --- |
| `game_theory.strategic_game.zero_sum.core.strong_complementarity` | `MatrixGame.exists_strong_complementary_pair` | Same theorem as the math node, but surfaced under the Lean file namespace rather than the authored node namespace. | `false_abend` |
| `math.minimax.strong_complementarity` | `MatrixGame.exists_strong_complementary_pair` | Same theorem as above; this is a many-to-one mapping from one Lean theorem to two authored nodes. | `false_abend` |
| `foundation.cost.examples.boyer_moore` | `BoyerMoore.majority`, `BoyerMoore.loop_cost`, `BoyerMoore.majority_peak_le` | Qualified-name mismatch only; Lean also exposes a helper lemma (`loop_cost`) that is part of the formalization artifact. | `false_abend` |
| `foundation.cost.examples.gcd` | `GCD.gcd`, `GCD.gcd_cost_le`, `GCD.gcd_cost_log_le` | Namespace prefix drift only; theorem content matches the authored node. | `false_abend` |
| `foundation.cost.examples.lcs` | `LCS.lcs`, `LCS.lcs_cost_subset`, `LCS.lcs_cost_card_le` | Namespace prefix drift only; the extra extracted dependency is the expected helper lemma `lcs_cost_subset`. | `false_abend` |
| `foundation.cost.examples.memo_fib` | `MemoFib.fibAux`, `MemoFib.fib`, `MemoFib.fibAux_ret`, `MemoFib.fib_value`, `MemoFib.fibAux_cost`, `MemoFib.fib_cost`, `MemoFib.fib_cost_card` | Qualified-name mismatch only, with extra helper lemmas surfaced by the extractor. | `false_abend` |
| `foundation.cost.examples.par_all` | `ParAll.parMap_unit_cost_le` | Namespace prefix drift only. | `false_abend` |
| `foundation.cost.examples.par_sum` | `ParSum.parSum`, `ParSum.parSum_cost_le_clog`, `ParSum.parSum_cost_le_length` | Namespace prefix drift only; helper dependency `parSum` is expected. | `false_abend` |
| `foundation.cost.examples.reverse_space` | `ReverseSpace.naiveReverse`, `ReverseSpace.naiveReverse_cost_le` | Namespace prefix drift only. | `false_abend` |
| `game_theory.extensive_game.perfect_information.simple_perfect_information_game` | `Examples.SimpleGameTree.sample`, `Examples.SimpleGameTree.sample_zero_sum`, `Examples.SimpleGameTree.sample_zermelo_spe`, `Examples.SimpleGameTree.sample_zermelo_ne`, `Examples.SimpleGameTree.sample_value_zero_sum` | The Lean artifact is the same example tree family; the mismatch is entirely in extracted qualification and module home. | `false_abend` |
| `game_theory.strategic_game.prisoners_dilemma` | `PrisonersDilemma.PD`, `PrisonersDilemma.pd_defect_weakly_dominant`, `PrisonersDilemma.pd_defect_nash`, `PrisonersDilemma.pd_nash_unique`, `PrisonersDilemma.pd_pareto_suboptimal` | Namespace prefix drift only. | `false_abend` |
| `game_theory.strategic_game.zero_sum.applications.perron_frobenius_positive_matrix` | `EconCSLib.LinearAlgebra.perron_frobenius` | Topical home differs from the Lean module home, but the theorem content is the same. | `false_abend` |
| `game_theory.strategic_game.zero_sum.core.mixed_extension` | `expectedPayoffMatrix` | Same Lean fact, but the extractor also surfaced many supporting simplex lemmas and one missing authored use. | `false_abend` |
| `game_theory.strategic_game.zero_sum.core.mixed_strategy_simplex` | `stdSimplex.pure`, `wsum` | Same Lean fact, with helper-theorem spillover from the simplex library. | `false_abend` |
| `game_theory.strategic_game.zero_sum.examples.computation_three_by_two_example` | `EconCSLib.StrategicGame.Examples.threeByTwoExample`, `EconCSLib.StrategicGame.Examples.threeByTwoRowOpt`, `EconCSLib.StrategicGame.Examples.threeByTwoColOpt`, `EconCSLib.StrategicGame.Examples.threeByTwoExample_value` | Same example family, but the Lean file uses a different namespace root than the authored node. | `false_abend` |
| `game_theory.strategic_game.zero_sum.examples.diagonal_matrix_game_value` | `EconCSLib.StrategicGame.Examples.diagonalGame_value` | Same example theorem, with namespace prefix drift and extra helper declarations. | `false_abend` |

## Discrepancy Table

| Node | Discrepancy class | Evidence | Adjudication |
| --- | --- | --- | --- |
| `game_theory.strategic_game.zero_sum.core.strong_complementarity` | `many_to_one_mapping`, `missing_theorem`, `extra_theorem` | One Lean theorem mapped to two authored nodes; the name is unqualified in Lean and qualified in the authored graph. | Benign artifact |
| `math.minimax.strong_complementarity` | `many_to_one_mapping`, `missing_theorem`, `extra_theorem` | Same Lean theorem as above, intentionally reused across two topic homes. | Benign artifact |
| `foundation.cost.examples.boyer_moore` | `missing_declaration`, `extra_declaration`, `helper_lemma_leakage`, `missing_dependency` | Lean exposes unqualified declarations plus `loop_cost`; authored node uses are not surfaced as extracted dependencies. | Benign artifact |
| `foundation.cost.examples.gcd` | `missing_declaration`, `extra_declaration` | Pure namespace mismatch between `GCD.*` authored declarations and `gcd*` Lean extraction. | Benign artifact |
| `foundation.cost.examples.lcs` | `missing_declaration`, `extra_declaration`, `helper_lemma_leakage`, `missing_dependency` | Same pattern as above, plus the extracted helper dependency `lcs_cost_subset`. | Benign artifact |
| `foundation.cost.examples.memo_fib` | `missing_declaration`, `extra_declaration`, `helper_lemma_leakage`, `missing_dependency` | Namespace drift plus helper lemmas and missing surfaced authored uses. | Benign artifact |
| `foundation.cost.examples.par_all` | `missing_declaration`, `extra_declaration` | Qualified-name mismatch only. | Benign artifact |
| `foundation.cost.examples.par_sum` | `missing_declaration`, `extra_declaration`, `helper_lemma_leakage`, `missing_dependency` | Namespace drift plus helper dependency `parSum`. | Benign artifact |
| `foundation.cost.examples.reverse_space` | `missing_declaration`, `extra_declaration`, `missing_dependency` | Namespace drift only. | Benign artifact |
| `game_theory.extensive_game.perfect_information.simple_perfect_information_game` | `missing_declaration`, `extra_declaration`, `missing_dependency` | Same example family, but Lean exports it under `Examples.SimpleGameTree`. | Benign artifact |
| `game_theory.strategic_game.prisoners_dilemma` | `missing_declaration`, `extra_declaration`, `missing_dependency` | Namespace drift plus the authored topical use nodes are not surfaced in the Lean extraction. | Benign artifact |
| `game_theory.strategic_game.zero_sum.applications.perron_frobenius_positive_matrix` | `missing_declaration`, `extra_declaration` | Topic-home mismatch only. | Benign artifact |
| `game_theory.strategic_game.zero_sum.core.mixed_extension` | `extra_declaration`, `missing_dependency`, `formalization_artifact_not_in_authored_graph` | The Lean file exports many supporting simplex lemmas not present in the authored node. | Benign artifact |
| `game_theory.strategic_game.zero_sum.core.mixed_strategy_simplex` | `extra_declaration`, `missing_dependency`, `formalization_artifact_not_in_authored_graph` | The Lean file exports helper simplex lemmas beyond the authored node. | Benign artifact |
| `game_theory.strategic_game.zero_sum.examples.computation_three_by_two_example` | `missing_declaration`, `extra_declaration`, `missing_dependency` | Namespace drift plus a different Lean namespace root for the example family. | Benign artifact |
| `game_theory.strategic_game.zero_sum.examples.diagonal_matrix_game_value` | `missing_declaration`, `extra_declaration`, `missing_dependency` | Namespace drift plus a different Lean namespace root for the example. | Benign artifact |

## Final Judgment Table

| Node | Verdict | Confidence | Rationale |
| --- | --- | --- | --- |
| `game_theory.strategic_game.zero_sum.core.strong_complementarity` | `accept` | `0.94` | Same theorem appears in Lean; the mismatch is naming and canonical-home granularity. |
| `math.minimax.strong_complementarity` | `accept` | `0.94` | Same theorem appears in Lean; duplicate topical ownership is a review issue, not a factual discrepancy. |
| `foundation.cost.examples.boyer_moore` | `accept` | `0.96` | The Lean declarations and the authored node describe the same cost example. |
| `foundation.cost.examples.gcd` | `accept` | `0.97` | Pure namespace drift. |
| `foundation.cost.examples.lcs` | `accept` | `0.96` | Same theorem family; helper lemma spillover is expected. |
| `foundation.cost.examples.memo_fib` | `accept` | `0.95` | Same theorem family; extractor granularity is finer than the authored node. |
| `foundation.cost.examples.par_all` | `accept` | `0.97` | Pure namespace drift. |
| `foundation.cost.examples.par_sum` | `accept` | `0.95` | Same theorem family; helper dependency is a formalization artifact. |
| `foundation.cost.examples.reverse_space` | `accept` | `0.96` | Pure namespace drift. |
| `game_theory.extensive_game.perfect_information.simple_perfect_information_game` | `accept` | `0.93` | Lean exports the same example tree through a different namespace. |
| `game_theory.strategic_game.prisoners_dilemma` | `accept` | `0.94` | The proof content matches; topical uses are not a semantic conflict. |
| `game_theory.strategic_game.zero_sum.applications.perron_frobenius_positive_matrix` | `accept` | `0.92` | Same theorem, different home. |
| `game_theory.strategic_game.zero_sum.core.mixed_extension` | `accept` | `0.91` | Same core fact; extracted support lemmas are supplementary. |
| `game_theory.strategic_game.zero_sum.core.mixed_strategy_simplex` | `accept` | `0.91` | Same core fact; helper lemmas are supplementary. |
| `game_theory.strategic_game.zero_sum.examples.computation_three_by_two_example` | `accept` | `0.93` | Same example theorem family, different namespace root. |
| `game_theory.strategic_game.zero_sum.examples.diagonal_matrix_game_value` | `accept` | `0.93` | Same example theorem family, different namespace root. |

## Final Filter Table

| Node | Final filter | Why |
| --- | --- | --- |
| `game_theory.strategic_game.zero_sum.core.strong_complementarity` | `false_abend` | The theorem is present; only the namespace and canonical-home choice differ. |
| `math.minimax.strong_complementarity` | `false_abend` | The theorem is present; the duplicate topical home is intentional or editorial. |
| `foundation.cost.examples.boyer_moore` | `false_abend` | The Lean declarations match the authored example, with helper-lemma spillover. |
| `foundation.cost.examples.gcd` | `false_abend` | Pure namespace drift. |
| `foundation.cost.examples.lcs` | `false_abend` | Same theorem content, with expected helper-lemma extraction. |
| `foundation.cost.examples.memo_fib` | `false_abend` | Same theorem content, with expected helper-lemma extraction. |
| `foundation.cost.examples.par_all` | `false_abend` | Pure namespace drift. |
| `foundation.cost.examples.par_sum` | `false_abend` | Same theorem content, with helper-lemma spillover. |
| `foundation.cost.examples.reverse_space` | `false_abend` | Pure namespace drift. |
| `game_theory.extensive_game.perfect_information.simple_perfect_information_game` | `false_abend` | Same example family, different namespace root. |
| `game_theory.strategic_game.prisoners_dilemma` | `false_abend` | Same theorem family, different namespace root. |
| `game_theory.strategic_game.zero_sum.applications.perron_frobenius_positive_matrix` | `false_abend` | Same theorem, different conceptual home. |
| `game_theory.strategic_game.zero_sum.core.mixed_extension` | `false_abend` | Same theorem, with extra supporting simplex lemmas. |
| `game_theory.strategic_game.zero_sum.core.mixed_strategy_simplex` | `false_abend` | Same theorem, with extra supporting simplex lemmas. |
| `game_theory.strategic_game.zero_sum.examples.computation_three_by_two_example` | `false_abend` | Same theorem family, different namespace root. |
| `game_theory.strategic_game.zero_sum.examples.diagonal_matrix_game_value` | `false_abend` | Same theorem family, different namespace root. |

## Skipped Candidate

- `game_theory.strategic_game.zero_sum.examples.matching_pennies` was listed in `skipped.json` with reason `max-countercheck-pairs limit reached`.
- It was not part of the adjudicated pair set, so this report makes no judgment on it.

## Conclusion

The adjudicated countercheck set contains no true discrepancies. All 16 checked pairs are false abends caused by namespace qualification, topic-home divergence, helper-lemma leakage, or many-to-one mapping between one Lean theorem and two authored nodes.
