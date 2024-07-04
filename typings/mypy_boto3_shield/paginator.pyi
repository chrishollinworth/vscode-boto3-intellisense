"""
Type annotations for shield service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/paginators.html)

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

from .type_defs import (
    InclusionProtectionFiltersTypeDef,
    ListAttacksResponseTypeDef,
    ListProtectionsResponseTypeDef,
    PaginatorConfigTypeDef,
    TimeRangeTypeDef,
)

__all__ = ("ListAttacksPaginator", "ListProtectionsPaginator")

class ListAttacksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/shield.html#Shield.Paginator.ListAttacks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/paginators.html#listattackspaginator)
    """

    def paginate(
        self,
        *,
        ResourceArns: List[str] = None,
        StartTime: "TimeRangeTypeDef" = None,
        EndTime: "TimeRangeTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAttacksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/shield.html#Shield.Paginator.ListAttacks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/paginators.html#listattackspaginator)
        """

class ListProtectionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/shield.html#Shield.Paginator.ListProtections)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/paginators.html#listprotectionspaginator)
    """

    def paginate(
        self,
        *,
        InclusionFilters: "InclusionProtectionFiltersTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProtectionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/shield.html#Shield.Paginator.ListProtections.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/paginators.html#listprotectionspaginator)
        """
