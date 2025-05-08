"""
Type annotations for sso service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_sso.client import SSOClient
    from mypy_boto3_sso.paginator import (
        ListAccountRolesPaginator,
        ListAccountsPaginator,
    )

    session = Session()
    client: SSOClient = session.client("sso")

    list_account_roles_paginator: ListAccountRolesPaginator = client.get_paginator("list_account_roles")
    list_accounts_paginator: ListAccountsPaginator = client.get_paginator("list_accounts")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAccountRolesRequestPaginateTypeDef,
    ListAccountRolesResponseTypeDef,
    ListAccountsRequestPaginateTypeDef,
    ListAccountsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListAccountRolesPaginator", "ListAccountsPaginator")

if TYPE_CHECKING:
    _ListAccountRolesPaginatorBase = Paginator[ListAccountRolesResponseTypeDef]
else:
    _ListAccountRolesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccountRolesPaginator(_ListAccountRolesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso/paginator/ListAccountRoles.html#SSO.Paginator.ListAccountRoles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso/paginators/#listaccountrolespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccountRolesRequestPaginateTypeDef]
    ) -> PageIterator[ListAccountRolesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso/paginator/ListAccountRoles.html#SSO.Paginator.ListAccountRoles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso/paginators/#listaccountrolespaginator)
        """

if TYPE_CHECKING:
    _ListAccountsPaginatorBase = Paginator[ListAccountsResponseTypeDef]
else:
    _ListAccountsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccountsPaginator(_ListAccountsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso/paginator/ListAccounts.html#SSO.Paginator.ListAccounts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso/paginators/#listaccountspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccountsRequestPaginateTypeDef]
    ) -> PageIterator[ListAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso/paginator/ListAccounts.html#SSO.Paginator.ListAccounts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso/paginators/#listaccountspaginator)
        """
