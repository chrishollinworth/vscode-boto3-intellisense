"""
Type annotations for networkflowmonitor service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_networkflowmonitor.client import NetworkFlowMonitorClient

    session = Session()
    client: NetworkFlowMonitorClient = session.client("networkflowmonitor")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    GetQueryResultsMonitorTopContributorsPaginator,
    GetQueryResultsWorkloadInsightsTopContributorsDataPaginator,
    GetQueryResultsWorkloadInsightsTopContributorsPaginator,
    ListMonitorsPaginator,
    ListScopesPaginator,
)
from .type_defs import (
    CreateMonitorInputTypeDef,
    CreateMonitorOutputTypeDef,
    CreateScopeInputTypeDef,
    CreateScopeOutputTypeDef,
    DeleteMonitorInputTypeDef,
    DeleteScopeInputTypeDef,
    GetMonitorInputTypeDef,
    GetMonitorOutputTypeDef,
    GetQueryResultsMonitorTopContributorsInputTypeDef,
    GetQueryResultsMonitorTopContributorsOutputTypeDef,
    GetQueryResultsWorkloadInsightsTopContributorsDataInputTypeDef,
    GetQueryResultsWorkloadInsightsTopContributorsDataOutputTypeDef,
    GetQueryResultsWorkloadInsightsTopContributorsInputTypeDef,
    GetQueryResultsWorkloadInsightsTopContributorsOutputTypeDef,
    GetQueryStatusMonitorTopContributorsInputTypeDef,
    GetQueryStatusMonitorTopContributorsOutputTypeDef,
    GetQueryStatusWorkloadInsightsTopContributorsDataInputTypeDef,
    GetQueryStatusWorkloadInsightsTopContributorsDataOutputTypeDef,
    GetQueryStatusWorkloadInsightsTopContributorsInputTypeDef,
    GetQueryStatusWorkloadInsightsTopContributorsOutputTypeDef,
    GetScopeInputTypeDef,
    GetScopeOutputTypeDef,
    ListMonitorsInputTypeDef,
    ListMonitorsOutputTypeDef,
    ListScopesInputTypeDef,
    ListScopesOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    StartQueryMonitorTopContributorsInputTypeDef,
    StartQueryMonitorTopContributorsOutputTypeDef,
    StartQueryWorkloadInsightsTopContributorsDataInputTypeDef,
    StartQueryWorkloadInsightsTopContributorsDataOutputTypeDef,
    StartQueryWorkloadInsightsTopContributorsInputTypeDef,
    StartQueryWorkloadInsightsTopContributorsOutputTypeDef,
    StopQueryMonitorTopContributorsInputTypeDef,
    StopQueryWorkloadInsightsTopContributorsDataInputTypeDef,
    StopQueryWorkloadInsightsTopContributorsInputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateMonitorInputTypeDef,
    UpdateMonitorOutputTypeDef,
    UpdateScopeInputTypeDef,
    UpdateScopeOutputTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("NetworkFlowMonitorClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class NetworkFlowMonitorClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor.html#NetworkFlowMonitor.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        NetworkFlowMonitorClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor.html#NetworkFlowMonitor.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#generate_presigned_url)
        """

    def create_monitor(
        self, **kwargs: Unpack[CreateMonitorInputTypeDef]
    ) -> CreateMonitorOutputTypeDef:
        """
        Create a monitor for specific network flows between local and remote resources,
        so that you can monitor network performance for one or several of your
        workloads.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/create_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#create_monitor)
        """

    def create_scope(self, **kwargs: Unpack[CreateScopeInputTypeDef]) -> CreateScopeOutputTypeDef:
        """
        Create a scope of resources that you want to be available for Network Flow
        Monitor to generate metrics for, when you have active agents on those resources
        sending metrics reports to the Network Flow Monitor backend.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/create_scope.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#create_scope)
        """

    def delete_monitor(self, **kwargs: Unpack[DeleteMonitorInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes a monitor in Network Flow Monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/delete_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#delete_monitor)
        """

    def delete_scope(self, **kwargs: Unpack[DeleteScopeInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes a scope that has been defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/delete_scope.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#delete_scope)
        """

    def get_monitor(self, **kwargs: Unpack[GetMonitorInputTypeDef]) -> GetMonitorOutputTypeDef:
        """
        Gets information about a monitor in Network Flow Monitor based on a monitor
        name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/get_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#get_monitor)
        """

    def get_query_results_monitor_top_contributors(
        self, **kwargs: Unpack[GetQueryResultsMonitorTopContributorsInputTypeDef]
    ) -> GetQueryResultsMonitorTopContributorsOutputTypeDef:
        """
        Return the data for a query with the Network Flow Monitor query interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/get_query_results_monitor_top_contributors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#get_query_results_monitor_top_contributors)
        """

    def get_query_results_workload_insights_top_contributors(
        self, **kwargs: Unpack[GetQueryResultsWorkloadInsightsTopContributorsInputTypeDef]
    ) -> GetQueryResultsWorkloadInsightsTopContributorsOutputTypeDef:
        """
        Return the data for a query with the Network Flow Monitor query interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/get_query_results_workload_insights_top_contributors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#get_query_results_workload_insights_top_contributors)
        """

    def get_query_results_workload_insights_top_contributors_data(
        self, **kwargs: Unpack[GetQueryResultsWorkloadInsightsTopContributorsDataInputTypeDef]
    ) -> GetQueryResultsWorkloadInsightsTopContributorsDataOutputTypeDef:
        """
        Return the data for a query with the Network Flow Monitor query interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/get_query_results_workload_insights_top_contributors_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#get_query_results_workload_insights_top_contributors_data)
        """

    def get_query_status_monitor_top_contributors(
        self, **kwargs: Unpack[GetQueryStatusMonitorTopContributorsInputTypeDef]
    ) -> GetQueryStatusMonitorTopContributorsOutputTypeDef:
        """
        Returns the current status of a query for the Network Flow Monitor query
        interface, for a specified query ID and monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/get_query_status_monitor_top_contributors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#get_query_status_monitor_top_contributors)
        """

    def get_query_status_workload_insights_top_contributors(
        self, **kwargs: Unpack[GetQueryStatusWorkloadInsightsTopContributorsInputTypeDef]
    ) -> GetQueryStatusWorkloadInsightsTopContributorsOutputTypeDef:
        """
        Return the data for a query with the Network Flow Monitor query interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/get_query_status_workload_insights_top_contributors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#get_query_status_workload_insights_top_contributors)
        """

    def get_query_status_workload_insights_top_contributors_data(
        self, **kwargs: Unpack[GetQueryStatusWorkloadInsightsTopContributorsDataInputTypeDef]
    ) -> GetQueryStatusWorkloadInsightsTopContributorsDataOutputTypeDef:
        """
        Returns the current status of a query for the Network Flow Monitor query
        interface, for a specified query ID and monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/get_query_status_workload_insights_top_contributors_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#get_query_status_workload_insights_top_contributors_data)
        """

    def get_scope(self, **kwargs: Unpack[GetScopeInputTypeDef]) -> GetScopeOutputTypeDef:
        """
        Gets information about a scope, including the name, status, tags, and target
        details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/get_scope.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#get_scope)
        """

    def list_monitors(
        self, **kwargs: Unpack[ListMonitorsInputTypeDef]
    ) -> ListMonitorsOutputTypeDef:
        """
        List all monitors in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/list_monitors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#list_monitors)
        """

    def list_scopes(self, **kwargs: Unpack[ListScopesInputTypeDef]) -> ListScopesOutputTypeDef:
        """
        List all the scopes for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/list_scopes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#list_scopes)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Returns all the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#list_tags_for_resource)
        """

    def start_query_monitor_top_contributors(
        self, **kwargs: Unpack[StartQueryMonitorTopContributorsInputTypeDef]
    ) -> StartQueryMonitorTopContributorsOutputTypeDef:
        """
        Start a query to return the data with the Network Flow Monitor query interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/start_query_monitor_top_contributors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#start_query_monitor_top_contributors)
        """

    def start_query_workload_insights_top_contributors(
        self, **kwargs: Unpack[StartQueryWorkloadInsightsTopContributorsInputTypeDef]
    ) -> StartQueryWorkloadInsightsTopContributorsOutputTypeDef:
        """
        Start a query to return the data with the Network Flow Monitor query interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/start_query_workload_insights_top_contributors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#start_query_workload_insights_top_contributors)
        """

    def start_query_workload_insights_top_contributors_data(
        self, **kwargs: Unpack[StartQueryWorkloadInsightsTopContributorsDataInputTypeDef]
    ) -> StartQueryWorkloadInsightsTopContributorsDataOutputTypeDef:
        """
        Start a query to return the with the Network Flow Monitor query interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/start_query_workload_insights_top_contributors_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#start_query_workload_insights_top_contributors_data)
        """

    def stop_query_monitor_top_contributors(
        self, **kwargs: Unpack[StopQueryMonitorTopContributorsInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Stop a query with the Network Flow Monitor query interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/stop_query_monitor_top_contributors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#stop_query_monitor_top_contributors)
        """

    def stop_query_workload_insights_top_contributors(
        self, **kwargs: Unpack[StopQueryWorkloadInsightsTopContributorsInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Stop a query with the Network Flow Monitor query interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/stop_query_workload_insights_top_contributors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#stop_query_workload_insights_top_contributors)
        """

    def stop_query_workload_insights_top_contributors_data(
        self, **kwargs: Unpack[StopQueryWorkloadInsightsTopContributorsDataInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Return the data for a query with the Network Flow Monitor query interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/stop_query_workload_insights_top_contributors_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#stop_query_workload_insights_top_contributors_data)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Adds a tag to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Removes a tag from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#untag_resource)
        """

    def update_monitor(
        self, **kwargs: Unpack[UpdateMonitorInputTypeDef]
    ) -> UpdateMonitorOutputTypeDef:
        """
        Update a monitor to add or remove local or remote resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/update_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#update_monitor)
        """

    def update_scope(self, **kwargs: Unpack[UpdateScopeInputTypeDef]) -> UpdateScopeOutputTypeDef:
        """
        Update a scope to add or remove resources that you want to be available for
        Network Flow Monitor to generate metrics for, when you have active agents on
        those resources sending metrics reports to the Network Flow Monitor backend.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/update_scope.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#update_scope)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_query_results_monitor_top_contributors"]
    ) -> GetQueryResultsMonitorTopContributorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_query_results_workload_insights_top_contributors_data"]
    ) -> GetQueryResultsWorkloadInsightsTopContributorsDataPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_query_results_workload_insights_top_contributors"]
    ) -> GetQueryResultsWorkloadInsightsTopContributorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_monitors"]
    ) -> ListMonitorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_scopes"]
    ) -> ListScopesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkflowmonitor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/client/#get_paginator)
        """
