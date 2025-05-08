"""
Type annotations for chime service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_chime.client import ChimeClient
    from mypy_boto3_chime.paginator import (
        ListAccountsPaginator,
        ListUsersPaginator,
    )

    session = Session()
    client: ChimeClient = session.client("chime")

    list_accounts_paginator: ListAccountsPaginator = client.get_paginator("list_accounts")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAccountsRequestPaginateTypeDef,
    ListAccountsResponseTypeDef,
    ListUsersRequestPaginateTypeDef,
    ListUsersResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListAccountsPaginator", "ListUsersPaginator")

if TYPE_CHECKING:
    _ListAccountsPaginatorBase = Paginator[ListAccountsResponseTypeDef]
else:
    _ListAccountsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccountsPaginator(_ListAccountsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/paginator/ListAccounts.html#Chime.Paginator.ListAccounts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/paginators/#listaccountspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccountsRequestPaginateTypeDef]
    ) -> PageIterator[ListAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/paginator/ListAccounts.html#Chime.Paginator.ListAccounts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/paginators/#listaccountspaginator)
        """

if TYPE_CHECKING:
    _ListUsersPaginatorBase = Paginator[ListUsersResponseTypeDef]
else:
    _ListUsersPaginatorBase = Paginator  # type: ignore[assignment]

class ListUsersPaginator(_ListUsersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/paginator/ListUsers.html#Chime.Paginator.ListUsers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/paginators/#listuserspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUsersRequestPaginateTypeDef]
    ) -> PageIterator[ListUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime/paginator/ListUsers.html#Chime.Paginator.ListUsers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/paginators/#listuserspaginator)
        """
