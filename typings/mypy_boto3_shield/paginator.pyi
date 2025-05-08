"""
Type annotations for shield service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_shield.client import ShieldClient
    from mypy_boto3_shield.paginator import (
        ListAttacksPaginator,
        ListProtectionsPaginator,
    )

    session = Session()
    client: ShieldClient = session.client("shield")

    list_attacks_paginator: ListAttacksPaginator = client.get_paginator("list_attacks")
    list_protections_paginator: ListProtectionsPaginator = client.get_paginator("list_protections")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAttacksRequestPaginateTypeDef,
    ListAttacksResponseTypeDef,
    ListProtectionsRequestPaginateTypeDef,
    ListProtectionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListAttacksPaginator", "ListProtectionsPaginator")

if TYPE_CHECKING:
    _ListAttacksPaginatorBase = Paginator[ListAttacksResponseTypeDef]
else:
    _ListAttacksPaginatorBase = Paginator  # type: ignore[assignment]

class ListAttacksPaginator(_ListAttacksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/paginator/ListAttacks.html#Shield.Paginator.ListAttacks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/paginators/#listattackspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAttacksRequestPaginateTypeDef]
    ) -> PageIterator[ListAttacksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/paginator/ListAttacks.html#Shield.Paginator.ListAttacks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/paginators/#listattackspaginator)
        """

if TYPE_CHECKING:
    _ListProtectionsPaginatorBase = Paginator[ListProtectionsResponseTypeDef]
else:
    _ListProtectionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListProtectionsPaginator(_ListProtectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/paginator/ListProtections.html#Shield.Paginator.ListProtections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/paginators/#listprotectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProtectionsRequestPaginateTypeDef]
    ) -> PageIterator[ListProtectionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/paginator/ListProtections.html#Shield.Paginator.ListProtections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/paginators/#listprotectionspaginator)
        """
