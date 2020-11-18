# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for mediaconnect service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_mediaconnect import MediaConnectClient
    from mypy_boto3_mediaconnect.paginator import (
        ListEntitlementsPaginator,
        ListFlowsPaginator,
        ListOfferingsPaginator,
        ListReservationsPaginator,
    )

    client: MediaConnectClient = boto3.client("mediaconnect")

    list_entitlements_paginator: ListEntitlementsPaginator = client.get_paginator("list_entitlements")
    list_flows_paginator: ListFlowsPaginator = client.get_paginator("list_flows")
    list_offerings_paginator: ListOfferingsPaginator = client.get_paginator("list_offerings")
    list_reservations_paginator: ListReservationsPaginator = client.get_paginator("list_reservations")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_mediaconnect.type_defs import (
    ListEntitlementsResponseTypeDef,
    ListFlowsResponseTypeDef,
    ListOfferingsResponseTypeDef,
    ListReservationsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListEntitlementsPaginator",
    "ListFlowsPaginator",
    "ListOfferingsPaginator",
    "ListReservationsPaginator",
)


class ListEntitlementsPaginator(Boto3Paginator):
    """
    [Paginator.ListEntitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Paginator.ListEntitlements)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEntitlementsResponseTypeDef]:
        """
        [ListEntitlements.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Paginator.ListEntitlements.paginate)
        """


class ListFlowsPaginator(Boto3Paginator):
    """
    [Paginator.ListFlows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Paginator.ListFlows)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFlowsResponseTypeDef]:
        """
        [ListFlows.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Paginator.ListFlows.paginate)
        """


class ListOfferingsPaginator(Boto3Paginator):
    """
    [Paginator.ListOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Paginator.ListOfferings)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOfferingsResponseTypeDef]:
        """
        [ListOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Paginator.ListOfferings.paginate)
        """


class ListReservationsPaginator(Boto3Paginator):
    """
    [Paginator.ListReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Paginator.ListReservations)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReservationsResponseTypeDef]:
        """
        [ListReservations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconnect.html#MediaConnect.Paginator.ListReservations.paginate)
        """
