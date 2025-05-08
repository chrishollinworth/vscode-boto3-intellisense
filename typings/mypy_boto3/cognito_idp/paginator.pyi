"""
Type annotations for cognito-idp service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cognito_idp.client import CognitoIdentityProviderClient
    from mypy_boto3_cognito_idp.paginator import (
        AdminListGroupsForUserPaginator,
        AdminListUserAuthEventsPaginator,
        ListGroupsPaginator,
        ListIdentityProvidersPaginator,
        ListResourceServersPaginator,
        ListUserPoolClientsPaginator,
        ListUserPoolsPaginator,
        ListUsersInGroupPaginator,
        ListUsersPaginator,
    )

    session = Session()
    client: CognitoIdentityProviderClient = session.client("cognito-idp")

    admin_list_groups_for_user_paginator: AdminListGroupsForUserPaginator = client.get_paginator("admin_list_groups_for_user")
    admin_list_user_auth_events_paginator: AdminListUserAuthEventsPaginator = client.get_paginator("admin_list_user_auth_events")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    list_identity_providers_paginator: ListIdentityProvidersPaginator = client.get_paginator("list_identity_providers")
    list_resource_servers_paginator: ListResourceServersPaginator = client.get_paginator("list_resource_servers")
    list_user_pool_clients_paginator: ListUserPoolClientsPaginator = client.get_paginator("list_user_pool_clients")
    list_user_pools_paginator: ListUserPoolsPaginator = client.get_paginator("list_user_pools")
    list_users_in_group_paginator: ListUsersInGroupPaginator = client.get_paginator("list_users_in_group")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    AdminListGroupsForUserRequestPaginateTypeDef,
    AdminListGroupsForUserResponseTypeDef,
    AdminListUserAuthEventsRequestPaginateTypeDef,
    AdminListUserAuthEventsResponseTypeDef,
    ListGroupsRequestPaginateTypeDef,
    ListGroupsResponseTypeDef,
    ListIdentityProvidersRequestPaginateTypeDef,
    ListIdentityProvidersResponseTypeDef,
    ListResourceServersRequestPaginateTypeDef,
    ListResourceServersResponseTypeDef,
    ListUserPoolClientsRequestPaginateTypeDef,
    ListUserPoolClientsResponseTypeDef,
    ListUserPoolsRequestPaginateTypeDef,
    ListUserPoolsResponseTypeDef,
    ListUsersInGroupRequestPaginateTypeDef,
    ListUsersInGroupResponseTypeDef,
    ListUsersRequestPaginateTypeDef,
    ListUsersResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "AdminListGroupsForUserPaginator",
    "AdminListUserAuthEventsPaginator",
    "ListGroupsPaginator",
    "ListIdentityProvidersPaginator",
    "ListResourceServersPaginator",
    "ListUserPoolClientsPaginator",
    "ListUserPoolsPaginator",
    "ListUsersInGroupPaginator",
    "ListUsersPaginator",
)

if TYPE_CHECKING:
    _AdminListGroupsForUserPaginatorBase = Paginator[AdminListGroupsForUserResponseTypeDef]
else:
    _AdminListGroupsForUserPaginatorBase = Paginator  # type: ignore[assignment]

class AdminListGroupsForUserPaginator(_AdminListGroupsForUserPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/paginator/AdminListGroupsForUser.html#CognitoIdentityProvider.Paginator.AdminListGroupsForUser)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators/#adminlistgroupsforuserpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[AdminListGroupsForUserRequestPaginateTypeDef]
    ) -> PageIterator[AdminListGroupsForUserResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/paginator/AdminListGroupsForUser.html#CognitoIdentityProvider.Paginator.AdminListGroupsForUser.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators/#adminlistgroupsforuserpaginator)
        """

if TYPE_CHECKING:
    _AdminListUserAuthEventsPaginatorBase = Paginator[AdminListUserAuthEventsResponseTypeDef]
else:
    _AdminListUserAuthEventsPaginatorBase = Paginator  # type: ignore[assignment]

