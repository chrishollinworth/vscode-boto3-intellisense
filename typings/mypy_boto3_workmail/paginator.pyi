# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for workmail service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_workmail import WorkMailClient
    from mypy_boto3_workmail.paginator import (
        ListAliasesPaginator,
        ListGroupMembersPaginator,
        ListGroupsPaginator,
        ListMailboxPermissionsPaginator,
        ListOrganizationsPaginator,
        ListResourceDelegatesPaginator,
        ListResourcesPaginator,
        ListUsersPaginator,
    )

    client: WorkMailClient = boto3.client("workmail")

    list_aliases_paginator: ListAliasesPaginator = client.get_paginator("list_aliases")
    list_group_members_paginator: ListGroupMembersPaginator = client.get_paginator("list_group_members")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    list_mailbox_permissions_paginator: ListMailboxPermissionsPaginator = client.get_paginator("list_mailbox_permissions")
    list_organizations_paginator: ListOrganizationsPaginator = client.get_paginator("list_organizations")
    list_resource_delegates_paginator: ListResourceDelegatesPaginator = client.get_paginator("list_resource_delegates")
    list_resources_paginator: ListResourcesPaginator = client.get_paginator("list_resources")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_workmail.type_defs import (
    ListAliasesResponseTypeDef,
    ListGroupMembersResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListMailboxPermissionsResponseTypeDef,
    ListOrganizationsResponseTypeDef,
    ListResourceDelegatesResponseTypeDef,
    ListResourcesResponseTypeDef,
    ListUsersResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListAliasesPaginator",
    "ListGroupMembersPaginator",
    "ListGroupsPaginator",
    "ListMailboxPermissionsPaginator",
    "ListOrganizationsPaginator",
    "ListResourceDelegatesPaginator",
    "ListResourcesPaginator",
    "ListUsersPaginator",
)


class ListAliasesPaginator(Boto3Paginator):
    """
    [Paginator.ListAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workmail.html#WorkMail.Paginator.ListAliases)
    """

    def paginate(
        self, OrganizationId: str, EntityId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAliasesResponseTypeDef]:
        """
        [ListAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workmail.html#WorkMail.Paginator.ListAliases.paginate)
        """


class ListGroupMembersPaginator(Boto3Paginator):
    """
    [Paginator.ListGroupMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workmail.html#WorkMail.Paginator.ListGroupMembers)
    """

    def paginate(
        self, OrganizationId: str, GroupId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupMembersResponseTypeDef]:
        """
        [ListGroupMembers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workmail.html#WorkMail.Paginator.ListGroupMembers.paginate)
        """


class ListGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workmail.html#WorkMail.Paginator.ListGroups)
    """

    def paginate(
        self, OrganizationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupsResponseTypeDef]:
        """
        [ListGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workmail.html#WorkMail.Paginator.ListGroups.paginate)
        """


class ListMailboxPermissionsPaginator(Boto3Paginator):
    """
    [Paginator.ListMailboxPermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workmail.html#WorkMail.Paginator.ListMailboxPermissions)
    """

    def paginate(
        self, OrganizationId: str, EntityId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMailboxPermissionsResponseTypeDef]:
        """
        [ListMailboxPermissions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workmail.html#WorkMail.Paginator.ListMailboxPermissions.paginate)
        """


class ListOrganizationsPaginator(Boto3Paginator):
    """
    [Paginator.ListOrganizations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workmail.html#WorkMail.Paginator.ListOrganizations)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOrganizationsResponseTypeDef]:
        """
        [ListOrganizations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workmail.html#WorkMail.Paginator.ListOrganizations.paginate)
        """


class ListResourceDelegatesPaginator(Boto3Paginator):
    """
    [Paginator.ListResourceDelegates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workmail.html#WorkMail.Paginator.ListResourceDelegates)
    """

    def paginate(
        self, OrganizationId: str, ResourceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceDelegatesResponseTypeDef]:
        """
        [ListResourceDelegates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workmail.html#WorkMail.Paginator.ListResourceDelegates.paginate)
        """


class ListResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workmail.html#WorkMail.Paginator.ListResources)
    """

    def paginate(
        self, OrganizationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourcesResponseTypeDef]:
        """
        [ListResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workmail.html#WorkMail.Paginator.ListResources.paginate)
        """


class ListUsersPaginator(Boto3Paginator):
    """
    [Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workmail.html#WorkMail.Paginator.ListUsers)
    """

    def paginate(
        self, OrganizationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUsersResponseTypeDef]:
        """
        [ListUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workmail.html#WorkMail.Paginator.ListUsers.paginate)
        """
