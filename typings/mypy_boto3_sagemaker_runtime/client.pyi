# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for sagemaker-runtime service client

Usage::

    ```python
    import boto3
    from mypy_boto3_sagemaker_runtime import SageMakerRuntimeClient

    client: SageMakerRuntimeClient = boto3.client("sagemaker-runtime")
    ```
"""
from typing import IO, Any, Dict, Type, Union

from botocore.client import ClientMeta

from mypy_boto3_sagemaker_runtime.type_defs import InvokeEndpointOutputTypeDef

__all__ = ("SageMakerRuntimeClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalFailure: Type[BotocoreClientError]
    ModelError: Type[BotocoreClientError]
    ServiceUnavailable: Type[BotocoreClientError]
    ValidationError: Type[BotocoreClientError]


class SageMakerRuntimeClient:
    """
    [SageMakerRuntime.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.generate_presigned_url)
        """

    def invoke_endpoint(
        self,
        EndpointName: str,
        Body: Union[bytes, IO[bytes]],
        ContentType: str = None,
        Accept: str = None,
        CustomAttributes: str = None,
        TargetModel: str = None,
        TargetVariant: str = None,
    ) -> InvokeEndpointOutputTypeDef:
        """
        [Client.invoke_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.invoke_endpoint)
        """
