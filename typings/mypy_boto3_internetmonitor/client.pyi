"""
Type annotations for internetmonitor service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_internetmonitor.client import CloudWatchInternetMonitorClient

    session = Session()
    client: CloudWatchInternetMonitorClient = session.client("internetmonitor")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListHealthEventsPaginator, ListInternetEventsPaginator, ListMonitorsPaginator
from .type_defs import (
    CreateMonitorInputTypeDef,
    CreateMonitorOutputTypeDef,
    DeleteMonitorInputTypeDef,
    GetHealthEventInputTypeDef,
    GetHealthEventOutputTypeDef,
    GetInternetEventInputTypeDef,
    GetInternetEventOutputTypeDef,
    GetMonitorInputTypeDef,
    GetMonitorOutputTypeDef,
    GetQueryResultsInputTypeDef,
    GetQueryResultsOutputTypeDef,
    GetQueryStatusInputTypeDef,
    GetQueryStatusOutputTypeDef,
    ListHealthEventsInputTypeDef,
    ListHealthEventsOutputTypeDef,
    ListInternetEventsInputTypeDef,
    ListInternetEventsOutputTypeDef,
    ListMonitorsInputTypeDef,
    ListMonitorsOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    StartQueryInputTypeDef,
    StartQueryOutputTypeDef,
    StopQueryInputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateMonitorInputTypeDef,
    UpdateMonitorOutputTypeDef,
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

__all__ = ("CloudWatchInternetMonitorClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CloudWatchInternetMonitorClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudWatchInternetMonitorClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#generate_presigned_url)
        """

    def create_monitor(
        self, **kwargs: Unpack[CreateMonitorInputTypeDef]
    ) -> CreateMonitorOutputTypeDef:
        """
        Creates a monitor in Amazon CloudWatch Internet Monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/create_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#create_monitor)
        """

    def delete_monitor(self, **kwargs: Unpack[DeleteMonitorInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes a monitor in Amazon CloudWatch Internet Monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/delete_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#delete_monitor)
        """

    def get_health_event(
        self, **kwargs: Unpack[GetHealthEventInputTypeDef]
    ) -> GetHealthEventOutputTypeDef:
        """
        Gets information that Amazon CloudWatch Internet Monitor has created and stored
        about a health event for a specified monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/get_health_event.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#get_health_event)
        """

    def get_internet_event(
        self, **kwargs: Unpack[GetInternetEventInputTypeDef]
    ) -> GetInternetEventOutputTypeDef:
        """
        Gets information that Amazon CloudWatch Internet Monitor has generated about an
        internet event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/get_internet_event.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#get_internet_event)
        """

    def get_monitor(self, **kwargs: Unpack[GetMonitorInputTypeDef]) -> GetMonitorOutputTypeDef:
        """
        Gets information about a monitor in Amazon CloudWatch Internet Monitor based on
        a monitor name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/get_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#get_monitor)
        """

    def get_query_results(
        self, **kwargs: Unpack[GetQueryResultsInputTypeDef]
    ) -> GetQueryResultsOutputTypeDef:
        """
        Return the data for a query with the Amazon CloudWatch Internet Monitor query
        interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/get_query_results.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#get_query_results)
        """

    def get_query_status(
        self, **kwargs: Unpack[GetQueryStatusInputTypeDef]
    ) -> GetQueryStatusOutputTypeDef:
        """
        Returns the current status of a query for the Amazon CloudWatch Internet
        Monitor query interface, for a specified query ID and monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/get_query_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#get_query_status)
        """

    def list_health_events(
        self, **kwargs: Unpack[ListHealthEventsInputTypeDef]
    ) -> ListHealthEventsOutputTypeDef:
        """
        Lists all health events for a monitor in Amazon CloudWatch Internet Monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/list_health_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#list_health_events)
        """

    def list_internet_events(
        self, **kwargs: Unpack[ListInternetEventsInputTypeDef]
    ) -> ListInternetEventsOutputTypeDef:
        """
        Lists internet events that cause performance or availability issues for client
        locations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/list_internet_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#list_internet_events)
        """

    def list_monitors(
        self, **kwargs: Unpack[ListMonitorsInputTypeDef]
    ) -> ListMonitorsOutputTypeDef:
        """
        Lists all of your monitors for Amazon CloudWatch Internet Monitor and their
        statuses, along with the Amazon Resource Name (ARN) and name of each monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/list_monitors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#list_monitors)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Lists the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#list_tags_for_resource)
        """

    def start_query(self, **kwargs: Unpack[StartQueryInputTypeDef]) -> StartQueryOutputTypeDef:
        """
        Start a query to return data for a specific query type for the Amazon
        CloudWatch Internet Monitor query interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/start_query.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#start_query)
        """

    def stop_query(self, **kwargs: Unpack[StopQueryInputTypeDef]) -> Dict[str, Any]:
        """
        Stop a query that is progress for a specific monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/stop_query.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#stop_query)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Adds a tag to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Removes a tag from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#untag_resource)
        """

    def update_monitor(
        self, **kwargs: Unpack[UpdateMonitorInputTypeDef]
    ) -> UpdateMonitorOutputTypeDef:
        """
        Updates a monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/update_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#update_monitor)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_health_events"]
    ) -> ListHealthEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_internet_events"]
    ) -> ListInternetEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_monitors"]
    ) -> ListMonitorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client/#get_paginator)
        """
