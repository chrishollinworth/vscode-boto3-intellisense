# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
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

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_sagemaker_runtime.type_defs import InvokeEndpointOutputTypeDef

__all__ = ("SageMakerRuntimeClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    InternalFailure: Type[Boto3ClientError]
    ModelError: Type[Boto3ClientError]
    ServiceUnavailable: Type[Boto3ClientError]
    ValidationError: Type[Boto3ClientError]


class SageMakerRuntimeClient:
    """
    [SageMakerRuntime.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.generate_presigned_url)
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
        [Client.invoke_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.invoke_endpoint)
        """
