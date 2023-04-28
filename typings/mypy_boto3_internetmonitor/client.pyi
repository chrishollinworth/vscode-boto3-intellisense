"""
Type annotations for internetmonitor service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_internetmonitor import CloudWatchInternetMonitorClient

    client: CloudWatchInternetMonitorClient = boto3.client("internetmonitor")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import HealthEventStatusType, MonitorConfigStateType
from .paginator import ListHealthEventsPaginator, ListMonitorsPaginator
from .type_defs import (
    CreateMonitorOutputTypeDef,
    GetHealthEventOutputTypeDef,
    GetMonitorOutputTypeDef,
    InternetMeasurementsLogDeliveryTypeDef,
    ListHealthEventsOutputTypeDef,
    ListMonitorsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    UpdateMonitorOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CloudWatchInternetMonitorClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudWatchInternetMonitorClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client.html#close)
        """
    def create_monitor(
        self,
        *,
        MonitorName: str,
        Resources: List[str] = None,
        ClientToken: str = None,
        Tags: Dict[str, str] = None,
        MaxCityNetworksToMonitor: int = None,
        InternetMeasurementsLogDelivery: "InternetMeasurementsLogDeliveryTypeDef" = None,
        TrafficPercentageToMonitor: int = None
    ) -> CreateMonitorOutputTypeDef:
        """
        Creates a monitor in Amazon CloudWatch Internet Monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Client.create_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client.html#create_monitor)
        """
    def delete_monitor(self, *, MonitorName: str) -> Dict[str, Any]:
        """
        Deletes a monitor in Amazon CloudWatch Internet Monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Client.delete_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client.html#delete_monitor)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client.html#generate_presigned_url)
        """
    def get_health_event(self, *, MonitorName: str, EventId: str) -> GetHealthEventOutputTypeDef:
        """
        Gets information the Amazon CloudWatch Internet Monitor has created and stored
        about a health event for a specified monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Client.get_health_event)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client.html#get_health_event)
        """
    def get_monitor(self, *, MonitorName: str) -> GetMonitorOutputTypeDef:
        """
        Gets information about a monitor in Amazon CloudWatch Internet Monitor based on
        a monitor name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Client.get_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client.html#get_monitor)
        """
    def list_health_events(
        self,
        *,
        MonitorName: str,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        EventStatus: HealthEventStatusType = None
    ) -> ListHealthEventsOutputTypeDef:
        """
        Lists all health events for a monitor in Amazon CloudWatch Internet Monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Client.list_health_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client.html#list_health_events)
        """
    def list_monitors(
        self, *, NextToken: str = None, MaxResults: int = None, MonitorStatus: str = None
    ) -> ListMonitorsOutputTypeDef:
        """
        Lists all of your monitors for Amazon CloudWatch Internet Monitor and their
        statuses, along with the Amazon Resource Name (ARN) and name of each monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Client.list_monitors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client.html#list_monitors)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Lists the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client.html#list_tags_for_resource)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds a tag to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client.html#untag_resource)
        """
    def update_monitor(
        self,
        *,
        MonitorName: str,
        ResourcesToAdd: List[str] = None,
        ResourcesToRemove: List[str] = None,
        Status: MonitorConfigStateType = None,
        ClientToken: str = None,
        MaxCityNetworksToMonitor: int = None,
        InternetMeasurementsLogDelivery: "InternetMeasurementsLogDeliveryTypeDef" = None,
        TrafficPercentageToMonitor: int = None
    ) -> UpdateMonitorOutputTypeDef:
        """
        Updates a monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Client.update_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/client.html#update_monitor)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_health_events"]
    ) -> ListHealthEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Paginator.ListHealthEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators.html#listhealtheventspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_monitors"]) -> ListMonitorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Paginator.ListMonitors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators.html#listmonitorspaginator)
        """
