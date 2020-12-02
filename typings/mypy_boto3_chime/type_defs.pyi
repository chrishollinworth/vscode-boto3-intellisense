"""
Main interface for chime service type definitions.

Usage::

    ```python
    from mypy_boto3_chime.type_defs import AccountSettingsTypeDef

    data: AccountSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
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
    "AccountSettingsTypeDef",
    "AccountTypeDef",
    "AlexaForBusinessMetadataTypeDef",
    "AppInstanceAdminSummaryTypeDef",
    "AppInstanceAdminTypeDef",
    "AppInstanceRetentionSettingsTypeDef",
    "AppInstanceStreamingConfigurationTypeDef",
    "AppInstanceSummaryTypeDef",
    "AppInstanceTypeDef",
    "AppInstanceUserMembershipSummaryTypeDef",
    "AppInstanceUserSummaryTypeDef",
    "AppInstanceUserTypeDef",
    "AttendeeTypeDef",
    "BotTypeDef",
    "BusinessCallingSettingsTypeDef",
    "ChannelBanSummaryTypeDef",
    "ChannelBanTypeDef",
    "ChannelMembershipForAppInstanceUserSummaryTypeDef",
    "ChannelMembershipSummaryTypeDef",
    "ChannelMembershipTypeDef",
    "ChannelMessageSummaryTypeDef",
    "ChannelMessageTypeDef",
    "ChannelModeratedByAppInstanceUserSummaryTypeDef",
    "ChannelModeratorSummaryTypeDef",
    "ChannelModeratorTypeDef",
    "ChannelRetentionSettingsTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "ConversationRetentionSettingsTypeDef",
    "CreateAttendeeErrorTypeDef",
    "DNISEmergencyCallingConfigurationTypeDef",
    "EmergencyCallingConfigurationTypeDef",
    "EventsConfigurationTypeDef",
    "GeoMatchParamsTypeDef",
    "IdentityTypeDef",
    "InviteTypeDef",
    "LoggingConfigurationTypeDef",
    "MediaPlacementTypeDef",
    "MeetingTypeDef",
    "MemberErrorTypeDef",
    "MemberTypeDef",
    "MessagingSessionEndpointTypeDef",
    "OrderedPhoneNumberTypeDef",
    "OriginationRouteTypeDef",
    "OriginationTypeDef",
    "ParticipantTypeDef",
    "PhoneNumberAssociationTypeDef",
    "PhoneNumberCapabilitiesTypeDef",
    "PhoneNumberErrorTypeDef",
    "PhoneNumberOrderTypeDef",
    "PhoneNumberTypeDef",
    "ProxySessionTypeDef",
    "ProxyTypeDef",
    "RetentionSettingsTypeDef",
    "RoomMembershipTypeDef",
    "RoomRetentionSettingsTypeDef",
    "RoomTypeDef",
    "SigninDelegateGroupTypeDef",
    "SipMediaApplicationCallTypeDef",
    "SipMediaApplicationEndpointTypeDef",
    "SipMediaApplicationLoggingConfigurationTypeDef",
    "SipMediaApplicationTypeDef",
    "SipRuleTargetApplicationTypeDef",
    "SipRuleTypeDef",
    "StreamingConfigurationTypeDef",
    "StreamingNotificationTargetTypeDef",
    "TagTypeDef",
    "TelephonySettingsTypeDef",
    "TerminationHealthTypeDef",
    "TerminationTypeDef",
    "UserErrorTypeDef",
    "UserSettingsTypeDef",
    "UserTypeDef",
    "VoiceConnectorGroupTypeDef",
    "VoiceConnectorItemTypeDef",
    "VoiceConnectorSettingsTypeDef",
    "VoiceConnectorTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    "BatchCreateAttendeeResponseTypeDef",
    "BatchCreateRoomMembershipResponseTypeDef",
    "BatchDeletePhoneNumberResponseTypeDef",
    "BatchSuspendUserResponseTypeDef",
    "BatchUnsuspendUserResponseTypeDef",
    "BatchUpdatePhoneNumberResponseTypeDef",
    "BatchUpdateUserResponseTypeDef",
    "CreateAccountResponseTypeDef",
    "CreateAppInstanceAdminResponseTypeDef",
    "CreateAppInstanceResponseTypeDef",
    "CreateAppInstanceUserResponseTypeDef",
    "CreateAttendeeRequestItemTypeDef",
    "CreateAttendeeResponseTypeDef",
    "CreateBotResponseTypeDef",
    "CreateChannelBanResponseTypeDef",
    "CreateChannelMembershipResponseTypeDef",
    "CreateChannelModeratorResponseTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateMeetingDialOutResponseTypeDef",
    "CreateMeetingResponseTypeDef",
    "CreateMeetingWithAttendeesResponseTypeDef",
    "CreatePhoneNumberOrderResponseTypeDef",
    "CreateProxySessionResponseTypeDef",
    "CreateRoomMembershipResponseTypeDef",
    "CreateRoomResponseTypeDef",
    "CreateSipMediaApplicationCallResponseTypeDef",
    "CreateSipMediaApplicationResponseTypeDef",
    "CreateSipRuleResponseTypeDef",
    "CreateUserResponseTypeDef",
    "CreateVoiceConnectorGroupResponseTypeDef",
    "CreateVoiceConnectorResponseTypeDef",
    "CredentialTypeDef",
    "DescribeAppInstanceAdminResponseTypeDef",
    "DescribeAppInstanceResponseTypeDef",
    "DescribeAppInstanceUserResponseTypeDef",
    "DescribeChannelBanResponseTypeDef",
    "DescribeChannelMembershipForAppInstanceUserResponseTypeDef",
    "DescribeChannelMembershipResponseTypeDef",
    "DescribeChannelModeratedByAppInstanceUserResponseTypeDef",
    "DescribeChannelModeratorResponseTypeDef",
    "DescribeChannelResponseTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    "GetAccountResponseTypeDef",
    "GetAccountSettingsResponseTypeDef",
    "GetAppInstanceRetentionSettingsResponseTypeDef",
    "GetAppInstanceStreamingConfigurationsResponseTypeDef",
    "GetAttendeeResponseTypeDef",
    "GetBotResponseTypeDef",
    "GetChannelMessageResponseTypeDef",
    "GetEventsConfigurationResponseTypeDef",
    "GetGlobalSettingsResponseTypeDef",
    "GetMeetingResponseTypeDef",
    "GetMessagingSessionEndpointResponseTypeDef",
    "GetPhoneNumberOrderResponseTypeDef",
    "GetPhoneNumberResponseTypeDef",
    "GetPhoneNumberSettingsResponseTypeDef",
    "GetProxySessionResponseTypeDef",
    "GetRetentionSettingsResponseTypeDef",
    "GetRoomResponseTypeDef",
    "GetSipMediaApplicationLoggingConfigurationResponseTypeDef",
    "GetSipMediaApplicationResponseTypeDef",
    "GetSipRuleResponseTypeDef",
    "GetUserResponseTypeDef",
    "GetUserSettingsResponseTypeDef",
    "GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    "GetVoiceConnectorGroupResponseTypeDef",
    "GetVoiceConnectorLoggingConfigurationResponseTypeDef",
    "GetVoiceConnectorOriginationResponseTypeDef",
    "GetVoiceConnectorProxyResponseTypeDef",
    "GetVoiceConnectorResponseTypeDef",
    "GetVoiceConnectorStreamingConfigurationResponseTypeDef",
    "GetVoiceConnectorTerminationHealthResponseTypeDef",
    "GetVoiceConnectorTerminationResponseTypeDef",
    "InviteUsersResponseTypeDef",
    "ListAccountsResponseTypeDef",
    "ListAppInstanceAdminsResponseTypeDef",
    "ListAppInstanceUsersResponseTypeDef",
    "ListAppInstancesResponseTypeDef",
    "ListAttendeeTagsResponseTypeDef",
    "ListAttendeesResponseTypeDef",
    "ListBotsResponseTypeDef",
    "ListChannelBansResponseTypeDef",
    "ListChannelMembershipsForAppInstanceUserResponseTypeDef",
    "ListChannelMembershipsResponseTypeDef",
    "ListChannelMessagesResponseTypeDef",
    "ListChannelModeratorsResponseTypeDef",
    "ListChannelsModeratedByAppInstanceUserResponseTypeDef",
    "ListChannelsResponseTypeDef",
    "ListMeetingTagsResponseTypeDef",
    "ListMeetingsResponseTypeDef",
    "ListPhoneNumberOrdersResponseTypeDef",
    "ListPhoneNumbersResponseTypeDef",
    "ListProxySessionsResponseTypeDef",
    "ListRoomMembershipsResponseTypeDef",
    "ListRoomsResponseTypeDef",
    "ListSipMediaApplicationsResponseTypeDef",
    "ListSipRulesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsersResponseTypeDef",
    "ListVoiceConnectorGroupsResponseTypeDef",
    "ListVoiceConnectorTerminationCredentialsResponseTypeDef",
    "ListVoiceConnectorsResponseTypeDef",
    "MeetingNotificationConfigurationTypeDef",
    "MembershipItemTypeDef",
    "PaginatorConfigTypeDef",
    "PutAppInstanceRetentionSettingsResponseTypeDef",
    "PutAppInstanceStreamingConfigurationsResponseTypeDef",
    "PutEventsConfigurationResponseTypeDef",
    "PutRetentionSettingsResponseTypeDef",
    "PutSipMediaApplicationLoggingConfigurationResponseTypeDef",
    "PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    "PutVoiceConnectorLoggingConfigurationResponseTypeDef",
    "PutVoiceConnectorOriginationResponseTypeDef",
    "PutVoiceConnectorProxyResponseTypeDef",
    "PutVoiceConnectorStreamingConfigurationResponseTypeDef",
    "PutVoiceConnectorTerminationResponseTypeDef",
    "RedactChannelMessageResponseTypeDef",
    "RegenerateSecurityTokenResponseTypeDef",
    "ResetPersonalPINResponseTypeDef",
    "RestorePhoneNumberResponseTypeDef",
    "SearchAvailablePhoneNumbersResponseTypeDef",
    "SendChannelMessageResponseTypeDef",
    "UpdateAccountResponseTypeDef",
    "UpdateAppInstanceResponseTypeDef",
    "UpdateAppInstanceUserResponseTypeDef",
    "UpdateBotResponseTypeDef",
    "UpdateChannelMessageResponseTypeDef",
    "UpdateChannelReadMarkerResponseTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdatePhoneNumberRequestItemTypeDef",
    "UpdatePhoneNumberResponseTypeDef",
    "UpdateProxySessionResponseTypeDef",
    "UpdateRoomMembershipResponseTypeDef",
    "UpdateRoomResponseTypeDef",
    "UpdateSipMediaApplicationResponseTypeDef",
    "UpdateSipRuleResponseTypeDef",
    "UpdateUserRequestItemTypeDef",
    "UpdateUserResponseTypeDef",
    "UpdateVoiceConnectorGroupResponseTypeDef",
    "UpdateVoiceConnectorResponseTypeDef",
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef", {"DisableRemoteControl": bool, "EnableDialOut": bool}, total=False
)

_RequiredAccountTypeDef = TypedDict(
    "_RequiredAccountTypeDef", {"AwsAccountId": str, "AccountId": str, "Name": str}
)
_OptionalAccountTypeDef = TypedDict(
    "_OptionalAccountTypeDef",
    {
        "AccountType": Literal["Team", "EnterpriseDirectory", "EnterpriseLWA", "EnterpriseOIDC"],
        "CreatedTimestamp": datetime,
        "DefaultLicense": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "SupportedLicenses": List[Literal["Basic", "Plus", "Pro", "ProTrial"]],
        "SigninDelegateGroups": List["SigninDelegateGroupTypeDef"],
    },
    total=False,
)


class AccountTypeDef(_RequiredAccountTypeDef, _OptionalAccountTypeDef):
    pass


AlexaForBusinessMetadataTypeDef = TypedDict(
    "AlexaForBusinessMetadataTypeDef",
    {"IsAlexaForBusinessEnabled": bool, "AlexaForBusinessRoomArn": str},
    total=False,
)

AppInstanceAdminSummaryTypeDef = TypedDict(
    "AppInstanceAdminSummaryTypeDef", {"Admin": "IdentityTypeDef"}, total=False
)

AppInstanceAdminTypeDef = TypedDict(
    "AppInstanceAdminTypeDef",
    {"Admin": "IdentityTypeDef", "AppInstanceArn": str, "CreatedTimestamp": datetime},
    total=False,
)

AppInstanceRetentionSettingsTypeDef = TypedDict(
    "AppInstanceRetentionSettingsTypeDef",
    {"ChannelRetentionSettings": "ChannelRetentionSettingsTypeDef"},
    total=False,
)

AppInstanceStreamingConfigurationTypeDef = TypedDict(
    "AppInstanceStreamingConfigurationTypeDef",
    {"AppInstanceDataType": Literal["Channel", "ChannelMessage"], "ResourceArn": str},
)

AppInstanceSummaryTypeDef = TypedDict(
    "AppInstanceSummaryTypeDef", {"AppInstanceArn": str, "Name": str, "Metadata": str}, total=False
)

AppInstanceTypeDef = TypedDict(
    "AppInstanceTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "Metadata": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
    },
    total=False,
)

AppInstanceUserMembershipSummaryTypeDef = TypedDict(
    "AppInstanceUserMembershipSummaryTypeDef",
    {"Type": Literal["DEFAULT", "HIDDEN"], "ReadMarkerTimestamp": datetime},
    total=False,
)

AppInstanceUserSummaryTypeDef = TypedDict(
    "AppInstanceUserSummaryTypeDef",
    {"AppInstanceUserArn": str, "Name": str, "Metadata": str},
    total=False,
)

AppInstanceUserTypeDef = TypedDict(
    "AppInstanceUserTypeDef",
    {
        "AppInstanceUserArn": str,
        "Name": str,
        "CreatedTimestamp": datetime,
        "Metadata": str,
        "LastUpdatedTimestamp": datetime,
    },
    total=False,
)

AttendeeTypeDef = TypedDict(
    "AttendeeTypeDef", {"ExternalUserId": str, "AttendeeId": str, "JoinToken": str}, total=False
)

BotTypeDef = TypedDict(
    "BotTypeDef",
    {
        "BotId": str,
        "UserId": str,
        "DisplayName": str,
        "BotType": Literal["ChatBot"],
        "Disabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "BotEmail": str,
        "SecurityToken": str,
    },
    total=False,
)

BusinessCallingSettingsTypeDef = TypedDict(
    "BusinessCallingSettingsTypeDef", {"CdrBucket": str}, total=False
)

ChannelBanSummaryTypeDef = TypedDict(
    "ChannelBanSummaryTypeDef", {"Member": "IdentityTypeDef"}, total=False
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

ChannelMembershipForAppInstanceUserSummaryTypeDef = TypedDict(
    "ChannelMembershipForAppInstanceUserSummaryTypeDef",
    {
        "ChannelSummary": "ChannelSummaryTypeDef",
        "AppInstanceUserMembershipSummary": "AppInstanceUserMembershipSummaryTypeDef",
    },
    total=False,
)

ChannelMembershipSummaryTypeDef = TypedDict(
    "ChannelMembershipSummaryTypeDef", {"Member": "IdentityTypeDef"}, total=False
)

ChannelMembershipTypeDef = TypedDict(
    "ChannelMembershipTypeDef",
    {
        "InvitedBy": "IdentityTypeDef",
        "Type": Literal["DEFAULT", "HIDDEN"],
        "Member": "IdentityTypeDef",
        "ChannelArn": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
    },
    total=False,
)

ChannelMessageSummaryTypeDef = TypedDict(
    "ChannelMessageSummaryTypeDef",
    {
        "MessageId": str,
        "Content": str,
        "Metadata": str,
        "Type": Literal["STANDARD", "CONTROL"],
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "LastEditedTimestamp": datetime,
        "Sender": "IdentityTypeDef",
        "Redacted": bool,
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
        "Type": Literal["STANDARD", "CONTROL"],
        "CreatedTimestamp": datetime,
        "LastEditedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "Sender": "IdentityTypeDef",
        "Redacted": bool,
        "Persistence": Literal["PERSISTENT", "NON_PERSISTENT"],
    },
    total=False,
)

ChannelModeratedByAppInstanceUserSummaryTypeDef = TypedDict(
    "ChannelModeratedByAppInstanceUserSummaryTypeDef",
    {"ChannelSummary": "ChannelSummaryTypeDef"},
    total=False,
)

ChannelModeratorSummaryTypeDef = TypedDict(
    "ChannelModeratorSummaryTypeDef", {"Moderator": "IdentityTypeDef"}, total=False
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

ChannelRetentionSettingsTypeDef = TypedDict(
    "ChannelRetentionSettingsTypeDef", {"RetentionDays": int}, total=False
)

ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "Name": str,
        "ChannelArn": str,
        "Mode": Literal["UNRESTRICTED", "RESTRICTED"],
        "Privacy": Literal["PUBLIC", "PRIVATE"],
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
        "Mode": Literal["UNRESTRICTED", "RESTRICTED"],
        "Privacy": Literal["PUBLIC", "PRIVATE"],
        "Metadata": str,
        "CreatedBy": "IdentityTypeDef",
        "CreatedTimestamp": datetime,
        "LastMessageTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
    },
    total=False,
)

ConversationRetentionSettingsTypeDef = TypedDict(
    "ConversationRetentionSettingsTypeDef", {"RetentionDays": int}, total=False
)

CreateAttendeeErrorTypeDef = TypedDict(
    "CreateAttendeeErrorTypeDef",
    {"ExternalUserId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

_RequiredDNISEmergencyCallingConfigurationTypeDef = TypedDict(
    "_RequiredDNISEmergencyCallingConfigurationTypeDef",
    {"EmergencyPhoneNumber": str, "CallingCountry": str},
)
_OptionalDNISEmergencyCallingConfigurationTypeDef = TypedDict(
    "_OptionalDNISEmergencyCallingConfigurationTypeDef", {"TestPhoneNumber": str}, total=False
)


class DNISEmergencyCallingConfigurationTypeDef(
    _RequiredDNISEmergencyCallingConfigurationTypeDef,
    _OptionalDNISEmergencyCallingConfigurationTypeDef,
):
    pass


EmergencyCallingConfigurationTypeDef = TypedDict(
    "EmergencyCallingConfigurationTypeDef",
    {"DNIS": List["DNISEmergencyCallingConfigurationTypeDef"]},
    total=False,
)

EventsConfigurationTypeDef = TypedDict(
    "EventsConfigurationTypeDef",
    {"BotId": str, "OutboundEventsHTTPSEndpoint": str, "LambdaFunctionArn": str},
    total=False,
)

GeoMatchParamsTypeDef = TypedDict("GeoMatchParamsTypeDef", {"Country": str, "AreaCode": str})

IdentityTypeDef = TypedDict("IdentityTypeDef", {"Arn": str, "Name": str}, total=False)

InviteTypeDef = TypedDict(
    "InviteTypeDef",
    {
        "InviteId": str,
        "Status": Literal["Pending", "Accepted", "Failed"],
        "EmailAddress": str,
        "EmailStatus": Literal["NotSent", "Sent", "Failed"],
    },
    total=False,
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef", {"EnableSIPLogs": bool}, total=False
)

MediaPlacementTypeDef = TypedDict(
    "MediaPlacementTypeDef",
    {
        "AudioHostUrl": str,
        "AudioFallbackUrl": str,
        "ScreenDataUrl": str,
        "ScreenSharingUrl": str,
        "ScreenViewingUrl": str,
        "SignalingUrl": str,
        "TurnControlUrl": str,
    },
    total=False,
)

MeetingTypeDef = TypedDict(
    "MeetingTypeDef",
    {
        "MeetingId": str,
        "ExternalMeetingId": str,
        "MediaPlacement": "MediaPlacementTypeDef",
        "MediaRegion": str,
    },
    total=False,
)

MemberErrorTypeDef = TypedDict(
    "MemberErrorTypeDef",
    {
        "MemberId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Throttling",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "MemberId": str,
        "MemberType": Literal["User", "Bot", "Webhook"],
        "Email": str,
        "FullName": str,
        "AccountId": str,
    },
    total=False,
)

MessagingSessionEndpointTypeDef = TypedDict(
    "MessagingSessionEndpointTypeDef", {"Url": str}, total=False
)

OrderedPhoneNumberTypeDef = TypedDict(
    "OrderedPhoneNumberTypeDef",
    {"E164PhoneNumber": str, "Status": Literal["Processing", "Acquired", "Failed"]},
    total=False,
)

OriginationRouteTypeDef = TypedDict(
    "OriginationRouteTypeDef",
    {"Host": str, "Port": int, "Protocol": Literal["TCP", "UDP"], "Priority": int, "Weight": int},
    total=False,
)

OriginationTypeDef = TypedDict(
    "OriginationTypeDef", {"Routes": List["OriginationRouteTypeDef"], "Disabled": bool}, total=False
)

ParticipantTypeDef = TypedDict(
    "ParticipantTypeDef", {"PhoneNumber": str, "ProxyPhoneNumber": str}, total=False
)

PhoneNumberAssociationTypeDef = TypedDict(
    "PhoneNumberAssociationTypeDef",
    {
        "Value": str,
        "Name": Literal[
            "AccountId", "UserId", "VoiceConnectorId", "VoiceConnectorGroupId", "SipRuleId"
        ],
        "AssociatedTimestamp": datetime,
    },
    total=False,
)

PhoneNumberCapabilitiesTypeDef = TypedDict(
    "PhoneNumberCapabilitiesTypeDef",
    {
        "InboundCall": bool,
        "OutboundCall": bool,
        "InboundSMS": bool,
        "OutboundSMS": bool,
        "InboundMMS": bool,
        "OutboundMMS": bool,
    },
    total=False,
)

PhoneNumberErrorTypeDef = TypedDict(
    "PhoneNumberErrorTypeDef",
    {
        "PhoneNumberId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Throttling",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

PhoneNumberOrderTypeDef = TypedDict(
    "PhoneNumberOrderTypeDef",
    {
        "PhoneNumberOrderId": str,
        "ProductType": Literal["BusinessCalling", "VoiceConnector"],
        "Status": Literal["Processing", "Successful", "Failed", "Partial"],
        "OrderedPhoneNumbers": List["OrderedPhoneNumberTypeDef"],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

PhoneNumberTypeDef = TypedDict(
    "PhoneNumberTypeDef",
    {
        "PhoneNumberId": str,
        "E164PhoneNumber": str,
        "Type": Literal["Local", "TollFree"],
        "ProductType": Literal["BusinessCalling", "VoiceConnector"],
        "Status": Literal[
            "AcquireInProgress",
            "AcquireFailed",
            "Unassigned",
            "Assigned",
            "ReleaseInProgress",
            "DeleteInProgress",
            "ReleaseFailed",
            "DeleteFailed",
        ],
        "Capabilities": "PhoneNumberCapabilitiesTypeDef",
        "Associations": List["PhoneNumberAssociationTypeDef"],
        "CallingName": str,
        "CallingNameStatus": Literal[
            "Unassigned", "UpdateInProgress", "UpdateSucceeded", "UpdateFailed"
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "DeletionTimestamp": datetime,
    },
    total=False,
)

ProxySessionTypeDef = TypedDict(
    "ProxySessionTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
        "Name": str,
        "Status": Literal["Open", "InProgress", "Closed"],
        "ExpiryMinutes": int,
        "Capabilities": List[Literal["Voice", "SMS"]],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "EndedTimestamp": datetime,
        "Participants": List["ParticipantTypeDef"],
        "NumberSelectionBehavior": Literal["PreferSticky", "AvoidSticky"],
        "GeoMatchLevel": Literal["Country", "AreaCode"],
        "GeoMatchParams": "GeoMatchParamsTypeDef",
    },
    total=False,
)

ProxyTypeDef = TypedDict(
    "ProxyTypeDef",
    {
        "DefaultSessionExpiryMinutes": int,
        "Disabled": bool,
        "FallBackPhoneNumber": str,
        "PhoneNumberCountries": List[str],
    },
    total=False,
)

RetentionSettingsTypeDef = TypedDict(
    "RetentionSettingsTypeDef",
    {
        "RoomRetentionSettings": "RoomRetentionSettingsTypeDef",
        "ConversationRetentionSettings": "ConversationRetentionSettingsTypeDef",
    },
    total=False,
)

RoomMembershipTypeDef = TypedDict(
    "RoomMembershipTypeDef",
    {
        "RoomId": str,
        "Member": "MemberTypeDef",
        "Role": Literal["Administrator", "Member"],
        "InvitedBy": str,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

RoomRetentionSettingsTypeDef = TypedDict(
    "RoomRetentionSettingsTypeDef", {"RetentionDays": int}, total=False
)

RoomTypeDef = TypedDict(
    "RoomTypeDef",
    {
        "RoomId": str,
        "Name": str,
        "AccountId": str,
        "CreatedBy": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

SigninDelegateGroupTypeDef = TypedDict(
    "SigninDelegateGroupTypeDef", {"GroupName": str}, total=False
)

SipMediaApplicationCallTypeDef = TypedDict(
    "SipMediaApplicationCallTypeDef", {"TransactionId": str}, total=False
)

SipMediaApplicationEndpointTypeDef = TypedDict(
    "SipMediaApplicationEndpointTypeDef", {"LambdaArn": str}, total=False
)

SipMediaApplicationLoggingConfigurationTypeDef = TypedDict(
    "SipMediaApplicationLoggingConfigurationTypeDef",
    {"EnableSipMediaApplicationMessageLogs": bool},
    total=False,
)

SipMediaApplicationTypeDef = TypedDict(
    "SipMediaApplicationTypeDef",
    {
        "SipMediaApplicationId": str,
        "AwsRegion": str,
        "Name": str,
        "Endpoints": List["SipMediaApplicationEndpointTypeDef"],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

SipRuleTargetApplicationTypeDef = TypedDict(
    "SipRuleTargetApplicationTypeDef",
    {"SipMediaApplicationId": str, "Priority": int, "AwsRegion": str},
    total=False,
)

SipRuleTypeDef = TypedDict(
    "SipRuleTypeDef",
    {
        "SipRuleId": str,
        "Name": str,
        "Disabled": bool,
        "TriggerType": Literal["ToPhoneNumber", "RequestUriHostname"],
        "TriggerValue": str,
        "TargetApplications": List["SipRuleTargetApplicationTypeDef"],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

_RequiredStreamingConfigurationTypeDef = TypedDict(
    "_RequiredStreamingConfigurationTypeDef", {"DataRetentionInHours": int}
)
_OptionalStreamingConfigurationTypeDef = TypedDict(
    "_OptionalStreamingConfigurationTypeDef",
    {"Disabled": bool, "StreamingNotificationTargets": List["StreamingNotificationTargetTypeDef"]},
    total=False,
)


class StreamingConfigurationTypeDef(
    _RequiredStreamingConfigurationTypeDef, _OptionalStreamingConfigurationTypeDef
):
    pass


StreamingNotificationTargetTypeDef = TypedDict(
    "StreamingNotificationTargetTypeDef",
    {"NotificationTarget": Literal["EventBridge", "SNS", "SQS"]},
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

TelephonySettingsTypeDef = TypedDict(
    "TelephonySettingsTypeDef", {"InboundCalling": bool, "OutboundCalling": bool, "SMS": bool}
)

TerminationHealthTypeDef = TypedDict(
    "TerminationHealthTypeDef", {"Timestamp": datetime, "Source": str}, total=False
)

TerminationTypeDef = TypedDict(
    "TerminationTypeDef",
    {
        "CpsLimit": int,
        "DefaultPhoneNumber": str,
        "CallingRegions": List[str],
        "CidrAllowedList": List[str],
        "Disabled": bool,
    },
    total=False,
)

UserErrorTypeDef = TypedDict(
    "UserErrorTypeDef",
    {
        "UserId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Throttling",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

UserSettingsTypeDef = TypedDict("UserSettingsTypeDef", {"Telephony": "TelephonySettingsTypeDef"})

_RequiredUserTypeDef = TypedDict("_RequiredUserTypeDef", {"UserId": str})
_OptionalUserTypeDef = TypedDict(
    "_OptionalUserTypeDef",
    {
        "AccountId": str,
        "PrimaryEmail": str,
        "PrimaryProvisionedNumber": str,
        "DisplayName": str,
        "LicenseType": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "UserType": Literal["PrivateUser", "SharedDevice"],
        "UserRegistrationStatus": Literal["Unregistered", "Registered", "Suspended"],
        "UserInvitationStatus": Literal["Pending", "Accepted", "Failed"],
        "RegisteredOn": datetime,
        "InvitedOn": datetime,
        "AlexaForBusinessMetadata": "AlexaForBusinessMetadataTypeDef",
        "PersonalPIN": str,
    },
    total=False,
)


class UserTypeDef(_RequiredUserTypeDef, _OptionalUserTypeDef):
    pass


VoiceConnectorGroupTypeDef = TypedDict(
    "VoiceConnectorGroupTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": List["VoiceConnectorItemTypeDef"],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

VoiceConnectorItemTypeDef = TypedDict(
    "VoiceConnectorItemTypeDef", {"VoiceConnectorId": str, "Priority": int}
)

VoiceConnectorSettingsTypeDef = TypedDict(
    "VoiceConnectorSettingsTypeDef", {"CdrBucket": str}, total=False
)

VoiceConnectorTypeDef = TypedDict(
    "VoiceConnectorTypeDef",
    {
        "VoiceConnectorId": str,
        "AwsRegion": Literal["us-east-1", "us-west-2"],
        "Name": str,
        "OutboundHostName": str,
        "RequireEncryption": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef = TypedDict(
    "AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    {"PhoneNumberErrors": List["PhoneNumberErrorTypeDef"]},
    total=False,
)

AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef = TypedDict(
    "AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    {"PhoneNumberErrors": List["PhoneNumberErrorTypeDef"]},
    total=False,
)

BatchCreateAttendeeResponseTypeDef = TypedDict(
    "BatchCreateAttendeeResponseTypeDef",
    {"Attendees": List["AttendeeTypeDef"], "Errors": List["CreateAttendeeErrorTypeDef"]},
    total=False,
)

BatchCreateRoomMembershipResponseTypeDef = TypedDict(
    "BatchCreateRoomMembershipResponseTypeDef", {"Errors": List["MemberErrorTypeDef"]}, total=False
)

BatchDeletePhoneNumberResponseTypeDef = TypedDict(
    "BatchDeletePhoneNumberResponseTypeDef",
    {"PhoneNumberErrors": List["PhoneNumberErrorTypeDef"]},
    total=False,
)

BatchSuspendUserResponseTypeDef = TypedDict(
    "BatchSuspendUserResponseTypeDef", {"UserErrors": List["UserErrorTypeDef"]}, total=False
)

BatchUnsuspendUserResponseTypeDef = TypedDict(
    "BatchUnsuspendUserResponseTypeDef", {"UserErrors": List["UserErrorTypeDef"]}, total=False
)

BatchUpdatePhoneNumberResponseTypeDef = TypedDict(
    "BatchUpdatePhoneNumberResponseTypeDef",
    {"PhoneNumberErrors": List["PhoneNumberErrorTypeDef"]},
    total=False,
)

BatchUpdateUserResponseTypeDef = TypedDict(
    "BatchUpdateUserResponseTypeDef", {"UserErrors": List["UserErrorTypeDef"]}, total=False
)

CreateAccountResponseTypeDef = TypedDict(
    "CreateAccountResponseTypeDef", {"Account": "AccountTypeDef"}, total=False
)

CreateAppInstanceAdminResponseTypeDef = TypedDict(
    "CreateAppInstanceAdminResponseTypeDef",
    {"AppInstanceAdmin": "IdentityTypeDef", "AppInstanceArn": str},
    total=False,
)

CreateAppInstanceResponseTypeDef = TypedDict(
    "CreateAppInstanceResponseTypeDef", {"AppInstanceArn": str}, total=False
)

CreateAppInstanceUserResponseTypeDef = TypedDict(
    "CreateAppInstanceUserResponseTypeDef", {"AppInstanceUserArn": str}, total=False
)

_RequiredCreateAttendeeRequestItemTypeDef = TypedDict(
    "_RequiredCreateAttendeeRequestItemTypeDef", {"ExternalUserId": str}
)
_OptionalCreateAttendeeRequestItemTypeDef = TypedDict(
    "_OptionalCreateAttendeeRequestItemTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)


class CreateAttendeeRequestItemTypeDef(
    _RequiredCreateAttendeeRequestItemTypeDef, _OptionalCreateAttendeeRequestItemTypeDef
):
    pass


CreateAttendeeResponseTypeDef = TypedDict(
    "CreateAttendeeResponseTypeDef", {"Attendee": "AttendeeTypeDef"}, total=False
)

CreateBotResponseTypeDef = TypedDict("CreateBotResponseTypeDef", {"Bot": "BotTypeDef"}, total=False)

CreateChannelBanResponseTypeDef = TypedDict(
    "CreateChannelBanResponseTypeDef", {"ChannelArn": str, "Member": "IdentityTypeDef"}, total=False
)

CreateChannelMembershipResponseTypeDef = TypedDict(
    "CreateChannelMembershipResponseTypeDef",
    {"ChannelArn": str, "Member": "IdentityTypeDef"},
    total=False,
)

CreateChannelModeratorResponseTypeDef = TypedDict(
    "CreateChannelModeratorResponseTypeDef",
    {"ChannelArn": str, "ChannelModerator": "IdentityTypeDef"},
    total=False,
)

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef", {"ChannelArn": str}, total=False
)

CreateMeetingDialOutResponseTypeDef = TypedDict(
    "CreateMeetingDialOutResponseTypeDef", {"TransactionId": str}, total=False
)

CreateMeetingResponseTypeDef = TypedDict(
    "CreateMeetingResponseTypeDef", {"Meeting": "MeetingTypeDef"}, total=False
)

CreateMeetingWithAttendeesResponseTypeDef = TypedDict(
    "CreateMeetingWithAttendeesResponseTypeDef",
    {
        "Meeting": "MeetingTypeDef",
        "Attendees": List["AttendeeTypeDef"],
        "Errors": List["CreateAttendeeErrorTypeDef"],
    },
    total=False,
)

CreatePhoneNumberOrderResponseTypeDef = TypedDict(
    "CreatePhoneNumberOrderResponseTypeDef",
    {"PhoneNumberOrder": "PhoneNumberOrderTypeDef"},
    total=False,
)

CreateProxySessionResponseTypeDef = TypedDict(
    "CreateProxySessionResponseTypeDef", {"ProxySession": "ProxySessionTypeDef"}, total=False
)

CreateRoomMembershipResponseTypeDef = TypedDict(
    "CreateRoomMembershipResponseTypeDef", {"RoomMembership": "RoomMembershipTypeDef"}, total=False
)

CreateRoomResponseTypeDef = TypedDict(
    "CreateRoomResponseTypeDef", {"Room": "RoomTypeDef"}, total=False
)

CreateSipMediaApplicationCallResponseTypeDef = TypedDict(
    "CreateSipMediaApplicationCallResponseTypeDef",
    {"SipMediaApplicationCall": "SipMediaApplicationCallTypeDef"},
    total=False,
)

CreateSipMediaApplicationResponseTypeDef = TypedDict(
    "CreateSipMediaApplicationResponseTypeDef",
    {"SipMediaApplication": "SipMediaApplicationTypeDef"},
    total=False,
)

CreateSipRuleResponseTypeDef = TypedDict(
    "CreateSipRuleResponseTypeDef", {"SipRule": "SipRuleTypeDef"}, total=False
)

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef", {"User": "UserTypeDef"}, total=False
)

CreateVoiceConnectorGroupResponseTypeDef = TypedDict(
    "CreateVoiceConnectorGroupResponseTypeDef",
    {"VoiceConnectorGroup": "VoiceConnectorGroupTypeDef"},
    total=False,
)

CreateVoiceConnectorResponseTypeDef = TypedDict(
    "CreateVoiceConnectorResponseTypeDef", {"VoiceConnector": "VoiceConnectorTypeDef"}, total=False
)

CredentialTypeDef = TypedDict("CredentialTypeDef", {"Username": str, "Password": str}, total=False)

DescribeAppInstanceAdminResponseTypeDef = TypedDict(
    "DescribeAppInstanceAdminResponseTypeDef",
    {"AppInstanceAdmin": "AppInstanceAdminTypeDef"},
    total=False,
)

DescribeAppInstanceResponseTypeDef = TypedDict(
    "DescribeAppInstanceResponseTypeDef", {"AppInstance": "AppInstanceTypeDef"}, total=False
)

DescribeAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeAppInstanceUserResponseTypeDef",
    {"AppInstanceUser": "AppInstanceUserTypeDef"},
    total=False,
)

DescribeChannelBanResponseTypeDef = TypedDict(
    "DescribeChannelBanResponseTypeDef", {"ChannelBan": "ChannelBanTypeDef"}, total=False
)

DescribeChannelMembershipForAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeChannelMembershipForAppInstanceUserResponseTypeDef",
    {"ChannelMembership": "ChannelMembershipForAppInstanceUserSummaryTypeDef"},
    total=False,
)

DescribeChannelMembershipResponseTypeDef = TypedDict(
    "DescribeChannelMembershipResponseTypeDef",
    {"ChannelMembership": "ChannelMembershipTypeDef"},
    total=False,
)

DescribeChannelModeratedByAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeChannelModeratedByAppInstanceUserResponseTypeDef",
    {"Channel": "ChannelModeratedByAppInstanceUserSummaryTypeDef"},
    total=False,
)

DescribeChannelModeratorResponseTypeDef = TypedDict(
    "DescribeChannelModeratorResponseTypeDef",
    {"ChannelModerator": "ChannelModeratorTypeDef"},
    total=False,
)

DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef", {"Channel": "ChannelTypeDef"}, total=False
)

DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    {"PhoneNumberErrors": List["PhoneNumberErrorTypeDef"]},
    total=False,
)

DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    {"PhoneNumberErrors": List["PhoneNumberErrorTypeDef"]},
    total=False,
)

GetAccountResponseTypeDef = TypedDict(
    "GetAccountResponseTypeDef", {"Account": "AccountTypeDef"}, total=False
)

GetAccountSettingsResponseTypeDef = TypedDict(
    "GetAccountSettingsResponseTypeDef", {"AccountSettings": "AccountSettingsTypeDef"}, total=False
)

GetAppInstanceRetentionSettingsResponseTypeDef = TypedDict(
    "GetAppInstanceRetentionSettingsResponseTypeDef",
    {
        "AppInstanceRetentionSettings": "AppInstanceRetentionSettingsTypeDef",
        "InitiateDeletionTimestamp": datetime,
    },
    total=False,
)

GetAppInstanceStreamingConfigurationsResponseTypeDef = TypedDict(
    "GetAppInstanceStreamingConfigurationsResponseTypeDef",
    {"AppInstanceStreamingConfigurations": List["AppInstanceStreamingConfigurationTypeDef"]},
    total=False,
)

GetAttendeeResponseTypeDef = TypedDict(
    "GetAttendeeResponseTypeDef", {"Attendee": "AttendeeTypeDef"}, total=False
)

GetBotResponseTypeDef = TypedDict("GetBotResponseTypeDef", {"Bot": "BotTypeDef"}, total=False)

GetChannelMessageResponseTypeDef = TypedDict(
    "GetChannelMessageResponseTypeDef", {"ChannelMessage": "ChannelMessageTypeDef"}, total=False
)

GetEventsConfigurationResponseTypeDef = TypedDict(
    "GetEventsConfigurationResponseTypeDef",
    {"EventsConfiguration": "EventsConfigurationTypeDef"},
    total=False,
)

GetGlobalSettingsResponseTypeDef = TypedDict(
    "GetGlobalSettingsResponseTypeDef",
    {
        "BusinessCalling": "BusinessCallingSettingsTypeDef",
        "VoiceConnector": "VoiceConnectorSettingsTypeDef",
    },
    total=False,
)

GetMeetingResponseTypeDef = TypedDict(
    "GetMeetingResponseTypeDef", {"Meeting": "MeetingTypeDef"}, total=False
)

GetMessagingSessionEndpointResponseTypeDef = TypedDict(
    "GetMessagingSessionEndpointResponseTypeDef",
    {"Endpoint": "MessagingSessionEndpointTypeDef"},
    total=False,
)

GetPhoneNumberOrderResponseTypeDef = TypedDict(
    "GetPhoneNumberOrderResponseTypeDef",
    {"PhoneNumberOrder": "PhoneNumberOrderTypeDef"},
    total=False,
)

GetPhoneNumberResponseTypeDef = TypedDict(
    "GetPhoneNumberResponseTypeDef", {"PhoneNumber": "PhoneNumberTypeDef"}, total=False
)

GetPhoneNumberSettingsResponseTypeDef = TypedDict(
    "GetPhoneNumberSettingsResponseTypeDef",
    {"CallingName": str, "CallingNameUpdatedTimestamp": datetime},
    total=False,
)

GetProxySessionResponseTypeDef = TypedDict(
    "GetProxySessionResponseTypeDef", {"ProxySession": "ProxySessionTypeDef"}, total=False
)

GetRetentionSettingsResponseTypeDef = TypedDict(
    "GetRetentionSettingsResponseTypeDef",
    {"RetentionSettings": "RetentionSettingsTypeDef", "InitiateDeletionTimestamp": datetime},
    total=False,
)

GetRoomResponseTypeDef = TypedDict("GetRoomResponseTypeDef", {"Room": "RoomTypeDef"}, total=False)

GetSipMediaApplicationLoggingConfigurationResponseTypeDef = TypedDict(
    "GetSipMediaApplicationLoggingConfigurationResponseTypeDef",
    {"SipMediaApplicationLoggingConfiguration": "SipMediaApplicationLoggingConfigurationTypeDef"},
    total=False,
)

GetSipMediaApplicationResponseTypeDef = TypedDict(
    "GetSipMediaApplicationResponseTypeDef",
    {"SipMediaApplication": "SipMediaApplicationTypeDef"},
    total=False,
)

GetSipRuleResponseTypeDef = TypedDict(
    "GetSipRuleResponseTypeDef", {"SipRule": "SipRuleTypeDef"}, total=False
)

GetUserResponseTypeDef = TypedDict("GetUserResponseTypeDef", {"User": "UserTypeDef"}, total=False)

GetUserSettingsResponseTypeDef = TypedDict(
    "GetUserSettingsResponseTypeDef", {"UserSettings": "UserSettingsTypeDef"}, total=False
)

GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef = TypedDict(
    "GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    {"EmergencyCallingConfiguration": "EmergencyCallingConfigurationTypeDef"},
    total=False,
)

GetVoiceConnectorGroupResponseTypeDef = TypedDict(
    "GetVoiceConnectorGroupResponseTypeDef",
    {"VoiceConnectorGroup": "VoiceConnectorGroupTypeDef"},
    total=False,
)

GetVoiceConnectorLoggingConfigurationResponseTypeDef = TypedDict(
    "GetVoiceConnectorLoggingConfigurationResponseTypeDef",
    {"LoggingConfiguration": "LoggingConfigurationTypeDef"},
    total=False,
)

GetVoiceConnectorOriginationResponseTypeDef = TypedDict(
    "GetVoiceConnectorOriginationResponseTypeDef",
    {"Origination": "OriginationTypeDef"},
    total=False,
)

GetVoiceConnectorProxyResponseTypeDef = TypedDict(
    "GetVoiceConnectorProxyResponseTypeDef", {"Proxy": "ProxyTypeDef"}, total=False
)

GetVoiceConnectorResponseTypeDef = TypedDict(
    "GetVoiceConnectorResponseTypeDef", {"VoiceConnector": "VoiceConnectorTypeDef"}, total=False
)

GetVoiceConnectorStreamingConfigurationResponseTypeDef = TypedDict(
    "GetVoiceConnectorStreamingConfigurationResponseTypeDef",
    {"StreamingConfiguration": "StreamingConfigurationTypeDef"},
    total=False,
)

GetVoiceConnectorTerminationHealthResponseTypeDef = TypedDict(
    "GetVoiceConnectorTerminationHealthResponseTypeDef",
    {"TerminationHealth": "TerminationHealthTypeDef"},
    total=False,
)

GetVoiceConnectorTerminationResponseTypeDef = TypedDict(
    "GetVoiceConnectorTerminationResponseTypeDef",
    {"Termination": "TerminationTypeDef"},
    total=False,
)

InviteUsersResponseTypeDef = TypedDict(
    "InviteUsersResponseTypeDef", {"Invites": List["InviteTypeDef"]}, total=False
)

ListAccountsResponseTypeDef = TypedDict(
    "ListAccountsResponseTypeDef",
    {"Accounts": List["AccountTypeDef"], "NextToken": str},
    total=False,
)

ListAppInstanceAdminsResponseTypeDef = TypedDict(
    "ListAppInstanceAdminsResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceAdmins": List["AppInstanceAdminSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListAppInstanceUsersResponseTypeDef = TypedDict(
    "ListAppInstanceUsersResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceUsers": List["AppInstanceUserSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListAppInstancesResponseTypeDef = TypedDict(
    "ListAppInstancesResponseTypeDef",
    {"AppInstances": List["AppInstanceSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListAttendeeTagsResponseTypeDef = TypedDict(
    "ListAttendeeTagsResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

ListAttendeesResponseTypeDef = TypedDict(
    "ListAttendeesResponseTypeDef",
    {"Attendees": List["AttendeeTypeDef"], "NextToken": str},
    total=False,
)

ListBotsResponseTypeDef = TypedDict(
    "ListBotsResponseTypeDef", {"Bots": List["BotTypeDef"], "NextToken": str}, total=False
)

ListChannelBansResponseTypeDef = TypedDict(
    "ListChannelBansResponseTypeDef",
    {"ChannelArn": str, "NextToken": str, "ChannelBans": List["ChannelBanSummaryTypeDef"]},
    total=False,
)

ListChannelMembershipsForAppInstanceUserResponseTypeDef = TypedDict(
    "ListChannelMembershipsForAppInstanceUserResponseTypeDef",
    {
        "ChannelMemberships": List["ChannelMembershipForAppInstanceUserSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListChannelMembershipsResponseTypeDef = TypedDict(
    "ListChannelMembershipsResponseTypeDef",
    {
        "ChannelArn": str,
        "ChannelMemberships": List["ChannelMembershipSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListChannelMessagesResponseTypeDef = TypedDict(
    "ListChannelMessagesResponseTypeDef",
    {"ChannelArn": str, "NextToken": str, "ChannelMessages": List["ChannelMessageSummaryTypeDef"]},
    total=False,
)

ListChannelModeratorsResponseTypeDef = TypedDict(
    "ListChannelModeratorsResponseTypeDef",
    {
        "ChannelArn": str,
        "NextToken": str,
        "ChannelModerators": List["ChannelModeratorSummaryTypeDef"],
    },
    total=False,
)

ListChannelsModeratedByAppInstanceUserResponseTypeDef = TypedDict(
    "ListChannelsModeratedByAppInstanceUserResponseTypeDef",
    {"Channels": List["ChannelModeratedByAppInstanceUserSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {"Channels": List["ChannelSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListMeetingTagsResponseTypeDef = TypedDict(
    "ListMeetingTagsResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

ListMeetingsResponseTypeDef = TypedDict(
    "ListMeetingsResponseTypeDef",
    {"Meetings": List["MeetingTypeDef"], "NextToken": str},
    total=False,
)

ListPhoneNumberOrdersResponseTypeDef = TypedDict(
    "ListPhoneNumberOrdersResponseTypeDef",
    {"PhoneNumberOrders": List["PhoneNumberOrderTypeDef"], "NextToken": str},
    total=False,
)

ListPhoneNumbersResponseTypeDef = TypedDict(
    "ListPhoneNumbersResponseTypeDef",
    {"PhoneNumbers": List["PhoneNumberTypeDef"], "NextToken": str},
    total=False,
)

ListProxySessionsResponseTypeDef = TypedDict(
    "ListProxySessionsResponseTypeDef",
    {"ProxySessions": List["ProxySessionTypeDef"], "NextToken": str},
    total=False,
)

ListRoomMembershipsResponseTypeDef = TypedDict(
    "ListRoomMembershipsResponseTypeDef",
    {"RoomMemberships": List["RoomMembershipTypeDef"], "NextToken": str},
    total=False,
)

ListRoomsResponseTypeDef = TypedDict(
    "ListRoomsResponseTypeDef", {"Rooms": List["RoomTypeDef"], "NextToken": str}, total=False
)

ListSipMediaApplicationsResponseTypeDef = TypedDict(
    "ListSipMediaApplicationsResponseTypeDef",
    {"SipMediaApplications": List["SipMediaApplicationTypeDef"], "NextToken": str},
    total=False,
)

ListSipRulesResponseTypeDef = TypedDict(
    "ListSipRulesResponseTypeDef",
    {"SipRules": List["SipRuleTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef", {"Users": List["UserTypeDef"], "NextToken": str}, total=False
)

ListVoiceConnectorGroupsResponseTypeDef = TypedDict(
    "ListVoiceConnectorGroupsResponseTypeDef",
    {"VoiceConnectorGroups": List["VoiceConnectorGroupTypeDef"], "NextToken": str},
    total=False,
)

ListVoiceConnectorTerminationCredentialsResponseTypeDef = TypedDict(
    "ListVoiceConnectorTerminationCredentialsResponseTypeDef", {"Usernames": List[str]}, total=False
)

ListVoiceConnectorsResponseTypeDef = TypedDict(
    "ListVoiceConnectorsResponseTypeDef",
    {"VoiceConnectors": List["VoiceConnectorTypeDef"], "NextToken": str},
    total=False,
)

MeetingNotificationConfigurationTypeDef = TypedDict(
    "MeetingNotificationConfigurationTypeDef", {"SnsTopicArn": str, "SqsQueueArn": str}, total=False
)

MembershipItemTypeDef = TypedDict(
    "MembershipItemTypeDef",
    {"MemberId": str, "Role": Literal["Administrator", "Member"]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutAppInstanceRetentionSettingsResponseTypeDef = TypedDict(
    "PutAppInstanceRetentionSettingsResponseTypeDef",
    {
        "AppInstanceRetentionSettings": "AppInstanceRetentionSettingsTypeDef",
        "InitiateDeletionTimestamp": datetime,
    },
    total=False,
)

PutAppInstanceStreamingConfigurationsResponseTypeDef = TypedDict(
    "PutAppInstanceStreamingConfigurationsResponseTypeDef",
    {"AppInstanceStreamingConfigurations": List["AppInstanceStreamingConfigurationTypeDef"]},
    total=False,
)

PutEventsConfigurationResponseTypeDef = TypedDict(
    "PutEventsConfigurationResponseTypeDef",
    {"EventsConfiguration": "EventsConfigurationTypeDef"},
    total=False,
)

PutRetentionSettingsResponseTypeDef = TypedDict(
    "PutRetentionSettingsResponseTypeDef",
    {"RetentionSettings": "RetentionSettingsTypeDef", "InitiateDeletionTimestamp": datetime},
    total=False,
)

PutSipMediaApplicationLoggingConfigurationResponseTypeDef = TypedDict(
    "PutSipMediaApplicationLoggingConfigurationResponseTypeDef",
    {"SipMediaApplicationLoggingConfiguration": "SipMediaApplicationLoggingConfigurationTypeDef"},
    total=False,
)

PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef = TypedDict(
    "PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    {"EmergencyCallingConfiguration": "EmergencyCallingConfigurationTypeDef"},
    total=False,
)

PutVoiceConnectorLoggingConfigurationResponseTypeDef = TypedDict(
    "PutVoiceConnectorLoggingConfigurationResponseTypeDef",
    {"LoggingConfiguration": "LoggingConfigurationTypeDef"},
    total=False,
)

PutVoiceConnectorOriginationResponseTypeDef = TypedDict(
    "PutVoiceConnectorOriginationResponseTypeDef",
    {"Origination": "OriginationTypeDef"},
    total=False,
)

PutVoiceConnectorProxyResponseTypeDef = TypedDict(
    "PutVoiceConnectorProxyResponseTypeDef", {"Proxy": "ProxyTypeDef"}, total=False
)

PutVoiceConnectorStreamingConfigurationResponseTypeDef = TypedDict(
    "PutVoiceConnectorStreamingConfigurationResponseTypeDef",
    {"StreamingConfiguration": "StreamingConfigurationTypeDef"},
    total=False,
)

PutVoiceConnectorTerminationResponseTypeDef = TypedDict(
    "PutVoiceConnectorTerminationResponseTypeDef",
    {"Termination": "TerminationTypeDef"},
    total=False,
)

RedactChannelMessageResponseTypeDef = TypedDict(
    "RedactChannelMessageResponseTypeDef", {"ChannelArn": str, "MessageId": str}, total=False
)

RegenerateSecurityTokenResponseTypeDef = TypedDict(
    "RegenerateSecurityTokenResponseTypeDef", {"Bot": "BotTypeDef"}, total=False
)

ResetPersonalPINResponseTypeDef = TypedDict(
    "ResetPersonalPINResponseTypeDef", {"User": "UserTypeDef"}, total=False
)

RestorePhoneNumberResponseTypeDef = TypedDict(
    "RestorePhoneNumberResponseTypeDef", {"PhoneNumber": "PhoneNumberTypeDef"}, total=False
)

SearchAvailablePhoneNumbersResponseTypeDef = TypedDict(
    "SearchAvailablePhoneNumbersResponseTypeDef", {"E164PhoneNumbers": List[str]}, total=False
)

SendChannelMessageResponseTypeDef = TypedDict(
    "SendChannelMessageResponseTypeDef", {"ChannelArn": str, "MessageId": str}, total=False
)

UpdateAccountResponseTypeDef = TypedDict(
    "UpdateAccountResponseTypeDef", {"Account": "AccountTypeDef"}, total=False
)

UpdateAppInstanceResponseTypeDef = TypedDict(
    "UpdateAppInstanceResponseTypeDef", {"AppInstanceArn": str}, total=False
)

UpdateAppInstanceUserResponseTypeDef = TypedDict(
    "UpdateAppInstanceUserResponseTypeDef", {"AppInstanceUserArn": str}, total=False
)

UpdateBotResponseTypeDef = TypedDict("UpdateBotResponseTypeDef", {"Bot": "BotTypeDef"}, total=False)

UpdateChannelMessageResponseTypeDef = TypedDict(
    "UpdateChannelMessageResponseTypeDef", {"ChannelArn": str, "MessageId": str}, total=False
)

UpdateChannelReadMarkerResponseTypeDef = TypedDict(
    "UpdateChannelReadMarkerResponseTypeDef", {"ChannelArn": str}, total=False
)

UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef", {"ChannelArn": str}, total=False
)

_RequiredUpdatePhoneNumberRequestItemTypeDef = TypedDict(
    "_RequiredUpdatePhoneNumberRequestItemTypeDef", {"PhoneNumberId": str}
)
_OptionalUpdatePhoneNumberRequestItemTypeDef = TypedDict(
    "_OptionalUpdatePhoneNumberRequestItemTypeDef",
    {"ProductType": Literal["BusinessCalling", "VoiceConnector"], "CallingName": str},
    total=False,
)


class UpdatePhoneNumberRequestItemTypeDef(
    _RequiredUpdatePhoneNumberRequestItemTypeDef, _OptionalUpdatePhoneNumberRequestItemTypeDef
):
    pass


UpdatePhoneNumberResponseTypeDef = TypedDict(
    "UpdatePhoneNumberResponseTypeDef", {"PhoneNumber": "PhoneNumberTypeDef"}, total=False
)

UpdateProxySessionResponseTypeDef = TypedDict(
    "UpdateProxySessionResponseTypeDef", {"ProxySession": "ProxySessionTypeDef"}, total=False
)

UpdateRoomMembershipResponseTypeDef = TypedDict(
    "UpdateRoomMembershipResponseTypeDef", {"RoomMembership": "RoomMembershipTypeDef"}, total=False
)

UpdateRoomResponseTypeDef = TypedDict(
    "UpdateRoomResponseTypeDef", {"Room": "RoomTypeDef"}, total=False
)

UpdateSipMediaApplicationResponseTypeDef = TypedDict(
    "UpdateSipMediaApplicationResponseTypeDef",
    {"SipMediaApplication": "SipMediaApplicationTypeDef"},
    total=False,
)

UpdateSipRuleResponseTypeDef = TypedDict(
    "UpdateSipRuleResponseTypeDef", {"SipRule": "SipRuleTypeDef"}, total=False
)

_RequiredUpdateUserRequestItemTypeDef = TypedDict(
    "_RequiredUpdateUserRequestItemTypeDef", {"UserId": str}
)
_OptionalUpdateUserRequestItemTypeDef = TypedDict(
    "_OptionalUpdateUserRequestItemTypeDef",
    {
        "LicenseType": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "UserType": Literal["PrivateUser", "SharedDevice"],
        "AlexaForBusinessMetadata": "AlexaForBusinessMetadataTypeDef",
    },
    total=False,
)


class UpdateUserRequestItemTypeDef(
    _RequiredUpdateUserRequestItemTypeDef, _OptionalUpdateUserRequestItemTypeDef
):
    pass


UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef", {"User": "UserTypeDef"}, total=False
)

UpdateVoiceConnectorGroupResponseTypeDef = TypedDict(
    "UpdateVoiceConnectorGroupResponseTypeDef",
    {"VoiceConnectorGroup": "VoiceConnectorGroupTypeDef"},
    total=False,
)

UpdateVoiceConnectorResponseTypeDef = TypedDict(
    "UpdateVoiceConnectorResponseTypeDef", {"VoiceConnector": "VoiceConnectorTypeDef"}, total=False
)
