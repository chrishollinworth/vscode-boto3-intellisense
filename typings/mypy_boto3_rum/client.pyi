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

from .paginator import GetAppMonitorDataPaginator, ListAppMonitorsPaginator
from .type_defs import (
    AppMonitorConfigurationTypeDef,
    AppMonitorDetailsTypeDef,
    CreateAppMonitorResponseTypeDef,
    GetAppMonitorDataResponseTypeDef,
    GetAppMonitorResponseTypeDef,
    ListAppMonitorsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/rum.html#CloudWatchRUM.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        CloudWatchRUMClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/rum.html#CloudWatchRUM.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#can_paginate)
        """
    def create_app_monitor(
        self,
        *,
        Domain: str,
        Name: str,
        AppMonitorConfiguration: "AppMonitorConfigurationTypeDef" = None,
        CwLogEnabled: bool = None,
        Tags: Dict[str, str] = None
    ) -> CreateAppMonitorResponseTypeDef:
        """
        Creates a Amazon CloudWatch RUM app monitor, which collects telemetry data from
        your application and sends that data to RUM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/rum.html#CloudWatchRUM.Client.create_app_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#create_app_monitor)
        """
    def delete_app_monitor(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes an existing app monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/rum.html#CloudWatchRUM.Client.delete_app_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#delete_app_monitor)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/rum.html#CloudWatchRUM.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#generate_presigned_url)
        """
    def get_app_monitor(self, *, Name: str) -> GetAppMonitorResponseTypeDef:
        """
        Retrieves the complete configuration information for one app monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/rum.html#CloudWatchRUM.Client.get_app_monitor)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/rum.html#CloudWatchRUM.Client.get_app_monitor_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#get_app_monitor_data)
        """
    def list_app_monitors(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListAppMonitorsResponseTypeDef:
        """
        Returns a list of the Amazon CloudWatch RUM app monitors in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/rum.html#CloudWatchRUM.Client.list_app_monitors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#list_app_monitors)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Displays the tags associated with a CloudWatch RUM resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/rum.html#CloudWatchRUM.Client.list_tags_for_resource)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/rum.html#CloudWatchRUM.Client.put_rum_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#put_rum_events)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified CloudWatch RUM
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/rum.html#CloudWatchRUM.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/rum.html#CloudWatchRUM.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#untag_resource)
        """
    def update_app_monitor(
        self,
        *,
        Name: str,
        AppMonitorConfiguration: "AppMonitorConfigurationTypeDef" = None,
        CwLogEnabled: bool = None,
        Domain: str = None
    ) -> Dict[str, Any]:
        """
        Updates the configuration of an existing app monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/rum.html#CloudWatchRUM.Client.update_app_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/client.html#update_app_monitor)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_app_monitor_data"]
    ) -> GetAppMonitorDataPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/rum.html#CloudWatchRUM.Paginator.GetAppMonitorData)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators.html#getappmonitordatapaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_app_monitors"]
    ) -> ListAppMonitorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/rum.html#CloudWatchRUM.Paginator.ListAppMonitors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators.html#listappmonitorspaginator)
        """
