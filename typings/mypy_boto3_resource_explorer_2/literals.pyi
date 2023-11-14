"""
Type annotations for resource-explorer-2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/literals.html)

Usage::

    ```python
    from mypy_boto3_resource_explorer_2.literals import IndexStateType

    data: IndexStateType = "ACTIVE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "IndexStateType",
    "IndexTypeType",
    "ListIndexesPaginatorName",
    "ListSupportedResourceTypesPaginatorName",
    "ListViewsPaginatorName",
    "SearchPaginatorName",
)

IndexStateType = Literal["ACTIVE", "CREATING", "DELETED", "DELETING", "UPDATING"]
IndexTypeType = Literal["AGGREGATOR", "LOCAL"]
ListIndexesPaginatorName = Literal["list_indexes"]
ListSupportedResourceTypesPaginatorName = Literal["list_supported_resource_types"]
ListViewsPaginatorName = Literal["list_views"]
SearchPaginatorName = Literal["search"]
