"""
Type annotations for identitystore service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_identitystore import IdentityStoreClient
    from mypy_boto3_identitystore.paginator import (
        ListGroupMembershipsPaginator,
        ListGroupMembershipsForMemberPaginator,
        ListGroupsPaginator,
        ListUsersPaginator,
    )

    client: IdentityStoreClient = boto3.client("identitystore")

    list_group_memberships_paginator: ListGroupMembershipsPaginator = client.get_paginator("list_group_memberships")
    list_group_memberships_for_member_paginator: ListGroupMembershipsForMemberPaginator = client.get_paginator("list_group_memberships_for_member")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    FilterTypeDef,
    ListGroupMembershipsForMemberResponseTypeDef,
    ListGroupMembershipsResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListUsersResponseTypeDef,
    MemberIdTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListGroupMembershipsPaginator",
    "ListGroupMembershipsForMemberPaginator",
    "ListGroupsPaginator",
    "ListUsersPaginator",
)

class ListGroupMembershipsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/identitystore.html#IdentityStore.Paginator.ListGroupMemberships)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators.html#listgroupmembershipspaginator)
    """

    def paginate(
        self, *, IdentityStoreId: str, GroupId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupMembershipsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/identitystore.html#IdentityStore.Paginator.ListGroupMemberships.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators.html#listgroupmembershipspaginator)
        """

class ListGroupMembershipsForMemberPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/identitystore.html#IdentityStore.Paginator.ListGroupMembershipsForMember)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators.html#listgroupmembershipsformemberpaginator)
    """

    def paginate(
        self,
        *,
        IdentityStoreId: str,
        MemberId: "MemberIdTypeDef",
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupMembershipsForMemberResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/identitystore.html#IdentityStore.Paginator.ListGroupMembershipsForMember.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators.html#listgroupmembershipsformemberpaginator)
        """

class ListGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/identitystore.html#IdentityStore.Paginator.ListGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators.html#listgroupspaginator)
    """

    def paginate(
        self,
        *,
        IdentityStoreId: str,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/identitystore.html#IdentityStore.Paginator.ListGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators.html#listgroupspaginator)
        """

class ListUsersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/identitystore.html#IdentityStore.Paginator.ListUsers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators.html#listuserspaginator)
    """

    def paginate(
        self,
        *,
        IdentityStoreId: str,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/identitystore.html#IdentityStore.Paginator.ListUsers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/paginators.html#listuserspaginator)
        """
