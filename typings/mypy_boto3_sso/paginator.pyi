# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for sso service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_sso import SSOClient
    from mypy_boto3_sso.paginator import (
        ListAccountRolesPaginator,
        ListAccountsPaginator,
    )

    client: SSOClient = boto3.client("sso")

    list_account_roles_paginator: ListAccountRolesPaginator = client.get_paginator("list_account_roles")
    list_accounts_paginator: ListAccountsPaginator = client.get_paginator("list_accounts")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_sso.type_defs import (
    ListAccountRolesResponseTypeDef,
    ListAccountsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListAccountRolesPaginator", "ListAccountsPaginator")


class ListAccountRolesPaginator(Boto3Paginator):
    """
    [Paginator.ListAccountRoles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso.html#SSO.Paginator.ListAccountRoles)
    """

    def paginate(
        self, accessToken: str, accountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountRolesResponseTypeDef]:
        """
        [ListAccountRoles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso.html#SSO.Paginator.ListAccountRoles.paginate)
        """


class ListAccountsPaginator(Boto3Paginator):
    """
    [Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso.html#SSO.Paginator.ListAccounts)
    """

    def paginate(
        self, accessToken: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountsResponseTypeDef]:
        """
        [ListAccounts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso.html#SSO.Paginator.ListAccounts.paginate)
        """
