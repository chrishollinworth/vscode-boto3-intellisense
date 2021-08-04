"""
Type annotations for location service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/literals.html)

Usage::

    ```python
    from mypy_boto3_location.literals import BatchItemErrorCodeType

    data: BatchItemErrorCodeType = "AccessDeniedError"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BatchItemErrorCodeType",
    "DimensionUnitType",
    "DistanceUnitType",
    "GetDevicePositionHistoryPaginatorName",
    "IntendedUseType",
    "ListDevicePositionsPaginatorName",
    "ListGeofenceCollectionsPaginatorName",
    "ListGeofencesPaginatorName",
    "ListMapsPaginatorName",
    "ListPlaceIndexesPaginatorName",
    "ListRouteCalculatorsPaginatorName",
    "ListTrackerConsumersPaginatorName",
    "ListTrackersPaginatorName",
    "PricingPlanType",
    "TravelModeType",
    "VehicleWeightUnitType",
)

BatchItemErrorCodeType = Literal[
    "AccessDeniedError",
    "ConflictError",
    "InternalServerError",
    "ResourceNotFoundError",
    "ThrottlingError",
    "ValidationError",
]
DimensionUnitType = Literal["Feet", "Meters"]
DistanceUnitType = Literal["Kilometers", "Miles"]
GetDevicePositionHistoryPaginatorName = Literal["get_device_position_history"]
IntendedUseType = Literal["SingleUse", "Storage"]
ListDevicePositionsPaginatorName = Literal["list_device_positions"]
ListGeofenceCollectionsPaginatorName = Literal["list_geofence_collections"]
ListGeofencesPaginatorName = Literal["list_geofences"]
ListMapsPaginatorName = Literal["list_maps"]
ListPlaceIndexesPaginatorName = Literal["list_place_indexes"]
ListRouteCalculatorsPaginatorName = Literal["list_route_calculators"]
ListTrackerConsumersPaginatorName = Literal["list_tracker_consumers"]
ListTrackersPaginatorName = Literal["list_trackers"]
PricingPlanType = Literal["MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"]
TravelModeType = Literal["Car", "Truck", "Walking"]
VehicleWeightUnitType = Literal["Kilograms", "Pounds"]
