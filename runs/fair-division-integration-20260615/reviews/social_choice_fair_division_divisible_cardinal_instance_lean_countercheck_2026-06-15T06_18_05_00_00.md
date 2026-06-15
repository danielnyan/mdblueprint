---
agent: lean-countercheck
node_id: social_choice.fair_division.divisible.cardinal_instance
created_at: "2026-06-15T06:18:05+00:00"
---

# Lean Countercheck: Divisible Cardinal Instance

## Inputs

- node file: `/home/azureuser/EconCSLib/docs/knowledge/nodes/social_choice/fair_division/divisible/cardinal_instance.md`
- lean file: `/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Divisible/Instance.lean`
- corpus root: `/home/azureuser/EconCSLib`

## Method Status

- heuristic: used

## Matched Declarations

- `SocialChoice.FairDivision.Divisible.CardinalInstance.toGenericCardinalInstance`
- `SocialChoice.FairDivision.Divisible.CardinalInstance.toShareInstance`
- `SocialChoice.FairDivision.Divisible.CardinalInstance.IsEnvyFree`
- `SocialChoice.FairDivision.Divisible.CardinalInstance.IsProportional`
- `SocialChoice.FairDivision.Divisible.CardinalInstance.IsEquitable`
- `SocialChoice.FairDivision.Divisible.CardinalInstance.IsParetoOptimal`

## Missing Declarations

- `SocialChoice.FairDivision.Divisible.CardinalInstance`
- `SocialChoice.FairDivision.Divisible.CardinalInstance.utilitarianWelfare`
- `SocialChoice.FairDivision.Divisible.CardinalInstance.egalitarianWelfare`

## Extra Declarations

- `feasible`
- `feasible`
- `toCakeValuation`
- `feasible`
- `isEnvyFree_iff_toCardinalInstance_isEnvyFree`

## Node Uses vs Extracted Dependencies

- node uses: `social_choice.fair_division.divisible.ordinal_instance`, `social_choice.fair_division.cardinal_instance`, `social_choice.fair_division.envy_free`, `social_choice.fair_division.proportional`, `social_choice.fair_division.utilitarian_welfare`, `social_choice.fair_division.egalitarian_welfare`
- missing uses: `social_choice.fair_division.divisible.ordinal_instance`, `social_choice.fair_division.cardinal_instance`, `social_choice.fair_division.envy_free`, `social_choice.fair_division.proportional`, `social_choice.fair_division.utilitarian_welfare`, `social_choice.fair_division.egalitarian_welfare`
- extra uses: `IsEnvyFree`, `IsProportional`, `toCakeValuation`, `toGenericCardinalInstance`, `toShareInstance`

## Raw Snapshot

