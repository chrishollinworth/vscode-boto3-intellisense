"""
Type annotations for chime-sdk-messaging service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/type_defs.html)

Usage::

    ```python
    from mypy_boto3_chime_sdk_messaging.type_defs import AppInstanceUserMembershipSummaryTypeDef

    data: AppInstanceUserMembershipSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AllowNotificationsType,
    ChannelMembershipTypeType,
    ChannelMessagePersistenceTypeType,
    ChannelMessageStatusType,
    ChannelMessageTypeType,
    ChannelModeType,
    ChannelPrivacyType,
    ErrorCodeType,
    FallbackActionType,
    PushNotificationTypeType,
    SearchFieldOperatorType,
    SortOrderType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AppInstanceUserMembershipSummaryTypeDef",
    "AssociateChannelFlowRequestRequestTypeDef",
    "BatchChannelMembershipsTypeDef",
    "BatchCreateChannelMembershipErrorTypeDef",
    "BatchCreateChannelMembershipRequestRequestTypeDef",
    "BatchCreateChannelMembershipResponseTypeDef",
    "ChannelAssociatedWithFlowSummaryTypeDef",
    "ChannelBanSummaryTypeDef",
    "ChannelBanTypeDef",
    "ChannelFlowCallbackRequestRequestTypeDef",
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
    "CreateChannelBanRequestRequestTypeDef",
    "CreateChannelBanResponseTypeDef",
    "CreateChannelFlowRequestRequestTypeDef",
    "CreateChannelFlowResponseTypeDef",
    "CreateChannelMembershipRequestRequestTypeDef",
    "CreateChannelMembershipResponseTypeDef",
    "CreateChannelModeratorRequestRequestTypeDef",
    "CreateChannelModeratorResponseTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "DeleteChannelBanRequestRequestTypeDef",
    "DeleteChannelFlowRequestRequestTypeDef",
    "DeleteChannelMembershipRequestRequestTypeDef",
    "DeleteChannelMessageRequestRequestTypeDef",
    "DeleteChannelModeratorRequestRequestTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DescribeChannelBanRequestRequestTypeDef",
    "DescribeChannelBanResponseTypeDef",
    "DescribeChannelFlowRequestRequestTypeDef",
    "DescribeChannelFlowResponseTypeDef",
    "DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef",
    "DescribeChannelMembershipForAppInstanceUserResponseTypeDef",
    "DescribeChannelMembershipRequestRequestTypeDef",
    "DescribeChannelMembershipResponseTypeDef",
    "DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef",
    "DescribeChannelModeratedByAppInstanceUserResponseTypeDef",
    "DescribeChannelModeratorRequestRequestTypeDef",
    "DescribeChannelModeratorResponseTypeDef",
    "DescribeChannelRequestRequestTypeDef",
    "DescribeChannelResponseTypeDef",
    "DisassociateChannelFlowRequestRequestTypeDef",
    "GetChannelMembershipPreferencesRequestRequestTypeDef",
    "GetChannelMembershipPreferencesResponseTypeDef",
    "GetChannelMessageRequestRequestTypeDef",
    "GetChannelMessageResponseTypeDef",
    "GetChannelMessageStatusRequestRequestTypeDef",
    "GetChannelMessageStatusResponseTypeDef",
    "GetMessagingSessionEndpointResponseTypeDef",
    "IdentityTypeDef",
    "LambdaConfigurationTypeDef",
    "ListChannelBansRequestRequestTypeDef",
    "ListChannelBansResponseTypeDef",
    "ListChannelFlowsRequestRequestTypeDef",
    "ListChannelFlowsResponseTypeDef",
    "ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef",
    "ListChannelMembershipsForAppInstanceUserResponseTypeDef",
    "ListChannelMembershipsRequestRequestTypeDef",
    "ListChannelMembershipsResponseTypeDef",
    "ListChannelMessagesRequestRequestTypeDef",
    "ListChannelMessagesResponseTypeDef",
    "ListChannelModeratorsRequestRequestTypeDef",
    "ListChannelModeratorsResponseTypeDef",
    "ListChannelsAssociatedWithChannelFlowRequestRequestTypeDef",
    "ListChannelsAssociatedWithChannelFlowResponseTypeDef",
    "ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef",
    "ListChannelsModeratedByAppInstanceUserResponseTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MessageAttributeValueTypeDef",
    "MessagingSessionEndpointTypeDef",
    "ProcessorConfigurationTypeDef",
    "ProcessorTypeDef",
    "PushNotificationConfigurationTypeDef",
    "PushNotificationPreferencesTypeDef",
    "PutChannelMembershipPreferencesRequestRequestTypeDef",
    "PutChannelMembershipPreferencesResponseTypeDef",
    "RedactChannelMessageRequestRequestTypeDef",
    "RedactChannelMessageResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SearchChannelsRequestRequestTypeDef",
    "SearchChannelsResponseTypeDef",
    "SearchFieldTypeDef",
    "SendChannelMessageRequestRequestTypeDef",
    "SendChannelMessageResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateChannelFlowRequestRequestTypeDef",
    "UpdateChannelFlowResponseTypeDef",
    "UpdateChannelMessageRequestRequestTypeDef",
    "UpdateChannelMessageResponseTypeDef",
    "UpdateChannelReadMarkerRequestRequestTypeDef",
    "UpdateChannelReadMarkerResponseTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "UpdateChannelResponseTypeDef",
)

AppInstanceUserMembershipSummaryTypeDef = TypedDict(
    "AppInstanceUserMembershipSummaryTypeDef",
    {
        "Type": ChannelMembershipTypeType,
        "ReadMarkerTimestamp": datetime,
    },
    total=False,
)

AssociateChannelFlowRequestRequestTypeDef = TypedDict(
    "AssociateChannelFlowRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelFlowArn": str,
        "ChimeBearer": str,
    },
)

BatchChannelMembershipsTypeDef = TypedDict(
    "BatchChannelMembershipsTypeDef",
    {
        "InvitedBy": "IdentityTypeDef",
        "Type": ChannelMembershipTypeType,
        "Members": List["IdentityTypeDef"],
        "ChannelArn": str,
    },
    total=False,
)

BatchCreateChannelMembershipErrorTypeDef = TypedDict(
    "BatchCreateChannelMembershipErrorTypeDef",
    {
        "MemberArn": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredBatchCreateChannelMembershipRequestRequestTypeDef = TypedDict(
    "_RequiredBatchCreateChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArns": List[str],
        "ChimeBearer": str,
    },
)
_OptionalBatchCreateChannelMembershipRequestRequestTypeDef = TypedDict(
    "_OptionalBatchCreateChannelMembershipRequestRequestTypeDef",
    {
        "Type": ChannelMembershipTypeType,
    },
    total=False,
)

class BatchCreateChannelMembershipRequestRequestTypeDef(
    _RequiredBatchCreateChannelMembershipRequestRequestTypeDef,
    _OptionalBatchCreateChannelMembershipRequestRequestTypeDef,
):
    pass

BatchCreateChannelMembershipResponseTypeDef = TypedDict(
    "BatchCreateChannelMembershipResponseTypeDef",
    {
        "BatchChannelMemberships": "BatchChannelMembershipsTypeDef",
        "Errors": List["BatchCreateChannelMembershipErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChannelAssociatedWithFlowSummaryTypeDef = TypedDict(
    "ChannelAssociatedWithFlowSummaryTypeDef",
    {
        "Name": str,
        "ChannelArn": str,
        "Mode": ChannelModeType,
        "Privacy": ChannelPrivacyType,
        "Metadata": str,
    },
    total=False,
)

ChannelBanSummaryTypeDef = TypedDict(
    "ChannelBanSummaryTypeDef",
    {
        "Member": "IdentityTypeDef",
    },
    total=False,
)

ChannelBanTypeDef = TypedDict(
    "ChannelBanTypeDef",
    {
        "Member": "IdentityTypeDef",
        "ChannelArn": str,
        "CreatedTimestamp": datetime,
        "CreatedBy": "IdentityTypeDef",
    },
    total=False,
)

_RequiredChannelFlowCallbackRequestRequestTypeDef = TypedDict(
    "_RequiredChannelFlowCallbackRequestRequestTypeDef",
    {
        "CallbackId": str,
        "ChannelArn": str,
        "ChannelMessage": "ChannelMessageCallbackTypeDef",
    },
)
_OptionalChannelFlowCallbackRequestRequestTypeDef = TypedDict(
    "_OptionalChannelFlowCallbackRequestRequestTypeDef",
    {
        "DeleteResource": bool,
    },
    total=False,
)

class ChannelFlowCallbackRequestRequestTypeDef(
    _RequiredChannelFlowCallbackRequestRequestTypeDef,
    _OptionalChannelFlowCallbackRequestRequestTypeDef,
):
    pass

ChannelFlowCallbackResponseTypeDef = TypedDict(
    "ChannelFlowCallbackResponseTypeDef",
    {
        "ChannelArn": str,
        "CallbackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChannelFlowSummaryTypeDef = TypedDict(
    "ChannelFlowSummaryTypeDef",
    {
        "ChannelFlowArn": str,
        "Name": str,
        "Processors": List["ProcessorTypeDef"],
    },
    total=False,
)

ChannelFlowTypeDef = TypedDict(
    "ChannelFlowTypeDef",
    {
        "ChannelFlowArn": str,
        "Processors": List["ProcessorTypeDef"],
        "Name": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
    },
    total=False,
)

ChannelMembershipForAppInstanceUserSummaryTypeDef = TypedDict(
    "ChannelMembershipForAppInstanceUserSummaryTypeDef",
    {
        "ChannelSummary": "ChannelSummaryTypeDef",
        "AppInstanceUserMembershipSummary": "AppInstanceUserMembershipSummaryTypeDef",
    },
    total=False,
)

ChannelMembershipPreferencesTypeDef = TypedDict(
    "ChannelMembershipPreferencesTypeDef",
    {
        "PushNotifications": "PushNotificationPreferencesTypeDef",
    },
    total=False,
)

ChannelMembershipSummaryTypeDef = TypedDict(
    "ChannelMembershipSummaryTypeDef",
    {
        "Member": "IdentityTypeDef",
    },
    total=False,
)

ChannelMembershipTypeDef = TypedDict(
    "ChannelMembershipTypeDef",
    {
        "InvitedBy": "IdentityTypeDef",
        "Type": ChannelMembershipTypeType,
        "Member": "IdentityTypeDef",
        "ChannelArn": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
    },
    total=False,
)

_RequiredChannelMessageCallbackTypeDef = TypedDict(
    "_RequiredChannelMessageCallbackTypeDef",
    {
        "MessageId": str,
    },
)
_OptionalChannelMessageCallbackTypeDef = TypedDict(
    "_OptionalChannelMessageCallbackTypeDef",
    {
        "Content": str,
        "Metadata": str,
        "PushNotification": "PushNotificationConfigurationTypeDef",
        "MessageAttributes": Dict[str, "MessageAttributeValueTypeDef"],
    },
    total=False,
)

class ChannelMessageCallbackTypeDef(
    _RequiredChannelMessageCallbackTypeDef, _OptionalChannelMessageCallbackTypeDef
):
    pass

ChannelMessageStatusStructureTypeDef = TypedDict(
    "ChannelMessageStatusStructureTypeDef",
    {
        "Value": ChannelMessageStatusType,
        "Detail": str,
    },
    total=False,
)

ChannelMessageSummaryTypeDef = TypedDict(
    "ChannelMessageSummaryTypeDef",
    {
        "MessageId": str,
        "Content": str,
        "Metadata": str,
        "Type": ChannelMessageTypeType,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "LastEditedTimestamp": datetime,
        "Sender": "IdentityTypeDef",
        "Redacted": bool,
        "Status": "ChannelMessageStatusStructureTypeDef",
        "MessageAttributes": Dict[str, "MessageAttributeValueTypeDef"],
    },
    total=False,
)

ChannelMessageTypeDef = TypedDict(
    "ChannelMessageTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "Content": str,
        "Metadata": str,
        "Type": ChannelMessageTypeType,
        "CreatedTimestamp": datetime,
        "LastEditedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "Sender": "IdentityTypeDef",
        "Redacted": bool,
        "Persistence": ChannelMessagePersistenceTypeType,
        "Status": "ChannelMessageStatusStructureTypeDef",
        "MessageAttributes": Dict[str, "MessageAttributeValueTypeDef"],
    },
    total=False,
)

ChannelModeratedByAppInstanceUserSummaryTypeDef = TypedDict(
    "ChannelModeratedByAppInstanceUserSummaryTypeDef",
    {
        "ChannelSummary": "ChannelSummaryTypeDef",
    },
    total=False,
)

ChannelModeratorSummaryTypeDef = TypedDict(
    "ChannelModeratorSummaryTypeDef",
    {
        "Moderator": "IdentityTypeDef",
    },
    total=False,
)

ChannelModeratorTypeDef = TypedDict(
    "ChannelModeratorTypeDef",
    {
        "Moderator": "IdentityTypeDef",
        "ChannelArn": str,
        "CreatedTimestamp": datetime,
        "CreatedBy": "IdentityTypeDef",
    },
    total=False,
)

ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "Name": str,
        "ChannelArn": str,
        "Mode": ChannelModeType,
        "Privacy": ChannelPrivacyType,
        "Metadata": str,
        "LastMessageTimestamp": datetime,
    },
    total=False,
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "Name": str,
        "ChannelArn": str,
        "Mode": ChannelModeType,
        "Privacy": ChannelPrivacyType,
        "Metadata": str,
        "CreatedBy": "IdentityTypeDef",
        "CreatedTimestamp": datetime,
        "LastMessageTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "ChannelFlowArn": str,
    },
    total=False,
)

CreateChannelBanRequestRequestTypeDef = TypedDict(
    "CreateChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)

CreateChannelBanResponseTypeDef = TypedDict(
    "CreateChannelBanResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": "IdentityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateChannelFlowRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChannelFlowRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Processors": List["ProcessorTypeDef"],
        "Name": str,
        "ClientRequestToken": str,
    },
)
_OptionalCreateChannelFlowRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChannelFlowRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateChannelFlowRequestRequestTypeDef(
    _RequiredCreateChannelFlowRequestRequestTypeDef, _OptionalCreateChannelFlowRequestRequestTypeDef
):
    pass

CreateChannelFlowResponseTypeDef = TypedDict(
    "CreateChannelFlowResponseTypeDef",
    {
        "ChannelFlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateChannelMembershipRequestRequestTypeDef = TypedDict(
    "CreateChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "Type": ChannelMembershipTypeType,
        "ChimeBearer": str,
    },
)

CreateChannelMembershipResponseTypeDef = TypedDict(
    "CreateChannelMembershipResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": "IdentityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateChannelModeratorRequestRequestTypeDef = TypedDict(
    "CreateChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
        "ChimeBearer": str,
    },
)

CreateChannelModeratorResponseTypeDef = TypedDict(
    "CreateChannelModeratorResponseTypeDef",
    {
        "ChannelArn": str,
        "ChannelModerator": "IdentityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateChannelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChannelRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "ClientRequestToken": str,
        "ChimeBearer": str,
    },
)
_OptionalCreateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChannelRequestRequestTypeDef",
    {
        "Mode": ChannelModeType,
        "Privacy": ChannelPrivacyType,
        "Metadata": str,
        "Tags": List["TagTypeDef"],
        "ChannelId": str,
        "MemberArns": List[str],
        "ModeratorArns": List[str],
    },
    total=False,
)

class CreateChannelRequestRequestTypeDef(
    _RequiredCreateChannelRequestRequestTypeDef, _OptionalCreateChannelRequestRequestTypeDef
):
    pass

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteChannelBanRequestRequestTypeDef = TypedDict(
    "DeleteChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)

DeleteChannelFlowRequestRequestTypeDef = TypedDict(
    "DeleteChannelFlowRequestRequestTypeDef",
    {
        "ChannelFlowArn": str,
    },
)

DeleteChannelMembershipRequestRequestTypeDef = TypedDict(
    "DeleteChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)

DeleteChannelMessageRequestRequestTypeDef = TypedDict(
    "DeleteChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": str,
    },
)

DeleteChannelModeratorRequestRequestTypeDef = TypedDict(
    "DeleteChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
        "ChimeBearer": str,
    },
)

DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)

DescribeChannelBanRequestRequestTypeDef = TypedDict(
    "DescribeChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)

DescribeChannelBanResponseTypeDef = TypedDict(
    "DescribeChannelBanResponseTypeDef",
    {
        "ChannelBan": "ChannelBanTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChannelFlowRequestRequestTypeDef = TypedDict(
    "DescribeChannelFlowRequestRequestTypeDef",
    {
        "ChannelFlowArn": str,
    },
)

DescribeChannelFlowResponseTypeDef = TypedDict(
    "DescribeChannelFlowResponseTypeDef",
    {
        "ChannelFlow": "ChannelFlowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "AppInstanceUserArn": str,
        "ChimeBearer": str,
    },
)

DescribeChannelMembershipForAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeChannelMembershipForAppInstanceUserResponseTypeDef",
    {
        "ChannelMembership": "ChannelMembershipForAppInstanceUserSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChannelMembershipRequestRequestTypeDef = TypedDict(
    "DescribeChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)

DescribeChannelMembershipResponseTypeDef = TypedDict(
    "DescribeChannelMembershipResponseTypeDef",
    {
        "ChannelMembership": "ChannelMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "AppInstanceUserArn": str,
        "ChimeBearer": str,
    },
)

DescribeChannelModeratedByAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeChannelModeratedByAppInstanceUserResponseTypeDef",
    {
        "Channel": "ChannelModeratedByAppInstanceUserSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChannelModeratorRequestRequestTypeDef = TypedDict(
    "DescribeChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
        "ChimeBearer": str,
    },
)

DescribeChannelModeratorResponseTypeDef = TypedDict(
    "DescribeChannelModeratorResponseTypeDef",
    {
        "ChannelModerator": "ChannelModeratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChannelRequestRequestTypeDef = TypedDict(
    "DescribeChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)

DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "Channel": "ChannelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateChannelFlowRequestRequestTypeDef = TypedDict(
    "DisassociateChannelFlowRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelFlowArn": str,
        "ChimeBearer": str,
    },
)

GetChannelMembershipPreferencesRequestRequestTypeDef = TypedDict(
    "GetChannelMembershipPreferencesRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)

GetChannelMembershipPreferencesResponseTypeDef = TypedDict(
    "GetChannelMembershipPreferencesResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": "IdentityTypeDef",
        "Preferences": "ChannelMembershipPreferencesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChannelMessageRequestRequestTypeDef = TypedDict(
    "GetChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": str,
    },
)

GetChannelMessageResponseTypeDef = TypedDict(
    "GetChannelMessageResponseTypeDef",
    {
        "ChannelMessage": "ChannelMessageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChannelMessageStatusRequestRequestTypeDef = TypedDict(
    "GetChannelMessageStatusRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": str,
    },
)

GetChannelMessageStatusResponseTypeDef = TypedDict(
    "GetChannelMessageStatusResponseTypeDef",
    {
        "Status": "ChannelMessageStatusStructureTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMessagingSessionEndpointResponseTypeDef = TypedDict(
    "GetMessagingSessionEndpointResponseTypeDef",
    {
        "Endpoint": "MessagingSessionEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

LambdaConfigurationTypeDef = TypedDict(
    "LambdaConfigurationTypeDef",
    {
        "ResourceArn": str,
        "InvocationType": Literal["ASYNC"],
    },
)

_RequiredListChannelBansRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelBansRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)
_OptionalListChannelBansRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelBansRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListChannelBansRequestRequestTypeDef(
    _RequiredListChannelBansRequestRequestTypeDef, _OptionalListChannelBansRequestRequestTypeDef
):
    pass

ListChannelBansResponseTypeDef = TypedDict(
    "ListChannelBansResponseTypeDef",
    {
        "ChannelArn": str,
        "NextToken": str,
        "ChannelBans": List["ChannelBanSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChannelFlowsRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelFlowsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
_OptionalListChannelFlowsRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelFlowsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListChannelFlowsRequestRequestTypeDef(
    _RequiredListChannelFlowsRequestRequestTypeDef, _OptionalListChannelFlowsRequestRequestTypeDef
):
    pass

ListChannelFlowsResponseTypeDef = TypedDict(
    "ListChannelFlowsResponseTypeDef",
    {
        "ChannelFlows": List["ChannelFlowSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChannelMembershipsForAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelMembershipsForAppInstanceUserRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
)
_OptionalListChannelMembershipsForAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelMembershipsForAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef(
    _RequiredListChannelMembershipsForAppInstanceUserRequestRequestTypeDef,
    _OptionalListChannelMembershipsForAppInstanceUserRequestRequestTypeDef,
):
    pass

ListChannelMembershipsForAppInstanceUserResponseTypeDef = TypedDict(
    "ListChannelMembershipsForAppInstanceUserResponseTypeDef",
    {
        "ChannelMemberships": List["ChannelMembershipForAppInstanceUserSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChannelMembershipsRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelMembershipsRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)
_OptionalListChannelMembershipsRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelMembershipsRequestRequestTypeDef",
    {
        "Type": ChannelMembershipTypeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListChannelMembershipsRequestRequestTypeDef(
    _RequiredListChannelMembershipsRequestRequestTypeDef,
    _OptionalListChannelMembershipsRequestRequestTypeDef,
):
    pass

ListChannelMembershipsResponseTypeDef = TypedDict(
    "ListChannelMembershipsResponseTypeDef",
    {
        "ChannelArn": str,
        "ChannelMemberships": List["ChannelMembershipSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChannelMessagesRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelMessagesRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)
_OptionalListChannelMessagesRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelMessagesRequestRequestTypeDef",
    {
        "SortOrder": SortOrderType,
        "NotBefore": Union[datetime, str],
        "NotAfter": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListChannelMessagesRequestRequestTypeDef(
    _RequiredListChannelMessagesRequestRequestTypeDef,
    _OptionalListChannelMessagesRequestRequestTypeDef,
):
    pass

ListChannelMessagesResponseTypeDef = TypedDict(
    "ListChannelMessagesResponseTypeDef",
    {
        "ChannelArn": str,
        "NextToken": str,
        "ChannelMessages": List["ChannelMessageSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChannelModeratorsRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelModeratorsRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)
_OptionalListChannelModeratorsRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelModeratorsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListChannelModeratorsRequestRequestTypeDef(
    _RequiredListChannelModeratorsRequestRequestTypeDef,
    _OptionalListChannelModeratorsRequestRequestTypeDef,
):
    pass

ListChannelModeratorsResponseTypeDef = TypedDict(
    "ListChannelModeratorsResponseTypeDef",
    {
        "ChannelArn": str,
        "NextToken": str,
        "ChannelModerators": List["ChannelModeratorSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChannelsAssociatedWithChannelFlowRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelsAssociatedWithChannelFlowRequestRequestTypeDef",
    {
        "ChannelFlowArn": str,
    },
)
_OptionalListChannelsAssociatedWithChannelFlowRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelsAssociatedWithChannelFlowRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListChannelsAssociatedWithChannelFlowRequestRequestTypeDef(
    _RequiredListChannelsAssociatedWithChannelFlowRequestRequestTypeDef,
    _OptionalListChannelsAssociatedWithChannelFlowRequestRequestTypeDef,
):
    pass

ListChannelsAssociatedWithChannelFlowResponseTypeDef = TypedDict(
    "ListChannelsAssociatedWithChannelFlowResponseTypeDef",
    {
        "Channels": List["ChannelAssociatedWithFlowSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChannelsModeratedByAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelsModeratedByAppInstanceUserRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
)
_OptionalListChannelsModeratedByAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelsModeratedByAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef(
    _RequiredListChannelsModeratedByAppInstanceUserRequestRequestTypeDef,
    _OptionalListChannelsModeratedByAppInstanceUserRequestRequestTypeDef,
):
    pass

ListChannelsModeratedByAppInstanceUserResponseTypeDef = TypedDict(
    "ListChannelsModeratedByAppInstanceUserResponseTypeDef",
    {
        "Channels": List["ChannelModeratedByAppInstanceUserSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChannelsRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "ChimeBearer": str,
    },
)
_OptionalListChannelsRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelsRequestRequestTypeDef",
    {
        "Privacy": ChannelPrivacyType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListChannelsRequestRequestTypeDef(
    _RequiredListChannelsRequestRequestTypeDef, _OptionalListChannelsRequestRequestTypeDef
):
    pass

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "Channels": List["ChannelSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MessageAttributeValueTypeDef = TypedDict(
    "MessageAttributeValueTypeDef",
    {
        "StringValues": List[str],
    },
    total=False,
)

MessagingSessionEndpointTypeDef = TypedDict(
    "MessagingSessionEndpointTypeDef",
    {
        "Url": str,
    },
    total=False,
)

ProcessorConfigurationTypeDef = TypedDict(
    "ProcessorConfigurationTypeDef",
    {
        "Lambda": "LambdaConfigurationTypeDef",
    },
)

ProcessorTypeDef = TypedDict(
    "ProcessorTypeDef",
    {
        "Name": str,
        "Configuration": "ProcessorConfigurationTypeDef",
        "ExecutionOrder": int,
        "FallbackAction": FallbackActionType,
    },
)

PushNotificationConfigurationTypeDef = TypedDict(
    "PushNotificationConfigurationTypeDef",
    {
        "Title": str,
        "Body": str,
        "Type": PushNotificationTypeType,
    },
    total=False,
)

_RequiredPushNotificationPreferencesTypeDef = TypedDict(
    "_RequiredPushNotificationPreferencesTypeDef",
    {
        "AllowNotifications": AllowNotificationsType,
    },
)
_OptionalPushNotificationPreferencesTypeDef = TypedDict(
    "_OptionalPushNotificationPreferencesTypeDef",
    {
        "FilterRule": str,
    },
    total=False,
)

class PushNotificationPreferencesTypeDef(
    _RequiredPushNotificationPreferencesTypeDef, _OptionalPushNotificationPreferencesTypeDef
):
    pass

PutChannelMembershipPreferencesRequestRequestTypeDef = TypedDict(
    "PutChannelMembershipPreferencesRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
        "Preferences": "ChannelMembershipPreferencesTypeDef",
    },
)

PutChannelMembershipPreferencesResponseTypeDef = TypedDict(
    "PutChannelMembershipPreferencesResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": "IdentityTypeDef",
        "Preferences": "ChannelMembershipPreferencesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RedactChannelMessageRequestRequestTypeDef = TypedDict(
    "RedactChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": str,
    },
)

RedactChannelMessageResponseTypeDef = TypedDict(
    "RedactChannelMessageResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredSearchChannelsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchChannelsRequestRequestTypeDef",
    {
        "Fields": List["SearchFieldTypeDef"],
    },
)
_OptionalSearchChannelsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchChannelsRequestRequestTypeDef",
    {
        "ChimeBearer": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class SearchChannelsRequestRequestTypeDef(
    _RequiredSearchChannelsRequestRequestTypeDef, _OptionalSearchChannelsRequestRequestTypeDef
):
    pass

SearchChannelsResponseTypeDef = TypedDict(
    "SearchChannelsResponseTypeDef",
    {
        "Channels": List["ChannelSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchFieldTypeDef = TypedDict(
    "SearchFieldTypeDef",
    {
        "Key": Literal["MEMBERS"],
        "Values": List[str],
        "Operator": SearchFieldOperatorType,
    },
)

_RequiredSendChannelMessageRequestRequestTypeDef = TypedDict(
    "_RequiredSendChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "Content": str,
        "Type": ChannelMessageTypeType,
        "Persistence": ChannelMessagePersistenceTypeType,
        "ClientRequestToken": str,
        "ChimeBearer": str,
    },
)
_OptionalSendChannelMessageRequestRequestTypeDef = TypedDict(
    "_OptionalSendChannelMessageRequestRequestTypeDef",
    {
        "Metadata": str,
        "PushNotification": "PushNotificationConfigurationTypeDef",
        "MessageAttributes": Dict[str, "MessageAttributeValueTypeDef"],
    },
    total=False,
)

class SendChannelMessageRequestRequestTypeDef(
    _RequiredSendChannelMessageRequestRequestTypeDef,
    _OptionalSendChannelMessageRequestRequestTypeDef,
):
    pass

SendChannelMessageResponseTypeDef = TypedDict(
    "SendChannelMessageResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "Status": "ChannelMessageStatusStructureTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

UpdateChannelFlowRequestRequestTypeDef = TypedDict(
    "UpdateChannelFlowRequestRequestTypeDef",
    {
        "ChannelFlowArn": str,
        "Processors": List["ProcessorTypeDef"],
        "Name": str,
    },
)

UpdateChannelFlowResponseTypeDef = TypedDict(
    "UpdateChannelFlowResponseTypeDef",
    {
        "ChannelFlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateChannelMessageRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": str,
    },
)
_OptionalUpdateChannelMessageRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelMessageRequestRequestTypeDef",
    {
        "Content": str,
        "Metadata": str,
    },
    total=False,
)

class UpdateChannelMessageRequestRequestTypeDef(
    _RequiredUpdateChannelMessageRequestRequestTypeDef,
    _OptionalUpdateChannelMessageRequestRequestTypeDef,
):
    pass

UpdateChannelMessageResponseTypeDef = TypedDict(
    "UpdateChannelMessageResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "Status": "ChannelMessageStatusStructureTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateChannelReadMarkerRequestRequestTypeDef = TypedDict(
    "UpdateChannelReadMarkerRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)

UpdateChannelReadMarkerResponseTypeDef = TypedDict(
    "UpdateChannelReadMarkerResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateChannelRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)
_OptionalUpdateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelRequestRequestTypeDef",
    {
        "Name": str,
        "Mode": ChannelModeType,
        "Metadata": str,
    },
    total=False,
)

class UpdateChannelRequestRequestTypeDef(
    _RequiredUpdateChannelRequestRequestTypeDef, _OptionalUpdateChannelRequestRequestTypeDef
):
    pass

UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
