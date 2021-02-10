"""
Main interface for location service.

Usage::

    ```python
    import boto3
    from mypy_boto3_location import (
        Client,
        GetDevicePositionHistoryPaginator,
        ListGeofenceCollectionsPaginator,
        ListGeofencesPaginator,
        ListMapsPaginator,
        ListPlaceIndexesPaginator,
        ListTrackerConsumersPaginator,
        ListTrackersPaginator,
        LocationServiceClient,
    )

    session = boto3.Session()

    client: LocationServiceClient = boto3.client("location")
    session_client: LocationServiceClient = session.client("location")

    get_device_position_history_paginator: GetDevicePositionHistoryPaginator = client.get_paginator("get_device_position_history")
    list_geofence_collections_paginator: ListGeofenceCollectionsPaginator = client.get_paginator("list_geofence_collections")
    list_geofences_paginator: ListGeofencesPaginator = client.get_paginator("list_geofences")
    list_maps_paginator: ListMapsPaginator = client.get_paginator("list_maps")
    list_place_indexes_paginator: ListPlaceIndexesPaginator = client.get_paginator("list_place_indexes")
    list_tracker_consumers_paginator: ListTrackerConsumersPaginator = client.get_paginator("list_tracker_consumers")
    list_trackers_paginator: ListTrackersPaginator = client.get_paginator("list_trackers")
    ```
"""
from mypy_boto3_location.client import LocationServiceClient
from mypy_boto3_location.paginator import (
    GetDevicePositionHistoryPaginator,
    ListGeofenceCollectionsPaginator,
    ListGeofencesPaginator,
    ListMapsPaginator,
    ListPlaceIndexesPaginator,
    ListTrackerConsumersPaginator,
    ListTrackersPaginator,
)

Client = LocationServiceClient


__all__ = (
    "Client",
    "GetDevicePositionHistoryPaginator",
    "ListGeofenceCollectionsPaginator",
    "ListGeofencesPaginator",
    "ListMapsPaginator",
    "ListPlaceIndexesPaginator",
    "ListTrackerConsumersPaginator",
    "ListTrackersPaginator",
    "LocationServiceClient",
)