```json
{
  "corpus_root": "/home/azureuser/EconCSLib",
  "dependencies": [
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "source": "toShareInstance",
      "target": "toGenericCardinalInstance"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "source": "IsEnvyFree",
      "target": "toGenericCardinalInstance"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "source": "IsProportional",
      "target": "toGenericCardinalInstance"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "source": "IsEquitable",
      "target": "toGenericCardinalInstance"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "source": "IsParetoOptimal",
      "target": "toGenericCardinalInstance"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "source": "feasible",
      "target": "toGenericCardinalInstance"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "source": "feasible",
      "target": "toShareInstance"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "source": "IsEnvyFree",
      "target": "toCakeValuation"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "source": "isEnvyFree_iff_toCardinalInstance_isEnvyFree",
      "target": "IsEnvyFree"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "source": "IsProportional",
      "target": "toCakeValuation"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "source": "IsEquitable",
      "target": "toCakeValuation"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "source": "IsEnvyFree.isProportional",
      "target": "IsProportional"
    },
    {
      "kind": "hard",
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "source": "IsEnvyFree.isProportional",
      "target": "IsEnvyFree"
    }
  ],
  "lean_file": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Divisible/Instance.lean",
  "method_status": {
    "heuristic": "used"
  },
  "node": {
    "body": "# Divisible Cardinal Instance\n\nA *divisible cardinal instance* assigns each agent a real-valued utility\nfor every measurable cake piece:\n$$\n\\mathrm{utility} : N \\to \\mathrm{Set}\\ \\Omega \\to \\mathbb{R}.\n$$\n\nIn Lean: structure `SocialChoice.FairDivision.Divisible.CardinalInstance N \u03a9`.\n\n## Bridges\n\n- `toGenericCardinalInstance` \u2014 view as a generic real-valued cardinal\n  fair-division instance\n  ([[social_choice.fair_division.cardinal_instance]]) over share type\n  $\\mathrm{Set}\\ \\Omega$ and resource $\\mathrm{Set.univ}$.\n- `toShareInstance` \u2014 compose with `inducedSharePref` to get the\n  underlying divisible *ordinal* instance\n  ([[social_choice.fair_division.divisible.ordinal_instance]]).\n\n## Instance-keyed fairness and welfare\n\nA complete set of instance-keyed wrappers re-exports the generic\npredicates:\n\n- `IsEnvyFree A`, `IsProportional n A`, `IsEquitable A`,\n  `IsParetoOptimal A` \u2014 fairness / efficiency predicates pinned to the\n  current instance's utility and feasibility.\n- `utilitarianWelfare A`, `egalitarianWelfare A` \u2014 welfare aggregations\n  ([[social_choice.fair_division.utilitarian_welfare]],\n  [[social_choice.fair_division.egalitarian_welfare]]).\n\nAll wrappers are definitional passes through to the corresponding\ngeneric predicates with $I.\\mathrm{utility}$ and feasibility supplied\nfrom the instance.\n\n## References\n\n- [AGT Chapter 13] Nisan, Roughgarden, Tardos, and Vazirani, *Algorithmic Game Theory*. Cardinal valuations in cake-cutting.",
    "file_path": "/home/azureuser/EconCSLib/docs/knowledge/nodes/social_choice/fair_division/divisible/cardinal_instance.md",
    "id": "social_choice.fair_division.divisible.cardinal_instance",
    "kind": "definition",
    "lean": {
      "declarations": [
        "SocialChoice.FairDivision.Divisible.CardinalInstance",
        "SocialChoice.FairDivision.Divisible.CardinalInstance.toGenericCardinalInstance",
        "SocialChoice.FairDivision.Divisible.CardinalInstance.toShareInstance",
        "SocialChoice.FairDivision.Divisible.CardinalInstance.IsEnvyFree",
        "SocialChoice.FairDivision.Divisible.CardinalInstance.IsProportional",
        "SocialChoice.FairDivision.Divisible.CardinalInstance.IsEquitable",
        "SocialChoice.FairDivision.Divisible.CardinalInstance.IsParetoOptimal",
        "SocialChoice.FairDivision.Divisible.CardinalInstance.utilitarianWelfare",
        "SocialChoice.FairDivision.Divisible.CardinalInstance.egalitarianWelfare"
      ],
      "modules": [
        "EconCSLib.SocialChoice.FairDivision.Divisible.Instance"
      ],
      "repository": null
    },
    "status": "formalized",
    "tags": [
      "fair-division",
      "divisible",
      "instance",
      "cardinal"
    ],
    "title": "Divisible Cardinal Instance",
    "uses": [
      "social_choice.fair_division.divisible.ordinal_instance",
      "social_choice.fair_division.cardinal_instance",
      "social_choice.fair_division.envy_free",
      "social_choice.fair_division.proportional",
      "social_choice.fair_division.utilitarian_welfare",
      "social_choice.fair_division.egalitarian_welfare"
    ]
  },
  "source_root": "/home/azureuser/EconCSLib",
  "theorems": [
    {
      "body": "def feasible {N \u03a9 : Type*} [MeasurableSpace \u03a9] [Fintype N]\n    (_I : Instance N \u03a9) (A : Allocation N \u03a9) : Prop :=\n  IsAllocation A\n\n/-- View a divisible ordinal instance as a generic no-externality fair-division\n    share instance. The resource is the whole cake `Set.univ`. -/\n",
      "column": 1,
      "end": 1454,
      "kind": "theorem",
      "line": 39,
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "name": "feasible",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Divisible/Instance.lean",
      "start": 1176
    },
    {
      "body": "def toShareInstance {N \u03a9 : Type*} [MeasurableSpace \u03a9] [Fintype N]\n    (I : Instance N \u03a9) :\n    SocialChoice.FairDivision.ShareInstance N (Set \u03a9) (Set \u03a9) where\n  resource := Set.univ\n  feasible := fun A => IsAllocation A\n  sharePref := I.sharePref\n\nend Instance\n\n/-- A real-valued cardinal divisible-goods instance. -/\nstructure CardinalInstance (N \u03a9 : Type*) where\n  /-- Utility assigned by each agent to each cake piece. -/\n  utility : N \u2192 Set \u03a9 \u2192 \u211d\n\nnamespace CardinalInstance\n\n/-- Feasibility for a cardinal divisible instance. -/\n",
      "column": 1,
      "end": 1988,
      "kind": "theorem",
      "line": 45,
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "name": "toShareInstance",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Divisible/Instance.lean",
      "start": 1454
    },
    {
      "body": "def feasible {N \u03a9 : Type*} [MeasurableSpace \u03a9] [Fintype N]\n    (_I : CardinalInstance N \u03a9)\n    (A : Allocation N \u03a9) : Prop :=\n  IsAllocation A\n\n/-- View a divisible cardinal instance as a generic real-valued cardinal\n    fair-division instance. The resource is the whole cake `Set.univ`. -/\n",
      "column": 1,
      "end": 2279,
      "kind": "theorem",
      "line": 62,
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "name": "feasible",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Divisible/Instance.lean",
      "start": 1988
    },
    {
      "body": "def toGenericCardinalInstance {N \u03a9 : Type*} [MeasurableSpace \u03a9] [Fintype N]\n    (I : CardinalInstance N \u03a9) :\n    SocialChoice.FairDivision.CardinalInstance N (Set \u03a9) (Set \u03a9) where\n  resource := Set.univ\n  feasible := fun A => IsAllocation A\n  utility := I.utility\n\n/-- View a divisible cardinal instance as the induced generic ordinal\n    no-externality instance. -/\n",
      "column": 1,
      "end": 2646,
      "kind": "theorem",
      "line": 69,
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "name": "toGenericCardinalInstance",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Divisible/Instance.lean",
      "start": 2279
    },
    {
      "body": "def toShareInstance {N \u03a9 : Type*} [MeasurableSpace \u03a9] [Fintype N]\n    (I : CardinalInstance N \u03a9) :\n    SocialChoice.FairDivision.ShareInstance N (Set \u03a9) (Set \u03a9) :=\n  I.toGenericCardinalInstance.toShareInstance\n\n/-! ### Instance-relative fairness and welfare wrappers -/\n\n/-- Envy-freeness for a divisible cardinal instance. -/\n",
      "column": 1,
      "end": 2973,
      "kind": "theorem",
      "line": 78,
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "name": "toShareInstance",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Divisible/Instance.lean",
      "start": 2646
    },
    {
      "body": "def IsEnvyFree {N \u03a9 : Type*} [MeasurableSpace \u03a9] [Fintype N]\n    (I : CardinalInstance N \u03a9) (A : Allocation N \u03a9) : Prop :=\n  SocialChoice.FairDivision.CardinalInstance.IsEnvyFree\n    I.toGenericCardinalInstance A\n\n/-- Proportionality for a divisible cardinal instance, relative to the whole cake. -/\n",
      "column": 1,
      "end": 3273,
      "kind": "theorem",
      "line": 86,
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "name": "IsEnvyFree",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Divisible/Instance.lean",
      "start": 2973
    },
    {
      "body": "def IsProportional {N \u03a9 : Type*} [MeasurableSpace \u03a9] [Fintype N]\n    (I : CardinalInstance N \u03a9) (n : \u2115) (A : Allocation N \u03a9) : Prop :=\n  SocialChoice.FairDivision.CardinalInstance.IsProportional\n    I.toGenericCardinalInstance n Set.univ A\n\n/-- Equitability for a divisible cardinal instance. -/\n",
      "column": 1,
      "end": 3569,
      "kind": "theorem",
      "line": 92,
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "name": "IsProportional",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Divisible/Instance.lean",
      "start": 3273
    },
    {
      "body": "def IsEquitable {N \u03a9 : Type*} [MeasurableSpace \u03a9] [Fintype N]\n    (I : CardinalInstance N \u03a9) (A : Allocation N \u03a9) : Prop :=\n  SocialChoice.FairDivision.CardinalInstance.IsEquitable\n    I.toGenericCardinalInstance A\n\n/-- Pareto optimality for a divisible cardinal instance. -/\n",
      "column": 1,
      "end": 3845,
      "kind": "theorem",
      "line": 98,
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "name": "IsEquitable",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Divisible/Instance.lean",
      "start": 3569
    },
    {
      "body": "def IsParetoOptimal {N \u03a9 : Type*} [MeasurableSpace \u03a9] [Fintype N]\n    (I : CardinalInstance N \u03a9) (A : Allocation N \u03a9) : Prop :=\n  SocialChoice.FairDivision.CardinalInstance.IsParetoOptimal\n    I.toGenericCardinalInstance A\n\n/-- Utilitarian welfare for a divisible cardinal instance. -/\nnoncomputable def utilitarianWelfare {N \u03a9 : Type*}\n    [MeasurableSpace \u03a9] [Fintype N]\n    (I : CardinalInstance N \u03a9) (A : Allocation N \u03a9) : \u211d :=\n  SocialChoice.FairDivision.CardinalInstance.utilitarianWelfare\n    I.toGenericCardinalInstance A\n\n/-- Egalitarian welfare for a divisible cardinal instance. -/\nnoncomputable def egalitarianWelfare {N \u03a9 : Type*}\n    [MeasurableSpace \u03a9] [Fintype N] [Nonempty N]\n    (I : CardinalInstance N \u03a9) (A : Allocation N \u03a9) : \u211d :=\n  SocialChoice.FairDivision.CardinalInstance.egalitarianWelfare\n    I.toGenericCardinalInstance A\n\nend CardinalInstance\n\n/-- A measure-based divisible-goods instance. -/\nstructure MeasureInstance (N \u03a9 : Type*) [MeasurableSpace \u03a9] where\n  /-- Each agent's measure over cake pieces. -/\n  measure : N \u2192 Measure \u03a9\n\nnamespace MeasureInstance\n\n/-- The raw cake valuation induced by a measure instance. -/\n",
      "column": 1,
      "end": 4996,
      "kind": "theorem",
      "line": 104,
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "name": "IsParetoOptimal",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Divisible/Instance.lean",
      "start": 3845
    },
    {
      "body": "def toCakeValuation {N \u03a9 : Type*} [MeasurableSpace \u03a9]\n    (I : MeasureInstance N \u03a9) : CakeValuation N \u03a9 ENNReal :=\n  MeasureValuation I.measure\n\n/-- The real-valued cardinal instance induced by measure values. -/\nnoncomputable def toCardinalInstance {N \u03a9 : Type*} [MeasurableSpace \u03a9]\n    (I : MeasureInstance N \u03a9) : CardinalInstance N \u03a9 where\n  utility := fun i S => (I.measure i S).toReal\n\n/-- Feasibility for a measure-based divisible instance. Like the ordinal and\n    cardinal divisible cases, this depends only on the ambient cake: a feasible\n    allocation is a measurable partition of `Set.univ`. -/\n",
      "column": 1,
      "end": 5603,
      "kind": "theorem",
      "line": 133,
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "name": "toCakeValuation",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Divisible/Instance.lean",
      "start": 4996
    },
    {
      "body": "def feasible {N \u03a9 : Type*} [MeasurableSpace \u03a9] [Fintype N]\n    (_I : MeasureInstance N \u03a9) (A : Allocation N \u03a9) : Prop :=\n  IsAllocation A\n\n/-- View a measure instance as a generic real-valued cardinal fair-division\n    instance. -/\nnoncomputable def toGenericCardinalInstance {N \u03a9 : Type*}\n    [MeasurableSpace \u03a9] [Fintype N]\n    (I : MeasureInstance N \u03a9) :\n    SocialChoice.FairDivision.CardinalInstance N (Set \u03a9) (Set \u03a9) :=\n  I.toCardinalInstance.toGenericCardinalInstance\n\n/-- View a measure instance as the induced generic ordinal no-externality\n    instance. -/\nnoncomputable def toShareInstance {N \u03a9 : Type*} [MeasurableSpace \u03a9] [Fintype N]\n    (I : MeasureInstance N \u03a9) :\n    SocialChoice.FairDivision.ShareInstance N (Set \u03a9) (Set \u03a9) :=\n  I.toGenericCardinalInstance.toShareInstance\n\n/-! ### Instance-relative fairness wrappers -/\n\n/-- Envy-freeness for a measure-based divisible instance, stated in `ENNReal`. -/\n",
      "column": 1,
      "end": 6524,
      "kind": "theorem",
      "line": 145,
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "name": "feasible",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Divisible/Instance.lean",
      "start": 5603
    },
    {
      "body": "def IsEnvyFree {N \u03a9 : Type*} [MeasurableSpace \u03a9]\n    (I : MeasureInstance N \u03a9) (A : Allocation N \u03a9) : Prop :=\n  SocialChoice.FairDivision.Divisible.IsEnvyFree I.toCakeValuation A\n\n/-- For finite measure instances, the raw `ENNReal` envy-freeness predicate agrees with\n    the real-valued cardinal predicate induced by `toReal`. -/\n",
      "column": 1,
      "end": 6855,
      "kind": "theorem",
      "line": 167,
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "name": "IsEnvyFree",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Divisible/Instance.lean",
      "start": 6524
    },
    {
      "body": "theorem isEnvyFree_iff_toCardinalInstance_isEnvyFree\n    {N \u03a9 : Type*} [MeasurableSpace \u03a9] [Fintype N]\n    (I : MeasureInstance N \u03a9) [\u2200 i, IsFiniteMeasure (I.measure i)]\n    (A : Allocation N \u03a9) :\n    I.IsEnvyFree A \u2194 I.toCardinalInstance.IsEnvyFree A := by\n  constructor\n  \u00b7 intro h i j\n    exact (ENNReal.toReal_le_toReal (measure_ne_top _ _) (measure_ne_top _ _)).mpr (h i j)\n  \u00b7 intro h i j\n    exact (ENNReal.toReal_le_toReal (measure_ne_top _ _) (measure_ne_top _ _)).mp (h i j)\n\n/-- Proportionality for a measure-based divisible instance, stated in `ENNReal`. -/\n",
      "column": 1,
      "end": 7425,
      "kind": "theorem",
      "line": 173,
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "name": "isEnvyFree_iff_toCardinalInstance_isEnvyFree",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Divisible/Instance.lean",
      "start": 6855
    },
    {
      "body": "def IsProportional {N \u03a9 : Type*} [MeasurableSpace \u03a9]\n    (I : MeasureInstance N \u03a9) (n : \u2115) (A : Allocation N \u03a9) : Prop :=\n  SocialChoice.FairDivision.Divisible.IsProportional n I.toCakeValuation A\n\n/-- Equitability for a measure-based divisible instance, stated in `ENNReal`. -/\n",
      "column": 1,
      "end": 7704,
      "kind": "theorem",
      "line": 185,
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "name": "IsProportional",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Divisible/Instance.lean",
      "start": 7425
    },
    {
      "body": "def IsEquitable {N \u03a9 : Type*} [MeasurableSpace \u03a9]\n    (I : MeasureInstance N \u03a9) (A : Allocation N \u03a9) : Prop :=\n  SocialChoice.FairDivision.Divisible.IsEquitable I.toCakeValuation A\n\n/-- Envy-freeness implies proportionality for complete measure-based divisible allocations. -/\n",
      "column": 1,
      "end": 7981,
      "kind": "theorem",
      "line": 190,
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "name": "IsEquitable",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Divisible/Instance.lean",
      "start": 7704
    },
    {
      "body": "theorem IsEnvyFree.isProportional {N \u03a9 : Type*}\n    [MeasurableSpace \u03a9] [Fintype N]\n    (I : MeasureInstance N \u03a9)\n    (A : Allocation N \u03a9)\n    (ha : IsAllocation A)\n    (hef : I.IsEnvyFree A) :\n    I.IsProportional (Fintype.card N) A :=\n  SocialChoice.FairDivision.Divisible.IsEnvyFree.isProportional I.measure A ha hef\n\nend MeasureInstance\n\nend Divisible\nend FairDivision\nend SocialChoice\n",
      "column": 1,
      "end": 8371,
      "kind": "theorem",
      "line": 195,
      "module": "EconCSLib.SocialChoice.FairDivision.Divisible.Instance",
      "name": "IsEnvyFree.isProportional",
      "source_path": "/home/azureuser/EconCSLib/EconCSLib/SocialChoice/FairDivision/Divisible/Instance.lean",
      "start": 7981
    }
  ]
}
```

## Intent

- Lean is acting as a counterchecker only.
- Blank or flawed proofs are recorded as incompleteness, not inconsistency.
- Any new lemmata discovered here are proposals for review, not automatic edits.