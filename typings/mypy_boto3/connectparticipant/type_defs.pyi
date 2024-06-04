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
    "DescribeViewRequestRequestTypeDef",
    "DescribeViewResponseTypeDef",
    "DisconnectParticipantRequestRequestTypeDef",
    "GetAttachmentRequestRequestTypeDef",
    "GetAttachmentResponseTypeDef",
    "GetTranscriptRequestRequestTypeDef",
    "GetTranscriptResponseTypeDef",
    "ItemTypeDef",
    "MessageMetadataTypeDef",
    "ReceiptTypeDef",
    "ResponseMetadataTypeDef",
    "SendEventRequestRequestTypeDef",
    "SendEventResponseTypeDef",
    "SendMessageRequestRequestTypeDef",
    "SendMessageResponseTypeDef",
    "StartAttachmentUploadRequestRequestTypeDef",
    "StartAttachmentUploadResponseTypeDef",
    "StartPositionTypeDef",
    "UploadMetadataTypeDef",
    "ViewContentTypeDef",
    "ViewTypeDef",
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

_RequiredCreateParticipantConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateParticipantConnectionRequestRequestTypeDef",
    {
        "ParticipantToken": str,
    },
)
_OptionalCreateParticipantConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateParticipantConnectionRequestRequestTypeDef",
    {
        "Type": List[ConnectionTypeType],
        "ConnectParticipant": bool,
    },
    total=False,
)

class CreateParticipantConnectionRequestRequestTypeDef(
    _RequiredCreateParticipantConnectionRequestRequestTypeDef,
    _OptionalCreateParticipantConnectionRequestRequestTypeDef,
):
    pass

CreateParticipantConnectionResponseTypeDef = TypedDict(
    "CreateParticipantConnectionResponseTypeDef",
    {
        "Websocket": "WebsocketTypeDef",
        "ConnectionCredentials": "ConnectionCredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeViewRequestRequestTypeDef = TypedDict(
    "DescribeViewRequestRequestTypeDef",
    {
        "ViewToken": str,
        "ConnectionToken": str,
    },
)

DescribeViewResponseTypeDef = TypedDict(
    "DescribeViewResponseTypeDef",
    {
        "View": "ViewTypeDef",
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
        "MessageMetadata": "MessageMetadataTypeDef",
        "RelatedContactId": str,
        "ContactId": str,
    },
    total=False,
)

MessageMetadataTypeDef = TypedDict(
    "MessageMetadataTypeDef",
    {
        "MessageId": str,
        "Receipts": List["ReceiptTypeDef"],
    },
    total=False,
)

ReceiptTypeDef = TypedDict(
    "ReceiptTypeDef",
    {
        "DeliveredTimestamp": str,
        "ReadTimestamp": str,
        "RecipientParticipantId": str,
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

ViewContentTypeDef = TypedDict(
    "ViewContentTypeDef",
    {
        "InputSchema": str,
        "Template": str,
        "Actions": List[str],
    },
    total=False,
)

ViewTypeDef = TypedDict(
    "ViewTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Version": int,
        "Content": "ViewContentTypeDef",
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
