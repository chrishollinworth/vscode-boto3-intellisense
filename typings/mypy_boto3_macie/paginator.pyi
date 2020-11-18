# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for macie service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_macie import MacieClient
    from mypy_boto3_macie.paginator import (
        ListMemberAccountsPaginator,
        ListS3ResourcesPaginator,
    )

    client: MacieClient = boto3.client("macie")

    list_member_accounts_paginator: ListMemberAccountsPaginator = client.get_paginator("list_member_accounts")
    list_s3_resources_paginator: ListS3ResourcesPaginator = client.get_paginator("list_s3_resources")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_macie.type_defs import (
    ListMemberAccountsResultTypeDef,
    ListS3ResourcesResultTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListMemberAccountsPaginator", "ListS3ResourcesPaginator")


class ListMemberAccountsPaginator(Boto3Paginator):
    """
    [Paginator.ListMemberAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie.html#Macie.Paginator.ListMemberAccounts)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMemberAccountsResultTypeDef]:
        """
        [ListMemberAccounts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie.html#Macie.Paginator.ListMemberAccounts.paginate)
        """


class ListS3ResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListS3Resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie.html#Macie.Paginator.ListS3Resources)
    """

    def paginate(
        self, memberAccountId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListS3ResourcesResultTypeDef]:
        """
        [ListS3Resources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie.html#Macie.Paginator.ListS3Resources.paginate)
        """
