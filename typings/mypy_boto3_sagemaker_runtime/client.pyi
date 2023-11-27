"""
Type annotations for sagemaker-runtime service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_sagemaker_runtime import SageMakerRuntimeClient

    client: SageMakerRuntimeClient = boto3.client("sagemaker-runtime")
    ```
"""
from typing import IO, Any, Dict, Type, Union

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .type_defs import (
    InvokeEndpointAsyncOutputTypeDef,
    InvokeEndpointOutputTypeDef,
    InvokeEndpointWithResponseStreamOutputTypeDef,
)

__all__ = ("SageMakerRuntimeClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalDependencyException: Type[BotocoreClientError]
    InternalFailure: Type[BotocoreClientError]
    InternalStreamFailure: Type[BotocoreClientError]
    ModelError: Type[BotocoreClientError]
    ModelNotReadyException: Type[BotocoreClientError]
    ModelStreamError: Type[BotocoreClientError]
    ServiceUnavailable: Type[BotocoreClientError]
    ValidationError: Type[BotocoreClientError]

class SageMakerRuntimeClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SageMakerRuntimeClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client.html#generate_presigned_url)
        """
    def invoke_endpoint(
        self,
        *,
        EndpointName: str,
        Body: Union[bytes, IO[bytes], StreamingBody],
        ContentType: str = None,
        Accept: str = None,
        CustomAttributes: str = None,
        TargetModel: str = None,
        TargetVariant: str = None,
        TargetContainerHostname: str = None,
        InferenceId: str = None,
        EnableExplanations: str = None
    ) -> InvokeEndpointOutputTypeDef:
        """
        After you deploy a model into production using Amazon SageMaker hosting
        services, your client applications use this API to get inferences from the model
        hosted at the specified endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.invoke_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client.html#invoke_endpoint)
        """
    def invoke_endpoint_async(
        self,
        *,
        EndpointName: str,
        InputLocation: str,
        ContentType: str = None,
        Accept: str = None,
        CustomAttributes: str = None,
        InferenceId: str = None,
        RequestTTLSeconds: int = None,
        InvocationTimeoutSeconds: int = None
    ) -> InvokeEndpointAsyncOutputTypeDef:
        """
        After you deploy a model into production using Amazon SageMaker hosting
        services, your client applications use this API to get inferences from the model
        hosted at the specified endpoint in an asynchronous manner.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.invoke_endpoint_async)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client.html#invoke_endpoint_async)
        """
    def invoke_endpoint_with_response_stream(
        self,
        *,
        EndpointName: str,
        Body: Union[bytes, IO[bytes], StreamingBody],
        ContentType: str = None,
        Accept: str = None,
        CustomAttributes: str = None,
        TargetVariant: str = None,
        TargetContainerHostname: str = None,
        InferenceId: str = None
    ) -> InvokeEndpointWithResponseStreamOutputTypeDef:
        """
        Invokes a model at the specified endpoint to return the inference response as a
        stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.invoke_endpoint_with_response_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client.html#invoke_endpoint_with_response_stream)
        """
