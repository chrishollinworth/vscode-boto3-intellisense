"""
Type annotations for arc-zonal-shift service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_arc_zonal_shift.client import ARCZonalShiftClient
    from mypy_boto3_arc_zonal_shift.paginator import (
        ListAutoshiftsPaginator,
        ListManagedResourcesPaginator,
        ListZonalShiftsPaginator,
    )

    session = Session()
    client: ARCZonalShiftClient = session.client("arc-zonal-shift")

    list_autoshifts_paginator: ListAutoshiftsPaginator = client.get_paginator("list_autoshifts")
    list_managed_resources_paginator: ListManagedResourcesPaginator = client.get_paginator("list_managed_resources")
    list_zonal_shifts_paginator: ListZonalShiftsPaginator = client.get_paginator("list_zonal_shifts")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAutoshiftsRequestPaginateTypeDef,
    ListAutoshiftsResponseTypeDef,
    ListManagedResourcesRequestPaginateTypeDef,
    ListManagedResourcesResponseTypeDef,
    ListZonalShiftsRequestPaginateTypeDef,
    ListZonalShiftsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListAutoshiftsPaginator", "ListManagedResourcesPaginator", "ListZonalShiftsPaginator")

if TYPE_CHECKING:
    _ListAutoshiftsPaginatorBase = Paginator[ListAutoshiftsResponseTypeDef]
else:
    _ListAutoshiftsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAutoshiftsPaginator(_ListAutoshiftsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/paginator/ListAutoshifts.html#ARCZonalShift.Paginator.ListAutoshifts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/paginators/#listautoshiftspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAutoshiftsRequestPaginateTypeDef]
    ) -> PageIterator[ListAutoshiftsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/paginator/ListAutoshifts.html#ARCZonalShift.Paginator.ListAutoshifts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/paginators/#listautoshiftspaginator)
        """

if TYPE_CHECKING:
    _ListManagedResourcesPaginatorBase = Paginator[ListManagedResourcesResponseTypeDef]
else:
    _ListManagedResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListManagedResourcesPaginator(_ListManagedResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/paginator/ListManagedResources.html#ARCZonalShift.Paginator.ListManagedResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/paginators/#listmanagedresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListManagedResourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListManagedResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/paginator/ListManagedResources.html#ARCZonalShift.Paginator.ListManagedResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/paginators/#listmanagedresourcespaginator)
        """

if TYPE_CHECKING:
    _ListZonalShiftsPaginatorBase = Paginator[ListZonalShiftsResponseTypeDef]
else:
    _ListZonalShiftsPaginatorBase = Paginator  # type: ignore[assignment]

class ListZonalShiftsPaginator(_ListZonalShiftsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/paginator/ListZonalShifts.html#ARCZonalShift.Paginator.ListZonalShifts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/paginators/#listzonalshiftspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListZonalShiftsRequestPaginateTypeDef]
    ) -> PageIterator[ListZonalShiftsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/paginator/ListZonalShifts.html#ARCZonalShift.Paginator.ListZonalShifts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/paginators/#listzonalshiftspaginator)
        """
