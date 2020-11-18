# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for braket service client

Usage::

    ```python
    import boto3
    from mypy_boto3_braket import BraketClient

    client: BraketClient = boto3.client("braket")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_braket.paginator import SearchDevicesPaginator, SearchQuantumTasksPaginator
from mypy_boto3_braket.type_defs import (
    CancelQuantumTaskResponseTypeDef,
    CreateQuantumTaskResponseTypeDef,
    GetDeviceResponseTypeDef,
    GetQuantumTaskResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    SearchDevicesFilterTypeDef,
    SearchDevicesResponseTypeDef,
    SearchQuantumTasksFilterTypeDef,
    SearchQuantumTasksResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("BraketClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DeviceOfflineException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class BraketClient:
    """
    [Braket.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/braket.html#Braket.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/braket.html#Braket.Client.can_paginate)
        """

    def cancel_quantum_task(
        self, clientToken: str, quantumTaskArn: str
    ) -> CancelQuantumTaskResponseTypeDef:
        """
        [Client.cancel_quantum_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/braket.html#Braket.Client.cancel_quantum_task)
        """

    def create_quantum_task(
        self,
        action: str,
        clientToken: str,
        deviceArn: str,
        outputS3Bucket: str,
        outputS3KeyPrefix: str,
        shots: int,
        deviceParameters: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateQuantumTaskResponseTypeDef:
        """
        [Client.create_quantum_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/braket.html#Braket.Client.create_quantum_task)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/braket.html#Braket.Client.generate_presigned_url)
        """

    def get_device(self, deviceArn: str) -> GetDeviceResponseTypeDef:
        """
        [Client.get_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/braket.html#Braket.Client.get_device)
        """

    def get_quantum_task(self, quantumTaskArn: str) -> GetQuantumTaskResponseTypeDef:
        """
        [Client.get_quantum_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/braket.html#Braket.Client.get_quantum_task)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/braket.html#Braket.Client.list_tags_for_resource)
        """

    def search_devices(
        self,
        filters: List[SearchDevicesFilterTypeDef],
        maxResults: int = None,
        nextToken: str = None,
    ) -> SearchDevicesResponseTypeDef:
        """
        [Client.search_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/braket.html#Braket.Client.search_devices)
        """

    def search_quantum_tasks(
        self,
        filters: List[SearchQuantumTasksFilterTypeDef],
        maxResults: int = None,
        nextToken: str = None,
    ) -> SearchQuantumTasksResponseTypeDef:
        """
        [Client.search_quantum_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/braket.html#Braket.Client.search_quantum_tasks)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/braket.html#Braket.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/braket.html#Braket.Client.untag_resource)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_devices"]) -> SearchDevicesPaginator:
        """
        [Paginator.SearchDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/braket.html#Braket.Paginator.SearchDevices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_quantum_tasks"]
    ) -> SearchQuantumTasksPaginator:
        """
        [Paginator.SearchQuantumTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/braket.html#Braket.Paginator.SearchQuantumTasks)
        """
