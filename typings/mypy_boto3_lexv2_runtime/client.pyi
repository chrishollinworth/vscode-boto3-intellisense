"""
Main interface for lexv2-runtime service client

Usage::

    ```python
    import boto3
    from mypy_boto3_lexv2_runtime import LexRuntimeV2Client

    client: LexRuntimeV2Client = boto3.client("lexv2-runtime")
    ```
"""
from typing import IO, Any, Dict, List, Type, Union

from botocore.client import ClientMeta

from mypy_boto3_lexv2_runtime.type_defs import (
    DeleteSessionResponseTypeDef,
    GetSessionResponseTypeDef,
    MessageTypeDef,
    PutSessionResponseTypeDef,
    RecognizeTextResponseTypeDef,
    RecognizeUtteranceResponseTypeDef,
    SessionStateTypeDef,
)

__all__ = ("LexRuntimeV2Client",)


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
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class LexRuntimeV2Client:
    """
    [LexRuntimeV2.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-runtime.html#LexRuntimeV2.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.can_paginate)
        """

    def delete_session(
        self, botId: str, botAliasId: str, localeId: str, sessionId: str
    ) -> DeleteSessionResponseTypeDef:
        """
        [Client.delete_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.delete_session)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.generate_presigned_url)
        """

    def get_session(
        self, botId: str, botAliasId: str, localeId: str, sessionId: str
    ) -> GetSessionResponseTypeDef:
        """
        [Client.get_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.get_session)
        """

    def put_session(
        self,
        botId: str,
        botAliasId: str,
        localeId: str,
        sessionId: str,
        sessionState: "SessionStateTypeDef",
        messages: List["MessageTypeDef"] = None,
        requestAttributes: Dict[str, str] = None,
        responseContentType: str = None,
    ) -> PutSessionResponseTypeDef:
        """
        [Client.put_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.put_session)
        """

    def recognize_text(
        self,
        botId: str,
        botAliasId: str,
        localeId: str,
        sessionId: str,
        text: str,
        sessionState: "SessionStateTypeDef" = None,
        requestAttributes: Dict[str, str] = None,
    ) -> RecognizeTextResponseTypeDef:
        """
        [Client.recognize_text documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.recognize_text)
        """

    def recognize_utterance(
        self,
        botId: str,
        botAliasId: str,
        localeId: str,
        sessionId: str,
        requestContentType: str,
        sessionState: str = None,
        requestAttributes: str = None,
        responseContentType: str = None,
        inputStream: Union[bytes, IO[bytes]] = None,
    ) -> RecognizeUtteranceResponseTypeDef:
        """
        [Client.recognize_utterance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.recognize_utterance)
        """
