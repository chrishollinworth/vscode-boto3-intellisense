"""
Type annotations for sagemaker-edge service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_sagemaker_edge import SagemakerEdgeManagerClient

    client: SagemakerEdgeManagerClient = boto3.client("sagemaker-edge")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import EdgeMetricTypeDef, GetDeviceRegistrationResultTypeDef, ModelTypeDef

__all__ = ("SagemakerEdgeManagerClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]

class SagemakerEdgeManagerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        SagemakerEdgeManagerClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client.html#can_paginate)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client.html#generate_presigned_url)
        """
    def get_device_registration(
        self, *, DeviceName: str, DeviceFleetName: str
    ) -> GetDeviceRegistrationResultTypeDef:
        """
        Use to check if a device is registered with SageMaker Edge Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client.get_device_registration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client.html#get_device_registration)
        """
    def send_heartbeat(
        self,
        *,
        AgentVersion: str,
        DeviceName: str,
        DeviceFleetName: str,
        AgentMetrics: List["EdgeMetricTypeDef"] = None,
        Models: List["ModelTypeDef"] = None
    ) -> None:
        """
        Use to get the current status of devices registered on SageMaker Edge Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client.send_heartbeat)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client.html#send_heartbeat)
        """
