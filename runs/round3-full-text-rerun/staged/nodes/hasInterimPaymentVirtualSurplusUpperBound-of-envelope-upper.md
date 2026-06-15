---
id: hasInterimPaymentVirtualSurplusUpperBound-of-envelope-upper
title: hasInterimPaymentVirtualSurplusUpperBound_of_envelope_upper
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - hasInterimPaymentVirtualSurplusUpperBound_of_envelope_upper
uses:
  - HasInterimPaymentEnvelopeUpperBound
  - HasEnvelopeVirtualSurplusUpperBound
  - HasInterimPaymentVirtualSurplusUpperBound
---

# hasInterimPaymentVirtualSurplusUpperBound_of_envelope_upper

## Lean type

```lean
theorem hasInterimPaymentVirtualSurplusUpperBound_of_envelope_upper [Fintype I] (A B : BayesianSingleItemAuction I) (hpay : A.HasInterimPaymentEnvelopeUpperBound B) (henv : A.HasEnvelopeVirtualSurplusUpperBound B) : A.HasInterimPaymentVirtualSurplusUpperBound B
```

## Dependencies

- HasInterimPaymentEnvelopeUpperBound
- HasEnvelopeVirtualSurplusUpperBound
- HasInterimPaymentVirtualSurplusUpperBound
