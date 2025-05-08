"""
Type annotations for networkmonitor service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_networkmonitor.client import CloudWatchNetworkMonitorClient

    session = Session()
    client: CloudWatchNetworkMonitorClient = session.client("networkmonitor")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListMonitorsPaginator
from .type_defs import (
    CreateMonitorInputTypeDef,
    CreateMonitorOutputTypeDef,
    CreateProbeInputTypeDef,
    CreateProbeOutputTypeDef,
    DeleteMonitorInputTypeDef,
    DeleteProbeInputTypeDef,
    GetMonitorInputTypeDef,
    GetMonitorOutputTypeDef,
    GetProbeInputTypeDef,
    GetProbeOutputTypeDef,
    ListMonitorsInputTypeDef,
    ListMonitorsOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateMonitorInputTypeDef,
    UpdateMonitorOutputTypeDef,
    UpdateProbeInputTypeDef,
    UpdateProbeOutputTypeDef,
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

__all__ = ("CloudWatchNetworkMonitorClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudWatchNetworkMonitorClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#generate_presigned_url)
        """

    def create_monitor(
        self, **kwargs: Unpack[CreateMonitorInputTypeDef]
    ) -> CreateMonitorOutputTypeDef:
        """
        Creates a monitor between a source subnet and destination IP address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor/client/create_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#create_monitor)
        """

    def create_probe(self, **kwargs: Unpack[CreateProbeInputTypeDef]) -> CreateProbeOutputTypeDef:
        """
        Create a probe within a monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor/client/create_probe.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#create_probe)
        """

    def delete_monitor(self, **kwargs: Unpack[DeleteMonitorInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes a specified monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor/client/delete_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#delete_monitor)
        """

    def delete_probe(self, **kwargs: Unpack[DeleteProbeInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified probe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor/client/delete_probe.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#delete_probe)
        """

    def get_monitor(self, **kwargs: Unpack[GetMonitorInputTypeDef]) -> GetMonitorOutputTypeDef:
        """
        Returns details about a specific monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor/client/get_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#get_monitor)
        """

    def get_probe(self, **kwargs: Unpack[GetProbeInputTypeDef]) -> GetProbeOutputTypeDef:
        """
        Returns the details about a probe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor/client/get_probe.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#get_probe)
        """

    def list_monitors(
        self, **kwargs: Unpack[ListMonitorsInputTypeDef]
    ) -> ListMonitorsOutputTypeDef:
        """
        Returns a list of all of your monitors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor/client/list_monitors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#list_monitors)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Lists the tags assigned to this resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#list_tags_for_resource)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Adds key-value pairs to a monitor or probe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Removes a key-value pair from a monitor or probe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#untag_resource)
        """

    def update_monitor(
        self, **kwargs: Unpack[UpdateMonitorInputTypeDef]
    ) -> UpdateMonitorOutputTypeDef:
        """
        Updates the <code>aggregationPeriod</code> for a monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor/client/update_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#update_monitor)
        """

    def update_probe(self, **kwargs: Unpack[UpdateProbeInputTypeDef]) -> UpdateProbeOutputTypeDef:
        """
        Updates a monitor probe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor/client/update_probe.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#update_probe)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_monitors"]
    ) -> ListMonitorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#get_paginator)
        """
