"""
Type annotations for workmail service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_workmail.client import WorkMailClient
    from mypy_boto3_workmail.paginator import (
        ListAliasesPaginator,
        ListAvailabilityConfigurationsPaginator,
        ListGroupMembersPaginator,
        ListGroupsPaginator,
        ListMailboxPermissionsPaginator,
        ListOrganizationsPaginator,
        ListPersonalAccessTokensPaginator,
        ListResourceDelegatesPaginator,
        ListResourcesPaginator,
        ListUsersPaginator,
    )

    session = Session()
    client: WorkMailClient = session.client("workmail")

    list_aliases_paginator: ListAliasesPaginator = client.get_paginator("list_aliases")
    list_availability_configurations_paginator: ListAvailabilityConfigurationsPaginator = client.get_paginator("list_availability_configurations")
    list_group_members_paginator: ListGroupMembersPaginator = client.get_paginator("list_group_members")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    list_mailbox_permissions_paginator: ListMailboxPermissionsPaginator = client.get_paginator("list_mailbox_permissions")
    list_organizations_paginator: ListOrganizationsPaginator = client.get_paginator("list_organizations")
    list_personal_access_tokens_paginator: ListPersonalAccessTokensPaginator = client.get_paginator("list_personal_access_tokens")
    list_resource_delegates_paginator: ListResourceDelegatesPaginator = client.get_paginator("list_resource_delegates")
    list_resources_paginator: ListResourcesPaginator = client.get_paginator("list_resources")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAliasesRequestPaginateTypeDef,
    ListAliasesResponseTypeDef,
    ListAvailabilityConfigurationsRequestPaginateTypeDef,
    ListAvailabilityConfigurationsResponseTypeDef,
    ListGroupMembersRequestPaginateTypeDef,
    ListGroupMembersResponseTypeDef,
    ListGroupsRequestPaginateTypeDef,
    ListGroupsResponseTypeDef,
    ListMailboxPermissionsRequestPaginateTypeDef,
    ListMailboxPermissionsResponseTypeDef,
    ListOrganizationsRequestPaginateTypeDef,
    ListOrganizationsResponseTypeDef,
    ListPersonalAccessTokensRequestPaginateTypeDef,
    ListPersonalAccessTokensResponseTypeDef,
    ListResourceDelegatesRequestPaginateTypeDef,
    ListResourceDelegatesResponseTypeDef,
    ListResourcesRequestPaginateTypeDef,
    ListResourcesResponseTypeDef,
    ListUsersRequestPaginateTypeDef,
    ListUsersResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAliasesPaginator",
    "ListAvailabilityConfigurationsPaginator",
    "ListGroupMembersPaginator",
    "ListGroupsPaginator",
    "ListMailboxPermissionsPaginator",
    "ListOrganizationsPaginator",
    "ListPersonalAccessTokensPaginator",
    "ListResourceDelegatesPaginator",
    "ListResourcesPaginator",
    "ListUsersPaginator",
)

if TYPE_CHECKING:
    _ListAliasesPaginatorBase = Paginator[ListAliasesResponseTypeDef]
else:
    _ListAliasesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAliasesPaginator(_ListAliasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListAliases.html#WorkMail.Paginator.ListAliases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listaliasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAliasesRequestPaginateTypeDef]
    ) -> PageIterator[ListAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListAliases.html#WorkMail.Paginator.ListAliases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listaliasespaginator)
        """

if TYPE_CHECKING:
    _ListAvailabilityConfigurationsPaginatorBase = Paginator[
        ListAvailabilityConfigurationsResponseTypeDef
    ]
