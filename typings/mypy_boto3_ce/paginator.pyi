"""
Type annotations for ce service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ce.client import CostExplorerClient
    from mypy_boto3_ce.paginator import (
        GetAnomaliesPaginator,
        GetAnomalyMonitorsPaginator,
        GetAnomalySubscriptionsPaginator,
    )

    session = Session()
    client: CostExplorerClient = session.client("ce")

    get_anomalies_paginator: GetAnomaliesPaginator = client.get_paginator("get_anomalies")
    get_anomaly_monitors_paginator: GetAnomalyMonitorsPaginator = client.get_paginator("get_anomaly_monitors")
    get_anomaly_subscriptions_paginator: GetAnomalySubscriptionsPaginator = client.get_paginator("get_anomaly_subscriptions")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetAnomaliesRequestPaginateTypeDef,
    GetAnomaliesResponseTypeDef,
    GetAnomalyMonitorsRequestPaginateTypeDef,
    GetAnomalyMonitorsResponsePaginatorTypeDef,
    GetAnomalySubscriptionsRequestPaginateTypeDef,
    GetAnomalySubscriptionsResponsePaginatorTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetAnomaliesPaginator",
    "GetAnomalyMonitorsPaginator",
    "GetAnomalySubscriptionsPaginator",
)

if TYPE_CHECKING:
    _GetAnomaliesPaginatorBase = Paginator[GetAnomaliesResponseTypeDef]
else:
    _GetAnomaliesPaginatorBase = Paginator  # type: ignore[assignment]

class GetAnomaliesPaginator(_GetAnomaliesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/GetAnomalies.html#CostExplorer.Paginator.GetAnomalies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#getanomaliespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetAnomaliesRequestPaginateTypeDef]
    ) -> PageIterator[GetAnomaliesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/GetAnomalies.html#CostExplorer.Paginator.GetAnomalies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#getanomaliespaginator)
        """

if TYPE_CHECKING:
    _GetAnomalyMonitorsPaginatorBase = Paginator[GetAnomalyMonitorsResponsePaginatorTypeDef]
else:
    _GetAnomalyMonitorsPaginatorBase = Paginator  # type: ignore[assignment]

class GetAnomalyMonitorsPaginator(_GetAnomalyMonitorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/GetAnomalyMonitors.html#CostExplorer.Paginator.GetAnomalyMonitors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#getanomalymonitorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetAnomalyMonitorsRequestPaginateTypeDef]
    ) -> PageIterator[GetAnomalyMonitorsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/GetAnomalyMonitors.html#CostExplorer.Paginator.GetAnomalyMonitors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#getanomalymonitorspaginator)
        """

if TYPE_CHECKING:
    _GetAnomalySubscriptionsPaginatorBase = Paginator[
        GetAnomalySubscriptionsResponsePaginatorTypeDef
    ]
else:
    _GetAnomalySubscriptionsPaginatorBase = Paginator  # type: ignore[assignment]

class GetAnomalySubscriptionsPaginator(_GetAnomalySubscriptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/GetAnomalySubscriptions.html#CostExplorer.Paginator.GetAnomalySubscriptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#getanomalysubscriptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetAnomalySubscriptionsRequestPaginateTypeDef]
    ) -> PageIterator[GetAnomalySubscriptionsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/GetAnomalySubscriptions.html#CostExplorer.Paginator.GetAnomalySubscriptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#getanomalysubscriptionspaginator)
        """
