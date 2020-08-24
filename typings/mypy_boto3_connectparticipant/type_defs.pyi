"""
Main interface for connectparticipant service type definitions.

Usage::

    ```python
    from mypy_boto3_connectparticipant.type_defs import ConnectionCredentialsTypeDef

    data: ConnectionCredentialsTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ConnectionCredentialsTypeDef",
    "ItemTypeDef",
    "WebsocketTypeDef",
    "CreateParticipantConnectionResponseTypeDef",
    "GetTranscriptResponseTypeDef",
    "SendEventResponseTypeDef",
    "SendMessageResponseTypeDef",
    "StartPositionTypeDef",
)

ConnectionCredentialsTypeDef = TypedDict(
    "ConnectionCredentialsTypeDef", {"ConnectionToken": str, "Expiry": str}, total=False
)

ItemTypeDef = TypedDict(
    "ItemTypeDef",
    {
        "AbsoluteTime": str,
        "Content": str,
        "ContentType": str,
        "Id": str,
        "Type": Literal["MESSAGE", "EVENT", "CONNECTION_ACK"],
        "ParticipantId": str,
        "DisplayName": str,
        "ParticipantRole": Literal["AGENT", "CUSTOMER", "SYSTEM"],
    },
    total=False,
)

WebsocketTypeDef = TypedDict("WebsocketTypeDef", {"Url": str, "ConnectionExpiry": str}, total=False)

CreateParticipantConnectionResponseTypeDef = TypedDict(
    "CreateParticipantConnectionResponseTypeDef",
    {"Websocket": "WebsocketTypeDef", "ConnectionCredentials": "ConnectionCredentialsTypeDef"},
    total=False,
)

GetTranscriptResponseTypeDef = TypedDict(
    "GetTranscriptResponseTypeDef",
    {"InitialContactId": str, "Transcript": List["ItemTypeDef"], "NextToken": str},
    total=False,
)

SendEventResponseTypeDef = TypedDict(
    "SendEventResponseTypeDef", {"Id": str, "AbsoluteTime": str}, total=False
)

SendMessageResponseTypeDef = TypedDict(
    "SendMessageResponseTypeDef", {"Id": str, "AbsoluteTime": str}, total=False
)

StartPositionTypeDef = TypedDict(
    "StartPositionTypeDef", {"Id": str, "AbsoluteTime": str, "MostRecent": int}, total=False
)
