"""
Main interface for location service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_location import (
        Client,
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
        LocationServiceClient,
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

from .client import LocationServiceClient
from .paginator import (
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

Client = LocationServiceClient

__all__ = (
    "Client",
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
    "LocationServiceClient",
)
