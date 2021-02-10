"""
Main interface for connectparticipant service type definitions.

Usage::

    ```python
    from mypy_boto3_connectparticipant.type_defs import AttachmentItemTypeDef

    data: AttachmentItemTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttachmentItemTypeDef",
    "ConnectionCredentialsTypeDef",
    "ItemTypeDef",
    "UploadMetadataTypeDef",
    "WebsocketTypeDef",
    "CreateParticipantConnectionResponseTypeDef",
    "GetAttachmentResponseTypeDef",
    "GetTranscriptResponseTypeDef",
    "SendEventResponseTypeDef",
    "SendMessageResponseTypeDef",
    "StartAttachmentUploadResponseTypeDef",
    "StartPositionTypeDef",
)

AttachmentItemTypeDef = TypedDict(
    "AttachmentItemTypeDef",
    {
        "ContentType": str,
        "AttachmentId": str,
        "AttachmentName": str,
        "Status": Literal["APPROVED", "REJECTED", "IN_PROGRESS"],
    },
    total=False,
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
        "Type": Literal[
            "TYPING",
            "PARTICIPANT_JOINED",
            "PARTICIPANT_LEFT",
            "CHAT_ENDED",
            "TRANSFER_SUCCEEDED",
            "TRANSFER_FAILED",
            "MESSAGE",
            "EVENT",
            "ATTACHMENT",
            "CONNECTION_ACK",
        ],
        "ParticipantId": str,
        "DisplayName": str,
        "ParticipantRole": Literal["AGENT", "CUSTOMER", "SYSTEM"],
        "Attachments": List["AttachmentItemTypeDef"],
    },
    total=False,
)

UploadMetadataTypeDef = TypedDict(
    "UploadMetadataTypeDef",
    {"Url": str, "UrlExpiry": str, "HeadersToInclude": Dict[str, str]},
    total=False,
)

WebsocketTypeDef = TypedDict("WebsocketTypeDef", {"Url": str, "ConnectionExpiry": str}, total=False)

CreateParticipantConnectionResponseTypeDef = TypedDict(
    "CreateParticipantConnectionResponseTypeDef",
    {"Websocket": "WebsocketTypeDef", "ConnectionCredentials": "ConnectionCredentialsTypeDef"},
    total=False,
)

GetAttachmentResponseTypeDef = TypedDict(
    "GetAttachmentResponseTypeDef", {"Url": str, "UrlExpiry": str}, total=False
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

StartAttachmentUploadResponseTypeDef = TypedDict(
    "StartAttachmentUploadResponseTypeDef",
    {"AttachmentId": str, "UploadMetadata": "UploadMetadataTypeDef"},
    total=False,
)

StartPositionTypeDef = TypedDict(
    "StartPositionTypeDef", {"Id": str, "AbsoluteTime": str, "MostRecent": int}, total=False
)
