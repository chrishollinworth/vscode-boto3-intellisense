"""
Type annotations for rum service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_rum import CloudWatchRUMClient

    client: CloudWatchRUMClient = boto3.client("rum")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import MetricDestinationType
from .paginator import (
    BatchGetRumMetricDefinitionsPaginator,
    GetAppMonitorDataPaginator,
    ListAppMonitorsPaginator,
    ListRumMetricsDestinationsPaginator,
)
from .type_defs import (
    AppMonitorConfigurationTypeDef,
    AppMonitorDetailsTypeDef,
    BatchCreateRumMetricDefinitionsResponseTypeDef,
    BatchDeleteRumMetricDefinitionsResponseTypeDef,
    BatchGetRumMetricDefinitionsResponseTypeDef,
    CreateAppMonitorResponseTypeDef,
    CustomEventsTypeDef,
    GetAppMonitorDataResponseTypeDef,
    GetAppMonitorResponseTypeDef,
    ListAppMonitorsResponseTypeDef,
    ListRumMetricsDestinationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MetricDefinitionRequestTypeDef,
    QueryFilterTypeDef,
    RumEventTypeDef,
    TimeRangeTypeDef,
    UserDetailsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CloudWatchRUMClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CloudWatchRUMClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudWatchRUMClient exceptions.
        """
    def batch_create_rum_metric_definitions(
        self,
        *,
        AppMonitorName: str,
        Destination: MetricDestinationType,
        MetricDefinitions: List["MetricDefinitionRequestTypeDef"],
        DestinationArn: str = None
    ) -> BatchCreateRumMetricDefinitionsResponseTypeDef:
        """
        Specifies the extended metrics and custom metrics that you want a CloudWatch RUM
        app monitor to send to a destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.batch_create_rum_metric_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#batch_create_rum_metric_definitions)
        """
    def batch_delete_rum_metric_definitions(
        self,
        *,
        AppMonitorName: str,
        Destination: MetricDestinationType,
        MetricDefinitionIds: List[str],
        DestinationArn: str = None
    ) -> BatchDeleteRumMetricDefinitionsResponseTypeDef:
        """
        Removes the specified metrics from being sent to an extended metrics
        destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.batch_delete_rum_metric_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#batch_delete_rum_metric_definitions)
        """
    def batch_get_rum_metric_definitions(
        self,
        *,
        AppMonitorName: str,
        Destination: MetricDestinationType,
        DestinationArn: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> BatchGetRumMetricDefinitionsResponseTypeDef:
        """
        Retrieves the list of metrics and dimensions that a RUM app monitor is sending
        to a single destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.batch_get_rum_metric_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#batch_get_rum_metric_definitions)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#close)
        """
    def create_app_monitor(
        self,
        *,
        Domain: str,
        Name: str,
        AppMonitorConfiguration: "AppMonitorConfigurationTypeDef" = None,
        CustomEvents: "CustomEventsTypeDef" = None,
        CwLogEnabled: bool = None,
        Tags: Dict[str, str] = None
    ) -> CreateAppMonitorResponseTypeDef:
        """
        Creates a Amazon CloudWatch RUM app monitor, which collects telemetry data from
        your application and sends that data to RUM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.create_app_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#create_app_monitor)
        """
    def delete_app_monitor(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes an existing app monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.delete_app_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#delete_app_monitor)
        """
    def delete_rum_metrics_destination(
        self, *, AppMonitorName: str, Destination: MetricDestinationType, DestinationArn: str = None
    ) -> Dict[str, Any]:
        """
        Deletes a destination for CloudWatch RUM extended metrics, so that the specified
        app monitor stops sending extended metrics to that destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.delete_rum_metrics_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#delete_rum_metrics_destination)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#generate_presigned_url)
        """
    def get_app_monitor(self, *, Name: str) -> GetAppMonitorResponseTypeDef:
        """
        Retrieves the complete configuration information for one app monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.get_app_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#get_app_monitor)
        """
    def get_app_monitor_data(
        self,
        *,
        Name: str,
        TimeRange: "TimeRangeTypeDef",
        Filters: List["QueryFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetAppMonitorDataResponseTypeDef:
        """
        Retrieves the raw performance events that RUM has collected from your web
        application, so that you can do your own processing or analysis of this data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.get_app_monitor_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#get_app_monitor_data)
        """
    def list_app_monitors(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListAppMonitorsResponseTypeDef:
        """
        Returns a list of the Amazon CloudWatch RUM app monitors in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.list_app_monitors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#list_app_monitors)
        """
    def list_rum_metrics_destinations(
        self, *, AppMonitorName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListRumMetricsDestinationsResponseTypeDef:
        """
        Returns a list of destinations that you have created to receive RUM extended
        metrics, for the specified app monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.list_rum_metrics_destinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#list_rum_metrics_destinations)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Displays the tags associated with a CloudWatch RUM resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#list_tags_for_resource)
        """
    def put_rum_events(
        self,
        *,
        AppMonitorDetails: "AppMonitorDetailsTypeDef",
        BatchId: str,
        Id: str,
        RumEvents: List["RumEventTypeDef"],
        UserDetails: "UserDetailsTypeDef"
    ) -> Dict[str, Any]:
        """
        Sends telemetry events about your application performance and user behavior to
        CloudWatch RUM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.put_rum_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#put_rum_events)
        """
    def put_rum_metrics_destination(
        self,
        *,
        AppMonitorName: str,
        Destination: MetricDestinationType,
        DestinationArn: str = None,
        IamRoleArn: str = None
    ) -> Dict[str, Any]:
        """
        Creates or updates a destination to receive extended metrics from CloudWatch
        RUM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.put_rum_metrics_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#put_rum_metrics_destination)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified CloudWatch RUM
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#untag_resource)
        """
    def update_app_monitor(
        self,
        *,
        Name: str,
        AppMonitorConfiguration: "AppMonitorConfigurationTypeDef" = None,
        CustomEvents: "CustomEventsTypeDef" = None,
        CwLogEnabled: bool = None,
        Domain: str = None
    ) -> Dict[str, Any]:
        """
        Updates the configuration of an existing app monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.update_app_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#update_app_monitor)
        """
    def update_rum_metric_definition(
        self,
        *,
        AppMonitorName: str,
        Destination: MetricDestinationType,
        MetricDefinition: "MetricDefinitionRequestTypeDef",
        MetricDefinitionId: str,
        DestinationArn: str = None
    ) -> Dict[str, Any]:
        """
        Modifies one existing metric definition for CloudWatch RUM extended metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Client.update_rum_metric_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#update_rum_metric_definition)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["batch_get_rum_metric_definitions"]
    ) -> BatchGetRumMetricDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Paginator.BatchGetRumMetricDefinitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators.html#batchgetrummetricdefinitionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_app_monitor_data"]
    ) -> GetAppMonitorDataPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Paginator.GetAppMonitorData)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators.html#getappmonitordatapaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_app_monitors"]
    ) -> ListAppMonitorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Paginator.ListAppMonitors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators.html#listappmonitorspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_rum_metrics_destinations"]
    ) -> ListRumMetricsDestinationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rum.html#CloudWatchRUM.Paginator.ListRumMetricsDestinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators.html#listrummetricsdestinationspaginator)
        """
