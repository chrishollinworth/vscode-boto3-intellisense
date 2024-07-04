"""
Type annotations for bedrock-agent-runtime service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_bedrock_agent_runtime import AgentsforBedrockRuntimeClient

    client: AgentsforBedrockRuntimeClient = boto3.client("bedrock-agent-runtime")
    ```
"""

import sys
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .paginator import RetrievePaginator
from .type_defs import (
    InvokeAgentResponseTypeDef,
    KnowledgeBaseQueryTypeDef,
    KnowledgeBaseRetrievalConfigurationTypeDef,
    RetrieveAndGenerateConfigurationTypeDef,
    RetrieveAndGenerateInputTypeDef,
    RetrieveAndGenerateResponseTypeDef,
    RetrieveAndGenerateSessionConfigurationTypeDef,
    RetrieveResponseTypeDef,
    SessionStateTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AgentsforBedrockRuntimeClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadGatewayException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DependencyFailedException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class AgentsforBedrockRuntimeClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AgentsforBedrockRuntimeClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/client.html#generate_presigned_url)
        """

    def invoke_agent(
        self,
        *,
        agentAliasId: str,
        agentId: str,
        sessionId: str,
        enableTrace: bool = None,
        endSession: bool = None,
        inputText: str = None,
        sessionState: "SessionStateTypeDef" = None
    ) -> InvokeAgentResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Client.invoke_agent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/client.html#invoke_agent)
        """

    def retrieve(
        self,
        *,
        knowledgeBaseId: str,
        retrievalQuery: "KnowledgeBaseQueryTypeDef",
        nextToken: str = None,
        retrievalConfiguration: "KnowledgeBaseRetrievalConfigurationTypeDef" = None
    ) -> RetrieveResponseTypeDef:
        """
        Queries a knowledge base and retrieves information from it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Client.retrieve)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/client.html#retrieve)
        """

    def retrieve_and_generate(
        self,
        *,
        input: "RetrieveAndGenerateInputTypeDef",
        retrieveAndGenerateConfiguration: "RetrieveAndGenerateConfigurationTypeDef" = None,
        sessionConfiguration: "RetrieveAndGenerateSessionConfigurationTypeDef" = None,
        sessionId: str = None
    ) -> RetrieveAndGenerateResponseTypeDef:
        """
        Queries a knowledge base and generates responses based on the retrieved results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Client.retrieve_and_generate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/client.html#retrieve_and_generate)
        """

    def get_paginator(self, operation_name: Literal["retrieve"]) -> RetrievePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Paginator.Retrieve)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators.html#retrievepaginator)
        """
