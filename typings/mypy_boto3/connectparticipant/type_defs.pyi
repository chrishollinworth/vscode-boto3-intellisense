"""
Type annotations for connectparticipant service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_connectparticipant.type_defs import AttachmentItemTypeDef

    data: AttachmentItemTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

from .literals import (
    ArtifactStatusType,
    ChatItemTypeType,
    ConnectionTypeType,
    ParticipantRoleType,
    ScanDirectionType,
    SortKeyType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AttachmentItemTypeDef",
    "CancelParticipantAuthenticationRequestTypeDef",
    "CompleteAttachmentUploadRequestTypeDef",
    "ConnectionCredentialsTypeDef",
    "CreateParticipantConnectionRequestTypeDef",
    "CreateParticipantConnectionResponseTypeDef",
    "DescribeViewRequestTypeDef",
    "DescribeViewResponseTypeDef",
    "DisconnectParticipantRequestTypeDef",
    "GetAttachmentRequestTypeDef",
    "GetAttachmentResponseTypeDef",
    "GetAuthenticationUrlRequestTypeDef",
    "GetAuthenticationUrlResponseTypeDef",
    "GetTranscriptRequestTypeDef",
    "GetTranscriptResponseTypeDef",
    "ItemTypeDef",
    "MessageMetadataTypeDef",
    "ReceiptTypeDef",
    "ResponseMetadataTypeDef",
    "SendEventRequestTypeDef",
    "SendEventResponseTypeDef",
    "SendMessageRequestTypeDef",
    "SendMessageResponseTypeDef",
    "StartAttachmentUploadRequestTypeDef",
    "StartAttachmentUploadResponseTypeDef",
    "StartPositionTypeDef",
    "UploadMetadataTypeDef",
    "ViewContentTypeDef",
    "ViewTypeDef",
    "WebsocketTypeDef",
)

class AttachmentItemTypeDef(TypedDict):
    ContentType: NotRequired[str]
    AttachmentId: NotRequired[str]
    AttachmentName: NotRequired[str]
    Status: NotRequired[ArtifactStatusType]

class CancelParticipantAuthenticationRequestTypeDef(TypedDict):
    SessionId: str
    ConnectionToken: str

class CompleteAttachmentUploadRequestTypeDef(TypedDict):
    AttachmentIds: Sequence[str]
    ClientToken: str
    ConnectionToken: str

class ConnectionCredentialsTypeDef(TypedDict):
    ConnectionToken: NotRequired[str]
    Expiry: NotRequired[str]

CreateParticipantConnectionRequestTypeDef = TypedDict(
    "CreateParticipantConnectionRequestTypeDef",
    {
        "ParticipantToken": str,
        "Type": NotRequired[Sequence[ConnectionTypeType]],
        "ConnectParticipant": NotRequired[bool],
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class WebsocketTypeDef(TypedDict):
    Url: NotRequired[str]
    ConnectionExpiry: NotRequired[str]

class DescribeViewRequestTypeDef(TypedDict):
    ViewToken: str
    ConnectionToken: str

class DisconnectParticipantRequestTypeDef(TypedDict):
    ConnectionToken: str
    ClientToken: NotRequired[str]

class GetAttachmentRequestTypeDef(TypedDict):
    AttachmentId: str
    ConnectionToken: str
    UrlExpiryInSeconds: NotRequired[int]

class GetAuthenticationUrlRequestTypeDef(TypedDict):
    SessionId: str
    RedirectUri: str
    ConnectionToken: str

class StartPositionTypeDef(TypedDict):
    Id: NotRequired[str]
    AbsoluteTime: NotRequired[str]
    MostRecent: NotRequired[int]

class ReceiptTypeDef(TypedDict):
    DeliveredTimestamp: NotRequired[str]
    ReadTimestamp: NotRequired[str]
    RecipientParticipantId: NotRequired[str]

class SendEventRequestTypeDef(TypedDict):
    ContentType: str
    ConnectionToken: str
    Content: NotRequired[str]
    ClientToken: NotRequired[str]

class SendMessageRequestTypeDef(TypedDict):
    ContentType: str
    Content: str
    ConnectionToken: str
    ClientToken: NotRequired[str]

class StartAttachmentUploadRequestTypeDef(TypedDict):
    ContentType: str
    AttachmentSizeInBytes: int
    AttachmentName: str
    ClientToken: str
    ConnectionToken: str

class UploadMetadataTypeDef(TypedDict):
    Url: NotRequired[str]
    UrlExpiry: NotRequired[str]
    HeadersToInclude: NotRequired[Dict[str, str]]

class ViewContentTypeDef(TypedDict):
    InputSchema: NotRequired[str]
    Template: NotRequired[str]
    Actions: NotRequired[List[str]]

class GetAttachmentResponseTypeDef(TypedDict):
    Url: str
    UrlExpiry: str
    AttachmentSizeInBytes: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetAuthenticationUrlResponseTypeDef(TypedDict):
    AuthenticationUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendEventResponseTypeDef(TypedDict):
    Id: str
    AbsoluteTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendMessageResponseTypeDef(TypedDict):
    Id: str
    AbsoluteTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateParticipantConnectionResponseTypeDef(TypedDict):
    Websocket: WebsocketTypeDef
    ConnectionCredentials: ConnectionCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTranscriptRequestTypeDef(TypedDict):
    ConnectionToken: str
    ContactId: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    ScanDirection: NotRequired[ScanDirectionType]
    SortOrder: NotRequired[SortKeyType]
    StartPosition: NotRequired[StartPositionTypeDef]

class MessageMetadataTypeDef(TypedDict):
    MessageId: NotRequired[str]
    Receipts: NotRequired[List[ReceiptTypeDef]]

class StartAttachmentUploadResponseTypeDef(TypedDict):
    AttachmentId: str
    UploadMetadata: UploadMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ViewTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    Version: NotRequired[int]
    Content: NotRequired[ViewContentTypeDef]

ItemTypeDef = TypedDict(
    "ItemTypeDef",
    {
        "AbsoluteTime": NotRequired[str],
        "Content": NotRequired[str],
        "ContentType": NotRequired[str],
        "Id": NotRequired[str],
        "Type": NotRequired[ChatItemTypeType],
        "ParticipantId": NotRequired[str],
        "DisplayName": NotRequired[str],
        "ParticipantRole": NotRequired[ParticipantRoleType],
        "Attachments": NotRequired[List[AttachmentItemTypeDef]],
        "MessageMetadata": NotRequired[MessageMetadataTypeDef],
        "RelatedContactId": NotRequired[str],
        "ContactId": NotRequired[str],
    },
)

class DescribeViewResponseTypeDef(TypedDict):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTranscriptResponseTypeDef(TypedDict):
    InitialContactId: str
    Transcript: List[ItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
