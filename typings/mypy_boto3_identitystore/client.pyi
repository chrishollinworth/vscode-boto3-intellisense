"""
Type annotations for identitystore service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_identitystore import IdentityStoreClient

    client: IdentityStoreClient = boto3.client("identitystore")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListGroupMembershipsForMemberPaginator,
    ListGroupMembershipsPaginator,
    ListGroupsPaginator,
    ListUsersPaginator,
)
from .type_defs import (
    AddressTypeDef,
    AlternateIdentifierTypeDef,
    AttributeOperationTypeDef,
    CreateGroupMembershipResponseTypeDef,
    CreateGroupResponseTypeDef,
    CreateUserResponseTypeDef,
    DescribeGroupMembershipResponseTypeDef,
    DescribeGroupResponseTypeDef,
    DescribeUserResponseTypeDef,
    EmailTypeDef,
    FilterTypeDef,
    GetGroupIdResponseTypeDef,
    GetGroupMembershipIdResponseTypeDef,
    GetUserIdResponseTypeDef,
    IsMemberInGroupsResponseTypeDef,
    ListGroupMembershipsForMemberResponseTypeDef,
    ListGroupMembershipsResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListUsersResponseTypeDef,
    MemberIdTypeDef,
    NameTypeDef,
    PhoneNumberTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("IdentityStoreClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class IdentityStoreClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IdentityStoreClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#close)
        """
    def create_group(
        self, *, IdentityStoreId: str, DisplayName: str = None, Description: str = None
    ) -> CreateGroupResponseTypeDef:
        """
        Creates a group within the specified identity store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.create_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#create_group)
        """
    def create_group_membership(
        self, *, IdentityStoreId: str, GroupId: str, MemberId: "MemberIdTypeDef"
    ) -> CreateGroupMembershipResponseTypeDef:
        """
        Creates a relationship between a member and a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.create_group_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#create_group_membership)
        """
    def create_user(
        self,
        *,
        IdentityStoreId: str,
        UserName: str = None,
        Name: "NameTypeDef" = None,
        DisplayName: str = None,
        NickName: str = None,
        ProfileUrl: str = None,
        Emails: List["EmailTypeDef"] = None,
        Addresses: List["AddressTypeDef"] = None,
        PhoneNumbers: List["PhoneNumberTypeDef"] = None,
        UserType: str = None,
        Title: str = None,
        PreferredLanguage: str = None,
        Locale: str = None,
        Timezone: str = None
    ) -> CreateUserResponseTypeDef:
        """
        Creates a user within the specified identity store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#create_user)
        """
    def delete_group(self, *, IdentityStoreId: str, GroupId: str) -> Dict[str, Any]:
        """
        Delete a group within an identity store given `GroupId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.delete_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#delete_group)
        """
    def delete_group_membership(self, *, IdentityStoreId: str, MembershipId: str) -> Dict[str, Any]:
        """
        Delete a membership within a group given `MembershipId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.delete_group_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#delete_group_membership)
        """
    def delete_user(self, *, IdentityStoreId: str, UserId: str) -> Dict[str, Any]:
        """
        Deletes a user within an identity store given `UserId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#delete_user)
        """
    def describe_group(self, *, IdentityStoreId: str, GroupId: str) -> DescribeGroupResponseTypeDef:
        """
        Retrieves the group metadata and attributes from `GroupId` in an identity store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.describe_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#describe_group)
        """
    def describe_group_membership(
        self, *, IdentityStoreId: str, MembershipId: str
    ) -> DescribeGroupMembershipResponseTypeDef:
        """
        Retrieves membership metadata and attributes from `MembershipId` in an identity
        store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.describe_group_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#describe_group_membership)
        """
    def describe_user(self, *, IdentityStoreId: str, UserId: str) -> DescribeUserResponseTypeDef:
        """
        Retrieves the user metadata and attributes from the `UserId` in an identity
        store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.describe_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#describe_user)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#generate_presigned_url)
        """
    def get_group_id(
        self, *, IdentityStoreId: str, AlternateIdentifier: "AlternateIdentifierTypeDef"
    ) -> GetGroupIdResponseTypeDef:
        """
        Retrieves `GroupId` in an identity store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.get_group_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#get_group_id)
        """
    def get_group_membership_id(
        self, *, IdentityStoreId: str, GroupId: str, MemberId: "MemberIdTypeDef"
    ) -> GetGroupMembershipIdResponseTypeDef:
        """
        Retrieves the `MembershipId` in an identity store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.get_group_membership_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#get_group_membership_id)
        """
    def get_user_id(
        self, *, IdentityStoreId: str, AlternateIdentifier: "AlternateIdentifierTypeDef"
    ) -> GetUserIdResponseTypeDef:
        """
        Retrieves the `UserId` in an identity store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.get_user_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#get_user_id)
        """
    def is_member_in_groups(
        self, *, IdentityStoreId: str, MemberId: "MemberIdTypeDef", GroupIds: List[str]
    ) -> IsMemberInGroupsResponseTypeDef:
        """
        Checks the user's membership in all requested groups and returns if the member
        exists in all queried groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.is_member_in_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#is_member_in_groups)
        """
    def list_group_memberships(
        self, *, IdentityStoreId: str, GroupId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListGroupMembershipsResponseTypeDef:
        """
        For the specified group in the specified identity store, returns the list of all
        `GroupMembership` objects and returns results in paginated form.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.list_group_memberships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#list_group_memberships)
        """
    def list_group_memberships_for_member(
        self,
        *,
        IdentityStoreId: str,
        MemberId: "MemberIdTypeDef",
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListGroupMembershipsForMemberResponseTypeDef:
        """
        For the specified member in the specified identity store, returns the list of
        all `GroupMembership` objects and returns results in paginated form.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.list_group_memberships_for_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#list_group_memberships_for_member)
        """
    def list_groups(
        self,
        *,
        IdentityStoreId: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["FilterTypeDef"] = None
    ) -> ListGroupsResponseTypeDef:
        """
        Lists all groups in the identity store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.list_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#list_groups)
        """
    def list_users(
        self,
        *,
        IdentityStoreId: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["FilterTypeDef"] = None
    ) -> ListUsersResponseTypeDef:
        """
        Lists all users in the identity store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.list_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#list_users)
        """
    def update_group(
        self, *, IdentityStoreId: str, GroupId: str, Operations: List["AttributeOperationTypeDef"]
    ) -> Dict[str, Any]:
        """
        For the specified group in the specified identity store, updates the group
        metadata and attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.update_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#update_group)
        """
    def update_user(
        self, *, IdentityStoreId: str, UserId: str, Operations: List["AttributeOperationTypeDef"]
    ) -> Dict[str, Any]:
        """
        For the specified user in the specified identity store, updates the user
        metadata and attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Client.update_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#update_user)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_group_memberships"]
    ) -> ListGroupMembershipsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Paginator.ListGroupMemberships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators.html#listgroupmembershipspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_group_memberships_for_member"]
    ) -> ListGroupMembershipsForMemberPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Paginator.ListGroupMembershipsForMember)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators.html#listgroupmembershipsformemberpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_groups"]) -> ListGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Paginator.ListGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators.html#listgroupspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/identitystore.html#IdentityStore.Paginator.ListUsers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators.html#listuserspaginator)
        """