class AdminListUserAuthEventsPaginator(_AdminListUserAuthEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/paginator/AdminListUserAuthEvents.html#CognitoIdentityProvider.Paginator.AdminListUserAuthEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators/#adminlistuserautheventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[AdminListUserAuthEventsRequestPaginateTypeDef]
    ) -> PageIterator[AdminListUserAuthEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/paginator/AdminListUserAuthEvents.html#CognitoIdentityProvider.Paginator.AdminListUserAuthEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators/#adminlistuserautheventspaginator)
        """

if TYPE_CHECKING:
    _ListGroupsPaginatorBase = Paginator[ListGroupsResponseTypeDef]
else:
    _ListGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListGroupsPaginator(_ListGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/paginator/ListGroups.html#CognitoIdentityProvider.Paginator.ListGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators/#listgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/paginator/ListGroups.html#CognitoIdentityProvider.Paginator.ListGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators/#listgroupspaginator)
        """

if TYPE_CHECKING:
    _ListIdentityProvidersPaginatorBase = Paginator[ListIdentityProvidersResponseTypeDef]
else:
    _ListIdentityProvidersPaginatorBase = Paginator  # type: ignore[assignment]

class ListIdentityProvidersPaginator(_ListIdentityProvidersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/paginator/ListIdentityProviders.html#CognitoIdentityProvider.Paginator.ListIdentityProviders)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators/#listidentityproviderspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIdentityProvidersRequestPaginateTypeDef]
    ) -> PageIterator[ListIdentityProvidersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/paginator/ListIdentityProviders.html#CognitoIdentityProvider.Paginator.ListIdentityProviders.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators/#listidentityproviderspaginator)
        """

if TYPE_CHECKING:
    _ListResourceServersPaginatorBase = Paginator[ListResourceServersResponseTypeDef]
else:
    _ListResourceServersPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceServersPaginator(_ListResourceServersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/paginator/ListResourceServers.html#CognitoIdentityProvider.Paginator.ListResourceServers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators/#listresourceserverspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceServersRequestPaginateTypeDef]
    ) -> PageIterator[ListResourceServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/paginator/ListResourceServers.html#CognitoIdentityProvider.Paginator.ListResourceServers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators/#listresourceserverspaginator)
        """

if TYPE_CHECKING:
    _ListUserPoolClientsPaginatorBase = Paginator[ListUserPoolClientsResponseTypeDef]
else:
    _ListUserPoolClientsPaginatorBase = Paginator  # type: ignore[assignment]

class ListUserPoolClientsPaginator(_ListUserPoolClientsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/paginator/ListUserPoolClients.html#CognitoIdentityProvider.Paginator.ListUserPoolClients)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators/#listuserpoolclientspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUserPoolClientsRequestPaginateTypeDef]
    ) -> PageIterator[ListUserPoolClientsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/paginator/ListUserPoolClients.html#CognitoIdentityProvider.Paginator.ListUserPoolClients.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators/#listuserpoolclientspaginator)
        """

if TYPE_CHECKING:
    _ListUserPoolsPaginatorBase = Paginator[ListUserPoolsResponseTypeDef]
else:
    _ListUserPoolsPaginatorBase = Paginator  # type: ignore[assignment]

class ListUserPoolsPaginator(_ListUserPoolsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/paginator/ListUserPools.html#CognitoIdentityProvider.Paginator.ListUserPools)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators/#listuserpoolspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUserPoolsRequestPaginateTypeDef]
    ) -> PageIterator[ListUserPoolsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/paginator/ListUserPools.html#CognitoIdentityProvider.Paginator.ListUserPools.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators/#listuserpoolspaginator)
        """

if TYPE_CHECKING:
    _ListUsersInGroupPaginatorBase = Paginator[ListUsersInGroupResponseTypeDef]
else:
    _ListUsersInGroupPaginatorBase = Paginator  # type: ignore[assignment]

class ListUsersInGroupPaginator(_ListUsersInGroupPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/paginator/ListUsersInGroup.html#CognitoIdentityProvider.Paginator.ListUsersInGroup)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators/#listusersingrouppaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUsersInGroupRequestPaginateTypeDef]
    ) -> PageIterator[ListUsersInGroupResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/paginator/ListUsersInGroup.html#CognitoIdentityProvider.Paginator.ListUsersInGroup.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators/#listusersingrouppaginator)
        """

if TYPE_CHECKING:
    _ListUsersPaginatorBase = Paginator[ListUsersResponseTypeDef]
else:
    _ListUsersPaginatorBase = Paginator  # type: ignore[assignment]

class ListUsersPaginator(_ListUsersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/paginator/ListUsers.html#CognitoIdentityProvider.Paginator.ListUsers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators/#listuserspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUsersRequestPaginateTypeDef]
    ) -> PageIterator[ListUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/paginator/ListUsers.html#CognitoIdentityProvider.Paginator.ListUsers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators/#listuserspaginator)
        """
