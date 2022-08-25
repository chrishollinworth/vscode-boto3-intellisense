"""
Type annotations for alexaforbusiness service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_alexaforbusiness import AlexaForBusinessClient

    client: AlexaForBusinessClient = boto3.client("alexaforbusiness")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    BusinessReportFormatType,
    ConferenceProviderTypeType,
    DeviceEventTypeType,
    DistanceUnitType,
    EnablementTypeFilterType,
    FeatureType,
    NetworkSecurityTypeType,
    SkillTypeFilterType,
    TemperatureUnitType,
    WakeWordType,
)
from .paginator import (
    ListBusinessReportSchedulesPaginator,
    ListConferenceProvidersPaginator,
    ListDeviceEventsPaginator,
    ListSkillsPaginator,
    ListSkillsStoreCategoriesPaginator,
    ListSkillsStoreSkillsByCategoryPaginator,
    ListSmartHomeAppliancesPaginator,
    ListTagsPaginator,
    SearchDevicesPaginator,
    SearchProfilesPaginator,
    SearchRoomsPaginator,
    SearchSkillGroupsPaginator,
    SearchUsersPaginator,
)
from .type_defs import (
    BusinessReportContentRangeTypeDef,
    BusinessReportRecurrenceTypeDef,
    ConferencePreferenceTypeDef,
    ContentTypeDef,
    CreateAddressBookResponseTypeDef,
    CreateBusinessReportScheduleResponseTypeDef,
    CreateConferenceProviderResponseTypeDef,
    CreateContactResponseTypeDef,
    CreateGatewayGroupResponseTypeDef,
    CreateMeetingRoomConfigurationTypeDef,
    CreateNetworkProfileResponseTypeDef,
    CreateProfileResponseTypeDef,
    CreateRoomResponseTypeDef,
    CreateSkillGroupResponseTypeDef,
    CreateUserResponseTypeDef,
    FilterTypeDef,
    GetAddressBookResponseTypeDef,
    GetConferencePreferenceResponseTypeDef,
    GetConferenceProviderResponseTypeDef,
    GetContactResponseTypeDef,
    GetDeviceResponseTypeDef,
    GetGatewayGroupResponseTypeDef,
    GetGatewayResponseTypeDef,
    GetInvitationConfigurationResponseTypeDef,
    GetNetworkProfileResponseTypeDef,
    GetProfileResponseTypeDef,
    GetRoomResponseTypeDef,
    GetRoomSkillParameterResponseTypeDef,
    GetSkillGroupResponseTypeDef,
    IPDialInTypeDef,
    ListBusinessReportSchedulesResponseTypeDef,
    ListConferenceProvidersResponseTypeDef,
    ListDeviceEventsResponseTypeDef,
    ListGatewayGroupsResponseTypeDef,
    ListGatewaysResponseTypeDef,
    ListSkillsResponseTypeDef,
    ListSkillsStoreCategoriesResponseTypeDef,
    ListSkillsStoreSkillsByCategoryResponseTypeDef,
    ListSmartHomeAppliancesResponseTypeDef,
    ListTagsResponseTypeDef,
    MeetingSettingTypeDef,
    PhoneNumberTypeDef,
    PSTNDialInTypeDef,
    RegisterAVSDeviceResponseTypeDef,
    ResolveRoomResponseTypeDef,
    RoomSkillParameterTypeDef,
    SearchAddressBooksResponseTypeDef,
    SearchContactsResponseTypeDef,
    SearchDevicesResponseTypeDef,
    SearchNetworkProfilesResponseTypeDef,
    SearchProfilesResponseTypeDef,
    SearchRoomsResponseTypeDef,
    SearchSkillGroupsResponseTypeDef,
    SearchUsersResponseTypeDef,
    SendAnnouncementResponseTypeDef,
    SipAddressTypeDef,
    SortTypeDef,
    TagTypeDef,
    UpdateMeetingRoomConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AlexaForBusinessClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AlreadyExistsException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    DeviceNotRegisteredException: Type[BotocoreClientError]
    InvalidCertificateAuthorityException: Type[BotocoreClientError]
    InvalidDeviceException: Type[BotocoreClientError]
    InvalidSecretsManagerResourceException: Type[BotocoreClientError]
    InvalidServiceLinkedRoleStateException: Type[BotocoreClientError]
    InvalidUserStatusException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NameInUseException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceAssociatedException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    SkillNotLinkedException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]

class AlexaForBusinessClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AlexaForBusinessClient exceptions.
        """
    def approve_skill(self, *, SkillId: str) -> Dict[str, Any]:
        """
        Associates a skill with the organization under the customer's AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.approve_skill)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#approve_skill)
        """
    def associate_contact_with_address_book(
        self, *, ContactArn: str, AddressBookArn: str
    ) -> Dict[str, Any]:
        """
        Associates a contact with a given address book.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.associate_contact_with_address_book)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#associate_contact_with_address_book)
        """
    def associate_device_with_network_profile(
        self, *, DeviceArn: str, NetworkProfileArn: str
    ) -> Dict[str, Any]:
        """
        Associates a device with the specified network profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.associate_device_with_network_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#associate_device_with_network_profile)
        """
    def associate_device_with_room(
        self, *, DeviceArn: str = None, RoomArn: str = None
    ) -> Dict[str, Any]:
        """
        Associates a device with a given room.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.associate_device_with_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#associate_device_with_room)
        """
    def associate_skill_group_with_room(
        self, *, SkillGroupArn: str = None, RoomArn: str = None
    ) -> Dict[str, Any]:
        """
        Associates a skill group with a given room.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.associate_skill_group_with_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#associate_skill_group_with_room)
        """
    def associate_skill_with_skill_group(
        self, *, SkillId: str, SkillGroupArn: str = None
    ) -> Dict[str, Any]:
        """
        Associates a skill with a skill group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.associate_skill_with_skill_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#associate_skill_with_skill_group)
        """
    def associate_skill_with_users(self, *, SkillId: str) -> Dict[str, Any]:
        """
        Makes a private skill available for enrolled users to enable on their devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.associate_skill_with_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#associate_skill_with_users)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#close)
        """
    def create_address_book(
        self,
        *,
        Name: str,
        Description: str = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAddressBookResponseTypeDef:
        """
        Creates an address book with the specified details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_address_book)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#create_address_book)
        """
    def create_business_report_schedule(
        self,
        *,
        Format: BusinessReportFormatType,
        ContentRange: "BusinessReportContentRangeTypeDef",
        ScheduleName: str = None,
        S3BucketName: str = None,
        S3KeyPrefix: str = None,
        Recurrence: "BusinessReportRecurrenceTypeDef" = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateBusinessReportScheduleResponseTypeDef:
        """
        Creates a recurring schedule for usage reports to deliver to the specified S3
        location with a specified daily or weekly interval.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_business_report_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#create_business_report_schedule)
        """
    def create_conference_provider(
        self,
        *,
        ConferenceProviderName: str,
        ConferenceProviderType: ConferenceProviderTypeType,
        MeetingSetting: "MeetingSettingTypeDef",
        IPDialIn: "IPDialInTypeDef" = None,
        PSTNDialIn: "PSTNDialInTypeDef" = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateConferenceProviderResponseTypeDef:
        """
        Adds a new conference provider under the user's AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_conference_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#create_conference_provider)
        """
    def create_contact(
        self,
        *,
        FirstName: str,
        DisplayName: str = None,
        LastName: str = None,
        PhoneNumber: str = None,
        PhoneNumbers: List["PhoneNumberTypeDef"] = None,
        SipAddresses: List["SipAddressTypeDef"] = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateContactResponseTypeDef:
        """
        Creates a contact with the specified details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#create_contact)
        """
    def create_gateway_group(
        self,
        *,
        Name: str,
        ClientRequestToken: str,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateGatewayGroupResponseTypeDef:
        """
        Creates a gateway group with the specified details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_gateway_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#create_gateway_group)
        """
    def create_network_profile(
        self,
        *,
        NetworkProfileName: str,
        Ssid: str,
        SecurityType: NetworkSecurityTypeType,
        ClientRequestToken: str,
        Description: str = None,
        EapMethod: Literal["EAP_TLS"] = None,
        CurrentPassword: str = None,
        NextPassword: str = None,
        CertificateAuthorityArn: str = None,
        TrustAnchors: List[str] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateNetworkProfileResponseTypeDef:
        """
        Creates a network profile with the specified details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_network_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#create_network_profile)
        """
    def create_profile(
        self,
        *,
        ProfileName: str,
        Timezone: str,
        Address: str,
        DistanceUnit: DistanceUnitType,
        TemperatureUnit: TemperatureUnitType,
        WakeWord: WakeWordType,
        Locale: str = None,
        ClientRequestToken: str = None,
        SetupModeDisabled: bool = None,
        MaxVolumeLimit: int = None,
        PSTNEnabled: bool = None,
        DataRetentionOptIn: bool = None,
        MeetingRoomConfiguration: "CreateMeetingRoomConfigurationTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateProfileResponseTypeDef:
        """
        Creates a new room profile with the specified details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#create_profile)
        """
    def create_room(
        self,
        *,
        RoomName: str,
        Description: str = None,
        ProfileArn: str = None,
        ProviderCalendarId: str = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateRoomResponseTypeDef:
        """
        Creates a room with the specified details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#create_room)
        """
    def create_skill_group(
        self,
        *,
        SkillGroupName: str,
        Description: str = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateSkillGroupResponseTypeDef:
        """
        Creates a skill group with a specified name and description.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_skill_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#create_skill_group)
        """
    def create_user(
        self,
        *,
        UserId: str,
        FirstName: str = None,
        LastName: str = None,
        Email: str = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateUserResponseTypeDef:
        """
        Creates a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#create_user)
        """
    def delete_address_book(self, *, AddressBookArn: str) -> Dict[str, Any]:
        """
        Deletes an address book by the address book ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_address_book)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#delete_address_book)
        """
    def delete_business_report_schedule(self, *, ScheduleArn: str) -> Dict[str, Any]:
        """
        Deletes the recurring report delivery schedule with the specified schedule ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_business_report_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#delete_business_report_schedule)
        """
    def delete_conference_provider(self, *, ConferenceProviderArn: str) -> Dict[str, Any]:
        """
        Deletes a conference provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_conference_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#delete_conference_provider)
        """
    def delete_contact(self, *, ContactArn: str) -> Dict[str, Any]:
        """
        Deletes a contact by the contact ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#delete_contact)
        """
    def delete_device(self, *, DeviceArn: str) -> Dict[str, Any]:
        """
        Removes a device from Alexa For Business.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#delete_device)
        """
    def delete_device_usage_data(
        self, *, DeviceArn: str, DeviceUsageType: Literal["VOICE"]
    ) -> Dict[str, Any]:
        """
        When this action is called for a specified shared device, it allows authorized
        users to delete the device's entire previous history of voice input data and
        associated response data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_device_usage_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#delete_device_usage_data)
        """
    def delete_gateway_group(self, *, GatewayGroupArn: str) -> Dict[str, Any]:
        """
        Deletes a gateway group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_gateway_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#delete_gateway_group)
        """
    def delete_network_profile(self, *, NetworkProfileArn: str) -> Dict[str, Any]:
        """
        Deletes a network profile by the network profile ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_network_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#delete_network_profile)
        """
    def delete_profile(self, *, ProfileArn: str = None) -> Dict[str, Any]:
        """
        Deletes a room profile by the profile ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#delete_profile)
        """
    def delete_room(self, *, RoomArn: str = None) -> Dict[str, Any]:
        """
        Deletes a room by the room ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#delete_room)
        """
    def delete_room_skill_parameter(
        self, *, SkillId: str, ParameterKey: str, RoomArn: str = None
    ) -> Dict[str, Any]:
        """
        Deletes room skill parameter details by room, skill, and parameter key ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_room_skill_parameter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#delete_room_skill_parameter)
        """
    def delete_skill_authorization(self, *, SkillId: str, RoomArn: str = None) -> Dict[str, Any]:
        """
        Unlinks a third-party account from a skill.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_skill_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#delete_skill_authorization)
        """
    def delete_skill_group(self, *, SkillGroupArn: str = None) -> Dict[str, Any]:
        """
        Deletes a skill group by skill group ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_skill_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#delete_skill_group)
        """
    def delete_user(self, *, EnrollmentId: str, UserArn: str = None) -> Dict[str, Any]:
        """
        Deletes a specified user by user ARN and enrollment ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#delete_user)
        """
    def disassociate_contact_from_address_book(
        self, *, ContactArn: str, AddressBookArn: str
    ) -> Dict[str, Any]:
        """
        Disassociates a contact from a given address book.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.disassociate_contact_from_address_book)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#disassociate_contact_from_address_book)
        """
    def disassociate_device_from_room(self, *, DeviceArn: str = None) -> Dict[str, Any]:
        """
        Disassociates a device from its current room.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.disassociate_device_from_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#disassociate_device_from_room)
        """
    def disassociate_skill_from_skill_group(
        self, *, SkillId: str, SkillGroupArn: str = None
    ) -> Dict[str, Any]:
        """
        Disassociates a skill from a skill group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.disassociate_skill_from_skill_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#disassociate_skill_from_skill_group)
        """
    def disassociate_skill_from_users(self, *, SkillId: str) -> Dict[str, Any]:
        """
        Makes a private skill unavailable for enrolled users and prevents them from
        enabling it on their devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.disassociate_skill_from_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#disassociate_skill_from_users)
        """
    def disassociate_skill_group_from_room(
        self, *, SkillGroupArn: str = None, RoomArn: str = None
    ) -> Dict[str, Any]:
        """
        Disassociates a skill group from a specified room.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.disassociate_skill_group_from_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#disassociate_skill_group_from_room)
        """
    def forget_smart_home_appliances(self, *, RoomArn: str) -> Dict[str, Any]:
        """
        Forgets smart home appliances associated to a room.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.forget_smart_home_appliances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#forget_smart_home_appliances)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#generate_presigned_url)
        """
    def get_address_book(self, *, AddressBookArn: str) -> GetAddressBookResponseTypeDef:
        """
        Gets address the book details by the address book ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_address_book)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#get_address_book)
        """
    def get_conference_preference(self) -> GetConferencePreferenceResponseTypeDef:
        """
        Retrieves the existing conference preferences.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_conference_preference)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#get_conference_preference)
        """
    def get_conference_provider(
        self, *, ConferenceProviderArn: str
    ) -> GetConferenceProviderResponseTypeDef:
        """
        Gets details about a specific conference provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_conference_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#get_conference_provider)
        """
    def get_contact(self, *, ContactArn: str) -> GetContactResponseTypeDef:
        """
        Gets the contact details by the contact ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#get_contact)
        """
    def get_device(self, *, DeviceArn: str = None) -> GetDeviceResponseTypeDef:
        """
        Gets the details of a device by device ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#get_device)
        """
    def get_gateway(self, *, GatewayArn: str) -> GetGatewayResponseTypeDef:
        """
        Retrieves the details of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#get_gateway)
        """
    def get_gateway_group(self, *, GatewayGroupArn: str) -> GetGatewayGroupResponseTypeDef:
        """
        Retrieves the details of a gateway group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_gateway_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#get_gateway_group)
        """
    def get_invitation_configuration(self) -> GetInvitationConfigurationResponseTypeDef:
        """
        Retrieves the configured values for the user enrollment invitation email
        template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_invitation_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#get_invitation_configuration)
        """
    def get_network_profile(self, *, NetworkProfileArn: str) -> GetNetworkProfileResponseTypeDef:
        """
        Gets the network profile details by the network profile ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_network_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#get_network_profile)
        """
    def get_profile(self, *, ProfileArn: str = None) -> GetProfileResponseTypeDef:
        """
        Gets the details of a room profile by profile ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#get_profile)
        """
    def get_room(self, *, RoomArn: str = None) -> GetRoomResponseTypeDef:
        """
        Gets room details by room ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#get_room)
        """
    def get_room_skill_parameter(
        self, *, SkillId: str, ParameterKey: str, RoomArn: str = None
    ) -> GetRoomSkillParameterResponseTypeDef:
        """
        Gets room skill parameter details by room, skill, and parameter key ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_room_skill_parameter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#get_room_skill_parameter)
        """
    def get_skill_group(self, *, SkillGroupArn: str = None) -> GetSkillGroupResponseTypeDef:
        """
        Gets skill group details by skill group ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_skill_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#get_skill_group)
        """
    def list_business_report_schedules(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListBusinessReportSchedulesResponseTypeDef:
        """
        Lists the details of the schedules that a user configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_business_report_schedules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#list_business_report_schedules)
        """
    def list_conference_providers(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListConferenceProvidersResponseTypeDef:
        """
        Lists conference providers under a specific AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_conference_providers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#list_conference_providers)
        """
    def list_device_events(
        self,
        *,
        DeviceArn: str,
        EventType: DeviceEventTypeType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListDeviceEventsResponseTypeDef:
        """
        Lists the device event history, including device connection status, for up to 30
        days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_device_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#list_device_events)
        """
    def list_gateway_groups(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListGatewayGroupsResponseTypeDef:
        """
        Retrieves a list of gateway group summaries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_gateway_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#list_gateway_groups)
        """
    def list_gateways(
        self, *, GatewayGroupArn: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListGatewaysResponseTypeDef:
        """
        Retrieves a list of gateway summaries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#list_gateways)
        """
    def list_skills(
        self,
        *,
        SkillGroupArn: str = None,
        EnablementType: EnablementTypeFilterType = None,
        SkillType: SkillTypeFilterType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListSkillsResponseTypeDef:
        """
        Lists all enabled skills in a specific skill group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_skills)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#list_skills)
        """
    def list_skills_store_categories(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListSkillsStoreCategoriesResponseTypeDef:
        """
        Lists all categories in the Alexa skill store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_skills_store_categories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#list_skills_store_categories)
        """
    def list_skills_store_skills_by_category(
        self, *, CategoryId: int, NextToken: str = None, MaxResults: int = None
    ) -> ListSkillsStoreSkillsByCategoryResponseTypeDef:
        """
        Lists all skills in the Alexa skill store by category.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_skills_store_skills_by_category)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#list_skills_store_skills_by_category)
        """
    def list_smart_home_appliances(
        self, *, RoomArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListSmartHomeAppliancesResponseTypeDef:
        """
        Lists all of the smart home appliances associated with a room.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_smart_home_appliances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#list_smart_home_appliances)
        """
    def list_tags(
        self, *, Arn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsResponseTypeDef:
        """
        Lists all tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#list_tags)
        """
    def put_conference_preference(
        self, *, ConferencePreference: "ConferencePreferenceTypeDef"
    ) -> Dict[str, Any]:
        """
        Sets the conference preferences on a specific conference provider at the account
        level.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.put_conference_preference)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#put_conference_preference)
        """
    def put_invitation_configuration(
        self, *, OrganizationName: str, ContactEmail: str = None, PrivateSkillIds: List[str] = None
    ) -> Dict[str, Any]:
        """
        Configures the email template for the user enrollment invitation with the
        specified attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.put_invitation_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#put_invitation_configuration)
        """
    def put_room_skill_parameter(
        self, *, SkillId: str, RoomSkillParameter: "RoomSkillParameterTypeDef", RoomArn: str = None
    ) -> Dict[str, Any]:
        """
        Updates room skill parameter details by room, skill, and parameter key ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.put_room_skill_parameter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#put_room_skill_parameter)
        """
    def put_skill_authorization(
        self, *, AuthorizationResult: Dict[str, str], SkillId: str, RoomArn: str = None
    ) -> Dict[str, Any]:
        """
        Links a user's account to a third-party skill provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.put_skill_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#put_skill_authorization)
        """
    def register_avs_device(
        self,
        *,
        ClientId: str,
        UserCode: str,
        ProductId: str,
        AmazonId: str,
        DeviceSerialNumber: str = None,
        RoomArn: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> RegisterAVSDeviceResponseTypeDef:
        """
        Registers an Alexa-enabled device built by an Original Equipment Manufacturer
        (OEM) using Alexa Voice Service (AVS).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.register_avs_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#register_avs_device)
        """
    def reject_skill(self, *, SkillId: str) -> Dict[str, Any]:
        """
        Disassociates a skill from the organization under a user's AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.reject_skill)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#reject_skill)
        """
    def resolve_room(self, *, UserId: str, SkillId: str) -> ResolveRoomResponseTypeDef:
        """
        Determines the details for the room from which a skill request was invoked.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.resolve_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#resolve_room)
        """
    def revoke_invitation(self, *, UserArn: str = None, EnrollmentId: str = None) -> Dict[str, Any]:
        """
        Revokes an invitation and invalidates the enrollment URL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.revoke_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#revoke_invitation)
        """
    def search_address_books(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        SortCriteria: List["SortTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> SearchAddressBooksResponseTypeDef:
        """
        Searches address books and lists the ones that meet a set of filter and sort
        criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_address_books)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#search_address_books)
        """
    def search_contacts(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        SortCriteria: List["SortTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> SearchContactsResponseTypeDef:
        """
        Searches contacts and lists the ones that meet a set of filter and sort
        criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_contacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#search_contacts)
        """
    def search_devices(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None,
        SortCriteria: List["SortTypeDef"] = None
    ) -> SearchDevicesResponseTypeDef:
        """
        Searches devices and lists the ones that meet a set of filter criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#search_devices)
        """
    def search_network_profiles(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None,
        SortCriteria: List["SortTypeDef"] = None
    ) -> SearchNetworkProfilesResponseTypeDef:
        """
        Searches network profiles and lists the ones that meet a set of filter and sort
        criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_network_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#search_network_profiles)
        """
    def search_profiles(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None,
        SortCriteria: List["SortTypeDef"] = None
    ) -> SearchProfilesResponseTypeDef:
        """
        Searches room profiles and lists the ones that meet a set of filter criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#search_profiles)
        """
    def search_rooms(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None,
        SortCriteria: List["SortTypeDef"] = None
    ) -> SearchRoomsResponseTypeDef:
        """
        Searches rooms and lists the ones that meet a set of filter and sort criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_rooms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#search_rooms)
        """
    def search_skill_groups(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None,
        SortCriteria: List["SortTypeDef"] = None
    ) -> SearchSkillGroupsResponseTypeDef:
        """
        Searches skill groups and lists the ones that meet a set of filter and sort
        criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_skill_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#search_skill_groups)
        """
    def search_users(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None,
        SortCriteria: List["SortTypeDef"] = None
    ) -> SearchUsersResponseTypeDef:
        """
        Searches users and lists the ones that meet a set of filter and sort criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#search_users)
        """
    def send_announcement(
        self,
        *,
        RoomFilters: List["FilterTypeDef"],
        Content: "ContentTypeDef",
        ClientRequestToken: str,
        TimeToLiveInSeconds: int = None
    ) -> SendAnnouncementResponseTypeDef:
        """
        Triggers an asynchronous flow to send text, SSML, or audio announcements to
        rooms that are identified by a search or filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.send_announcement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#send_announcement)
        """
    def send_invitation(self, *, UserArn: str = None) -> Dict[str, Any]:
        """
        Sends an enrollment invitation email with a URL to a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.send_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#send_invitation)
        """
    def start_device_sync(
        self, *, Features: List[FeatureType], RoomArn: str = None, DeviceArn: str = None
    ) -> Dict[str, Any]:
        """
        Resets a device and its account to the known default settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.start_device_sync)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#start_device_sync)
        """
    def start_smart_home_appliance_discovery(self, *, RoomArn: str) -> Dict[str, Any]:
        """
        Initiates the discovery of any smart home appliances associated with the room.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.start_smart_home_appliance_discovery)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#start_smart_home_appliance_discovery)
        """
    def tag_resource(self, *, Arn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds metadata tags to a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#tag_resource)
        """
    def untag_resource(self, *, Arn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes metadata tags from a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#untag_resource)
        """
    def update_address_book(
        self, *, AddressBookArn: str, Name: str = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        Updates address book details by the address book ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_address_book)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#update_address_book)
        """
    def update_business_report_schedule(
        self,
        *,
        ScheduleArn: str,
        S3BucketName: str = None,
        S3KeyPrefix: str = None,
        Format: BusinessReportFormatType = None,
        ScheduleName: str = None,
        Recurrence: "BusinessReportRecurrenceTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates the configuration of the report delivery schedule with the specified
        schedule ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_business_report_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#update_business_report_schedule)
        """
    def update_conference_provider(
        self,
        *,
        ConferenceProviderArn: str,
        ConferenceProviderType: ConferenceProviderTypeType,
        MeetingSetting: "MeetingSettingTypeDef",
        IPDialIn: "IPDialInTypeDef" = None,
        PSTNDialIn: "PSTNDialInTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates an existing conference provider's settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_conference_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#update_conference_provider)
        """
    def update_contact(
        self,
        *,
        ContactArn: str,
        DisplayName: str = None,
        FirstName: str = None,
        LastName: str = None,
        PhoneNumber: str = None,
        PhoneNumbers: List["PhoneNumberTypeDef"] = None,
        SipAddresses: List["SipAddressTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Updates the contact details by the contact ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#update_contact)
        """
    def update_device(self, *, DeviceArn: str = None, DeviceName: str = None) -> Dict[str, Any]:
        """
        Updates the device name by device ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#update_device)
        """
    def update_gateway(
        self,
        *,
        GatewayArn: str,
        Name: str = None,
        Description: str = None,
        SoftwareVersion: str = None
    ) -> Dict[str, Any]:
        """
        Updates the details of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#update_gateway)
        """
    def update_gateway_group(
        self, *, GatewayGroupArn: str, Name: str = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        Updates the details of a gateway group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_gateway_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#update_gateway_group)
        """
    def update_network_profile(
        self,
        *,
        NetworkProfileArn: str,
        NetworkProfileName: str = None,
        Description: str = None,
        CurrentPassword: str = None,
        NextPassword: str = None,
        CertificateAuthorityArn: str = None,
        TrustAnchors: List[str] = None
    ) -> Dict[str, Any]:
        """
        Updates a network profile by the network profile ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_network_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#update_network_profile)
        """
    def update_profile(
        self,
        *,
        ProfileArn: str = None,
        ProfileName: str = None,
        IsDefault: bool = None,
        Timezone: str = None,
        Address: str = None,
        DistanceUnit: DistanceUnitType = None,
        TemperatureUnit: TemperatureUnitType = None,
        WakeWord: WakeWordType = None,
        Locale: str = None,
        SetupModeDisabled: bool = None,
        MaxVolumeLimit: int = None,
        PSTNEnabled: bool = None,
        DataRetentionOptIn: bool = None,
        MeetingRoomConfiguration: "UpdateMeetingRoomConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates an existing room profile by room profile ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#update_profile)
        """
    def update_room(
        self,
        *,
        RoomArn: str = None,
        RoomName: str = None,
        Description: str = None,
        ProviderCalendarId: str = None,
        ProfileArn: str = None
    ) -> Dict[str, Any]:
        """
        Updates room details by room ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#update_room)
        """
    def update_skill_group(
        self, *, SkillGroupArn: str = None, SkillGroupName: str = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        Updates skill group details by skill group ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_skill_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/client.html#update_skill_group)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_business_report_schedules"]
    ) -> ListBusinessReportSchedulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListBusinessReportSchedules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/paginators.html#listbusinessreportschedulespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_conference_providers"]
    ) -> ListConferenceProvidersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListConferenceProviders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/paginators.html#listconferenceproviderspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_events"]
    ) -> ListDeviceEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListDeviceEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/paginators.html#listdeviceeventspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_skills"]) -> ListSkillsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkills)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/paginators.html#listskillspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_skills_store_categories"]
    ) -> ListSkillsStoreCategoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkillsStoreCategories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/paginators.html#listskillsstorecategoriespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_skills_store_skills_by_category"]
    ) -> ListSkillsStoreSkillsByCategoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkillsStoreSkillsByCategory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/paginators.html#listskillsstoreskillsbycategorypaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_smart_home_appliances"]
    ) -> ListSmartHomeAppliancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSmartHomeAppliances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/paginators.html#listsmarthomeappliancespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_tags"]) -> ListTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListTags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/paginators.html#listtagspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["search_devices"]) -> SearchDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchDevices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/paginators.html#searchdevicespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["search_profiles"]) -> SearchProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/paginators.html#searchprofilespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["search_rooms"]) -> SearchRoomsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchRooms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/paginators.html#searchroomspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["search_skill_groups"]
    ) -> SearchSkillGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchSkillGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/paginators.html#searchskillgroupspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["search_users"]) -> SearchUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchUsers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/paginators.html#searchuserspaginator)
        """
