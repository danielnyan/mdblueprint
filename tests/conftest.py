from __future__ import annotations

from pathlib import Path

import pytest


ECONCSLIB_CHECKOUT = Path(__file__).parent / "fixtures" / "econcslib"


@pytest.fixture
def econcslib_checkout() -> Path:
    if not ECONCSLIB_CHECKOUT.exists():
        pytest.skip(
            "EconCSLib fixture checkout is missing. Clone or symlink the repo "
            "into tests/fixtures/econcslib/ (see tests/README.md)."
        )
    return ECONCSLIB_CHECKOUT
