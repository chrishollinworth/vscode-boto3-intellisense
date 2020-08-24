# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for lex-runtime service client

Usage::

    ```python
    import boto3
    from mypy_boto3_lex_runtime import LexRuntimeServiceClient

    client: LexRuntimeServiceClient = boto3.client("lex-runtime")
    ```
"""
from typing import IO, Any, Dict, List, Type, Union

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_lex_runtime.type_defs import (
    DeleteSessionResponseTypeDef,
    DialogActionTypeDef,
    GetSessionResponseTypeDef,
    IntentSummaryTypeDef,
    PostContentResponseTypeDef,
    PostTextResponseTypeDef,
    PutSessionResponseTypeDef,
)

__all__ = ("LexRuntimeServiceClient",)


class Exceptions:
    BadGatewayException: Type[Boto3ClientError]
    BadRequestException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    ConflictException: Type[Boto3ClientError]
    DependencyFailedException: Type[Boto3ClientError]
    InternalFailureException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    LoopDetectedException: Type[Boto3ClientError]
    NotAcceptableException: Type[Boto3ClientError]
    NotFoundException: Type[Boto3ClientError]
    RequestTimeoutException: Type[Boto3ClientError]
    UnsupportedMediaTypeException: Type[Boto3ClientError]


class LexRuntimeServiceClient:
    """
    [LexRuntimeService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/lex-runtime.html#LexRuntimeService.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/lex-runtime.html#LexRuntimeService.Client.can_paginate)
        """

    def delete_session(
        self, botName: str, botAlias: str, userId: str
    ) -> DeleteSessionResponseTypeDef:
        """
        [Client.delete_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/lex-runtime.html#LexRuntimeService.Client.delete_session)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/lex-runtime.html#LexRuntimeService.Client.generate_presigned_url)
        """

    def get_session(
        self, botName: str, botAlias: str, userId: str, checkpointLabelFilter: str = None
    ) -> GetSessionResponseTypeDef:
        """
        [Client.get_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/lex-runtime.html#LexRuntimeService.Client.get_session)
        """

    def post_content(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        contentType: str,
        inputStream: Union[bytes, IO[bytes]],
        sessionAttributes: str = None,
        requestAttributes: str = None,
        accept: str = None,
    ) -> PostContentResponseTypeDef:
        """
        [Client.post_content documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/lex-runtime.html#LexRuntimeService.Client.post_content)
        """

    def post_text(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        inputText: str,
        sessionAttributes: Dict[str, str] = None,
        requestAttributes: Dict[str, str] = None,
    ) -> PostTextResponseTypeDef:
        """
        [Client.post_text documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/lex-runtime.html#LexRuntimeService.Client.post_text)
        """

    def put_session(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        sessionAttributes: Dict[str, str] = None,
        dialogAction: "DialogActionTypeDef" = None,
        recentIntentSummaryView: List["IntentSummaryTypeDef"] = None,
        accept: str = None,
    ) -> PutSessionResponseTypeDef:
        """
        [Client.put_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/lex-runtime.html#LexRuntimeService.Client.put_session)
        """
