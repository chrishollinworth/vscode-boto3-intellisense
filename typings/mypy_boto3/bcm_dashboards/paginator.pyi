"""
Type annotations for bcm-dashboards service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_dashboards/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_bcm_dashboards.client import BillingandCostManagementDashboardsClient
    from mypy_boto3_bcm_dashboards.paginator import (
        ListDashboardsPaginator,
    )

    session = Session()
    client: BillingandCostManagementDashboardsClient = session.client("bcm-dashboards")

    list_dashboards_paginator: ListDashboardsPaginator = client.get_paginator("list_dashboards")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListDashboardsRequestPaginateTypeDef, ListDashboardsResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListDashboardsPaginator",)

if TYPE_CHECKING:
    _ListDashboardsPaginatorBase = Paginator[ListDashboardsResponseTypeDef]
else:
    _ListDashboardsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDashboardsPaginator(_ListDashboardsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-dashboards/paginator/ListDashboards.html#BillingandCostManagementDashboards.Paginator.ListDashboards)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_dashboards/paginators/#listdashboardspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDashboardsRequestPaginateTypeDef]
    ) -> PageIterator[ListDashboardsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-dashboards/paginator/ListDashboards.html#BillingandCostManagementDashboards.Paginator.ListDashboards.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_dashboards/paginators/#listdashboardspaginator)
        """
