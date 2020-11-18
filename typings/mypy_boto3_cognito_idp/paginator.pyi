# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for cognito-idp service client paginators.

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

from mypy_boto3_cognito_idp.type_defs import (
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
    [Paginator.AdminListGroupsForUser documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListGroupsForUser)
    """

    def paginate(
        self, Username: str, UserPoolId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[AdminListGroupsForUserResponseTypeDef]:
        """
        [AdminListGroupsForUser.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListGroupsForUser.paginate)
        """


class AdminListUserAuthEventsPaginator(Boto3Paginator):
    """
    [Paginator.AdminListUserAuthEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListUserAuthEvents)
    """

    def paginate(
        self, UserPoolId: str, Username: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[AdminListUserAuthEventsResponseTypeDef]:
        """
        [AdminListUserAuthEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListUserAuthEvents.paginate)
        """


class ListGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListGroups)
    """

    def paginate(
        self, UserPoolId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupsResponseTypeDef]:
        """
        [ListGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListGroups.paginate)
        """


class ListIdentityProvidersPaginator(Boto3Paginator):
    """
    [Paginator.ListIdentityProviders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListIdentityProviders)
    """

    def paginate(
        self, UserPoolId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIdentityProvidersResponseTypeDef]:
        """
        [ListIdentityProviders.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListIdentityProviders.paginate)
        """


class ListResourceServersPaginator(Boto3Paginator):
    """
    [Paginator.ListResourceServers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListResourceServers)
    """

    def paginate(
        self, UserPoolId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceServersResponseTypeDef]:
        """
        [ListResourceServers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListResourceServers.paginate)
        """


class ListUserPoolClientsPaginator(Boto3Paginator):
    """
    [Paginator.ListUserPoolClients documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPoolClients)
    """

    def paginate(
        self, UserPoolId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUserPoolClientsResponseTypeDef]:
        """
        [ListUserPoolClients.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPoolClients.paginate)
        """


class ListUserPoolsPaginator(Boto3Paginator):
    """
    [Paginator.ListUserPools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPools)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUserPoolsResponseTypeDef]:
        """
        [ListUserPools.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPools.paginate)
        """


class ListUsersPaginator(Boto3Paginator):
    """
    [Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsers)
    """

    def paginate(
        self,
        UserPoolId: str,
        AttributesToGet: List[str] = None,
        Filter: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListUsersResponseTypeDef]:
        """
        [ListUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsers.paginate)
        """


class ListUsersInGroupPaginator(Boto3Paginator):
    """
    [Paginator.ListUsersInGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsersInGroup)
    """

    def paginate(
        self, UserPoolId: str, GroupName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUsersInGroupResponseTypeDef]:
        """
        [ListUsersInGroup.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsersInGroup.paginate)
        """
