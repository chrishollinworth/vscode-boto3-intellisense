"""
Type annotations for ds-data service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ds_data.client import DirectoryServiceDataClient
    from mypy_boto3_ds_data.paginator import (
        ListGroupMembersPaginator,
        ListGroupsForMemberPaginator,
        ListGroupsPaginator,
        ListUsersPaginator,
        SearchGroupsPaginator,
        SearchUsersPaginator,
    )

    session = Session()
    client: DirectoryServiceDataClient = session.client("ds-data")

    list_group_members_paginator: ListGroupMembersPaginator = client.get_paginator("list_group_members")
    list_groups_for_member_paginator: ListGroupsForMemberPaginator = client.get_paginator("list_groups_for_member")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    search_groups_paginator: SearchGroupsPaginator = client.get_paginator("search_groups")
    search_users_paginator: SearchUsersPaginator = client.get_paginator("search_users")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListGroupMembersRequestPaginateTypeDef,
    ListGroupMembersResultTypeDef,
    ListGroupsForMemberRequestPaginateTypeDef,
    ListGroupsForMemberResultTypeDef,
    ListGroupsRequestPaginateTypeDef,
    ListGroupsResultTypeDef,
    ListUsersRequestPaginateTypeDef,
    ListUsersResultTypeDef,
    SearchGroupsRequestPaginateTypeDef,
    SearchGroupsResultTypeDef,
    SearchUsersRequestPaginateTypeDef,
    SearchUsersResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListGroupMembersPaginator",
    "ListGroupsForMemberPaginator",
    "ListGroupsPaginator",
    "ListUsersPaginator",
    "SearchGroupsPaginator",
    "SearchUsersPaginator",
)

if TYPE_CHECKING:
    _ListGroupMembersPaginatorBase = Paginator[ListGroupMembersResultTypeDef]
else:
    _ListGroupMembersPaginatorBase = Paginator  # type: ignore[assignment]

class ListGroupMembersPaginator(_ListGroupMembersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/paginator/ListGroupMembers.html#DirectoryServiceData.Paginator.ListGroupMembers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/paginators/#listgroupmemberspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGroupMembersRequestPaginateTypeDef]
    ) -> PageIterator[ListGroupMembersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/paginator/ListGroupMembers.html#DirectoryServiceData.Paginator.ListGroupMembers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/paginators/#listgroupmemberspaginator)
        """

if TYPE_CHECKING:
    _ListGroupsForMemberPaginatorBase = Paginator[ListGroupsForMemberResultTypeDef]
else:
    _ListGroupsForMemberPaginatorBase = Paginator  # type: ignore[assignment]

class ListGroupsForMemberPaginator(_ListGroupsForMemberPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/paginator/ListGroupsForMember.html#DirectoryServiceData.Paginator.ListGroupsForMember)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/paginators/#listgroupsformemberpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGroupsForMemberRequestPaginateTypeDef]
    ) -> PageIterator[ListGroupsForMemberResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/paginator/ListGroupsForMember.html#DirectoryServiceData.Paginator.ListGroupsForMember.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/paginators/#listgroupsformemberpaginator)
        """

if TYPE_CHECKING:
    _ListGroupsPaginatorBase = Paginator[ListGroupsResultTypeDef]
else:
    _ListGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListGroupsPaginator(_ListGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/paginator/ListGroups.html#DirectoryServiceData.Paginator.ListGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/paginators/#listgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/paginator/ListGroups.html#DirectoryServiceData.Paginator.ListGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/paginators/#listgroupspaginator)
        """

if TYPE_CHECKING:
    _ListUsersPaginatorBase = Paginator[ListUsersResultTypeDef]
else:
    _ListUsersPaginatorBase = Paginator  # type: ignore[assignment]

class ListUsersPaginator(_ListUsersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/paginator/ListUsers.html#DirectoryServiceData.Paginator.ListUsers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/paginators/#listuserspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUsersRequestPaginateTypeDef]
    ) -> PageIterator[ListUsersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/paginator/ListUsers.html#DirectoryServiceData.Paginator.ListUsers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/paginators/#listuserspaginator)
        """

if TYPE_CHECKING:
    _SearchGroupsPaginatorBase = Paginator[SearchGroupsResultTypeDef]
else:
    _SearchGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchGroupsPaginator(_SearchGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/paginator/SearchGroups.html#DirectoryServiceData.Paginator.SearchGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/paginators/#searchgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchGroupsRequestPaginateTypeDef]
    ) -> PageIterator[SearchGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/paginator/SearchGroups.html#DirectoryServiceData.Paginator.SearchGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/paginators/#searchgroupspaginator)
        """

if TYPE_CHECKING:
    _SearchUsersPaginatorBase = Paginator[SearchUsersResultTypeDef]
else:
    _SearchUsersPaginatorBase = Paginator  # type: ignore[assignment]

class SearchUsersPaginator(_SearchUsersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/paginator/SearchUsers.html#DirectoryServiceData.Paginator.SearchUsers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/paginators/#searchuserspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchUsersRequestPaginateTypeDef]
    ) -> PageIterator[SearchUsersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds-data/paginator/SearchUsers.html#DirectoryServiceData.Paginator.SearchUsers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/paginators/#searchuserspaginator)
        """
