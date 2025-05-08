"""
Type annotations for location service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_location.client import LocationServiceClient
    from mypy_boto3_location.paginator import (
        ForecastGeofenceEventsPaginator,
        GetDevicePositionHistoryPaginator,
        ListDevicePositionsPaginator,
        ListGeofenceCollectionsPaginator,
        ListGeofencesPaginator,
        ListKeysPaginator,
        ListMapsPaginator,
        ListPlaceIndexesPaginator,
        ListRouteCalculatorsPaginator,
        ListTrackerConsumersPaginator,
        ListTrackersPaginator,
    )

    session = Session()
    client: LocationServiceClient = session.client("location")

    forecast_geofence_events_paginator: ForecastGeofenceEventsPaginator = client.get_paginator("forecast_geofence_events")
    get_device_position_history_paginator: GetDevicePositionHistoryPaginator = client.get_paginator("get_device_position_history")
    list_device_positions_paginator: ListDevicePositionsPaginator = client.get_paginator("list_device_positions")
    list_geofence_collections_paginator: ListGeofenceCollectionsPaginator = client.get_paginator("list_geofence_collections")
    list_geofences_paginator: ListGeofencesPaginator = client.get_paginator("list_geofences")
    list_keys_paginator: ListKeysPaginator = client.get_paginator("list_keys")
    list_maps_paginator: ListMapsPaginator = client.get_paginator("list_maps")
    list_place_indexes_paginator: ListPlaceIndexesPaginator = client.get_paginator("list_place_indexes")
    list_route_calculators_paginator: ListRouteCalculatorsPaginator = client.get_paginator("list_route_calculators")
    list_tracker_consumers_paginator: ListTrackerConsumersPaginator = client.get_paginator("list_tracker_consumers")
    list_trackers_paginator: ListTrackersPaginator = client.get_paginator("list_trackers")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ForecastGeofenceEventsRequestPaginateTypeDef,
    ForecastGeofenceEventsResponseTypeDef,
    GetDevicePositionHistoryRequestPaginateTypeDef,
    GetDevicePositionHistoryResponseTypeDef,
    ListDevicePositionsRequestPaginateTypeDef,
    ListDevicePositionsResponseTypeDef,
    ListGeofenceCollectionsRequestPaginateTypeDef,
    ListGeofenceCollectionsResponseTypeDef,
    ListGeofencesRequestPaginateTypeDef,
    ListGeofencesResponseTypeDef,
    ListKeysRequestPaginateTypeDef,
    ListKeysResponseTypeDef,
    ListMapsRequestPaginateTypeDef,
    ListMapsResponseTypeDef,
    ListPlaceIndexesRequestPaginateTypeDef,
    ListPlaceIndexesResponseTypeDef,
    ListRouteCalculatorsRequestPaginateTypeDef,
    ListRouteCalculatorsResponseTypeDef,
    ListTrackerConsumersRequestPaginateTypeDef,
    ListTrackerConsumersResponseTypeDef,
    ListTrackersRequestPaginateTypeDef,
    ListTrackersResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ForecastGeofenceEventsPaginator",
    "GetDevicePositionHistoryPaginator",
    "ListDevicePositionsPaginator",
    "ListGeofenceCollectionsPaginator",
    "ListGeofencesPaginator",
    "ListKeysPaginator",
    "ListMapsPaginator",
    "ListPlaceIndexesPaginator",
    "ListRouteCalculatorsPaginator",
    "ListTrackerConsumersPaginator",
    "ListTrackersPaginator",
)

if TYPE_CHECKING:
    _ForecastGeofenceEventsPaginatorBase = Paginator[ForecastGeofenceEventsResponseTypeDef]
else:
    _ForecastGeofenceEventsPaginatorBase = Paginator  # type: ignore[assignment]

class ForecastGeofenceEventsPaginator(_ForecastGeofenceEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ForecastGeofenceEvents.html#LocationService.Paginator.ForecastGeofenceEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#forecastgeofenceeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ForecastGeofenceEventsRequestPaginateTypeDef]
    ) -> PageIterator[ForecastGeofenceEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ForecastGeofenceEvents.html#LocationService.Paginator.ForecastGeofenceEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#forecastgeofenceeventspaginator)
        """

if TYPE_CHECKING:
    _GetDevicePositionHistoryPaginatorBase = Paginator[GetDevicePositionHistoryResponseTypeDef]
