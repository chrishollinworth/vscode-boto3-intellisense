"""
Type annotations for marketplace-agreement service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/literals.html)

Usage::

    ```python
    from mypy_boto3_marketplace_agreement.literals import AgreementStatusType

    data: AgreementStatusType = "ACTIVE"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AgreementStatusType", "SortOrderType")

AgreementStatusType = Literal[
    "ACTIVE",
    "ARCHIVED",
    "CANCELLED",
    "EXPIRED",
    "RENEWED",
    "REPLACED",
    "ROLLED_BACK",
    "SUPERSEDED",
    "TERMINATED",
]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
