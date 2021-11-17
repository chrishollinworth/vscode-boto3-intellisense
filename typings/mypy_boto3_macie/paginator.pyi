"""
Type annotations for macie service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/paginators.html)

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

from .type_defs import (
    ListMemberAccountsResultTypeDef,
    ListS3ResourcesResultTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListMemberAccountsPaginator", "ListS3ResourcesPaginator")

class ListMemberAccountsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/macie.html#Macie.Paginator.ListMemberAccounts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/paginators.html#listmemberaccountspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMemberAccountsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/macie.html#Macie.Paginator.ListMemberAccounts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/paginators.html#listmemberaccountspaginator)
        """

class ListS3ResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/macie.html#Macie.Paginator.ListS3Resources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/paginators.html#lists3resourcespaginator)
    """

    def paginate(
        self, *, memberAccountId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListS3ResourcesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/macie.html#Macie.Paginator.ListS3Resources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/paginators.html#lists3resourcespaginator)
        """
