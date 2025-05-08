"""
Type annotations for chime service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_chime.client import ChimeClient

    session = Session()
    client: ChimeClient = session.client("chime")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListAccountsPaginator, ListUsersPaginator
from .type_defs import (
    AssociatePhoneNumberWithUserRequestTypeDef,
    AssociateSigninDelegateGroupsWithAccountRequestTypeDef,
    BatchCreateRoomMembershipRequestTypeDef,
    BatchCreateRoomMembershipResponseTypeDef,
    BatchDeletePhoneNumberRequestTypeDef,
    BatchDeletePhoneNumberResponseTypeDef,
    BatchSuspendUserRequestTypeDef,
    BatchSuspendUserResponseTypeDef,
    BatchUnsuspendUserRequestTypeDef,
    BatchUnsuspendUserResponseTypeDef,
    BatchUpdatePhoneNumberRequestTypeDef,
    BatchUpdatePhoneNumberResponseTypeDef,
    BatchUpdateUserRequestTypeDef,
    BatchUpdateUserResponseTypeDef,
    CreateAccountRequestTypeDef,
    CreateAccountResponseTypeDef,
    CreateBotRequestTypeDef,
    CreateBotResponseTypeDef,
    CreateMeetingDialOutRequestTypeDef,
    CreateMeetingDialOutResponseTypeDef,
    CreatePhoneNumberOrderRequestTypeDef,
    CreatePhoneNumberOrderResponseTypeDef,
    CreateRoomMembershipRequestTypeDef,
    CreateRoomMembershipResponseTypeDef,
    CreateRoomRequestTypeDef,
    CreateRoomResponseTypeDef,
    CreateUserRequestTypeDef,
    CreateUserResponseTypeDef,
    DeleteAccountRequestTypeDef,
    DeleteEventsConfigurationRequestTypeDef,
    DeletePhoneNumberRequestTypeDef,
    DeleteRoomMembershipRequestTypeDef,
    DeleteRoomRequestTypeDef,
    DisassociatePhoneNumberFromUserRequestTypeDef,
    DisassociateSigninDelegateGroupsFromAccountRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAccountRequestTypeDef,
    GetAccountResponseTypeDef,
    GetAccountSettingsRequestTypeDef,
    GetAccountSettingsResponseTypeDef,
    GetBotRequestTypeDef,
    GetBotResponseTypeDef,
    GetEventsConfigurationRequestTypeDef,
    GetEventsConfigurationResponseTypeDef,
    GetGlobalSettingsResponseTypeDef,
    GetPhoneNumberOrderRequestTypeDef,
    GetPhoneNumberOrderResponseTypeDef,
    GetPhoneNumberRequestTypeDef,
    GetPhoneNumberResponseTypeDef,
    GetPhoneNumberSettingsResponseTypeDef,
    GetRetentionSettingsRequestTypeDef,
    GetRetentionSettingsResponseTypeDef,
    GetRoomRequestTypeDef,
    GetRoomResponseTypeDef,
    GetUserRequestTypeDef,
    GetUserResponseTypeDef,
    GetUserSettingsRequestTypeDef,
    GetUserSettingsResponseTypeDef,
    InviteUsersRequestTypeDef,
    InviteUsersResponseTypeDef,
    ListAccountsRequestTypeDef,
    ListAccountsResponseTypeDef,
    ListBotsRequestTypeDef,
    ListBotsResponseTypeDef,
    ListPhoneNumberOrdersRequestTypeDef,
    ListPhoneNumberOrdersResponseTypeDef,
    ListPhoneNumbersRequestTypeDef,
    ListPhoneNumbersResponseTypeDef,
    ListRoomMembershipsRequestTypeDef,
    ListRoomMembershipsResponseTypeDef,
    ListRoomsRequestTypeDef,
    ListRoomsResponseTypeDef,
    ListSupportedPhoneNumberCountriesRequestTypeDef,
    ListSupportedPhoneNumberCountriesResponseTypeDef,
    ListUsersRequestTypeDef,
    ListUsersResponseTypeDef,
    LogoutUserRequestTypeDef,
    PutEventsConfigurationRequestTypeDef,
    PutEventsConfigurationResponseTypeDef,
    PutRetentionSettingsRequestTypeDef,
    PutRetentionSettingsResponseTypeDef,
    RedactConversationMessageRequestTypeDef,
    RedactRoomMessageRequestTypeDef,
    RegenerateSecurityTokenRequestTypeDef,
    RegenerateSecurityTokenResponseTypeDef,
    ResetPersonalPINRequestTypeDef,
    ResetPersonalPINResponseTypeDef,
    RestorePhoneNumberRequestTypeDef,
    RestorePhoneNumberResponseTypeDef,
    SearchAvailablePhoneNumbersRequestTypeDef,
    SearchAvailablePhoneNumbersResponseTypeDef,
    UpdateAccountRequestTypeDef,
    UpdateAccountResponseTypeDef,
    UpdateAccountSettingsRequestTypeDef,
    UpdateBotRequestTypeDef,
    UpdateBotResponseTypeDef,
    UpdateGlobalSettingsRequestTypeDef,
    UpdatePhoneNumberRequestTypeDef,
    UpdatePhoneNumberResponseTypeDef,
    UpdatePhoneNumberSettingsRequestTypeDef,
    UpdateRoomMembershipRequestTypeDef,
    UpdateRoomMembershipResponseTypeDef,
    UpdateRoomRequestTypeDef,
    UpdateRoomResponseTypeDef,
    UpdateUserRequestTypeDef,
    UpdateUserResponseTypeDef,
    UpdateUserSettingsRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("ChimeClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ServiceFailureException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottledClientException: Type[BotocoreClientError]
    UnauthorizedClientException: Type[BotocoreClientError]
    UnprocessableEntityException: Type[BotocoreClientError]

class ChimeClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ChimeClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#generate_presigned_url)
        """

    def associate_phone_number_with_user(
        self, **kwargs: Unpack[AssociatePhoneNumberWithUserRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates a phone number with the specified Amazon Chime user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/associate_phone_number_with_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#associate_phone_number_with_user)
        """

    def associate_signin_delegate_groups_with_account(
        self, **kwargs: Unpack[AssociateSigninDelegateGroupsWithAccountRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates the specified sign-in delegate groups with the specified Amazon
        Chime account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/associate_signin_delegate_groups_with_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#associate_signin_delegate_groups_with_account)
        """

    def batch_create_room_membership(
        self, **kwargs: Unpack[BatchCreateRoomMembershipRequestTypeDef]
    ) -> BatchCreateRoomMembershipResponseTypeDef:
        """
        Adds up to 50 members to a chat room in an Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/batch_create_room_membership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#batch_create_room_membership)
        """

    def batch_delete_phone_number(
        self, **kwargs: Unpack[BatchDeletePhoneNumberRequestTypeDef]
    ) -> BatchDeletePhoneNumberResponseTypeDef:
        """
        Moves phone numbers into the <b>Deletion queue</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/batch_delete_phone_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#batch_delete_phone_number)
        """

    def batch_suspend_user(
        self, **kwargs: Unpack[BatchSuspendUserRequestTypeDef]
    ) -> BatchSuspendUserResponseTypeDef:
        """
        Suspends up to 50 users from a <code>Team</code> or <code>EnterpriseLWA</code>
        Amazon Chime account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/batch_suspend_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#batch_suspend_user)
        """

    def batch_unsuspend_user(
        self, **kwargs: Unpack[BatchUnsuspendUserRequestTypeDef]
    ) -> BatchUnsuspendUserResponseTypeDef:
        """
        Removes the suspension from up to 50 previously suspended users for the
        specified Amazon Chime <code>EnterpriseLWA</code> account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/batch_unsuspend_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#batch_unsuspend_user)
        """

    def batch_update_phone_number(
        self, **kwargs: Unpack[BatchUpdatePhoneNumberRequestTypeDef]
    ) -> BatchUpdatePhoneNumberResponseTypeDef:
        """
        Updates phone number product types or calling names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/batch_update_phone_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#batch_update_phone_number)
        """

    def batch_update_user(
        self, **kwargs: Unpack[BatchUpdateUserRequestTypeDef]
    ) -> BatchUpdateUserResponseTypeDef:
        """
        Updates user details within the <a>UpdateUserRequestItem</a> object for up to
        20 users for the specified Amazon Chime account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/batch_update_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#batch_update_user)
        """

    def create_account(
        self, **kwargs: Unpack[CreateAccountRequestTypeDef]
    ) -> CreateAccountResponseTypeDef:
        """
        Creates an Amazon Chime account under the administrator's AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/create_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#create_account)
        """

    def create_bot(self, **kwargs: Unpack[CreateBotRequestTypeDef]) -> CreateBotResponseTypeDef:
        """
        Creates a bot for an Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/create_bot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#create_bot)
        """

    def create_meeting_dial_out(
        self, **kwargs: Unpack[CreateMeetingDialOutRequestTypeDef]
    ) -> CreateMeetingDialOutResponseTypeDef:
        """
        Uses the join token and call metadata in a meeting request (From number, To
        number, and so forth) to initiate an outbound call to a public switched
        telephone network (PSTN) and join them into a Chime meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/create_meeting_dial_out.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#create_meeting_dial_out)
        """

    def create_phone_number_order(
        self, **kwargs: Unpack[CreatePhoneNumberOrderRequestTypeDef]
    ) -> CreatePhoneNumberOrderResponseTypeDef:
        """
        Creates an order for phone numbers to be provisioned.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/create_phone_number_order.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#create_phone_number_order)
        """

    def create_room(self, **kwargs: Unpack[CreateRoomRequestTypeDef]) -> CreateRoomResponseTypeDef:
        """
        Creates a chat room for the specified Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/create_room.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#create_room)
        """

    def create_room_membership(
        self, **kwargs: Unpack[CreateRoomMembershipRequestTypeDef]
    ) -> CreateRoomMembershipResponseTypeDef:
        """
        Adds a member to a chat room in an Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/create_room_membership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#create_room_membership)
        """

    def create_user(self, **kwargs: Unpack[CreateUserRequestTypeDef]) -> CreateUserResponseTypeDef:
        """
        Creates a user under the specified Amazon Chime account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/create_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#create_user)
        """

    def delete_account(self, **kwargs: Unpack[DeleteAccountRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified Amazon Chime account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/delete_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#delete_account)
        """

    def delete_events_configuration(
        self, **kwargs: Unpack[DeleteEventsConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the events configuration that allows a bot to receive outgoing events.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/delete_events_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#delete_events_configuration)
        """

    def delete_phone_number(
        self, **kwargs: Unpack[DeletePhoneNumberRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Moves the specified phone number into the <b>Deletion queue</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/delete_phone_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#delete_phone_number)
        """

    def delete_room(
        self, **kwargs: Unpack[DeleteRoomRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a chat room in an Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/delete_room.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#delete_room)
        """

    def delete_room_membership(
        self, **kwargs: Unpack[DeleteRoomMembershipRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes a member from a chat room in an Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/delete_room_membership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#delete_room_membership)
        """

    def disassociate_phone_number_from_user(
        self, **kwargs: Unpack[DisassociatePhoneNumberFromUserRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates the primary provisioned phone number from the specified Amazon
        Chime user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/disassociate_phone_number_from_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#disassociate_phone_number_from_user)
        """

    def disassociate_signin_delegate_groups_from_account(
        self, **kwargs: Unpack[DisassociateSigninDelegateGroupsFromAccountRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates the specified sign-in delegate groups from the specified Amazon
        Chime account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/disassociate_signin_delegate_groups_from_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#disassociate_signin_delegate_groups_from_account)
        """

    def get_account(self, **kwargs: Unpack[GetAccountRequestTypeDef]) -> GetAccountResponseTypeDef:
        """
        Retrieves details for the specified Amazon Chime account, such as account type
        and supported licenses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/get_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#get_account)
        """

    def get_account_settings(
        self, **kwargs: Unpack[GetAccountSettingsRequestTypeDef]
    ) -> GetAccountSettingsResponseTypeDef:
        """
        Retrieves account settings for the specified Amazon Chime account ID, such as
        remote control and dialout settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/get_account_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#get_account_settings)
        """

    def get_bot(self, **kwargs: Unpack[GetBotRequestTypeDef]) -> GetBotResponseTypeDef:
        """
        Retrieves details for the specified bot, such as bot email address, bot type,
        status, and display name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/get_bot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#get_bot)
        """

    def get_events_configuration(
        self, **kwargs: Unpack[GetEventsConfigurationRequestTypeDef]
    ) -> GetEventsConfigurationResponseTypeDef:
        """
        Gets details for an events configuration that allows a bot to receive outgoing
        events, such as an HTTPS endpoint or Lambda function ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/get_events_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#get_events_configuration)
        """

    def get_global_settings(self) -> GetGlobalSettingsResponseTypeDef:
        """
        Retrieves global settings for the administrator's AWS account, such as Amazon
        Chime Business Calling and Amazon Chime Voice Connector settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/get_global_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#get_global_settings)
        """

    def get_phone_number(
        self, **kwargs: Unpack[GetPhoneNumberRequestTypeDef]
    ) -> GetPhoneNumberResponseTypeDef:
        """
        Retrieves details for the specified phone number ID, such as associations,
        capabilities, and product type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/get_phone_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#get_phone_number)
        """

    def get_phone_number_order(
        self, **kwargs: Unpack[GetPhoneNumberOrderRequestTypeDef]
    ) -> GetPhoneNumberOrderResponseTypeDef:
        """
        Retrieves details for the specified phone number order, such as the order
        creation timestamp, phone numbers in E.164 format, product type, and order
        status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/get_phone_number_order.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#get_phone_number_order)
        """

    def get_phone_number_settings(self) -> GetPhoneNumberSettingsResponseTypeDef:
        """
        Retrieves the phone number settings for the administrator's AWS account, such
        as the default outbound calling name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/get_phone_number_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#get_phone_number_settings)
        """

    def get_retention_settings(
        self, **kwargs: Unpack[GetRetentionSettingsRequestTypeDef]
    ) -> GetRetentionSettingsResponseTypeDef:
        """
        Gets the retention settings for the specified Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/get_retention_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#get_retention_settings)
        """

    def get_room(self, **kwargs: Unpack[GetRoomRequestTypeDef]) -> GetRoomResponseTypeDef:
        """
        Retrieves room details, such as the room name, for a room in an Amazon Chime
        Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/get_room.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#get_room)
        """

    def get_user(self, **kwargs: Unpack[GetUserRequestTypeDef]) -> GetUserResponseTypeDef:
        """
        Retrieves details for the specified user ID, such as primary email address,
        license type,and personal meeting PIN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/get_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#get_user)
        """

    def get_user_settings(
        self, **kwargs: Unpack[GetUserSettingsRequestTypeDef]
    ) -> GetUserSettingsResponseTypeDef:
        """
        Retrieves settings for the specified user ID, such as any associated phone
        number settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/get_user_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#get_user_settings)
        """

    def invite_users(
        self, **kwargs: Unpack[InviteUsersRequestTypeDef]
    ) -> InviteUsersResponseTypeDef:
        """
        Sends email to a maximum of 50 users, inviting them to the specified Amazon
        Chime <code>Team</code> account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/invite_users.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#invite_users)
        """

    def list_accounts(
        self, **kwargs: Unpack[ListAccountsRequestTypeDef]
    ) -> ListAccountsResponseTypeDef:
        """
        Lists the Amazon Chime accounts under the administrator's AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/list_accounts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#list_accounts)
        """

    def list_bots(self, **kwargs: Unpack[ListBotsRequestTypeDef]) -> ListBotsResponseTypeDef:
        """
        Lists the bots associated with the administrator's Amazon Chime Enterprise
        account ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/list_bots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#list_bots)
        """

    def list_phone_number_orders(
        self, **kwargs: Unpack[ListPhoneNumberOrdersRequestTypeDef]
    ) -> ListPhoneNumberOrdersResponseTypeDef:
        """
        Lists the phone number orders for the administrator's Amazon Chime account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/list_phone_number_orders.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#list_phone_number_orders)
        """

    def list_phone_numbers(
        self, **kwargs: Unpack[ListPhoneNumbersRequestTypeDef]
    ) -> ListPhoneNumbersResponseTypeDef:
        """
        Lists the phone numbers for the specified Amazon Chime account, Amazon Chime
        user, Amazon Chime Voice Connector, or Amazon Chime Voice Connector group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/list_phone_numbers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#list_phone_numbers)
        """

    def list_room_memberships(
        self, **kwargs: Unpack[ListRoomMembershipsRequestTypeDef]
    ) -> ListRoomMembershipsResponseTypeDef:
        """
        Lists the membership details for the specified room in an Amazon Chime
        Enterprise account, such as the members' IDs, email addresses, and names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/list_room_memberships.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#list_room_memberships)
        """

    def list_rooms(self, **kwargs: Unpack[ListRoomsRequestTypeDef]) -> ListRoomsResponseTypeDef:
        """
        Lists the room details for the specified Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/list_rooms.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#list_rooms)
        """

    def list_supported_phone_number_countries(
        self, **kwargs: Unpack[ListSupportedPhoneNumberCountriesRequestTypeDef]
    ) -> ListSupportedPhoneNumberCountriesResponseTypeDef:
        """
        Lists supported phone number countries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/list_supported_phone_number_countries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#list_supported_phone_number_countries)
        """

    def list_users(self, **kwargs: Unpack[ListUsersRequestTypeDef]) -> ListUsersResponseTypeDef:
        """
        Lists the users that belong to the specified Amazon Chime account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/list_users.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#list_users)
        """

    def logout_user(self, **kwargs: Unpack[LogoutUserRequestTypeDef]) -> Dict[str, Any]:
        """
        Logs out the specified user from all of the devices they are currently logged
        into.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/logout_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#logout_user)
        """

    def put_events_configuration(
        self, **kwargs: Unpack[PutEventsConfigurationRequestTypeDef]
    ) -> PutEventsConfigurationResponseTypeDef:
        """
        Creates an events configuration that allows a bot to receive outgoing events
        sent by Amazon Chime.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/put_events_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#put_events_configuration)
        """

    def put_retention_settings(
        self, **kwargs: Unpack[PutRetentionSettingsRequestTypeDef]
    ) -> PutRetentionSettingsResponseTypeDef:
        """
        Puts retention settings for the specified Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/put_retention_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#put_retention_settings)
        """

    def redact_conversation_message(
        self, **kwargs: Unpack[RedactConversationMessageRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Redacts the specified message from the specified Amazon Chime conversation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/redact_conversation_message.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#redact_conversation_message)
        """

    def redact_room_message(
        self, **kwargs: Unpack[RedactRoomMessageRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Redacts the specified message from the specified Amazon Chime channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/redact_room_message.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#redact_room_message)
        """

    def regenerate_security_token(
        self, **kwargs: Unpack[RegenerateSecurityTokenRequestTypeDef]
    ) -> RegenerateSecurityTokenResponseTypeDef:
        """
        Regenerates the security token for a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/regenerate_security_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#regenerate_security_token)
        """

    def reset_personal_pin(
        self, **kwargs: Unpack[ResetPersonalPINRequestTypeDef]
    ) -> ResetPersonalPINResponseTypeDef:
        """
        Resets the personal meeting PIN for the specified user on an Amazon Chime
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/reset_personal_pin.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#reset_personal_pin)
        """

    def restore_phone_number(
        self, **kwargs: Unpack[RestorePhoneNumberRequestTypeDef]
    ) -> RestorePhoneNumberResponseTypeDef:
        """
        Moves a phone number from the <b>Deletion queue</b> back into the phone number
        <b>Inventory</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/restore_phone_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#restore_phone_number)
        """

    def search_available_phone_numbers(
        self, **kwargs: Unpack[SearchAvailablePhoneNumbersRequestTypeDef]
    ) -> SearchAvailablePhoneNumbersResponseTypeDef:
        """
        Searches for phone numbers that can be ordered.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/search_available_phone_numbers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#search_available_phone_numbers)
        """

    def update_account(
        self, **kwargs: Unpack[UpdateAccountRequestTypeDef]
    ) -> UpdateAccountResponseTypeDef:
        """
        Updates account details for the specified Amazon Chime account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/update_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#update_account)
        """

    def update_account_settings(
        self, **kwargs: Unpack[UpdateAccountSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the settings for the specified Amazon Chime account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/update_account_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#update_account_settings)
        """

    def update_bot(self, **kwargs: Unpack[UpdateBotRequestTypeDef]) -> UpdateBotResponseTypeDef:
        """
        Updates the status of the specified bot, such as starting or stopping the bot
        from running in your Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/update_bot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#update_bot)
        """

    def update_global_settings(
        self, **kwargs: Unpack[UpdateGlobalSettingsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates global settings for the administrator's AWS account, such as Amazon
        Chime Business Calling and Amazon Chime Voice Connector settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/update_global_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#update_global_settings)
        """

    def update_phone_number(
        self, **kwargs: Unpack[UpdatePhoneNumberRequestTypeDef]
    ) -> UpdatePhoneNumberResponseTypeDef:
        """
        Updates phone number details, such as product type or calling name, for the
        specified phone number ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/update_phone_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#update_phone_number)
        """

    def update_phone_number_settings(
        self, **kwargs: Unpack[UpdatePhoneNumberSettingsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the phone number settings for the administrator's AWS account, such as
        the default outbound calling name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/update_phone_number_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#update_phone_number_settings)
        """

    def update_room(self, **kwargs: Unpack[UpdateRoomRequestTypeDef]) -> UpdateRoomResponseTypeDef:
        """
        Updates room details, such as the room name, for a room in an Amazon Chime
        Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/update_room.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#update_room)
        """

    def update_room_membership(
        self, **kwargs: Unpack[UpdateRoomMembershipRequestTypeDef]
    ) -> UpdateRoomMembershipResponseTypeDef:
        """
        Updates room membership details, such as the member role, for a room in an
        Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/update_room_membership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#update_room_membership)
        """

    def update_user(self, **kwargs: Unpack[UpdateUserRequestTypeDef]) -> UpdateUserResponseTypeDef:
        """
        Updates user details for a specified user ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/update_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#update_user)
        """

    def update_user_settings(
        self, **kwargs: Unpack[UpdateUserSettingsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the settings for the specified user, such as phone number settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/update_user_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#update_user_settings)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_accounts"]
    ) -> ListAccountsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_users"]
    ) -> ListUsersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/client/#get_paginator)
        """
