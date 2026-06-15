---
agent: graph-refactor-proposer
target:
  knowledge_root: /home/azureuser/EconCSLib/docs/knowledge
  topic: social_choice.fair_division
decision: proposals
created_at: "2026-06-15T00:00:00Z"
inputs:
  - /home/azureuser/mdblueprint-clean/runs/fair-division-integration-20260615/divisible-pack.json
  - /home/azureuser/mdblueprint-clean/runs/fair-division-integration-20260615/indivisible-pack.json
  - /home/azureuser/EconCSLib/docs/knowledge/nodes/social_choice/fair_division/divisible/cardinal_instance.md
  - /home/azureuser/EconCSLib/docs/knowledge/nodes/social_choice/fair_division/indivisible/cardinal_instance.md
  - /home/azureuser/EconCSLib/docs/knowledge/nodes/social_choice/fair_division/cardinal_instance_wrappers.md
summary: Fair-division wrappers exhibit missing specialization ancestry; propose bounded add-dependency edits to make the instance wrappers explicit without changing admitted truth.
baseline:
  check: not_run
  lint: findings
  stats: collected
formulation_impact:
  reviewed: true
  reason: The proposal adds explicit ancestry edges only; it does not weaken or delete downstream claims, but it should still be checked against wrapper semantics.
---

# Fair-Division Wrapper Proposal Report

## Scope

This report covers an admitted+staged fair-division slice of the EconCSLib
knowledge base. The review focuses on the wrapper-heavy cardinal-instance
family in:

- `social_choice.fair_division.cardinal_instance_wrappers`
- `social_choice.fair_division.divisible.cardinal_instance`
- `social_choice.fair_division.indivisible.cardinal_instance`
- the immediate allocation ancestors for the divisible and indivisible
  specializations

Staged nodes were included in the refactor packs, but the concrete proposals
below concern admitted nodes only.

## Deterministic Baseline

The bounded packs for the two specialization targets produced the following
signals:

- `social_choice.fair_division.divisible.cardinal_instance`
  - selected node count: `30`
  - direct dependencies:
    - `social_choice.fair_division.cardinal_instance`
    - `social_choice.fair_division.divisible.ordinal_instance`
    - `social_choice.fair_division.egalitarian_welfare`
    - `social_choice.fair_division.envy_free`
    - `social_choice.fair_division.proportional`
    - `social_choice.fair_division.utilitarian_welfare`
  - direct dependents:
    - `social_choice.fair_division.divisible.measure_instance`
  - formulation impact:
    - `review_recommended: true`
    - descendants through `measure_instance`
  - lint findings:
    - near-duplicate with `social_choice.fair_division.indivisible.cardinal_instance`
    - near-duplicate with `social_choice.fair_division.divisible.ordinal_instance`
    - near-duplicate with `social_choice.fair_division.divisible.allocation`
    - near-duplicate with `social_choice.fair_division.indivisible.allocation`

- `social_choice.fair_division.indivisible.cardinal_instance`
  - selected node count: `28`
  - direct dependencies:
    - `social_choice.fair_division.cardinal_instance`
    - `social_choice.fair_division.egalitarian_welfare`
    - `social_choice.fair_division.envy_free`
    - `social_choice.fair_division.indivisible.valuation`
    - `social_choice.fair_division.proportional`
    - `social_choice.fair_division.utilitarian_welfare`
  - direct dependents:
    - `social_choice.fair_division.indivisible.additive_instance`
  - formulation impact:
    - `review_recommended: true`
    - descendants through `additive_instance`
  - lint findings:
    - near-duplicate with `social_choice.fair_division.indivisible.ordinal_instance`
    - near-duplicate with `social_choice.fair_division.divisible.cardinal_instance`
    - near-duplicate with `social_choice.fair_division.indivisible.allocation`

The baseline also confirms that the wrapper umbrella node
`social_choice.fair_division.cardinal_instance_wrappers` is an admitted
definition node whose role is to package the shared wrapper API. That node is
not the direct refactor target in this run; it is a context anchor.

## Refinement Pass

The semantic proposals were ranked ahead of the duplicate-hygiene findings
because the wrapper ancestry is the higher-value graph improvement. The
duplicate findings were retained as evidence, but they were not promoted into
separate merge/split proposals because the current run is about explicit
ancestry, not canonicalization.

Important signals considered but not promoted:

