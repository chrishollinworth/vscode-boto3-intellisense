"""
Type annotations for lex-runtime service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_runtime/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_lex_runtime import LexRuntimeServiceClient

    client: LexRuntimeServiceClient = boto3.client("lex-runtime")
    ```
"""
from typing import IO, Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .type_defs import (
    ActiveContextTypeDef,
    DeleteSessionResponseTypeDef,
    DialogActionTypeDef,
    GetSessionResponseTypeDef,
    IntentSummaryTypeDef,
    PostContentResponseTypeDef,
    PostTextResponseTypeDef,
    PutSessionResponseTypeDef,
)

__all__ = ("LexRuntimeServiceClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BadGatewayException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DependencyFailedException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    LoopDetectedException: Type[BotocoreClientError]
    NotAcceptableException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    RequestTimeoutException: Type[BotocoreClientError]
    UnsupportedMediaTypeException: Type[BotocoreClientError]

class LexRuntimeServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/lex-runtime.html#LexRuntimeService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_runtime/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        LexRuntimeServiceClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/lex-runtime.html#LexRuntimeService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_runtime/client.html#can_paginate)
        """
    def delete_session(
        self, *, botName: str, botAlias: str, userId: str
    ) -> DeleteSessionResponseTypeDef:
        """
        Removes session information for a specified bot, alias, and user ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/lex-runtime.html#LexRuntimeService.Client.delete_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_runtime/client.html#delete_session)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/lex-runtime.html#LexRuntimeService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_runtime/client.html#generate_presigned_url)
        """
    def get_session(
        self, *, botName: str, botAlias: str, userId: str, checkpointLabelFilter: str = None
    ) -> GetSessionResponseTypeDef:
        """
        Returns session information for a specified bot, alias, and user ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/lex-runtime.html#LexRuntimeService.Client.get_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_runtime/client.html#get_session)
        """
    def post_content(
        self,
        *,
        botName: str,
        botAlias: str,
        userId: str,
        contentType: str,
        inputStream: Union[bytes, IO[bytes], StreamingBody],
        sessionAttributes: str = None,
        requestAttributes: str = None,
        accept: str = None,
        activeContexts: str = None
    ) -> PostContentResponseTypeDef:
        """
        Sends user input (text or speech) to Amazon Lex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/lex-runtime.html#LexRuntimeService.Client.post_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_runtime/client.html#post_content)
        """
    def post_text(
        self,
        *,
        botName: str,
        botAlias: str,
        userId: str,
        inputText: str,
        sessionAttributes: Dict[str, str] = None,
        requestAttributes: Dict[str, str] = None,
        activeContexts: List["ActiveContextTypeDef"] = None
    ) -> PostTextResponseTypeDef:
        """
        Sends user input to Amazon Lex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/lex-runtime.html#LexRuntimeService.Client.post_text)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_runtime/client.html#post_text)
        """
    def put_session(
        self,
        *,
        botName: str,
        botAlias: str,
        userId: str,
        sessionAttributes: Dict[str, str] = None,
        dialogAction: "DialogActionTypeDef" = None,
        recentIntentSummaryView: List["IntentSummaryTypeDef"] = None,
        accept: str = None,
        activeContexts: List["ActiveContextTypeDef"] = None
    ) -> PutSessionResponseTypeDef:
        """
        Creates a new session or modifies an existing session with an Amazon Lex bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/lex-runtime.html#LexRuntimeService.Client.put_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_runtime/client.html#put_session)
        """
