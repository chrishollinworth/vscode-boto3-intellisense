"""
Main interface for amp service client

Usage::

    ```python
    import boto3
    from mypy_boto3_amp import PrometheusServiceClient

    client: PrometheusServiceClient = boto3.client("amp")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from mypy_boto3_amp.paginator import ListWorkspacesPaginator
from mypy_boto3_amp.type_defs import (
    CreateWorkspaceResponseTypeDef,
    DescribeWorkspaceResponseTypeDef,
    ListWorkspacesResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("PrometheusServiceClient",)


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


class PrometheusServiceClient:
    """
    [PrometheusService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/amp.html#PrometheusService.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/amp.html#PrometheusService.Client.can_paginate)
        """

    def create_workspace(
        self, alias: str = None, clientToken: str = None
    ) -> CreateWorkspaceResponseTypeDef:
        """
        [Client.create_workspace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/amp.html#PrometheusService.Client.create_workspace)
        """

    def delete_workspace(self, workspaceId: str, clientToken: str = None) -> None:
        """
        [Client.delete_workspace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/amp.html#PrometheusService.Client.delete_workspace)
        """

    def describe_workspace(self, workspaceId: str) -> DescribeWorkspaceResponseTypeDef:
        """
        [Client.describe_workspace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/amp.html#PrometheusService.Client.describe_workspace)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/amp.html#PrometheusService.Client.generate_presigned_url)
        """

    def list_workspaces(
        self, alias: str = None, maxResults: int = None, nextToken: str = None
    ) -> ListWorkspacesResponseTypeDef:
        """
        [Client.list_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/amp.html#PrometheusService.Client.list_workspaces)
        """

    def update_workspace_alias(
        self, workspaceId: str, alias: str = None, clientToken: str = None
    ) -> None:
        """
        [Client.update_workspace_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/amp.html#PrometheusService.Client.update_workspace_alias)
        """

    def get_paginator(self, operation_name: Literal["list_workspaces"]) -> ListWorkspacesPaginator:
        """
        [Paginator.ListWorkspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/amp.html#PrometheusService.Paginator.ListWorkspaces)
        """
