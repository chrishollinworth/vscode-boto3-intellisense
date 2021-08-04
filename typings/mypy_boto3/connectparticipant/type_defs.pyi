"""
Type annotations for connectparticipant service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/type_defs.html)

Usage::

    ```python
    from mypy_boto3_connectparticipant.type_defs import AttachmentItemTypeDef

    data: AttachmentItemTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    ArtifactStatusType,
    ChatItemTypeType,
    ConnectionTypeType,
    ParticipantRoleType,
    ScanDirectionType,
    SortKeyType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AttachmentItemTypeDef",
    "CompleteAttachmentUploadRequestRequestTypeDef",
    "ConnectionCredentialsTypeDef",
    "CreateParticipantConnectionRequestRequestTypeDef",
    "CreateParticipantConnectionResponseTypeDef",
    "DisconnectParticipantRequestRequestTypeDef",
    "GetAttachmentRequestRequestTypeDef",
    "GetAttachmentResponseTypeDef",
    "GetTranscriptRequestRequestTypeDef",
    "GetTranscriptResponseTypeDef",
    "ItemTypeDef",
    "ResponseMetadataTypeDef",
    "SendEventRequestRequestTypeDef",
    "SendEventResponseTypeDef",
    "SendMessageRequestRequestTypeDef",
    "SendMessageResponseTypeDef",
    "StartAttachmentUploadRequestRequestTypeDef",
    "StartAttachmentUploadResponseTypeDef",
    "StartPositionTypeDef",
    "UploadMetadataTypeDef",
    "WebsocketTypeDef",
)

AttachmentItemTypeDef = TypedDict(
    "AttachmentItemTypeDef",
    {
        "ContentType": str,
        "AttachmentId": str,
        "AttachmentName": str,
        "Status": ArtifactStatusType,
    },
    total=False,
)

CompleteAttachmentUploadRequestRequestTypeDef = TypedDict(
    "CompleteAttachmentUploadRequestRequestTypeDef",
    {
        "AttachmentIds": List[str],
        "ClientToken": str,
        "ConnectionToken": str,
    },
)

ConnectionCredentialsTypeDef = TypedDict(
    "ConnectionCredentialsTypeDef",
    {
        "ConnectionToken": str,
        "Expiry": str,
    },
    total=False,
)

CreateParticipantConnectionRequestRequestTypeDef = TypedDict(
    "CreateParticipantConnectionRequestRequestTypeDef",
    {
        "Type": List[ConnectionTypeType],
        "ParticipantToken": str,
    },
)

CreateParticipantConnectionResponseTypeDef = TypedDict(
    "CreateParticipantConnectionResponseTypeDef",
    {
        "Websocket": "WebsocketTypeDef",
        "ConnectionCredentials": "ConnectionCredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisconnectParticipantRequestRequestTypeDef = TypedDict(
    "_RequiredDisconnectParticipantRequestRequestTypeDef",
    {
        "ConnectionToken": str,
    },
)
_OptionalDisconnectParticipantRequestRequestTypeDef = TypedDict(
    "_OptionalDisconnectParticipantRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class DisconnectParticipantRequestRequestTypeDef(
    _RequiredDisconnectParticipantRequestRequestTypeDef,
    _OptionalDisconnectParticipantRequestRequestTypeDef,
):
    pass

GetAttachmentRequestRequestTypeDef = TypedDict(
    "GetAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
        "ConnectionToken": str,
    },
)

GetAttachmentResponseTypeDef = TypedDict(
    "GetAttachmentResponseTypeDef",
    {
        "Url": str,
        "UrlExpiry": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTranscriptRequestRequestTypeDef = TypedDict(
    "_RequiredGetTranscriptRequestRequestTypeDef",
    {
        "ConnectionToken": str,
    },
)
_OptionalGetTranscriptRequestRequestTypeDef = TypedDict(
    "_OptionalGetTranscriptRequestRequestTypeDef",
    {
        "ContactId": str,
        "MaxResults": int,
        "NextToken": str,
        "ScanDirection": ScanDirectionType,
        "SortOrder": SortKeyType,
        "StartPosition": "StartPositionTypeDef",
    },
    total=False,
)

class GetTranscriptRequestRequestTypeDef(
    _RequiredGetTranscriptRequestRequestTypeDef, _OptionalGetTranscriptRequestRequestTypeDef
):
    pass

GetTranscriptResponseTypeDef = TypedDict(
    "GetTranscriptResponseTypeDef",
    {
        "InitialContactId": str,
        "Transcript": List["ItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ItemTypeDef = TypedDict(
    "ItemTypeDef",
    {
        "AbsoluteTime": str,
        "Content": str,
        "ContentType": str,
        "Id": str,
        "Type": ChatItemTypeType,
        "ParticipantId": str,
        "DisplayName": str,
        "ParticipantRole": ParticipantRoleType,
        "Attachments": List["AttachmentItemTypeDef"],
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredSendEventRequestRequestTypeDef = TypedDict(
    "_RequiredSendEventRequestRequestTypeDef",
    {
        "ContentType": str,
        "ConnectionToken": str,
    },
)
_OptionalSendEventRequestRequestTypeDef = TypedDict(
    "_OptionalSendEventRequestRequestTypeDef",
    {
        "Content": str,
        "ClientToken": str,
    },
    total=False,
)

class SendEventRequestRequestTypeDef(
    _RequiredSendEventRequestRequestTypeDef, _OptionalSendEventRequestRequestTypeDef
):
    pass

SendEventResponseTypeDef = TypedDict(
    "SendEventResponseTypeDef",
    {
        "Id": str,
        "AbsoluteTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendMessageRequestRequestTypeDef = TypedDict(
    "_RequiredSendMessageRequestRequestTypeDef",
    {
        "ContentType": str,
        "Content": str,
        "ConnectionToken": str,
    },
)
_OptionalSendMessageRequestRequestTypeDef = TypedDict(
    "_OptionalSendMessageRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class SendMessageRequestRequestTypeDef(
    _RequiredSendMessageRequestRequestTypeDef, _OptionalSendMessageRequestRequestTypeDef
):
    pass

SendMessageResponseTypeDef = TypedDict(
    "SendMessageResponseTypeDef",
    {
        "Id": str,
        "AbsoluteTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartAttachmentUploadRequestRequestTypeDef = TypedDict(
    "StartAttachmentUploadRequestRequestTypeDef",
    {
        "ContentType": str,
        "AttachmentSizeInBytes": int,
        "AttachmentName": str,
        "ClientToken": str,
        "ConnectionToken": str,
    },
)

StartAttachmentUploadResponseTypeDef = TypedDict(
    "StartAttachmentUploadResponseTypeDef",
    {
        "AttachmentId": str,
        "UploadMetadata": "UploadMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartPositionTypeDef = TypedDict(
    "StartPositionTypeDef",
    {
        "Id": str,
        "AbsoluteTime": str,
        "MostRecent": int,
    },
    total=False,
)

UploadMetadataTypeDef = TypedDict(
    "UploadMetadataTypeDef",
    {
        "Url": str,
        "UrlExpiry": str,
        "HeadersToInclude": Dict[str, str],
    },
    total=False,
)

WebsocketTypeDef = TypedDict(
    "WebsocketTypeDef",
    {
        "Url": str,
        "ConnectionExpiry": str,
    },
    total=False,
)
