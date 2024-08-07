"""
Type annotations for location service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_location import LocationServiceClient
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

    client: LocationServiceClient = boto3.client("location")

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

from datetime import datetime
from typing import Iterator, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import DistanceUnitType, SpeedUnitType
from .type_defs import (
    ApiKeyFilterTypeDef,
    ForecastGeofenceEventsDeviceStateTypeDef,
    ForecastGeofenceEventsResponseTypeDef,
    GetDevicePositionHistoryResponseTypeDef,
    ListDevicePositionsResponseTypeDef,
    ListGeofenceCollectionsResponseTypeDef,
    ListGeofencesResponseTypeDef,
    ListKeysResponseTypeDef,
    ListMapsResponseTypeDef,
    ListPlaceIndexesResponseTypeDef,
    ListRouteCalculatorsResponseTypeDef,
    ListTrackerConsumersResponseTypeDef,
    ListTrackersResponseTypeDef,
    PaginatorConfigTypeDef,
    TrackingFilterGeometryTypeDef,
)

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

class ForecastGeofenceEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ForecastGeofenceEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#forecastgeofenceeventspaginator)
    """

    def paginate(
        self,
        *,
        CollectionName: str,
        DeviceState: "ForecastGeofenceEventsDeviceStateTypeDef",
        TimeHorizonMinutes: float = None,
        DistanceUnit: DistanceUnitType = None,
        SpeedUnit: SpeedUnitType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ForecastGeofenceEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ForecastGeofenceEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#forecastgeofenceeventspaginator)
        """

class GetDevicePositionHistoryPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.GetDevicePositionHistory)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#getdevicepositionhistorypaginator)
    """

    def paginate(
        self,
        *,
        TrackerName: str,
        DeviceId: str,
        StartTimeInclusive: Union[datetime, str] = None,
        EndTimeExclusive: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDevicePositionHistoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.GetDevicePositionHistory.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#getdevicepositionhistorypaginator)
        """

class ListDevicePositionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ListDevicePositions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listdevicepositionspaginator)
    """

    def paginate(
        self,
        *,
        TrackerName: str,
        FilterGeometry: "TrackingFilterGeometryTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDevicePositionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ListDevicePositions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listdevicepositionspaginator)
        """

class ListGeofenceCollectionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ListGeofenceCollections)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listgeofencecollectionspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGeofenceCollectionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ListGeofenceCollections.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listgeofencecollectionspaginator)
        """

class ListGeofencesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ListGeofences)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listgeofencespaginator)
    """

    def paginate(
        self, *, CollectionName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGeofencesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ListGeofences.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listgeofencespaginator)
        """

class ListKeysPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ListKeys)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listkeyspaginator)
    """

    def paginate(
        self,
        *,
        Filter: "ApiKeyFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListKeysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ListKeys.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listkeyspaginator)
        """

class ListMapsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ListMaps)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listmapspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMapsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ListMaps.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listmapspaginator)
        """

class ListPlaceIndexesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ListPlaceIndexes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listplaceindexespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPlaceIndexesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ListPlaceIndexes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listplaceindexespaginator)
        """

class ListRouteCalculatorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ListRouteCalculators)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listroutecalculatorspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRouteCalculatorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ListRouteCalculators.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listroutecalculatorspaginator)
        """

class ListTrackerConsumersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ListTrackerConsumers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listtrackerconsumerspaginator)
    """

    def paginate(
        self, *, TrackerName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTrackerConsumersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ListTrackerConsumers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listtrackerconsumerspaginator)
        """

class ListTrackersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ListTrackers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listtrackerspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTrackersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/location.html#LocationService.Paginator.ListTrackers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listtrackerspaginator)
        """
