# Lean Node Generation Sample Study

Random sample of 20 EconCSLib nodes backed by Lean metadata:

- 10 / 20 sampled nodes were backed by exactly one Lean declaration.
- 18 / 20 sampled nodes had at least one exact Lean declaration match in the
  Lean index.
- 2 / 20 sampled nodes had a title that appeared verbatim in a Lean docstring.
- 1 / 20 sampled nodes had a title recoverable by simple leaf-name
  titleization.
- 0 / 20 sampled Lean files exposed explicit `Blueprint:` markers in the Lean
  index.

Representative cases:

- `social_choice.fair_division.divisible.proportional_exists`
- `social_choice.fair_division.indivisible.round_robin_alloc`
- `mechanism_design.auction.knapsack.relaxations_dynamic_programming`
- `game_theory.extensive_game.perfect_information.kuhn_spe_existence_no_chance`

Interpretation:

- Lean is enough to recover the formal spine of a node.
- Lean is not enough to recover the final editorial title, uses graph, or
  citation metadata.
- Some nodes are concept clusters rather than one-to-one declaration wrappers.
