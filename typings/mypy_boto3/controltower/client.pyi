"""
Type annotations for controltower service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_controltower import ControlTowerClient

    client: ControlTowerClient = boto3.client("controltower")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .paginator import ListEnabledControlsPaginator
from .type_defs import (
    DisableControlOutputTypeDef,
    EnableControlOutputTypeDef,
    GetControlOperationOutputTypeDef,
    ListEnabledControlsOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ControlTowerClient",)

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

class ControlTowerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/controltower.html#ControlTower.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ControlTowerClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/controltower.html#ControlTower.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/controltower.html#ControlTower.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#close)
        """
    def disable_control(
        self, *, controlIdentifier: str, targetIdentifier: str
    ) -> DisableControlOutputTypeDef:
        """
        This API call turns off a control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/controltower.html#ControlTower.Client.disable_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#disable_control)
        """
    def enable_control(
        self, *, controlIdentifier: str, targetIdentifier: str
    ) -> EnableControlOutputTypeDef:
        """
        This API call activates a control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/controltower.html#ControlTower.Client.enable_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#enable_control)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/controltower.html#ControlTower.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#generate_presigned_url)
        """
    def get_control_operation(
        self, *, operationIdentifier: str
    ) -> GetControlOperationOutputTypeDef:
        """
        Returns the status of a particular `EnableControl` or `DisableControl`
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/controltower.html#ControlTower.Client.get_control_operation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#get_control_operation)
        """
    def list_enabled_controls(
        self, *, targetIdentifier: str, maxResults: int = None, nextToken: str = None
    ) -> ListEnabledControlsOutputTypeDef:
        """
        Lists the controls enabled by AWS Control Tower on the specified organizational
        unit and the accounts it contains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/controltower.html#ControlTower.Client.list_enabled_controls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#list_enabled_controls)
        """
    def get_paginator(
        self, operation_name: Literal["list_enabled_controls"]
    ) -> ListEnabledControlsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/controltower.html#ControlTower.Paginator.ListEnabledControls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html#listenabledcontrolspaginator)
        """
