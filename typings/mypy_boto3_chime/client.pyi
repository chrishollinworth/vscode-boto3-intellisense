# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for chime service client

Usage::

    ```python
    import boto3
    from mypy_boto3_chime import ChimeClient

    client: ChimeClient = boto3.client("chime")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_chime.paginator import ListAccountsPaginator, ListUsersPaginator
from mypy_boto3_chime.type_defs import (
    AccountSettingsTypeDef,
    AlexaForBusinessMetadataTypeDef,
    AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef,
    AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef,
    BatchCreateAttendeeResponseTypeDef,
    BatchCreateRoomMembershipResponseTypeDef,
    BatchDeletePhoneNumberResponseTypeDef,
    BatchSuspendUserResponseTypeDef,
    BatchUnsuspendUserResponseTypeDef,
    BatchUpdatePhoneNumberResponseTypeDef,
    BatchUpdateUserResponseTypeDef,
    BusinessCallingSettingsTypeDef,
    CreateAccountResponseTypeDef,
    CreateAttendeeRequestItemTypeDef,
    CreateAttendeeResponseTypeDef,
    CreateBotResponseTypeDef,
    CreateMeetingResponseTypeDef,
    CreateMeetingWithAttendeesResponseTypeDef,
    CreatePhoneNumberOrderResponseTypeDef,
    CreateProxySessionResponseTypeDef,
    CreateRoomMembershipResponseTypeDef,
    CreateRoomResponseTypeDef,
    CreateUserResponseTypeDef,
    CreateVoiceConnectorGroupResponseTypeDef,
    CreateVoiceConnectorResponseTypeDef,
    CredentialTypeDef,
    DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef,
    DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef,
    EmergencyCallingConfigurationTypeDef,
    GeoMatchParamsTypeDef,
    GetAccountResponseTypeDef,
    GetAccountSettingsResponseTypeDef,
    GetAttendeeResponseTypeDef,
    GetBotResponseTypeDef,
    GetEventsConfigurationResponseTypeDef,
    GetGlobalSettingsResponseTypeDef,
    GetMeetingResponseTypeDef,
    GetPhoneNumberOrderResponseTypeDef,
    GetPhoneNumberResponseTypeDef,
    GetPhoneNumberSettingsResponseTypeDef,
    GetProxySessionResponseTypeDef,
    GetRetentionSettingsResponseTypeDef,
    GetRoomResponseTypeDef,
    GetUserResponseTypeDef,
    GetUserSettingsResponseTypeDef,
    GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef,
    GetVoiceConnectorGroupResponseTypeDef,
    GetVoiceConnectorLoggingConfigurationResponseTypeDef,
    GetVoiceConnectorOriginationResponseTypeDef,
    GetVoiceConnectorProxyResponseTypeDef,
    GetVoiceConnectorResponseTypeDef,
    GetVoiceConnectorStreamingConfigurationResponseTypeDef,
    GetVoiceConnectorTerminationHealthResponseTypeDef,
    GetVoiceConnectorTerminationResponseTypeDef,
    InviteUsersResponseTypeDef,
    ListAccountsResponseTypeDef,
    ListAttendeesResponseTypeDef,
    ListAttendeeTagsResponseTypeDef,
    ListBotsResponseTypeDef,
    ListMeetingsResponseTypeDef,
    ListMeetingTagsResponseTypeDef,
    ListPhoneNumberOrdersResponseTypeDef,
    ListPhoneNumbersResponseTypeDef,
    ListProxySessionsResponseTypeDef,
    ListRoomMembershipsResponseTypeDef,
    ListRoomsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsersResponseTypeDef,
    ListVoiceConnectorGroupsResponseTypeDef,
    ListVoiceConnectorsResponseTypeDef,
    ListVoiceConnectorTerminationCredentialsResponseTypeDef,
    LoggingConfigurationTypeDef,
    MeetingNotificationConfigurationTypeDef,
    MembershipItemTypeDef,
    OriginationTypeDef,
    PutEventsConfigurationResponseTypeDef,
    PutRetentionSettingsResponseTypeDef,
    PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef,
    PutVoiceConnectorLoggingConfigurationResponseTypeDef,
    PutVoiceConnectorOriginationResponseTypeDef,
    PutVoiceConnectorProxyResponseTypeDef,
    PutVoiceConnectorStreamingConfigurationResponseTypeDef,
    PutVoiceConnectorTerminationResponseTypeDef,
    RegenerateSecurityTokenResponseTypeDef,
    ResetPersonalPINResponseTypeDef,
    RestorePhoneNumberResponseTypeDef,
    RetentionSettingsTypeDef,
    SearchAvailablePhoneNumbersResponseTypeDef,
    SigninDelegateGroupTypeDef,
    StreamingConfigurationTypeDef,
    TagTypeDef,
    TerminationTypeDef,
    UpdateAccountResponseTypeDef,
    UpdateBotResponseTypeDef,
    UpdatePhoneNumberRequestItemTypeDef,
    UpdatePhoneNumberResponseTypeDef,
    UpdateProxySessionResponseTypeDef,
    UpdateRoomMembershipResponseTypeDef,
    UpdateRoomResponseTypeDef,
    UpdateUserRequestItemTypeDef,
    UpdateUserResponseTypeDef,
    UpdateVoiceConnectorGroupResponseTypeDef,
    UpdateVoiceConnectorResponseTypeDef,
    UserSettingsTypeDef,
    VoiceConnectorItemTypeDef,
    VoiceConnectorSettingsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ChimeClient",)


class Exceptions:
    AccessDeniedException: Type[Boto3ClientError]
    BadRequestException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    ConflictException: Type[Boto3ClientError]
    ForbiddenException: Type[Boto3ClientError]
    NotFoundException: Type[Boto3ClientError]
    ResourceLimitExceededException: Type[Boto3ClientError]
    ServiceFailureException: Type[Boto3ClientError]
    ServiceUnavailableException: Type[Boto3ClientError]
    ThrottledClientException: Type[Boto3ClientError]
    UnauthorizedClientException: Type[Boto3ClientError]
    UnprocessableEntityException: Type[Boto3ClientError]


class ChimeClient:
    """
    [Chime.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client)
    """

    exceptions: Exceptions

    def associate_phone_number_with_user(
        self, AccountId: str, UserId: str, E164PhoneNumber: str
    ) -> Dict[str, Any]:
        """
        [Client.associate_phone_number_with_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.associate_phone_number_with_user)
        """

    def associate_phone_numbers_with_voice_connector(
        self, VoiceConnectorId: str, E164PhoneNumbers: List[str], ForceAssociate: bool = None
    ) -> AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef:
        """
        [Client.associate_phone_numbers_with_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.associate_phone_numbers_with_voice_connector)
        """

    def associate_phone_numbers_with_voice_connector_group(
        self, VoiceConnectorGroupId: str, E164PhoneNumbers: List[str], ForceAssociate: bool = None
    ) -> AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef:
        """
        [Client.associate_phone_numbers_with_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.associate_phone_numbers_with_voice_connector_group)
        """

    def associate_signin_delegate_groups_with_account(
        self, AccountId: str, SigninDelegateGroups: List["SigninDelegateGroupTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Client.associate_signin_delegate_groups_with_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.associate_signin_delegate_groups_with_account)
        """

    def batch_create_attendee(
        self, MeetingId: str, Attendees: List[CreateAttendeeRequestItemTypeDef]
    ) -> BatchCreateAttendeeResponseTypeDef:
        """
        [Client.batch_create_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.batch_create_attendee)
        """

    def batch_create_room_membership(
        self, AccountId: str, RoomId: str, MembershipItemList: List[MembershipItemTypeDef]
    ) -> BatchCreateRoomMembershipResponseTypeDef:
        """
        [Client.batch_create_room_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.batch_create_room_membership)
        """

    def batch_delete_phone_number(
        self, PhoneNumberIds: List[str]
    ) -> BatchDeletePhoneNumberResponseTypeDef:
        """
        [Client.batch_delete_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.batch_delete_phone_number)
        """

    def batch_suspend_user(
        self, AccountId: str, UserIdList: List[str]
    ) -> BatchSuspendUserResponseTypeDef:
        """
        [Client.batch_suspend_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.batch_suspend_user)
        """

    def batch_unsuspend_user(
        self, AccountId: str, UserIdList: List[str]
    ) -> BatchUnsuspendUserResponseTypeDef:
        """
        [Client.batch_unsuspend_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.batch_unsuspend_user)
        """

    def batch_update_phone_number(
        self, UpdatePhoneNumberRequestItems: List[UpdatePhoneNumberRequestItemTypeDef]
    ) -> BatchUpdatePhoneNumberResponseTypeDef:
        """
        [Client.batch_update_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.batch_update_phone_number)
        """

    def batch_update_user(
        self, AccountId: str, UpdateUserRequestItems: List[UpdateUserRequestItemTypeDef]
    ) -> BatchUpdateUserResponseTypeDef:
        """
        [Client.batch_update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.batch_update_user)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.can_paginate)
        """

    def create_account(self, Name: str) -> CreateAccountResponseTypeDef:
        """
        [Client.create_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.create_account)
        """

    def create_attendee(
        self, MeetingId: str, ExternalUserId: str, Tags: List["TagTypeDef"] = None
    ) -> CreateAttendeeResponseTypeDef:
        """
        [Client.create_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.create_attendee)
        """

    def create_bot(
        self, AccountId: str, DisplayName: str, Domain: str = None
    ) -> CreateBotResponseTypeDef:
        """
        [Client.create_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.create_bot)
        """

    def create_meeting(
        self,
        ClientRequestToken: str,
        ExternalMeetingId: str = None,
        MeetingHostId: str = None,
        MediaRegion: str = None,
        Tags: List["TagTypeDef"] = None,
        NotificationsConfiguration: MeetingNotificationConfigurationTypeDef = None,
    ) -> CreateMeetingResponseTypeDef:
        """
        [Client.create_meeting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.create_meeting)
        """

    def create_meeting_with_attendees(
        self,
        ClientRequestToken: str,
        ExternalMeetingId: str = None,
        MeetingHostId: str = None,
        MediaRegion: str = None,
        Tags: List["TagTypeDef"] = None,
        NotificationsConfiguration: MeetingNotificationConfigurationTypeDef = None,
        Attendees: List[CreateAttendeeRequestItemTypeDef] = None,
    ) -> CreateMeetingWithAttendeesResponseTypeDef:
        """
        [Client.create_meeting_with_attendees documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.create_meeting_with_attendees)
        """

    def create_phone_number_order(
        self, ProductType: Literal["BusinessCalling", "VoiceConnector"], E164PhoneNumbers: List[str]
    ) -> CreatePhoneNumberOrderResponseTypeDef:
        """
        [Client.create_phone_number_order documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.create_phone_number_order)
        """

    def create_proxy_session(
        self,
        VoiceConnectorId: str,
        ParticipantPhoneNumbers: List[str],
        Capabilities: List[Literal["Voice", "SMS"]],
        Name: str = None,
        ExpiryMinutes: int = None,
        NumberSelectionBehavior: Literal["PreferSticky", "AvoidSticky"] = None,
        GeoMatchLevel: Literal["Country", "AreaCode"] = None,
        GeoMatchParams: "GeoMatchParamsTypeDef" = None,
    ) -> CreateProxySessionResponseTypeDef:
        """
        [Client.create_proxy_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.create_proxy_session)
        """

    def create_room(
        self, AccountId: str, Name: str, ClientRequestToken: str = None
    ) -> CreateRoomResponseTypeDef:
        """
        [Client.create_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.create_room)
        """

    def create_room_membership(
        self,
        AccountId: str,
        RoomId: str,
        MemberId: str,
        Role: Literal["Administrator", "Member"] = None,
    ) -> CreateRoomMembershipResponseTypeDef:
        """
        [Client.create_room_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.create_room_membership)
        """

    def create_user(
        self,
        AccountId: str,
        Username: str = None,
        Email: str = None,
        UserType: Literal["PrivateUser", "SharedDevice"] = None,
    ) -> CreateUserResponseTypeDef:
        """
        [Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.create_user)
        """

    def create_voice_connector(
        self,
        Name: str,
        RequireEncryption: bool,
        AwsRegion: Literal["us-east-1", "us-west-2"] = None,
    ) -> CreateVoiceConnectorResponseTypeDef:
        """
        [Client.create_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.create_voice_connector)
        """

    def create_voice_connector_group(
        self, Name: str, VoiceConnectorItems: List["VoiceConnectorItemTypeDef"] = None
    ) -> CreateVoiceConnectorGroupResponseTypeDef:
        """
        [Client.create_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.create_voice_connector_group)
        """

    def delete_account(self, AccountId: str) -> Dict[str, Any]:
        """
        [Client.delete_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.delete_account)
        """

    def delete_attendee(self, MeetingId: str, AttendeeId: str) -> None:
        """
        [Client.delete_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.delete_attendee)
        """

    def delete_events_configuration(self, AccountId: str, BotId: str) -> None:
        """
        [Client.delete_events_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.delete_events_configuration)
        """

    def delete_meeting(self, MeetingId: str) -> None:
        """
        [Client.delete_meeting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.delete_meeting)
        """

    def delete_phone_number(self, PhoneNumberId: str) -> None:
        """
        [Client.delete_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.delete_phone_number)
        """

    def delete_proxy_session(self, VoiceConnectorId: str, ProxySessionId: str) -> None:
        """
        [Client.delete_proxy_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.delete_proxy_session)
        """

    def delete_room(self, AccountId: str, RoomId: str) -> None:
        """
        [Client.delete_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.delete_room)
        """

    def delete_room_membership(self, AccountId: str, RoomId: str, MemberId: str) -> None:
        """
        [Client.delete_room_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.delete_room_membership)
        """

    def delete_voice_connector(self, VoiceConnectorId: str) -> None:
        """
        [Client.delete_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.delete_voice_connector)
        """

    def delete_voice_connector_emergency_calling_configuration(self, VoiceConnectorId: str) -> None:
        """
        [Client.delete_voice_connector_emergency_calling_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.delete_voice_connector_emergency_calling_configuration)
        """

    def delete_voice_connector_group(self, VoiceConnectorGroupId: str) -> None:
        """
        [Client.delete_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.delete_voice_connector_group)
        """

    def delete_voice_connector_origination(self, VoiceConnectorId: str) -> None:
        """
        [Client.delete_voice_connector_origination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.delete_voice_connector_origination)
        """

    def delete_voice_connector_proxy(self, VoiceConnectorId: str) -> None:
        """
        [Client.delete_voice_connector_proxy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.delete_voice_connector_proxy)
        """

    def delete_voice_connector_streaming_configuration(self, VoiceConnectorId: str) -> None:
        """
        [Client.delete_voice_connector_streaming_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.delete_voice_connector_streaming_configuration)
        """

    def delete_voice_connector_termination(self, VoiceConnectorId: str) -> None:
        """
        [Client.delete_voice_connector_termination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.delete_voice_connector_termination)
        """

    def delete_voice_connector_termination_credentials(
        self, VoiceConnectorId: str, Usernames: List[str]
    ) -> None:
        """
        [Client.delete_voice_connector_termination_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.delete_voice_connector_termination_credentials)
        """

    def disassociate_phone_number_from_user(self, AccountId: str, UserId: str) -> Dict[str, Any]:
        """
        [Client.disassociate_phone_number_from_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.disassociate_phone_number_from_user)
        """

    def disassociate_phone_numbers_from_voice_connector(
        self, VoiceConnectorId: str, E164PhoneNumbers: List[str]
    ) -> DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef:
        """
        [Client.disassociate_phone_numbers_from_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.disassociate_phone_numbers_from_voice_connector)
        """

    def disassociate_phone_numbers_from_voice_connector_group(
        self, VoiceConnectorGroupId: str, E164PhoneNumbers: List[str]
    ) -> DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef:
        """
        [Client.disassociate_phone_numbers_from_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.disassociate_phone_numbers_from_voice_connector_group)
        """

    def disassociate_signin_delegate_groups_from_account(
        self, AccountId: str, GroupNames: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_signin_delegate_groups_from_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.disassociate_signin_delegate_groups_from_account)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.generate_presigned_url)
        """

    def get_account(self, AccountId: str) -> GetAccountResponseTypeDef:
        """
        [Client.get_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_account)
        """

    def get_account_settings(self, AccountId: str) -> GetAccountSettingsResponseTypeDef:
        """
        [Client.get_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_account_settings)
        """

    def get_attendee(self, MeetingId: str, AttendeeId: str) -> GetAttendeeResponseTypeDef:
        """
        [Client.get_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_attendee)
        """

    def get_bot(self, AccountId: str, BotId: str) -> GetBotResponseTypeDef:
        """
        [Client.get_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_bot)
        """

    def get_events_configuration(
        self, AccountId: str, BotId: str
    ) -> GetEventsConfigurationResponseTypeDef:
        """
        [Client.get_events_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_events_configuration)
        """

    def get_global_settings(self) -> GetGlobalSettingsResponseTypeDef:
        """
        [Client.get_global_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_global_settings)
        """

    def get_meeting(self, MeetingId: str) -> GetMeetingResponseTypeDef:
        """
        [Client.get_meeting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_meeting)
        """

    def get_phone_number(self, PhoneNumberId: str) -> GetPhoneNumberResponseTypeDef:
        """
        [Client.get_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_phone_number)
        """

    def get_phone_number_order(self, PhoneNumberOrderId: str) -> GetPhoneNumberOrderResponseTypeDef:
        """
        [Client.get_phone_number_order documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_phone_number_order)
        """

    def get_phone_number_settings(self) -> GetPhoneNumberSettingsResponseTypeDef:
        """
        [Client.get_phone_number_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_phone_number_settings)
        """

    def get_proxy_session(
        self, VoiceConnectorId: str, ProxySessionId: str
    ) -> GetProxySessionResponseTypeDef:
        """
        [Client.get_proxy_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_proxy_session)
        """

    def get_retention_settings(self, AccountId: str) -> GetRetentionSettingsResponseTypeDef:
        """
        [Client.get_retention_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_retention_settings)
        """

    def get_room(self, AccountId: str, RoomId: str) -> GetRoomResponseTypeDef:
        """
        [Client.get_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_room)
        """

    def get_user(self, AccountId: str, UserId: str) -> GetUserResponseTypeDef:
        """
        [Client.get_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_user)
        """

    def get_user_settings(self, AccountId: str, UserId: str) -> GetUserSettingsResponseTypeDef:
        """
        [Client.get_user_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_user_settings)
        """

    def get_voice_connector(self, VoiceConnectorId: str) -> GetVoiceConnectorResponseTypeDef:
        """
        [Client.get_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_voice_connector)
        """

    def get_voice_connector_emergency_calling_configuration(
        self, VoiceConnectorId: str
    ) -> GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef:
        """
        [Client.get_voice_connector_emergency_calling_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_voice_connector_emergency_calling_configuration)
        """

    def get_voice_connector_group(
        self, VoiceConnectorGroupId: str
    ) -> GetVoiceConnectorGroupResponseTypeDef:
        """
        [Client.get_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_voice_connector_group)
        """

    def get_voice_connector_logging_configuration(
        self, VoiceConnectorId: str
    ) -> GetVoiceConnectorLoggingConfigurationResponseTypeDef:
        """
        [Client.get_voice_connector_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_voice_connector_logging_configuration)
        """

    def get_voice_connector_origination(
        self, VoiceConnectorId: str
    ) -> GetVoiceConnectorOriginationResponseTypeDef:
        """
        [Client.get_voice_connector_origination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_voice_connector_origination)
        """

    def get_voice_connector_proxy(
        self, VoiceConnectorId: str
    ) -> GetVoiceConnectorProxyResponseTypeDef:
        """
        [Client.get_voice_connector_proxy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_voice_connector_proxy)
        """

    def get_voice_connector_streaming_configuration(
        self, VoiceConnectorId: str
    ) -> GetVoiceConnectorStreamingConfigurationResponseTypeDef:
        """
        [Client.get_voice_connector_streaming_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_voice_connector_streaming_configuration)
        """

    def get_voice_connector_termination(
        self, VoiceConnectorId: str
    ) -> GetVoiceConnectorTerminationResponseTypeDef:
        """
        [Client.get_voice_connector_termination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_voice_connector_termination)
        """

    def get_voice_connector_termination_health(
        self, VoiceConnectorId: str
    ) -> GetVoiceConnectorTerminationHealthResponseTypeDef:
        """
        [Client.get_voice_connector_termination_health documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.get_voice_connector_termination_health)
        """

    def invite_users(
        self,
        AccountId: str,
        UserEmailList: List[str],
        UserType: Literal["PrivateUser", "SharedDevice"] = None,
    ) -> InviteUsersResponseTypeDef:
        """
        [Client.invite_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.invite_users)
        """

    def list_accounts(
        self, Name: str = None, UserEmail: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListAccountsResponseTypeDef:
        """
        [Client.list_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.list_accounts)
        """

    def list_attendee_tags(
        self, MeetingId: str, AttendeeId: str
    ) -> ListAttendeeTagsResponseTypeDef:
        """
        [Client.list_attendee_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.list_attendee_tags)
        """

    def list_attendees(
        self, MeetingId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAttendeesResponseTypeDef:
        """
        [Client.list_attendees documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.list_attendees)
        """

    def list_bots(
        self, AccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListBotsResponseTypeDef:
        """
        [Client.list_bots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.list_bots)
        """

    def list_meeting_tags(self, MeetingId: str) -> ListMeetingTagsResponseTypeDef:
        """
        [Client.list_meeting_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.list_meeting_tags)
        """

    def list_meetings(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListMeetingsResponseTypeDef:
        """
        [Client.list_meetings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.list_meetings)
        """

    def list_phone_number_orders(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListPhoneNumberOrdersResponseTypeDef:
        """
        [Client.list_phone_number_orders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.list_phone_number_orders)
        """

    def list_phone_numbers(
        self,
        Status: Literal[
            "AcquireInProgress",
            "AcquireFailed",
            "Unassigned",
            "Assigned",
            "ReleaseInProgress",
            "DeleteInProgress",
            "ReleaseFailed",
            "DeleteFailed",
        ] = None,
        ProductType: Literal["BusinessCalling", "VoiceConnector"] = None,
        FilterName: Literal[
            "AccountId", "UserId", "VoiceConnectorId", "VoiceConnectorGroupId"
        ] = None,
        FilterValue: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListPhoneNumbersResponseTypeDef:
        """
        [Client.list_phone_numbers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.list_phone_numbers)
        """

    def list_proxy_sessions(
        self,
        VoiceConnectorId: str,
        Status: Literal["Open", "InProgress", "Closed"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListProxySessionsResponseTypeDef:
        """
        [Client.list_proxy_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.list_proxy_sessions)
        """

    def list_room_memberships(
        self, AccountId: str, RoomId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListRoomMembershipsResponseTypeDef:
        """
        [Client.list_room_memberships documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.list_room_memberships)
        """

    def list_rooms(
        self, AccountId: str, MemberId: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListRoomsResponseTypeDef:
        """
        [Client.list_rooms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.list_rooms)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.list_tags_for_resource)
        """

    def list_users(
        self,
        AccountId: str,
        UserEmail: str = None,
        UserType: Literal["PrivateUser", "SharedDevice"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListUsersResponseTypeDef:
        """
        [Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.list_users)
        """

    def list_voice_connector_groups(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListVoiceConnectorGroupsResponseTypeDef:
        """
        [Client.list_voice_connector_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.list_voice_connector_groups)
        """

    def list_voice_connector_termination_credentials(
        self, VoiceConnectorId: str
    ) -> ListVoiceConnectorTerminationCredentialsResponseTypeDef:
        """
        [Client.list_voice_connector_termination_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.list_voice_connector_termination_credentials)
        """

    def list_voice_connectors(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListVoiceConnectorsResponseTypeDef:
        """
        [Client.list_voice_connectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.list_voice_connectors)
        """

    def logout_user(self, AccountId: str, UserId: str) -> Dict[str, Any]:
        """
        [Client.logout_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.logout_user)
        """

    def put_events_configuration(
        self,
        AccountId: str,
        BotId: str,
        OutboundEventsHTTPSEndpoint: str = None,
        LambdaFunctionArn: str = None,
    ) -> PutEventsConfigurationResponseTypeDef:
        """
        [Client.put_events_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.put_events_configuration)
        """

    def put_retention_settings(
        self, AccountId: str, RetentionSettings: "RetentionSettingsTypeDef"
    ) -> PutRetentionSettingsResponseTypeDef:
        """
        [Client.put_retention_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.put_retention_settings)
        """

    def put_voice_connector_emergency_calling_configuration(
        self,
        VoiceConnectorId: str,
        EmergencyCallingConfiguration: "EmergencyCallingConfigurationTypeDef",
    ) -> PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef:
        """
        [Client.put_voice_connector_emergency_calling_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.put_voice_connector_emergency_calling_configuration)
        """

    def put_voice_connector_logging_configuration(
        self, VoiceConnectorId: str, LoggingConfiguration: "LoggingConfigurationTypeDef"
    ) -> PutVoiceConnectorLoggingConfigurationResponseTypeDef:
        """
        [Client.put_voice_connector_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.put_voice_connector_logging_configuration)
        """

    def put_voice_connector_origination(
        self, VoiceConnectorId: str, Origination: "OriginationTypeDef"
    ) -> PutVoiceConnectorOriginationResponseTypeDef:
        """
        [Client.put_voice_connector_origination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.put_voice_connector_origination)
        """

    def put_voice_connector_proxy(
        self,
        VoiceConnectorId: str,
        DefaultSessionExpiryMinutes: int,
        PhoneNumberPoolCountries: List[str],
        FallBackPhoneNumber: str = None,
        Disabled: bool = None,
    ) -> PutVoiceConnectorProxyResponseTypeDef:
        """
        [Client.put_voice_connector_proxy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.put_voice_connector_proxy)
        """

    def put_voice_connector_streaming_configuration(
        self, VoiceConnectorId: str, StreamingConfiguration: "StreamingConfigurationTypeDef"
    ) -> PutVoiceConnectorStreamingConfigurationResponseTypeDef:
        """
        [Client.put_voice_connector_streaming_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.put_voice_connector_streaming_configuration)
        """

    def put_voice_connector_termination(
        self, VoiceConnectorId: str, Termination: "TerminationTypeDef"
    ) -> PutVoiceConnectorTerminationResponseTypeDef:
        """
        [Client.put_voice_connector_termination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.put_voice_connector_termination)
        """

    def put_voice_connector_termination_credentials(
        self, VoiceConnectorId: str, Credentials: List[CredentialTypeDef] = None
    ) -> None:
        """
        [Client.put_voice_connector_termination_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.put_voice_connector_termination_credentials)
        """

    def redact_conversation_message(
        self, AccountId: str, ConversationId: str, MessageId: str
    ) -> Dict[str, Any]:
        """
        [Client.redact_conversation_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.redact_conversation_message)
        """

    def redact_room_message(self, AccountId: str, RoomId: str, MessageId: str) -> Dict[str, Any]:
        """
        [Client.redact_room_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.redact_room_message)
        """

    def regenerate_security_token(
        self, AccountId: str, BotId: str
    ) -> RegenerateSecurityTokenResponseTypeDef:
        """
        [Client.regenerate_security_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.regenerate_security_token)
        """

    def reset_personal_pin(self, AccountId: str, UserId: str) -> ResetPersonalPINResponseTypeDef:
        """
        [Client.reset_personal_pin documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.reset_personal_pin)
        """

    def restore_phone_number(self, PhoneNumberId: str) -> RestorePhoneNumberResponseTypeDef:
        """
        [Client.restore_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.restore_phone_number)
        """

    def search_available_phone_numbers(
        self,
        AreaCode: str = None,
        City: str = None,
        Country: str = None,
        State: str = None,
        TollFreePrefix: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> SearchAvailablePhoneNumbersResponseTypeDef:
        """
        [Client.search_available_phone_numbers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.search_available_phone_numbers)
        """

    def tag_attendee(self, MeetingId: str, AttendeeId: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Client.tag_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.tag_attendee)
        """

    def tag_meeting(self, MeetingId: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Client.tag_meeting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.tag_meeting)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.tag_resource)
        """

    def untag_attendee(self, MeetingId: str, AttendeeId: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.untag_attendee)
        """

    def untag_meeting(self, MeetingId: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_meeting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.untag_meeting)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.untag_resource)
        """

    def update_account(self, AccountId: str, Name: str = None) -> UpdateAccountResponseTypeDef:
        """
        [Client.update_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.update_account)
        """

    def update_account_settings(
        self, AccountId: str, AccountSettings: "AccountSettingsTypeDef"
    ) -> Dict[str, Any]:
        """
        [Client.update_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.update_account_settings)
        """

    def update_bot(
        self, AccountId: str, BotId: str, Disabled: bool = None
    ) -> UpdateBotResponseTypeDef:
        """
        [Client.update_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.update_bot)
        """

    def update_global_settings(
        self,
        BusinessCalling: "BusinessCallingSettingsTypeDef",
        VoiceConnector: "VoiceConnectorSettingsTypeDef",
    ) -> None:
        """
        [Client.update_global_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.update_global_settings)
        """

    def update_phone_number(
        self,
        PhoneNumberId: str,
        ProductType: Literal["BusinessCalling", "VoiceConnector"] = None,
        CallingName: str = None,
    ) -> UpdatePhoneNumberResponseTypeDef:
        """
        [Client.update_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.update_phone_number)
        """

    def update_phone_number_settings(self, CallingName: str) -> None:
        """
        [Client.update_phone_number_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.update_phone_number_settings)
        """

    def update_proxy_session(
        self,
        VoiceConnectorId: str,
        ProxySessionId: str,
        Capabilities: List[Literal["Voice", "SMS"]],
        ExpiryMinutes: int = None,
    ) -> UpdateProxySessionResponseTypeDef:
        """
        [Client.update_proxy_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.update_proxy_session)
        """

    def update_room(
        self, AccountId: str, RoomId: str, Name: str = None
    ) -> UpdateRoomResponseTypeDef:
        """
        [Client.update_room documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.update_room)
        """

    def update_room_membership(
        self,
        AccountId: str,
        RoomId: str,
        MemberId: str,
        Role: Literal["Administrator", "Member"] = None,
    ) -> UpdateRoomMembershipResponseTypeDef:
        """
        [Client.update_room_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.update_room_membership)
        """

    def update_user(
        self,
        AccountId: str,
        UserId: str,
        LicenseType: Literal["Basic", "Plus", "Pro", "ProTrial"] = None,
        UserType: Literal["PrivateUser", "SharedDevice"] = None,
        AlexaForBusinessMetadata: "AlexaForBusinessMetadataTypeDef" = None,
    ) -> UpdateUserResponseTypeDef:
        """
        [Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.update_user)
        """

    def update_user_settings(
        self, AccountId: str, UserId: str, UserSettings: "UserSettingsTypeDef"
    ) -> None:
        """
        [Client.update_user_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.update_user_settings)
        """

    def update_voice_connector(
        self, VoiceConnectorId: str, Name: str, RequireEncryption: bool
    ) -> UpdateVoiceConnectorResponseTypeDef:
        """
        [Client.update_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.update_voice_connector)
        """

    def update_voice_connector_group(
        self,
        VoiceConnectorGroupId: str,
        Name: str,
        VoiceConnectorItems: List["VoiceConnectorItemTypeDef"],
    ) -> UpdateVoiceConnectorGroupResponseTypeDef:
        """
        [Client.update_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Client.update_voice_connector_group)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_accounts"]) -> ListAccountsPaginator:
        """
        [Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Paginator.ListAccounts)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/chime.html#Chime.Paginator.ListUsers)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
