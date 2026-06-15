---
agent: lean-countercheck
node_id: market_design.matching.one_to_one.lattice
created_at: "2026-06-15T12:50:28+00:00"
---

# Lean Countercheck: Lattice Structure of Stable Matchings (Conway-Knuth)

## Inputs

- node file: `/home/azureuser/EconCSLib/docs/knowledge/nodes/market_design/matching/one_to_one/lattice.md`
- lean file: `/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean`
- corpus root: `/home/azureuser/EconCSLib`

## Method Status

- heuristic: used

## Matched Declarations

- `GS.opposed_preferences`
- `GS.stableJoin_isStable`
- `GS.stableMeet_isStable`
- `GS.StableMatching`
- `GS.StableMatching.gsStable_isGreatest`

## Missing Declarations

- `(none)`

## Extra Declarations

- `wPartner_eq_iff`
- `joinWoman_eq_or`
- `joinWoman_mem_men`
- `joinWoman_worse_left`
- `joinWoman_worse_right`
- `joinWoman_injective`
- `prefM_strict`
- `prefW_strict`
- `joinWoman_le_left`
- `joinWoman_le_right`
- `opposed_preferences_women`
- `meetMan_eq_or`
- `meetMan_mem_women`
- `meetMan_worse_left`
- `meetMan_worse_right`
- `meetMan_injective`
- `meetMan_le_left`
- `meetMan_le_right`
- `wPartner_stableJoin`
- `wPartner_stableMeet`
- `meetEquiv_symm_eq_or`
- `stableMeet_ge_left`
- `stableMeet_ge_right`
- `matchW_partner`
- `gsStable_greatest`

## Node Uses vs Extracted Dependencies

- node uses: `market_design.matching.one_to_one.stability`, `market_design.matching.one_to_one.proposing_optimal`
- missing uses: `market_design.matching.one_to_one.stability`, `market_design.matching.one_to_one.proposing_optimal`
- extra uses: `StableMatching`, `gsStable_greatest`, `joinWoman_eq_or`, `joinWoman_injective`, `joinWoman_le_left`, `joinWoman_le_right`, `joinWoman_mem_men`, `joinWoman_worse_left`, `joinWoman_worse_right`, `matchW_partner`, `meetEquiv_symm_eq_or`, `meetMan_eq_or`, `meetMan_le_left`, `meetMan_le_right`, `meetMan_mem_women`, `meetMan_worse_left`, `meetMan_worse_right`, `opposed_preferences`, `opposed_preferences_women`, `prefM_strict`, `prefW_strict`, `stableJoin_isStable`, `stableMeet_ge_left`, `stableMeet_ge_right`, `stableMeet_isStable`, `wPartner_eq_iff`

## Raw Snapshot

