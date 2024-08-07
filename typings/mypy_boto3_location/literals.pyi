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
    "ForecastGeofenceEventsPaginatorName",
    "ForecastedGeofenceEventTypeType",
    "GetDevicePositionHistoryPaginatorName",
    "IntendedUseType",
    "ListDevicePositionsPaginatorName",
    "ListGeofenceCollectionsPaginatorName",
    "ListGeofencesPaginatorName",
    "ListKeysPaginatorName",
    "ListMapsPaginatorName",
    "ListPlaceIndexesPaginatorName",
    "ListRouteCalculatorsPaginatorName",
    "ListTrackerConsumersPaginatorName",
    "ListTrackersPaginatorName",
    "OptimizationModeType",
    "PositionFilteringType",
    "PricingPlanType",
    "RouteMatrixErrorCodeType",
    "SpeedUnitType",
    "StatusType",
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
ForecastGeofenceEventsPaginatorName = Literal["forecast_geofence_events"]
ForecastedGeofenceEventTypeType = Literal["ENTER", "EXIT", "IDLE"]
GetDevicePositionHistoryPaginatorName = Literal["get_device_position_history"]
IntendedUseType = Literal["SingleUse", "Storage"]
ListDevicePositionsPaginatorName = Literal["list_device_positions"]
ListGeofenceCollectionsPaginatorName = Literal["list_geofence_collections"]
ListGeofencesPaginatorName = Literal["list_geofences"]
ListKeysPaginatorName = Literal["list_keys"]
ListMapsPaginatorName = Literal["list_maps"]
ListPlaceIndexesPaginatorName = Literal["list_place_indexes"]
ListRouteCalculatorsPaginatorName = Literal["list_route_calculators"]
ListTrackerConsumersPaginatorName = Literal["list_tracker_consumers"]
ListTrackersPaginatorName = Literal["list_trackers"]
OptimizationModeType = Literal["FastestRoute", "ShortestRoute"]
PositionFilteringType = Literal["AccuracyBased", "DistanceBased", "TimeBased"]
PricingPlanType = Literal["MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"]
RouteMatrixErrorCodeType = Literal[
    "DeparturePositionNotFound",
    "DestinationPositionNotFound",
    "OtherValidationError",
    "PositionsNotFound",
    "RouteNotFound",
    "RouteTooLong",
]
SpeedUnitType = Literal["KilometersPerHour", "MilesPerHour"]
StatusType = Literal["Active", "Expired"]
TravelModeType = Literal["Bicycle", "Car", "Motorcycle", "Truck", "Walking"]
VehicleWeightUnitType = Literal["Kilograms", "Pounds"]
