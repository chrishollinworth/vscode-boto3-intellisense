"""
Type annotations for aiops service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_aiops/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_aiops.client import AIOpsClient
    from mypy_boto3_aiops.paginator import (
        ListInvestigationGroupsPaginator,
    )

    session = Session()
    client: AIOpsClient = session.client("aiops")

    list_investigation_groups_paginator: ListInvestigationGroupsPaginator = client.get_paginator("list_investigation_groups")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListInvestigationGroupsInputPaginateTypeDef,
    ListInvestigationGroupsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListInvestigationGroupsPaginator",)

if TYPE_CHECKING:
    _ListInvestigationGroupsPaginatorBase = Paginator[ListInvestigationGroupsOutputTypeDef]
else:
    _ListInvestigationGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListInvestigationGroupsPaginator(_ListInvestigationGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/aiops/paginator/ListInvestigationGroups.html#AIOps.Paginator.ListInvestigationGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_aiops/paginators/#listinvestigationgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInvestigationGroupsInputPaginateTypeDef]
    ) -> PageIterator[ListInvestigationGroupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/aiops/paginator/ListInvestigationGroups.html#AIOps.Paginator.ListInvestigationGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_aiops/paginators/#listinvestigationgroupspaginator)
        """
