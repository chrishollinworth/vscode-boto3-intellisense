"""
Main interface for sagemaker-edge service client

Usage::

    ```python
    import boto3
    from mypy_boto3_sagemaker_edge import SagemakerEdgeManagerClient

    client: SagemakerEdgeManagerClient = boto3.client("sagemaker-edge")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_sagemaker_edge.type_defs import (
    EdgeMetricTypeDef,
    GetDeviceRegistrationResultTypeDef,
    ModelTypeDef,
)

__all__ = ("SagemakerEdgeManagerClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]


class SagemakerEdgeManagerClient:
    """
    [SagemakerEdgeManager.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client.generate_presigned_url)
        """

    def get_device_registration(
        self, DeviceName: str, DeviceFleetName: str
    ) -> GetDeviceRegistrationResultTypeDef:
        """
        [Client.get_device_registration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client.get_device_registration)
        """

    def send_heartbeat(
        self,
        AgentVersion: str,
        DeviceName: str,
        DeviceFleetName: str,
        AgentMetrics: List["EdgeMetricTypeDef"] = None,
        Models: List[ModelTypeDef] = None,
    ) -> None:
        """
        [Client.send_heartbeat documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client.send_heartbeat)
        """
