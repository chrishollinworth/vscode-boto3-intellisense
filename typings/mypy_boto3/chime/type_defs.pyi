"""
Type annotations for chime service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_chime.type_defs import AccountSettingsTypeDef

    data: AccountSettingsTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    AccountStatusType,
    AccountTypeType,
    CallingNameStatusType,
    EmailStatusType,
    ErrorCodeType,
    InviteStatusType,
    LicenseType,
    MemberTypeType,
    OrderedPhoneNumberStatusType,
    PhoneNumberAssociationNameType,
    PhoneNumberOrderStatusType,
    PhoneNumberProductTypeType,
    PhoneNumberStatusType,
    PhoneNumberTypeType,
    RegistrationStatusType,
    RoomMembershipRoleType,
    UserTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccountSettingsTypeDef",
    "AccountTypeDef",
    "AlexaForBusinessMetadataTypeDef",
    "AssociatePhoneNumberWithUserRequestTypeDef",
    "AssociateSigninDelegateGroupsWithAccountRequestTypeDef",
    "BatchCreateRoomMembershipRequestTypeDef",
    "BatchCreateRoomMembershipResponseTypeDef",
    "BatchDeletePhoneNumberRequestTypeDef",
    "BatchDeletePhoneNumberResponseTypeDef",
    "BatchSuspendUserRequestTypeDef",
    "BatchSuspendUserResponseTypeDef",
    "BatchUnsuspendUserRequestTypeDef",
    "BatchUnsuspendUserResponseTypeDef",
    "BatchUpdatePhoneNumberRequestTypeDef",
    "BatchUpdatePhoneNumberResponseTypeDef",
    "BatchUpdateUserRequestTypeDef",
    "BatchUpdateUserResponseTypeDef",
    "BotTypeDef",
    "BusinessCallingSettingsTypeDef",
    "ConversationRetentionSettingsTypeDef",
    "CreateAccountRequestTypeDef",
    "CreateAccountResponseTypeDef",
    "CreateBotRequestTypeDef",
    "CreateBotResponseTypeDef",
    "CreateMeetingDialOutRequestTypeDef",
    "CreateMeetingDialOutResponseTypeDef",
    "CreatePhoneNumberOrderRequestTypeDef",
    "CreatePhoneNumberOrderResponseTypeDef",
    "CreateRoomMembershipRequestTypeDef",
    "CreateRoomMembershipResponseTypeDef",
    "CreateRoomRequestTypeDef",
    "CreateRoomResponseTypeDef",
    "CreateUserRequestTypeDef",
    "CreateUserResponseTypeDef",
    "DeleteAccountRequestTypeDef",
    "DeleteEventsConfigurationRequestTypeDef",
    "DeletePhoneNumberRequestTypeDef",
    "DeleteRoomMembershipRequestTypeDef",
    "DeleteRoomRequestTypeDef",
    "DisassociatePhoneNumberFromUserRequestTypeDef",
    "DisassociateSigninDelegateGroupsFromAccountRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EventsConfigurationTypeDef",
    "GetAccountRequestTypeDef",
    "GetAccountResponseTypeDef",
    "GetAccountSettingsRequestTypeDef",
    "GetAccountSettingsResponseTypeDef",
    "GetBotRequestTypeDef",
    "GetBotResponseTypeDef",
    "GetEventsConfigurationRequestTypeDef",
    "GetEventsConfigurationResponseTypeDef",
    "GetGlobalSettingsResponseTypeDef",
    "GetPhoneNumberOrderRequestTypeDef",
    "GetPhoneNumberOrderResponseTypeDef",
    "GetPhoneNumberRequestTypeDef",
    "GetPhoneNumberResponseTypeDef",
    "GetPhoneNumberSettingsResponseTypeDef",
    "GetRetentionSettingsRequestTypeDef",
    "GetRetentionSettingsResponseTypeDef",
    "GetRoomRequestTypeDef",
    "GetRoomResponseTypeDef",
    "GetUserRequestTypeDef",
    "GetUserResponseTypeDef",
    "GetUserSettingsRequestTypeDef",
    "GetUserSettingsResponseTypeDef",
    "InviteTypeDef",
    "InviteUsersRequestTypeDef",
    "InviteUsersResponseTypeDef",
    "ListAccountsRequestPaginateTypeDef",
    "ListAccountsRequestTypeDef",
    "ListAccountsResponseTypeDef",
    "ListBotsRequestTypeDef",
    "ListBotsResponseTypeDef",
    "ListPhoneNumberOrdersRequestTypeDef",
    "ListPhoneNumberOrdersResponseTypeDef",
    "ListPhoneNumbersRequestTypeDef",
    "ListPhoneNumbersResponseTypeDef",
    "ListRoomMembershipsRequestTypeDef",
    "ListRoomMembershipsResponseTypeDef",
    "ListRoomsRequestTypeDef",
    "ListRoomsResponseTypeDef",
    "ListSupportedPhoneNumberCountriesRequestTypeDef",
    "ListSupportedPhoneNumberCountriesResponseTypeDef",
    "ListUsersRequestPaginateTypeDef",
    "ListUsersRequestTypeDef",
    "ListUsersResponseTypeDef",
    "LogoutUserRequestTypeDef",
    "MemberErrorTypeDef",
    "MemberTypeDef",
    "MembershipItemTypeDef",
    "OrderedPhoneNumberTypeDef",
    "PaginatorConfigTypeDef",
    "PhoneNumberAssociationTypeDef",
    "PhoneNumberCapabilitiesTypeDef",
    "PhoneNumberCountryTypeDef",
    "PhoneNumberErrorTypeDef",
    "PhoneNumberOrderTypeDef",
    "PhoneNumberTypeDef",
    "PutEventsConfigurationRequestTypeDef",
    "PutEventsConfigurationResponseTypeDef",
    "PutRetentionSettingsRequestTypeDef",
    "PutRetentionSettingsResponseTypeDef",
    "RedactConversationMessageRequestTypeDef",
    "RedactRoomMessageRequestTypeDef",
    "RegenerateSecurityTokenRequestTypeDef",
    "RegenerateSecurityTokenResponseTypeDef",
    "ResetPersonalPINRequestTypeDef",
    "ResetPersonalPINResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RestorePhoneNumberRequestTypeDef",
    "RestorePhoneNumberResponseTypeDef",
    "RetentionSettingsTypeDef",
    "RoomMembershipTypeDef",
    "RoomRetentionSettingsTypeDef",
    "RoomTypeDef",
    "SearchAvailablePhoneNumbersRequestTypeDef",
    "SearchAvailablePhoneNumbersResponseTypeDef",
    "SigninDelegateGroupTypeDef",
    "TelephonySettingsTypeDef",
    "UpdateAccountRequestTypeDef",
    "UpdateAccountResponseTypeDef",
    "UpdateAccountSettingsRequestTypeDef",
    "UpdateBotRequestTypeDef",
    "UpdateBotResponseTypeDef",
    "UpdateGlobalSettingsRequestTypeDef",
    "UpdatePhoneNumberRequestItemTypeDef",
    "UpdatePhoneNumberRequestTypeDef",
    "UpdatePhoneNumberResponseTypeDef",
    "UpdatePhoneNumberSettingsRequestTypeDef",
    "UpdateRoomMembershipRequestTypeDef",
    "UpdateRoomMembershipResponseTypeDef",
    "UpdateRoomRequestTypeDef",
    "UpdateRoomResponseTypeDef",
    "UpdateUserRequestItemTypeDef",
    "UpdateUserRequestTypeDef",
    "UpdateUserResponseTypeDef",
    "UpdateUserSettingsRequestTypeDef",
    "UserErrorTypeDef",
    "UserSettingsTypeDef",
    "UserTypeDef",
    "VoiceConnectorSettingsTypeDef",
)

class AccountSettingsTypeDef(TypedDict):
    DisableRemoteControl: NotRequired[bool]
    EnableDialOut: NotRequired[bool]

class SigninDelegateGroupTypeDef(TypedDict):
    GroupName: NotRequired[str]

class AlexaForBusinessMetadataTypeDef(TypedDict):
    IsAlexaForBusinessEnabled: NotRequired[bool]
    AlexaForBusinessRoomArn: NotRequired[str]

class AssociatePhoneNumberWithUserRequestTypeDef(TypedDict):
    AccountId: str
    UserId: str
    E164PhoneNumber: str

class MembershipItemTypeDef(TypedDict):
    MemberId: NotRequired[str]
    Role: NotRequired[RoomMembershipRoleType]

class MemberErrorTypeDef(TypedDict):
    MemberId: NotRequired[str]
    ErrorCode: NotRequired[ErrorCodeType]
    ErrorMessage: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BatchDeletePhoneNumberRequestTypeDef(TypedDict):
    PhoneNumberIds: Sequence[str]

class PhoneNumberErrorTypeDef(TypedDict):
    PhoneNumberId: NotRequired[str]
    ErrorCode: NotRequired[ErrorCodeType]
    ErrorMessage: NotRequired[str]

class BatchSuspendUserRequestTypeDef(TypedDict):
    AccountId: str
    UserIdList: Sequence[str]

class UserErrorTypeDef(TypedDict):
    UserId: NotRequired[str]
    ErrorCode: NotRequired[ErrorCodeType]
    ErrorMessage: NotRequired[str]

class BatchUnsuspendUserRequestTypeDef(TypedDict):
    AccountId: str
    UserIdList: Sequence[str]

class UpdatePhoneNumberRequestItemTypeDef(TypedDict):
    PhoneNumberId: str
    ProductType: NotRequired[PhoneNumberProductTypeType]
    CallingName: NotRequired[str]

class BotTypeDef(TypedDict):
    BotId: NotRequired[str]
    UserId: NotRequired[str]
    DisplayName: NotRequired[str]
    BotType: NotRequired[Literal["ChatBot"]]
    Disabled: NotRequired[bool]
    CreatedTimestamp: NotRequired[datetime]
    UpdatedTimestamp: NotRequired[datetime]
    BotEmail: NotRequired[str]
    SecurityToken: NotRequired[str]

class BusinessCallingSettingsTypeDef(TypedDict):
    CdrBucket: NotRequired[str]

class ConversationRetentionSettingsTypeDef(TypedDict):
    RetentionDays: NotRequired[int]

class CreateAccountRequestTypeDef(TypedDict):
    Name: str

class CreateBotRequestTypeDef(TypedDict):
    AccountId: str
    DisplayName: str
    Domain: NotRequired[str]

class CreateMeetingDialOutRequestTypeDef(TypedDict):
    MeetingId: str
    FromPhoneNumber: str
    ToPhoneNumber: str
    JoinToken: str

class CreatePhoneNumberOrderRequestTypeDef(TypedDict):
    ProductType: PhoneNumberProductTypeType
    E164PhoneNumbers: Sequence[str]

class CreateRoomMembershipRequestTypeDef(TypedDict):
    AccountId: str
    RoomId: str
    MemberId: str
    Role: NotRequired[RoomMembershipRoleType]

class CreateRoomRequestTypeDef(TypedDict):
    AccountId: str
    Name: str
    ClientRequestToken: NotRequired[str]

class RoomTypeDef(TypedDict):
    RoomId: NotRequired[str]
    Name: NotRequired[str]
    AccountId: NotRequired[str]
    CreatedBy: NotRequired[str]
    CreatedTimestamp: NotRequired[datetime]
    UpdatedTimestamp: NotRequired[datetime]

class CreateUserRequestTypeDef(TypedDict):
    AccountId: str
    Username: NotRequired[str]
    Email: NotRequired[str]
    UserType: NotRequired[UserTypeType]

class DeleteAccountRequestTypeDef(TypedDict):
    AccountId: str

class DeleteEventsConfigurationRequestTypeDef(TypedDict):
    AccountId: str
    BotId: str

class DeletePhoneNumberRequestTypeDef(TypedDict):
    PhoneNumberId: str

class DeleteRoomMembershipRequestTypeDef(TypedDict):
    AccountId: str
    RoomId: str
    MemberId: str

class DeleteRoomRequestTypeDef(TypedDict):
    AccountId: str
    RoomId: str

class DisassociatePhoneNumberFromUserRequestTypeDef(TypedDict):
    AccountId: str
    UserId: str

class DisassociateSigninDelegateGroupsFromAccountRequestTypeDef(TypedDict):
    AccountId: str
    GroupNames: Sequence[str]

class EventsConfigurationTypeDef(TypedDict):
    BotId: NotRequired[str]
    OutboundEventsHTTPSEndpoint: NotRequired[str]
    LambdaFunctionArn: NotRequired[str]

class GetAccountRequestTypeDef(TypedDict):
    AccountId: str

class GetAccountSettingsRequestTypeDef(TypedDict):
    AccountId: str

class GetBotRequestTypeDef(TypedDict):
    AccountId: str
    BotId: str

class GetEventsConfigurationRequestTypeDef(TypedDict):
    AccountId: str
    BotId: str

class VoiceConnectorSettingsTypeDef(TypedDict):
    CdrBucket: NotRequired[str]

class GetPhoneNumberOrderRequestTypeDef(TypedDict):
    PhoneNumberOrderId: str

class GetPhoneNumberRequestTypeDef(TypedDict):
    PhoneNumberId: str

class GetRetentionSettingsRequestTypeDef(TypedDict):
    AccountId: str

class GetRoomRequestTypeDef(TypedDict):
    AccountId: str
    RoomId: str

class GetUserRequestTypeDef(TypedDict):
    AccountId: str
    UserId: str

class GetUserSettingsRequestTypeDef(TypedDict):
    AccountId: str
    UserId: str

class InviteTypeDef(TypedDict):
    InviteId: NotRequired[str]
    Status: NotRequired[InviteStatusType]
    EmailAddress: NotRequired[str]
    EmailStatus: NotRequired[EmailStatusType]

class InviteUsersRequestTypeDef(TypedDict):
    AccountId: str
    UserEmailList: Sequence[str]
    UserType: NotRequired[UserTypeType]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAccountsRequestTypeDef(TypedDict):
    Name: NotRequired[str]
    UserEmail: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListBotsRequestTypeDef(TypedDict):
    AccountId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListPhoneNumberOrdersRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListPhoneNumbersRequestTypeDef(TypedDict):
    Status: NotRequired[PhoneNumberStatusType]
    ProductType: NotRequired[PhoneNumberProductTypeType]
    FilterName: NotRequired[PhoneNumberAssociationNameType]
    FilterValue: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListRoomMembershipsRequestTypeDef(TypedDict):
    AccountId: str
    RoomId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListRoomsRequestTypeDef(TypedDict):
    AccountId: str
    MemberId: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListSupportedPhoneNumberCountriesRequestTypeDef(TypedDict):
    ProductType: PhoneNumberProductTypeType

class PhoneNumberCountryTypeDef(TypedDict):
    CountryCode: NotRequired[str]
    SupportedPhoneNumberTypes: NotRequired[List[PhoneNumberTypeType]]

class ListUsersRequestTypeDef(TypedDict):
    AccountId: str
    UserEmail: NotRequired[str]
    UserType: NotRequired[UserTypeType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class LogoutUserRequestTypeDef(TypedDict):
    AccountId: str
    UserId: str

class MemberTypeDef(TypedDict):
    MemberId: NotRequired[str]
    MemberType: NotRequired[MemberTypeType]
    Email: NotRequired[str]
    FullName: NotRequired[str]
    AccountId: NotRequired[str]

class OrderedPhoneNumberTypeDef(TypedDict):
    E164PhoneNumber: NotRequired[str]
    Status: NotRequired[OrderedPhoneNumberStatusType]

class PhoneNumberAssociationTypeDef(TypedDict):
    Value: NotRequired[str]
    Name: NotRequired[PhoneNumberAssociationNameType]
    AssociatedTimestamp: NotRequired[datetime]

class PhoneNumberCapabilitiesTypeDef(TypedDict):
    InboundCall: NotRequired[bool]
    OutboundCall: NotRequired[bool]
    InboundSMS: NotRequired[bool]
    OutboundSMS: NotRequired[bool]
    InboundMMS: NotRequired[bool]
    OutboundMMS: NotRequired[bool]

class PutEventsConfigurationRequestTypeDef(TypedDict):
    AccountId: str
    BotId: str
    OutboundEventsHTTPSEndpoint: NotRequired[str]
    LambdaFunctionArn: NotRequired[str]

class RedactConversationMessageRequestTypeDef(TypedDict):
    AccountId: str
    ConversationId: str
    MessageId: str

class RedactRoomMessageRequestTypeDef(TypedDict):
    AccountId: str
    RoomId: str
    MessageId: str

class RegenerateSecurityTokenRequestTypeDef(TypedDict):
    AccountId: str
    BotId: str

class ResetPersonalPINRequestTypeDef(TypedDict):
    AccountId: str
    UserId: str

class RestorePhoneNumberRequestTypeDef(TypedDict):
    PhoneNumberId: str

class RoomRetentionSettingsTypeDef(TypedDict):
    RetentionDays: NotRequired[int]

class SearchAvailablePhoneNumbersRequestTypeDef(TypedDict):
    AreaCode: NotRequired[str]
    City: NotRequired[str]
    Country: NotRequired[str]
    State: NotRequired[str]
    TollFreePrefix: NotRequired[str]
    PhoneNumberType: NotRequired[PhoneNumberTypeType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class TelephonySettingsTypeDef(TypedDict):
    InboundCalling: bool
    OutboundCalling: bool
    SMS: bool

class UpdateAccountRequestTypeDef(TypedDict):
    AccountId: str
    Name: NotRequired[str]
    DefaultLicense: NotRequired[LicenseType]

class UpdateBotRequestTypeDef(TypedDict):
    AccountId: str
    BotId: str
    Disabled: NotRequired[bool]

class UpdatePhoneNumberRequestTypeDef(TypedDict):
    PhoneNumberId: str
    ProductType: NotRequired[PhoneNumberProductTypeType]
    CallingName: NotRequired[str]

class UpdatePhoneNumberSettingsRequestTypeDef(TypedDict):
    CallingName: str

class UpdateRoomMembershipRequestTypeDef(TypedDict):
    AccountId: str
    RoomId: str
    MemberId: str
    Role: NotRequired[RoomMembershipRoleType]

class UpdateRoomRequestTypeDef(TypedDict):
    AccountId: str
    RoomId: str
    Name: NotRequired[str]

class UpdateAccountSettingsRequestTypeDef(TypedDict):
    AccountId: str
    AccountSettings: AccountSettingsTypeDef

class AccountTypeDef(TypedDict):
    AwsAccountId: str
    AccountId: str
    Name: str
    AccountType: NotRequired[AccountTypeType]
    CreatedTimestamp: NotRequired[datetime]
    DefaultLicense: NotRequired[LicenseType]
    SupportedLicenses: NotRequired[List[LicenseType]]
    AccountStatus: NotRequired[AccountStatusType]
    SigninDelegateGroups: NotRequired[List[SigninDelegateGroupTypeDef]]

class AssociateSigninDelegateGroupsWithAccountRequestTypeDef(TypedDict):
    AccountId: str
    SigninDelegateGroups: Sequence[SigninDelegateGroupTypeDef]

UpdateUserRequestItemTypeDef = TypedDict(
    "UpdateUserRequestItemTypeDef",
    {
        "UserId": str,
        "LicenseType": NotRequired[LicenseType],
        "UserType": NotRequired[UserTypeType],
        "AlexaForBusinessMetadata": NotRequired[AlexaForBusinessMetadataTypeDef],
    },
)
UpdateUserRequestTypeDef = TypedDict(
    "UpdateUserRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
        "LicenseType": NotRequired[LicenseType],
        "UserType": NotRequired[UserTypeType],
        "AlexaForBusinessMetadata": NotRequired[AlexaForBusinessMetadataTypeDef],
    },
)
UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "UserId": str,
        "AccountId": NotRequired[str],
        "PrimaryEmail": NotRequired[str],
        "PrimaryProvisionedNumber": NotRequired[str],
        "DisplayName": NotRequired[str],
        "LicenseType": NotRequired[LicenseType],
        "UserType": NotRequired[UserTypeType],
        "UserRegistrationStatus": NotRequired[RegistrationStatusType],
        "UserInvitationStatus": NotRequired[InviteStatusType],
        "RegisteredOn": NotRequired[datetime],
        "InvitedOn": NotRequired[datetime],
        "AlexaForBusinessMetadata": NotRequired[AlexaForBusinessMetadataTypeDef],
        "PersonalPIN": NotRequired[str],
    },
)

class BatchCreateRoomMembershipRequestTypeDef(TypedDict):
    AccountId: str
    RoomId: str
    MembershipItemList: Sequence[MembershipItemTypeDef]

class BatchCreateRoomMembershipResponseTypeDef(TypedDict):
    Errors: List[MemberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMeetingDialOutResponseTypeDef(TypedDict):
    TransactionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountSettingsResponseTypeDef(TypedDict):
    AccountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPhoneNumberSettingsResponseTypeDef(TypedDict):
    CallingName: str
    CallingNameUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class SearchAvailablePhoneNumbersResponseTypeDef(TypedDict):
    E164PhoneNumbers: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BatchDeletePhoneNumberResponseTypeDef(TypedDict):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdatePhoneNumberResponseTypeDef(TypedDict):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchSuspendUserResponseTypeDef(TypedDict):
    UserErrors: List[UserErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUnsuspendUserResponseTypeDef(TypedDict):
    UserErrors: List[UserErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateUserResponseTypeDef(TypedDict):
    UserErrors: List[UserErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdatePhoneNumberRequestTypeDef(TypedDict):
    UpdatePhoneNumberRequestItems: Sequence[UpdatePhoneNumberRequestItemTypeDef]

class CreateBotResponseTypeDef(TypedDict):
    Bot: BotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBotResponseTypeDef(TypedDict):
    Bot: BotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListBotsResponseTypeDef(TypedDict):
    Bots: List[BotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RegenerateSecurityTokenResponseTypeDef(TypedDict):
    Bot: BotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBotResponseTypeDef(TypedDict):
    Bot: BotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRoomResponseTypeDef(TypedDict):
    Room: RoomTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRoomResponseTypeDef(TypedDict):
    Room: RoomTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRoomsResponseTypeDef(TypedDict):
    Rooms: List[RoomTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateRoomResponseTypeDef(TypedDict):
    Room: RoomTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEventsConfigurationResponseTypeDef(TypedDict):
    EventsConfiguration: EventsConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutEventsConfigurationResponseTypeDef(TypedDict):
    EventsConfiguration: EventsConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGlobalSettingsResponseTypeDef(TypedDict):
    BusinessCalling: BusinessCallingSettingsTypeDef
    VoiceConnector: VoiceConnectorSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGlobalSettingsRequestTypeDef(TypedDict):
    BusinessCalling: NotRequired[BusinessCallingSettingsTypeDef]
    VoiceConnector: NotRequired[VoiceConnectorSettingsTypeDef]

class InviteUsersResponseTypeDef(TypedDict):
    Invites: List[InviteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountsRequestPaginateTypeDef(TypedDict):
    Name: NotRequired[str]
    UserEmail: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUsersRequestPaginateTypeDef(TypedDict):
    AccountId: str
    UserEmail: NotRequired[str]
    UserType: NotRequired[UserTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSupportedPhoneNumberCountriesResponseTypeDef(TypedDict):
    PhoneNumberCountries: List[PhoneNumberCountryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RoomMembershipTypeDef(TypedDict):
    RoomId: NotRequired[str]
    Member: NotRequired[MemberTypeDef]
    Role: NotRequired[RoomMembershipRoleType]
    InvitedBy: NotRequired[str]
    UpdatedTimestamp: NotRequired[datetime]

class PhoneNumberOrderTypeDef(TypedDict):
    PhoneNumberOrderId: NotRequired[str]
    ProductType: NotRequired[PhoneNumberProductTypeType]
    Status: NotRequired[PhoneNumberOrderStatusType]
    OrderedPhoneNumbers: NotRequired[List[OrderedPhoneNumberTypeDef]]
    CreatedTimestamp: NotRequired[datetime]
    UpdatedTimestamp: NotRequired[datetime]

PhoneNumberTypeDef = TypedDict(
    "PhoneNumberTypeDef",
    {
        "PhoneNumberId": NotRequired[str],
        "E164PhoneNumber": NotRequired[str],
        "Country": NotRequired[str],
        "Type": NotRequired[PhoneNumberTypeType],
        "ProductType": NotRequired[PhoneNumberProductTypeType],
        "Status": NotRequired[PhoneNumberStatusType],
        "Capabilities": NotRequired[PhoneNumberCapabilitiesTypeDef],
        "Associations": NotRequired[List[PhoneNumberAssociationTypeDef]],
        "CallingName": NotRequired[str],
        "CallingNameStatus": NotRequired[CallingNameStatusType],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "DeletionTimestamp": NotRequired[datetime],
    },
)

class RetentionSettingsTypeDef(TypedDict):
    RoomRetentionSettings: NotRequired[RoomRetentionSettingsTypeDef]
    ConversationRetentionSettings: NotRequired[ConversationRetentionSettingsTypeDef]

class UserSettingsTypeDef(TypedDict):
    Telephony: TelephonySettingsTypeDef

class CreateAccountResponseTypeDef(TypedDict):
    Account: AccountTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountResponseTypeDef(TypedDict):
    Account: AccountTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountsResponseTypeDef(TypedDict):
    Accounts: List[AccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateAccountResponseTypeDef(TypedDict):
    Account: AccountTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateUserRequestTypeDef(TypedDict):
    AccountId: str
    UpdateUserRequestItems: Sequence[UpdateUserRequestItemTypeDef]

class CreateUserResponseTypeDef(TypedDict):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserResponseTypeDef(TypedDict):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUsersResponseTypeDef(TypedDict):
    Users: List[UserTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ResetPersonalPINResponseTypeDef(TypedDict):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserResponseTypeDef(TypedDict):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRoomMembershipResponseTypeDef(TypedDict):
    RoomMembership: RoomMembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRoomMembershipsResponseTypeDef(TypedDict):
    RoomMemberships: List[RoomMembershipTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateRoomMembershipResponseTypeDef(TypedDict):
    RoomMembership: RoomMembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePhoneNumberOrderResponseTypeDef(TypedDict):
    PhoneNumberOrder: PhoneNumberOrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPhoneNumberOrderResponseTypeDef(TypedDict):
    PhoneNumberOrder: PhoneNumberOrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPhoneNumberOrdersResponseTypeDef(TypedDict):
    PhoneNumberOrders: List[PhoneNumberOrderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetPhoneNumberResponseTypeDef(TypedDict):
    PhoneNumber: PhoneNumberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPhoneNumbersResponseTypeDef(TypedDict):
    PhoneNumbers: List[PhoneNumberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RestorePhoneNumberResponseTypeDef(TypedDict):
    PhoneNumber: PhoneNumberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePhoneNumberResponseTypeDef(TypedDict):
    PhoneNumber: PhoneNumberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRetentionSettingsResponseTypeDef(TypedDict):
    RetentionSettings: RetentionSettingsTypeDef
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutRetentionSettingsRequestTypeDef(TypedDict):
    AccountId: str
    RetentionSettings: RetentionSettingsTypeDef

class PutRetentionSettingsResponseTypeDef(TypedDict):
    RetentionSettings: RetentionSettingsTypeDef
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserSettingsResponseTypeDef(TypedDict):
    UserSettings: UserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserSettingsRequestTypeDef(TypedDict):
    AccountId: str
    UserId: str
    UserSettings: UserSettingsTypeDef