else:
    _ListAvailabilityConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAvailabilityConfigurationsPaginator(_ListAvailabilityConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListAvailabilityConfigurations.html#WorkMail.Paginator.ListAvailabilityConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listavailabilityconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAvailabilityConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListAvailabilityConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListAvailabilityConfigurations.html#WorkMail.Paginator.ListAvailabilityConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listavailabilityconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListGroupMembersPaginatorBase = Paginator[ListGroupMembersResponseTypeDef]
else:
    _ListGroupMembersPaginatorBase = Paginator  # type: ignore[assignment]

class ListGroupMembersPaginator(_ListGroupMembersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListGroupMembers.html#WorkMail.Paginator.ListGroupMembers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listgroupmemberspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGroupMembersRequestPaginateTypeDef]
    ) -> PageIterator[ListGroupMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListGroupMembers.html#WorkMail.Paginator.ListGroupMembers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listgroupmemberspaginator)
        """

if TYPE_CHECKING:
    _ListGroupsPaginatorBase = Paginator[ListGroupsResponseTypeDef]
else:
    _ListGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListGroupsPaginator(_ListGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListGroups.html#WorkMail.Paginator.ListGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListGroups.html#WorkMail.Paginator.ListGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listgroupspaginator)
        """

if TYPE_CHECKING:
    _ListMailboxPermissionsPaginatorBase = Paginator[ListMailboxPermissionsResponseTypeDef]
else:
    _ListMailboxPermissionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMailboxPermissionsPaginator(_ListMailboxPermissionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListMailboxPermissions.html#WorkMail.Paginator.ListMailboxPermissions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listmailboxpermissionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMailboxPermissionsRequestPaginateTypeDef]
    ) -> PageIterator[ListMailboxPermissionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListMailboxPermissions.html#WorkMail.Paginator.ListMailboxPermissions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listmailboxpermissionspaginator)
        """

if TYPE_CHECKING:
    _ListOrganizationsPaginatorBase = Paginator[ListOrganizationsResponseTypeDef]
else:
    _ListOrganizationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOrganizationsPaginator(_ListOrganizationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListOrganizations.html#WorkMail.Paginator.ListOrganizations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listorganizationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOrganizationsRequestPaginateTypeDef]
    ) -> PageIterator[ListOrganizationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListOrganizations.html#WorkMail.Paginator.ListOrganizations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listorganizationspaginator)
        """

if TYPE_CHECKING:
    _ListPersonalAccessTokensPaginatorBase = Paginator[ListPersonalAccessTokensResponseTypeDef]
else:
    _ListPersonalAccessTokensPaginatorBase = Paginator  # type: ignore[assignment]

class ListPersonalAccessTokensPaginator(_ListPersonalAccessTokensPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListPersonalAccessTokens.html#WorkMail.Paginator.ListPersonalAccessTokens)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listpersonalaccesstokenspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPersonalAccessTokensRequestPaginateTypeDef]
    ) -> PageIterator[ListPersonalAccessTokensResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListPersonalAccessTokens.html#WorkMail.Paginator.ListPersonalAccessTokens.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listpersonalaccesstokenspaginator)
        """

if TYPE_CHECKING:
    _ListResourceDelegatesPaginatorBase = Paginator[ListResourceDelegatesResponseTypeDef]
else:
    _ListResourceDelegatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceDelegatesPaginator(_ListResourceDelegatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListResourceDelegates.html#WorkMail.Paginator.ListResourceDelegates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listresourcedelegatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceDelegatesRequestPaginateTypeDef]
    ) -> PageIterator[ListResourceDelegatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListResourceDelegates.html#WorkMail.Paginator.ListResourceDelegates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listresourcedelegatespaginator)
        """

if TYPE_CHECKING:
    _ListResourcesPaginatorBase = Paginator[ListResourcesResponseTypeDef]
else:
    _ListResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourcesPaginator(_ListResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListResources.html#WorkMail.Paginator.ListResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListResources.html#WorkMail.Paginator.ListResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listresourcespaginator)
        """

if TYPE_CHECKING:
    _ListUsersPaginatorBase = Paginator[ListUsersResponseTypeDef]
else:
    _ListUsersPaginatorBase = Paginator  # type: ignore[assignment]

class ListUsersPaginator(_ListUsersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListUsers.html#WorkMail.Paginator.ListUsers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listuserspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUsersRequestPaginateTypeDef]
    ) -> PageIterator[ListUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail/paginator/ListUsers.html#WorkMail.Paginator.ListUsers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listuserspaginator)
        """
