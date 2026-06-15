---
id: internal-door-two-rooms
title: internal_door_two_rooms
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - internal_door_two_rooms
uses:
  - isInternalDoor
  - isRoom
  - isDominant
  - keylemma_of_dominant
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - injOn_sdiff
  - M_set
  - M_sets_disjoint
  - is_maximal_in_M_set
  - m_element_is_maximal
  - m_element_not_in_tau
  - sublemma_3_2
  - idoor_determines_element
  - sublemma_3_1
  - maximal_element_unique
  - odoor_index_in_pair
  - Scarf
---

# internal_door_two_rooms

## Lean type

```lean
theorem internal_door_two_rooms [Fintype T] (τ : Finset T) (D : Finset I) (h_int_door : IST.isInternalDoor τ D) : ∃ (σ₁ σ₂ : Finset T) (C₁ C₂ : Finset I), (σ₁, C₁) ≠ (σ₂, C₂) ∧ IST.isRoom σ₁ C₁ ∧ IST.isRoom σ₂ C₂ ∧ isDoorof τ D σ₁ C₁ ∧ isDoorof τ D σ₂ C₂ ∧ (∀ σ C, IST.isRoom σ C → isDoorof τ D σ C → (σ = σ₁ ∧ C = C₁) ∨ (σ = σ₂ ∧ C = C₂))
```

## Dependencies

- isInternalDoor
- isRoom
- isDominant
- keylemma_of_dominant
- IsPositiveAffineOf.symm
- Indifferent.symm
- injOn_sdiff
- M_set
- M_sets_disjoint
- is_maximal_in_M_set
- m_element_is_maximal
- m_element_not_in_tau
- sublemma_3_2
- idoor_determines_element
- sublemma_3_1
- maximal_element_unique
- odoor_index_in_pair
- Scarf