| signal | targets | why_not_proposed | follow_up |
| --- | --- | --- | --- |
| `LINT_FUZZY_DUP` | `social_choice.fair_division.divisible.allocation`, `social_choice.fair_division.indivisible.allocation` | Likely expected sibling overlap; does not by itself justify a merge or split. | Revisit only if a later review finds actual content duplication rather than parallel specialization. |
| `LINT_FUZZY_DUP` | `social_choice.fair_division.divisible.cardinal_instance`, `social_choice.fair_division.indivisible.cardinal_instance` | The overlap is semantic and structural, but the intended fix here is ancestry clarity, not node collapse. | Consider a dedicated split/generalization review if the wrapper family becomes ambiguous. |
| `social_choice.fair_division.cardinal_instance_wrappers` | umbrella wrapper node | Already a context anchor; it is not the direct missing-ancestry problem. | Use as a reference node in future review passes. |

## Proposals

| proposal_id | kind | classification | targets | action | evidence | risk | validation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| refactor-001 | add-missing-dependency | semantic-review | `social_choice.fair_division.divisible.cardinal_instance` | Add `social_choice.fair_division.divisible.allocation` to the node's `uses` list so the specialized cardinal wrapper explicitly records its divisible allocation ancestor. | The node body is a divisible wrapper layer; the Lean module sits above `Divisible.Allocation` and `Divisible.IsAllocation`; the pack shows direct reachability through `measure_instance`, so the specialization chain is materially useful. | Overstating a conceptual rather than logical prerequisite if the allocation ancestor is meant to stay implicit. | Dry-run with `refactor_dry_run`; verify the added edge is accepted and does not create errors. |
| refactor-002 | add-missing-dependency | semantic-review | `social_choice.fair_division.indivisible.cardinal_instance` | Add `social_choice.fair_division.indivisible.allocation` to the node's `uses` list so the specialized cardinal wrapper explicitly records its indivisible allocation ancestor. | The node body is a wrapper around `Allocation N G`, `IsAllocation`, and the cardinal wrappers; the Lean module sits above `Indivisible.Basic`, and the current graph omits the allocation ancestor. | Same as above: the edge may be judged too explicit if the graph policy wants to keep this bridge implicit. | Dry-run with `refactor_dry_run`; verify the added edge is accepted and the output stays error-free. |

## Generality Gate

This run does not generalize, split, merge, or rehome mathematical content.
It only makes the existing specialization ancestry explicit by adding
allocation-wrapper dependencies to the relevant specialized cardinal-instance
nodes.

The current nodes already represent the intended level of abstraction for the
fair-division slice. The proposals therefore keep the current node granularity
and avoid any request-file workflow.

## Formulation-Sensitive Impact

The proposed edges are ancestry-only additions.

- `social_choice.fair_division.divisible.cardinal_instance`
  - descendant reviewed: `social_choice.fair_division.divisible.measure_instance`
  - effect of the change: no descendant theorem or definition is weakened;
    the proposal only makes the divisible allocation ancestor explicit
  - other ancestors that preserve the descendant claim: the generic
    `cardinal_instance`, fairness predicates, and measure-instance bridge
    already carry the actual mathematical content

- `social_choice.fair_division.indivisible.cardinal_instance`
  - descendant reviewed: `social_choice.fair_division.indivisible.additive_instance`
  - effect of the change: no descendant theorem or definition is weakened;
    the proposal only makes the indivisible allocation ancestor explicit
  - other ancestors that preserve the descendant claim: the generic
    `cardinal_instance`, fairness predicates, valuation bridge, and additive
    bridge already carry the actual mathematical content

Neither proposal deletes content or changes statement strength, so there is no
bridge/split/generalization request required here.

## Request Files

No request files are needed for this run. Both proposals only add explicit
dependencies to already-loaded admitted nodes, and no new node, split, merge,
or generalization request is being written.


## Human Decisions

The proposals are intentionally conservative. They do not attempt to merge the
divisible and indivisible wrappers even though the lint layer notices their
similarity. The intended improvement is to make the specialization chain more
explicit for reviewers and downstream graph consumers.

## Conclusion

This fair-division slice does produce actionable proposals, but they are
wrapper-ancestry proposals rather than graph-collapse proposals. The graph can
be made clearer by making the allocation specializations explicit in the
specialized cardinal-instance nodes.
