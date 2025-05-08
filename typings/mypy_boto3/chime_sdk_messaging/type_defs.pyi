"""
Type annotations for chime-sdk-messaging service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_chime_sdk_messaging.type_defs import AppInstanceUserMembershipSummaryTypeDef

    data: AppInstanceUserMembershipSummaryTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AllowNotificationsType,
    ChannelMembershipTypeType,
    ChannelMessagePersistenceTypeType,
    ChannelMessageStatusType,
    ChannelMessageTypeType,
    ChannelModeType,
    ChannelPrivacyType,
    ErrorCodeType,
    ExpirationCriterionType,
    FallbackActionType,
    MessagingDataTypeType,
    PushNotificationTypeType,
    SearchFieldOperatorType,
    SortOrderType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AppInstanceUserMembershipSummaryTypeDef",
    "AssociateChannelFlowRequestTypeDef",
    "BatchChannelMembershipsTypeDef",
    "BatchCreateChannelMembershipErrorTypeDef",
    "BatchCreateChannelMembershipRequestTypeDef",
    "BatchCreateChannelMembershipResponseTypeDef",
    "ChannelAssociatedWithFlowSummaryTypeDef",
    "ChannelBanSummaryTypeDef",
    "ChannelBanTypeDef",
    "ChannelFlowCallbackRequestTypeDef",
    "ChannelFlowCallbackResponseTypeDef",
    "ChannelFlowSummaryTypeDef",
    "ChannelFlowTypeDef",
    "ChannelMembershipForAppInstanceUserSummaryTypeDef",
    "ChannelMembershipPreferencesTypeDef",
    "ChannelMembershipSummaryTypeDef",
    "ChannelMembershipTypeDef",
    "ChannelMessageCallbackTypeDef",
    "ChannelMessageStatusStructureTypeDef",
    "ChannelMessageSummaryTypeDef",
    "ChannelMessageTypeDef",
    "ChannelModeratedByAppInstanceUserSummaryTypeDef",
    "ChannelModeratorSummaryTypeDef",
    "ChannelModeratorTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "CreateChannelBanRequestTypeDef",
    "CreateChannelBanResponseTypeDef",
    "CreateChannelFlowRequestTypeDef",
    "CreateChannelFlowResponseTypeDef",
    "CreateChannelMembershipRequestTypeDef",
    "CreateChannelMembershipResponseTypeDef",
    "CreateChannelModeratorRequestTypeDef",
    "CreateChannelModeratorResponseTypeDef",
    "CreateChannelRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "DeleteChannelBanRequestTypeDef",
    "DeleteChannelFlowRequestTypeDef",
    "DeleteChannelMembershipRequestTypeDef",
    "DeleteChannelMessageRequestTypeDef",
    "DeleteChannelModeratorRequestTypeDef",
    "DeleteChannelRequestTypeDef",
    "DeleteMessagingStreamingConfigurationsRequestTypeDef",
    "DescribeChannelBanRequestTypeDef",
    "DescribeChannelBanResponseTypeDef",
    "DescribeChannelFlowRequestTypeDef",
    "DescribeChannelFlowResponseTypeDef",
    "DescribeChannelMembershipForAppInstanceUserRequestTypeDef",
    "DescribeChannelMembershipForAppInstanceUserResponseTypeDef",
    "DescribeChannelMembershipRequestTypeDef",
    "DescribeChannelMembershipResponseTypeDef",
    "DescribeChannelModeratedByAppInstanceUserRequestTypeDef",
    "DescribeChannelModeratedByAppInstanceUserResponseTypeDef",
    "DescribeChannelModeratorRequestTypeDef",
    "DescribeChannelModeratorResponseTypeDef",
    "DescribeChannelRequestTypeDef",
    "DescribeChannelResponseTypeDef",
    "DisassociateChannelFlowRequestTypeDef",
    "ElasticChannelConfigurationTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExpirationSettingsTypeDef",
    "GetChannelMembershipPreferencesRequestTypeDef",
    "GetChannelMembershipPreferencesResponseTypeDef",
    "GetChannelMessageRequestTypeDef",
    "GetChannelMessageResponseTypeDef",
    "GetChannelMessageStatusRequestTypeDef",
    "GetChannelMessageStatusResponseTypeDef",
    "GetMessagingSessionEndpointResponseTypeDef",
    "GetMessagingStreamingConfigurationsRequestTypeDef",
    "GetMessagingStreamingConfigurationsResponseTypeDef",
    "IdentityTypeDef",
    "LambdaConfigurationTypeDef",
    "ListChannelBansRequestTypeDef",
    "ListChannelBansResponseTypeDef",
    "ListChannelFlowsRequestTypeDef",
    "ListChannelFlowsResponseTypeDef",
    "ListChannelMembershipsForAppInstanceUserRequestTypeDef",
    "ListChannelMembershipsForAppInstanceUserResponseTypeDef",
    "ListChannelMembershipsRequestTypeDef",
    "ListChannelMembershipsResponseTypeDef",
    "ListChannelMessagesRequestTypeDef",
    "ListChannelMessagesResponseTypeDef",
    "ListChannelModeratorsRequestTypeDef",
    "ListChannelModeratorsResponseTypeDef",
    "ListChannelsAssociatedWithChannelFlowRequestTypeDef",
    "ListChannelsAssociatedWithChannelFlowResponseTypeDef",
    "ListChannelsModeratedByAppInstanceUserRequestTypeDef",
    "ListChannelsModeratedByAppInstanceUserResponseTypeDef",
    "ListChannelsRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListSubChannelsRequestTypeDef",
    "ListSubChannelsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MessageAttributeValueOutputTypeDef",
    "MessageAttributeValueTypeDef",
    "MessageAttributeValueUnionTypeDef",
    "MessagingSessionEndpointTypeDef",
    "ProcessorConfigurationTypeDef",
    "ProcessorTypeDef",
    "PushNotificationConfigurationTypeDef",
    "PushNotificationPreferencesTypeDef",
    "PutChannelExpirationSettingsRequestTypeDef",
    "PutChannelExpirationSettingsResponseTypeDef",
    "PutChannelMembershipPreferencesRequestTypeDef",
    "PutChannelMembershipPreferencesResponseTypeDef",
    "PutMessagingStreamingConfigurationsRequestTypeDef",
    "PutMessagingStreamingConfigurationsResponseTypeDef",
    "RedactChannelMessageRequestTypeDef",
    "RedactChannelMessageResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SearchChannelsRequestTypeDef",
    "SearchChannelsResponseTypeDef",
    "SearchFieldTypeDef",
    "SendChannelMessageRequestTypeDef",
    "SendChannelMessageResponseTypeDef",
    "StreamingConfigurationTypeDef",
    "SubChannelSummaryTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TargetTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateChannelFlowRequestTypeDef",
    "UpdateChannelFlowResponseTypeDef",
    "UpdateChannelMessageRequestTypeDef",
    "UpdateChannelMessageResponseTypeDef",
    "UpdateChannelReadMarkerRequestTypeDef",
    "UpdateChannelReadMarkerResponseTypeDef",
    "UpdateChannelRequestTypeDef",
    "UpdateChannelResponseTypeDef",
)

AppInstanceUserMembershipSummaryTypeDef = TypedDict(
    "AppInstanceUserMembershipSummaryTypeDef",
    {
        "Type": NotRequired[ChannelMembershipTypeType],
        "ReadMarkerTimestamp": NotRequired[datetime],
        "SubChannelId": NotRequired[str],
    },
)

class AssociateChannelFlowRequestTypeDef(TypedDict):
    ChannelArn: str
    ChannelFlowArn: str
    ChimeBearer: str

class IdentityTypeDef(TypedDict):
    Arn: NotRequired[str]
    Name: NotRequired[str]

class BatchCreateChannelMembershipErrorTypeDef(TypedDict):
    MemberArn: NotRequired[str]
    ErrorCode: NotRequired[ErrorCodeType]
    ErrorMessage: NotRequired[str]

BatchCreateChannelMembershipRequestTypeDef = TypedDict(
    "BatchCreateChannelMembershipRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArns": Sequence[str],
        "ChimeBearer": str,
        "Type": NotRequired[ChannelMembershipTypeType],
        "SubChannelId": NotRequired[str],
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ChannelAssociatedWithFlowSummaryTypeDef(TypedDict):
    Name: NotRequired[str]
    ChannelArn: NotRequired[str]
    Mode: NotRequired[ChannelModeType]
    Privacy: NotRequired[ChannelPrivacyType]
    Metadata: NotRequired[str]

class ChannelSummaryTypeDef(TypedDict):
    Name: NotRequired[str]
    ChannelArn: NotRequired[str]
    Mode: NotRequired[ChannelModeType]
    Privacy: NotRequired[ChannelPrivacyType]
    Metadata: NotRequired[str]
    LastMessageTimestamp: NotRequired[datetime]

class PushNotificationPreferencesTypeDef(TypedDict):
    AllowNotifications: AllowNotificationsType
    FilterRule: NotRequired[str]

PushNotificationConfigurationTypeDef = TypedDict(
    "PushNotificationConfigurationTypeDef",
    {
        "Title": NotRequired[str],
        "Body": NotRequired[str],
        "Type": NotRequired[PushNotificationTypeType],
    },
)

class ChannelMessageStatusStructureTypeDef(TypedDict):
    Value: NotRequired[ChannelMessageStatusType]
    Detail: NotRequired[str]

class MessageAttributeValueOutputTypeDef(TypedDict):
    StringValues: NotRequired[List[str]]

class TargetTypeDef(TypedDict):
    MemberArn: NotRequired[str]

class ElasticChannelConfigurationTypeDef(TypedDict):
    MaximumSubChannels: int
    TargetMembershipsPerSubChannel: int
    MinimumMembershipPercentage: int

class ExpirationSettingsTypeDef(TypedDict):
    ExpirationDays: int
    ExpirationCriterion: ExpirationCriterionType

class CreateChannelBanRequestTypeDef(TypedDict):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str

class TagTypeDef(TypedDict):
    Key: str
    Value: str

CreateChannelMembershipRequestTypeDef = TypedDict(
    "CreateChannelMembershipRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "Type": ChannelMembershipTypeType,
        "ChimeBearer": str,
        "SubChannelId": NotRequired[str],
    },
)

class CreateChannelModeratorRequestTypeDef(TypedDict):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: str

class DeleteChannelBanRequestTypeDef(TypedDict):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str

class DeleteChannelFlowRequestTypeDef(TypedDict):
    ChannelFlowArn: str

class DeleteChannelMembershipRequestTypeDef(TypedDict):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str
    SubChannelId: NotRequired[str]

class DeleteChannelMessageRequestTypeDef(TypedDict):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: NotRequired[str]

class DeleteChannelModeratorRequestTypeDef(TypedDict):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: str

class DeleteChannelRequestTypeDef(TypedDict):
    ChannelArn: str
    ChimeBearer: str

class DeleteMessagingStreamingConfigurationsRequestTypeDef(TypedDict):
    AppInstanceArn: str

class DescribeChannelBanRequestTypeDef(TypedDict):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str

class DescribeChannelFlowRequestTypeDef(TypedDict):
    ChannelFlowArn: str

class DescribeChannelMembershipForAppInstanceUserRequestTypeDef(TypedDict):
    ChannelArn: str
    AppInstanceUserArn: str
    ChimeBearer: str

class DescribeChannelMembershipRequestTypeDef(TypedDict):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str
    SubChannelId: NotRequired[str]

class DescribeChannelModeratedByAppInstanceUserRequestTypeDef(TypedDict):
    ChannelArn: str
    AppInstanceUserArn: str
    ChimeBearer: str

class DescribeChannelModeratorRequestTypeDef(TypedDict):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: str

class DescribeChannelRequestTypeDef(TypedDict):
    ChannelArn: str
    ChimeBearer: str

class DisassociateChannelFlowRequestTypeDef(TypedDict):
    ChannelArn: str
    ChannelFlowArn: str
    ChimeBearer: str

class GetChannelMembershipPreferencesRequestTypeDef(TypedDict):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str

class GetChannelMessageRequestTypeDef(TypedDict):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: NotRequired[str]

class GetChannelMessageStatusRequestTypeDef(TypedDict):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: NotRequired[str]

class MessagingSessionEndpointTypeDef(TypedDict):
    Url: NotRequired[str]

class GetMessagingStreamingConfigurationsRequestTypeDef(TypedDict):
    AppInstanceArn: str

class StreamingConfigurationTypeDef(TypedDict):
    DataType: MessagingDataTypeType
    ResourceArn: str

class LambdaConfigurationTypeDef(TypedDict):
    ResourceArn: str
    InvocationType: Literal["ASYNC"]

class ListChannelBansRequestTypeDef(TypedDict):
    ChannelArn: str
    ChimeBearer: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListChannelFlowsRequestTypeDef(TypedDict):
    AppInstanceArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListChannelMembershipsForAppInstanceUserRequestTypeDef(TypedDict):
    ChimeBearer: str
    AppInstanceUserArn: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

ListChannelMembershipsRequestTypeDef = TypedDict(
    "ListChannelMembershipsRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
        "Type": NotRequired[ChannelMembershipTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SubChannelId": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]

class ListChannelModeratorsRequestTypeDef(TypedDict):
    ChannelArn: str
    ChimeBearer: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListChannelsAssociatedWithChannelFlowRequestTypeDef(TypedDict):
    ChannelFlowArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListChannelsModeratedByAppInstanceUserRequestTypeDef(TypedDict):
    ChimeBearer: str
    AppInstanceUserArn: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListChannelsRequestTypeDef(TypedDict):
    AppInstanceArn: str
    ChimeBearer: str
    Privacy: NotRequired[ChannelPrivacyType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListSubChannelsRequestTypeDef(TypedDict):
    ChannelArn: str
    ChimeBearer: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class SubChannelSummaryTypeDef(TypedDict):
    SubChannelId: NotRequired[str]
    MembershipCount: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class MessageAttributeValueTypeDef(TypedDict):
    StringValues: NotRequired[Sequence[str]]

class RedactChannelMessageRequestTypeDef(TypedDict):
    ChannelArn: str
    MessageId: str
    ChimeBearer: str
    SubChannelId: NotRequired[str]

class SearchFieldTypeDef(TypedDict):
    Key: Literal["MEMBERS"]
    Values: Sequence[str]
    Operator: SearchFieldOperatorType

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateChannelMessageRequestTypeDef(TypedDict):
    ChannelArn: str
    MessageId: str
    Content: str
    ChimeBearer: str
    Metadata: NotRequired[str]
    SubChannelId: NotRequired[str]
    ContentType: NotRequired[str]

class UpdateChannelReadMarkerRequestTypeDef(TypedDict):
    ChannelArn: str
    ChimeBearer: str

class UpdateChannelRequestTypeDef(TypedDict):
    ChannelArn: str
    ChimeBearer: str
    Name: NotRequired[str]
    Mode: NotRequired[ChannelModeType]
    Metadata: NotRequired[str]

BatchChannelMembershipsTypeDef = TypedDict(
    "BatchChannelMembershipsTypeDef",
    {
        "InvitedBy": NotRequired[IdentityTypeDef],
        "Type": NotRequired[ChannelMembershipTypeType],
        "Members": NotRequired[List[IdentityTypeDef]],
        "ChannelArn": NotRequired[str],
        "SubChannelId": NotRequired[str],
    },
)

class ChannelBanSummaryTypeDef(TypedDict):
    Member: NotRequired[IdentityTypeDef]

class ChannelBanTypeDef(TypedDict):
    Member: NotRequired[IdentityTypeDef]
    ChannelArn: NotRequired[str]
    CreatedTimestamp: NotRequired[datetime]
    CreatedBy: NotRequired[IdentityTypeDef]

class ChannelMembershipSummaryTypeDef(TypedDict):
    Member: NotRequired[IdentityTypeDef]

ChannelMembershipTypeDef = TypedDict(
    "ChannelMembershipTypeDef",
    {
        "InvitedBy": NotRequired[IdentityTypeDef],
        "Type": NotRequired[ChannelMembershipTypeType],
        "Member": NotRequired[IdentityTypeDef],
        "ChannelArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "SubChannelId": NotRequired[str],
    },
)

class ChannelModeratorSummaryTypeDef(TypedDict):
    Moderator: NotRequired[IdentityTypeDef]

class ChannelModeratorTypeDef(TypedDict):
    Moderator: NotRequired[IdentityTypeDef]
    ChannelArn: NotRequired[str]
    CreatedTimestamp: NotRequired[datetime]
    CreatedBy: NotRequired[IdentityTypeDef]

class ChannelFlowCallbackResponseTypeDef(TypedDict):
    ChannelArn: str
    CallbackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelBanResponseTypeDef(TypedDict):
    ChannelArn: str
    Member: IdentityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelFlowResponseTypeDef(TypedDict):
    ChannelFlowArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelMembershipResponseTypeDef(TypedDict):
    ChannelArn: str
    Member: IdentityTypeDef
    SubChannelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelModeratorResponseTypeDef(TypedDict):
    ChannelArn: str
    ChannelModerator: IdentityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelResponseTypeDef(TypedDict):
    ChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class RedactChannelMessageResponseTypeDef(TypedDict):
    ChannelArn: str
    MessageId: str
    SubChannelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelFlowResponseTypeDef(TypedDict):
    ChannelFlowArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelReadMarkerResponseTypeDef(TypedDict):
    ChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelResponseTypeDef(TypedDict):
    ChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelsAssociatedWithChannelFlowResponseTypeDef(TypedDict):
    Channels: List[ChannelAssociatedWithFlowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ChannelMembershipForAppInstanceUserSummaryTypeDef(TypedDict):
    ChannelSummary: NotRequired[ChannelSummaryTypeDef]
    AppInstanceUserMembershipSummary: NotRequired[AppInstanceUserMembershipSummaryTypeDef]

class ChannelModeratedByAppInstanceUserSummaryTypeDef(TypedDict):
    ChannelSummary: NotRequired[ChannelSummaryTypeDef]

class ListChannelsResponseTypeDef(TypedDict):
    Channels: List[ChannelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SearchChannelsResponseTypeDef(TypedDict):
    Channels: List[ChannelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ChannelMembershipPreferencesTypeDef(TypedDict):
    PushNotifications: NotRequired[PushNotificationPreferencesTypeDef]

class GetChannelMessageStatusResponseTypeDef(TypedDict):
    Status: ChannelMessageStatusStructureTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SendChannelMessageResponseTypeDef(TypedDict):
    ChannelArn: str
    MessageId: str
    Status: ChannelMessageStatusStructureTypeDef
    SubChannelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelMessageResponseTypeDef(TypedDict):
    ChannelArn: str
    MessageId: str
    Status: ChannelMessageStatusStructureTypeDef
    SubChannelId: str
    ResponseMetadata: ResponseMetadataTypeDef

ChannelMessageSummaryTypeDef = TypedDict(
    "ChannelMessageSummaryTypeDef",
    {
        "MessageId": NotRequired[str],
        "Content": NotRequired[str],
        "Metadata": NotRequired[str],
        "Type": NotRequired[ChannelMessageTypeType],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "LastEditedTimestamp": NotRequired[datetime],
        "Sender": NotRequired[IdentityTypeDef],
        "Redacted": NotRequired[bool],
        "Status": NotRequired[ChannelMessageStatusStructureTypeDef],
        "MessageAttributes": NotRequired[Dict[str, MessageAttributeValueOutputTypeDef]],
        "ContentType": NotRequired[str],
        "Target": NotRequired[List[TargetTypeDef]],
    },
)
ChannelMessageTypeDef = TypedDict(
    "ChannelMessageTypeDef",
    {
        "ChannelArn": NotRequired[str],
        "MessageId": NotRequired[str],
        "Content": NotRequired[str],
        "Metadata": NotRequired[str],
        "Type": NotRequired[ChannelMessageTypeType],
        "CreatedTimestamp": NotRequired[datetime],
        "LastEditedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "Sender": NotRequired[IdentityTypeDef],
        "Redacted": NotRequired[bool],
        "Persistence": NotRequired[ChannelMessagePersistenceTypeType],
        "Status": NotRequired[ChannelMessageStatusStructureTypeDef],
        "MessageAttributes": NotRequired[Dict[str, MessageAttributeValueOutputTypeDef]],
        "SubChannelId": NotRequired[str],
        "ContentType": NotRequired[str],
        "Target": NotRequired[List[TargetTypeDef]],
    },
)

class ChannelTypeDef(TypedDict):
    Name: NotRequired[str]
    ChannelArn: NotRequired[str]
    Mode: NotRequired[ChannelModeType]
    Privacy: NotRequired[ChannelPrivacyType]
    Metadata: NotRequired[str]
    CreatedBy: NotRequired[IdentityTypeDef]
    CreatedTimestamp: NotRequired[datetime]
    LastMessageTimestamp: NotRequired[datetime]
    LastUpdatedTimestamp: NotRequired[datetime]
    ChannelFlowArn: NotRequired[str]
    ElasticChannelConfiguration: NotRequired[ElasticChannelConfigurationTypeDef]
    ExpirationSettings: NotRequired[ExpirationSettingsTypeDef]

class PutChannelExpirationSettingsRequestTypeDef(TypedDict):
    ChannelArn: str
    ChimeBearer: NotRequired[str]
    ExpirationSettings: NotRequired[ExpirationSettingsTypeDef]

class PutChannelExpirationSettingsResponseTypeDef(TypedDict):
    ChannelArn: str
    ExpirationSettings: ExpirationSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelRequestTypeDef(TypedDict):
    AppInstanceArn: str
    Name: str
    ClientRequestToken: str
    ChimeBearer: str
    Mode: NotRequired[ChannelModeType]
    Privacy: NotRequired[ChannelPrivacyType]
    Metadata: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ChannelId: NotRequired[str]
    MemberArns: NotRequired[Sequence[str]]
    ModeratorArns: NotRequired[Sequence[str]]
    ElasticChannelConfiguration: NotRequired[ElasticChannelConfigurationTypeDef]
    ExpirationSettings: NotRequired[ExpirationSettingsTypeDef]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class GetMessagingSessionEndpointResponseTypeDef(TypedDict):
    Endpoint: MessagingSessionEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMessagingStreamingConfigurationsResponseTypeDef(TypedDict):
    StreamingConfigurations: List[StreamingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutMessagingStreamingConfigurationsRequestTypeDef(TypedDict):
    AppInstanceArn: str
    StreamingConfigurations: Sequence[StreamingConfigurationTypeDef]

class PutMessagingStreamingConfigurationsResponseTypeDef(TypedDict):
    StreamingConfigurations: List[StreamingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ProcessorConfigurationTypeDef(TypedDict):
    Lambda: LambdaConfigurationTypeDef

class ListChannelMessagesRequestTypeDef(TypedDict):
    ChannelArn: str
    ChimeBearer: str
    SortOrder: NotRequired[SortOrderType]
    NotBefore: NotRequired[TimestampTypeDef]
    NotAfter: NotRequired[TimestampTypeDef]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    SubChannelId: NotRequired[str]

class ListSubChannelsResponseTypeDef(TypedDict):
    ChannelArn: str
    SubChannels: List[SubChannelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

MessageAttributeValueUnionTypeDef = Union[
    MessageAttributeValueTypeDef, MessageAttributeValueOutputTypeDef
]

class SearchChannelsRequestTypeDef(TypedDict):
    Fields: Sequence[SearchFieldTypeDef]
    ChimeBearer: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class BatchCreateChannelMembershipResponseTypeDef(TypedDict):
    BatchChannelMemberships: BatchChannelMembershipsTypeDef
    Errors: List[BatchCreateChannelMembershipErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelBansResponseTypeDef(TypedDict):
    ChannelArn: str
    ChannelBans: List[ChannelBanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeChannelBanResponseTypeDef(TypedDict):
    ChannelBan: ChannelBanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelMembershipsResponseTypeDef(TypedDict):
    ChannelArn: str
    ChannelMemberships: List[ChannelMembershipSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeChannelMembershipResponseTypeDef(TypedDict):
    ChannelMembership: ChannelMembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelModeratorsResponseTypeDef(TypedDict):
    ChannelArn: str
    ChannelModerators: List[ChannelModeratorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeChannelModeratorResponseTypeDef(TypedDict):
    ChannelModerator: ChannelModeratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelMembershipForAppInstanceUserResponseTypeDef(TypedDict):
    ChannelMembership: ChannelMembershipForAppInstanceUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelMembershipsForAppInstanceUserResponseTypeDef(TypedDict):
    ChannelMemberships: List[ChannelMembershipForAppInstanceUserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeChannelModeratedByAppInstanceUserResponseTypeDef(TypedDict):
    Channel: ChannelModeratedByAppInstanceUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelsModeratedByAppInstanceUserResponseTypeDef(TypedDict):
    Channels: List[ChannelModeratedByAppInstanceUserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetChannelMembershipPreferencesResponseTypeDef(TypedDict):
    ChannelArn: str
    Member: IdentityTypeDef
    Preferences: ChannelMembershipPreferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutChannelMembershipPreferencesRequestTypeDef(TypedDict):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: str
    Preferences: ChannelMembershipPreferencesTypeDef

class PutChannelMembershipPreferencesResponseTypeDef(TypedDict):
    ChannelArn: str
    Member: IdentityTypeDef
    Preferences: ChannelMembershipPreferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelMessagesResponseTypeDef(TypedDict):
    ChannelArn: str
    ChannelMessages: List[ChannelMessageSummaryTypeDef]
    SubChannelId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetChannelMessageResponseTypeDef(TypedDict):
    ChannelMessage: ChannelMessageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelResponseTypeDef(TypedDict):
    Channel: ChannelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ProcessorTypeDef(TypedDict):
    Name: str
    Configuration: ProcessorConfigurationTypeDef
    ExecutionOrder: int
    FallbackAction: FallbackActionType

class ChannelMessageCallbackTypeDef(TypedDict):
    MessageId: str
    Content: NotRequired[str]
    Metadata: NotRequired[str]
    PushNotification: NotRequired[PushNotificationConfigurationTypeDef]
    MessageAttributes: NotRequired[Mapping[str, MessageAttributeValueUnionTypeDef]]
    SubChannelId: NotRequired[str]
    ContentType: NotRequired[str]

SendChannelMessageRequestTypeDef = TypedDict(
    "SendChannelMessageRequestTypeDef",
    {
        "ChannelArn": str,
        "Content": str,
        "Type": ChannelMessageTypeType,
        "Persistence": ChannelMessagePersistenceTypeType,
        "ClientRequestToken": str,
        "ChimeBearer": str,
        "Metadata": NotRequired[str],
        "PushNotification": NotRequired[PushNotificationConfigurationTypeDef],
        "MessageAttributes": NotRequired[Mapping[str, MessageAttributeValueUnionTypeDef]],
        "SubChannelId": NotRequired[str],
        "ContentType": NotRequired[str],
        "Target": NotRequired[Sequence[TargetTypeDef]],
    },
)

class ChannelFlowSummaryTypeDef(TypedDict):
    ChannelFlowArn: NotRequired[str]
    Name: NotRequired[str]
    Processors: NotRequired[List[ProcessorTypeDef]]

class ChannelFlowTypeDef(TypedDict):
    ChannelFlowArn: NotRequired[str]
    Processors: NotRequired[List[ProcessorTypeDef]]
    Name: NotRequired[str]
    CreatedTimestamp: NotRequired[datetime]
    LastUpdatedTimestamp: NotRequired[datetime]

class CreateChannelFlowRequestTypeDef(TypedDict):
    AppInstanceArn: str
    Processors: Sequence[ProcessorTypeDef]
    Name: str
    ClientRequestToken: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class UpdateChannelFlowRequestTypeDef(TypedDict):
    ChannelFlowArn: str
    Processors: Sequence[ProcessorTypeDef]
    Name: str

class ChannelFlowCallbackRequestTypeDef(TypedDict):
    CallbackId: str
    ChannelArn: str
    ChannelMessage: ChannelMessageCallbackTypeDef
    DeleteResource: NotRequired[bool]

class ListChannelFlowsResponseTypeDef(TypedDict):
    ChannelFlows: List[ChannelFlowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeChannelFlowResponseTypeDef(TypedDict):
    ChannelFlow: ChannelFlowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
