"""
Type annotations for mediaconnect service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_mediaconnect.client import MediaConnectClient
    from mypy_boto3_mediaconnect.paginator import (
        ListBridgesPaginator,
        ListEntitlementsPaginator,
        ListFlowsPaginator,
        ListGatewayInstancesPaginator,
        ListGatewaysPaginator,
        ListOfferingsPaginator,
        ListReservationsPaginator,
    )

    session = Session()
    client: MediaConnectClient = session.client("mediaconnect")

    list_bridges_paginator: ListBridgesPaginator = client.get_paginator("list_bridges")
    list_entitlements_paginator: ListEntitlementsPaginator = client.get_paginator("list_entitlements")
    list_flows_paginator: ListFlowsPaginator = client.get_paginator("list_flows")
    list_gateway_instances_paginator: ListGatewayInstancesPaginator = client.get_paginator("list_gateway_instances")
    list_gateways_paginator: ListGatewaysPaginator = client.get_paginator("list_gateways")
    list_offerings_paginator: ListOfferingsPaginator = client.get_paginator("list_offerings")
    list_reservations_paginator: ListReservationsPaginator = client.get_paginator("list_reservations")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListBridgesRequestPaginateTypeDef,
    ListBridgesResponseTypeDef,
    ListEntitlementsRequestPaginateTypeDef,
    ListEntitlementsResponseTypeDef,
    ListFlowsRequestPaginateTypeDef,
    ListFlowsResponseTypeDef,
    ListGatewayInstancesRequestPaginateTypeDef,
    ListGatewayInstancesResponseTypeDef,
    ListGatewaysRequestPaginateTypeDef,
    ListGatewaysResponseTypeDef,
    ListOfferingsRequestPaginateTypeDef,
    ListOfferingsResponseTypeDef,
    ListReservationsRequestPaginateTypeDef,
    ListReservationsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListBridgesPaginator",
    "ListEntitlementsPaginator",
    "ListFlowsPaginator",
    "ListGatewayInstancesPaginator",
    "ListGatewaysPaginator",
    "ListOfferingsPaginator",
    "ListReservationsPaginator",
)

if TYPE_CHECKING:
    _ListBridgesPaginatorBase = Paginator[ListBridgesResponseTypeDef]
else:
    _ListBridgesPaginatorBase = Paginator  # type: ignore[assignment]

class ListBridgesPaginator(_ListBridgesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/paginator/ListBridges.html#MediaConnect.Paginator.ListBridges)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators/#listbridgespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBridgesRequestPaginateTypeDef]
    ) -> PageIterator[ListBridgesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/paginator/ListBridges.html#MediaConnect.Paginator.ListBridges.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators/#listbridgespaginator)
        """

if TYPE_CHECKING:
    _ListEntitlementsPaginatorBase = Paginator[ListEntitlementsResponseTypeDef]
else:
    _ListEntitlementsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEntitlementsPaginator(_ListEntitlementsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/paginator/ListEntitlements.html#MediaConnect.Paginator.ListEntitlements)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators/#listentitlementspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEntitlementsRequestPaginateTypeDef]
    ) -> PageIterator[ListEntitlementsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/paginator/ListEntitlements.html#MediaConnect.Paginator.ListEntitlements.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators/#listentitlementspaginator)
        """

if TYPE_CHECKING:
    _ListFlowsPaginatorBase = Paginator[ListFlowsResponseTypeDef]
else:
    _ListFlowsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFlowsPaginator(_ListFlowsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/paginator/ListFlows.html#MediaConnect.Paginator.ListFlows)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators/#listflowspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFlowsRequestPaginateTypeDef]
    ) -> PageIterator[ListFlowsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/paginator/ListFlows.html#MediaConnect.Paginator.ListFlows.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators/#listflowspaginator)
        """

if TYPE_CHECKING:
    _ListGatewayInstancesPaginatorBase = Paginator[ListGatewayInstancesResponseTypeDef]
else:
    _ListGatewayInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class ListGatewayInstancesPaginator(_ListGatewayInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/paginator/ListGatewayInstances.html#MediaConnect.Paginator.ListGatewayInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators/#listgatewayinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGatewayInstancesRequestPaginateTypeDef]
    ) -> PageIterator[ListGatewayInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/paginator/ListGatewayInstances.html#MediaConnect.Paginator.ListGatewayInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators/#listgatewayinstancespaginator)
        """

if TYPE_CHECKING:
    _ListGatewaysPaginatorBase = Paginator[ListGatewaysResponseTypeDef]
else:
    _ListGatewaysPaginatorBase = Paginator  # type: ignore[assignment]

class ListGatewaysPaginator(_ListGatewaysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/paginator/ListGateways.html#MediaConnect.Paginator.ListGateways)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators/#listgatewayspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGatewaysRequestPaginateTypeDef]
    ) -> PageIterator[ListGatewaysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/paginator/ListGateways.html#MediaConnect.Paginator.ListGateways.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators/#listgatewayspaginator)
        """

if TYPE_CHECKING:
    _ListOfferingsPaginatorBase = Paginator[ListOfferingsResponseTypeDef]
else:
    _ListOfferingsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOfferingsPaginator(_ListOfferingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/paginator/ListOfferings.html#MediaConnect.Paginator.ListOfferings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators/#listofferingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOfferingsRequestPaginateTypeDef]
    ) -> PageIterator[ListOfferingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/paginator/ListOfferings.html#MediaConnect.Paginator.ListOfferings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators/#listofferingspaginator)
        """

if TYPE_CHECKING:
    _ListReservationsPaginatorBase = Paginator[ListReservationsResponseTypeDef]
else:
    _ListReservationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListReservationsPaginator(_ListReservationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/paginator/ListReservations.html#MediaConnect.Paginator.ListReservations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators/#listreservationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReservationsRequestPaginateTypeDef]
    ) -> PageIterator[ListReservationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/paginator/ListReservations.html#MediaConnect.Paginator.ListReservations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/paginators/#listreservationspaginator)
        """
