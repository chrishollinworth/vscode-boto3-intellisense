"""
Type annotations for chime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_chime.type_defs import AccountSettingsTypeDef

    data: AccountSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AccountStatusType,
    AccountTypeType,
    AppInstanceDataTypeType,
    CallingNameStatusType,
    CapabilityType,
    ChannelMembershipTypeType,
    ChannelMessagePersistenceTypeType,
    ChannelMessageTypeType,
    ChannelModeType,
    ChannelPrivacyType,
    EmailStatusType,
    ErrorCodeType,
    GeoMatchLevelType,
    InviteStatusType,
    LicenseType,
    MediaPipelineStatusType,
    MemberTypeType,
    NotificationTargetType,
    NumberSelectionBehaviorType,
    OrderedPhoneNumberStatusType,
    OriginationRouteProtocolType,
    PhoneNumberAssociationNameType,
    PhoneNumberOrderStatusType,
    PhoneNumberProductTypeType,
    PhoneNumberStatusType,
    PhoneNumberTypeType,
    ProxySessionStatusType,
    RegistrationStatusType,
    RoomMembershipRoleType,
    SipRuleTriggerTypeType,
    SortOrderType,
    TranscribeLanguageCodeType,
    TranscribeMedicalRegionType,
    TranscribeMedicalSpecialtyType,
    TranscribeMedicalTypeType,
    TranscribeRegionType,
    TranscribeVocabularyFilterMethodType,
    UserTypeType,
    VoiceConnectorAwsRegionType,
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
    "AssociatePhoneNumberWithUserRequestRequestTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    "AssociateSigninDelegateGroupsWithAccountRequestRequestTypeDef",
    "AttendeeTypeDef",
    "BatchChannelMembershipsTypeDef",
    "BatchCreateAttendeeRequestRequestTypeDef",
    "BatchCreateAttendeeResponseTypeDef",
    "BatchCreateChannelMembershipErrorTypeDef",
    "BatchCreateChannelMembershipRequestRequestTypeDef",
    "BatchCreateChannelMembershipResponseTypeDef",
    "BatchCreateRoomMembershipRequestRequestTypeDef",
    "BatchCreateRoomMembershipResponseTypeDef",
    "BatchDeletePhoneNumberRequestRequestTypeDef",
    "BatchDeletePhoneNumberResponseTypeDef",
    "BatchSuspendUserRequestRequestTypeDef",
    "BatchSuspendUserResponseTypeDef",
    "BatchUnsuspendUserRequestRequestTypeDef",
    "BatchUnsuspendUserResponseTypeDef",
    "BatchUpdatePhoneNumberRequestRequestTypeDef",
    "BatchUpdatePhoneNumberResponseTypeDef",
    "BatchUpdateUserRequestRequestTypeDef",
    "BatchUpdateUserResponseTypeDef",
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
    "CreateAccountRequestRequestTypeDef",
    "CreateAccountResponseTypeDef",
    "CreateAppInstanceAdminRequestRequestTypeDef",
    "CreateAppInstanceAdminResponseTypeDef",
    "CreateAppInstanceRequestRequestTypeDef",
    "CreateAppInstanceResponseTypeDef",
    "CreateAppInstanceUserRequestRequestTypeDef",
    "CreateAppInstanceUserResponseTypeDef",
    "CreateAttendeeErrorTypeDef",
    "CreateAttendeeRequestItemTypeDef",
    "CreateAttendeeRequestRequestTypeDef",
    "CreateAttendeeResponseTypeDef",
    "CreateBotRequestRequestTypeDef",
    "CreateBotResponseTypeDef",
    "CreateChannelBanRequestRequestTypeDef",
    "CreateChannelBanResponseTypeDef",
    "CreateChannelMembershipRequestRequestTypeDef",
    "CreateChannelMembershipResponseTypeDef",
    "CreateChannelModeratorRequestRequestTypeDef",
    "CreateChannelModeratorResponseTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateMediaCapturePipelineRequestRequestTypeDef",
    "CreateMediaCapturePipelineResponseTypeDef",
    "CreateMeetingDialOutRequestRequestTypeDef",
    "CreateMeetingDialOutResponseTypeDef",
    "CreateMeetingRequestRequestTypeDef",
    "CreateMeetingResponseTypeDef",
    "CreateMeetingWithAttendeesRequestRequestTypeDef",
    "CreateMeetingWithAttendeesResponseTypeDef",
    "CreatePhoneNumberOrderRequestRequestTypeDef",
    "CreatePhoneNumberOrderResponseTypeDef",
    "CreateProxySessionRequestRequestTypeDef",
    "CreateProxySessionResponseTypeDef",
    "CreateRoomMembershipRequestRequestTypeDef",
    "CreateRoomMembershipResponseTypeDef",
    "CreateRoomRequestRequestTypeDef",
    "CreateRoomResponseTypeDef",
    "CreateSipMediaApplicationCallRequestRequestTypeDef",
    "CreateSipMediaApplicationCallResponseTypeDef",
    "CreateSipMediaApplicationRequestRequestTypeDef",
    "CreateSipMediaApplicationResponseTypeDef",
    "CreateSipRuleRequestRequestTypeDef",
    "CreateSipRuleResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserResponseTypeDef",
    "CreateVoiceConnectorGroupRequestRequestTypeDef",
    "CreateVoiceConnectorGroupResponseTypeDef",
    "CreateVoiceConnectorRequestRequestTypeDef",
    "CreateVoiceConnectorResponseTypeDef",
    "CredentialTypeDef",
    "DNISEmergencyCallingConfigurationTypeDef",
    "DeleteAccountRequestRequestTypeDef",
    "DeleteAppInstanceAdminRequestRequestTypeDef",
    "DeleteAppInstanceRequestRequestTypeDef",
    "DeleteAppInstanceStreamingConfigurationsRequestRequestTypeDef",
    "DeleteAppInstanceUserRequestRequestTypeDef",
    "DeleteAttendeeRequestRequestTypeDef",
    "DeleteChannelBanRequestRequestTypeDef",
    "DeleteChannelMembershipRequestRequestTypeDef",
    "DeleteChannelMessageRequestRequestTypeDef",
    "DeleteChannelModeratorRequestRequestTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteEventsConfigurationRequestRequestTypeDef",
    "DeleteMediaCapturePipelineRequestRequestTypeDef",
    "DeleteMeetingRequestRequestTypeDef",
    "DeletePhoneNumberRequestRequestTypeDef",
    "DeleteProxySessionRequestRequestTypeDef",
    "DeleteRoomMembershipRequestRequestTypeDef",
    "DeleteRoomRequestRequestTypeDef",
    "DeleteSipMediaApplicationRequestRequestTypeDef",
    "DeleteSipRuleRequestRequestTypeDef",
    "DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    "DeleteVoiceConnectorGroupRequestRequestTypeDef",
    "DeleteVoiceConnectorOriginationRequestRequestTypeDef",
    "DeleteVoiceConnectorProxyRequestRequestTypeDef",
    "DeleteVoiceConnectorRequestRequestTypeDef",
    "DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    "DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    "DeleteVoiceConnectorTerminationRequestRequestTypeDef",
    "DescribeAppInstanceAdminRequestRequestTypeDef",
    "DescribeAppInstanceAdminResponseTypeDef",
    "DescribeAppInstanceRequestRequestTypeDef",
    "DescribeAppInstanceResponseTypeDef",
    "DescribeAppInstanceUserRequestRequestTypeDef",
    "DescribeAppInstanceUserResponseTypeDef",
    "DescribeChannelBanRequestRequestTypeDef",
    "DescribeChannelBanResponseTypeDef",
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
    "DisassociatePhoneNumberFromUserRequestRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    "DisassociateSigninDelegateGroupsFromAccountRequestRequestTypeDef",
    "EmergencyCallingConfigurationTypeDef",
    "EngineTranscribeMedicalSettingsTypeDef",
    "EngineTranscribeSettingsTypeDef",
    "EventsConfigurationTypeDef",
    "GeoMatchParamsTypeDef",
    "GetAccountRequestRequestTypeDef",
    "GetAccountResponseTypeDef",
    "GetAccountSettingsRequestRequestTypeDef",
    "GetAccountSettingsResponseTypeDef",
    "GetAppInstanceRetentionSettingsRequestRequestTypeDef",
    "GetAppInstanceRetentionSettingsResponseTypeDef",
    "GetAppInstanceStreamingConfigurationsRequestRequestTypeDef",
    "GetAppInstanceStreamingConfigurationsResponseTypeDef",
    "GetAttendeeRequestRequestTypeDef",
    "GetAttendeeResponseTypeDef",
    "GetBotRequestRequestTypeDef",
    "GetBotResponseTypeDef",
    "GetChannelMessageRequestRequestTypeDef",
    "GetChannelMessageResponseTypeDef",
    "GetEventsConfigurationRequestRequestTypeDef",
    "GetEventsConfigurationResponseTypeDef",
    "GetGlobalSettingsResponseTypeDef",
    "GetMediaCapturePipelineRequestRequestTypeDef",
    "GetMediaCapturePipelineResponseTypeDef",
    "GetMeetingRequestRequestTypeDef",
    "GetMeetingResponseTypeDef",
    "GetMessagingSessionEndpointResponseTypeDef",
    "GetPhoneNumberOrderRequestRequestTypeDef",
    "GetPhoneNumberOrderResponseTypeDef",
    "GetPhoneNumberRequestRequestTypeDef",
    "GetPhoneNumberResponseTypeDef",
    "GetPhoneNumberSettingsResponseTypeDef",
    "GetProxySessionRequestRequestTypeDef",
    "GetProxySessionResponseTypeDef",
    "GetRetentionSettingsRequestRequestTypeDef",
    "GetRetentionSettingsResponseTypeDef",
    "GetRoomRequestRequestTypeDef",
    "GetRoomResponseTypeDef",
    "GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    "GetSipMediaApplicationLoggingConfigurationResponseTypeDef",
    "GetSipMediaApplicationRequestRequestTypeDef",
    "GetSipMediaApplicationResponseTypeDef",
    "GetSipRuleRequestRequestTypeDef",
    "GetSipRuleResponseTypeDef",
    "GetUserRequestRequestTypeDef",
    "GetUserResponseTypeDef",
    "GetUserSettingsRequestRequestTypeDef",
    "GetUserSettingsResponseTypeDef",
    "GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    "GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    "GetVoiceConnectorGroupRequestRequestTypeDef",
    "GetVoiceConnectorGroupResponseTypeDef",
    "GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    "GetVoiceConnectorLoggingConfigurationResponseTypeDef",
    "GetVoiceConnectorOriginationRequestRequestTypeDef",
    "GetVoiceConnectorOriginationResponseTypeDef",
    "GetVoiceConnectorProxyRequestRequestTypeDef",
    "GetVoiceConnectorProxyResponseTypeDef",
    "GetVoiceConnectorRequestRequestTypeDef",
    "GetVoiceConnectorResponseTypeDef",
    "GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    "GetVoiceConnectorStreamingConfigurationResponseTypeDef",
    "GetVoiceConnectorTerminationHealthRequestRequestTypeDef",
    "GetVoiceConnectorTerminationHealthResponseTypeDef",
    "GetVoiceConnectorTerminationRequestRequestTypeDef",
    "GetVoiceConnectorTerminationResponseTypeDef",
    "IdentityTypeDef",
    "InviteTypeDef",
    "InviteUsersRequestRequestTypeDef",
    "InviteUsersResponseTypeDef",
    "ListAccountsRequestRequestTypeDef",
    "ListAccountsResponseTypeDef",
    "ListAppInstanceAdminsRequestRequestTypeDef",
    "ListAppInstanceAdminsResponseTypeDef",
    "ListAppInstanceUsersRequestRequestTypeDef",
    "ListAppInstanceUsersResponseTypeDef",
    "ListAppInstancesRequestRequestTypeDef",
    "ListAppInstancesResponseTypeDef",
    "ListAttendeeTagsRequestRequestTypeDef",
    "ListAttendeeTagsResponseTypeDef",
    "ListAttendeesRequestRequestTypeDef",
    "ListAttendeesResponseTypeDef",
    "ListBotsRequestRequestTypeDef",
    "ListBotsResponseTypeDef",
    "ListChannelBansRequestRequestTypeDef",
    "ListChannelBansResponseTypeDef",
    "ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef",
    "ListChannelMembershipsForAppInstanceUserResponseTypeDef",
    "ListChannelMembershipsRequestRequestTypeDef",
    "ListChannelMembershipsResponseTypeDef",
    "ListChannelMessagesRequestRequestTypeDef",
    "ListChannelMessagesResponseTypeDef",
    "ListChannelModeratorsRequestRequestTypeDef",
    "ListChannelModeratorsResponseTypeDef",
    "ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef",
    "ListChannelsModeratedByAppInstanceUserResponseTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListMediaCapturePipelinesRequestRequestTypeDef",
    "ListMediaCapturePipelinesResponseTypeDef",
    "ListMeetingTagsRequestRequestTypeDef",
    "ListMeetingTagsResponseTypeDef",
    "ListMeetingsRequestRequestTypeDef",
    "ListMeetingsResponseTypeDef",
    "ListPhoneNumberOrdersRequestRequestTypeDef",
    "ListPhoneNumberOrdersResponseTypeDef",
    "ListPhoneNumbersRequestRequestTypeDef",
    "ListPhoneNumbersResponseTypeDef",
    "ListProxySessionsRequestRequestTypeDef",
    "ListProxySessionsResponseTypeDef",
    "ListRoomMembershipsRequestRequestTypeDef",
    "ListRoomMembershipsResponseTypeDef",
    "ListRoomsRequestRequestTypeDef",
    "ListRoomsResponseTypeDef",
    "ListSipMediaApplicationsRequestRequestTypeDef",
    "ListSipMediaApplicationsResponseTypeDef",
    "ListSipRulesRequestRequestTypeDef",
    "ListSipRulesResponseTypeDef",
    "ListSupportedPhoneNumberCountriesRequestRequestTypeDef",
    "ListSupportedPhoneNumberCountriesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "ListVoiceConnectorGroupsRequestRequestTypeDef",
    "ListVoiceConnectorGroupsResponseTypeDef",
    "ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    "ListVoiceConnectorTerminationCredentialsResponseTypeDef",
    "ListVoiceConnectorsRequestRequestTypeDef",
    "ListVoiceConnectorsResponseTypeDef",
    "LoggingConfigurationTypeDef",
    "LogoutUserRequestRequestTypeDef",
    "MediaCapturePipelineTypeDef",
    "MediaPlacementTypeDef",
    "MeetingNotificationConfigurationTypeDef",
    "MeetingTypeDef",
    "MemberErrorTypeDef",
    "MemberTypeDef",
    "MembershipItemTypeDef",
    "MessagingSessionEndpointTypeDef",
    "OrderedPhoneNumberTypeDef",
    "OriginationRouteTypeDef",
    "OriginationTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantTypeDef",
    "PhoneNumberAssociationTypeDef",
    "PhoneNumberCapabilitiesTypeDef",
    "PhoneNumberCountryTypeDef",
    "PhoneNumberErrorTypeDef",
    "PhoneNumberOrderTypeDef",
    "PhoneNumberTypeDef",
    "ProxySessionTypeDef",
    "ProxyTypeDef",
    "PutAppInstanceRetentionSettingsRequestRequestTypeDef",
    "PutAppInstanceRetentionSettingsResponseTypeDef",
    "PutAppInstanceStreamingConfigurationsRequestRequestTypeDef",
    "PutAppInstanceStreamingConfigurationsResponseTypeDef",
    "PutEventsConfigurationRequestRequestTypeDef",
    "PutEventsConfigurationResponseTypeDef",
    "PutRetentionSettingsRequestRequestTypeDef",
    "PutRetentionSettingsResponseTypeDef",
    "PutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    "PutSipMediaApplicationLoggingConfigurationResponseTypeDef",
    "PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    "PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    "PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    "PutVoiceConnectorLoggingConfigurationResponseTypeDef",
    "PutVoiceConnectorOriginationRequestRequestTypeDef",
    "PutVoiceConnectorOriginationResponseTypeDef",
    "PutVoiceConnectorProxyRequestRequestTypeDef",
    "PutVoiceConnectorProxyResponseTypeDef",
    "PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    "PutVoiceConnectorStreamingConfigurationResponseTypeDef",
    "PutVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    "PutVoiceConnectorTerminationRequestRequestTypeDef",
    "PutVoiceConnectorTerminationResponseTypeDef",
    "RedactChannelMessageRequestRequestTypeDef",
    "RedactChannelMessageResponseTypeDef",
    "RedactConversationMessageRequestRequestTypeDef",
    "RedactRoomMessageRequestRequestTypeDef",
    "RegenerateSecurityTokenRequestRequestTypeDef",
    "RegenerateSecurityTokenResponseTypeDef",
    "ResetPersonalPINRequestRequestTypeDef",
    "ResetPersonalPINResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RestorePhoneNumberRequestRequestTypeDef",
    "RestorePhoneNumberResponseTypeDef",
    "RetentionSettingsTypeDef",
    "RoomMembershipTypeDef",
    "RoomRetentionSettingsTypeDef",
    "RoomTypeDef",
    "SearchAvailablePhoneNumbersRequestRequestTypeDef",
    "SearchAvailablePhoneNumbersResponseTypeDef",
    "SendChannelMessageRequestRequestTypeDef",
    "SendChannelMessageResponseTypeDef",
    "SigninDelegateGroupTypeDef",
    "SipMediaApplicationCallTypeDef",
    "SipMediaApplicationEndpointTypeDef",
    "SipMediaApplicationLoggingConfigurationTypeDef",
    "SipMediaApplicationTypeDef",
    "SipRuleTargetApplicationTypeDef",
    "SipRuleTypeDef",
    "StartMeetingTranscriptionRequestRequestTypeDef",
    "StopMeetingTranscriptionRequestRequestTypeDef",
    "StreamingConfigurationTypeDef",
    "StreamingNotificationTargetTypeDef",
    "TagAttendeeRequestRequestTypeDef",
    "TagMeetingRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TelephonySettingsTypeDef",
    "TerminationHealthTypeDef",
    "TerminationTypeDef",
    "TranscriptionConfigurationTypeDef",
    "UntagAttendeeRequestRequestTypeDef",
    "UntagMeetingRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccountRequestRequestTypeDef",
    "UpdateAccountResponseTypeDef",
    "UpdateAccountSettingsRequestRequestTypeDef",
    "UpdateAppInstanceRequestRequestTypeDef",
    "UpdateAppInstanceResponseTypeDef",
    "UpdateAppInstanceUserRequestRequestTypeDef",
    "UpdateAppInstanceUserResponseTypeDef",
    "UpdateBotRequestRequestTypeDef",
    "UpdateBotResponseTypeDef",
    "UpdateChannelMessageRequestRequestTypeDef",
    "UpdateChannelMessageResponseTypeDef",
    "UpdateChannelReadMarkerRequestRequestTypeDef",
    "UpdateChannelReadMarkerResponseTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdateGlobalSettingsRequestRequestTypeDef",
    "UpdatePhoneNumberRequestItemTypeDef",
    "UpdatePhoneNumberRequestRequestTypeDef",
    "UpdatePhoneNumberResponseTypeDef",
    "UpdatePhoneNumberSettingsRequestRequestTypeDef",
    "UpdateProxySessionRequestRequestTypeDef",
    "UpdateProxySessionResponseTypeDef",
    "UpdateRoomMembershipRequestRequestTypeDef",
    "UpdateRoomMembershipResponseTypeDef",
    "UpdateRoomRequestRequestTypeDef",
    "UpdateRoomResponseTypeDef",
    "UpdateSipMediaApplicationCallRequestRequestTypeDef",
    "UpdateSipMediaApplicationCallResponseTypeDef",
    "UpdateSipMediaApplicationRequestRequestTypeDef",
    "UpdateSipMediaApplicationResponseTypeDef",
    "UpdateSipRuleRequestRequestTypeDef",
    "UpdateSipRuleResponseTypeDef",
    "UpdateUserRequestItemTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateUserResponseTypeDef",
    "UpdateUserSettingsRequestRequestTypeDef",
    "UpdateVoiceConnectorGroupRequestRequestTypeDef",
    "UpdateVoiceConnectorGroupResponseTypeDef",
    "UpdateVoiceConnectorRequestRequestTypeDef",
    "UpdateVoiceConnectorResponseTypeDef",
    "UserErrorTypeDef",
    "UserSettingsTypeDef",
    "UserTypeDef",
    "VoiceConnectorGroupTypeDef",
    "VoiceConnectorItemTypeDef",
    "VoiceConnectorSettingsTypeDef",
    "VoiceConnectorTypeDef",
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "DisableRemoteControl": bool,
        "EnableDialOut": bool,
    },
    total=False,
)

_RequiredAccountTypeDef = TypedDict(
    "_RequiredAccountTypeDef",
    {
        "AwsAccountId": str,
        "AccountId": str,
        "Name": str,
    },
)
_OptionalAccountTypeDef = TypedDict(
    "_OptionalAccountTypeDef",
    {
        "AccountType": AccountTypeType,
        "CreatedTimestamp": datetime,
        "DefaultLicense": LicenseType,
        "SupportedLicenses": List[LicenseType],
        "AccountStatus": AccountStatusType,
        "SigninDelegateGroups": List["SigninDelegateGroupTypeDef"],
    },
    total=False,
)

class AccountTypeDef(_RequiredAccountTypeDef, _OptionalAccountTypeDef):
    pass

AlexaForBusinessMetadataTypeDef = TypedDict(
    "AlexaForBusinessMetadataTypeDef",
    {
        "IsAlexaForBusinessEnabled": bool,
        "AlexaForBusinessRoomArn": str,
    },
    total=False,
)

AppInstanceAdminSummaryTypeDef = TypedDict(
    "AppInstanceAdminSummaryTypeDef",
    {
        "Admin": "IdentityTypeDef",
    },
    total=False,
)

AppInstanceAdminTypeDef = TypedDict(
    "AppInstanceAdminTypeDef",
    {
        "Admin": "IdentityTypeDef",
        "AppInstanceArn": str,
        "CreatedTimestamp": datetime,
    },
    total=False,
)

AppInstanceRetentionSettingsTypeDef = TypedDict(
    "AppInstanceRetentionSettingsTypeDef",
    {
        "ChannelRetentionSettings": "ChannelRetentionSettingsTypeDef",
    },
    total=False,
)

AppInstanceStreamingConfigurationTypeDef = TypedDict(
    "AppInstanceStreamingConfigurationTypeDef",
    {
        "AppInstanceDataType": AppInstanceDataTypeType,
        "ResourceArn": str,
    },
)

AppInstanceSummaryTypeDef = TypedDict(
    "AppInstanceSummaryTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "Metadata": str,
    },
    total=False,
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
    {
        "Type": ChannelMembershipTypeType,
        "ReadMarkerTimestamp": datetime,
    },
    total=False,
)

AppInstanceUserSummaryTypeDef = TypedDict(
    "AppInstanceUserSummaryTypeDef",
    {
        "AppInstanceUserArn": str,
        "Name": str,
        "Metadata": str,
    },
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

AssociatePhoneNumberWithUserRequestRequestTypeDef = TypedDict(
    "AssociatePhoneNumberWithUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
        "E164PhoneNumber": str,
    },
)

_RequiredAssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "_RequiredAssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "E164PhoneNumbers": List[str],
    },
)
_OptionalAssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "_OptionalAssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef",
    {
        "ForceAssociate": bool,
    },
    total=False,
)

class AssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef(
    _RequiredAssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef,
    _OptionalAssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef,
):
    pass

AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef = TypedDict(
    "AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef = TypedDict(
    "_RequiredAssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "E164PhoneNumbers": List[str],
    },
)
_OptionalAssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef = TypedDict(
    "_OptionalAssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef",
    {
        "ForceAssociate": bool,
    },
    total=False,
)

class AssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef(
    _RequiredAssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef,
    _OptionalAssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef,
):
    pass

AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef = TypedDict(
    "AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateSigninDelegateGroupsWithAccountRequestRequestTypeDef = TypedDict(
    "AssociateSigninDelegateGroupsWithAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "SigninDelegateGroups": List["SigninDelegateGroupTypeDef"],
    },
)

AttendeeTypeDef = TypedDict(
    "AttendeeTypeDef",
    {
        "ExternalUserId": str,
        "AttendeeId": str,
        "JoinToken": str,
    },
    total=False,
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

BatchCreateAttendeeRequestRequestTypeDef = TypedDict(
    "BatchCreateAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "Attendees": List["CreateAttendeeRequestItemTypeDef"],
    },
)

BatchCreateAttendeeResponseTypeDef = TypedDict(
    "BatchCreateAttendeeResponseTypeDef",
    {
        "Attendees": List["AttendeeTypeDef"],
        "Errors": List["CreateAttendeeErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
    },
)
_OptionalBatchCreateChannelMembershipRequestRequestTypeDef = TypedDict(
    "_OptionalBatchCreateChannelMembershipRequestRequestTypeDef",
    {
        "Type": ChannelMembershipTypeType,
        "ChimeBearer": str,
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

BatchCreateRoomMembershipRequestRequestTypeDef = TypedDict(
    "BatchCreateRoomMembershipRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MembershipItemList": List["MembershipItemTypeDef"],
    },
)

BatchCreateRoomMembershipResponseTypeDef = TypedDict(
    "BatchCreateRoomMembershipResponseTypeDef",
    {
        "Errors": List["MemberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeletePhoneNumberRequestRequestTypeDef = TypedDict(
    "BatchDeletePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberIds": List[str],
    },
)

BatchDeletePhoneNumberResponseTypeDef = TypedDict(
    "BatchDeletePhoneNumberResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchSuspendUserRequestRequestTypeDef = TypedDict(
    "BatchSuspendUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserIdList": List[str],
    },
)

BatchSuspendUserResponseTypeDef = TypedDict(
    "BatchSuspendUserResponseTypeDef",
    {
        "UserErrors": List["UserErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUnsuspendUserRequestRequestTypeDef = TypedDict(
    "BatchUnsuspendUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserIdList": List[str],
    },
)

BatchUnsuspendUserResponseTypeDef = TypedDict(
    "BatchUnsuspendUserResponseTypeDef",
    {
        "UserErrors": List["UserErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "BatchUpdatePhoneNumberRequestRequestTypeDef",
    {
        "UpdatePhoneNumberRequestItems": List["UpdatePhoneNumberRequestItemTypeDef"],
    },
)

BatchUpdatePhoneNumberResponseTypeDef = TypedDict(
    "BatchUpdatePhoneNumberResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdateUserRequestRequestTypeDef = TypedDict(
    "BatchUpdateUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UpdateUserRequestItems": List["UpdateUserRequestItemTypeDef"],
    },
)

BatchUpdateUserResponseTypeDef = TypedDict(
    "BatchUpdateUserResponseTypeDef",
    {
        "UserErrors": List["UserErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
    "BusinessCallingSettingsTypeDef",
    {
        "CdrBucket": str,
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

ChannelMembershipForAppInstanceUserSummaryTypeDef = TypedDict(
    "ChannelMembershipForAppInstanceUserSummaryTypeDef",
    {
        "ChannelSummary": "ChannelSummaryTypeDef",
        "AppInstanceUserMembershipSummary": "AppInstanceUserMembershipSummaryTypeDef",
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

ChannelRetentionSettingsTypeDef = TypedDict(
    "ChannelRetentionSettingsTypeDef",
    {
        "RetentionDays": int,
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
    },
    total=False,
)

ConversationRetentionSettingsTypeDef = TypedDict(
    "ConversationRetentionSettingsTypeDef",
    {
        "RetentionDays": int,
    },
    total=False,
)

CreateAccountRequestRequestTypeDef = TypedDict(
    "CreateAccountRequestRequestTypeDef",
    {
        "Name": str,
    },
)

CreateAccountResponseTypeDef = TypedDict(
    "CreateAccountResponseTypeDef",
    {
        "Account": "AccountTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "CreateAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)

CreateAppInstanceAdminResponseTypeDef = TypedDict(
    "CreateAppInstanceAdminResponseTypeDef",
    {
        "AppInstanceAdmin": "IdentityTypeDef",
        "AppInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAppInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppInstanceRequestRequestTypeDef",
    {
        "Name": str,
        "ClientRequestToken": str,
    },
)
_OptionalCreateAppInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppInstanceRequestRequestTypeDef",
    {
        "Metadata": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateAppInstanceRequestRequestTypeDef(
    _RequiredCreateAppInstanceRequestRequestTypeDef, _OptionalCreateAppInstanceRequestRequestTypeDef
):
    pass

CreateAppInstanceResponseTypeDef = TypedDict(
    "CreateAppInstanceResponseTypeDef",
    {
        "AppInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceUserId": str,
        "Name": str,
        "ClientRequestToken": str,
    },
)
_OptionalCreateAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppInstanceUserRequestRequestTypeDef",
    {
        "Metadata": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateAppInstanceUserRequestRequestTypeDef(
    _RequiredCreateAppInstanceUserRequestRequestTypeDef,
    _OptionalCreateAppInstanceUserRequestRequestTypeDef,
):
    pass

CreateAppInstanceUserResponseTypeDef = TypedDict(
    "CreateAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAttendeeErrorTypeDef = TypedDict(
    "CreateAttendeeErrorTypeDef",
    {
        "ExternalUserId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredCreateAttendeeRequestItemTypeDef = TypedDict(
    "_RequiredCreateAttendeeRequestItemTypeDef",
    {
        "ExternalUserId": str,
    },
)
_OptionalCreateAttendeeRequestItemTypeDef = TypedDict(
    "_OptionalCreateAttendeeRequestItemTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateAttendeeRequestItemTypeDef(
    _RequiredCreateAttendeeRequestItemTypeDef, _OptionalCreateAttendeeRequestItemTypeDef
):
    pass

_RequiredCreateAttendeeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "ExternalUserId": str,
    },
)
_OptionalCreateAttendeeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAttendeeRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateAttendeeRequestRequestTypeDef(
    _RequiredCreateAttendeeRequestRequestTypeDef, _OptionalCreateAttendeeRequestRequestTypeDef
):
    pass

CreateAttendeeResponseTypeDef = TypedDict(
    "CreateAttendeeResponseTypeDef",
    {
        "Attendee": "AttendeeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBotRequestRequestTypeDef",
    {
        "AccountId": str,
        "DisplayName": str,
    },
)
_OptionalCreateBotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBotRequestRequestTypeDef",
    {
        "Domain": str,
    },
    total=False,
)

class CreateBotRequestRequestTypeDef(
    _RequiredCreateBotRequestRequestTypeDef, _OptionalCreateBotRequestRequestTypeDef
):
    pass

CreateBotResponseTypeDef = TypedDict(
    "CreateBotResponseTypeDef",
    {
        "Bot": "BotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateChannelBanRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
    },
)
_OptionalCreateChannelBanRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChannelBanRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)

class CreateChannelBanRequestRequestTypeDef(
    _RequiredCreateChannelBanRequestRequestTypeDef, _OptionalCreateChannelBanRequestRequestTypeDef
):
    pass

CreateChannelBanResponseTypeDef = TypedDict(
    "CreateChannelBanResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": "IdentityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateChannelMembershipRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "Type": ChannelMembershipTypeType,
    },
)
_OptionalCreateChannelMembershipRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChannelMembershipRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)

class CreateChannelMembershipRequestRequestTypeDef(
    _RequiredCreateChannelMembershipRequestRequestTypeDef,
    _OptionalCreateChannelMembershipRequestRequestTypeDef,
):
    pass

CreateChannelMembershipResponseTypeDef = TypedDict(
    "CreateChannelMembershipResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": "IdentityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateChannelModeratorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
    },
)
_OptionalCreateChannelModeratorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChannelModeratorRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)

class CreateChannelModeratorRequestRequestTypeDef(
    _RequiredCreateChannelModeratorRequestRequestTypeDef,
    _OptionalCreateChannelModeratorRequestRequestTypeDef,
):
    pass

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
    },
)
_OptionalCreateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChannelRequestRequestTypeDef",
    {
        "Mode": ChannelModeType,
        "Privacy": ChannelPrivacyType,
        "Metadata": str,
        "Tags": List["TagTypeDef"],
        "ChimeBearer": str,
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

_RequiredCreateMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMediaCapturePipelineRequestRequestTypeDef",
    {
        "SourceType": Literal["ChimeSdkMeeting"],
        "SourceArn": str,
        "SinkType": Literal["S3Bucket"],
        "SinkArn": str,
    },
)
_OptionalCreateMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMediaCapturePipelineRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class CreateMediaCapturePipelineRequestRequestTypeDef(
    _RequiredCreateMediaCapturePipelineRequestRequestTypeDef,
    _OptionalCreateMediaCapturePipelineRequestRequestTypeDef,
):
    pass

CreateMediaCapturePipelineResponseTypeDef = TypedDict(
    "CreateMediaCapturePipelineResponseTypeDef",
    {
        "MediaCapturePipeline": "MediaCapturePipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMeetingDialOutRequestRequestTypeDef = TypedDict(
    "CreateMeetingDialOutRequestRequestTypeDef",
    {
        "MeetingId": str,
        "FromPhoneNumber": str,
        "ToPhoneNumber": str,
        "JoinToken": str,
    },
)

CreateMeetingDialOutResponseTypeDef = TypedDict(
    "CreateMeetingDialOutResponseTypeDef",
    {
        "TransactionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMeetingRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMeetingRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
)
_OptionalCreateMeetingRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMeetingRequestRequestTypeDef",
    {
        "ExternalMeetingId": str,
        "MeetingHostId": str,
        "MediaRegion": str,
        "Tags": List["TagTypeDef"],
        "NotificationsConfiguration": "MeetingNotificationConfigurationTypeDef",
    },
    total=False,
)

class CreateMeetingRequestRequestTypeDef(
    _RequiredCreateMeetingRequestRequestTypeDef, _OptionalCreateMeetingRequestRequestTypeDef
):
    pass

CreateMeetingResponseTypeDef = TypedDict(
    "CreateMeetingResponseTypeDef",
    {
        "Meeting": "MeetingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMeetingWithAttendeesRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMeetingWithAttendeesRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
)
_OptionalCreateMeetingWithAttendeesRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMeetingWithAttendeesRequestRequestTypeDef",
    {
        "ExternalMeetingId": str,
        "MeetingHostId": str,
        "MediaRegion": str,
        "Tags": List["TagTypeDef"],
        "NotificationsConfiguration": "MeetingNotificationConfigurationTypeDef",
        "Attendees": List["CreateAttendeeRequestItemTypeDef"],
    },
    total=False,
)

class CreateMeetingWithAttendeesRequestRequestTypeDef(
    _RequiredCreateMeetingWithAttendeesRequestRequestTypeDef,
    _OptionalCreateMeetingWithAttendeesRequestRequestTypeDef,
):
    pass

CreateMeetingWithAttendeesResponseTypeDef = TypedDict(
    "CreateMeetingWithAttendeesResponseTypeDef",
    {
        "Meeting": "MeetingTypeDef",
        "Attendees": List["AttendeeTypeDef"],
        "Errors": List["CreateAttendeeErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePhoneNumberOrderRequestRequestTypeDef = TypedDict(
    "CreatePhoneNumberOrderRequestRequestTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
        "E164PhoneNumbers": List[str],
    },
)

CreatePhoneNumberOrderResponseTypeDef = TypedDict(
    "CreatePhoneNumberOrderResponseTypeDef",
    {
        "PhoneNumberOrder": "PhoneNumberOrderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProxySessionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ParticipantPhoneNumbers": List[str],
        "Capabilities": List[CapabilityType],
    },
)
_OptionalCreateProxySessionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProxySessionRequestRequestTypeDef",
    {
        "Name": str,
        "ExpiryMinutes": int,
        "NumberSelectionBehavior": NumberSelectionBehaviorType,
        "GeoMatchLevel": GeoMatchLevelType,
        "GeoMatchParams": "GeoMatchParamsTypeDef",
    },
    total=False,
)

class CreateProxySessionRequestRequestTypeDef(
    _RequiredCreateProxySessionRequestRequestTypeDef,
    _OptionalCreateProxySessionRequestRequestTypeDef,
):
    pass

CreateProxySessionResponseTypeDef = TypedDict(
    "CreateProxySessionResponseTypeDef",
    {
        "ProxySession": "ProxySessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRoomMembershipRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRoomMembershipRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MemberId": str,
    },
)
_OptionalCreateRoomMembershipRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRoomMembershipRequestRequestTypeDef",
    {
        "Role": RoomMembershipRoleType,
    },
    total=False,
)

class CreateRoomMembershipRequestRequestTypeDef(
    _RequiredCreateRoomMembershipRequestRequestTypeDef,
    _OptionalCreateRoomMembershipRequestRequestTypeDef,
):
    pass

CreateRoomMembershipResponseTypeDef = TypedDict(
    "CreateRoomMembershipResponseTypeDef",
    {
        "RoomMembership": "RoomMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRoomRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRoomRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)
_OptionalCreateRoomRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRoomRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class CreateRoomRequestRequestTypeDef(
    _RequiredCreateRoomRequestRequestTypeDef, _OptionalCreateRoomRequestRequestTypeDef
):
    pass

CreateRoomResponseTypeDef = TypedDict(
    "CreateRoomResponseTypeDef",
    {
        "Room": "RoomTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSipMediaApplicationCallRequestRequestTypeDef = TypedDict(
    "CreateSipMediaApplicationCallRequestRequestTypeDef",
    {
        "FromPhoneNumber": str,
        "ToPhoneNumber": str,
        "SipMediaApplicationId": str,
    },
)

CreateSipMediaApplicationCallResponseTypeDef = TypedDict(
    "CreateSipMediaApplicationCallResponseTypeDef",
    {
        "SipMediaApplicationCall": "SipMediaApplicationCallTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "CreateSipMediaApplicationRequestRequestTypeDef",
    {
        "AwsRegion": str,
        "Name": str,
        "Endpoints": List["SipMediaApplicationEndpointTypeDef"],
    },
)

CreateSipMediaApplicationResponseTypeDef = TypedDict(
    "CreateSipMediaApplicationResponseTypeDef",
    {
        "SipMediaApplication": "SipMediaApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSipRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSipRuleRequestRequestTypeDef",
    {
        "Name": str,
        "TriggerType": SipRuleTriggerTypeType,
        "TriggerValue": str,
        "TargetApplications": List["SipRuleTargetApplicationTypeDef"],
    },
)
_OptionalCreateSipRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSipRuleRequestRequestTypeDef",
    {
        "Disabled": bool,
    },
    total=False,
)

class CreateSipRuleRequestRequestTypeDef(
    _RequiredCreateSipRuleRequestRequestTypeDef, _OptionalCreateSipRuleRequestRequestTypeDef
):
    pass

CreateSipRuleResponseTypeDef = TypedDict(
    "CreateSipRuleResponseTypeDef",
    {
        "SipRule": "SipRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalCreateUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestRequestTypeDef",
    {
        "Username": str,
        "Email": str,
        "UserType": UserTypeType,
    },
    total=False,
)

class CreateUserRequestRequestTypeDef(
    _RequiredCreateUserRequestRequestTypeDef, _OptionalCreateUserRequestRequestTypeDef
):
    pass

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVoiceConnectorGroupRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorItems": List["VoiceConnectorItemTypeDef"],
    },
    total=False,
)

class CreateVoiceConnectorGroupRequestRequestTypeDef(
    _RequiredCreateVoiceConnectorGroupRequestRequestTypeDef,
    _OptionalCreateVoiceConnectorGroupRequestRequestTypeDef,
):
    pass

CreateVoiceConnectorGroupResponseTypeDef = TypedDict(
    "CreateVoiceConnectorGroupResponseTypeDef",
    {
        "VoiceConnectorGroup": "VoiceConnectorGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVoiceConnectorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVoiceConnectorRequestRequestTypeDef",
    {
        "Name": str,
        "RequireEncryption": bool,
    },
)
_OptionalCreateVoiceConnectorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVoiceConnectorRequestRequestTypeDef",
    {
        "AwsRegion": VoiceConnectorAwsRegionType,
    },
    total=False,
)

class CreateVoiceConnectorRequestRequestTypeDef(
    _RequiredCreateVoiceConnectorRequestRequestTypeDef,
    _OptionalCreateVoiceConnectorRequestRequestTypeDef,
):
    pass

CreateVoiceConnectorResponseTypeDef = TypedDict(
    "CreateVoiceConnectorResponseTypeDef",
    {
        "VoiceConnector": "VoiceConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CredentialTypeDef = TypedDict(
    "CredentialTypeDef",
    {
        "Username": str,
        "Password": str,
    },
    total=False,
)

_RequiredDNISEmergencyCallingConfigurationTypeDef = TypedDict(
    "_RequiredDNISEmergencyCallingConfigurationTypeDef",
    {
        "EmergencyPhoneNumber": str,
        "CallingCountry": str,
    },
)
_OptionalDNISEmergencyCallingConfigurationTypeDef = TypedDict(
    "_OptionalDNISEmergencyCallingConfigurationTypeDef",
    {
        "TestPhoneNumber": str,
    },
    total=False,
)

class DNISEmergencyCallingConfigurationTypeDef(
    _RequiredDNISEmergencyCallingConfigurationTypeDef,
    _OptionalDNISEmergencyCallingConfigurationTypeDef,
):
    pass

DeleteAccountRequestRequestTypeDef = TypedDict(
    "DeleteAccountRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

DeleteAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)

DeleteAppInstanceRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

DeleteAppInstanceStreamingConfigurationsRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceStreamingConfigurationsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

DeleteAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)

DeleteAttendeeRequestRequestTypeDef = TypedDict(
    "DeleteAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)

_RequiredDeleteChannelBanRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
    },
)
_OptionalDeleteChannelBanRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteChannelBanRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)

class DeleteChannelBanRequestRequestTypeDef(
    _RequiredDeleteChannelBanRequestRequestTypeDef, _OptionalDeleteChannelBanRequestRequestTypeDef
):
    pass

_RequiredDeleteChannelMembershipRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
    },
)
_OptionalDeleteChannelMembershipRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteChannelMembershipRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)

class DeleteChannelMembershipRequestRequestTypeDef(
    _RequiredDeleteChannelMembershipRequestRequestTypeDef,
    _OptionalDeleteChannelMembershipRequestRequestTypeDef,
):
    pass

_RequiredDeleteChannelMessageRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
    },
)
_OptionalDeleteChannelMessageRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteChannelMessageRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)

class DeleteChannelMessageRequestRequestTypeDef(
    _RequiredDeleteChannelMessageRequestRequestTypeDef,
    _OptionalDeleteChannelMessageRequestRequestTypeDef,
):
    pass

_RequiredDeleteChannelModeratorRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
    },
)
_OptionalDeleteChannelModeratorRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteChannelModeratorRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)

class DeleteChannelModeratorRequestRequestTypeDef(
    _RequiredDeleteChannelModeratorRequestRequestTypeDef,
    _OptionalDeleteChannelModeratorRequestRequestTypeDef,
):
    pass

_RequiredDeleteChannelRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
    },
)
_OptionalDeleteChannelRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteChannelRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)

class DeleteChannelRequestRequestTypeDef(
    _RequiredDeleteChannelRequestRequestTypeDef, _OptionalDeleteChannelRequestRequestTypeDef
):
    pass

DeleteEventsConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteEventsConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)

DeleteMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "DeleteMediaCapturePipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)

DeleteMeetingRequestRequestTypeDef = TypedDict(
    "DeleteMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)

DeletePhoneNumberRequestRequestTypeDef = TypedDict(
    "DeletePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)

DeleteProxySessionRequestRequestTypeDef = TypedDict(
    "DeleteProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
    },
)

DeleteRoomMembershipRequestRequestTypeDef = TypedDict(
    "DeleteRoomMembershipRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MemberId": str,
    },
)

DeleteRoomRequestRequestTypeDef = TypedDict(
    "DeleteRoomRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
    },
)

DeleteSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "DeleteSipMediaApplicationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)

DeleteSipRuleRequestRequestTypeDef = TypedDict(
    "DeleteSipRuleRequestRequestTypeDef",
    {
        "SipRuleId": str,
    },
)

DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
    },
)

DeleteVoiceConnectorOriginationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorOriginationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorProxyRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorProxyRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Usernames": List[str],
    },
)

DeleteVoiceConnectorTerminationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorTerminationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DescribeAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)

DescribeAppInstanceAdminResponseTypeDef = TypedDict(
    "DescribeAppInstanceAdminResponseTypeDef",
    {
        "AppInstanceAdmin": "AppInstanceAdminTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppInstanceRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

DescribeAppInstanceResponseTypeDef = TypedDict(
    "DescribeAppInstanceResponseTypeDef",
    {
        "AppInstance": "AppInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)

DescribeAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUser": "AppInstanceUserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeChannelBanRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
    },
)
_OptionalDescribeChannelBanRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeChannelBanRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)

class DescribeChannelBanRequestRequestTypeDef(
    _RequiredDescribeChannelBanRequestRequestTypeDef,
    _OptionalDescribeChannelBanRequestRequestTypeDef,
):
    pass

DescribeChannelBanResponseTypeDef = TypedDict(
    "DescribeChannelBanResponseTypeDef",
    {
        "ChannelBan": "ChannelBanTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "AppInstanceUserArn": str,
    },
)
_OptionalDescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)

class DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef(
    _RequiredDescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef,
    _OptionalDescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef,
):
    pass

DescribeChannelMembershipForAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeChannelMembershipForAppInstanceUserResponseTypeDef",
    {
        "ChannelMembership": "ChannelMembershipForAppInstanceUserSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeChannelMembershipRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
    },
)
_OptionalDescribeChannelMembershipRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeChannelMembershipRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)

class DescribeChannelMembershipRequestRequestTypeDef(
    _RequiredDescribeChannelMembershipRequestRequestTypeDef,
    _OptionalDescribeChannelMembershipRequestRequestTypeDef,
):
    pass

DescribeChannelMembershipResponseTypeDef = TypedDict(
    "DescribeChannelMembershipResponseTypeDef",
    {
        "ChannelMembership": "ChannelMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "AppInstanceUserArn": str,
    },
)
_OptionalDescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)

class DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef(
    _RequiredDescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef,
    _OptionalDescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef,
):
    pass

DescribeChannelModeratedByAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeChannelModeratedByAppInstanceUserResponseTypeDef",
    {
        "Channel": "ChannelModeratedByAppInstanceUserSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeChannelModeratorRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
    },
)
_OptionalDescribeChannelModeratorRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeChannelModeratorRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)

class DescribeChannelModeratorRequestRequestTypeDef(
    _RequiredDescribeChannelModeratorRequestRequestTypeDef,
    _OptionalDescribeChannelModeratorRequestRequestTypeDef,
):
    pass

DescribeChannelModeratorResponseTypeDef = TypedDict(
    "DescribeChannelModeratorResponseTypeDef",
    {
        "ChannelModerator": "ChannelModeratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeChannelRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
    },
)
_OptionalDescribeChannelRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeChannelRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)

class DescribeChannelRequestRequestTypeDef(
    _RequiredDescribeChannelRequestRequestTypeDef, _OptionalDescribeChannelRequestRequestTypeDef
):
    pass

DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "Channel": "ChannelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociatePhoneNumberFromUserRequestRequestTypeDef = TypedDict(
    "DisassociatePhoneNumberFromUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)

DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "E164PhoneNumbers": List[str],
    },
)

DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "E164PhoneNumbers": List[str],
    },
)

DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateSigninDelegateGroupsFromAccountRequestRequestTypeDef = TypedDict(
    "DisassociateSigninDelegateGroupsFromAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "GroupNames": List[str],
    },
)

EmergencyCallingConfigurationTypeDef = TypedDict(
    "EmergencyCallingConfigurationTypeDef",
    {
        "DNIS": List["DNISEmergencyCallingConfigurationTypeDef"],
    },
    total=False,
)

_RequiredEngineTranscribeMedicalSettingsTypeDef = TypedDict(
    "_RequiredEngineTranscribeMedicalSettingsTypeDef",
    {
        "LanguageCode": Literal["en-US"],
        "Specialty": TranscribeMedicalSpecialtyType,
        "Type": TranscribeMedicalTypeType,
    },
)
_OptionalEngineTranscribeMedicalSettingsTypeDef = TypedDict(
    "_OptionalEngineTranscribeMedicalSettingsTypeDef",
    {
        "VocabularyName": str,
        "Region": TranscribeMedicalRegionType,
    },
    total=False,
)

class EngineTranscribeMedicalSettingsTypeDef(
    _RequiredEngineTranscribeMedicalSettingsTypeDef, _OptionalEngineTranscribeMedicalSettingsTypeDef
):
    pass

_RequiredEngineTranscribeSettingsTypeDef = TypedDict(
    "_RequiredEngineTranscribeSettingsTypeDef",
    {
        "LanguageCode": TranscribeLanguageCodeType,
    },
)
_OptionalEngineTranscribeSettingsTypeDef = TypedDict(
    "_OptionalEngineTranscribeSettingsTypeDef",
    {
        "VocabularyFilterMethod": TranscribeVocabularyFilterMethodType,
        "VocabularyFilterName": str,
        "VocabularyName": str,
        "Region": TranscribeRegionType,
    },
    total=False,
)

class EngineTranscribeSettingsTypeDef(
    _RequiredEngineTranscribeSettingsTypeDef, _OptionalEngineTranscribeSettingsTypeDef
):
    pass

EventsConfigurationTypeDef = TypedDict(
    "EventsConfigurationTypeDef",
    {
        "BotId": str,
        "OutboundEventsHTTPSEndpoint": str,
        "LambdaFunctionArn": str,
    },
    total=False,
)

GeoMatchParamsTypeDef = TypedDict(
    "GeoMatchParamsTypeDef",
    {
        "Country": str,
        "AreaCode": str,
    },
)

GetAccountRequestRequestTypeDef = TypedDict(
    "GetAccountRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

GetAccountResponseTypeDef = TypedDict(
    "GetAccountResponseTypeDef",
    {
        "Account": "AccountTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccountSettingsRequestRequestTypeDef = TypedDict(
    "GetAccountSettingsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

GetAccountSettingsResponseTypeDef = TypedDict(
    "GetAccountSettingsResponseTypeDef",
    {
        "AccountSettings": "AccountSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppInstanceRetentionSettingsRequestRequestTypeDef = TypedDict(
    "GetAppInstanceRetentionSettingsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

GetAppInstanceRetentionSettingsResponseTypeDef = TypedDict(
    "GetAppInstanceRetentionSettingsResponseTypeDef",
    {
        "AppInstanceRetentionSettings": "AppInstanceRetentionSettingsTypeDef",
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppInstanceStreamingConfigurationsRequestRequestTypeDef = TypedDict(
    "GetAppInstanceStreamingConfigurationsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

GetAppInstanceStreamingConfigurationsResponseTypeDef = TypedDict(
    "GetAppInstanceStreamingConfigurationsResponseTypeDef",
    {
        "AppInstanceStreamingConfigurations": List["AppInstanceStreamingConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAttendeeRequestRequestTypeDef = TypedDict(
    "GetAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)

GetAttendeeResponseTypeDef = TypedDict(
    "GetAttendeeResponseTypeDef",
    {
        "Attendee": "AttendeeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBotRequestRequestTypeDef = TypedDict(
    "GetBotRequestRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)

GetBotResponseTypeDef = TypedDict(
    "GetBotResponseTypeDef",
    {
        "Bot": "BotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetChannelMessageRequestRequestTypeDef = TypedDict(
    "_RequiredGetChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
    },
)
_OptionalGetChannelMessageRequestRequestTypeDef = TypedDict(
    "_OptionalGetChannelMessageRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)

class GetChannelMessageRequestRequestTypeDef(
    _RequiredGetChannelMessageRequestRequestTypeDef, _OptionalGetChannelMessageRequestRequestTypeDef
):
    pass

GetChannelMessageResponseTypeDef = TypedDict(
    "GetChannelMessageResponseTypeDef",
    {
        "ChannelMessage": "ChannelMessageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventsConfigurationRequestRequestTypeDef = TypedDict(
    "GetEventsConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)

GetEventsConfigurationResponseTypeDef = TypedDict(
    "GetEventsConfigurationResponseTypeDef",
    {
        "EventsConfiguration": "EventsConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGlobalSettingsResponseTypeDef = TypedDict(
    "GetGlobalSettingsResponseTypeDef",
    {
        "BusinessCalling": "BusinessCallingSettingsTypeDef",
        "VoiceConnector": "VoiceConnectorSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "GetMediaCapturePipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)

GetMediaCapturePipelineResponseTypeDef = TypedDict(
    "GetMediaCapturePipelineResponseTypeDef",
    {
        "MediaCapturePipeline": "MediaCapturePipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMeetingRequestRequestTypeDef = TypedDict(
    "GetMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)

GetMeetingResponseTypeDef = TypedDict(
    "GetMeetingResponseTypeDef",
    {
        "Meeting": "MeetingTypeDef",
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

GetPhoneNumberOrderRequestRequestTypeDef = TypedDict(
    "GetPhoneNumberOrderRequestRequestTypeDef",
    {
        "PhoneNumberOrderId": str,
    },
)

GetPhoneNumberOrderResponseTypeDef = TypedDict(
    "GetPhoneNumberOrderResponseTypeDef",
    {
        "PhoneNumberOrder": "PhoneNumberOrderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPhoneNumberRequestRequestTypeDef = TypedDict(
    "GetPhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)

GetPhoneNumberResponseTypeDef = TypedDict(
    "GetPhoneNumberResponseTypeDef",
    {
        "PhoneNumber": "PhoneNumberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPhoneNumberSettingsResponseTypeDef = TypedDict(
    "GetPhoneNumberSettingsResponseTypeDef",
    {
        "CallingName": str,
        "CallingNameUpdatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProxySessionRequestRequestTypeDef = TypedDict(
    "GetProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
    },
)

GetProxySessionResponseTypeDef = TypedDict(
    "GetProxySessionResponseTypeDef",
    {
        "ProxySession": "ProxySessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRetentionSettingsRequestRequestTypeDef = TypedDict(
    "GetRetentionSettingsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

GetRetentionSettingsResponseTypeDef = TypedDict(
    "GetRetentionSettingsResponseTypeDef",
    {
        "RetentionSettings": "RetentionSettingsTypeDef",
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRoomRequestRequestTypeDef = TypedDict(
    "GetRoomRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
    },
)

GetRoomResponseTypeDef = TypedDict(
    "GetRoomResponseTypeDef",
    {
        "Room": "RoomTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)

GetSipMediaApplicationLoggingConfigurationResponseTypeDef = TypedDict(
    "GetSipMediaApplicationLoggingConfigurationResponseTypeDef",
    {
        "SipMediaApplicationLoggingConfiguration": "SipMediaApplicationLoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "GetSipMediaApplicationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)

GetSipMediaApplicationResponseTypeDef = TypedDict(
    "GetSipMediaApplicationResponseTypeDef",
    {
        "SipMediaApplication": "SipMediaApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSipRuleRequestRequestTypeDef = TypedDict(
    "GetSipRuleRequestRequestTypeDef",
    {
        "SipRuleId": str,
    },
)

GetSipRuleResponseTypeDef = TypedDict(
    "GetSipRuleResponseTypeDef",
    {
        "SipRule": "SipRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserRequestRequestTypeDef = TypedDict(
    "GetUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)

GetUserResponseTypeDef = TypedDict(
    "GetUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserSettingsRequestRequestTypeDef = TypedDict(
    "GetUserSettingsRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)

GetUserSettingsResponseTypeDef = TypedDict(
    "GetUserSettingsResponseTypeDef",
    {
        "UserSettings": "UserSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef = TypedDict(
    "GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    {
        "EmergencyCallingConfiguration": "EmergencyCallingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
    },
)

GetVoiceConnectorGroupResponseTypeDef = TypedDict(
    "GetVoiceConnectorGroupResponseTypeDef",
    {
        "VoiceConnectorGroup": "VoiceConnectorGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorLoggingConfigurationResponseTypeDef = TypedDict(
    "GetVoiceConnectorLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorOriginationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorOriginationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorOriginationResponseTypeDef = TypedDict(
    "GetVoiceConnectorOriginationResponseTypeDef",
    {
        "Origination": "OriginationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorProxyRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorProxyRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorProxyResponseTypeDef = TypedDict(
    "GetVoiceConnectorProxyResponseTypeDef",
    {
        "Proxy": "ProxyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorResponseTypeDef = TypedDict(
    "GetVoiceConnectorResponseTypeDef",
    {
        "VoiceConnector": "VoiceConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorStreamingConfigurationResponseTypeDef = TypedDict(
    "GetVoiceConnectorStreamingConfigurationResponseTypeDef",
    {
        "StreamingConfiguration": "StreamingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorTerminationHealthRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorTerminationHealthRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorTerminationHealthResponseTypeDef = TypedDict(
    "GetVoiceConnectorTerminationHealthResponseTypeDef",
    {
        "TerminationHealth": "TerminationHealthTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorTerminationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorTerminationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorTerminationResponseTypeDef = TypedDict(
    "GetVoiceConnectorTerminationResponseTypeDef",
    {
        "Termination": "TerminationTypeDef",
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

InviteTypeDef = TypedDict(
    "InviteTypeDef",
    {
        "InviteId": str,
        "Status": InviteStatusType,
        "EmailAddress": str,
        "EmailStatus": EmailStatusType,
    },
    total=False,
)

_RequiredInviteUsersRequestRequestTypeDef = TypedDict(
    "_RequiredInviteUsersRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserEmailList": List[str],
    },
)
_OptionalInviteUsersRequestRequestTypeDef = TypedDict(
    "_OptionalInviteUsersRequestRequestTypeDef",
    {
        "UserType": UserTypeType,
    },
    total=False,
)

class InviteUsersRequestRequestTypeDef(
    _RequiredInviteUsersRequestRequestTypeDef, _OptionalInviteUsersRequestRequestTypeDef
):
    pass

InviteUsersResponseTypeDef = TypedDict(
    "InviteUsersResponseTypeDef",
    {
        "Invites": List["InviteTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAccountsRequestRequestTypeDef = TypedDict(
    "ListAccountsRequestRequestTypeDef",
    {
        "Name": str,
        "UserEmail": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListAccountsResponseTypeDef = TypedDict(
    "ListAccountsResponseTypeDef",
    {
        "Accounts": List["AccountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAppInstanceAdminsRequestRequestTypeDef = TypedDict(
    "_RequiredListAppInstanceAdminsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
_OptionalListAppInstanceAdminsRequestRequestTypeDef = TypedDict(
    "_OptionalListAppInstanceAdminsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAppInstanceAdminsRequestRequestTypeDef(
    _RequiredListAppInstanceAdminsRequestRequestTypeDef,
    _OptionalListAppInstanceAdminsRequestRequestTypeDef,
):
    pass

ListAppInstanceAdminsResponseTypeDef = TypedDict(
    "ListAppInstanceAdminsResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceAdmins": List["AppInstanceAdminSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAppInstanceUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListAppInstanceUsersRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
_OptionalListAppInstanceUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListAppInstanceUsersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAppInstanceUsersRequestRequestTypeDef(
    _RequiredListAppInstanceUsersRequestRequestTypeDef,
    _OptionalListAppInstanceUsersRequestRequestTypeDef,
):
    pass

ListAppInstanceUsersResponseTypeDef = TypedDict(
    "ListAppInstanceUsersResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceUsers": List["AppInstanceUserSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppInstancesRequestRequestTypeDef = TypedDict(
    "ListAppInstancesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListAppInstancesResponseTypeDef = TypedDict(
    "ListAppInstancesResponseTypeDef",
    {
        "AppInstances": List["AppInstanceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAttendeeTagsRequestRequestTypeDef = TypedDict(
    "ListAttendeeTagsRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)

ListAttendeeTagsResponseTypeDef = TypedDict(
    "ListAttendeeTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAttendeesRequestRequestTypeDef = TypedDict(
    "_RequiredListAttendeesRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)
_OptionalListAttendeesRequestRequestTypeDef = TypedDict(
    "_OptionalListAttendeesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListAttendeesRequestRequestTypeDef(
    _RequiredListAttendeesRequestRequestTypeDef, _OptionalListAttendeesRequestRequestTypeDef
):
    pass

ListAttendeesResponseTypeDef = TypedDict(
    "ListAttendeesResponseTypeDef",
    {
        "Attendees": List["AttendeeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBotsRequestRequestTypeDef = TypedDict(
    "_RequiredListBotsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListBotsRequestRequestTypeDef = TypedDict(
    "_OptionalListBotsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListBotsRequestRequestTypeDef(
    _RequiredListBotsRequestRequestTypeDef, _OptionalListBotsRequestRequestTypeDef
):
    pass

ListBotsResponseTypeDef = TypedDict(
    "ListBotsResponseTypeDef",
    {
        "Bots": List["BotTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChannelBansRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelBansRequestRequestTypeDef",
    {
        "ChannelArn": str,
    },
)
_OptionalListChannelBansRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelBansRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ChimeBearer": str,
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

ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef = TypedDict(
    "ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "MaxResults": int,
        "NextToken": str,
        "ChimeBearer": str,
    },
    total=False,
)

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
    },
)
_OptionalListChannelMembershipsRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelMembershipsRequestRequestTypeDef",
    {
        "Type": ChannelMembershipTypeType,
        "MaxResults": int,
        "NextToken": str,
        "ChimeBearer": str,
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
        "ChimeBearer": str,
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
    },
)
_OptionalListChannelModeratorsRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelModeratorsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ChimeBearer": str,
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

ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef = TypedDict(
    "ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "MaxResults": int,
        "NextToken": str,
        "ChimeBearer": str,
    },
    total=False,
)

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
    },
)
_OptionalListChannelsRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelsRequestRequestTypeDef",
    {
        "Privacy": ChannelPrivacyType,
        "MaxResults": int,
        "NextToken": str,
        "ChimeBearer": str,
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

ListMediaCapturePipelinesRequestRequestTypeDef = TypedDict(
    "ListMediaCapturePipelinesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListMediaCapturePipelinesResponseTypeDef = TypedDict(
    "ListMediaCapturePipelinesResponseTypeDef",
    {
        "MediaCapturePipelines": List["MediaCapturePipelineTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMeetingTagsRequestRequestTypeDef = TypedDict(
    "ListMeetingTagsRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)

ListMeetingTagsResponseTypeDef = TypedDict(
    "ListMeetingTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMeetingsRequestRequestTypeDef = TypedDict(
    "ListMeetingsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListMeetingsResponseTypeDef = TypedDict(
    "ListMeetingsResponseTypeDef",
    {
        "Meetings": List["MeetingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPhoneNumberOrdersRequestRequestTypeDef = TypedDict(
    "ListPhoneNumberOrdersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPhoneNumberOrdersResponseTypeDef = TypedDict(
    "ListPhoneNumberOrdersResponseTypeDef",
    {
        "PhoneNumberOrders": List["PhoneNumberOrderTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPhoneNumbersRequestRequestTypeDef = TypedDict(
    "ListPhoneNumbersRequestRequestTypeDef",
    {
        "Status": PhoneNumberStatusType,
        "ProductType": PhoneNumberProductTypeType,
        "FilterName": PhoneNumberAssociationNameType,
        "FilterValue": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListPhoneNumbersResponseTypeDef = TypedDict(
    "ListPhoneNumbersResponseTypeDef",
    {
        "PhoneNumbers": List["PhoneNumberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProxySessionsRequestRequestTypeDef = TypedDict(
    "_RequiredListProxySessionsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
_OptionalListProxySessionsRequestRequestTypeDef = TypedDict(
    "_OptionalListProxySessionsRequestRequestTypeDef",
    {
        "Status": ProxySessionStatusType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListProxySessionsRequestRequestTypeDef(
    _RequiredListProxySessionsRequestRequestTypeDef, _OptionalListProxySessionsRequestRequestTypeDef
):
    pass

ListProxySessionsResponseTypeDef = TypedDict(
    "ListProxySessionsResponseTypeDef",
    {
        "ProxySessions": List["ProxySessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRoomMembershipsRequestRequestTypeDef = TypedDict(
    "_RequiredListRoomMembershipsRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
    },
)
_OptionalListRoomMembershipsRequestRequestTypeDef = TypedDict(
    "_OptionalListRoomMembershipsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListRoomMembershipsRequestRequestTypeDef(
    _RequiredListRoomMembershipsRequestRequestTypeDef,
    _OptionalListRoomMembershipsRequestRequestTypeDef,
):
    pass

ListRoomMembershipsResponseTypeDef = TypedDict(
    "ListRoomMembershipsResponseTypeDef",
    {
        "RoomMemberships": List["RoomMembershipTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRoomsRequestRequestTypeDef = TypedDict(
    "_RequiredListRoomsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListRoomsRequestRequestTypeDef = TypedDict(
    "_OptionalListRoomsRequestRequestTypeDef",
    {
        "MemberId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListRoomsRequestRequestTypeDef(
    _RequiredListRoomsRequestRequestTypeDef, _OptionalListRoomsRequestRequestTypeDef
):
    pass

ListRoomsResponseTypeDef = TypedDict(
    "ListRoomsResponseTypeDef",
    {
        "Rooms": List["RoomTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSipMediaApplicationsRequestRequestTypeDef = TypedDict(
    "ListSipMediaApplicationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSipMediaApplicationsResponseTypeDef = TypedDict(
    "ListSipMediaApplicationsResponseTypeDef",
    {
        "SipMediaApplications": List["SipMediaApplicationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSipRulesRequestRequestTypeDef = TypedDict(
    "ListSipRulesRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSipRulesResponseTypeDef = TypedDict(
    "ListSipRulesResponseTypeDef",
    {
        "SipRules": List["SipRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSupportedPhoneNumberCountriesRequestRequestTypeDef = TypedDict(
    "ListSupportedPhoneNumberCountriesRequestRequestTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
    },
)

ListSupportedPhoneNumberCountriesResponseTypeDef = TypedDict(
    "ListSupportedPhoneNumberCountriesResponseTypeDef",
    {
        "PhoneNumberCountries": List["PhoneNumberCountryTypeDef"],
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

_RequiredListUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestRequestTypeDef",
    {
        "UserEmail": str,
        "UserType": UserTypeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListUsersRequestRequestTypeDef(
    _RequiredListUsersRequestRequestTypeDef, _OptionalListUsersRequestRequestTypeDef
):
    pass

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "Users": List["UserTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVoiceConnectorGroupsRequestRequestTypeDef = TypedDict(
    "ListVoiceConnectorGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListVoiceConnectorGroupsResponseTypeDef = TypedDict(
    "ListVoiceConnectorGroupsResponseTypeDef",
    {
        "VoiceConnectorGroups": List["VoiceConnectorGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef = TypedDict(
    "ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

ListVoiceConnectorTerminationCredentialsResponseTypeDef = TypedDict(
    "ListVoiceConnectorTerminationCredentialsResponseTypeDef",
    {
        "Usernames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVoiceConnectorsRequestRequestTypeDef = TypedDict(
    "ListVoiceConnectorsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListVoiceConnectorsResponseTypeDef = TypedDict(
    "ListVoiceConnectorsResponseTypeDef",
    {
        "VoiceConnectors": List["VoiceConnectorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "EnableSIPLogs": bool,
    },
    total=False,
)

LogoutUserRequestRequestTypeDef = TypedDict(
    "LogoutUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)

MediaCapturePipelineTypeDef = TypedDict(
    "MediaCapturePipelineTypeDef",
    {
        "MediaPipelineId": str,
        "SourceType": Literal["ChimeSdkMeeting"],
        "SourceArn": str,
        "Status": MediaPipelineStatusType,
        "SinkType": Literal["S3Bucket"],
        "SinkArn": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
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
        "EventIngestionUrl": str,
    },
    total=False,
)

MeetingNotificationConfigurationTypeDef = TypedDict(
    "MeetingNotificationConfigurationTypeDef",
    {
        "SnsTopicArn": str,
        "SqsQueueArn": str,
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
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "MemberId": str,
        "MemberType": MemberTypeType,
        "Email": str,
        "FullName": str,
        "AccountId": str,
    },
    total=False,
)

MembershipItemTypeDef = TypedDict(
    "MembershipItemTypeDef",
    {
        "MemberId": str,
        "Role": RoomMembershipRoleType,
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

OrderedPhoneNumberTypeDef = TypedDict(
    "OrderedPhoneNumberTypeDef",
    {
        "E164PhoneNumber": str,
        "Status": OrderedPhoneNumberStatusType,
    },
    total=False,
)

OriginationRouteTypeDef = TypedDict(
    "OriginationRouteTypeDef",
    {
        "Host": str,
        "Port": int,
        "Protocol": OriginationRouteProtocolType,
        "Priority": int,
        "Weight": int,
    },
    total=False,
)

OriginationTypeDef = TypedDict(
    "OriginationTypeDef",
    {
        "Routes": List["OriginationRouteTypeDef"],
        "Disabled": bool,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ParticipantTypeDef = TypedDict(
    "ParticipantTypeDef",
    {
        "PhoneNumber": str,
        "ProxyPhoneNumber": str,
    },
    total=False,
)

PhoneNumberAssociationTypeDef = TypedDict(
    "PhoneNumberAssociationTypeDef",
    {
        "Value": str,
        "Name": PhoneNumberAssociationNameType,
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

PhoneNumberCountryTypeDef = TypedDict(
    "PhoneNumberCountryTypeDef",
    {
        "CountryCode": str,
        "SupportedPhoneNumberTypes": List[PhoneNumberTypeType],
    },
    total=False,
)

PhoneNumberErrorTypeDef = TypedDict(
    "PhoneNumberErrorTypeDef",
    {
        "PhoneNumberId": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

PhoneNumberOrderTypeDef = TypedDict(
    "PhoneNumberOrderTypeDef",
    {
        "PhoneNumberOrderId": str,
        "ProductType": PhoneNumberProductTypeType,
        "Status": PhoneNumberOrderStatusType,
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
        "Country": str,
        "Type": PhoneNumberTypeType,
        "ProductType": PhoneNumberProductTypeType,
        "Status": PhoneNumberStatusType,
        "Capabilities": "PhoneNumberCapabilitiesTypeDef",
        "Associations": List["PhoneNumberAssociationTypeDef"],
        "CallingName": str,
        "CallingNameStatus": CallingNameStatusType,
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
        "Status": ProxySessionStatusType,
        "ExpiryMinutes": int,
        "Capabilities": List[CapabilityType],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "EndedTimestamp": datetime,
        "Participants": List["ParticipantTypeDef"],
        "NumberSelectionBehavior": NumberSelectionBehaviorType,
        "GeoMatchLevel": GeoMatchLevelType,
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

PutAppInstanceRetentionSettingsRequestRequestTypeDef = TypedDict(
    "PutAppInstanceRetentionSettingsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceRetentionSettings": "AppInstanceRetentionSettingsTypeDef",
    },
)

PutAppInstanceRetentionSettingsResponseTypeDef = TypedDict(
    "PutAppInstanceRetentionSettingsResponseTypeDef",
    {
        "AppInstanceRetentionSettings": "AppInstanceRetentionSettingsTypeDef",
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutAppInstanceStreamingConfigurationsRequestRequestTypeDef = TypedDict(
    "PutAppInstanceStreamingConfigurationsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceStreamingConfigurations": List["AppInstanceStreamingConfigurationTypeDef"],
    },
)

PutAppInstanceStreamingConfigurationsResponseTypeDef = TypedDict(
    "PutAppInstanceStreamingConfigurationsResponseTypeDef",
    {
        "AppInstanceStreamingConfigurations": List["AppInstanceStreamingConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutEventsConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutEventsConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)
_OptionalPutEventsConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutEventsConfigurationRequestRequestTypeDef",
    {
        "OutboundEventsHTTPSEndpoint": str,
        "LambdaFunctionArn": str,
    },
    total=False,
)

class PutEventsConfigurationRequestRequestTypeDef(
    _RequiredPutEventsConfigurationRequestRequestTypeDef,
    _OptionalPutEventsConfigurationRequestRequestTypeDef,
):
    pass

PutEventsConfigurationResponseTypeDef = TypedDict(
    "PutEventsConfigurationResponseTypeDef",
    {
        "EventsConfiguration": "EventsConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRetentionSettingsRequestRequestTypeDef = TypedDict(
    "PutRetentionSettingsRequestRequestTypeDef",
    {
        "AccountId": str,
        "RetentionSettings": "RetentionSettingsTypeDef",
    },
)

PutRetentionSettingsResponseTypeDef = TypedDict(
    "PutRetentionSettingsResponseTypeDef",
    {
        "RetentionSettings": "RetentionSettingsTypeDef",
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)
_OptionalPutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationLoggingConfiguration": "SipMediaApplicationLoggingConfigurationTypeDef",
    },
    total=False,
)

class PutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef(
    _RequiredPutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef,
    _OptionalPutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef,
):
    pass

PutSipMediaApplicationLoggingConfigurationResponseTypeDef = TypedDict(
    "PutSipMediaApplicationLoggingConfigurationResponseTypeDef",
    {
        "SipMediaApplicationLoggingConfiguration": "SipMediaApplicationLoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "EmergencyCallingConfiguration": "EmergencyCallingConfigurationTypeDef",
    },
)

PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef = TypedDict(
    "PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    {
        "EmergencyCallingConfiguration": "EmergencyCallingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
    },
)

PutVoiceConnectorLoggingConfigurationResponseTypeDef = TypedDict(
    "PutVoiceConnectorLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorOriginationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorOriginationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Origination": "OriginationTypeDef",
    },
)

PutVoiceConnectorOriginationResponseTypeDef = TypedDict(
    "PutVoiceConnectorOriginationResponseTypeDef",
    {
        "Origination": "OriginationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutVoiceConnectorProxyRequestRequestTypeDef = TypedDict(
    "_RequiredPutVoiceConnectorProxyRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "DefaultSessionExpiryMinutes": int,
        "PhoneNumberPoolCountries": List[str],
    },
)
_OptionalPutVoiceConnectorProxyRequestRequestTypeDef = TypedDict(
    "_OptionalPutVoiceConnectorProxyRequestRequestTypeDef",
    {
        "FallBackPhoneNumber": str,
        "Disabled": bool,
    },
    total=False,
)

class PutVoiceConnectorProxyRequestRequestTypeDef(
    _RequiredPutVoiceConnectorProxyRequestRequestTypeDef,
    _OptionalPutVoiceConnectorProxyRequestRequestTypeDef,
):
    pass

PutVoiceConnectorProxyResponseTypeDef = TypedDict(
    "PutVoiceConnectorProxyResponseTypeDef",
    {
        "Proxy": "ProxyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "StreamingConfiguration": "StreamingConfigurationTypeDef",
    },
)

PutVoiceConnectorStreamingConfigurationResponseTypeDef = TypedDict(
    "PutVoiceConnectorStreamingConfigurationResponseTypeDef",
    {
        "StreamingConfiguration": "StreamingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutVoiceConnectorTerminationCredentialsRequestRequestTypeDef = TypedDict(
    "_RequiredPutVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
_OptionalPutVoiceConnectorTerminationCredentialsRequestRequestTypeDef = TypedDict(
    "_OptionalPutVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    {
        "Credentials": List["CredentialTypeDef"],
    },
    total=False,
)

class PutVoiceConnectorTerminationCredentialsRequestRequestTypeDef(
    _RequiredPutVoiceConnectorTerminationCredentialsRequestRequestTypeDef,
    _OptionalPutVoiceConnectorTerminationCredentialsRequestRequestTypeDef,
):
    pass

PutVoiceConnectorTerminationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorTerminationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Termination": "TerminationTypeDef",
    },
)

PutVoiceConnectorTerminationResponseTypeDef = TypedDict(
    "PutVoiceConnectorTerminationResponseTypeDef",
    {
        "Termination": "TerminationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRedactChannelMessageRequestRequestTypeDef = TypedDict(
    "_RequiredRedactChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
    },
)
_OptionalRedactChannelMessageRequestRequestTypeDef = TypedDict(
    "_OptionalRedactChannelMessageRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)

class RedactChannelMessageRequestRequestTypeDef(
    _RequiredRedactChannelMessageRequestRequestTypeDef,
    _OptionalRedactChannelMessageRequestRequestTypeDef,
):
    pass

RedactChannelMessageResponseTypeDef = TypedDict(
    "RedactChannelMessageResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RedactConversationMessageRequestRequestTypeDef = TypedDict(
    "RedactConversationMessageRequestRequestTypeDef",
    {
        "AccountId": str,
        "ConversationId": str,
        "MessageId": str,
    },
)

RedactRoomMessageRequestRequestTypeDef = TypedDict(
    "RedactRoomMessageRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MessageId": str,
    },
)

RegenerateSecurityTokenRequestRequestTypeDef = TypedDict(
    "RegenerateSecurityTokenRequestRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)

RegenerateSecurityTokenResponseTypeDef = TypedDict(
    "RegenerateSecurityTokenResponseTypeDef",
    {
        "Bot": "BotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResetPersonalPINRequestRequestTypeDef = TypedDict(
    "ResetPersonalPINRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)

ResetPersonalPINResponseTypeDef = TypedDict(
    "ResetPersonalPINResponseTypeDef",
    {
        "User": "UserTypeDef",
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

RestorePhoneNumberRequestRequestTypeDef = TypedDict(
    "RestorePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)

RestorePhoneNumberResponseTypeDef = TypedDict(
    "RestorePhoneNumberResponseTypeDef",
    {
        "PhoneNumber": "PhoneNumberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "Role": RoomMembershipRoleType,
        "InvitedBy": str,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

RoomRetentionSettingsTypeDef = TypedDict(
    "RoomRetentionSettingsTypeDef",
    {
        "RetentionDays": int,
    },
    total=False,
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

SearchAvailablePhoneNumbersRequestRequestTypeDef = TypedDict(
    "SearchAvailablePhoneNumbersRequestRequestTypeDef",
    {
        "AreaCode": str,
        "City": str,
        "Country": str,
        "State": str,
        "TollFreePrefix": str,
        "PhoneNumberType": PhoneNumberTypeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

SearchAvailablePhoneNumbersResponseTypeDef = TypedDict(
    "SearchAvailablePhoneNumbersResponseTypeDef",
    {
        "E164PhoneNumbers": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
    },
)
_OptionalSendChannelMessageRequestRequestTypeDef = TypedDict(
    "_OptionalSendChannelMessageRequestRequestTypeDef",
    {
        "Metadata": str,
        "ChimeBearer": str,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SigninDelegateGroupTypeDef = TypedDict(
    "SigninDelegateGroupTypeDef",
    {
        "GroupName": str,
    },
    total=False,
)

SipMediaApplicationCallTypeDef = TypedDict(
    "SipMediaApplicationCallTypeDef",
    {
        "TransactionId": str,
    },
    total=False,
)

SipMediaApplicationEndpointTypeDef = TypedDict(
    "SipMediaApplicationEndpointTypeDef",
    {
        "LambdaArn": str,
    },
    total=False,
)

SipMediaApplicationLoggingConfigurationTypeDef = TypedDict(
    "SipMediaApplicationLoggingConfigurationTypeDef",
    {
        "EnableSipMediaApplicationMessageLogs": bool,
    },
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
    {
        "SipMediaApplicationId": str,
        "Priority": int,
        "AwsRegion": str,
    },
    total=False,
)

SipRuleTypeDef = TypedDict(
    "SipRuleTypeDef",
    {
        "SipRuleId": str,
        "Name": str,
        "Disabled": bool,
        "TriggerType": SipRuleTriggerTypeType,
        "TriggerValue": str,
        "TargetApplications": List["SipRuleTargetApplicationTypeDef"],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

StartMeetingTranscriptionRequestRequestTypeDef = TypedDict(
    "StartMeetingTranscriptionRequestRequestTypeDef",
    {
        "MeetingId": str,
        "TranscriptionConfiguration": "TranscriptionConfigurationTypeDef",
    },
)

StopMeetingTranscriptionRequestRequestTypeDef = TypedDict(
    "StopMeetingTranscriptionRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)

_RequiredStreamingConfigurationTypeDef = TypedDict(
    "_RequiredStreamingConfigurationTypeDef",
    {
        "DataRetentionInHours": int,
    },
)
_OptionalStreamingConfigurationTypeDef = TypedDict(
    "_OptionalStreamingConfigurationTypeDef",
    {
        "Disabled": bool,
        "StreamingNotificationTargets": List["StreamingNotificationTargetTypeDef"],
    },
    total=False,
)

class StreamingConfigurationTypeDef(
    _RequiredStreamingConfigurationTypeDef, _OptionalStreamingConfigurationTypeDef
):
    pass

StreamingNotificationTargetTypeDef = TypedDict(
    "StreamingNotificationTargetTypeDef",
    {
        "NotificationTarget": NotificationTargetType,
    },
)

TagAttendeeRequestRequestTypeDef = TypedDict(
    "TagAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
        "Tags": List["TagTypeDef"],
    },
)

TagMeetingRequestRequestTypeDef = TypedDict(
    "TagMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
        "Tags": List["TagTypeDef"],
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

TelephonySettingsTypeDef = TypedDict(
    "TelephonySettingsTypeDef",
    {
        "InboundCalling": bool,
        "OutboundCalling": bool,
        "SMS": bool,
    },
)

TerminationHealthTypeDef = TypedDict(
    "TerminationHealthTypeDef",
    {
        "Timestamp": datetime,
        "Source": str,
    },
    total=False,
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

TranscriptionConfigurationTypeDef = TypedDict(
    "TranscriptionConfigurationTypeDef",
    {
        "EngineTranscribeSettings": "EngineTranscribeSettingsTypeDef",
        "EngineTranscribeMedicalSettings": "EngineTranscribeMedicalSettingsTypeDef",
    },
    total=False,
)

UntagAttendeeRequestRequestTypeDef = TypedDict(
    "UntagAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
        "TagKeys": List[str],
    },
)

UntagMeetingRequestRequestTypeDef = TypedDict(
    "UntagMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
        "TagKeys": List[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAccountRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAccountRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalUpdateAccountRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAccountRequestRequestTypeDef",
    {
        "Name": str,
        "DefaultLicense": LicenseType,
    },
    total=False,
)

class UpdateAccountRequestRequestTypeDef(
    _RequiredUpdateAccountRequestRequestTypeDef, _OptionalUpdateAccountRequestRequestTypeDef
):
    pass

UpdateAccountResponseTypeDef = TypedDict(
    "UpdateAccountResponseTypeDef",
    {
        "Account": "AccountTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAccountSettingsRequestRequestTypeDef = TypedDict(
    "UpdateAccountSettingsRequestRequestTypeDef",
    {
        "AccountId": str,
        "AccountSettings": "AccountSettingsTypeDef",
    },
)

_RequiredUpdateAppInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
    },
)
_OptionalUpdateAppInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAppInstanceRequestRequestTypeDef",
    {
        "Metadata": str,
    },
    total=False,
)

class UpdateAppInstanceRequestRequestTypeDef(
    _RequiredUpdateAppInstanceRequestRequestTypeDef, _OptionalUpdateAppInstanceRequestRequestTypeDef
):
    pass

UpdateAppInstanceResponseTypeDef = TypedDict(
    "UpdateAppInstanceResponseTypeDef",
    {
        "AppInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "Name": str,
    },
)
_OptionalUpdateAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAppInstanceUserRequestRequestTypeDef",
    {
        "Metadata": str,
    },
    total=False,
)

class UpdateAppInstanceUserRequestRequestTypeDef(
    _RequiredUpdateAppInstanceUserRequestRequestTypeDef,
    _OptionalUpdateAppInstanceUserRequestRequestTypeDef,
):
    pass

UpdateAppInstanceUserResponseTypeDef = TypedDict(
    "UpdateAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateBotRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBotRequestRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)
_OptionalUpdateBotRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBotRequestRequestTypeDef",
    {
        "Disabled": bool,
    },
    total=False,
)

class UpdateBotRequestRequestTypeDef(
    _RequiredUpdateBotRequestRequestTypeDef, _OptionalUpdateBotRequestRequestTypeDef
):
    pass

UpdateBotResponseTypeDef = TypedDict(
    "UpdateBotResponseTypeDef",
    {
        "Bot": "BotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateChannelMessageRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
    },
)
_OptionalUpdateChannelMessageRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelMessageRequestRequestTypeDef",
    {
        "Content": str,
        "Metadata": str,
        "ChimeBearer": str,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateChannelReadMarkerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelReadMarkerRequestRequestTypeDef",
    {
        "ChannelArn": str,
    },
)
_OptionalUpdateChannelReadMarkerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelReadMarkerRequestRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)

class UpdateChannelReadMarkerRequestRequestTypeDef(
    _RequiredUpdateChannelReadMarkerRequestRequestTypeDef,
    _OptionalUpdateChannelReadMarkerRequestRequestTypeDef,
):
    pass

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
        "Name": str,
        "Mode": ChannelModeType,
    },
)
_OptionalUpdateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelRequestRequestTypeDef",
    {
        "Metadata": str,
        "ChimeBearer": str,
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

UpdateGlobalSettingsRequestRequestTypeDef = TypedDict(
    "UpdateGlobalSettingsRequestRequestTypeDef",
    {
        "BusinessCalling": "BusinessCallingSettingsTypeDef",
        "VoiceConnector": "VoiceConnectorSettingsTypeDef",
    },
)

_RequiredUpdatePhoneNumberRequestItemTypeDef = TypedDict(
    "_RequiredUpdatePhoneNumberRequestItemTypeDef",
    {
        "PhoneNumberId": str,
    },
)
_OptionalUpdatePhoneNumberRequestItemTypeDef = TypedDict(
    "_OptionalUpdatePhoneNumberRequestItemTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
        "CallingName": str,
    },
    total=False,
)

class UpdatePhoneNumberRequestItemTypeDef(
    _RequiredUpdatePhoneNumberRequestItemTypeDef, _OptionalUpdatePhoneNumberRequestItemTypeDef
):
    pass

_RequiredUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)
_OptionalUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePhoneNumberRequestRequestTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
        "CallingName": str,
    },
    total=False,
)

class UpdatePhoneNumberRequestRequestTypeDef(
    _RequiredUpdatePhoneNumberRequestRequestTypeDef, _OptionalUpdatePhoneNumberRequestRequestTypeDef
):
    pass

UpdatePhoneNumberResponseTypeDef = TypedDict(
    "UpdatePhoneNumberResponseTypeDef",
    {
        "PhoneNumber": "PhoneNumberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePhoneNumberSettingsRequestRequestTypeDef = TypedDict(
    "UpdatePhoneNumberSettingsRequestRequestTypeDef",
    {
        "CallingName": str,
    },
)

_RequiredUpdateProxySessionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
        "Capabilities": List[CapabilityType],
    },
)
_OptionalUpdateProxySessionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProxySessionRequestRequestTypeDef",
    {
        "ExpiryMinutes": int,
    },
    total=False,
)

class UpdateProxySessionRequestRequestTypeDef(
    _RequiredUpdateProxySessionRequestRequestTypeDef,
    _OptionalUpdateProxySessionRequestRequestTypeDef,
):
    pass

UpdateProxySessionResponseTypeDef = TypedDict(
    "UpdateProxySessionResponseTypeDef",
    {
        "ProxySession": "ProxySessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRoomMembershipRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRoomMembershipRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MemberId": str,
    },
)
_OptionalUpdateRoomMembershipRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRoomMembershipRequestRequestTypeDef",
    {
        "Role": RoomMembershipRoleType,
    },
    total=False,
)

class UpdateRoomMembershipRequestRequestTypeDef(
    _RequiredUpdateRoomMembershipRequestRequestTypeDef,
    _OptionalUpdateRoomMembershipRequestRequestTypeDef,
):
    pass

UpdateRoomMembershipResponseTypeDef = TypedDict(
    "UpdateRoomMembershipResponseTypeDef",
    {
        "RoomMembership": "RoomMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRoomRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRoomRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
    },
)
_OptionalUpdateRoomRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRoomRequestRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class UpdateRoomRequestRequestTypeDef(
    _RequiredUpdateRoomRequestRequestTypeDef, _OptionalUpdateRoomRequestRequestTypeDef
):
    pass

UpdateRoomResponseTypeDef = TypedDict(
    "UpdateRoomResponseTypeDef",
    {
        "Room": "RoomTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSipMediaApplicationCallRequestRequestTypeDef = TypedDict(
    "UpdateSipMediaApplicationCallRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
        "TransactionId": str,
        "Arguments": Dict[str, str],
    },
)

UpdateSipMediaApplicationCallResponseTypeDef = TypedDict(
    "UpdateSipMediaApplicationCallResponseTypeDef",
    {
        "SipMediaApplicationCall": "SipMediaApplicationCallTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSipMediaApplicationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)
_OptionalUpdateSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSipMediaApplicationRequestRequestTypeDef",
    {
        "Name": str,
        "Endpoints": List["SipMediaApplicationEndpointTypeDef"],
    },
    total=False,
)

class UpdateSipMediaApplicationRequestRequestTypeDef(
    _RequiredUpdateSipMediaApplicationRequestRequestTypeDef,
    _OptionalUpdateSipMediaApplicationRequestRequestTypeDef,
):
    pass

UpdateSipMediaApplicationResponseTypeDef = TypedDict(
    "UpdateSipMediaApplicationResponseTypeDef",
    {
        "SipMediaApplication": "SipMediaApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSipRuleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSipRuleRequestRequestTypeDef",
    {
        "SipRuleId": str,
        "Name": str,
    },
)
_OptionalUpdateSipRuleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSipRuleRequestRequestTypeDef",
    {
        "Disabled": bool,
        "TargetApplications": List["SipRuleTargetApplicationTypeDef"],
    },
    total=False,
)

class UpdateSipRuleRequestRequestTypeDef(
    _RequiredUpdateSipRuleRequestRequestTypeDef, _OptionalUpdateSipRuleRequestRequestTypeDef
):
    pass

UpdateSipRuleResponseTypeDef = TypedDict(
    "UpdateSipRuleResponseTypeDef",
    {
        "SipRule": "SipRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserRequestItemTypeDef = TypedDict(
    "_RequiredUpdateUserRequestItemTypeDef",
    {
        "UserId": str,
    },
)
_OptionalUpdateUserRequestItemTypeDef = TypedDict(
    "_OptionalUpdateUserRequestItemTypeDef",
    {
        "LicenseType": LicenseType,
        "UserType": UserTypeType,
        "AlexaForBusinessMetadata": "AlexaForBusinessMetadataTypeDef",
    },
    total=False,
)

class UpdateUserRequestItemTypeDef(
    _RequiredUpdateUserRequestItemTypeDef, _OptionalUpdateUserRequestItemTypeDef
):
    pass

_RequiredUpdateUserRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)
_OptionalUpdateUserRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserRequestRequestTypeDef",
    {
        "LicenseType": LicenseType,
        "UserType": UserTypeType,
        "AlexaForBusinessMetadata": "AlexaForBusinessMetadataTypeDef",
    },
    total=False,
)

class UpdateUserRequestRequestTypeDef(
    _RequiredUpdateUserRequestRequestTypeDef, _OptionalUpdateUserRequestRequestTypeDef
):
    pass

UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserSettingsRequestRequestTypeDef = TypedDict(
    "UpdateUserSettingsRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
        "UserSettings": "UserSettingsTypeDef",
    },
)

UpdateVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "UpdateVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": List["VoiceConnectorItemTypeDef"],
    },
)

UpdateVoiceConnectorGroupResponseTypeDef = TypedDict(
    "UpdateVoiceConnectorGroupResponseTypeDef",
    {
        "VoiceConnectorGroup": "VoiceConnectorGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVoiceConnectorRequestRequestTypeDef = TypedDict(
    "UpdateVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Name": str,
        "RequireEncryption": bool,
    },
)

UpdateVoiceConnectorResponseTypeDef = TypedDict(
    "UpdateVoiceConnectorResponseTypeDef",
    {
        "VoiceConnector": "VoiceConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserErrorTypeDef = TypedDict(
    "UserErrorTypeDef",
    {
        "UserId": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

UserSettingsTypeDef = TypedDict(
    "UserSettingsTypeDef",
    {
        "Telephony": "TelephonySettingsTypeDef",
    },
)

_RequiredUserTypeDef = TypedDict(
    "_RequiredUserTypeDef",
    {
        "UserId": str,
    },
)
_OptionalUserTypeDef = TypedDict(
    "_OptionalUserTypeDef",
    {
        "AccountId": str,
        "PrimaryEmail": str,
        "PrimaryProvisionedNumber": str,
        "DisplayName": str,
        "LicenseType": LicenseType,
        "UserType": UserTypeType,
        "UserRegistrationStatus": RegistrationStatusType,
        "UserInvitationStatus": InviteStatusType,
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
    "VoiceConnectorItemTypeDef",
    {
        "VoiceConnectorId": str,
        "Priority": int,
    },
)

VoiceConnectorSettingsTypeDef = TypedDict(
    "VoiceConnectorSettingsTypeDef",
    {
        "CdrBucket": str,
    },
    total=False,
)

VoiceConnectorTypeDef = TypedDict(
    "VoiceConnectorTypeDef",
    {
        "VoiceConnectorId": str,
        "AwsRegion": VoiceConnectorAwsRegionType,
        "Name": str,
        "OutboundHostName": str,
        "RequireEncryption": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)
