"""
Main interface for location service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_location import LocationServiceClient
    from mypy_boto3_location.paginator import (
        GetDevicePositionHistoryPaginator,
        ListGeofenceCollectionsPaginator,
        ListGeofencesPaginator,
        ListMapsPaginator,
        ListPlaceIndexesPaginator,
        ListTrackerConsumersPaginator,
        ListTrackersPaginator,
    )

    client: LocationServiceClient = boto3.client("location")

    get_device_position_history_paginator: GetDevicePositionHistoryPaginator = client.get_paginator("get_device_position_history")
    list_geofence_collections_paginator: ListGeofenceCollectionsPaginator = client.get_paginator("list_geofence_collections")
    list_geofences_paginator: ListGeofencesPaginator = client.get_paginator("list_geofences")
    list_maps_paginator: ListMapsPaginator = client.get_paginator("list_maps")
    list_place_indexes_paginator: ListPlaceIndexesPaginator = client.get_paginator("list_place_indexes")
    list_tracker_consumers_paginator: ListTrackerConsumersPaginator = client.get_paginator("list_tracker_consumers")
    list_trackers_paginator: ListTrackersPaginator = client.get_paginator("list_trackers")
    ```
"""
from datetime import datetime
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_location.type_defs import (
    GetDevicePositionHistoryResponseTypeDef,
    ListGeofenceCollectionsResponseTypeDef,
    ListGeofencesResponseTypeDef,
    ListMapsResponseTypeDef,
    ListPlaceIndexesResponseTypeDef,
    ListTrackerConsumersResponseTypeDef,
    ListTrackersResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "GetDevicePositionHistoryPaginator",
    "ListGeofenceCollectionsPaginator",
    "ListGeofencesPaginator",
    "ListMapsPaginator",
    "ListPlaceIndexesPaginator",
    "ListTrackerConsumersPaginator",
    "ListTrackersPaginator",
)


class GetDevicePositionHistoryPaginator(Boto3Paginator):
    """
    [Paginator.GetDevicePositionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.GetDevicePositionHistory)
    """

    def paginate(
        self,
        DeviceId: str,
        TrackerName: str,
        EndTimeExclusive: datetime = None,
        StartTimeInclusive: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetDevicePositionHistoryResponseTypeDef]:
        """
        [GetDevicePositionHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.GetDevicePositionHistory.paginate)
        """


class ListGeofenceCollectionsPaginator(Boto3Paginator):
    """
    [Paginator.ListGeofenceCollections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.ListGeofenceCollections)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGeofenceCollectionsResponseTypeDef]:
        """
        [ListGeofenceCollections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.ListGeofenceCollections.paginate)
        """


class ListGeofencesPaginator(Boto3Paginator):
    """
    [Paginator.ListGeofences documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.ListGeofences)
    """

    def paginate(
        self, CollectionName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGeofencesResponseTypeDef]:
        """
        [ListGeofences.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.ListGeofences.paginate)
        """


class ListMapsPaginator(Boto3Paginator):
    """
    [Paginator.ListMaps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.ListMaps)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMapsResponseTypeDef]:
        """
        [ListMaps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.ListMaps.paginate)
        """


class ListPlaceIndexesPaginator(Boto3Paginator):
    """
    [Paginator.ListPlaceIndexes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.ListPlaceIndexes)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPlaceIndexesResponseTypeDef]:
        """
        [ListPlaceIndexes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.ListPlaceIndexes.paginate)
        """


class ListTrackerConsumersPaginator(Boto3Paginator):
    """
    [Paginator.ListTrackerConsumers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.ListTrackerConsumers)
    """

    def paginate(
        self, TrackerName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTrackerConsumersResponseTypeDef]:
        """
        [ListTrackerConsumers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.ListTrackerConsumers.paginate)
        """


class ListTrackersPaginator(Boto3Paginator):
    """
    [Paginator.ListTrackers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.ListTrackers)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTrackersResponseTypeDef]:
        """
        [ListTrackers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.ListTrackers.paginate)
        """
