"""
Type annotations for identitystore service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_identitystore.client import IdentityStoreClient
    from mypy_boto3_identitystore.paginator import (
        ListGroupMembershipsForMemberPaginator,
        ListGroupMembershipsPaginator,
        ListGroupsPaginator,
        ListUsersPaginator,
    )

    session = Session()
    client: IdentityStoreClient = session.client("identitystore")

    list_group_memberships_for_member_paginator: ListGroupMembershipsForMemberPaginator = client.get_paginator("list_group_memberships_for_member")
    list_group_memberships_paginator: ListGroupMembershipsPaginator = client.get_paginator("list_group_memberships")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListGroupMembershipsForMemberRequestPaginateTypeDef,
    ListGroupMembershipsForMemberResponseTypeDef,
    ListGroupMembershipsRequestPaginateTypeDef,
    ListGroupMembershipsResponseTypeDef,
    ListGroupsRequestPaginateTypeDef,
    ListGroupsResponseTypeDef,
    ListUsersRequestPaginateTypeDef,
    ListUsersResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListGroupMembershipsForMemberPaginator",
    "ListGroupMembershipsPaginator",
    "ListGroupsPaginator",
    "ListUsersPaginator",
)

if TYPE_CHECKING:
    _ListGroupMembershipsForMemberPaginatorBase = Paginator[
        ListGroupMembershipsForMemberResponseTypeDef
    ]
else:
    _ListGroupMembershipsForMemberPaginatorBase = Paginator  # type: ignore[assignment]

class ListGroupMembershipsForMemberPaginator(_ListGroupMembershipsForMemberPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore/paginator/ListGroupMembershipsForMember.html#IdentityStore.Paginator.ListGroupMembershipsForMember)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators/#listgroupmembershipsformemberpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGroupMembershipsForMemberRequestPaginateTypeDef]
    ) -> PageIterator[ListGroupMembershipsForMemberResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore/paginator/ListGroupMembershipsForMember.html#IdentityStore.Paginator.ListGroupMembershipsForMember.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators/#listgroupmembershipsformemberpaginator)
        """

if TYPE_CHECKING:
    _ListGroupMembershipsPaginatorBase = Paginator[ListGroupMembershipsResponseTypeDef]
else:
    _ListGroupMembershipsPaginatorBase = Paginator  # type: ignore[assignment]

class ListGroupMembershipsPaginator(_ListGroupMembershipsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore/paginator/ListGroupMemberships.html#IdentityStore.Paginator.ListGroupMemberships)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators/#listgroupmembershipspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGroupMembershipsRequestPaginateTypeDef]
    ) -> PageIterator[ListGroupMembershipsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore/paginator/ListGroupMemberships.html#IdentityStore.Paginator.ListGroupMemberships.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators/#listgroupmembershipspaginator)
        """

if TYPE_CHECKING:
    _ListGroupsPaginatorBase = Paginator[ListGroupsResponseTypeDef]
else:
    _ListGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListGroupsPaginator(_ListGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore/paginator/ListGroups.html#IdentityStore.Paginator.ListGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators/#listgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore/paginator/ListGroups.html#IdentityStore.Paginator.ListGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators/#listgroupspaginator)
        """

if TYPE_CHECKING:
    _ListUsersPaginatorBase = Paginator[ListUsersResponseTypeDef]
else:
    _ListUsersPaginatorBase = Paginator  # type: ignore[assignment]

class ListUsersPaginator(_ListUsersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore/paginator/ListUsers.html#IdentityStore.Paginator.ListUsers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators/#listuserspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUsersRequestPaginateTypeDef]
    ) -> PageIterator[ListUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore/paginator/ListUsers.html#IdentityStore.Paginator.ListUsers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators/#listuserspaginator)
        """
