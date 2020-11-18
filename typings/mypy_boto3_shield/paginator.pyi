# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for shield service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_shield import ShieldClient
    from mypy_boto3_shield.paginator import (
        ListAttacksPaginator,
        ListProtectionsPaginator,
    )

    client: ShieldClient = boto3.client("shield")

    list_attacks_paginator: ListAttacksPaginator = client.get_paginator("list_attacks")
    list_protections_paginator: ListProtectionsPaginator = client.get_paginator("list_protections")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_shield.type_defs import (
    ListAttacksResponseTypeDef,
    ListProtectionsResponseTypeDef,
    PaginatorConfigTypeDef,
    TimeRangeTypeDef,
)

__all__ = ("ListAttacksPaginator", "ListProtectionsPaginator")


class ListAttacksPaginator(Boto3Paginator):
    """
    [Paginator.ListAttacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Paginator.ListAttacks)
    """

    def paginate(
        self,
        ResourceArns: List[str] = None,
        StartTime: "TimeRangeTypeDef" = None,
        EndTime: "TimeRangeTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAttacksResponseTypeDef]:
        """
        [ListAttacks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Paginator.ListAttacks.paginate)
        """


class ListProtectionsPaginator(Boto3Paginator):
    """
    [Paginator.ListProtections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Paginator.ListProtections)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProtectionsResponseTypeDef]:
        """
        [ListProtections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Paginator.ListProtections.paginate)
        """
