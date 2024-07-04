"""
Type annotations for networkmonitor service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_networkmonitor import CloudWatchNetworkMonitorClient

    client: CloudWatchNetworkMonitorClient = boto3.client("networkmonitor")
    ```
"""

import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import ProbeStateType, ProtocolType
from .paginator import ListMonitorsPaginator
from .type_defs import (
    CreateMonitorOutputTypeDef,
    CreateMonitorProbeInputTypeDef,
    CreateProbeOutputTypeDef,
    GetMonitorOutputTypeDef,
    GetProbeOutputTypeDef,
    ListMonitorsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ProbeInputTypeDef,
    UpdateMonitorOutputTypeDef,
    UpdateProbeOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CloudWatchNetworkMonitorClient",)

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

class CloudWatchNetworkMonitorClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudWatchNetworkMonitorClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client.html#close)
        """

    def create_monitor(
        self,
        *,
        monitorName: str,
        probes: List["CreateMonitorProbeInputTypeDef"] = None,
        aggregationPeriod: int = None,
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateMonitorOutputTypeDef:
        """
        Creates a monitor between a source subnet and destination IP address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.create_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client.html#create_monitor)
        """

    def create_probe(
        self,
        *,
        monitorName: str,
        probe: "ProbeInputTypeDef",
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateProbeOutputTypeDef:
        """
        Create a probe within a monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.create_probe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client.html#create_probe)
        """

    def delete_monitor(self, *, monitorName: str) -> Dict[str, Any]:
        """
        Deletes a specified monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.delete_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client.html#delete_monitor)
        """

    def delete_probe(self, *, monitorName: str, probeId: str) -> Dict[str, Any]:
        """
        Deletes the specified probe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.delete_probe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client.html#delete_probe)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client.html#generate_presigned_url)
        """

    def get_monitor(self, *, monitorName: str) -> GetMonitorOutputTypeDef:
        """
        Returns details about a specific monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.get_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client.html#get_monitor)
        """

    def get_probe(self, *, monitorName: str, probeId: str) -> GetProbeOutputTypeDef:
        """
        Returns the details about a probe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.get_probe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client.html#get_probe)
        """

    def list_monitors(
        self, *, nextToken: str = None, maxResults: int = None, state: str = None
    ) -> ListMonitorsOutputTypeDef:
        """
        Returns a list of all of your monitors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.list_monitors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client.html#list_monitors)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Lists the tags assigned to this resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client.html#list_tags_for_resource)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds key-value pairs to a monitor or probe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a key-value pair from a monitor or probe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client.html#untag_resource)
        """

    def update_monitor(
        self, *, monitorName: str, aggregationPeriod: int
    ) -> UpdateMonitorOutputTypeDef:
        """
        Updates the `aggregationPeriod` for a monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.update_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client.html#update_monitor)
        """

    def update_probe(
        self,
        *,
        monitorName: str,
        probeId: str,
        state: ProbeStateType = None,
        destination: str = None,
        destinationPort: int = None,
        protocol: ProtocolType = None,
        packetSize: int = None
    ) -> UpdateProbeOutputTypeDef:
        """
        Updates a monitor probe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.update_probe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client.html#update_probe)
        """

    def get_paginator(self, operation_name: Literal["list_monitors"]) -> ListMonitorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Paginator.ListMonitors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/paginators.html#listmonitorspaginator)
        """
