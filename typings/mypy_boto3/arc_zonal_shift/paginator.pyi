"""
Type annotations for arc-zonal-shift service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_arc_zonal_shift import ARCZonalShiftClient
    from mypy_boto3_arc_zonal_shift.paginator import (
        ListManagedResourcesPaginator,
        ListZonalShiftsPaginator,
    )

    client: ARCZonalShiftClient = boto3.client("arc-zonal-shift")

    list_managed_resources_paginator: ListManagedResourcesPaginator = client.get_paginator("list_managed_resources")
    list_zonal_shifts_paginator: ListZonalShiftsPaginator = client.get_paginator("list_zonal_shifts")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ZonalShiftStatusType
from .type_defs import (
    ListManagedResourcesResponseTypeDef,
    ListZonalShiftsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListManagedResourcesPaginator", "ListZonalShiftsPaginator")

class ListManagedResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/arc-zonal-shift.html#ARCZonalShift.Paginator.ListManagedResources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/paginators.html#listmanagedresourcespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListManagedResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/arc-zonal-shift.html#ARCZonalShift.Paginator.ListManagedResources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/paginators.html#listmanagedresourcespaginator)
        """

class ListZonalShiftsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/arc-zonal-shift.html#ARCZonalShift.Paginator.ListZonalShifts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/paginators.html#listzonalshiftspaginator)
    """

    def paginate(
        self,
        *,
        status: ZonalShiftStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListZonalShiftsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/arc-zonal-shift.html#ARCZonalShift.Paginator.ListZonalShifts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/paginators.html#listzonalshiftspaginator)
        """
