"""
Type annotations for cognito-idp service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_cognito_idp import CognitoIdentityProviderClient
    from mypy_boto3_cognito_idp.paginator import (
        AdminListGroupsForUserPaginator,
        AdminListUserAuthEventsPaginator,
        ListGroupsPaginator,
        ListIdentityProvidersPaginator,
        ListResourceServersPaginator,
        ListUserPoolClientsPaginator,
        ListUserPoolsPaginator,
        ListUsersPaginator,
        ListUsersInGroupPaginator,
    )

    client: CognitoIdentityProviderClient = boto3.client("cognito-idp")

    admin_list_groups_for_user_paginator: AdminListGroupsForUserPaginator = client.get_paginator("admin_list_groups_for_user")
    admin_list_user_auth_events_paginator: AdminListUserAuthEventsPaginator = client.get_paginator("admin_list_user_auth_events")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    list_identity_providers_paginator: ListIdentityProvidersPaginator = client.get_paginator("list_identity_providers")
    list_resource_servers_paginator: ListResourceServersPaginator = client.get_paginator("list_resource_servers")
    list_user_pool_clients_paginator: ListUserPoolClientsPaginator = client.get_paginator("list_user_pool_clients")
    list_user_pools_paginator: ListUserPoolsPaginator = client.get_paginator("list_user_pools")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    list_users_in_group_paginator: ListUsersInGroupPaginator = client.get_paginator("list_users_in_group")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    AdminListGroupsForUserResponseTypeDef,
    AdminListUserAuthEventsResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListIdentityProvidersResponseTypeDef,
    ListResourceServersResponseTypeDef,
    ListUserPoolClientsResponseTypeDef,
    ListUserPoolsResponseTypeDef,
    ListUsersInGroupResponseTypeDef,
    ListUsersResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "AdminListGroupsForUserPaginator",
    "AdminListUserAuthEventsPaginator",
    "ListGroupsPaginator",
    "ListIdentityProvidersPaginator",
    "ListResourceServersPaginator",
    "ListUserPoolClientsPaginator",
    "ListUserPoolsPaginator",
    "ListUsersPaginator",
    "ListUsersInGroupPaginator",
)

class AdminListGroupsForUserPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListGroupsForUser)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#adminlistgroupsforuserpaginator)
    """

    def paginate(
        self, *, Username: str, UserPoolId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[AdminListGroupsForUserResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListGroupsForUser.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#adminlistgroupsforuserpaginator)
        """

class AdminListUserAuthEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListUserAuthEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#adminlistuserautheventspaginator)
    """

    def paginate(
        self, *, UserPoolId: str, Username: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[AdminListUserAuthEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListUserAuthEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#adminlistuserautheventspaginator)
        """

class ListGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listgroupspaginator)
    """

    def paginate(
        self, *, UserPoolId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listgroupspaginator)
        """

class ListIdentityProvidersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListIdentityProviders)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listidentityproviderspaginator)
    """

    def paginate(
        self, *, UserPoolId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIdentityProvidersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListIdentityProviders.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listidentityproviderspaginator)
        """

class ListResourceServersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListResourceServers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listresourceserverspaginator)
    """

    def paginate(
        self, *, UserPoolId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListResourceServers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listresourceserverspaginator)
        """

class ListUserPoolClientsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPoolClients)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listuserpoolclientspaginator)
    """

    def paginate(
        self, *, UserPoolId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUserPoolClientsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPoolClients.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listuserpoolclientspaginator)
        """

class ListUserPoolsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPools)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listuserpoolspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUserPoolsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPools.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listuserpoolspaginator)
        """

class ListUsersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listuserspaginator)
    """

    def paginate(
        self,
        *,
        UserPoolId: str,
        AttributesToGet: List[str] = None,
        Filter: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listuserspaginator)
        """

class ListUsersInGroupPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsersInGroup)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listusersingrouppaginator)
    """

    def paginate(
        self, *, UserPoolId: str, GroupName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUsersInGroupResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsersInGroup.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listusersingrouppaginator)
        """
