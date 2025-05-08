"""
Type annotations for geo-routes service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_routes/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_geo_routes.type_defs import IsolineAllowOptionsTypeDef

    data: IsolineAllowOptionsTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Union

from .literals import (
    DayOfWeekType,
    GeometryFormatType,
    IsolineEngineTypeType,
    IsolineHazardousCargoTypeType,
    IsolineOptimizationObjectiveType,
    IsolineTravelModeType,
    IsolineTruckTypeType,
    IsolineZoneCategoryType,
    MatchingStrategyType,
    MeasurementSystemType,
    RoadSnapHazardousCargoTypeType,
    RoadSnapNoticeCodeType,
    RoadSnapTravelModeType,
    RouteDirectionType,
    RouteEngineTypeType,
    RouteFerryNoticeCodeType,
    RouteFerryTravelStepTypeType,
    RouteHazardousCargoTypeType,
    RouteLegAdditionalFeatureType,
    RouteLegTravelModeType,
    RouteLegTypeType,
    RouteMatrixErrorCodeType,
    RouteMatrixHazardousCargoTypeType,
    RouteMatrixTravelModeType,
    RouteMatrixTruckTypeType,
    RouteMatrixZoneCategoryType,
    RouteNoticeImpactType,
    RoutePedestrianNoticeCodeType,
    RoutePedestrianTravelStepTypeType,
    RouteResponseNoticeCodeType,
    RouteRoadTypeType,
    RouteSideOfStreetType,
    RouteSpanAdditionalFeatureType,
    RouteSpanCarAccessAttributeType,
    RouteSpanGateAttributeType,
    RouteSpanPedestrianAccessAttributeType,
    RouteSpanRailwayCrossingAttributeType,
    RouteSpanRoadAttributeType,
    RouteSpanScooterAccessAttributeType,
    RouteSpanTruckAccessAttributeType,
    RouteSteeringDirectionType,
    RouteTollPassValidityPeriodTypeType,
    RouteTollPaymentMethodType,
    RouteTravelModeType,
    RouteTravelStepTypeType,
    RouteTruckTypeType,
    RouteTurnIntensityType,
    RouteVehicleIncidentSeverityType,
    RouteVehicleIncidentTypeType,
    RouteVehicleNoticeCodeType,
    RouteVehicleTravelStepTypeType,
    RouteWeightConstraintTypeType,
    RouteZoneCategoryType,
    RoutingObjectiveType,
    SideOfStreetMatchingStrategyType,
    TrafficUsageType,
    WaypointOptimizationClusteringAlgorithmType,
    WaypointOptimizationConstraintType,
    WaypointOptimizationHazardousCargoTypeType,
    WaypointOptimizationSequencingObjectiveType,
    WaypointOptimizationServiceTimeTreatmentType,
    WaypointOptimizationTravelModeType,
    WaypointOptimizationTruckTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "CalculateIsolinesRequestTypeDef",
    "CalculateIsolinesResponseTypeDef",
    "CalculateRouteMatrixRequestTypeDef",
    "CalculateRouteMatrixResponseTypeDef",
    "CalculateRoutesRequestTypeDef",
    "CalculateRoutesResponseTypeDef",
    "CircleOutputTypeDef",
    "CircleTypeDef",
    "CorridorTypeDef",
    "IsolineAllowOptionsTypeDef",
    "IsolineAvoidanceAreaGeometryTypeDef",
    "IsolineAvoidanceAreaTypeDef",
    "IsolineAvoidanceOptionsTypeDef",
    "IsolineAvoidanceZoneCategoryTypeDef",
    "IsolineCarOptionsTypeDef",
    "IsolineConnectionGeometryTypeDef",
    "IsolineConnectionTypeDef",
    "IsolineDestinationOptionsTypeDef",
    "IsolineGranularityOptionsTypeDef",
    "IsolineMatchingOptionsTypeDef",
    "IsolineOriginOptionsTypeDef",
    "IsolineScooterOptionsTypeDef",
    "IsolineShapeGeometryTypeDef",
    "IsolineSideOfStreetOptionsTypeDef",
    "IsolineThresholdsTypeDef",
    "IsolineTrafficOptionsTypeDef",
    "IsolineTrailerOptionsTypeDef",
    "IsolineTravelModeOptionsTypeDef",
    "IsolineTruckOptionsTypeDef",
    "IsolineTypeDef",
    "IsolineVehicleLicensePlateTypeDef",
    "LocalizedStringTypeDef",
    "OptimizeWaypointsRequestTypeDef",
    "OptimizeWaypointsResponseTypeDef",
    "PolylineCorridorTypeDef",
    "ResponseMetadataTypeDef",
    "RoadSnapNoticeTypeDef",
    "RoadSnapSnappedGeometryTypeDef",
    "RoadSnapSnappedTracePointTypeDef",
    "RoadSnapTracePointTypeDef",
    "RoadSnapTrailerOptionsTypeDef",
    "RoadSnapTravelModeOptionsTypeDef",
    "RoadSnapTruckOptionsTypeDef",
    "RouteAllowOptionsTypeDef",
    "RouteAvoidanceAreaGeometryTypeDef",
    "RouteAvoidanceAreaTypeDef",
    "RouteAvoidanceOptionsTypeDef",
    "RouteAvoidanceZoneCategoryTypeDef",
    "RouteCarOptionsTypeDef",
    "RouteContinueHighwayStepDetailsTypeDef",
    "RouteContinueStepDetailsTypeDef",
    "RouteDestinationOptionsTypeDef",
    "RouteDriverOptionsTypeDef",
    "RouteDriverScheduleIntervalTypeDef",
    "RouteEmissionTypeTypeDef",
    "RouteEnterHighwayStepDetailsTypeDef",
    "RouteExclusionOptionsTypeDef",
    "RouteExitStepDetailsTypeDef",
    "RouteFerryAfterTravelStepTypeDef",
    "RouteFerryArrivalTypeDef",
    "RouteFerryBeforeTravelStepTypeDef",
    "RouteFerryDepartureTypeDef",
    "RouteFerryLegDetailsTypeDef",
    "RouteFerryNoticeTypeDef",
    "RouteFerryOverviewSummaryTypeDef",
    "RouteFerryPlaceTypeDef",
    "RouteFerrySpanTypeDef",
    "RouteFerrySummaryTypeDef",
    "RouteFerryTravelOnlySummaryTypeDef",
    "RouteFerryTravelStepTypeDef",
    "RouteKeepStepDetailsTypeDef",
    "RouteLegGeometryTypeDef",
    "RouteLegTypeDef",
    "RouteMajorRoadLabelTypeDef",
    "RouteMatchingOptionsTypeDef",
    "RouteMatrixAllowOptionsTypeDef",
    "RouteMatrixAutoCircleTypeDef",
    "RouteMatrixAvoidanceAreaGeometryTypeDef",
    "RouteMatrixAvoidanceAreaTypeDef",
    "RouteMatrixAvoidanceOptionsTypeDef",
    "RouteMatrixAvoidanceZoneCategoryTypeDef",
    "RouteMatrixBoundaryGeometryOutputTypeDef",
    "RouteMatrixBoundaryGeometryTypeDef",
    "RouteMatrixBoundaryOutputTypeDef",
    "RouteMatrixBoundaryTypeDef",
    "RouteMatrixBoundaryUnionTypeDef",
    "RouteMatrixCarOptionsTypeDef",
    "RouteMatrixDestinationOptionsTypeDef",
    "RouteMatrixDestinationTypeDef",
    "RouteMatrixEntryTypeDef",
    "RouteMatrixExclusionOptionsTypeDef",
    "RouteMatrixMatchingOptionsTypeDef",
    "RouteMatrixOriginOptionsTypeDef",
    "RouteMatrixOriginTypeDef",
    "RouteMatrixScooterOptionsTypeDef",
    "RouteMatrixSideOfStreetOptionsTypeDef",
    "RouteMatrixTrafficOptionsTypeDef",
    "RouteMatrixTrailerOptionsTypeDef",
    "RouteMatrixTravelModeOptionsTypeDef",
    "RouteMatrixTruckOptionsTypeDef",
    "RouteMatrixVehicleLicensePlateTypeDef",
    "RouteNoticeDetailRangeTypeDef",
    "RouteNumberTypeDef",
    "RouteOriginOptionsTypeDef",
    "RoutePassThroughPlaceTypeDef",
    "RoutePassThroughWaypointTypeDef",
    "RoutePedestrianArrivalTypeDef",
    "RoutePedestrianDepartureTypeDef",
    "RoutePedestrianLegDetailsTypeDef",
    "RoutePedestrianNoticeTypeDef",
    "RoutePedestrianOptionsTypeDef",
    "RoutePedestrianOverviewSummaryTypeDef",
    "RoutePedestrianPlaceTypeDef",
    "RoutePedestrianSpanTypeDef",
    "RoutePedestrianSummaryTypeDef",
    "RoutePedestrianTravelOnlySummaryTypeDef",
    "RoutePedestrianTravelStepTypeDef",
    "RouteRampStepDetailsTypeDef",
    "RouteResponseNoticeTypeDef",
    "RouteRoadTypeDef",
    "RouteRoundaboutEnterStepDetailsTypeDef",
    "RouteRoundaboutExitStepDetailsTypeDef",
    "RouteRoundaboutPassStepDetailsTypeDef",
    "RouteScooterOptionsTypeDef",
    "RouteSideOfStreetOptionsTypeDef",
    "RouteSignpostLabelTypeDef",
    "RouteSignpostTypeDef",
    "RouteSpanDynamicSpeedDetailsTypeDef",
    "RouteSpanSpeedLimitDetailsTypeDef",
    "RouteSummaryTypeDef",
    "RouteTollOptionsTypeDef",
    "RouteTollPassTypeDef",
    "RouteTollPassValidityPeriodTypeDef",
    "RouteTollPaymentSiteTypeDef",
    "RouteTollPriceSummaryTypeDef",
    "RouteTollPriceTypeDef",
    "RouteTollPriceValueRangeTypeDef",
    "RouteTollRateTypeDef",
    "RouteTollSummaryTypeDef",
    "RouteTollSystemTypeDef",
    "RouteTollTypeDef",
    "RouteTrafficOptionsTypeDef",
    "RouteTrailerOptionsTypeDef",
    "RouteTransponderTypeDef",
    "RouteTravelModeOptionsTypeDef",
    "RouteTruckOptionsTypeDef",
    "RouteTurnStepDetailsTypeDef",
    "RouteTypeDef",
    "RouteUTurnStepDetailsTypeDef",
    "RouteVehicleArrivalTypeDef",
    "RouteVehicleDepartureTypeDef",
    "RouteVehicleIncidentTypeDef",
    "RouteVehicleLegDetailsTypeDef",
    "RouteVehicleLicensePlateTypeDef",
    "RouteVehicleNoticeDetailTypeDef",
    "RouteVehicleNoticeTypeDef",
    "RouteVehicleOverviewSummaryTypeDef",
    "RouteVehiclePlaceTypeDef",
    "RouteVehicleSpanTypeDef",
    "RouteVehicleSummaryTypeDef",
    "RouteVehicleTravelOnlySummaryTypeDef",
    "RouteVehicleTravelStepTypeDef",
    "RouteViolatedConstraintsTypeDef",
    "RouteWaypointTypeDef",
    "RouteWeightConstraintTypeDef",
    "RouteZoneTypeDef",
    "SnapToRoadsRequestTypeDef",
    "SnapToRoadsResponseTypeDef",
    "WaypointOptimizationAccessHoursEntryTypeDef",
    "WaypointOptimizationAccessHoursTypeDef",
    "WaypointOptimizationAvoidanceAreaGeometryTypeDef",
    "WaypointOptimizationAvoidanceAreaTypeDef",
    "WaypointOptimizationAvoidanceOptionsTypeDef",
    "WaypointOptimizationClusteringOptionsTypeDef",
    "WaypointOptimizationConnectionTypeDef",
    "WaypointOptimizationDestinationOptionsTypeDef",
    "WaypointOptimizationDriverOptionsTypeDef",
    "WaypointOptimizationDrivingDistanceOptionsTypeDef",
    "WaypointOptimizationExclusionOptionsTypeDef",
    "WaypointOptimizationFailedConstraintTypeDef",
    "WaypointOptimizationImpedingWaypointTypeDef",
    "WaypointOptimizationOptimizedWaypointTypeDef",
    "WaypointOptimizationOriginOptionsTypeDef",
    "WaypointOptimizationPedestrianOptionsTypeDef",
    "WaypointOptimizationRestCycleDurationsTypeDef",
    "WaypointOptimizationRestCyclesTypeDef",
    "WaypointOptimizationRestProfileTypeDef",
    "WaypointOptimizationSideOfStreetOptionsTypeDef",
    "WaypointOptimizationTimeBreakdownTypeDef",
    "WaypointOptimizationTrafficOptionsTypeDef",
    "WaypointOptimizationTrailerOptionsTypeDef",
    "WaypointOptimizationTravelModeOptionsTypeDef",
    "WaypointOptimizationTruckOptionsTypeDef",
    "WaypointOptimizationWaypointTypeDef",
    "WeightPerAxleGroupTypeDef",
)

class IsolineAllowOptionsTypeDef(TypedDict):
    Hot: NotRequired[bool]
    Hov: NotRequired[bool]

class IsolineGranularityOptionsTypeDef(TypedDict):
    MaxPoints: NotRequired[int]
    MaxResolution: NotRequired[int]

class IsolineThresholdsTypeDef(TypedDict):
    Distance: NotRequired[Sequence[int]]
    Time: NotRequired[Sequence[int]]

class IsolineTrafficOptionsTypeDef(TypedDict):
    FlowEventThresholdOverride: NotRequired[int]
    Usage: NotRequired[TrafficUsageType]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class RouteMatrixAllowOptionsTypeDef(TypedDict):
    Hot: NotRequired[bool]
    Hov: NotRequired[bool]

class RouteMatrixExclusionOptionsTypeDef(TypedDict):
    Countries: Sequence[str]

class RouteMatrixTrafficOptionsTypeDef(TypedDict):
    FlowEventThresholdOverride: NotRequired[int]
    Usage: NotRequired[TrafficUsageType]

class RouteMatrixEntryTypeDef(TypedDict):
    Distance: int
    Duration: int
    Error: NotRequired[RouteMatrixErrorCodeType]

class RouteAllowOptionsTypeDef(TypedDict):
    Hot: NotRequired[bool]
    Hov: NotRequired[bool]

class RouteExclusionOptionsTypeDef(TypedDict):
    Countries: Sequence[str]

class RouteTrafficOptionsTypeDef(TypedDict):
    FlowEventThresholdOverride: NotRequired[int]
    Usage: NotRequired[TrafficUsageType]

class RouteResponseNoticeTypeDef(TypedDict):
    Code: RouteResponseNoticeCodeType
    Impact: NotRequired[RouteNoticeImpactType]

class CircleOutputTypeDef(TypedDict):
    Center: List[float]
    Radius: float

class CircleTypeDef(TypedDict):
    Center: Sequence[float]
    Radius: float

class CorridorTypeDef(TypedDict):
    LineString: Sequence[Sequence[float]]
    Radius: int

class PolylineCorridorTypeDef(TypedDict):
    Polyline: str
    Radius: int

class IsolineAvoidanceZoneCategoryTypeDef(TypedDict):
    Category: NotRequired[IsolineZoneCategoryType]

class IsolineVehicleLicensePlateTypeDef(TypedDict):
    LastCharacter: NotRequired[str]

class IsolineConnectionGeometryTypeDef(TypedDict):
    LineString: NotRequired[List[List[float]]]
    Polyline: NotRequired[str]

class IsolineMatchingOptionsTypeDef(TypedDict):
    NameHint: NotRequired[str]
    OnRoadThreshold: NotRequired[int]
    Radius: NotRequired[int]
    Strategy: NotRequired[MatchingStrategyType]

class IsolineSideOfStreetOptionsTypeDef(TypedDict):
    Position: Sequence[float]
    UseWith: NotRequired[SideOfStreetMatchingStrategyType]

class IsolineShapeGeometryTypeDef(TypedDict):
    Polygon: NotRequired[List[List[List[float]]]]
    PolylinePolygon: NotRequired[List[str]]

class IsolineTrailerOptionsTypeDef(TypedDict):
    AxleCount: NotRequired[int]
    TrailerCount: NotRequired[int]

class WeightPerAxleGroupTypeDef(TypedDict):
    Single: NotRequired[int]
    Tandem: NotRequired[int]
    Triple: NotRequired[int]
    Quad: NotRequired[int]
    Quint: NotRequired[int]

class LocalizedStringTypeDef(TypedDict):
    Value: str
    Language: NotRequired[str]

class WaypointOptimizationExclusionOptionsTypeDef(TypedDict):
    Countries: Sequence[str]

class WaypointOptimizationOriginOptionsTypeDef(TypedDict):
    Id: NotRequired[str]

class WaypointOptimizationTrafficOptionsTypeDef(TypedDict):
    Usage: NotRequired[TrafficUsageType]

class WaypointOptimizationConnectionTypeDef(TypedDict):
    Distance: int
    From: str
    RestDuration: int
    To: str
    TravelDuration: int
    WaitDuration: int

class WaypointOptimizationOptimizedWaypointTypeDef(TypedDict):
    DepartureTime: str
    Id: str
    Position: List[float]
    ArrivalTime: NotRequired[str]
    ClusterIndex: NotRequired[int]

class WaypointOptimizationTimeBreakdownTypeDef(TypedDict):
    RestDuration: int
    ServiceDuration: int
    TravelDuration: int
    WaitDuration: int

class RoadSnapNoticeTypeDef(TypedDict):
    Code: RoadSnapNoticeCodeType
    Title: str
    TracePointIndexes: List[int]

class RoadSnapSnappedGeometryTypeDef(TypedDict):
    LineString: NotRequired[List[List[float]]]
    Polyline: NotRequired[str]

class RoadSnapSnappedTracePointTypeDef(TypedDict):
    Confidence: float
    OriginalPosition: List[float]
    SnappedPosition: List[float]

class RoadSnapTracePointTypeDef(TypedDict):
    Position: Sequence[float]
    Heading: NotRequired[float]
    Speed: NotRequired[float]
    Timestamp: NotRequired[str]

class RoadSnapTrailerOptionsTypeDef(TypedDict):
    TrailerCount: NotRequired[int]

class RouteAvoidanceZoneCategoryTypeDef(TypedDict):
    Category: RouteZoneCategoryType

class RouteVehicleLicensePlateTypeDef(TypedDict):
    LastCharacter: NotRequired[str]

class RouteMatchingOptionsTypeDef(TypedDict):
    NameHint: NotRequired[str]
    OnRoadThreshold: NotRequired[int]
    Radius: NotRequired[int]
    Strategy: NotRequired[MatchingStrategyType]

class RouteSideOfStreetOptionsTypeDef(TypedDict):
    Position: Sequence[float]
    UseWith: NotRequired[SideOfStreetMatchingStrategyType]

class RouteDriverScheduleIntervalTypeDef(TypedDict):
    DriveDuration: int
    RestDuration: int

RouteEmissionTypeTypeDef = TypedDict(
    "RouteEmissionTypeTypeDef",
    {
        "Type": str,
        "Co2EmissionClass": NotRequired[str],
    },
)
RouteFerryAfterTravelStepTypeDef = TypedDict(
    "RouteFerryAfterTravelStepTypeDef",
    {
        "Duration": int,
        "Type": Literal["Deboard"],
        "Instruction": NotRequired[str],
    },
)

class RouteFerryPlaceTypeDef(TypedDict):
    Position: List[float]
    Name: NotRequired[str]
    OriginalPosition: NotRequired[List[float]]
    WaypointIndex: NotRequired[int]

RouteFerryBeforeTravelStepTypeDef = TypedDict(
    "RouteFerryBeforeTravelStepTypeDef",
    {
        "Duration": int,
        "Type": Literal["Board"],
        "Instruction": NotRequired[str],
    },
)

class RouteFerryNoticeTypeDef(TypedDict):
    Code: RouteFerryNoticeCodeType
    Impact: NotRequired[RouteNoticeImpactType]

RouteFerryTravelStepTypeDef = TypedDict(
    "RouteFerryTravelStepTypeDef",
    {
        "Duration": int,
        "Type": RouteFerryTravelStepTypeType,
        "Distance": NotRequired[int],
        "GeometryOffset": NotRequired[int],
        "Instruction": NotRequired[str],
    },
)

class RouteFerryOverviewSummaryTypeDef(TypedDict):
    Distance: int
    Duration: int

class RouteFerryTravelOnlySummaryTypeDef(TypedDict):
    Duration: int

class RouteLegGeometryTypeDef(TypedDict):
    LineString: NotRequired[List[List[float]]]
    Polyline: NotRequired[str]

class RouteNumberTypeDef(TypedDict):
    Value: str
    Direction: NotRequired[RouteDirectionType]
    Language: NotRequired[str]

class RouteMatrixAutoCircleTypeDef(TypedDict):
    Margin: NotRequired[int]
    MaxRadius: NotRequired[int]

class RouteMatrixAvoidanceAreaGeometryTypeDef(TypedDict):
    BoundingBox: NotRequired[Sequence[float]]
    Polygon: NotRequired[Sequence[Sequence[Sequence[float]]]]
    PolylinePolygon: NotRequired[Sequence[str]]

class RouteMatrixAvoidanceZoneCategoryTypeDef(TypedDict):
    Category: NotRequired[RouteMatrixZoneCategoryType]

class RouteMatrixVehicleLicensePlateTypeDef(TypedDict):
    LastCharacter: NotRequired[str]

class RouteMatrixMatchingOptionsTypeDef(TypedDict):
    NameHint: NotRequired[str]
    OnRoadThreshold: NotRequired[int]
    Radius: NotRequired[int]
    Strategy: NotRequired[MatchingStrategyType]

class RouteMatrixSideOfStreetOptionsTypeDef(TypedDict):
    Position: Sequence[float]
    UseWith: NotRequired[SideOfStreetMatchingStrategyType]

class RouteMatrixTrailerOptionsTypeDef(TypedDict):
    TrailerCount: NotRequired[int]

class RouteNoticeDetailRangeTypeDef(TypedDict):
    Min: NotRequired[int]
    Max: NotRequired[int]

class RoutePassThroughPlaceTypeDef(TypedDict):
    Position: List[float]
    OriginalPosition: NotRequired[List[float]]
    WaypointIndex: NotRequired[int]

class RoutePedestrianPlaceTypeDef(TypedDict):
    Position: List[float]
    Name: NotRequired[str]
    OriginalPosition: NotRequired[List[float]]
    SideOfStreet: NotRequired[RouteSideOfStreetType]
    WaypointIndex: NotRequired[int]

class RoutePedestrianNoticeTypeDef(TypedDict):
    Code: RoutePedestrianNoticeCodeType
    Impact: NotRequired[RouteNoticeImpactType]

class RoutePedestrianOptionsTypeDef(TypedDict):
    Speed: NotRequired[float]

class RoutePedestrianOverviewSummaryTypeDef(TypedDict):
    Distance: int
    Duration: int

class RouteSpanDynamicSpeedDetailsTypeDef(TypedDict):
    BestCaseSpeed: NotRequired[float]
    TurnDuration: NotRequired[int]
    TypicalSpeed: NotRequired[float]

class RouteSpanSpeedLimitDetailsTypeDef(TypedDict):
    MaxSpeed: NotRequired[float]
    Unlimited: NotRequired[bool]

class RoutePedestrianTravelOnlySummaryTypeDef(TypedDict):
    Duration: int

class RouteTollPassValidityPeriodTypeDef(TypedDict):
    Period: RouteTollPassValidityPeriodTypeType
    PeriodCount: NotRequired[int]

class RouteTollPaymentSiteTypeDef(TypedDict):
    Position: List[float]
    Name: NotRequired[str]

class RouteTollPriceValueRangeTypeDef(TypedDict):
    Min: float
    Max: float

class RouteTransponderTypeDef(TypedDict):
    SystemName: NotRequired[str]

class RouteTollSystemTypeDef(TypedDict):
    Name: NotRequired[str]

class RouteTrailerOptionsTypeDef(TypedDict):
    AxleCount: NotRequired[int]
    TrailerCount: NotRequired[int]

class RouteVehiclePlaceTypeDef(TypedDict):
    Position: List[float]
    Name: NotRequired[str]
    OriginalPosition: NotRequired[List[float]]
    SideOfStreet: NotRequired[RouteSideOfStreetType]
    WaypointIndex: NotRequired[int]

RouteVehicleIncidentTypeDef = TypedDict(
    "RouteVehicleIncidentTypeDef",
    {
        "Description": NotRequired[str],
        "EndTime": NotRequired[str],
        "Severity": NotRequired[RouteVehicleIncidentSeverityType],
        "StartTime": NotRequired[str],
        "Type": NotRequired[RouteVehicleIncidentTypeType],
    },
)

class RouteZoneTypeDef(TypedDict):
    Category: NotRequired[RouteZoneCategoryType]
    Name: NotRequired[str]

class RouteVehicleOverviewSummaryTypeDef(TypedDict):
    Distance: int
    Duration: int
    BestCaseDuration: NotRequired[int]
    TypicalDuration: NotRequired[int]

class RouteVehicleTravelOnlySummaryTypeDef(TypedDict):
    Duration: int
    BestCaseDuration: NotRequired[int]
    TypicalDuration: NotRequired[int]

RouteWeightConstraintTypeDef = TypedDict(
    "RouteWeightConstraintTypeDef",
    {
        "Type": RouteWeightConstraintTypeType,
        "Value": int,
    },
)

class WaypointOptimizationAccessHoursEntryTypeDef(TypedDict):
    DayOfWeek: DayOfWeekType
    TimeOfDay: str

class WaypointOptimizationAvoidanceAreaGeometryTypeDef(TypedDict):
    BoundingBox: NotRequired[Sequence[float]]

class WaypointOptimizationDrivingDistanceOptionsTypeDef(TypedDict):
    DrivingDistance: int

class WaypointOptimizationSideOfStreetOptionsTypeDef(TypedDict):
    Position: Sequence[float]
    UseWith: NotRequired[SideOfStreetMatchingStrategyType]

class WaypointOptimizationRestProfileTypeDef(TypedDict):
    Profile: str

class WaypointOptimizationFailedConstraintTypeDef(TypedDict):
    Constraint: NotRequired[WaypointOptimizationConstraintType]
    Reason: NotRequired[str]

class WaypointOptimizationPedestrianOptionsTypeDef(TypedDict):
    Speed: NotRequired[float]

class WaypointOptimizationRestCycleDurationsTypeDef(TypedDict):
    RestDuration: int
    WorkDuration: int

class WaypointOptimizationTrailerOptionsTypeDef(TypedDict):
    TrailerCount: NotRequired[int]

class IsolineAvoidanceAreaGeometryTypeDef(TypedDict):
    BoundingBox: NotRequired[Sequence[float]]
    Corridor: NotRequired[CorridorTypeDef]
    Polygon: NotRequired[Sequence[Sequence[Sequence[float]]]]
    PolylineCorridor: NotRequired[PolylineCorridorTypeDef]
    PolylinePolygon: NotRequired[Sequence[str]]

class RouteAvoidanceAreaGeometryTypeDef(TypedDict):
    Corridor: NotRequired[CorridorTypeDef]
    BoundingBox: NotRequired[Sequence[float]]
    Polygon: NotRequired[Sequence[Sequence[Sequence[float]]]]
    PolylineCorridor: NotRequired[PolylineCorridorTypeDef]
    PolylinePolygon: NotRequired[Sequence[str]]

class IsolineCarOptionsTypeDef(TypedDict):
    EngineType: NotRequired[IsolineEngineTypeType]
    LicensePlate: NotRequired[IsolineVehicleLicensePlateTypeDef]
    MaxSpeed: NotRequired[float]
    Occupancy: NotRequired[int]

class IsolineScooterOptionsTypeDef(TypedDict):
    EngineType: NotRequired[IsolineEngineTypeType]
    LicensePlate: NotRequired[IsolineVehicleLicensePlateTypeDef]
    MaxSpeed: NotRequired[float]
    Occupancy: NotRequired[int]

class IsolineConnectionTypeDef(TypedDict):
    FromPolygonIndex: int
    Geometry: IsolineConnectionGeometryTypeDef
    ToPolygonIndex: int

class IsolineDestinationOptionsTypeDef(TypedDict):
    AvoidActionsForDistance: NotRequired[int]
    Heading: NotRequired[float]
    Matching: NotRequired[IsolineMatchingOptionsTypeDef]
    SideOfStreet: NotRequired[IsolineSideOfStreetOptionsTypeDef]

class IsolineOriginOptionsTypeDef(TypedDict):
    AvoidActionsForDistance: NotRequired[int]
    Heading: NotRequired[float]
    Matching: NotRequired[IsolineMatchingOptionsTypeDef]
    SideOfStreet: NotRequired[IsolineSideOfStreetOptionsTypeDef]

class IsolineTruckOptionsTypeDef(TypedDict):
    AxleCount: NotRequired[int]
    EngineType: NotRequired[IsolineEngineTypeType]
    GrossWeight: NotRequired[int]
    HazardousCargos: NotRequired[Sequence[IsolineHazardousCargoTypeType]]
    Height: NotRequired[int]
    HeightAboveFirstAxle: NotRequired[int]
    KpraLength: NotRequired[int]
    Length: NotRequired[int]
    LicensePlate: NotRequired[IsolineVehicleLicensePlateTypeDef]
    MaxSpeed: NotRequired[float]
    Occupancy: NotRequired[int]
    PayloadCapacity: NotRequired[int]
    TireCount: NotRequired[int]
    Trailer: NotRequired[IsolineTrailerOptionsTypeDef]
    TruckType: NotRequired[IsolineTruckTypeType]
    TunnelRestrictionCode: NotRequired[str]
    WeightPerAxle: NotRequired[int]
    WeightPerAxleGroup: NotRequired[WeightPerAxleGroupTypeDef]
    Width: NotRequired[int]

class RouteContinueHighwayStepDetailsTypeDef(TypedDict):
    Intersection: List[LocalizedStringTypeDef]
    SteeringDirection: NotRequired[RouteSteeringDirectionType]
    TurnAngle: NotRequired[float]
    TurnIntensity: NotRequired[RouteTurnIntensityType]

class RouteContinueStepDetailsTypeDef(TypedDict):
    Intersection: List[LocalizedStringTypeDef]

class RouteEnterHighwayStepDetailsTypeDef(TypedDict):
    Intersection: List[LocalizedStringTypeDef]
    SteeringDirection: NotRequired[RouteSteeringDirectionType]
    TurnAngle: NotRequired[float]
    TurnIntensity: NotRequired[RouteTurnIntensityType]

class RouteExitStepDetailsTypeDef(TypedDict):
    Intersection: List[LocalizedStringTypeDef]
    RelativeExit: NotRequired[int]
    SteeringDirection: NotRequired[RouteSteeringDirectionType]
    TurnAngle: NotRequired[float]
    TurnIntensity: NotRequired[RouteTurnIntensityType]

class RouteFerrySpanTypeDef(TypedDict):
    Country: NotRequired[str]
    Distance: NotRequired[int]
    Duration: NotRequired[int]
    GeometryOffset: NotRequired[int]
    Names: NotRequired[List[LocalizedStringTypeDef]]
    Region: NotRequired[str]

class RouteKeepStepDetailsTypeDef(TypedDict):
    Intersection: List[LocalizedStringTypeDef]
    SteeringDirection: NotRequired[RouteSteeringDirectionType]
    TurnAngle: NotRequired[float]
    TurnIntensity: NotRequired[RouteTurnIntensityType]

class RouteRampStepDetailsTypeDef(TypedDict):
    Intersection: List[LocalizedStringTypeDef]
    SteeringDirection: NotRequired[RouteSteeringDirectionType]
    TurnAngle: NotRequired[float]
    TurnIntensity: NotRequired[RouteTurnIntensityType]

class RouteRoundaboutEnterStepDetailsTypeDef(TypedDict):
    Intersection: List[LocalizedStringTypeDef]
    SteeringDirection: NotRequired[RouteSteeringDirectionType]
    TurnAngle: NotRequired[float]
    TurnIntensity: NotRequired[RouteTurnIntensityType]

class RouteRoundaboutExitStepDetailsTypeDef(TypedDict):
    Intersection: List[LocalizedStringTypeDef]
    RelativeExit: NotRequired[int]
    RoundaboutAngle: NotRequired[float]
    SteeringDirection: NotRequired[RouteSteeringDirectionType]

class RouteRoundaboutPassStepDetailsTypeDef(TypedDict):
    Intersection: List[LocalizedStringTypeDef]
    SteeringDirection: NotRequired[RouteSteeringDirectionType]
    TurnAngle: NotRequired[float]
    TurnIntensity: NotRequired[RouteTurnIntensityType]

class RouteTurnStepDetailsTypeDef(TypedDict):
    Intersection: List[LocalizedStringTypeDef]
    SteeringDirection: NotRequired[RouteSteeringDirectionType]
    TurnAngle: NotRequired[float]
    TurnIntensity: NotRequired[RouteTurnIntensityType]

class RouteUTurnStepDetailsTypeDef(TypedDict):
    Intersection: List[LocalizedStringTypeDef]
    SteeringDirection: NotRequired[RouteSteeringDirectionType]
    TurnAngle: NotRequired[float]
    TurnIntensity: NotRequired[RouteTurnIntensityType]

class SnapToRoadsResponseTypeDef(TypedDict):
    Notices: List[RoadSnapNoticeTypeDef]
    PricingBucket: str
    SnappedGeometry: RoadSnapSnappedGeometryTypeDef
    SnappedGeometryFormat: GeometryFormatType
    SnappedTracePoints: List[RoadSnapSnappedTracePointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RoadSnapTruckOptionsTypeDef(TypedDict):
    GrossWeight: NotRequired[int]
    HazardousCargos: NotRequired[Sequence[RoadSnapHazardousCargoTypeType]]
    Height: NotRequired[int]
    Length: NotRequired[int]
    Trailer: NotRequired[RoadSnapTrailerOptionsTypeDef]
    TunnelRestrictionCode: NotRequired[str]
    Width: NotRequired[int]

class RouteCarOptionsTypeDef(TypedDict):
    EngineType: NotRequired[RouteEngineTypeType]
    LicensePlate: NotRequired[RouteVehicleLicensePlateTypeDef]
    MaxSpeed: NotRequired[float]
    Occupancy: NotRequired[int]

class RouteScooterOptionsTypeDef(TypedDict):
    EngineType: NotRequired[RouteEngineTypeType]
    LicensePlate: NotRequired[RouteVehicleLicensePlateTypeDef]
    MaxSpeed: NotRequired[float]
    Occupancy: NotRequired[int]

class RouteDestinationOptionsTypeDef(TypedDict):
    AvoidActionsForDistance: NotRequired[int]
    AvoidUTurns: NotRequired[bool]
    Heading: NotRequired[float]
    Matching: NotRequired[RouteMatchingOptionsTypeDef]
    SideOfStreet: NotRequired[RouteSideOfStreetOptionsTypeDef]
    StopDuration: NotRequired[int]

class RouteOriginOptionsTypeDef(TypedDict):
    AvoidActionsForDistance: NotRequired[int]
    AvoidUTurns: NotRequired[bool]
    Heading: NotRequired[float]
    Matching: NotRequired[RouteMatchingOptionsTypeDef]
    SideOfStreet: NotRequired[RouteSideOfStreetOptionsTypeDef]

class RouteWaypointTypeDef(TypedDict):
    Position: Sequence[float]
    AvoidActionsForDistance: NotRequired[int]
    AvoidUTurns: NotRequired[bool]
    Heading: NotRequired[float]
    Matching: NotRequired[RouteMatchingOptionsTypeDef]
    PassThrough: NotRequired[bool]
    SideOfStreet: NotRequired[RouteSideOfStreetOptionsTypeDef]
    StopDuration: NotRequired[int]

class RouteDriverOptionsTypeDef(TypedDict):
    Schedule: NotRequired[Sequence[RouteDriverScheduleIntervalTypeDef]]

class RouteTollOptionsTypeDef(TypedDict):
    AllTransponders: NotRequired[bool]
    AllVignettes: NotRequired[bool]
    Currency: NotRequired[str]
    EmissionType: NotRequired[RouteEmissionTypeTypeDef]
    VehicleCategory: NotRequired[Literal["Minibus"]]

class RouteFerryArrivalTypeDef(TypedDict):
    Place: RouteFerryPlaceTypeDef
    Time: NotRequired[str]

class RouteFerryDepartureTypeDef(TypedDict):
    Place: RouteFerryPlaceTypeDef
    Time: NotRequired[str]

class RouteFerrySummaryTypeDef(TypedDict):
    Overview: NotRequired[RouteFerryOverviewSummaryTypeDef]
    TravelOnly: NotRequired[RouteFerryTravelOnlySummaryTypeDef]

class RouteMajorRoadLabelTypeDef(TypedDict):
    RoadName: NotRequired[LocalizedStringTypeDef]
    RouteNumber: NotRequired[RouteNumberTypeDef]

RouteRoadTypeDef = TypedDict(
    "RouteRoadTypeDef",
    {
        "RoadName": List[LocalizedStringTypeDef],
        "RouteNumber": List[RouteNumberTypeDef],
        "Towards": List[LocalizedStringTypeDef],
        "Type": NotRequired[RouteRoadTypeType],
    },
)
RouteSignpostLabelTypeDef = TypedDict(
    "RouteSignpostLabelTypeDef",
    {
        "RouteNumber": NotRequired[RouteNumberTypeDef],
        "Text": NotRequired[LocalizedStringTypeDef],
    },
)

class RouteMatrixBoundaryGeometryOutputTypeDef(TypedDict):
    AutoCircle: NotRequired[RouteMatrixAutoCircleTypeDef]
    Circle: NotRequired[CircleOutputTypeDef]
    BoundingBox: NotRequired[List[float]]
    Polygon: NotRequired[List[List[List[float]]]]

class RouteMatrixBoundaryGeometryTypeDef(TypedDict):
    AutoCircle: NotRequired[RouteMatrixAutoCircleTypeDef]
    Circle: NotRequired[CircleTypeDef]
    BoundingBox: NotRequired[Sequence[float]]
    Polygon: NotRequired[Sequence[Sequence[Sequence[float]]]]

class RouteMatrixAvoidanceAreaTypeDef(TypedDict):
    Geometry: RouteMatrixAvoidanceAreaGeometryTypeDef

class RouteMatrixCarOptionsTypeDef(TypedDict):
    LicensePlate: NotRequired[RouteMatrixVehicleLicensePlateTypeDef]
    MaxSpeed: NotRequired[float]
    Occupancy: NotRequired[int]

class RouteMatrixScooterOptionsTypeDef(TypedDict):
    LicensePlate: NotRequired[RouteMatrixVehicleLicensePlateTypeDef]
    MaxSpeed: NotRequired[float]
    Occupancy: NotRequired[int]

class RouteMatrixDestinationOptionsTypeDef(TypedDict):
    AvoidActionsForDistance: NotRequired[int]
    Heading: NotRequired[float]
    Matching: NotRequired[RouteMatrixMatchingOptionsTypeDef]
    SideOfStreet: NotRequired[RouteMatrixSideOfStreetOptionsTypeDef]

class RouteMatrixOriginOptionsTypeDef(TypedDict):
    AvoidActionsForDistance: NotRequired[int]
    Heading: NotRequired[float]
    Matching: NotRequired[RouteMatrixMatchingOptionsTypeDef]
    SideOfStreet: NotRequired[RouteMatrixSideOfStreetOptionsTypeDef]

class RouteMatrixTruckOptionsTypeDef(TypedDict):
    AxleCount: NotRequired[int]
    GrossWeight: NotRequired[int]
    HazardousCargos: NotRequired[Sequence[RouteMatrixHazardousCargoTypeType]]
    Height: NotRequired[int]
    KpraLength: NotRequired[int]
    Length: NotRequired[int]
    LicensePlate: NotRequired[RouteMatrixVehicleLicensePlateTypeDef]
    MaxSpeed: NotRequired[float]
    Occupancy: NotRequired[int]
    PayloadCapacity: NotRequired[int]
    Trailer: NotRequired[RouteMatrixTrailerOptionsTypeDef]
    TruckType: NotRequired[RouteMatrixTruckTypeType]
    TunnelRestrictionCode: NotRequired[str]
    WeightPerAxle: NotRequired[int]
    WeightPerAxleGroup: NotRequired[WeightPerAxleGroupTypeDef]
    Width: NotRequired[int]

class RoutePassThroughWaypointTypeDef(TypedDict):
    Place: RoutePassThroughPlaceTypeDef
    GeometryOffset: NotRequired[int]

class RoutePedestrianArrivalTypeDef(TypedDict):
    Place: RoutePedestrianPlaceTypeDef
    Time: NotRequired[str]

class RoutePedestrianDepartureTypeDef(TypedDict):
    Place: RoutePedestrianPlaceTypeDef
    Time: NotRequired[str]

class RoutePedestrianSpanTypeDef(TypedDict):
    BestCaseDuration: NotRequired[int]
    Country: NotRequired[str]
    Distance: NotRequired[int]
    Duration: NotRequired[int]
    DynamicSpeed: NotRequired[RouteSpanDynamicSpeedDetailsTypeDef]
    FunctionalClassification: NotRequired[int]
    GeometryOffset: NotRequired[int]
    Incidents: NotRequired[List[int]]
    Names: NotRequired[List[LocalizedStringTypeDef]]
    PedestrianAccess: NotRequired[List[RouteSpanPedestrianAccessAttributeType]]
    Region: NotRequired[str]
    RoadAttributes: NotRequired[List[RouteSpanRoadAttributeType]]
    RouteNumbers: NotRequired[List[RouteNumberTypeDef]]
    SpeedLimit: NotRequired[RouteSpanSpeedLimitDetailsTypeDef]
    TypicalDuration: NotRequired[int]

class RouteVehicleSpanTypeDef(TypedDict):
    BestCaseDuration: NotRequired[int]
    CarAccess: NotRequired[List[RouteSpanCarAccessAttributeType]]
    Country: NotRequired[str]
    Distance: NotRequired[int]
    Duration: NotRequired[int]
    DynamicSpeed: NotRequired[RouteSpanDynamicSpeedDetailsTypeDef]
    FunctionalClassification: NotRequired[int]
    Gate: NotRequired[RouteSpanGateAttributeType]
    GeometryOffset: NotRequired[int]
    Incidents: NotRequired[List[int]]
    Names: NotRequired[List[LocalizedStringTypeDef]]
    Notices: NotRequired[List[int]]
    RailwayCrossing: NotRequired[RouteSpanRailwayCrossingAttributeType]
    Region: NotRequired[str]
    RoadAttributes: NotRequired[List[RouteSpanRoadAttributeType]]
    RouteNumbers: NotRequired[List[RouteNumberTypeDef]]
    ScooterAccess: NotRequired[List[RouteSpanScooterAccessAttributeType]]
    SpeedLimit: NotRequired[RouteSpanSpeedLimitDetailsTypeDef]
    TollSystems: NotRequired[List[int]]
    TruckAccess: NotRequired[List[RouteSpanTruckAccessAttributeType]]
    TruckRoadTypes: NotRequired[List[int]]
    TypicalDuration: NotRequired[int]
    Zones: NotRequired[List[int]]

class RoutePedestrianSummaryTypeDef(TypedDict):
    Overview: NotRequired[RoutePedestrianOverviewSummaryTypeDef]
    TravelOnly: NotRequired[RoutePedestrianTravelOnlySummaryTypeDef]

class RouteTollPassTypeDef(TypedDict):
    IncludesReturnTrip: NotRequired[bool]
    SeniorPass: NotRequired[bool]
    TransferCount: NotRequired[int]
    TripCount: NotRequired[int]
    ValidityPeriod: NotRequired[RouteTollPassValidityPeriodTypeDef]

class RouteTollPriceSummaryTypeDef(TypedDict):
    Currency: str
    Estimate: bool
    Range: bool
    Value: float
    RangeValue: NotRequired[RouteTollPriceValueRangeTypeDef]

class RouteTollPriceTypeDef(TypedDict):
    Currency: str
    Estimate: bool
    Range: bool
    Value: float
    PerDuration: NotRequired[int]
    RangeValue: NotRequired[RouteTollPriceValueRangeTypeDef]

class RouteTruckOptionsTypeDef(TypedDict):
    AxleCount: NotRequired[int]
    EngineType: NotRequired[RouteEngineTypeType]
    GrossWeight: NotRequired[int]
    HazardousCargos: NotRequired[Sequence[RouteHazardousCargoTypeType]]
    Height: NotRequired[int]
    HeightAboveFirstAxle: NotRequired[int]
    KpraLength: NotRequired[int]
    Length: NotRequired[int]
    LicensePlate: NotRequired[RouteVehicleLicensePlateTypeDef]
    MaxSpeed: NotRequired[float]
    Occupancy: NotRequired[int]
    PayloadCapacity: NotRequired[int]
    TireCount: NotRequired[int]
    Trailer: NotRequired[RouteTrailerOptionsTypeDef]
    TruckType: NotRequired[RouteTruckTypeType]
    TunnelRestrictionCode: NotRequired[str]
    WeightPerAxle: NotRequired[int]
    WeightPerAxleGroup: NotRequired[WeightPerAxleGroupTypeDef]
    Width: NotRequired[int]

class RouteVehicleArrivalTypeDef(TypedDict):
    Place: RouteVehiclePlaceTypeDef
    Time: NotRequired[str]

class RouteVehicleDepartureTypeDef(TypedDict):
    Place: RouteVehiclePlaceTypeDef
    Time: NotRequired[str]

class RouteVehicleSummaryTypeDef(TypedDict):
    Overview: NotRequired[RouteVehicleOverviewSummaryTypeDef]
    TravelOnly: NotRequired[RouteVehicleTravelOnlySummaryTypeDef]

class RouteViolatedConstraintsTypeDef(TypedDict):
    HazardousCargos: List[RouteHazardousCargoTypeType]
    AllHazardsRestricted: NotRequired[bool]
    AxleCount: NotRequired[RouteNoticeDetailRangeTypeDef]
    MaxHeight: NotRequired[int]
    MaxKpraLength: NotRequired[int]
    MaxLength: NotRequired[int]
    MaxPayloadCapacity: NotRequired[int]
    MaxWeight: NotRequired[RouteWeightConstraintTypeDef]
    MaxWeightPerAxle: NotRequired[int]
    MaxWeightPerAxleGroup: NotRequired[WeightPerAxleGroupTypeDef]
    MaxWidth: NotRequired[int]
    Occupancy: NotRequired[RouteNoticeDetailRangeTypeDef]
    RestrictedTimes: NotRequired[str]
    TimeDependent: NotRequired[bool]
    TrailerCount: NotRequired[RouteNoticeDetailRangeTypeDef]
    TravelMode: NotRequired[bool]
    TruckRoadType: NotRequired[str]
    TruckType: NotRequired[RouteTruckTypeType]
    TunnelRestrictionCode: NotRequired[str]

class WaypointOptimizationAccessHoursTypeDef(TypedDict):
    From: WaypointOptimizationAccessHoursEntryTypeDef
    To: WaypointOptimizationAccessHoursEntryTypeDef

class WaypointOptimizationAvoidanceAreaTypeDef(TypedDict):
    Geometry: WaypointOptimizationAvoidanceAreaGeometryTypeDef

class WaypointOptimizationClusteringOptionsTypeDef(TypedDict):
    Algorithm: WaypointOptimizationClusteringAlgorithmType
    DrivingDistanceOptions: NotRequired[WaypointOptimizationDrivingDistanceOptionsTypeDef]

class WaypointOptimizationImpedingWaypointTypeDef(TypedDict):
    FailedConstraints: List[WaypointOptimizationFailedConstraintTypeDef]
    Id: str
    Position: List[float]

class WaypointOptimizationRestCyclesTypeDef(TypedDict):
    LongCycle: WaypointOptimizationRestCycleDurationsTypeDef
    ShortCycle: WaypointOptimizationRestCycleDurationsTypeDef

class WaypointOptimizationTruckOptionsTypeDef(TypedDict):
    GrossWeight: NotRequired[int]
    HazardousCargos: NotRequired[Sequence[WaypointOptimizationHazardousCargoTypeType]]
    Height: NotRequired[int]
    Length: NotRequired[int]
    Trailer: NotRequired[WaypointOptimizationTrailerOptionsTypeDef]
    TruckType: NotRequired[WaypointOptimizationTruckTypeType]
    TunnelRestrictionCode: NotRequired[str]
    WeightPerAxle: NotRequired[int]
    Width: NotRequired[int]

class IsolineAvoidanceAreaTypeDef(TypedDict):
    Geometry: IsolineAvoidanceAreaGeometryTypeDef
    Except: NotRequired[Sequence[IsolineAvoidanceAreaGeometryTypeDef]]

class RouteAvoidanceAreaTypeDef(TypedDict):
    Geometry: RouteAvoidanceAreaGeometryTypeDef
    Except: NotRequired[Sequence[RouteAvoidanceAreaGeometryTypeDef]]

class IsolineTypeDef(TypedDict):
    Connections: List[IsolineConnectionTypeDef]
    Geometries: List[IsolineShapeGeometryTypeDef]
    DistanceThreshold: NotRequired[int]
    TimeThreshold: NotRequired[int]

class IsolineTravelModeOptionsTypeDef(TypedDict):
    Car: NotRequired[IsolineCarOptionsTypeDef]
    Scooter: NotRequired[IsolineScooterOptionsTypeDef]
    Truck: NotRequired[IsolineTruckOptionsTypeDef]

class RoadSnapTravelModeOptionsTypeDef(TypedDict):
    Truck: NotRequired[RoadSnapTruckOptionsTypeDef]

class RouteSignpostTypeDef(TypedDict):
    Labels: List[RouteSignpostLabelTypeDef]

class RouteMatrixBoundaryOutputTypeDef(TypedDict):
    Geometry: NotRequired[RouteMatrixBoundaryGeometryOutputTypeDef]
    Unbounded: NotRequired[bool]

class RouteMatrixBoundaryTypeDef(TypedDict):
    Geometry: NotRequired[RouteMatrixBoundaryGeometryTypeDef]
    Unbounded: NotRequired[bool]

class RouteMatrixAvoidanceOptionsTypeDef(TypedDict):
    Areas: NotRequired[Sequence[RouteMatrixAvoidanceAreaTypeDef]]
    CarShuttleTrains: NotRequired[bool]
    ControlledAccessHighways: NotRequired[bool]
    DirtRoads: NotRequired[bool]
    Ferries: NotRequired[bool]
    TollRoads: NotRequired[bool]
    TollTransponders: NotRequired[bool]
    TruckRoadTypes: NotRequired[Sequence[str]]
    Tunnels: NotRequired[bool]
    UTurns: NotRequired[bool]
    ZoneCategories: NotRequired[Sequence[RouteMatrixAvoidanceZoneCategoryTypeDef]]

class RouteMatrixDestinationTypeDef(TypedDict):
    Position: Sequence[float]
    Options: NotRequired[RouteMatrixDestinationOptionsTypeDef]

class RouteMatrixOriginTypeDef(TypedDict):
    Position: Sequence[float]
    Options: NotRequired[RouteMatrixOriginOptionsTypeDef]

class RouteMatrixTravelModeOptionsTypeDef(TypedDict):
    Car: NotRequired[RouteMatrixCarOptionsTypeDef]
    Scooter: NotRequired[RouteMatrixScooterOptionsTypeDef]
    Truck: NotRequired[RouteMatrixTruckOptionsTypeDef]

class RouteFerryLegDetailsTypeDef(TypedDict):
    AfterTravelSteps: List[RouteFerryAfterTravelStepTypeDef]
    Arrival: RouteFerryArrivalTypeDef
    BeforeTravelSteps: List[RouteFerryBeforeTravelStepTypeDef]
    Departure: RouteFerryDepartureTypeDef
    Notices: List[RouteFerryNoticeTypeDef]
    PassThroughWaypoints: List[RoutePassThroughWaypointTypeDef]
    Spans: List[RouteFerrySpanTypeDef]
    TravelSteps: List[RouteFerryTravelStepTypeDef]
    RouteName: NotRequired[str]
    Summary: NotRequired[RouteFerrySummaryTypeDef]

class RouteTollSummaryTypeDef(TypedDict):
    Total: NotRequired[RouteTollPriceSummaryTypeDef]

class RouteTollRateTypeDef(TypedDict):
    Id: str
    LocalPrice: RouteTollPriceTypeDef
    Name: str
    PaymentMethods: List[RouteTollPaymentMethodType]
    Transponders: List[RouteTransponderTypeDef]
    ApplicableTimes: NotRequired[str]
    ConvertedPrice: NotRequired[RouteTollPriceTypeDef]
    Pass: NotRequired[RouteTollPassTypeDef]

class RouteTravelModeOptionsTypeDef(TypedDict):
    Car: NotRequired[RouteCarOptionsTypeDef]
    Pedestrian: NotRequired[RoutePedestrianOptionsTypeDef]
    Scooter: NotRequired[RouteScooterOptionsTypeDef]
    Truck: NotRequired[RouteTruckOptionsTypeDef]

class RouteVehicleNoticeDetailTypeDef(TypedDict):
    Title: NotRequired[str]
    ViolatedConstraints: NotRequired[RouteViolatedConstraintsTypeDef]

class WaypointOptimizationDestinationOptionsTypeDef(TypedDict):
    AccessHours: NotRequired[WaypointOptimizationAccessHoursTypeDef]
    AppointmentTime: NotRequired[str]
    Heading: NotRequired[float]
    Id: NotRequired[str]
    ServiceDuration: NotRequired[int]
    SideOfStreet: NotRequired[WaypointOptimizationSideOfStreetOptionsTypeDef]

class WaypointOptimizationWaypointTypeDef(TypedDict):
    Position: Sequence[float]
    AccessHours: NotRequired[WaypointOptimizationAccessHoursTypeDef]
    AppointmentTime: NotRequired[str]
    Before: NotRequired[Sequence[int]]
    Heading: NotRequired[float]
    Id: NotRequired[str]
    ServiceDuration: NotRequired[int]
    SideOfStreet: NotRequired[WaypointOptimizationSideOfStreetOptionsTypeDef]

class WaypointOptimizationAvoidanceOptionsTypeDef(TypedDict):
    Areas: NotRequired[Sequence[WaypointOptimizationAvoidanceAreaTypeDef]]
    CarShuttleTrains: NotRequired[bool]
    ControlledAccessHighways: NotRequired[bool]
    DirtRoads: NotRequired[bool]
    Ferries: NotRequired[bool]
    TollRoads: NotRequired[bool]
    Tunnels: NotRequired[bool]
    UTurns: NotRequired[bool]

class OptimizeWaypointsResponseTypeDef(TypedDict):
    Connections: List[WaypointOptimizationConnectionTypeDef]
    Distance: int
    Duration: int
    ImpedingWaypoints: List[WaypointOptimizationImpedingWaypointTypeDef]
    OptimizedWaypoints: List[WaypointOptimizationOptimizedWaypointTypeDef]
    PricingBucket: str
    TimeBreakdown: WaypointOptimizationTimeBreakdownTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class WaypointOptimizationDriverOptionsTypeDef(TypedDict):
    RestCycles: NotRequired[WaypointOptimizationRestCyclesTypeDef]
    RestProfile: NotRequired[WaypointOptimizationRestProfileTypeDef]
    TreatServiceTimeAs: NotRequired[WaypointOptimizationServiceTimeTreatmentType]

class WaypointOptimizationTravelModeOptionsTypeDef(TypedDict):
    Pedestrian: NotRequired[WaypointOptimizationPedestrianOptionsTypeDef]
    Truck: NotRequired[WaypointOptimizationTruckOptionsTypeDef]

class IsolineAvoidanceOptionsTypeDef(TypedDict):
    Areas: NotRequired[Sequence[IsolineAvoidanceAreaTypeDef]]
    CarShuttleTrains: NotRequired[bool]
    ControlledAccessHighways: NotRequired[bool]
    DirtRoads: NotRequired[bool]
    Ferries: NotRequired[bool]
    SeasonalClosure: NotRequired[bool]
    TollRoads: NotRequired[bool]
    TollTransponders: NotRequired[bool]
    TruckRoadTypes: NotRequired[Sequence[str]]
    Tunnels: NotRequired[bool]
    UTurns: NotRequired[bool]
    ZoneCategories: NotRequired[Sequence[IsolineAvoidanceZoneCategoryTypeDef]]

class RouteAvoidanceOptionsTypeDef(TypedDict):
    Areas: NotRequired[Sequence[RouteAvoidanceAreaTypeDef]]
    CarShuttleTrains: NotRequired[bool]
    ControlledAccessHighways: NotRequired[bool]
    DirtRoads: NotRequired[bool]
    Ferries: NotRequired[bool]
    SeasonalClosure: NotRequired[bool]
    TollRoads: NotRequired[bool]
    TollTransponders: NotRequired[bool]
    TruckRoadTypes: NotRequired[Sequence[str]]
    Tunnels: NotRequired[bool]
    UTurns: NotRequired[bool]
    ZoneCategories: NotRequired[Sequence[RouteAvoidanceZoneCategoryTypeDef]]

class CalculateIsolinesResponseTypeDef(TypedDict):
    ArrivalTime: str
    DepartureTime: str
    IsolineGeometryFormat: GeometryFormatType
    Isolines: List[IsolineTypeDef]
    PricingBucket: str
    SnappedDestination: List[float]
    SnappedOrigin: List[float]
    ResponseMetadata: ResponseMetadataTypeDef

class SnapToRoadsRequestTypeDef(TypedDict):
    TracePoints: Sequence[RoadSnapTracePointTypeDef]
    Key: NotRequired[str]
    SnappedGeometryFormat: NotRequired[GeometryFormatType]
    SnapRadius: NotRequired[int]
    TravelMode: NotRequired[RoadSnapTravelModeType]
    TravelModeOptions: NotRequired[RoadSnapTravelModeOptionsTypeDef]

RoutePedestrianTravelStepTypeDef = TypedDict(
    "RoutePedestrianTravelStepTypeDef",
    {
        "Duration": int,
        "Type": RoutePedestrianTravelStepTypeType,
        "ContinueStepDetails": NotRequired[RouteContinueStepDetailsTypeDef],
        "CurrentRoad": NotRequired[RouteRoadTypeDef],
        "Distance": NotRequired[int],
        "ExitNumber": NotRequired[List[LocalizedStringTypeDef]],
        "GeometryOffset": NotRequired[int],
        "Instruction": NotRequired[str],
        "KeepStepDetails": NotRequired[RouteKeepStepDetailsTypeDef],
        "NextRoad": NotRequired[RouteRoadTypeDef],
        "RoundaboutEnterStepDetails": NotRequired[RouteRoundaboutEnterStepDetailsTypeDef],
        "RoundaboutExitStepDetails": NotRequired[RouteRoundaboutExitStepDetailsTypeDef],
        "RoundaboutPassStepDetails": NotRequired[RouteRoundaboutPassStepDetailsTypeDef],
        "Signpost": NotRequired[RouteSignpostTypeDef],
        "TurnStepDetails": NotRequired[RouteTurnStepDetailsTypeDef],
    },
)
RouteVehicleTravelStepTypeDef = TypedDict(
    "RouteVehicleTravelStepTypeDef",
    {
        "Duration": int,
        "Type": RouteVehicleTravelStepTypeType,
        "ContinueHighwayStepDetails": NotRequired[RouteContinueHighwayStepDetailsTypeDef],
        "ContinueStepDetails": NotRequired[RouteContinueStepDetailsTypeDef],
        "CurrentRoad": NotRequired[RouteRoadTypeDef],
        "Distance": NotRequired[int],
        "EnterHighwayStepDetails": NotRequired[RouteEnterHighwayStepDetailsTypeDef],
        "ExitNumber": NotRequired[List[LocalizedStringTypeDef]],
        "ExitStepDetails": NotRequired[RouteExitStepDetailsTypeDef],
        "GeometryOffset": NotRequired[int],
        "Instruction": NotRequired[str],
        "KeepStepDetails": NotRequired[RouteKeepStepDetailsTypeDef],
        "NextRoad": NotRequired[RouteRoadTypeDef],
        "RampStepDetails": NotRequired[RouteRampStepDetailsTypeDef],
        "RoundaboutEnterStepDetails": NotRequired[RouteRoundaboutEnterStepDetailsTypeDef],
        "RoundaboutExitStepDetails": NotRequired[RouteRoundaboutExitStepDetailsTypeDef],
        "RoundaboutPassStepDetails": NotRequired[RouteRoundaboutPassStepDetailsTypeDef],
        "Signpost": NotRequired[RouteSignpostTypeDef],
        "TurnStepDetails": NotRequired[RouteTurnStepDetailsTypeDef],
        "UTurnStepDetails": NotRequired[RouteUTurnStepDetailsTypeDef],
    },
)

class CalculateRouteMatrixResponseTypeDef(TypedDict):
    ErrorCount: int
    PricingBucket: str
    RouteMatrix: List[List[RouteMatrixEntryTypeDef]]
    RoutingBoundary: RouteMatrixBoundaryOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

RouteMatrixBoundaryUnionTypeDef = Union[
    RouteMatrixBoundaryTypeDef, RouteMatrixBoundaryOutputTypeDef
]

class RouteSummaryTypeDef(TypedDict):
    Distance: NotRequired[int]
    Duration: NotRequired[int]
    Tolls: NotRequired[RouteTollSummaryTypeDef]

class RouteTollTypeDef(TypedDict):
    PaymentSites: List[RouteTollPaymentSiteTypeDef]
    Rates: List[RouteTollRateTypeDef]
    Systems: List[int]
    Country: NotRequired[str]

class RouteVehicleNoticeTypeDef(TypedDict):
    Code: RouteVehicleNoticeCodeType
    Details: List[RouteVehicleNoticeDetailTypeDef]
    Impact: NotRequired[RouteNoticeImpactType]

class OptimizeWaypointsRequestTypeDef(TypedDict):
    Origin: Sequence[float]
    Avoid: NotRequired[WaypointOptimizationAvoidanceOptionsTypeDef]
    Clustering: NotRequired[WaypointOptimizationClusteringOptionsTypeDef]
    DepartureTime: NotRequired[str]
    Destination: NotRequired[Sequence[float]]
    DestinationOptions: NotRequired[WaypointOptimizationDestinationOptionsTypeDef]
    Driver: NotRequired[WaypointOptimizationDriverOptionsTypeDef]
    Exclude: NotRequired[WaypointOptimizationExclusionOptionsTypeDef]
    Key: NotRequired[str]
    OptimizeSequencingFor: NotRequired[WaypointOptimizationSequencingObjectiveType]
    OriginOptions: NotRequired[WaypointOptimizationOriginOptionsTypeDef]
    Traffic: NotRequired[WaypointOptimizationTrafficOptionsTypeDef]
    TravelMode: NotRequired[WaypointOptimizationTravelModeType]
    TravelModeOptions: NotRequired[WaypointOptimizationTravelModeOptionsTypeDef]
    Waypoints: NotRequired[Sequence[WaypointOptimizationWaypointTypeDef]]

class CalculateIsolinesRequestTypeDef(TypedDict):
    Thresholds: IsolineThresholdsTypeDef
    Allow: NotRequired[IsolineAllowOptionsTypeDef]
    ArrivalTime: NotRequired[str]
    Avoid: NotRequired[IsolineAvoidanceOptionsTypeDef]
    DepartNow: NotRequired[bool]
    DepartureTime: NotRequired[str]
    Destination: NotRequired[Sequence[float]]
    DestinationOptions: NotRequired[IsolineDestinationOptionsTypeDef]
    IsolineGeometryFormat: NotRequired[GeometryFormatType]
    IsolineGranularity: NotRequired[IsolineGranularityOptionsTypeDef]
    Key: NotRequired[str]
    OptimizeIsolineFor: NotRequired[IsolineOptimizationObjectiveType]
    OptimizeRoutingFor: NotRequired[RoutingObjectiveType]
    Origin: NotRequired[Sequence[float]]
    OriginOptions: NotRequired[IsolineOriginOptionsTypeDef]
    Traffic: NotRequired[IsolineTrafficOptionsTypeDef]
    TravelMode: NotRequired[IsolineTravelModeType]
    TravelModeOptions: NotRequired[IsolineTravelModeOptionsTypeDef]

class CalculateRoutesRequestTypeDef(TypedDict):
    Destination: Sequence[float]
    Origin: Sequence[float]
    Allow: NotRequired[RouteAllowOptionsTypeDef]
    ArrivalTime: NotRequired[str]
    Avoid: NotRequired[RouteAvoidanceOptionsTypeDef]
    DepartNow: NotRequired[bool]
    DepartureTime: NotRequired[str]
    DestinationOptions: NotRequired[RouteDestinationOptionsTypeDef]
    Driver: NotRequired[RouteDriverOptionsTypeDef]
    Exclude: NotRequired[RouteExclusionOptionsTypeDef]
    InstructionsMeasurementSystem: NotRequired[MeasurementSystemType]
    Key: NotRequired[str]
    Languages: NotRequired[Sequence[str]]
    LegAdditionalFeatures: NotRequired[Sequence[RouteLegAdditionalFeatureType]]
    LegGeometryFormat: NotRequired[GeometryFormatType]
    MaxAlternatives: NotRequired[int]
    OptimizeRoutingFor: NotRequired[RoutingObjectiveType]
    OriginOptions: NotRequired[RouteOriginOptionsTypeDef]
    SpanAdditionalFeatures: NotRequired[Sequence[RouteSpanAdditionalFeatureType]]
    Tolls: NotRequired[RouteTollOptionsTypeDef]
    Traffic: NotRequired[RouteTrafficOptionsTypeDef]
    TravelMode: NotRequired[RouteTravelModeType]
    TravelModeOptions: NotRequired[RouteTravelModeOptionsTypeDef]
    TravelStepType: NotRequired[RouteTravelStepTypeType]
    Waypoints: NotRequired[Sequence[RouteWaypointTypeDef]]

class RoutePedestrianLegDetailsTypeDef(TypedDict):
    Arrival: RoutePedestrianArrivalTypeDef
    Departure: RoutePedestrianDepartureTypeDef
    Notices: List[RoutePedestrianNoticeTypeDef]
    PassThroughWaypoints: List[RoutePassThroughWaypointTypeDef]
    Spans: List[RoutePedestrianSpanTypeDef]
    TravelSteps: List[RoutePedestrianTravelStepTypeDef]
    Summary: NotRequired[RoutePedestrianSummaryTypeDef]

class CalculateRouteMatrixRequestTypeDef(TypedDict):
    Destinations: Sequence[RouteMatrixDestinationTypeDef]
    Origins: Sequence[RouteMatrixOriginTypeDef]
    RoutingBoundary: RouteMatrixBoundaryUnionTypeDef
    Allow: NotRequired[RouteMatrixAllowOptionsTypeDef]
    Avoid: NotRequired[RouteMatrixAvoidanceOptionsTypeDef]
    DepartNow: NotRequired[bool]
    DepartureTime: NotRequired[str]
    Exclude: NotRequired[RouteMatrixExclusionOptionsTypeDef]
    Key: NotRequired[str]
    OptimizeRoutingFor: NotRequired[RoutingObjectiveType]
    Traffic: NotRequired[RouteMatrixTrafficOptionsTypeDef]
    TravelMode: NotRequired[RouteMatrixTravelModeType]
    TravelModeOptions: NotRequired[RouteMatrixTravelModeOptionsTypeDef]

class RouteVehicleLegDetailsTypeDef(TypedDict):
    Arrival: RouteVehicleArrivalTypeDef
    Departure: RouteVehicleDepartureTypeDef
    Incidents: List[RouteVehicleIncidentTypeDef]
    Notices: List[RouteVehicleNoticeTypeDef]
    PassThroughWaypoints: List[RoutePassThroughWaypointTypeDef]
    Spans: List[RouteVehicleSpanTypeDef]
    Tolls: List[RouteTollTypeDef]
    TollSystems: List[RouteTollSystemTypeDef]
    TravelSteps: List[RouteVehicleTravelStepTypeDef]
    TruckRoadTypes: List[str]
    Zones: List[RouteZoneTypeDef]
    Summary: NotRequired[RouteVehicleSummaryTypeDef]

RouteLegTypeDef = TypedDict(
    "RouteLegTypeDef",
    {
        "Geometry": RouteLegGeometryTypeDef,
        "TravelMode": RouteLegTravelModeType,
        "Type": RouteLegTypeType,
        "FerryLegDetails": NotRequired[RouteFerryLegDetailsTypeDef],
        "Language": NotRequired[str],
        "PedestrianLegDetails": NotRequired[RoutePedestrianLegDetailsTypeDef],
        "VehicleLegDetails": NotRequired[RouteVehicleLegDetailsTypeDef],
    },
)

class RouteTypeDef(TypedDict):
    Legs: List[RouteLegTypeDef]
    MajorRoadLabels: List[RouteMajorRoadLabelTypeDef]
    Summary: NotRequired[RouteSummaryTypeDef]

class CalculateRoutesResponseTypeDef(TypedDict):
    LegGeometryFormat: GeometryFormatType
    Notices: List[RouteResponseNoticeTypeDef]
    PricingBucket: str
    Routes: List[RouteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
