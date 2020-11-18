# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for connectparticipant service client

Usage::

    ```python
    import boto3
    from mypy_boto3_connectparticipant import ConnectParticipantClient

    client: ConnectParticipantClient = boto3.client("connectparticipant")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_connectparticipant.type_defs import (
    CreateParticipantConnectionResponseTypeDef,
    GetTranscriptResponseTypeDef,
    SendEventResponseTypeDef,
    SendMessageResponseTypeDef,
    StartPositionTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ConnectParticipantClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class ConnectParticipantClient:
    """
    [ConnectParticipant.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/connectparticipant.html#ConnectParticipant.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/connectparticipant.html#ConnectParticipant.Client.can_paginate)
        """

    def create_participant_connection(
        self, Type: List[Literal["WEBSOCKET", "CONNECTION_CREDENTIALS"]], ParticipantToken: str
    ) -> CreateParticipantConnectionResponseTypeDef:
        """
        [Client.create_participant_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/connectparticipant.html#ConnectParticipant.Client.create_participant_connection)
        """

    def disconnect_participant(
        self, ConnectionToken: str, ClientToken: str = None
    ) -> Dict[str, Any]:
        """
        [Client.disconnect_participant documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/connectparticipant.html#ConnectParticipant.Client.disconnect_participant)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/connectparticipant.html#ConnectParticipant.Client.generate_presigned_url)
        """

    def get_transcript(
        self,
        ConnectionToken: str,
        ContactId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        ScanDirection: Literal["FORWARD", "BACKWARD"] = None,
        SortOrder: Literal["DESCENDING", "ASCENDING"] = None,
        StartPosition: StartPositionTypeDef = None,
    ) -> GetTranscriptResponseTypeDef:
        """
        [Client.get_transcript documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/connectparticipant.html#ConnectParticipant.Client.get_transcript)
        """

    def send_event(
        self, ContentType: str, ConnectionToken: str, Content: str = None, ClientToken: str = None
    ) -> SendEventResponseTypeDef:
        """
        [Client.send_event documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/connectparticipant.html#ConnectParticipant.Client.send_event)
        """

    def send_message(
        self, ContentType: str, Content: str, ConnectionToken: str, ClientToken: str = None
    ) -> SendMessageResponseTypeDef:
        """
        [Client.send_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/connectparticipant.html#ConnectParticipant.Client.send_message)
        """