```json
{
  "corpus_root": "/home/azureuser/EconCSLib",
  "dependencies": [
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "joinWoman_mem_men",
      "target": "joinWoman_eq_or"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "joinWoman_mem_men",
      "target": "wPartner_eq_iff"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "joinWoman_worse_left",
      "target": "opposed_preferences"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "joinWoman_worse_left",
      "target": "wPartner_eq_iff"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "joinWoman_worse_right",
      "target": "opposed_preferences"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "joinWoman_worse_right",
      "target": "wPartner_eq_iff"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "joinWoman_injective",
      "target": "joinWoman_worse_right"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "joinWoman_injective",
      "target": "joinWoman_worse_left"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "joinWoman_injective",
      "target": "joinWoman_mem_men"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "prefW_strict",
      "target": "joinWoman_injective"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "stableJoin_isStable",
      "target": "opposed_preferences"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "stableJoin_isStable",
      "target": "joinWoman_le_right"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "stableJoin_isStable",
      "target": "joinWoman_le_left"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "stableJoin_isStable",
      "target": "joinWoman_mem_men"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "stableJoin_isStable",
      "target": "prefM_strict"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "stableJoin_isStable",
      "target": "prefW_strict"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "meetMan_mem_women",
      "target": "wPartner_eq_iff"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "meetMan_mem_women",
      "target": "meetMan_eq_or"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "meetMan_worse_left",
      "target": "opposed_preferences_women"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "meetMan_worse_left",
      "target": "wPartner_eq_iff"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "meetMan_worse_right",
      "target": "opposed_preferences_women"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "meetMan_worse_right",
      "target": "wPartner_eq_iff"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "meetMan_injective",
      "target": "meetMan_worse_right"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "meetMan_injective",
      "target": "meetMan_worse_left"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "meetMan_injective",
      "target": "meetMan_mem_women"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "stableMeet_isStable",
      "target": "meetMan_mem_women"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "stableMeet_isStable",
      "target": "meetMan_le_right"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "stableMeet_isStable",
      "target": "meetMan_le_left"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "stableMeet_isStable",
      "target": "prefM_strict"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "stableMeet_isStable",
      "target": "prefW_strict"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "wPartner_stableJoin",
      "target": "stableJoin_isStable"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "wPartner_stableMeet",
      "target": "stableMeet_isStable"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "meetEquiv_symm_eq_or",
      "target": "meetMan_mem_women"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "stableMeet_ge_left",
      "target": "meetMan_worse_right"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "stableMeet_ge_left",
      "target": "meetMan_mem_women"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "stableMeet_ge_right",
      "target": "meetMan_worse_left"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "stableMeet_ge_right",
      "target": "meetMan_mem_women"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "matchW_partner",
      "target": "meetEquiv_symm_eq_or"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "matchW_partner",
      "target": "stableJoin_isStable"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "matchW_partner",
      "target": "stableMeet_ge_right"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "matchW_partner",
      "target": "stableMeet_isStable"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "matchW_partner",
      "target": "joinWoman_le_right"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "matchW_partner",
      "target": "stableMeet_ge_left"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "matchW_partner",
      "target": "joinWoman_le_left"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "matchW_partner",
      "target": "joinWoman_eq_or"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "matchW_partner",
      "target": "StableMatching"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "gsStable_greatest",
      "target": "StableMatching"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "gsStable_greatest",
      "target": "matchW_partner"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "gsStable_isGreatest",
      "target": "gsStable_greatest"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "source": "gsStable_isGreatest",
      "target": "StableMatching"
    }
  ],
  "lean_file": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
  "method_status": {
    "heuristic": "used"
  },
  "node": {
    "body": "# Lattice of Stable Matchings\n\n**Theorem (Conway, reported by Knuth 1976).** The set of stable matchings\nof any finite one-to-one matching market forms a **complete distributive\nlattice** under the partial order\n\n$$\\mu \\le_M \\mu' \\quad \\iff \\quad \\mu(i) \\preceq_i \\mu'(i) \\text{ for all } i \\in M$$\n\n(\"men weakly prefer $\\mu'$ to $\\mu$\"). The join $\\mu \\vee \\mu'$ matches each\nman to his preferred of the two partners; the meet $\\mu \\wedge \\mu'$ matches\neach man to his less-preferred. Both are stable matchings.\n\nEquivalently, under $\\le_W$ defined dually (women's preference), the lattice\nis the order-dual.\n\n## Extrema\n\n- Top under $\\le_M$: the **men-optimal** matching $\\mu^M$ (output of\n  men-proposing GS \u2014 see [[proposing_optimal]]).\n- Bottom under $\\le_M$: the **women-optimal** matching $\\mu^W$ (output of\n  women-proposing GS).\n\nThese two are also the bottom and top respectively under $\\le_W$ \u2014 the men's\nand women's interests are exactly opposed across the stable set.\n\n## Proof Sketch\n\nThe non-trivial part is showing $\\mu \\vee \\mu'$ (each man picks his preferred\npartner from $\\mu$ and $\\mu'$) is itself a matching (not just a function) and\nis stable.\n\n*Matching*: We must show no woman is \"picked\" by two different men. If man\n$i_1$'s preferred partner is $j$, and $i_2$'s preferred is also $j$, then $j$\nis matched to $i_1$ in one of $\\mu, \\mu'$ and to $i_2$ in the other. By the\nopposed-preferences phenomenon (a corollary of stability), $j$ also prefers\nexactly the opposite \u2014 contradiction.\n\n*Stability*: If $(i, k)$ blocks $\\mu \\vee \\mu'$, then $k$ ranks higher on\n$i$'s list than his max of $\\mu(i), \\mu'(i)$, so $(i, k)$ blocks both $\\mu$\nand $\\mu'$ \u2014 contradicting stability of either.\n\nDistributivity follows from the same opposed-preferences structure.\n\n## Formalization\n\nIn the balanced full-preference Lean model (`Preferences n` via\n`MatchingMarket.ofEquivData`, every stable matching perfect), the lattice\nstructure is formalized as a `Lattice` instance on\n`GS.StableMatching w m` (`EconCSLib.MarketDesign.Matching.Lattice`):\n\n- `GS.opposed_preferences` (+ `opposed_preferences_women`) \u2014 the\n  opposed-preferences lemma, proved by a direct pairwise blocking argument.\n- `GS.stableJoin` / `GS.stableMeet` \u2014 the join and meet as `Matching`s, each\n  built from an injective-hence-bijective partner map (`joinWoman` /\n  `meetMan`); the injectivity is the \"no woman picked twice\" step and uses\n  `opposed_preferences`.\n- `GS.stableJoin_isStable` / `GS.stableMeet_isStable` \u2014 both operations are\n  closed within the stable set.\n- The `Lattice (GS.StableMatching w m)` instance \u2014 the men-preference order\n  (`\u03c3 \u2264 \u03c4` iff every man weakly prefers `\u03c4`) with `\u2294 = stableJoin`,\n  `\u2293 = stableMeet`, all lattice axioms discharged.\n- `GS.StableMatching.gsStable_isGreatest` \u2014 the **men-proposing GS output is\n  the greatest element** ($\\top$) of this lattice: every man weakly prefers\n  it to his partner in any other stable matching. This is\n  [[proposing_optimal]] (`galeShapley_isProposingOptimal`) packaged as the\n  lattice maximum, identifying the men-optimal extremum $\\mu^M$ with the GS\n  output.\n\nAll sorry-free (axioms: `propext`, `Classical.choice`, `Quot.sound`).\n\n**Not yet formalized** (classical, future refinements): *distributivity* of\nthe lattice, *completeness*, and the *women-proposing* bottom extremum\n$\\mu^W$ (no women-proposing GS is formalized yet). The general\n$\\bot$/unequal-cardinality version is also out of scope of the balanced model.\n\n## Consequences\n\n- The number of stable matchings is bounded by combinatorial counts on the\n  lattice (e.g., chain lengths, antichains).\n- The Conway-Knuth lattice is the foundation for the [[rural_hospitals]]\n  invariant (\"same set of matched participants across all stable matchings\").\n\n## References\n\n- [MSZ Ch.22, Thm 22.12] Maschler, Solan, Zamir, *Game Theory*.\n- Knuth (1976), *Marriages Stables*. Universit\u00e9 de Montr\u00e9al.\n- Roth & Sotomayor (1990), Ch. 2 \u00a72.3.",
    "file_path": "/home/azureuser/EconCSLib/docs/knowledge/nodes/market_design/matching/one_to_one/lattice.md",
    "id": "market_design.matching.one_to_one.lattice",
    "kind": "theorem",
    "lean": {
      "declarations": [
        "GS.opposed_preferences",
        "GS.stableJoin_isStable",
        "GS.stableMeet_isStable",
        "GS.StableMatching",
        "GS.StableMatching.gsStable_isGreatest"
      ],
      "modules": [
        "EconCSLib.MarketDesign.Matching.Lattice"
      ],
      "repository": null
    },
    "status": "proved",
    "tags": [
      "matching",
      "lattice",
      "stable-set"
    ],
    "title": "Lattice Structure of Stable Matchings (Conway-Knuth)",
    "uses": [
      "market_design.matching.one_to_one.stability",
      "market_design.matching.one_to_one.proposing_optimal"
    ]
  },
  "source_root": "/home/azureuser/EconCSLib",
  "theorems": [
    {
      "body": "theorem opposed_preferences\n    (\u03bc : Matching (Fin n) (Fin n))\n    (h\u03bc : Matching.IsStable (MatchingMarket.ofEquivData w m) \u03bc)\n    {j wj wj' m' : Fin n}\n    (h\u03bc_j : \u03bc.matchW j = some wj')\n    (hpref : (m.prefs j).idxOf wj < (m.prefs j).idxOf wj')\n    (h\u03bc_w : \u03bc.matchM wj = some m') :\n    (w.prefs wj).idxOf m' < (w.prefs wj).idxOf j := by\n  -- `wj \u2260 wj'` since `j` strictly prefers `wj` over `wj'`.\n  have hwj_ne : wj \u2260 wj' := by\n    intro he; rw [he] at hpref; exact (lt_irrefl _ hpref)\n  -- `j \u2260 m'`: else `\u03bc` would match `wj` to `j`, contradicting `\u03bc.matchW j = some wj'`.\n  have hj_ne : j \u2260 m' := by\n    intro he; subst he\n    have : \u03bc.matchW j = some wj := (\u03bc.consistent wj j).mp h\u03bc_w\n    rw [h\u03bc_j] at this\n    exact hwj_ne (Option.some.inj this).symm\n  -- Suppose `wj` does NOT strictly prefer `m'` to `j`; derive a blocking pair.\n  by_contra hle\n  push_neg at hle  -- (w.prefs wj).idxOf j \u2264 (w.prefs wj).idxOf m'\n  -- `wj` then strictly prefers `j` to `m'` (strictness from `j \u2260 m'`).\n  have hlt : (w.prefs wj).idxOf j < (w.prefs wj).idxOf m' := by\n    refine lt_of_le_of_ne hle (fun e => hj_ne ?_)\n    exact (List.idxOf_inj (pref_list_mem _ (w.valid wj).1 (w.valid wj).2 j)).mp e\n  -- `(wj, j)` blocks `\u03bc`.\n  exact h\u03bc wj j\n    \u27e8by rw [h\u03bc_w]; exact \u27e8by show (w.prefs wj).idxOf j \u2264 (w.prefs wj).idxOf m'; omega,\n                          by show \u00ac (w.prefs wj).idxOf m' \u2264 (w.prefs wj).idxOf j; omega\u27e9,\n     by rw [h\u03bc_j]; exact \u27e8by show (m.prefs j).idxOf wj \u2264 (m.prefs j).idxOf wj'; omega,\n                          by show \u00ac (m.prefs j).idxOf wj' \u2264 (m.prefs j).idxOf wj; omega\u27e9\u27e9\n\n/-! ### Partner extraction (stable \u21d2 perfect) -/\n\nvariable {w m}\n\n/-- The woman partnered to man `j` under a stable matching `\u03bc` (total, since a\nstable matching of the balanced market is perfect). -/\nnoncomputable def wPartner (\u03bc : Matching (Fin n) (Fin n))\n    (h\u03bc : Matching.IsStable (MatchingMarket.ofEquivData w m) \u03bc) (j : Fin n) : Fin n :=\n  (\u03bc.matchW j).get ((stable_matching_perfect w m \u03bc h\u03bc).2 j)\n\n/-- The man partnered to woman `i` under a stable matching `\u03bc`. -/\nnoncomputable def mPartner (\u03bc : Matching (Fin n) (Fin n))\n    (h\u03bc : Matching.IsStable (MatchingMarket.ofEquivData w m) \u03bc) (i : Fin n) : Fin n :=\n  (\u03bc.matchM i).get ((stable_matching_perfect w m \u03bc h\u03bc).1 i)\n\n@[simp] lemma matchW_wPartner (\u03bc : Matching (Fin n) (Fin n))\n    (h\u03bc : Matching.IsStable (MatchingMarket.ofEquivData w m) \u03bc) (j : Fin n) :\n    \u03bc.matchW j = some (wPartner \u03bc h\u03bc j) := (Option.some_get _).symm\n\n@[simp] lemma matchM_mPartner (\u03bc : Matching (Fin n) (Fin n))\n    (h\u03bc : Matching.IsStable (MatchingMarket.ofEquivData w m) \u03bc) (i : Fin n) :\n    \u03bc.matchM i = some (mPartner \u03bc h\u03bc i) := (Option.some_get _).symm\n\n/-- The man-of and woman-of partner maps are inverse to each other. -/\n",
      "column": 1,
      "end": 4521,
      "kind": "theorem",
      "line": 47,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "opposed_preferences",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 1769
    },
    {
      "body": "lemma wPartner_eq_iff (\u03bc : Matching (Fin n) (Fin n))\n    (h\u03bc : Matching.IsStable (MatchingMarket.ofEquivData w m) \u03bc) {i j : Fin n} :\n    wPartner \u03bc h\u03bc j = i \u2194 mPartner \u03bc h\u03bc i = j := by\n  constructor\n  \u00b7 intro h\n    have h1 : \u03bc.matchW j = some i := by rw [matchW_wPartner \u03bc h\u03bc j, h]\n    have h2 : \u03bc.matchM i = some j := (\u03bc.consistent i j).mpr h1\n    rw [matchM_mPartner \u03bc h\u03bc i] at h2\n    exact Option.some.inj h2\n  \u00b7 intro h\n    have h1 : \u03bc.matchM i = some j := by rw [matchM_mPartner \u03bc h\u03bc i, h]\n    have h2 : \u03bc.matchW j = some i := (\u03bc.consistent i j).mp h1\n    rw [matchW_wPartner \u03bc h\u03bc j] at h2\n    exact Option.some.inj h2\n\n/-! ### The join (man-optimal of two) and its injectivity -/\n\nvariable (\u03bc \u03bd : Matching (Fin n) (Fin n))\n  (h\u03bc : Matching.IsStable (MatchingMarket.ofEquivData w m) \u03bc)\n  (h\u03bd : Matching.IsStable (MatchingMarket.ofEquivData w m) \u03bd)\n\n/-- Man `j`'s more-preferred partner across stable matchings `\u03bc` and `\u03bd`. -/\nnoncomputable def joinWoman (j : Fin n) : Fin n :=\n  if (m.prefs j).idxOf (wPartner \u03bc h\u03bc j) \u2264 (m.prefs j).idxOf (wPartner \u03bd h\u03bd j)\n  then wPartner \u03bc h\u03bc j else wPartner \u03bd h\u03bd j\n\n",
      "column": 1,
      "end": 5627,
      "kind": "theorem",
      "line": 102,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "wPartner_eq_iff",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 4521
    },
    {
      "body": "lemma joinWoman_eq_or (j : Fin n) :\n    joinWoman \u03bc \u03bd h\u03bc h\u03bd j = wPartner \u03bc h\u03bc j \u2228 joinWoman \u03bc \u03bd h\u03bc h\u03bd j = wPartner \u03bd h\u03bd j := by\n  unfold joinWoman; split_ifs with h\n  \u00b7 exact Or.inl rfl\n  \u00b7 exact Or.inr rfl\n\n/-- If `i` is man `j`'s join-partner then `j` is one of `i`'s two men. -/\n",
      "column": 1,
      "end": 5909,
      "kind": "theorem",
      "line": 128,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "joinWoman_eq_or",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 5627
    },
    {
      "body": "lemma joinWoman_mem_men {j i : Fin n} (h : joinWoman \u03bc \u03bd h\u03bc h\u03bd j = i) :\n    mPartner \u03bc h\u03bc i = j \u2228 mPartner \u03bd h\u03bd i = j := by\n  rcases joinWoman_eq_or \u03bc \u03bd h\u03bc h\u03bd j with he | he\n  \u00b7 exact Or.inl ((wPartner_eq_iff \u03bc h\u03bc).mp (he \u25b8 h))\n  \u00b7 exact Or.inr ((wPartner_eq_iff \u03bd h\u03bd).mp (he \u25b8 h))\n\n/-- If `i` is the join-partner of her `\u03bc`-man `j`, then `i` weakly prefers her\n`\u03bd`-man to `j` (so `j` is her worse man). -/\n",
      "column": 1,
      "end": 6316,
      "kind": "theorem",
      "line": 135,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "joinWoman_mem_men",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 5909
    },
    {
      "body": "lemma joinWoman_worse_left {j i : Fin n}\n    (hji : joinWoman \u03bc \u03bd h\u03bc h\u03bd j = i) (h\u03bcji : mPartner \u03bc h\u03bc i = j) :\n    (w.prefs i).idxOf (mPartner \u03bd h\u03bd i) \u2264 (w.prefs i).idxOf j := by\n  have h\u03bcw : wPartner \u03bc h\u03bc j = i := (wPartner_eq_iff \u03bc h\u03bc).mpr h\u03bcji\n  by_cases heq : wPartner \u03bd h\u03bd j = i\n  \u00b7 -- `i` is also `j`'s \u03bd-woman, so `mPartner \u03bd i = j`.\n    have : mPartner \u03bd h\u03bd i = j := (wPartner_eq_iff \u03bd h\u03bd).mp heq\n    rw [this]\n  \u00b7 -- `j` strictly prefers `i` (his \u03bc-woman) over his \u03bd-woman; opposed prefs.\n    have hbranch : joinWoman \u03bc \u03bd h\u03bc h\u03bd j = wPartner \u03bc h\u03bc j := by rw [hji, h\u03bcw]\n    have hle : (m.prefs j).idxOf (wPartner \u03bc h\u03bc j) \u2264 (m.prefs j).idxOf (wPartner \u03bd h\u03bd j) := by\n      by_contra hgt\n      unfold joinWoman at hbranch\n      rw [if_neg hgt] at hbranch\n      exact heq (hbranch.trans h\u03bcw)\n    rw [h\u03bcw] at hle\n    have hlt : (m.prefs j).idxOf i < (m.prefs j).idxOf (wPartner \u03bd h\u03bd j) := by\n      refine lt_of_le_of_ne hle (fun e => heq ?_)\n      exact ((List.idxOf_inj (pref_list_mem _ (m.valid j).1 (m.valid j).2 i)).mp e).symm\n    have := opposed_preferences w m \u03bd h\u03bd (wj := i) (wj' := wPartner \u03bd h\u03bd j)\n      (m' := mPartner \u03bd h\u03bd i) (matchW_wPartner \u03bd h\u03bd j) hlt (matchM_mPartner \u03bd h\u03bd i)\n    omega\n\n/-- Dual of `joinWoman_worse_left` with the roles of `\u03bc`, `\u03bd` swapped. -/\n",
      "column": 1,
      "end": 7593,
      "kind": "theorem",
      "line": 143,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "joinWoman_worse_left",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 6316
    },
    {
      "body": "lemma joinWoman_worse_right {j i : Fin n}\n    (hji : joinWoman \u03bc \u03bd h\u03bc h\u03bd j = i) (h\u03bdji : mPartner \u03bd h\u03bd i = j) :\n    (w.prefs i).idxOf (mPartner \u03bc h\u03bc i) \u2264 (w.prefs i).idxOf j := by\n  have h\u03bdw : wPartner \u03bd h\u03bd j = i := (wPartner_eq_iff \u03bd h\u03bd).mpr h\u03bdji\n  by_cases heq : wPartner \u03bc h\u03bc j = i\n  \u00b7 have : mPartner \u03bc h\u03bc i = j := (wPartner_eq_iff \u03bc h\u03bc).mp heq\n    rw [this]\n  \u00b7 have hbranch : joinWoman \u03bc \u03bd h\u03bc h\u03bd j = wPartner \u03bd h\u03bd j := by rw [hji, h\u03bdw]\n    have hlt0 : (m.prefs j).idxOf (wPartner \u03bd h\u03bd j) < (m.prefs j).idxOf (wPartner \u03bc h\u03bc j) := by\n      by_contra hge\n      push_neg at hge\n      unfold joinWoman at hbranch\n      rw [if_pos hge] at hbranch\n      exact heq (hbranch.trans h\u03bdw)\n    rw [h\u03bdw] at hlt0\n    have hlt : (m.prefs j).idxOf i < (m.prefs j).idxOf (wPartner \u03bc h\u03bc j) := hlt0\n    have := opposed_preferences w m \u03bc h\u03bc (wj := i) (wj' := wPartner \u03bc h\u03bc j)\n      (m' := mPartner \u03bc h\u03bc i) (matchW_wPartner \u03bc h\u03bc j) hlt (matchM_mPartner \u03bc h\u03bc i)\n    omega\n\n/-- The join woman-assignment is injective. -/\n",
      "column": 1,
      "end": 8595,
      "kind": "theorem",
      "line": 167,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "joinWoman_worse_right",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 7593
    },
    {
      "body": "lemma joinWoman_injective : Function.Injective (joinWoman \u03bc \u03bd h\u03bc h\u03bd) := by\n  intro j1 j2 he\n  set i := joinWoman \u03bc \u03bd h\u03bc h\u03bd j1 with hidef\n  have h1 : joinWoman \u03bc \u03bd h\u03bc h\u03bd j1 = i := hidef.symm\n  have h2 : joinWoman \u03bc \u03bd h\u03bc h\u03bd j2 = i := he.symm.trans hidef.symm\n  rcases joinWoman_mem_men \u03bc \u03bd h\u03bc h\u03bd h1 with hm1 | hn1 <;>\n    rcases joinWoman_mem_men \u03bc \u03bd h\u03bc h\u03bd h2 with hm2 | hn2\n  \u00b7 exact hm1.symm.trans hm2          -- both \u03bc-men of i\n  \u00b7 -- j1 = \u03bc-man, j2 = \u03bd-man\n    have a := joinWoman_worse_left \u03bc \u03bd h\u03bc h\u03bd h1 hm1   -- idxOf (mPartner \u03bd i) \u2264 idxOf j1\n    have b := joinWoman_worse_right \u03bc \u03bd h\u03bc h\u03bd h2 hn2  -- idxOf (mPartner \u03bc i) \u2264 idxOf j2\n    rw [hn2] at a; rw [hm1] at b\n    exact (List.idxOf_inj (pref_list_mem _ (w.valid i).1 (w.valid i).2 j1)).mp\n      (le_antisymm b a)\n  \u00b7 -- j1 = \u03bd-man, j2 = \u03bc-man\n    have a := joinWoman_worse_right \u03bc \u03bd h\u03bc h\u03bd h1 hn1  -- idxOf (mPartner \u03bc i) \u2264 idxOf j1\n    have b := joinWoman_worse_left \u03bc \u03bd h\u03bc h\u03bd h2 hm2   -- idxOf (mPartner \u03bd i) \u2264 idxOf j2\n    rw [hm2] at a; rw [hn1] at b\n    exact (List.idxOf_inj (pref_list_mem _ (w.valid i).1 (w.valid i).2 j1)).mp\n      (le_antisymm b a)\n  \u00b7 exact hn1.symm.trans hn2          -- both \u03bd-men of i\n\n/-! ### Strict-preference reductions for the `ofEquivData` market -/\n\n",
      "column": 1,
      "end": 9841,
      "kind": "theorem",
      "line": 188,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "joinWoman_injective",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 8595
    },
    {
      "body": "lemma prefM_strict {i a b : Fin n} :\n    strict ((MatchingMarket.ofEquivData w m).prefM i).rel (some a) (some b) \u2194\n      (w.prefs i).idxOf a < (w.prefs i).idxOf b := by\n  constructor\n  \u00b7 rintro \u27e8h1, h2\u27e9\n    have e1 : (w.prefs i).idxOf a \u2264 (w.prefs i).idxOf b := h1\n    have e2 : \u00ac (w.prefs i).idxOf b \u2264 (w.prefs i).idxOf a := h2\n    omega\n  \u00b7 intro h\n    exact \u27e8show (w.prefs i).idxOf a \u2264 (w.prefs i).idxOf b by omega,\n           show \u00ac (w.prefs i).idxOf b \u2264 (w.prefs i).idxOf a by omega\u27e9\n\n",
      "column": 1,
      "end": 10331,
      "kind": "theorem",
      "line": 212,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "prefM_strict",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 9841
    },
    {
      "body": "lemma prefW_strict {j a b : Fin n} :\n    strict ((MatchingMarket.ofEquivData w m).prefW j).rel (some a) (some b) \u2194\n      (m.prefs j).idxOf a < (m.prefs j).idxOf b := by\n  constructor\n  \u00b7 rintro \u27e8h1, h2\u27e9\n    have e1 : (m.prefs j).idxOf a \u2264 (m.prefs j).idxOf b := h1\n    have e2 : \u00ac (m.prefs j).idxOf b \u2264 (m.prefs j).idxOf a := h2\n    omega\n  \u00b7 intro h\n    exact \u27e8show (m.prefs j).idxOf a \u2264 (m.prefs j).idxOf b by omega,\n           show \u00ac (m.prefs j).idxOf b \u2264 (m.prefs j).idxOf a by omega\u27e9\n\n/-! ### The join as a stable matching -/\n\n/-- The join woman-assignment packaged as an equivalence (injective on the\nfinite `Fin n`, hence bijective). -/\nnoncomputable def joinEquiv : Fin n \u2243 Fin n :=\n  Equiv.ofBijective (joinWoman \u03bc \u03bd h\u03bc h\u03bd)\n    (Finite.injective_iff_bijective.mp (joinWoman_injective \u03bc \u03bd h\u03bc h\u03bd))\n\n/-- The **join** `\u03bc \u2228 \u03bd`: each man keeps his more-preferred of the two\npartners; each woman keeps her less-preferred man. -/\nnoncomputable def stableJoin : Matching (Fin n) (Fin n) where\n  matchM i := some ((joinEquiv \u03bc \u03bd h\u03bc h\u03bd).symm i)\n  matchW j := some (joinWoman \u03bc \u03bd h\u03bc h\u03bd j)\n  consistent := by\n    intro i j\n    simp only [Option.some.injEq]\n    rw [Equiv.symm_apply_eq]\n    exact eq_comm\n\n@[simp] lemma stableJoin_matchW (j : Fin n) :\n    (stableJoin \u03bc \u03bd h\u03bc h\u03bd).matchW j = some (joinWoman \u03bc \u03bd h\u03bc h\u03bd j) := rfl\n\n@[simp] lemma stableJoin_matchM (i : Fin n) :\n    (stableJoin \u03bc \u03bd h\u03bc h\u03bd).matchM i = some ((joinEquiv \u03bc \u03bd h\u03bc h\u03bd).symm i) := rfl\n\n",
      "column": 1,
      "end": 11781,
      "kind": "theorem",
      "line": 224,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "prefW_strict",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 10331
    },
    {
      "body": "lemma joinWoman_le_left (j : Fin n) :\n    (m.prefs j).idxOf (joinWoman \u03bc \u03bd h\u03bc h\u03bd j) \u2264 (m.prefs j).idxOf (wPartner \u03bc h\u03bc j) := by\n  unfold joinWoman; split_ifs with h\n  \u00b7 exact le_refl _\n  \u00b7 push_neg at h; omega\n\n",
      "column": 1,
      "end": 11992,
      "kind": "theorem",
      "line": 261,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "joinWoman_le_left",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 11781
    },
    {
      "body": "lemma joinWoman_le_right (j : Fin n) :\n    (m.prefs j).idxOf (joinWoman \u03bc \u03bd h\u03bc h\u03bd j) \u2264 (m.prefs j).idxOf (wPartner \u03bd h\u03bd j) := by\n  unfold joinWoman; split_ifs with h\n  \u00b7 exact h\n  \u00b7 exact le_refl _\n\n/-- The join of two stable matchings is stable. -/\n",
      "column": 1,
      "end": 12242,
      "kind": "theorem",
      "line": 267,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "joinWoman_le_right",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 11992
    },
    {
      "body": "theorem stableJoin_isStable :\n    Matching.IsStable (MatchingMarket.ofEquivData w m) (stableJoin \u03bc \u03bd h\u03bc h\u03bd) := by\n  intro i j hblock\n  obtain \u27e8hi, hj\u27e9 := hblock\n  rw [stableJoin_matchM] at hi\n  rw [stableJoin_matchW] at hj\n  set jm := (joinEquiv \u03bc \u03bd h\u03bc h\u03bd).symm i with hjmdef\n  have hi' : (w.prefs i).idxOf j < (w.prefs i).idxOf jm := prefM_strict.mp hi\n  have hj' : (m.prefs j).idxOf i < (m.prefs j).idxOf (joinWoman \u03bc \u03bd h\u03bc h\u03bd j) := prefW_strict.mp hj\n  have hjoin_jm : joinWoman \u03bc \u03bd h\u03bc h\u03bd jm = i := (joinEquiv \u03bc \u03bd h\u03bc h\u03bd).apply_symm_apply i\n  rcases joinWoman_mem_men \u03bc \u03bd h\u03bc h\u03bd hjoin_jm with hm | hn\n  \u00b7 -- `jm` is `i`'s `\u03bc`-man, so `(i, j)` blocks `\u03bc`.\n    refine h\u03bc i j \u27e8?_, ?_\u27e9\n    \u00b7 rw [matchM_mPartner \u03bc h\u03bc i, hm]; exact prefM_strict.mpr hi'\n    \u00b7 rw [matchW_wPartner \u03bc h\u03bc j]\n      exact prefW_strict.mpr (lt_of_lt_of_le hj' (joinWoman_le_left \u03bc \u03bd h\u03bc h\u03bd j))\n  \u00b7 -- `jm` is `i`'s `\u03bd`-man, so `(i, j)` blocks `\u03bd`.\n    refine h\u03bd i j \u27e8?_, ?_\u27e9\n    \u00b7 rw [matchM_mPartner \u03bd h\u03bd i, hn]; exact prefM_strict.mpr hi'\n    \u00b7 rw [matchW_wPartner \u03bd h\u03bd j]\n      exact prefW_strict.mpr (lt_of_lt_of_le hj' (joinWoman_le_right \u03bc \u03bd h\u03bc h\u03bd j))\n\n/-! ### The meet (man-pessimal of two), dual to the join\n\nThe meet `\u03bc \u2227 \u03bd` gives every man his *worse* of the two partners, equivalently\nevery woman her *better* of the two men. We mirror the join construction over\nwomen: `meetMan` (each woman's preferred man) is the relevant bijection. -/\n\n/-- Dual of `opposed_preferences`: if woman `i` strictly prefers man `mi` to her\n`candidate`-man `mi'`, then `mi` strictly prefers his `candidate`-woman to `i`. -/\n",
      "column": 1,
      "end": 13827,
      "kind": "theorem",
      "line": 274,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "stableJoin_isStable",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 12242
    },
    {
      "body": "theorem opposed_preferences_women\n    (candidate : Matching (Fin n) (Fin n))\n    (hcandidate : Matching.IsStable (MatchingMarket.ofEquivData w m) candidate)\n    {i mi mi' j' : Fin n}\n    (hcandidate_i : candidate.matchM i = some mi')\n    (hpref : (w.prefs i).idxOf mi < (w.prefs i).idxOf mi')\n    (hcandidate_m : candidate.matchW mi = some j') :\n    (m.prefs mi).idxOf j' < (m.prefs mi).idxOf i := by\n  have hmi_ne : mi \u2260 mi' := by\n    intro he; rw [he] at hpref; exact (lt_irrefl _ hpref)\n  have hi_ne : i \u2260 j' := by\n    intro he; subst he\n    have : candidate.matchM i = some mi := (candidate.consistent i mi).mpr hcandidate_m\n    rw [hcandidate_i] at this\n    exact hmi_ne (Option.some.inj this).symm\n  by_contra hle\n  push_neg at hle\n  have hlt : (m.prefs mi).idxOf i < (m.prefs mi).idxOf j' := by\n    refine lt_of_le_of_ne hle (fun e => hi_ne ?_)\n    exact (List.idxOf_inj (pref_list_mem _ (m.valid mi).1 (m.valid mi).2 i)).mp e\n  exact hcandidate i mi\n    \u27e8by rw [hcandidate_i]; exact \u27e8by show (w.prefs i).idxOf mi \u2264 (w.prefs i).idxOf mi'; omega,\n                          by show \u00ac (w.prefs i).idxOf mi' \u2264 (w.prefs i).idxOf mi; omega\u27e9,\n     by rw [hcandidate_m]; exact \u27e8by show (m.prefs mi).idxOf i \u2264 (m.prefs mi).idxOf j'; omega,\n                          by show \u00ac (m.prefs mi).idxOf j' \u2264 (m.prefs mi).idxOf i; omega\u27e9\u27e9\n\n/-- Woman `i`'s more-preferred man across `\u03bc` and `\u03bd`. -/\nnoncomputable def meetMan (i : Fin n) : Fin n :=\n  if (w.prefs i).idxOf (mPartner \u03bc h\u03bc i) \u2264 (w.prefs i).idxOf (mPartner \u03bd h\u03bd i)\n  then mPartner \u03bc h\u03bc i else mPartner \u03bd h\u03bd i\n\n",
      "column": 1,
      "end": 15387,
      "kind": "theorem",
      "line": 304,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "opposed_preferences_women",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 13827
    },
    {
      "body": "lemma meetMan_eq_or (i : Fin n) :\n    meetMan \u03bc \u03bd h\u03bc h\u03bd i = mPartner \u03bc h\u03bc i \u2228 meetMan \u03bc \u03bd h\u03bc h\u03bd i = mPartner \u03bd h\u03bd i := by\n  unfold meetMan; split_ifs with h\n  \u00b7 exact Or.inl rfl\n  \u00b7 exact Or.inr rfl\n\n",
      "column": 1,
      "end": 15587,
      "kind": "theorem",
      "line": 335,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "meetMan_eq_or",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 15387
    },
    {
      "body": "lemma meetMan_mem_women {i j : Fin n} (h : meetMan \u03bc \u03bd h\u03bc h\u03bd i = j) :\n    wPartner \u03bc h\u03bc j = i \u2228 wPartner \u03bd h\u03bd j = i := by\n  rcases meetMan_eq_or \u03bc \u03bd h\u03bc h\u03bd i with he | he\n  \u00b7 exact Or.inl ((wPartner_eq_iff \u03bc h\u03bc).mpr (he \u25b8 h))\n  \u00b7 exact Or.inr ((wPartner_eq_iff \u03bd h\u03bd).mpr (he \u25b8 h))\n\n",
      "column": 1,
      "end": 15868,
      "kind": "theorem",
      "line": 341,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "meetMan_mem_women",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 15587
    },
    {
      "body": "lemma meetMan_worse_left {i j : Fin n}\n    (hij : meetMan \u03bc \u03bd h\u03bc h\u03bd i = j) (h\u03bcij : wPartner \u03bc h\u03bc j = i) :\n    (m.prefs j).idxOf (wPartner \u03bd h\u03bd j) \u2264 (m.prefs j).idxOf i := by\n  have h\u03bcm : mPartner \u03bc h\u03bc i = j := (wPartner_eq_iff \u03bc h\u03bc).mp h\u03bcij\n  by_cases heq : mPartner \u03bd h\u03bd i = j\n  \u00b7 have : wPartner \u03bd h\u03bd j = i := (wPartner_eq_iff \u03bd h\u03bd).mpr heq\n    rw [this]\n  \u00b7 have hbranch : meetMan \u03bc \u03bd h\u03bc h\u03bd i = mPartner \u03bc h\u03bc i := by rw [hij, h\u03bcm]\n    have hle : (w.prefs i).idxOf (mPartner \u03bc h\u03bc i) \u2264 (w.prefs i).idxOf (mPartner \u03bd h\u03bd i) := by\n      by_contra hgt\n      unfold meetMan at hbranch\n      rw [if_neg hgt] at hbranch\n      exact heq (hbranch.trans h\u03bcm)\n    rw [h\u03bcm] at hle\n    have hlt : (w.prefs i).idxOf j < (w.prefs i).idxOf (mPartner \u03bd h\u03bd i) := by\n      refine lt_of_le_of_ne hle (fun e => heq ?_)\n      exact ((List.idxOf_inj (pref_list_mem _ (w.valid i).1 (w.valid i).2 j)).mp e).symm\n    have := opposed_preferences_women \u03bd h\u03bd (mi := j) (mi' := mPartner \u03bd h\u03bd i)\n      (j' := wPartner \u03bd h\u03bd j) (matchM_mPartner \u03bd h\u03bd i) hlt (matchW_wPartner \u03bd h\u03bd j)\n    omega\n\n",
      "column": 1,
      "end": 16929,
      "kind": "theorem",
      "line": 347,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "meetMan_worse_left",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 15868
    },
    {
      "body": "lemma meetMan_worse_right {i j : Fin n}\n    (hij : meetMan \u03bc \u03bd h\u03bc h\u03bd i = j) (h\u03bdij : wPartner \u03bd h\u03bd j = i) :\n    (m.prefs j).idxOf (wPartner \u03bc h\u03bc j) \u2264 (m.prefs j).idxOf i := by\n  have h\u03bdm : mPartner \u03bd h\u03bd i = j := (wPartner_eq_iff \u03bd h\u03bd).mp h\u03bdij\n  by_cases heq : mPartner \u03bc h\u03bc i = j\n  \u00b7 have : wPartner \u03bc h\u03bc j = i := (wPartner_eq_iff \u03bc h\u03bc).mpr heq\n    rw [this]\n  \u00b7 have hbranch : meetMan \u03bc \u03bd h\u03bc h\u03bd i = mPartner \u03bd h\u03bd i := by rw [hij, h\u03bdm]\n    have hlt0 : (w.prefs i).idxOf (mPartner \u03bd h\u03bd i) < (w.prefs i).idxOf (mPartner \u03bc h\u03bc i) := by\n      by_contra hge\n      push_neg at hge\n      unfold meetMan at hbranch\n      rw [if_pos hge] at hbranch\n      exact heq (hbranch.trans h\u03bdm)\n    rw [h\u03bdm] at hlt0\n    have hlt : (w.prefs i).idxOf j < (w.prefs i).idxOf (mPartner \u03bc h\u03bc i) := hlt0\n    have := opposed_preferences_women \u03bc h\u03bc (mi := j) (mi' := mPartner \u03bc h\u03bc i)\n      (j' := wPartner \u03bc h\u03bc j) (matchM_mPartner \u03bc h\u03bc i) hlt (matchW_wPartner \u03bc h\u03bc j)\n    omega\n\n",
      "column": 1,
      "end": 17878,
      "kind": "theorem",
      "line": 368,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "meetMan_worse_right",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 16929
    },
    {
      "body": "lemma meetMan_injective : Function.Injective (meetMan \u03bc \u03bd h\u03bc h\u03bd) := by\n  intro i1 i2 he\n  set j := meetMan \u03bc \u03bd h\u03bc h\u03bd i1 with hjdef\n  have h1 : meetMan \u03bc \u03bd h\u03bc h\u03bd i1 = j := hjdef.symm\n  have h2 : meetMan \u03bc \u03bd h\u03bc h\u03bd i2 = j := he.symm.trans hjdef.symm\n  rcases meetMan_mem_women \u03bc \u03bd h\u03bc h\u03bd h1 with hm1 | hn1 <;>\n    rcases meetMan_mem_women \u03bc \u03bd h\u03bc h\u03bd h2 with hm2 | hn2\n  \u00b7 exact hm1.symm.trans hm2\n  \u00b7 have a := meetMan_worse_left \u03bc \u03bd h\u03bc h\u03bd h1 hm1\n    have b := meetMan_worse_right \u03bc \u03bd h\u03bc h\u03bd h2 hn2\n    rw [hn2] at a; rw [hm1] at b\n    exact (List.idxOf_inj (pref_list_mem _ (m.valid j).1 (m.valid j).2 i1)).mp\n      (le_antisymm b a)\n  \u00b7 have a := meetMan_worse_right \u03bc \u03bd h\u03bc h\u03bd h1 hn1\n    have b := meetMan_worse_left \u03bc \u03bd h\u03bc h\u03bd h2 hm2\n    rw [hm2] at a; rw [hn1] at b\n    exact (List.idxOf_inj (pref_list_mem _ (m.valid j).1 (m.valid j).2 i1)).mp\n      (le_antisymm b a)\n  \u00b7 exact hn1.symm.trans hn2\n\n/-- The meet man-assignment packaged as an equivalence. -/\nnoncomputable def meetEquiv : Fin n \u2243 Fin n :=\n  Equiv.ofBijective (meetMan \u03bc \u03bd h\u03bc h\u03bd)\n    (Finite.injective_iff_bijective.mp (meetMan_injective \u03bc \u03bd h\u03bc h\u03bd))\n\n/-- The **meet** `\u03bc \u2227 \u03bd`: each woman keeps her more-preferred man; each man\nkeeps his less-preferred woman. -/\nnoncomputable def stableMeet : Matching (Fin n) (Fin n) where\n  matchM i := some (meetMan \u03bc \u03bd h\u03bc h\u03bd i)\n  matchW j := some ((meetEquiv \u03bc \u03bd h\u03bc h\u03bd).symm j)\n  consistent := by\n    intro i j\n    simp only [Option.some.injEq]\n    rw [Equiv.symm_apply_eq]\n    exact eq_comm\n\n@[simp] lemma stableMeet_matchM (i : Fin n) :\n    (stableMeet \u03bc \u03bd h\u03bc h\u03bd).matchM i = some (meetMan \u03bc \u03bd h\u03bc h\u03bd i) := rfl\n\n@[simp] lemma stableMeet_matchW (j : Fin n) :\n    (stableMeet \u03bc \u03bd h\u03bc h\u03bd).matchW j = some ((meetEquiv \u03bc \u03bd h\u03bc h\u03bd).symm j) := rfl\n\n",
      "column": 1,
      "end": 19617,
      "kind": "theorem",
      "line": 388,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "meetMan_injective",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 17878
    },
    {
      "body": "lemma meetMan_le_left (i : Fin n) :\n    (w.prefs i).idxOf (meetMan \u03bc \u03bd h\u03bc h\u03bd i) \u2264 (w.prefs i).idxOf (mPartner \u03bc h\u03bc i) := by\n  unfold meetMan; split_ifs with h\n  \u00b7 exact le_refl _\n  \u00b7 push_neg at h; omega\n\n",
      "column": 1,
      "end": 19822,
      "kind": "theorem",
      "line": 430,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "meetMan_le_left",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 19617
    },
    {
      "body": "lemma meetMan_le_right (i : Fin n) :\n    (w.prefs i).idxOf (meetMan \u03bc \u03bd h\u03bc h\u03bd i) \u2264 (w.prefs i).idxOf (mPartner \u03bd h\u03bd i) := by\n  unfold meetMan; split_ifs with h\n  \u00b7 exact h\n  \u00b7 exact le_refl _\n\n/-- The meet of two stable matchings is stable. -/\n",
      "column": 1,
      "end": 20066,
      "kind": "theorem",
      "line": 436,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "meetMan_le_right",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 19822
    },
    {
      "body": "theorem stableMeet_isStable :\n    Matching.IsStable (MatchingMarket.ofEquivData w m) (stableMeet \u03bc \u03bd h\u03bc h\u03bd) := by\n  intro i j hblock\n  obtain \u27e8hi, hj\u27e9 := hblock\n  rw [stableMeet_matchM] at hi\n  rw [stableMeet_matchW] at hj\n  set jw := (meetEquiv \u03bc \u03bd h\u03bc h\u03bd).symm j with hjwdef\n  have hi' : (w.prefs i).idxOf j < (w.prefs i).idxOf (meetMan \u03bc \u03bd h\u03bc h\u03bd i) := prefM_strict.mp hi\n  have hj' : (m.prefs j).idxOf i < (m.prefs j).idxOf jw := prefW_strict.mp hj\n  have hmeet_jw : meetMan \u03bc \u03bd h\u03bc h\u03bd jw = j := (meetEquiv \u03bc \u03bd h\u03bc h\u03bd).apply_symm_apply j\n  rcases meetMan_mem_women \u03bc \u03bd h\u03bc h\u03bd hmeet_jw with hm | hn\n  \u00b7 -- `jw` is `j`'s `\u03bc`-woman, so `(i, j)` blocks `\u03bc`.\n    refine h\u03bc i j \u27e8?_, ?_\u27e9\n    \u00b7 rw [matchM_mPartner \u03bc h\u03bc i]\n      exact prefM_strict.mpr (lt_of_lt_of_le hi' (meetMan_le_left \u03bc \u03bd h\u03bc h\u03bd i))\n    \u00b7 rw [matchW_wPartner \u03bc h\u03bc j, hm]; exact prefW_strict.mpr hj'\n  \u00b7 -- `jw` is `j`'s `\u03bd`-woman, so `(i, j)` blocks `\u03bd`.\n    refine h\u03bd i j \u27e8?_, ?_\u27e9\n    \u00b7 rw [matchM_mPartner \u03bd h\u03bd i]\n      exact prefM_strict.mpr (lt_of_lt_of_le hi' (meetMan_le_right \u03bc \u03bd h\u03bc h\u03bd i))\n    \u00b7 rw [matchW_wPartner \u03bd h\u03bd j, hn]; exact prefW_strict.mpr hj'\n\n/-! ### Order-theoretic characterizations of join and meet -/\n\n",
      "column": 1,
      "end": 21254,
      "kind": "theorem",
      "line": 443,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "stableMeet_isStable",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 20066
    },
    {
      "body": "lemma wPartner_stableJoin (j : Fin n) :\n    wPartner (stableJoin \u03bc \u03bd h\u03bc h\u03bd) (stableJoin_isStable \u03bc \u03bd h\u03bc h\u03bd) j\n      = joinWoman \u03bc \u03bd h\u03bc h\u03bd j := rfl\n\n",
      "column": 1,
      "end": 21402,
      "kind": "theorem",
      "line": 467,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "wPartner_stableJoin",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 21254
    },
    {
      "body": "lemma wPartner_stableMeet (j : Fin n) :\n    wPartner (stableMeet \u03bc \u03bd h\u03bc h\u03bd) (stableMeet_isStable \u03bc \u03bd h\u03bc h\u03bd) j\n      = (meetEquiv \u03bc \u03bd h\u03bc h\u03bd).symm j := rfl\n\n/-- The meet woman of man `j` is one of his two partners (his worse). -/\n",
      "column": 1,
      "end": 21630,
      "kind": "theorem",
      "line": 471,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "wPartner_stableMeet",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 21402
    },
    {
      "body": "lemma meetEquiv_symm_eq_or (j : Fin n) :\n    (meetEquiv \u03bc \u03bd h\u03bc h\u03bd).symm j = wPartner \u03bc h\u03bc j \u2228\n    (meetEquiv \u03bc \u03bd h\u03bc h\u03bd).symm j = wPartner \u03bd h\u03bd j := by\n  have h : meetMan \u03bc \u03bd h\u03bc h\u03bd ((meetEquiv \u03bc \u03bd h\u03bc h\u03bd).symm j) = j :=\n    (meetEquiv \u03bc \u03bd h\u03bc h\u03bd).apply_symm_apply j\n  rcases meetMan_mem_women \u03bc \u03bd h\u03bc h\u03bd h with hm | hn\n  \u00b7 exact Or.inl hm.symm\n  \u00b7 exact Or.inr hn.symm\n\n",
      "column": 1,
      "end": 21996,
      "kind": "theorem",
      "line": 476,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "meetEquiv_symm_eq_or",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 21630
    },
    {
      "body": "lemma stableMeet_ge_left (j : Fin n) :\n    (m.prefs j).idxOf (wPartner \u03bc h\u03bc j) \u2264 (m.prefs j).idxOf ((meetEquiv \u03bc \u03bd h\u03bc h\u03bd).symm j) := by\n  have h : meetMan \u03bc \u03bd h\u03bc h\u03bd ((meetEquiv \u03bc \u03bd h\u03bc h\u03bd).symm j) = j :=\n    (meetEquiv \u03bc \u03bd h\u03bc h\u03bd).apply_symm_apply j\n  rcases meetMan_mem_women \u03bc \u03bd h\u03bc h\u03bd h with hm | hn\n  \u00b7 exact le_of_eq (congrArg (fun x => (m.prefs j).idxOf x) hm)\n  \u00b7 exact meetMan_worse_right \u03bc \u03bd h\u03bc h\u03bd h hn\n\n",
      "column": 1,
      "end": 22406,
      "kind": "theorem",
      "line": 485,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "stableMeet_ge_left",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 21996
    },
    {
      "body": "lemma stableMeet_ge_right (j : Fin n) :\n    (m.prefs j).idxOf (wPartner \u03bd h\u03bd j) \u2264 (m.prefs j).idxOf ((meetEquiv \u03bc \u03bd h\u03bc h\u03bd).symm j) := by\n  have h : meetMan \u03bc \u03bd h\u03bc h\u03bd ((meetEquiv \u03bc \u03bd h\u03bc h\u03bd).symm j) = j :=\n    (meetEquiv \u03bc \u03bd h\u03bc h\u03bd).apply_symm_apply j\n  rcases meetMan_mem_women \u03bc \u03bd h\u03bc h\u03bd h with hm | hn\n  \u00b7 exact meetMan_worse_left \u03bc \u03bd h\u03bc h\u03bd h hm\n  \u00b7 exact le_of_eq (congrArg (fun x => (m.prefs j).idxOf x) hn)\n\n/-! ### The lattice of stable matchings -/\n\n/-- The type of stable matchings of a one-to-one market. -/\n",
      "column": 1,
      "end": 22920,
      "kind": "theorem",
      "line": 493,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "stableMeet_ge_right",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 22406
    },
    {
      "body": "def StableMatching (w' m' : Preferences n) : Type :=\n  { \u03bc : Matching (Fin n) (Fin n) // Matching.IsStable (MatchingMarket.ofEquivData w' m') \u03bc }\n\nnamespace StableMatching\n\n/-- Man `j`'s partner under a stable matching. -/\nnoncomputable def partner (\u03bc : StableMatching w m) (j : Fin n) : Fin n := wPartner \u03bc.1 \u03bc.2 j\n\n",
      "column": 1,
      "end": 23237,
      "kind": "theorem",
      "line": 504,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "StableMatching",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 22920
    },
    {
      "body": "lemma matchW_partner (\u03bc : StableMatching w m) (j : Fin n) :\n    \u03bc.1.matchW j = some (\u03bc.partner j) := matchW_wPartner \u03bc.1 \u03bc.2 j\n\n/-- Men-preference order: `\u03bc \u2264 \u03bd` iff every man weakly prefers his `\u03bd`-partner\nto his `\u03bc`-partner (smaller `idxOf` = more preferred). -/\ninstance : PartialOrder (StableMatching w m) where\n  le \u03bc \u03bd := \u2200 j : Fin n, (m.prefs j).idxOf (\u03bd.partner j) \u2264 (m.prefs j).idxOf (\u03bc.partner j)\n  le_refl _ _ := le_refl _\n  le_trans _ _ _ h1 h2 j := le_trans (h2 j) (h1 j)\n  le_antisymm \u03bc \u03bd h1 h2 := by\n    have hpart : \u2200 j, \u03bc.partner j = \u03bd.partner j := fun j =>\n      (List.idxOf_inj (pref_list_mem _ (m.valid j).1 (m.valid j).2 _)).mp\n        (le_antisymm (h2 j) (h1 j))\n    apply Subtype.ext\n    apply Matching.ext\n    \u00b7 funext i\n      apply Option.ext; intro k\n      rw [\u03bc.1.consistent i k, \u03bd.1.consistent i k,\n        matchW_partner \u03bc k, matchW_partner \u03bd k, hpart k]\n    \u00b7 funext j\n      rw [matchW_partner \u03bc j, matchW_partner \u03bd j, hpart j]\n\n/-- **Conway\u2013Knuth lattice.** The stable matchings of a one-to-one market form\na lattice under the men-preference order: the join gives every man his more-\npreferred of two partners, the meet his less-preferred, and both are stable. -/\nnoncomputable instance : Lattice (StableMatching w m) :=\n  { (inferInstance : PartialOrder (StableMatching w m)) with\n    sup := fun \u03bc \u03bd => \u27e8stableJoin \u03bc.1 \u03bd.1 \u03bc.2 \u03bd.2, stableJoin_isStable \u03bc.1 \u03bd.1 \u03bc.2 \u03bd.2\u27e9\n    inf := fun \u03bc \u03bd => \u27e8stableMeet \u03bc.1 \u03bd.1 \u03bc.2 \u03bd.2, stableMeet_isStable \u03bc.1 \u03bd.1 \u03bc.2 \u03bd.2\u27e9\n    le_sup_left := fun \u03bc \u03bd j => joinWoman_le_left \u03bc.1 \u03bd.1 \u03bc.2 \u03bd.2 j\n    le_sup_right := fun \u03bc \u03bd j => joinWoman_le_right \u03bc.1 \u03bd.1 \u03bc.2 \u03bd.2 j\n    sup_le := fun \u03bc \u03bd bound h1 h2 j => by\n      show (m.prefs j).idxOf (bound.partner j) \u2264 (m.prefs j).idxOf (joinWoman \u03bc.1 \u03bd.1 \u03bc.2 \u03bd.2 j)\n      rcases joinWoman_eq_or \u03bc.1 \u03bd.1 \u03bc.2 \u03bd.2 j with he | he\n      \u00b7 rw [he]; exact h1 j\n      \u00b7 rw [he]; exact h2 j\n    inf_le_left := fun \u03bc \u03bd j => stableMeet_ge_left \u03bc.1 \u03bd.1 \u03bc.2 \u03bd.2 j\n    inf_le_right := fun \u03bc \u03bd j => stableMeet_ge_right \u03bc.1 \u03bd.1 \u03bc.2 \u03bd.2 j\n    le_inf := fun bound \u03bc \u03bd h1 h2 j => by\n      show (m.prefs j).idxOf ((meetEquiv \u03bc.1 \u03bd.1 \u03bc.2 \u03bd.2).symm j)\n        \u2264 (m.prefs j).idxOf (bound.partner j)\n      rcases meetEquiv_symm_eq_or \u03bc.1 \u03bd.1 \u03bc.2 \u03bd.2 j with he | he\n      \u00b7 rw [he]; exact h1 j\n      \u00b7 rw [he]; exact h2 j }\n\n/-! ### Men-optimality as the lattice maximum -/\n\n/-- The men-proposing Gale\u2013Shapley output, as an element of the lattice of\nstable matchings. -/\nnoncomputable def gsStable (w' m' : Preferences n) [NeZero n] : StableMatching w' m' :=\n  \u27e8Matching.ofGS (gs w' m') (gs_bijective w' m'), galeShapley_isStable w' m'\u27e9\n\n/-- **The GS output is the greatest stable matching** in the men-preference\norder: every man weakly prefers his GS partner to his partner in any other\nstable matching. This is `galeShapley_isProposingOptimal` packaged as the\nlattice maximum (`\u22a4`-like greatest element). -/\n",
      "column": 1,
      "end": 26123,
      "kind": "theorem",
      "line": 512,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "matchW_partner",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 23237
    },
    {
      "body": "theorem gsStable_greatest [NeZero n] (\u03bc : StableMatching w m) : \u03bc \u2264 gsStable w m := by\n  intro j\n  show (m.prefs j).idxOf ((gsStable w m).partner j) \u2264 (m.prefs j).idxOf (\u03bc.partner j)\n  have hg : (gsStable w m).partner j\n      = (Equiv.ofBijective (gs w m) (gs_bijective w m)).symm j := rfl\n  rw [hg]\n  exact galeShapley_isProposingOptimal w m \u03bc.1 \u03bc.2 j (\u03bc.partner j) (matchW_partner \u03bc j)\n\n/-- `gsStable` is the greatest element of the stable-matching lattice. -/\n",
      "column": 1,
      "end": 26586,
      "kind": "theorem",
      "line": 568,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "gsStable_greatest",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 26123
    },
    {
      "body": "theorem gsStable_isGreatest [NeZero n] :\n    IsGreatest (Set.univ : Set (StableMatching w m)) (gsStable w m) :=\n  \u27e8Set.mem_univ _, fun \u03bc _ => gsStable_greatest \u03bc\u27e9\n\nend StableMatching\n\nend GS\n",
      "column": 1,
      "end": 26777,
      "kind": "theorem",
      "line": 577,
      "module": "EconCSLib.MarketDesign.Matching.Lattice",
      "name": "gsStable_isGreatest",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/MarketDesign/Matching/Lattice.lean",
      "start": 26586
    }
  ]
}
```

## Intent

- Lean is acting as a counterchecker only.
- Blank or flawed proofs are recorded as incompleteness, not inconsistency.
- Any new lemmata discovered here are proposals for review, not automatic edits.