"""
Type annotations for lexv2-runtime service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_runtime/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_lexv2_runtime.client import LexRuntimeV2Client

    session = Session()
    client: LexRuntimeV2Client = session.client("lexv2-runtime")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    DeleteSessionRequestTypeDef,
    DeleteSessionResponseTypeDef,
    GetSessionRequestTypeDef,
    GetSessionResponseTypeDef,
    PutSessionRequestTypeDef,
    PutSessionResponseTypeDef,
    RecognizeTextRequestTypeDef,
    RecognizeTextResponseTypeDef,
    RecognizeUtteranceRequestTypeDef,
    RecognizeUtteranceResponseTypeDef,
    StartConversationRequestTypeDef,
    StartConversationResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("LexRuntimeV2Client",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    BadGatewayException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DependencyFailedException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class LexRuntimeV2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime.html#LexRuntimeV2.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_runtime/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LexRuntimeV2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime.html#LexRuntimeV2.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_runtime/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_runtime/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_runtime/client/#generate_presigned_url)
        """

    def delete_session(
        self, **kwargs: Unpack[DeleteSessionRequestTypeDef]
    ) -> DeleteSessionResponseTypeDef:
        """
        Removes session information for a specified bot, alias, and user ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime/client/delete_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_runtime/client/#delete_session)
        """

    def get_session(self, **kwargs: Unpack[GetSessionRequestTypeDef]) -> GetSessionResponseTypeDef:
        """
        Returns session information for a specified bot, alias, and user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime/client/get_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_runtime/client/#get_session)
        """

    def put_session(self, **kwargs: Unpack[PutSessionRequestTypeDef]) -> PutSessionResponseTypeDef:
        """
        Creates a new session or modifies an existing session with an Amazon Lex V2 bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime/client/put_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_runtime/client/#put_session)
        """

    def recognize_text(
        self, **kwargs: Unpack[RecognizeTextRequestTypeDef]
    ) -> RecognizeTextResponseTypeDef:
        """
        Sends user input to Amazon Lex V2.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime/client/recognize_text.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_runtime/client/#recognize_text)
        """

    def recognize_utterance(
        self, **kwargs: Unpack[RecognizeUtteranceRequestTypeDef]
    ) -> RecognizeUtteranceResponseTypeDef:
        """
        Sends user input to Amazon Lex V2.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime/client/recognize_utterance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_runtime/client/#recognize_utterance)
        """

    def start_conversation(
        self, **kwargs: Unpack[StartConversationRequestTypeDef]
    ) -> StartConversationResponseTypeDef:
        """
        Starts an HTTP/2 bidirectional event stream that enables you to send audio,
        text, or DTMF input in real time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime/client/start_conversation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_runtime/client/#start_conversation)
        """
