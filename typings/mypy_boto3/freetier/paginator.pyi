"""
Type annotations for freetier service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_freetier.client import FreeTierClient
    from mypy_boto3_freetier.paginator import (
        GetFreeTierUsagePaginator,
        ListAccountActivitiesPaginator,
    )

    session = Session()
    client: FreeTierClient = session.client("freetier")

    get_free_tier_usage_paginator: GetFreeTierUsagePaginator = client.get_paginator("get_free_tier_usage")
    list_account_activities_paginator: ListAccountActivitiesPaginator = client.get_paginator("list_account_activities")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetFreeTierUsageRequestPaginateTypeDef,
    GetFreeTierUsageResponseTypeDef,
    ListAccountActivitiesRequestPaginateTypeDef,
    ListAccountActivitiesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("GetFreeTierUsagePaginator", "ListAccountActivitiesPaginator")

if TYPE_CHECKING:
    _GetFreeTierUsagePaginatorBase = Paginator[GetFreeTierUsageResponseTypeDef]
else:
    _GetFreeTierUsagePaginatorBase = Paginator  # type: ignore[assignment]

class GetFreeTierUsagePaginator(_GetFreeTierUsagePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/freetier/paginator/GetFreeTierUsage.html#FreeTier.Paginator.GetFreeTierUsage)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/paginators/#getfreetierusagepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetFreeTierUsageRequestPaginateTypeDef]
    ) -> PageIterator[GetFreeTierUsageResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/freetier/paginator/GetFreeTierUsage.html#FreeTier.Paginator.GetFreeTierUsage.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/paginators/#getfreetierusagepaginator)
        """

if TYPE_CHECKING:
    _ListAccountActivitiesPaginatorBase = Paginator[ListAccountActivitiesResponseTypeDef]
else:
    _ListAccountActivitiesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccountActivitiesPaginator(_ListAccountActivitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/freetier/paginator/ListAccountActivities.html#FreeTier.Paginator.ListAccountActivities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/paginators/#listaccountactivitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccountActivitiesRequestPaginateTypeDef]
    ) -> PageIterator[ListAccountActivitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/freetier/paginator/ListAccountActivities.html#FreeTier.Paginator.ListAccountActivities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/paginators/#listaccountactivitiespaginator)
        """
