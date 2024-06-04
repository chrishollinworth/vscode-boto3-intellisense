"""
Type annotations for chime service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_chime import ChimeClient
    from mypy_boto3_chime.paginator import (
        ListAccountsPaginator,
        ListUsersPaginator,
    )

    client: ChimeClient = boto3.client("chime")

    list_accounts_paginator: ListAccountsPaginator = client.get_paginator("list_accounts")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import UserTypeType
from .type_defs import ListAccountsResponseTypeDef, ListUsersResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListAccountsPaginator", "ListUsersPaginator")

class ListAccountsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chime.html#Chime.Paginator.ListAccounts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/paginators.html#listaccountspaginator)
    """

    def paginate(
        self,
        *,
        Name: str = None,
        UserEmail: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chime.html#Chime.Paginator.ListAccounts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/paginators.html#listaccountspaginator)
        """

class ListUsersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chime.html#Chime.Paginator.ListUsers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/paginators.html#listuserspaginator)
    """

    def paginate(
        self,
        *,
        AccountId: str,
        UserEmail: str = None,
        UserType: UserTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chime.html#Chime.Paginator.ListUsers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/paginators.html#listuserspaginator)
        """
