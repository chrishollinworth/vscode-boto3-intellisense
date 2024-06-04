"""
Type annotations for bedrock-runtime service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_bedrock_runtime import BedrockRuntimeClient

    client: BedrockRuntimeClient = boto3.client("bedrock-runtime")
    ```
"""

from typing import IO, Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import TraceType
from .type_defs import (
    ConverseResponseTypeDef,
    ConverseStreamResponseTypeDef,
    InferenceConfigurationTypeDef,
    InvokeModelResponseTypeDef,
    InvokeModelWithResponseStreamResponseTypeDef,
    MessageTypeDef,
    SystemContentBlockTypeDef,
    ToolConfigurationTypeDef,
)

__all__ = ("BedrockRuntimeClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ModelErrorException: Type[BotocoreClientError]
    ModelNotReadyException: Type[BotocoreClientError]
    ModelStreamErrorException: Type[BotocoreClientError]
    ModelTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class BedrockRuntimeClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-runtime.html#BedrockRuntime.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BedrockRuntimeClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-runtime.html#BedrockRuntime.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-runtime.html#BedrockRuntime.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client.html#close)
        """

    def converse(
        self,
        *,
        modelId: str,
        messages: List["MessageTypeDef"],
        system: List["SystemContentBlockTypeDef"] = None,
        inferenceConfig: "InferenceConfigurationTypeDef" = None,
        toolConfig: "ToolConfigurationTypeDef" = None,
        additionalModelRequestFields: Dict[str, Any] = None,
        additionalModelResponseFieldPaths: List[str] = None
    ) -> ConverseResponseTypeDef:
        """
        Sends messages to the specified Amazon Bedrock model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-runtime.html#BedrockRuntime.Client.converse)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client.html#converse)
        """

    def converse_stream(
        self,
        *,
        modelId: str,
        messages: List["MessageTypeDef"],
        system: List["SystemContentBlockTypeDef"] = None,
        inferenceConfig: "InferenceConfigurationTypeDef" = None,
        toolConfig: "ToolConfigurationTypeDef" = None,
        additionalModelRequestFields: Dict[str, Any] = None,
        additionalModelResponseFieldPaths: List[str] = None
    ) -> ConverseStreamResponseTypeDef:
        """
        Sends messages to the specified Amazon Bedrock model and returns the response in
        a stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-runtime.html#BedrockRuntime.Client.converse_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client.html#converse_stream)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-runtime.html#BedrockRuntime.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client.html#generate_presigned_url)
        """

    def invoke_model(
        self,
        *,
        body: Union[bytes, IO[bytes], StreamingBody],
        modelId: str,
        contentType: str = None,
        accept: str = None,
        trace: TraceType = None,
        guardrailIdentifier: str = None,
        guardrailVersion: str = None
    ) -> InvokeModelResponseTypeDef:
        """
        Invokes the specified Amazon Bedrock model to run inference using the prompt and
        inference parameters provided in the request body.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-runtime.html#BedrockRuntime.Client.invoke_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client.html#invoke_model)
        """

    def invoke_model_with_response_stream(
        self,
        *,
        body: Union[bytes, IO[bytes], StreamingBody],
        modelId: str,
        contentType: str = None,
        accept: str = None,
        trace: TraceType = None,
        guardrailIdentifier: str = None,
        guardrailVersion: str = None
    ) -> InvokeModelWithResponseStreamResponseTypeDef:
        """
        Invoke the specified Amazon Bedrock model to run inference using the prompt and
        inference parameters provided in the request body.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-runtime.html#BedrockRuntime.Client.invoke_model_with_response_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/client.html#invoke_model_with_response_stream)
        """