else:
    _GetDevicePositionHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class GetDevicePositionHistoryPaginator(_GetDevicePositionHistoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/GetDevicePositionHistory.html#LocationService.Paginator.GetDevicePositionHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#getdevicepositionhistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetDevicePositionHistoryRequestPaginateTypeDef]
    ) -> PageIterator[GetDevicePositionHistoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/GetDevicePositionHistory.html#LocationService.Paginator.GetDevicePositionHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#getdevicepositionhistorypaginator)
        """

if TYPE_CHECKING:
    _ListDevicePositionsPaginatorBase = Paginator[ListDevicePositionsResponseTypeDef]
else:
    _ListDevicePositionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDevicePositionsPaginator(_ListDevicePositionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ListDevicePositions.html#LocationService.Paginator.ListDevicePositions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#listdevicepositionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDevicePositionsRequestPaginateTypeDef]
    ) -> PageIterator[ListDevicePositionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ListDevicePositions.html#LocationService.Paginator.ListDevicePositions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#listdevicepositionspaginator)
        """

if TYPE_CHECKING:
    _ListGeofenceCollectionsPaginatorBase = Paginator[ListGeofenceCollectionsResponseTypeDef]
else:
    _ListGeofenceCollectionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListGeofenceCollectionsPaginator(_ListGeofenceCollectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ListGeofenceCollections.html#LocationService.Paginator.ListGeofenceCollections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#listgeofencecollectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGeofenceCollectionsRequestPaginateTypeDef]
    ) -> PageIterator[ListGeofenceCollectionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ListGeofenceCollections.html#LocationService.Paginator.ListGeofenceCollections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#listgeofencecollectionspaginator)
        """

if TYPE_CHECKING:
    _ListGeofencesPaginatorBase = Paginator[ListGeofencesResponseTypeDef]
else:
    _ListGeofencesPaginatorBase = Paginator  # type: ignore[assignment]

class ListGeofencesPaginator(_ListGeofencesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ListGeofences.html#LocationService.Paginator.ListGeofences)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#listgeofencespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGeofencesRequestPaginateTypeDef]
    ) -> PageIterator[ListGeofencesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ListGeofences.html#LocationService.Paginator.ListGeofences.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#listgeofencespaginator)
        """

if TYPE_CHECKING:
    _ListKeysPaginatorBase = Paginator[ListKeysResponseTypeDef]
else:
    _ListKeysPaginatorBase = Paginator  # type: ignore[assignment]

class ListKeysPaginator(_ListKeysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ListKeys.html#LocationService.Paginator.ListKeys)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#listkeyspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListKeysRequestPaginateTypeDef]
    ) -> PageIterator[ListKeysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ListKeys.html#LocationService.Paginator.ListKeys.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#listkeyspaginator)
        """

if TYPE_CHECKING:
    _ListMapsPaginatorBase = Paginator[ListMapsResponseTypeDef]
else:
    _ListMapsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMapsPaginator(_ListMapsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ListMaps.html#LocationService.Paginator.ListMaps)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#listmapspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMapsRequestPaginateTypeDef]
    ) -> PageIterator[ListMapsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ListMaps.html#LocationService.Paginator.ListMaps.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#listmapspaginator)
        """

if TYPE_CHECKING:
    _ListPlaceIndexesPaginatorBase = Paginator[ListPlaceIndexesResponseTypeDef]
else:
    _ListPlaceIndexesPaginatorBase = Paginator  # type: ignore[assignment]

class ListPlaceIndexesPaginator(_ListPlaceIndexesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ListPlaceIndexes.html#LocationService.Paginator.ListPlaceIndexes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#listplaceindexespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPlaceIndexesRequestPaginateTypeDef]
    ) -> PageIterator[ListPlaceIndexesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ListPlaceIndexes.html#LocationService.Paginator.ListPlaceIndexes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#listplaceindexespaginator)
        """

if TYPE_CHECKING:
    _ListRouteCalculatorsPaginatorBase = Paginator[ListRouteCalculatorsResponseTypeDef]
else:
    _ListRouteCalculatorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRouteCalculatorsPaginator(_ListRouteCalculatorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ListRouteCalculators.html#LocationService.Paginator.ListRouteCalculators)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#listroutecalculatorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRouteCalculatorsRequestPaginateTypeDef]
    ) -> PageIterator[ListRouteCalculatorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ListRouteCalculators.html#LocationService.Paginator.ListRouteCalculators.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#listroutecalculatorspaginator)
        """

if TYPE_CHECKING:
    _ListTrackerConsumersPaginatorBase = Paginator[ListTrackerConsumersResponseTypeDef]
else:
    _ListTrackerConsumersPaginatorBase = Paginator  # type: ignore[assignment]

class ListTrackerConsumersPaginator(_ListTrackerConsumersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ListTrackerConsumers.html#LocationService.Paginator.ListTrackerConsumers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#listtrackerconsumerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTrackerConsumersRequestPaginateTypeDef]
    ) -> PageIterator[ListTrackerConsumersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ListTrackerConsumers.html#LocationService.Paginator.ListTrackerConsumers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#listtrackerconsumerspaginator)
        """

if TYPE_CHECKING:
    _ListTrackersPaginatorBase = Paginator[ListTrackersResponseTypeDef]
else:
    _ListTrackersPaginatorBase = Paginator  # type: ignore[assignment]

class ListTrackersPaginator(_ListTrackersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ListTrackers.html#LocationService.Paginator.ListTrackers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#listtrackerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTrackersRequestPaginateTypeDef]
    ) -> PageIterator[ListTrackersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/paginator/ListTrackers.html#LocationService.Paginator.ListTrackers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/paginators/#listtrackerspaginator)
        """
