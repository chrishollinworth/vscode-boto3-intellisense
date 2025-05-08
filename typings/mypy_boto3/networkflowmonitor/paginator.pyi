"""
Type annotations for networkflowmonitor service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_networkflowmonitor.client import NetworkFlowMonitorClient
    from mypy_boto3_networkflowmonitor.paginator import (
        GetQueryResultsMonitorTopContributorsPaginator,
        GetQueryResultsWorkloadInsightsTopContributorsDataPaginator,
        GetQueryResultsWorkloadInsightsTopContributorsPaginator,
        ListMonitorsPaginator,
        ListScopesPaginator,
    )

    session = Session()
    client: NetworkFlowMonitorClient = session.client("networkflowmonitor")

    get_query_results_monitor_top_contributors_paginator: GetQueryResultsMonitorTopContributorsPaginator = client.get_paginator("get_query_results_monitor_top_contributors")
    get_query_results_workload_insights_top_contributors_data_paginator: GetQueryResultsWorkloadInsightsTopContributorsDataPaginator = client.get_paginator("get_query_results_workload_insights_top_contributors_data")
    get_query_results_workload_insights_top_contributors_paginator: GetQueryResultsWorkloadInsightsTopContributorsPaginator = client.get_paginator("get_query_results_workload_insights_top_contributors")
    list_monitors_paginator: ListMonitorsPaginator = client.get_paginator("list_monitors")
    list_scopes_paginator: ListScopesPaginator = client.get_paginator("list_scopes")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetQueryResultsMonitorTopContributorsInputPaginateTypeDef,
    GetQueryResultsMonitorTopContributorsOutputTypeDef,
    GetQueryResultsWorkloadInsightsTopContributorsDataInputPaginateTypeDef,
    GetQueryResultsWorkloadInsightsTopContributorsDataOutputTypeDef,
    GetQueryResultsWorkloadInsightsTopContributorsInputPaginateTypeDef,
    GetQueryResultsWorkloadInsightsTopContributorsOutputTypeDef,
    ListMonitorsInputPaginateTypeDef,
    ListMonitorsOutputTypeDef,
    ListScopesInputPaginateTypeDef,
    ListScopesOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetQueryResultsMonitorTopContributorsPaginator",
    "GetQueryResultsWorkloadInsightsTopContributorsDataPaginator",
    "GetQueryResultsWorkloadInsightsTopContributorsPaginator",
    "ListMonitorsPaginator",
    "ListScopesPaginator",
)

if TYPE_CHECKING:
    _GetQueryResultsMonitorTopContributorsPaginatorBase = Paginator[
        GetQueryResultsMonitorTopContributorsOutputTypeDef
    ]
else:
    _GetQueryResultsMonitorTopContributorsPaginatorBase = Paginator  # type: ignore[assignment]

class GetQueryResultsMonitorTopContributorsPaginator(
    _GetQueryResultsMonitorTopContributorsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/paginator/GetQueryResultsMonitorTopContributors.html#NetworkFlowMonitor.Paginator.GetQueryResultsMonitorTopContributors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/paginators/#getqueryresultsmonitortopcontributorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetQueryResultsMonitorTopContributorsInputPaginateTypeDef]
    ) -> PageIterator[GetQueryResultsMonitorTopContributorsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/paginator/GetQueryResultsMonitorTopContributors.html#NetworkFlowMonitor.Paginator.GetQueryResultsMonitorTopContributors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/paginators/#getqueryresultsmonitortopcontributorspaginator)
        """

if TYPE_CHECKING:
    _GetQueryResultsWorkloadInsightsTopContributorsDataPaginatorBase = Paginator[
        GetQueryResultsWorkloadInsightsTopContributorsDataOutputTypeDef
    ]
else:
    _GetQueryResultsWorkloadInsightsTopContributorsDataPaginatorBase = Paginator  # type: ignore[assignment]

class GetQueryResultsWorkloadInsightsTopContributorsDataPaginator(
    _GetQueryResultsWorkloadInsightsTopContributorsDataPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/paginator/GetQueryResultsWorkloadInsightsTopContributorsData.html#NetworkFlowMonitor.Paginator.GetQueryResultsWorkloadInsightsTopContributorsData)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/paginators/#getqueryresultsworkloadinsightstopcontributorsdatapaginator)
    """
    def paginate(  # type: ignore[override]
        self,
        **kwargs: Unpack[GetQueryResultsWorkloadInsightsTopContributorsDataInputPaginateTypeDef],
    ) -> PageIterator[GetQueryResultsWorkloadInsightsTopContributorsDataOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/paginator/GetQueryResultsWorkloadInsightsTopContributorsData.html#NetworkFlowMonitor.Paginator.GetQueryResultsWorkloadInsightsTopContributorsData.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/paginators/#getqueryresultsworkloadinsightstopcontributorsdatapaginator)
        """

if TYPE_CHECKING:
    _GetQueryResultsWorkloadInsightsTopContributorsPaginatorBase = Paginator[
        GetQueryResultsWorkloadInsightsTopContributorsOutputTypeDef
    ]
else:
    _GetQueryResultsWorkloadInsightsTopContributorsPaginatorBase = Paginator  # type: ignore[assignment]

class GetQueryResultsWorkloadInsightsTopContributorsPaginator(
    _GetQueryResultsWorkloadInsightsTopContributorsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/paginator/GetQueryResultsWorkloadInsightsTopContributors.html#NetworkFlowMonitor.Paginator.GetQueryResultsWorkloadInsightsTopContributors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/paginators/#getqueryresultsworkloadinsightstopcontributorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetQueryResultsWorkloadInsightsTopContributorsInputPaginateTypeDef]
    ) -> PageIterator[GetQueryResultsWorkloadInsightsTopContributorsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/paginator/GetQueryResultsWorkloadInsightsTopContributors.html#NetworkFlowMonitor.Paginator.GetQueryResultsWorkloadInsightsTopContributors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/paginators/#getqueryresultsworkloadinsightstopcontributorspaginator)
        """

if TYPE_CHECKING:
    _ListMonitorsPaginatorBase = Paginator[ListMonitorsOutputTypeDef]
else:
    _ListMonitorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMonitorsPaginator(_ListMonitorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/paginator/ListMonitors.html#NetworkFlowMonitor.Paginator.ListMonitors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/paginators/#listmonitorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMonitorsInputPaginateTypeDef]
    ) -> PageIterator[ListMonitorsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/paginator/ListMonitors.html#NetworkFlowMonitor.Paginator.ListMonitors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/paginators/#listmonitorspaginator)
        """

if TYPE_CHECKING:
    _ListScopesPaginatorBase = Paginator[ListScopesOutputTypeDef]
else:
    _ListScopesPaginatorBase = Paginator  # type: ignore[assignment]

class ListScopesPaginator(_ListScopesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/paginator/ListScopes.html#NetworkFlowMonitor.Paginator.ListScopes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/paginators/#listscopespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListScopesInputPaginateTypeDef]
    ) -> PageIterator[ListScopesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/paginator/ListScopes.html#NetworkFlowMonitor.Paginator.ListScopes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/paginators/#listscopespaginator)
        """
