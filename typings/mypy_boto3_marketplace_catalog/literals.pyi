"""
Type annotations for marketplace-catalog service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/literals.html)

Usage::

    ```python
    from mypy_boto3_marketplace_catalog.literals import ChangeStatusType

    data: ChangeStatusType = "APPLYING"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ChangeStatusType",
    "FailureCodeType",
    "ListChangeSetsPaginatorName",
    "ListEntitiesPaginatorName",
    "OwnershipTypeType",
    "SortOrderType",
)

ChangeStatusType = Literal["APPLYING", "CANCELLED", "FAILED", "PREPARING", "SUCCEEDED"]
FailureCodeType = Literal["CLIENT_ERROR", "SERVER_FAULT"]
ListChangeSetsPaginatorName = Literal["list_change_sets"]
ListEntitiesPaginatorName = Literal["list_entities"]
OwnershipTypeType = Literal["SELF", "SHARED"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
