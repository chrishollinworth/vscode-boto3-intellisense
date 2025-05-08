"""
Type annotations for ds-data service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ds_data.client import DirectoryServiceDataClient

    session = Session()
    client: DirectoryServiceDataClient = session.client("ds-data")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListGroupMembersPaginator,
    ListGroupsForMemberPaginator,
    ListGroupsPaginator,
    ListUsersPaginator,
    SearchGroupsPaginator,
    SearchUsersPaginator,
)
from .type_defs import (
    AddGroupMemberRequestTypeDef,
    CreateGroupRequestTypeDef,
    CreateGroupResultTypeDef,
    CreateUserRequestTypeDef,
    CreateUserResultTypeDef,
    DeleteGroupRequestTypeDef,
    DeleteUserRequestTypeDef,
    DescribeGroupRequestTypeDef,
    DescribeGroupResultTypeDef,
    DescribeUserRequestTypeDef,
    DescribeUserResultTypeDef,
    DisableUserRequestTypeDef,
    ListGroupMembersRequestTypeDef,
    ListGroupMembersResultTypeDef,
    ListGroupsForMemberRequestTypeDef,
    ListGroupsForMemberResultTypeDef,
    ListGroupsRequestTypeDef,
    ListGroupsResultTypeDef,
    ListUsersRequestTypeDef,
    ListUsersResultTypeDef,
    RemoveGroupMemberRequestTypeDef,
    SearchGroupsRequestTypeDef,
    SearchGroupsResultTypeDef,
    SearchUsersRequestTypeDef,
    SearchUsersResultTypeDef,
    UpdateGroupRequestTypeDef,
    UpdateUserRequestTypeDef,
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

__all__ = ("DirectoryServiceDataClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DirectoryUnavailableException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class DirectoryServiceDataClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data.html#DirectoryServiceData.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DirectoryServiceDataClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data.html#DirectoryServiceData.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#generate_presigned_url)
        """

    def add_group_member(self, **kwargs: Unpack[AddGroupMemberRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds an existing user, group, or computer as a group member.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/add_group_member.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#add_group_member)
        """

    def create_group(self, **kwargs: Unpack[CreateGroupRequestTypeDef]) -> CreateGroupResultTypeDef:
        """
        Creates a new group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/create_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#create_group)
        """

    def create_user(self, **kwargs: Unpack[CreateUserRequestTypeDef]) -> CreateUserResultTypeDef:
        """
        Creates a new user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/create_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#create_user)
        """

    def delete_group(self, **kwargs: Unpack[DeleteGroupRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/delete_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#delete_group)
        """

    def delete_user(self, **kwargs: Unpack[DeleteUserRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/delete_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#delete_user)
        """

    def describe_group(
        self, **kwargs: Unpack[DescribeGroupRequestTypeDef]
    ) -> DescribeGroupResultTypeDef:
        """
        Returns information about a specific group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/describe_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#describe_group)
        """

    def describe_user(
        self, **kwargs: Unpack[DescribeUserRequestTypeDef]
    ) -> DescribeUserResultTypeDef:
        """
        Returns information about a specific user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/describe_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#describe_user)
        """

    def disable_user(self, **kwargs: Unpack[DisableUserRequestTypeDef]) -> Dict[str, Any]:
        """
        Deactivates an active user account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/disable_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#disable_user)
        """

    def list_group_members(
        self, **kwargs: Unpack[ListGroupMembersRequestTypeDef]
    ) -> ListGroupMembersResultTypeDef:
        """
        Returns member information for the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/list_group_members.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#list_group_members)
        """

    def list_groups(self, **kwargs: Unpack[ListGroupsRequestTypeDef]) -> ListGroupsResultTypeDef:
        """
        Returns group information for the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/list_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#list_groups)
        """

    def list_groups_for_member(
        self, **kwargs: Unpack[ListGroupsForMemberRequestTypeDef]
    ) -> ListGroupsForMemberResultTypeDef:
        """
        Returns group information for the specified member.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/list_groups_for_member.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#list_groups_for_member)
        """

    def list_users(self, **kwargs: Unpack[ListUsersRequestTypeDef]) -> ListUsersResultTypeDef:
        """
        Returns user information for the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/list_users.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#list_users)
        """

    def remove_group_member(
        self, **kwargs: Unpack[RemoveGroupMemberRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes a member from a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/remove_group_member.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#remove_group_member)
        """

    def search_groups(
        self, **kwargs: Unpack[SearchGroupsRequestTypeDef]
    ) -> SearchGroupsResultTypeDef:
        """
        Searches the specified directory for a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/search_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#search_groups)
        """

    def search_users(self, **kwargs: Unpack[SearchUsersRequestTypeDef]) -> SearchUsersResultTypeDef:
        """
        Searches the specified directory for a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/search_users.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#search_users)
        """

    def update_group(self, **kwargs: Unpack[UpdateGroupRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates group information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/update_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#update_group)
        """

    def update_user(self, **kwargs: Unpack[UpdateUserRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates user information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/update_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#update_user)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_group_members"]
    ) -> ListGroupMembersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_groups_for_member"]
    ) -> ListGroupsForMemberPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_groups"]
    ) -> ListGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_users"]
    ) -> ListUsersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_groups"]
    ) -> SearchGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_users"]
    ) -> SearchUsersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/client/#get_paginator)
        """
