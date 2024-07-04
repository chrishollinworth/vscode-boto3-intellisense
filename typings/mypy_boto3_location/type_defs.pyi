"""
Type annotations for location service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/type_defs.html)

Usage::

    ```python
    from mypy_boto3_location.type_defs import ApiKeyFilterTypeDef

    data: ApiKeyFilterTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    BatchItemErrorCodeType,
    DimensionUnitType,
    DistanceUnitType,
    ForecastedGeofenceEventTypeType,
    IntendedUseType,
    OptimizationModeType,
    PositionFilteringType,
    PricingPlanType,
    RouteMatrixErrorCodeType,
    SpeedUnitType,
    StatusType,
    TravelModeType,
    VehicleWeightUnitType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ApiKeyFilterTypeDef",
    "ApiKeyRestrictionsTypeDef",
    "AssociateTrackerConsumerRequestRequestTypeDef",
    "BatchDeleteDevicePositionHistoryErrorTypeDef",
    "BatchDeleteDevicePositionHistoryRequestRequestTypeDef",
    "BatchDeleteDevicePositionHistoryResponseTypeDef",
    "BatchDeleteGeofenceErrorTypeDef",
    "BatchDeleteGeofenceRequestRequestTypeDef",
    "BatchDeleteGeofenceResponseTypeDef",
    "BatchEvaluateGeofencesErrorTypeDef",
    "BatchEvaluateGeofencesRequestRequestTypeDef",
    "BatchEvaluateGeofencesResponseTypeDef",
    "BatchGetDevicePositionErrorTypeDef",
    "BatchGetDevicePositionRequestRequestTypeDef",
    "BatchGetDevicePositionResponseTypeDef",
    "BatchItemErrorTypeDef",
    "BatchPutGeofenceErrorTypeDef",
    "BatchPutGeofenceRequestEntryTypeDef",
    "BatchPutGeofenceRequestRequestTypeDef",
    "BatchPutGeofenceResponseTypeDef",
    "BatchPutGeofenceSuccessTypeDef",
    "BatchUpdateDevicePositionErrorTypeDef",
    "BatchUpdateDevicePositionRequestRequestTypeDef",
    "BatchUpdateDevicePositionResponseTypeDef",
    "CalculateRouteCarModeOptionsTypeDef",
    "CalculateRouteMatrixRequestRequestTypeDef",
    "CalculateRouteMatrixResponseTypeDef",
    "CalculateRouteMatrixSummaryTypeDef",
    "CalculateRouteRequestRequestTypeDef",
    "CalculateRouteResponseTypeDef",
    "CalculateRouteSummaryTypeDef",
    "CalculateRouteTruckModeOptionsTypeDef",
    "CellSignalsTypeDef",
    "CircleTypeDef",
    "CreateGeofenceCollectionRequestRequestTypeDef",
    "CreateGeofenceCollectionResponseTypeDef",
    "CreateKeyRequestRequestTypeDef",
    "CreateKeyResponseTypeDef",
    "CreateMapRequestRequestTypeDef",
    "CreateMapResponseTypeDef",
    "CreatePlaceIndexRequestRequestTypeDef",
    "CreatePlaceIndexResponseTypeDef",
    "CreateRouteCalculatorRequestRequestTypeDef",
    "CreateRouteCalculatorResponseTypeDef",
    "CreateTrackerRequestRequestTypeDef",
    "CreateTrackerResponseTypeDef",
    "DataSourceConfigurationTypeDef",
    "DeleteGeofenceCollectionRequestRequestTypeDef",
    "DeleteKeyRequestRequestTypeDef",
    "DeleteMapRequestRequestTypeDef",
    "DeletePlaceIndexRequestRequestTypeDef",
    "DeleteRouteCalculatorRequestRequestTypeDef",
    "DeleteTrackerRequestRequestTypeDef",
    "DescribeGeofenceCollectionRequestRequestTypeDef",
    "DescribeGeofenceCollectionResponseTypeDef",
    "DescribeKeyRequestRequestTypeDef",
    "DescribeKeyResponseTypeDef",
    "DescribeMapRequestRequestTypeDef",
    "DescribeMapResponseTypeDef",
    "DescribePlaceIndexRequestRequestTypeDef",
    "DescribePlaceIndexResponseTypeDef",
    "DescribeRouteCalculatorRequestRequestTypeDef",
    "DescribeRouteCalculatorResponseTypeDef",
    "DescribeTrackerRequestRequestTypeDef",
    "DescribeTrackerResponseTypeDef",
    "DevicePositionTypeDef",
    "DevicePositionUpdateTypeDef",
    "DeviceStateTypeDef",
    "DisassociateTrackerConsumerRequestRequestTypeDef",
    "ForecastGeofenceEventsDeviceStateTypeDef",
    "ForecastGeofenceEventsRequestRequestTypeDef",
    "ForecastGeofenceEventsResponseTypeDef",
    "ForecastedEventTypeDef",
    "GeofenceGeometryTypeDef",
    "GetDevicePositionHistoryRequestRequestTypeDef",
    "GetDevicePositionHistoryResponseTypeDef",
    "GetDevicePositionRequestRequestTypeDef",
    "GetDevicePositionResponseTypeDef",
    "GetGeofenceRequestRequestTypeDef",
    "GetGeofenceResponseTypeDef",
    "GetMapGlyphsRequestRequestTypeDef",
    "GetMapGlyphsResponseTypeDef",
    "GetMapSpritesRequestRequestTypeDef",
    "GetMapSpritesResponseTypeDef",
    "GetMapStyleDescriptorRequestRequestTypeDef",
    "GetMapStyleDescriptorResponseTypeDef",
    "GetMapTileRequestRequestTypeDef",
    "GetMapTileResponseTypeDef",
    "GetPlaceRequestRequestTypeDef",
    "GetPlaceResponseTypeDef",
    "InferredStateTypeDef",
    "LegGeometryTypeDef",
    "LegTypeDef",
    "ListDevicePositionsRequestRequestTypeDef",
    "ListDevicePositionsResponseEntryTypeDef",
    "ListDevicePositionsResponseTypeDef",
    "ListGeofenceCollectionsRequestRequestTypeDef",
    "ListGeofenceCollectionsResponseEntryTypeDef",
    "ListGeofenceCollectionsResponseTypeDef",
    "ListGeofenceResponseEntryTypeDef",
    "ListGeofencesRequestRequestTypeDef",
    "ListGeofencesResponseTypeDef",
    "ListKeysRequestRequestTypeDef",
    "ListKeysResponseEntryTypeDef",
    "ListKeysResponseTypeDef",
    "ListMapsRequestRequestTypeDef",
    "ListMapsResponseEntryTypeDef",
    "ListMapsResponseTypeDef",
    "ListPlaceIndexesRequestRequestTypeDef",
    "ListPlaceIndexesResponseEntryTypeDef",
    "ListPlaceIndexesResponseTypeDef",
    "ListRouteCalculatorsRequestRequestTypeDef",
    "ListRouteCalculatorsResponseEntryTypeDef",
    "ListRouteCalculatorsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTrackerConsumersRequestRequestTypeDef",
    "ListTrackerConsumersResponseTypeDef",
    "ListTrackersRequestRequestTypeDef",
    "ListTrackersResponseEntryTypeDef",
    "ListTrackersResponseTypeDef",
    "LteCellDetailsTypeDef",
    "LteLocalIdTypeDef",
    "LteNetworkMeasurementsTypeDef",
    "MapConfigurationTypeDef",
    "MapConfigurationUpdateTypeDef",
    "PaginatorConfigTypeDef",
    "PlaceGeometryTypeDef",
    "PlaceTypeDef",
    "PositionalAccuracyTypeDef",
    "PutGeofenceRequestRequestTypeDef",
    "PutGeofenceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RouteMatrixEntryErrorTypeDef",
    "RouteMatrixEntryTypeDef",
    "SearchForPositionResultTypeDef",
    "SearchForSuggestionsResultTypeDef",
    "SearchForTextResultTypeDef",
    "SearchPlaceIndexForPositionRequestRequestTypeDef",
    "SearchPlaceIndexForPositionResponseTypeDef",
    "SearchPlaceIndexForPositionSummaryTypeDef",
    "SearchPlaceIndexForSuggestionsRequestRequestTypeDef",
    "SearchPlaceIndexForSuggestionsResponseTypeDef",
    "SearchPlaceIndexForSuggestionsSummaryTypeDef",
    "SearchPlaceIndexForTextRequestRequestTypeDef",
    "SearchPlaceIndexForTextResponseTypeDef",
    "SearchPlaceIndexForTextSummaryTypeDef",
    "StepTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TimeZoneTypeDef",
    "TrackingFilterGeometryTypeDef",
    "TruckDimensionsTypeDef",
    "TruckWeightTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateGeofenceCollectionRequestRequestTypeDef",
    "UpdateGeofenceCollectionResponseTypeDef",
    "UpdateKeyRequestRequestTypeDef",
    "UpdateKeyResponseTypeDef",
    "UpdateMapRequestRequestTypeDef",
    "UpdateMapResponseTypeDef",
    "UpdatePlaceIndexRequestRequestTypeDef",
    "UpdatePlaceIndexResponseTypeDef",
    "UpdateRouteCalculatorRequestRequestTypeDef",
    "UpdateRouteCalculatorResponseTypeDef",
    "UpdateTrackerRequestRequestTypeDef",
    "UpdateTrackerResponseTypeDef",
    "VerifyDevicePositionRequestRequestTypeDef",
    "VerifyDevicePositionResponseTypeDef",
    "WiFiAccessPointTypeDef",
)

ApiKeyFilterTypeDef = TypedDict(
    "ApiKeyFilterTypeDef",
    {
        "KeyStatus": StatusType,
    },
    total=False,
)

_RequiredApiKeyRestrictionsTypeDef = TypedDict(
    "_RequiredApiKeyRestrictionsTypeDef",
    {
        "AllowActions": List[str],
        "AllowResources": List[str],
    },
)
_OptionalApiKeyRestrictionsTypeDef = TypedDict(
    "_OptionalApiKeyRestrictionsTypeDef",
    {
        "AllowReferers": List[str],
    },
    total=False,
)

class ApiKeyRestrictionsTypeDef(
    _RequiredApiKeyRestrictionsTypeDef, _OptionalApiKeyRestrictionsTypeDef
):
    pass

AssociateTrackerConsumerRequestRequestTypeDef = TypedDict(
    "AssociateTrackerConsumerRequestRequestTypeDef",
    {
        "TrackerName": str,
        "ConsumerArn": str,
    },
)

BatchDeleteDevicePositionHistoryErrorTypeDef = TypedDict(
    "BatchDeleteDevicePositionHistoryErrorTypeDef",
    {
        "DeviceId": str,
        "Error": "BatchItemErrorTypeDef",
    },
)

BatchDeleteDevicePositionHistoryRequestRequestTypeDef = TypedDict(
    "BatchDeleteDevicePositionHistoryRequestRequestTypeDef",
    {
        "TrackerName": str,
        "DeviceIds": List[str],
    },
)

BatchDeleteDevicePositionHistoryResponseTypeDef = TypedDict(
    "BatchDeleteDevicePositionHistoryResponseTypeDef",
    {
        "Errors": List["BatchDeleteDevicePositionHistoryErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteGeofenceErrorTypeDef = TypedDict(
    "BatchDeleteGeofenceErrorTypeDef",
    {
        "GeofenceId": str,
        "Error": "BatchItemErrorTypeDef",
    },
)

BatchDeleteGeofenceRequestRequestTypeDef = TypedDict(
    "BatchDeleteGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "GeofenceIds": List[str],
    },
)

BatchDeleteGeofenceResponseTypeDef = TypedDict(
    "BatchDeleteGeofenceResponseTypeDef",
    {
        "Errors": List["BatchDeleteGeofenceErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchEvaluateGeofencesErrorTypeDef = TypedDict(
    "BatchEvaluateGeofencesErrorTypeDef",
    {
        "DeviceId": str,
        "SampleTime": datetime,
        "Error": "BatchItemErrorTypeDef",
    },
)

BatchEvaluateGeofencesRequestRequestTypeDef = TypedDict(
    "BatchEvaluateGeofencesRequestRequestTypeDef",
    {
        "CollectionName": str,
        "DevicePositionUpdates": List["DevicePositionUpdateTypeDef"],
    },
)

BatchEvaluateGeofencesResponseTypeDef = TypedDict(
    "BatchEvaluateGeofencesResponseTypeDef",
    {
        "Errors": List["BatchEvaluateGeofencesErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDevicePositionErrorTypeDef = TypedDict(
    "BatchGetDevicePositionErrorTypeDef",
    {
        "DeviceId": str,
        "Error": "BatchItemErrorTypeDef",
    },
)

BatchGetDevicePositionRequestRequestTypeDef = TypedDict(
    "BatchGetDevicePositionRequestRequestTypeDef",
    {
        "TrackerName": str,
        "DeviceIds": List[str],
    },
)

BatchGetDevicePositionResponseTypeDef = TypedDict(
    "BatchGetDevicePositionResponseTypeDef",
    {
        "Errors": List["BatchGetDevicePositionErrorTypeDef"],
        "DevicePositions": List["DevicePositionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchItemErrorTypeDef = TypedDict(
    "BatchItemErrorTypeDef",
    {
        "Code": BatchItemErrorCodeType,
        "Message": str,
    },
    total=False,
)

BatchPutGeofenceErrorTypeDef = TypedDict(
    "BatchPutGeofenceErrorTypeDef",
    {
        "GeofenceId": str,
        "Error": "BatchItemErrorTypeDef",
    },
)

_RequiredBatchPutGeofenceRequestEntryTypeDef = TypedDict(
    "_RequiredBatchPutGeofenceRequestEntryTypeDef",
    {
        "GeofenceId": str,
        "Geometry": "GeofenceGeometryTypeDef",
    },
)
_OptionalBatchPutGeofenceRequestEntryTypeDef = TypedDict(
    "_OptionalBatchPutGeofenceRequestEntryTypeDef",
    {
        "GeofenceProperties": Dict[str, str],
    },
    total=False,
)

class BatchPutGeofenceRequestEntryTypeDef(
    _RequiredBatchPutGeofenceRequestEntryTypeDef, _OptionalBatchPutGeofenceRequestEntryTypeDef
):
    pass

BatchPutGeofenceRequestRequestTypeDef = TypedDict(
    "BatchPutGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "Entries": List["BatchPutGeofenceRequestEntryTypeDef"],
    },
)

BatchPutGeofenceResponseTypeDef = TypedDict(
    "BatchPutGeofenceResponseTypeDef",
    {
        "Successes": List["BatchPutGeofenceSuccessTypeDef"],
        "Errors": List["BatchPutGeofenceErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPutGeofenceSuccessTypeDef = TypedDict(
    "BatchPutGeofenceSuccessTypeDef",
    {
        "GeofenceId": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
    },
)

BatchUpdateDevicePositionErrorTypeDef = TypedDict(
    "BatchUpdateDevicePositionErrorTypeDef",
    {
        "DeviceId": str,
        "SampleTime": datetime,
        "Error": "BatchItemErrorTypeDef",
    },
)

BatchUpdateDevicePositionRequestRequestTypeDef = TypedDict(
    "BatchUpdateDevicePositionRequestRequestTypeDef",
    {
        "TrackerName": str,
        "Updates": List["DevicePositionUpdateTypeDef"],
    },
)

BatchUpdateDevicePositionResponseTypeDef = TypedDict(
    "BatchUpdateDevicePositionResponseTypeDef",
    {
        "Errors": List["BatchUpdateDevicePositionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CalculateRouteCarModeOptionsTypeDef = TypedDict(
    "CalculateRouteCarModeOptionsTypeDef",
    {
        "AvoidFerries": bool,
        "AvoidTolls": bool,
    },
    total=False,
)

_RequiredCalculateRouteMatrixRequestRequestTypeDef = TypedDict(
    "_RequiredCalculateRouteMatrixRequestRequestTypeDef",
    {
        "CalculatorName": str,
        "DeparturePositions": List[List[float]],
        "DestinationPositions": List[List[float]],
    },
)
_OptionalCalculateRouteMatrixRequestRequestTypeDef = TypedDict(
    "_OptionalCalculateRouteMatrixRequestRequestTypeDef",
    {
        "TravelMode": TravelModeType,
        "DepartureTime": Union[datetime, str],
        "DepartNow": bool,
        "DistanceUnit": DistanceUnitType,
        "CarModeOptions": "CalculateRouteCarModeOptionsTypeDef",
        "TruckModeOptions": "CalculateRouteTruckModeOptionsTypeDef",
        "Key": str,
    },
    total=False,
)

class CalculateRouteMatrixRequestRequestTypeDef(
    _RequiredCalculateRouteMatrixRequestRequestTypeDef,
    _OptionalCalculateRouteMatrixRequestRequestTypeDef,
):
    pass

CalculateRouteMatrixResponseTypeDef = TypedDict(
    "CalculateRouteMatrixResponseTypeDef",
    {
        "RouteMatrix": List[List["RouteMatrixEntryTypeDef"]],
        "SnappedDeparturePositions": List[List[float]],
        "SnappedDestinationPositions": List[List[float]],
        "Summary": "CalculateRouteMatrixSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CalculateRouteMatrixSummaryTypeDef = TypedDict(
    "CalculateRouteMatrixSummaryTypeDef",
    {
        "DataSource": str,
        "RouteCount": int,
        "ErrorCount": int,
        "DistanceUnit": DistanceUnitType,
    },
)

_RequiredCalculateRouteRequestRequestTypeDef = TypedDict(
    "_RequiredCalculateRouteRequestRequestTypeDef",
    {
        "CalculatorName": str,
        "DeparturePosition": List[float],
        "DestinationPosition": List[float],
    },
)
_OptionalCalculateRouteRequestRequestTypeDef = TypedDict(
    "_OptionalCalculateRouteRequestRequestTypeDef",
    {
        "WaypointPositions": List[List[float]],
        "TravelMode": TravelModeType,
        "DepartureTime": Union[datetime, str],
        "DepartNow": bool,
        "DistanceUnit": DistanceUnitType,
        "IncludeLegGeometry": bool,
        "CarModeOptions": "CalculateRouteCarModeOptionsTypeDef",
        "TruckModeOptions": "CalculateRouteTruckModeOptionsTypeDef",
        "ArrivalTime": Union[datetime, str],
        "OptimizeFor": OptimizationModeType,
        "Key": str,
    },
    total=False,
)

class CalculateRouteRequestRequestTypeDef(
    _RequiredCalculateRouteRequestRequestTypeDef, _OptionalCalculateRouteRequestRequestTypeDef
):
    pass

CalculateRouteResponseTypeDef = TypedDict(
    "CalculateRouteResponseTypeDef",
    {
        "Legs": List["LegTypeDef"],
        "Summary": "CalculateRouteSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CalculateRouteSummaryTypeDef = TypedDict(
    "CalculateRouteSummaryTypeDef",
    {
        "RouteBBox": List[float],
        "DataSource": str,
        "Distance": float,
        "DurationSeconds": float,
        "DistanceUnit": DistanceUnitType,
    },
)

CalculateRouteTruckModeOptionsTypeDef = TypedDict(
    "CalculateRouteTruckModeOptionsTypeDef",
    {
        "AvoidFerries": bool,
        "AvoidTolls": bool,
        "Dimensions": "TruckDimensionsTypeDef",
        "Weight": "TruckWeightTypeDef",
    },
    total=False,
)

CellSignalsTypeDef = TypedDict(
    "CellSignalsTypeDef",
    {
        "LteCellDetails": List["LteCellDetailsTypeDef"],
    },
)

CircleTypeDef = TypedDict(
    "CircleTypeDef",
    {
        "Center": List[float],
        "Radius": float,
    },
)

_RequiredCreateGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
    },
)
_OptionalCreateGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGeofenceCollectionRequestRequestTypeDef",
    {
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "Description": str,
        "Tags": Dict[str, str],
        "KmsKeyId": str,
    },
    total=False,
)

class CreateGeofenceCollectionRequestRequestTypeDef(
    _RequiredCreateGeofenceCollectionRequestRequestTypeDef,
    _OptionalCreateGeofenceCollectionRequestRequestTypeDef,
):
    pass

CreateGeofenceCollectionResponseTypeDef = TypedDict(
    "CreateGeofenceCollectionResponseTypeDef",
    {
        "CollectionName": str,
        "CollectionArn": str,
        "CreateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateKeyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateKeyRequestRequestTypeDef",
    {
        "KeyName": str,
        "Restrictions": "ApiKeyRestrictionsTypeDef",
    },
)
_OptionalCreateKeyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateKeyRequestRequestTypeDef",
    {
        "Description": str,
        "ExpireTime": Union[datetime, str],
        "NoExpiry": bool,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateKeyRequestRequestTypeDef(
    _RequiredCreateKeyRequestRequestTypeDef, _OptionalCreateKeyRequestRequestTypeDef
):
    pass

CreateKeyResponseTypeDef = TypedDict(
    "CreateKeyResponseTypeDef",
    {
        "Key": str,
        "KeyArn": str,
        "KeyName": str,
        "CreateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMapRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMapRequestRequestTypeDef",
    {
        "MapName": str,
        "Configuration": "MapConfigurationTypeDef",
    },
)
_OptionalCreateMapRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMapRequestRequestTypeDef",
    {
        "PricingPlan": PricingPlanType,
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateMapRequestRequestTypeDef(
    _RequiredCreateMapRequestRequestTypeDef, _OptionalCreateMapRequestRequestTypeDef
):
    pass

CreateMapResponseTypeDef = TypedDict(
    "CreateMapResponseTypeDef",
    {
        "MapName": str,
        "MapArn": str,
        "CreateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePlaceIndexRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePlaceIndexRequestRequestTypeDef",
    {
        "IndexName": str,
        "DataSource": str,
    },
)
_OptionalCreatePlaceIndexRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePlaceIndexRequestRequestTypeDef",
    {
        "PricingPlan": PricingPlanType,
        "Description": str,
        "DataSourceConfiguration": "DataSourceConfigurationTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreatePlaceIndexRequestRequestTypeDef(
    _RequiredCreatePlaceIndexRequestRequestTypeDef, _OptionalCreatePlaceIndexRequestRequestTypeDef
):
    pass

CreatePlaceIndexResponseTypeDef = TypedDict(
    "CreatePlaceIndexResponseTypeDef",
    {
        "IndexName": str,
        "IndexArn": str,
        "CreateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRouteCalculatorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
        "DataSource": str,
    },
)
_OptionalCreateRouteCalculatorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRouteCalculatorRequestRequestTypeDef",
    {
        "PricingPlan": PricingPlanType,
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateRouteCalculatorRequestRequestTypeDef(
    _RequiredCreateRouteCalculatorRequestRequestTypeDef,
    _OptionalCreateRouteCalculatorRequestRequestTypeDef,
):
    pass

CreateRouteCalculatorResponseTypeDef = TypedDict(
    "CreateRouteCalculatorResponseTypeDef",
    {
        "CalculatorName": str,
        "CalculatorArn": str,
        "CreateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrackerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
    },
)
_OptionalCreateTrackerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrackerRequestRequestTypeDef",
    {
        "PricingPlan": PricingPlanType,
        "KmsKeyId": str,
        "PricingPlanDataSource": str,
        "Description": str,
        "Tags": Dict[str, str],
        "PositionFiltering": PositionFilteringType,
        "EventBridgeEnabled": bool,
        "KmsKeyEnableGeospatialQueries": bool,
    },
    total=False,
)

class CreateTrackerRequestRequestTypeDef(
    _RequiredCreateTrackerRequestRequestTypeDef, _OptionalCreateTrackerRequestRequestTypeDef
):
    pass

CreateTrackerResponseTypeDef = TypedDict(
    "CreateTrackerResponseTypeDef",
    {
        "TrackerName": str,
        "TrackerArn": str,
        "CreateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceConfigurationTypeDef = TypedDict(
    "DataSourceConfigurationTypeDef",
    {
        "IntendedUse": IntendedUseType,
    },
    total=False,
)

DeleteGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "DeleteGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
    },
)

_RequiredDeleteKeyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteKeyRequestRequestTypeDef",
    {
        "KeyName": str,
    },
)
_OptionalDeleteKeyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteKeyRequestRequestTypeDef",
    {
        "ForceDelete": bool,
    },
    total=False,
)

class DeleteKeyRequestRequestTypeDef(
    _RequiredDeleteKeyRequestRequestTypeDef, _OptionalDeleteKeyRequestRequestTypeDef
):
    pass

DeleteMapRequestRequestTypeDef = TypedDict(
    "DeleteMapRequestRequestTypeDef",
    {
        "MapName": str,
    },
)

DeletePlaceIndexRequestRequestTypeDef = TypedDict(
    "DeletePlaceIndexRequestRequestTypeDef",
    {
        "IndexName": str,
    },
)

DeleteRouteCalculatorRequestRequestTypeDef = TypedDict(
    "DeleteRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
    },
)

DeleteTrackerRequestRequestTypeDef = TypedDict(
    "DeleteTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
    },
)

DescribeGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "DescribeGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
    },
)

DescribeGeofenceCollectionResponseTypeDef = TypedDict(
    "DescribeGeofenceCollectionResponseTypeDef",
    {
        "CollectionName": str,
        "CollectionArn": str,
        "Description": str,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "KmsKeyId": str,
        "Tags": Dict[str, str],
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "GeofenceCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeKeyRequestRequestTypeDef = TypedDict(
    "DescribeKeyRequestRequestTypeDef",
    {
        "KeyName": str,
    },
)

DescribeKeyResponseTypeDef = TypedDict(
    "DescribeKeyResponseTypeDef",
    {
        "Key": str,
        "KeyArn": str,
        "KeyName": str,
        "Restrictions": "ApiKeyRestrictionsTypeDef",
        "CreateTime": datetime,
        "ExpireTime": datetime,
        "UpdateTime": datetime,
        "Description": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMapRequestRequestTypeDef = TypedDict(
    "DescribeMapRequestRequestTypeDef",
    {
        "MapName": str,
    },
)

DescribeMapResponseTypeDef = TypedDict(
    "DescribeMapResponseTypeDef",
    {
        "MapName": str,
        "MapArn": str,
        "PricingPlan": PricingPlanType,
        "DataSource": str,
        "Configuration": "MapConfigurationTypeDef",
        "Description": str,
        "Tags": Dict[str, str],
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePlaceIndexRequestRequestTypeDef = TypedDict(
    "DescribePlaceIndexRequestRequestTypeDef",
    {
        "IndexName": str,
    },
)

DescribePlaceIndexResponseTypeDef = TypedDict(
    "DescribePlaceIndexResponseTypeDef",
    {
        "IndexName": str,
        "IndexArn": str,
        "PricingPlan": PricingPlanType,
        "Description": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "DataSource": str,
        "DataSourceConfiguration": "DataSourceConfigurationTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRouteCalculatorRequestRequestTypeDef = TypedDict(
    "DescribeRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
    },
)

DescribeRouteCalculatorResponseTypeDef = TypedDict(
    "DescribeRouteCalculatorResponseTypeDef",
    {
        "CalculatorName": str,
        "CalculatorArn": str,
        "PricingPlan": PricingPlanType,
        "Description": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "DataSource": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrackerRequestRequestTypeDef = TypedDict(
    "DescribeTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
    },
)

DescribeTrackerResponseTypeDef = TypedDict(
    "DescribeTrackerResponseTypeDef",
    {
        "TrackerName": str,
        "TrackerArn": str,
        "Description": str,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "Tags": Dict[str, str],
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "KmsKeyId": str,
        "PositionFiltering": PositionFilteringType,
        "EventBridgeEnabled": bool,
        "KmsKeyEnableGeospatialQueries": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDevicePositionTypeDef = TypedDict(
    "_RequiredDevicePositionTypeDef",
    {
        "SampleTime": datetime,
        "ReceivedTime": datetime,
        "Position": List[float],
    },
)
_OptionalDevicePositionTypeDef = TypedDict(
    "_OptionalDevicePositionTypeDef",
    {
        "DeviceId": str,
        "Accuracy": "PositionalAccuracyTypeDef",
        "PositionProperties": Dict[str, str],
    },
    total=False,
)

class DevicePositionTypeDef(_RequiredDevicePositionTypeDef, _OptionalDevicePositionTypeDef):
    pass

_RequiredDevicePositionUpdateTypeDef = TypedDict(
    "_RequiredDevicePositionUpdateTypeDef",
    {
        "DeviceId": str,
        "SampleTime": Union[datetime, str],
        "Position": List[float],
    },
)
_OptionalDevicePositionUpdateTypeDef = TypedDict(
    "_OptionalDevicePositionUpdateTypeDef",
    {
        "Accuracy": "PositionalAccuracyTypeDef",
        "PositionProperties": Dict[str, str],
    },
    total=False,
)

class DevicePositionUpdateTypeDef(
    _RequiredDevicePositionUpdateTypeDef, _OptionalDevicePositionUpdateTypeDef
):
    pass

_RequiredDeviceStateTypeDef = TypedDict(
    "_RequiredDeviceStateTypeDef",
    {
        "DeviceId": str,
        "SampleTime": Union[datetime, str],
        "Position": List[float],
    },
)
_OptionalDeviceStateTypeDef = TypedDict(
    "_OptionalDeviceStateTypeDef",
    {
        "Accuracy": "PositionalAccuracyTypeDef",
        "Ipv4Address": str,
        "WiFiAccessPoints": List["WiFiAccessPointTypeDef"],
        "CellSignals": "CellSignalsTypeDef",
    },
    total=False,
)

class DeviceStateTypeDef(_RequiredDeviceStateTypeDef, _OptionalDeviceStateTypeDef):
    pass

DisassociateTrackerConsumerRequestRequestTypeDef = TypedDict(
    "DisassociateTrackerConsumerRequestRequestTypeDef",
    {
        "TrackerName": str,
        "ConsumerArn": str,
    },
)

_RequiredForecastGeofenceEventsDeviceStateTypeDef = TypedDict(
    "_RequiredForecastGeofenceEventsDeviceStateTypeDef",
    {
        "Position": List[float],
    },
)
_OptionalForecastGeofenceEventsDeviceStateTypeDef = TypedDict(
    "_OptionalForecastGeofenceEventsDeviceStateTypeDef",
    {
        "Speed": float,
    },
    total=False,
)

class ForecastGeofenceEventsDeviceStateTypeDef(
    _RequiredForecastGeofenceEventsDeviceStateTypeDef,
    _OptionalForecastGeofenceEventsDeviceStateTypeDef,
):
    pass

_RequiredForecastGeofenceEventsRequestRequestTypeDef = TypedDict(
    "_RequiredForecastGeofenceEventsRequestRequestTypeDef",
    {
        "CollectionName": str,
        "DeviceState": "ForecastGeofenceEventsDeviceStateTypeDef",
    },
)
_OptionalForecastGeofenceEventsRequestRequestTypeDef = TypedDict(
    "_OptionalForecastGeofenceEventsRequestRequestTypeDef",
    {
        "TimeHorizonMinutes": float,
        "DistanceUnit": DistanceUnitType,
        "SpeedUnit": SpeedUnitType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ForecastGeofenceEventsRequestRequestTypeDef(
    _RequiredForecastGeofenceEventsRequestRequestTypeDef,
    _OptionalForecastGeofenceEventsRequestRequestTypeDef,
):
    pass

ForecastGeofenceEventsResponseTypeDef = TypedDict(
    "ForecastGeofenceEventsResponseTypeDef",
    {
        "ForecastedEvents": List["ForecastedEventTypeDef"],
        "NextToken": str,
        "DistanceUnit": DistanceUnitType,
        "SpeedUnit": SpeedUnitType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredForecastedEventTypeDef = TypedDict(
    "_RequiredForecastedEventTypeDef",
    {
        "EventId": str,
        "GeofenceId": str,
        "IsDeviceInGeofence": bool,
        "NearestDistance": float,
        "EventType": ForecastedGeofenceEventTypeType,
    },
)
_OptionalForecastedEventTypeDef = TypedDict(
    "_OptionalForecastedEventTypeDef",
    {
        "ForecastedBreachTime": datetime,
        "GeofenceProperties": Dict[str, str],
    },
    total=False,
)

class ForecastedEventTypeDef(_RequiredForecastedEventTypeDef, _OptionalForecastedEventTypeDef):
    pass

GeofenceGeometryTypeDef = TypedDict(
    "GeofenceGeometryTypeDef",
    {
        "Polygon": List[List[List[float]]],
        "Circle": "CircleTypeDef",
        "Geobuf": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

_RequiredGetDevicePositionHistoryRequestRequestTypeDef = TypedDict(
    "_RequiredGetDevicePositionHistoryRequestRequestTypeDef",
    {
        "TrackerName": str,
        "DeviceId": str,
    },
)
_OptionalGetDevicePositionHistoryRequestRequestTypeDef = TypedDict(
    "_OptionalGetDevicePositionHistoryRequestRequestTypeDef",
    {
        "NextToken": str,
        "StartTimeInclusive": Union[datetime, str],
        "EndTimeExclusive": Union[datetime, str],
        "MaxResults": int,
    },
    total=False,
)

class GetDevicePositionHistoryRequestRequestTypeDef(
    _RequiredGetDevicePositionHistoryRequestRequestTypeDef,
    _OptionalGetDevicePositionHistoryRequestRequestTypeDef,
):
    pass

GetDevicePositionHistoryResponseTypeDef = TypedDict(
    "GetDevicePositionHistoryResponseTypeDef",
    {
        "DevicePositions": List["DevicePositionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDevicePositionRequestRequestTypeDef = TypedDict(
    "GetDevicePositionRequestRequestTypeDef",
    {
        "TrackerName": str,
        "DeviceId": str,
    },
)

GetDevicePositionResponseTypeDef = TypedDict(
    "GetDevicePositionResponseTypeDef",
    {
        "DeviceId": str,
        "SampleTime": datetime,
        "ReceivedTime": datetime,
        "Position": List[float],
        "Accuracy": "PositionalAccuracyTypeDef",
        "PositionProperties": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGeofenceRequestRequestTypeDef = TypedDict(
    "GetGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "GeofenceId": str,
    },
)

GetGeofenceResponseTypeDef = TypedDict(
    "GetGeofenceResponseTypeDef",
    {
        "GeofenceId": str,
        "Geometry": "GeofenceGeometryTypeDef",
        "Status": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "GeofenceProperties": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMapGlyphsRequestRequestTypeDef = TypedDict(
    "_RequiredGetMapGlyphsRequestRequestTypeDef",
    {
        "MapName": str,
        "FontStack": str,
        "FontUnicodeRange": str,
    },
)
_OptionalGetMapGlyphsRequestRequestTypeDef = TypedDict(
    "_OptionalGetMapGlyphsRequestRequestTypeDef",
    {
        "Key": str,
    },
    total=False,
)

class GetMapGlyphsRequestRequestTypeDef(
    _RequiredGetMapGlyphsRequestRequestTypeDef, _OptionalGetMapGlyphsRequestRequestTypeDef
):
    pass

GetMapGlyphsResponseTypeDef = TypedDict(
    "GetMapGlyphsResponseTypeDef",
    {
        "Blob": bytes,
        "ContentType": str,
        "CacheControl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMapSpritesRequestRequestTypeDef = TypedDict(
    "_RequiredGetMapSpritesRequestRequestTypeDef",
    {
        "MapName": str,
        "FileName": str,
    },
)
_OptionalGetMapSpritesRequestRequestTypeDef = TypedDict(
    "_OptionalGetMapSpritesRequestRequestTypeDef",
    {
        "Key": str,
    },
    total=False,
)

class GetMapSpritesRequestRequestTypeDef(
    _RequiredGetMapSpritesRequestRequestTypeDef, _OptionalGetMapSpritesRequestRequestTypeDef
):
    pass

GetMapSpritesResponseTypeDef = TypedDict(
    "GetMapSpritesResponseTypeDef",
    {
        "Blob": bytes,
        "ContentType": str,
        "CacheControl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMapStyleDescriptorRequestRequestTypeDef = TypedDict(
    "_RequiredGetMapStyleDescriptorRequestRequestTypeDef",
    {
        "MapName": str,
    },
)
_OptionalGetMapStyleDescriptorRequestRequestTypeDef = TypedDict(
    "_OptionalGetMapStyleDescriptorRequestRequestTypeDef",
    {
        "Key": str,
    },
    total=False,
)

class GetMapStyleDescriptorRequestRequestTypeDef(
    _RequiredGetMapStyleDescriptorRequestRequestTypeDef,
    _OptionalGetMapStyleDescriptorRequestRequestTypeDef,
):
    pass

GetMapStyleDescriptorResponseTypeDef = TypedDict(
    "GetMapStyleDescriptorResponseTypeDef",
    {
        "Blob": bytes,
        "ContentType": str,
        "CacheControl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMapTileRequestRequestTypeDef = TypedDict(
    "_RequiredGetMapTileRequestRequestTypeDef",
    {
        "MapName": str,
        "Z": str,
        "X": str,
        "Y": str,
    },
)
_OptionalGetMapTileRequestRequestTypeDef = TypedDict(
    "_OptionalGetMapTileRequestRequestTypeDef",
    {
        "Key": str,
    },
    total=False,
)

class GetMapTileRequestRequestTypeDef(
    _RequiredGetMapTileRequestRequestTypeDef, _OptionalGetMapTileRequestRequestTypeDef
):
    pass

GetMapTileResponseTypeDef = TypedDict(
    "GetMapTileResponseTypeDef",
    {
        "Blob": bytes,
        "ContentType": str,
        "CacheControl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPlaceRequestRequestTypeDef = TypedDict(
    "_RequiredGetPlaceRequestRequestTypeDef",
    {
        "IndexName": str,
        "PlaceId": str,
    },
)
_OptionalGetPlaceRequestRequestTypeDef = TypedDict(
    "_OptionalGetPlaceRequestRequestTypeDef",
    {
        "Language": str,
        "Key": str,
    },
    total=False,
)

class GetPlaceRequestRequestTypeDef(
    _RequiredGetPlaceRequestRequestTypeDef, _OptionalGetPlaceRequestRequestTypeDef
):
    pass

GetPlaceResponseTypeDef = TypedDict(
    "GetPlaceResponseTypeDef",
    {
        "Place": "PlaceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredInferredStateTypeDef = TypedDict(
    "_RequiredInferredStateTypeDef",
    {
        "ProxyDetected": bool,
    },
)
_OptionalInferredStateTypeDef = TypedDict(
    "_OptionalInferredStateTypeDef",
    {
        "Position": List[float],
        "Accuracy": "PositionalAccuracyTypeDef",
        "DeviationDistance": float,
    },
    total=False,
)

class InferredStateTypeDef(_RequiredInferredStateTypeDef, _OptionalInferredStateTypeDef):
    pass

LegGeometryTypeDef = TypedDict(
    "LegGeometryTypeDef",
    {
        "LineString": List[List[float]],
    },
    total=False,
)

_RequiredLegTypeDef = TypedDict(
    "_RequiredLegTypeDef",
    {
        "StartPosition": List[float],
        "EndPosition": List[float],
        "Distance": float,
        "DurationSeconds": float,
        "Steps": List["StepTypeDef"],
    },
)
_OptionalLegTypeDef = TypedDict(
    "_OptionalLegTypeDef",
    {
        "Geometry": "LegGeometryTypeDef",
    },
    total=False,
)

class LegTypeDef(_RequiredLegTypeDef, _OptionalLegTypeDef):
    pass

_RequiredListDevicePositionsRequestRequestTypeDef = TypedDict(
    "_RequiredListDevicePositionsRequestRequestTypeDef",
    {
        "TrackerName": str,
    },
)
_OptionalListDevicePositionsRequestRequestTypeDef = TypedDict(
    "_OptionalListDevicePositionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "FilterGeometry": "TrackingFilterGeometryTypeDef",
    },
    total=False,
)

class ListDevicePositionsRequestRequestTypeDef(
    _RequiredListDevicePositionsRequestRequestTypeDef,
    _OptionalListDevicePositionsRequestRequestTypeDef,
):
    pass

_RequiredListDevicePositionsResponseEntryTypeDef = TypedDict(
    "_RequiredListDevicePositionsResponseEntryTypeDef",
    {
        "DeviceId": str,
        "SampleTime": datetime,
        "Position": List[float],
    },
)
_OptionalListDevicePositionsResponseEntryTypeDef = TypedDict(
    "_OptionalListDevicePositionsResponseEntryTypeDef",
    {
        "Accuracy": "PositionalAccuracyTypeDef",
        "PositionProperties": Dict[str, str],
    },
    total=False,
)

class ListDevicePositionsResponseEntryTypeDef(
    _RequiredListDevicePositionsResponseEntryTypeDef,
    _OptionalListDevicePositionsResponseEntryTypeDef,
):
    pass

ListDevicePositionsResponseTypeDef = TypedDict(
    "ListDevicePositionsResponseTypeDef",
    {
        "Entries": List["ListDevicePositionsResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGeofenceCollectionsRequestRequestTypeDef = TypedDict(
    "ListGeofenceCollectionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListGeofenceCollectionsResponseEntryTypeDef = TypedDict(
    "_RequiredListGeofenceCollectionsResponseEntryTypeDef",
    {
        "CollectionName": str,
        "Description": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
    },
)
_OptionalListGeofenceCollectionsResponseEntryTypeDef = TypedDict(
    "_OptionalListGeofenceCollectionsResponseEntryTypeDef",
    {
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
    },
    total=False,
)

class ListGeofenceCollectionsResponseEntryTypeDef(
    _RequiredListGeofenceCollectionsResponseEntryTypeDef,
    _OptionalListGeofenceCollectionsResponseEntryTypeDef,
):
    pass

ListGeofenceCollectionsResponseTypeDef = TypedDict(
    "ListGeofenceCollectionsResponseTypeDef",
    {
        "Entries": List["ListGeofenceCollectionsResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGeofenceResponseEntryTypeDef = TypedDict(
    "_RequiredListGeofenceResponseEntryTypeDef",
    {
        "GeofenceId": str,
        "Geometry": "GeofenceGeometryTypeDef",
        "Status": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
    },
)
_OptionalListGeofenceResponseEntryTypeDef = TypedDict(
    "_OptionalListGeofenceResponseEntryTypeDef",
    {
        "GeofenceProperties": Dict[str, str],
    },
    total=False,
)

class ListGeofenceResponseEntryTypeDef(
    _RequiredListGeofenceResponseEntryTypeDef, _OptionalListGeofenceResponseEntryTypeDef
):
    pass

_RequiredListGeofencesRequestRequestTypeDef = TypedDict(
    "_RequiredListGeofencesRequestRequestTypeDef",
    {
        "CollectionName": str,
    },
)
_OptionalListGeofencesRequestRequestTypeDef = TypedDict(
    "_OptionalListGeofencesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListGeofencesRequestRequestTypeDef(
    _RequiredListGeofencesRequestRequestTypeDef, _OptionalListGeofencesRequestRequestTypeDef
):
    pass

ListGeofencesResponseTypeDef = TypedDict(
    "ListGeofencesResponseTypeDef",
    {
        "Entries": List["ListGeofenceResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKeysRequestRequestTypeDef = TypedDict(
    "ListKeysRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filter": "ApiKeyFilterTypeDef",
    },
    total=False,
)

_RequiredListKeysResponseEntryTypeDef = TypedDict(
    "_RequiredListKeysResponseEntryTypeDef",
    {
        "KeyName": str,
        "ExpireTime": datetime,
        "Restrictions": "ApiKeyRestrictionsTypeDef",
        "CreateTime": datetime,
        "UpdateTime": datetime,
    },
)
_OptionalListKeysResponseEntryTypeDef = TypedDict(
    "_OptionalListKeysResponseEntryTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class ListKeysResponseEntryTypeDef(
    _RequiredListKeysResponseEntryTypeDef, _OptionalListKeysResponseEntryTypeDef
):
    pass

ListKeysResponseTypeDef = TypedDict(
    "ListKeysResponseTypeDef",
    {
        "Entries": List["ListKeysResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMapsRequestRequestTypeDef = TypedDict(
    "ListMapsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListMapsResponseEntryTypeDef = TypedDict(
    "_RequiredListMapsResponseEntryTypeDef",
    {
        "MapName": str,
        "Description": str,
        "DataSource": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
    },
)
_OptionalListMapsResponseEntryTypeDef = TypedDict(
    "_OptionalListMapsResponseEntryTypeDef",
    {
        "PricingPlan": PricingPlanType,
    },
    total=False,
)

class ListMapsResponseEntryTypeDef(
    _RequiredListMapsResponseEntryTypeDef, _OptionalListMapsResponseEntryTypeDef
):
    pass

ListMapsResponseTypeDef = TypedDict(
    "ListMapsResponseTypeDef",
    {
        "Entries": List["ListMapsResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPlaceIndexesRequestRequestTypeDef = TypedDict(
    "ListPlaceIndexesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListPlaceIndexesResponseEntryTypeDef = TypedDict(
    "_RequiredListPlaceIndexesResponseEntryTypeDef",
    {
        "IndexName": str,
        "Description": str,
        "DataSource": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
    },
)
_OptionalListPlaceIndexesResponseEntryTypeDef = TypedDict(
    "_OptionalListPlaceIndexesResponseEntryTypeDef",
    {
        "PricingPlan": PricingPlanType,
    },
    total=False,
)

class ListPlaceIndexesResponseEntryTypeDef(
    _RequiredListPlaceIndexesResponseEntryTypeDef, _OptionalListPlaceIndexesResponseEntryTypeDef
):
    pass

ListPlaceIndexesResponseTypeDef = TypedDict(
    "ListPlaceIndexesResponseTypeDef",
    {
        "Entries": List["ListPlaceIndexesResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRouteCalculatorsRequestRequestTypeDef = TypedDict(
    "ListRouteCalculatorsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListRouteCalculatorsResponseEntryTypeDef = TypedDict(
    "_RequiredListRouteCalculatorsResponseEntryTypeDef",
    {
        "CalculatorName": str,
        "Description": str,
        "DataSource": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
    },
)
_OptionalListRouteCalculatorsResponseEntryTypeDef = TypedDict(
    "_OptionalListRouteCalculatorsResponseEntryTypeDef",
    {
        "PricingPlan": PricingPlanType,
    },
    total=False,
)

class ListRouteCalculatorsResponseEntryTypeDef(
    _RequiredListRouteCalculatorsResponseEntryTypeDef,
    _OptionalListRouteCalculatorsResponseEntryTypeDef,
):
    pass

ListRouteCalculatorsResponseTypeDef = TypedDict(
    "ListRouteCalculatorsResponseTypeDef",
    {
        "Entries": List["ListRouteCalculatorsResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTrackerConsumersRequestRequestTypeDef = TypedDict(
    "_RequiredListTrackerConsumersRequestRequestTypeDef",
    {
        "TrackerName": str,
    },
)
_OptionalListTrackerConsumersRequestRequestTypeDef = TypedDict(
    "_OptionalListTrackerConsumersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListTrackerConsumersRequestRequestTypeDef(
    _RequiredListTrackerConsumersRequestRequestTypeDef,
    _OptionalListTrackerConsumersRequestRequestTypeDef,
):
    pass

ListTrackerConsumersResponseTypeDef = TypedDict(
    "ListTrackerConsumersResponseTypeDef",
    {
        "ConsumerArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrackersRequestRequestTypeDef = TypedDict(
    "ListTrackersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListTrackersResponseEntryTypeDef = TypedDict(
    "_RequiredListTrackersResponseEntryTypeDef",
    {
        "TrackerName": str,
        "Description": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
    },
)
_OptionalListTrackersResponseEntryTypeDef = TypedDict(
    "_OptionalListTrackersResponseEntryTypeDef",
    {
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
    },
    total=False,
)

class ListTrackersResponseEntryTypeDef(
    _RequiredListTrackersResponseEntryTypeDef, _OptionalListTrackersResponseEntryTypeDef
):
    pass

ListTrackersResponseTypeDef = TypedDict(
    "ListTrackersResponseTypeDef",
    {
        "Entries": List["ListTrackersResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLteCellDetailsTypeDef = TypedDict(
    "_RequiredLteCellDetailsTypeDef",
    {
        "CellId": int,
        "Mcc": int,
        "Mnc": int,
    },
)
_OptionalLteCellDetailsTypeDef = TypedDict(
    "_OptionalLteCellDetailsTypeDef",
    {
        "LocalId": "LteLocalIdTypeDef",
        "NetworkMeasurements": List["LteNetworkMeasurementsTypeDef"],
        "TimingAdvance": int,
        "NrCapable": bool,
        "Rsrp": int,
        "Rsrq": float,
        "Tac": int,
    },
    total=False,
)

class LteCellDetailsTypeDef(_RequiredLteCellDetailsTypeDef, _OptionalLteCellDetailsTypeDef):
    pass

LteLocalIdTypeDef = TypedDict(
    "LteLocalIdTypeDef",
    {
        "Earfcn": int,
        "Pci": int,
    },
)

_RequiredLteNetworkMeasurementsTypeDef = TypedDict(
    "_RequiredLteNetworkMeasurementsTypeDef",
    {
        "Earfcn": int,
        "CellId": int,
        "Pci": int,
    },
)
_OptionalLteNetworkMeasurementsTypeDef = TypedDict(
    "_OptionalLteNetworkMeasurementsTypeDef",
    {
        "Rsrp": int,
        "Rsrq": float,
    },
    total=False,
)

class LteNetworkMeasurementsTypeDef(
    _RequiredLteNetworkMeasurementsTypeDef, _OptionalLteNetworkMeasurementsTypeDef
):
    pass

_RequiredMapConfigurationTypeDef = TypedDict(
    "_RequiredMapConfigurationTypeDef",
    {
        "Style": str,
    },
)
_OptionalMapConfigurationTypeDef = TypedDict(
    "_OptionalMapConfigurationTypeDef",
    {
        "PoliticalView": str,
        "CustomLayers": List[str],
    },
    total=False,
)

class MapConfigurationTypeDef(_RequiredMapConfigurationTypeDef, _OptionalMapConfigurationTypeDef):
    pass

MapConfigurationUpdateTypeDef = TypedDict(
    "MapConfigurationUpdateTypeDef",
    {
        "PoliticalView": str,
        "CustomLayers": List[str],
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PlaceGeometryTypeDef = TypedDict(
    "PlaceGeometryTypeDef",
    {
        "Point": List[float],
    },
    total=False,
)

_RequiredPlaceTypeDef = TypedDict(
    "_RequiredPlaceTypeDef",
    {
        "Geometry": "PlaceGeometryTypeDef",
    },
)
_OptionalPlaceTypeDef = TypedDict(
    "_OptionalPlaceTypeDef",
    {
        "Label": str,
        "AddressNumber": str,
        "Street": str,
        "Neighborhood": str,
        "Municipality": str,
        "SubRegion": str,
        "Region": str,
        "Country": str,
        "PostalCode": str,
        "Interpolated": bool,
        "TimeZone": "TimeZoneTypeDef",
        "UnitType": str,
        "UnitNumber": str,
        "Categories": List[str],
        "SupplementalCategories": List[str],
        "SubMunicipality": str,
    },
    total=False,
)

class PlaceTypeDef(_RequiredPlaceTypeDef, _OptionalPlaceTypeDef):
    pass

PositionalAccuracyTypeDef = TypedDict(
    "PositionalAccuracyTypeDef",
    {
        "Horizontal": float,
    },
)

_RequiredPutGeofenceRequestRequestTypeDef = TypedDict(
    "_RequiredPutGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "GeofenceId": str,
        "Geometry": "GeofenceGeometryTypeDef",
    },
)
_OptionalPutGeofenceRequestRequestTypeDef = TypedDict(
    "_OptionalPutGeofenceRequestRequestTypeDef",
    {
        "GeofenceProperties": Dict[str, str],
    },
    total=False,
)

class PutGeofenceRequestRequestTypeDef(
    _RequiredPutGeofenceRequestRequestTypeDef, _OptionalPutGeofenceRequestRequestTypeDef
):
    pass

PutGeofenceResponseTypeDef = TypedDict(
    "PutGeofenceResponseTypeDef",
    {
        "GeofenceId": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredRouteMatrixEntryErrorTypeDef = TypedDict(
    "_RequiredRouteMatrixEntryErrorTypeDef",
    {
        "Code": RouteMatrixErrorCodeType,
    },
)
_OptionalRouteMatrixEntryErrorTypeDef = TypedDict(
    "_OptionalRouteMatrixEntryErrorTypeDef",
    {
        "Message": str,
    },
    total=False,
)

class RouteMatrixEntryErrorTypeDef(
    _RequiredRouteMatrixEntryErrorTypeDef, _OptionalRouteMatrixEntryErrorTypeDef
):
    pass

RouteMatrixEntryTypeDef = TypedDict(
    "RouteMatrixEntryTypeDef",
    {
        "Distance": float,
        "DurationSeconds": float,
        "Error": "RouteMatrixEntryErrorTypeDef",
    },
    total=False,
)

_RequiredSearchForPositionResultTypeDef = TypedDict(
    "_RequiredSearchForPositionResultTypeDef",
    {
        "Place": "PlaceTypeDef",
        "Distance": float,
    },
)
_OptionalSearchForPositionResultTypeDef = TypedDict(
    "_OptionalSearchForPositionResultTypeDef",
    {
        "PlaceId": str,
    },
    total=False,
)

class SearchForPositionResultTypeDef(
    _RequiredSearchForPositionResultTypeDef, _OptionalSearchForPositionResultTypeDef
):
    pass

_RequiredSearchForSuggestionsResultTypeDef = TypedDict(
    "_RequiredSearchForSuggestionsResultTypeDef",
    {
        "Text": str,
    },
)
_OptionalSearchForSuggestionsResultTypeDef = TypedDict(
    "_OptionalSearchForSuggestionsResultTypeDef",
    {
        "PlaceId": str,
        "Categories": List[str],
        "SupplementalCategories": List[str],
    },
    total=False,
)

class SearchForSuggestionsResultTypeDef(
    _RequiredSearchForSuggestionsResultTypeDef, _OptionalSearchForSuggestionsResultTypeDef
):
    pass

_RequiredSearchForTextResultTypeDef = TypedDict(
    "_RequiredSearchForTextResultTypeDef",
    {
        "Place": "PlaceTypeDef",
    },
)
_OptionalSearchForTextResultTypeDef = TypedDict(
    "_OptionalSearchForTextResultTypeDef",
    {
        "Distance": float,
        "Relevance": float,
        "PlaceId": str,
    },
    total=False,
)

class SearchForTextResultTypeDef(
    _RequiredSearchForTextResultTypeDef, _OptionalSearchForTextResultTypeDef
):
    pass

_RequiredSearchPlaceIndexForPositionRequestRequestTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForPositionRequestRequestTypeDef",
    {
        "IndexName": str,
        "Position": List[float],
    },
)
_OptionalSearchPlaceIndexForPositionRequestRequestTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForPositionRequestRequestTypeDef",
    {
        "MaxResults": int,
        "Language": str,
        "Key": str,
    },
    total=False,
)

class SearchPlaceIndexForPositionRequestRequestTypeDef(
    _RequiredSearchPlaceIndexForPositionRequestRequestTypeDef,
    _OptionalSearchPlaceIndexForPositionRequestRequestTypeDef,
):
    pass

SearchPlaceIndexForPositionResponseTypeDef = TypedDict(
    "SearchPlaceIndexForPositionResponseTypeDef",
    {
        "Summary": "SearchPlaceIndexForPositionSummaryTypeDef",
        "Results": List["SearchForPositionResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchPlaceIndexForPositionSummaryTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForPositionSummaryTypeDef",
    {
        "Position": List[float],
        "DataSource": str,
    },
)
_OptionalSearchPlaceIndexForPositionSummaryTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForPositionSummaryTypeDef",
    {
        "MaxResults": int,
        "Language": str,
    },
    total=False,
)

class SearchPlaceIndexForPositionSummaryTypeDef(
    _RequiredSearchPlaceIndexForPositionSummaryTypeDef,
    _OptionalSearchPlaceIndexForPositionSummaryTypeDef,
):
    pass

_RequiredSearchPlaceIndexForSuggestionsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForSuggestionsRequestRequestTypeDef",
    {
        "IndexName": str,
        "Text": str,
    },
)
_OptionalSearchPlaceIndexForSuggestionsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForSuggestionsRequestRequestTypeDef",
    {
        "BiasPosition": List[float],
        "FilterBBox": List[float],
        "FilterCountries": List[str],
        "MaxResults": int,
        "Language": str,
        "FilterCategories": List[str],
        "Key": str,
    },
    total=False,
)

class SearchPlaceIndexForSuggestionsRequestRequestTypeDef(
    _RequiredSearchPlaceIndexForSuggestionsRequestRequestTypeDef,
    _OptionalSearchPlaceIndexForSuggestionsRequestRequestTypeDef,
):
    pass

SearchPlaceIndexForSuggestionsResponseTypeDef = TypedDict(
    "SearchPlaceIndexForSuggestionsResponseTypeDef",
    {
        "Summary": "SearchPlaceIndexForSuggestionsSummaryTypeDef",
        "Results": List["SearchForSuggestionsResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchPlaceIndexForSuggestionsSummaryTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForSuggestionsSummaryTypeDef",
    {
        "Text": str,
        "DataSource": str,
    },
)
_OptionalSearchPlaceIndexForSuggestionsSummaryTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForSuggestionsSummaryTypeDef",
    {
        "BiasPosition": List[float],
        "FilterBBox": List[float],
        "FilterCountries": List[str],
        "MaxResults": int,
        "Language": str,
        "FilterCategories": List[str],
    },
    total=False,
)

class SearchPlaceIndexForSuggestionsSummaryTypeDef(
    _RequiredSearchPlaceIndexForSuggestionsSummaryTypeDef,
    _OptionalSearchPlaceIndexForSuggestionsSummaryTypeDef,
):
    pass

_RequiredSearchPlaceIndexForTextRequestRequestTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForTextRequestRequestTypeDef",
    {
        "IndexName": str,
        "Text": str,
    },
)
_OptionalSearchPlaceIndexForTextRequestRequestTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForTextRequestRequestTypeDef",
    {
        "BiasPosition": List[float],
        "FilterBBox": List[float],
        "FilterCountries": List[str],
        "MaxResults": int,
        "Language": str,
        "FilterCategories": List[str],
        "Key": str,
    },
    total=False,
)

class SearchPlaceIndexForTextRequestRequestTypeDef(
    _RequiredSearchPlaceIndexForTextRequestRequestTypeDef,
    _OptionalSearchPlaceIndexForTextRequestRequestTypeDef,
):
    pass

SearchPlaceIndexForTextResponseTypeDef = TypedDict(
    "SearchPlaceIndexForTextResponseTypeDef",
    {
        "Summary": "SearchPlaceIndexForTextSummaryTypeDef",
        "Results": List["SearchForTextResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchPlaceIndexForTextSummaryTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForTextSummaryTypeDef",
    {
        "Text": str,
        "DataSource": str,
    },
)
_OptionalSearchPlaceIndexForTextSummaryTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForTextSummaryTypeDef",
    {
        "BiasPosition": List[float],
        "FilterBBox": List[float],
        "FilterCountries": List[str],
        "MaxResults": int,
        "ResultBBox": List[float],
        "Language": str,
        "FilterCategories": List[str],
    },
    total=False,
)

class SearchPlaceIndexForTextSummaryTypeDef(
    _RequiredSearchPlaceIndexForTextSummaryTypeDef, _OptionalSearchPlaceIndexForTextSummaryTypeDef
):
    pass

_RequiredStepTypeDef = TypedDict(
    "_RequiredStepTypeDef",
    {
        "StartPosition": List[float],
        "EndPosition": List[float],
        "Distance": float,
        "DurationSeconds": float,
    },
)
_OptionalStepTypeDef = TypedDict(
    "_OptionalStepTypeDef",
    {
        "GeometryOffset": int,
    },
    total=False,
)

class StepTypeDef(_RequiredStepTypeDef, _OptionalStepTypeDef):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

_RequiredTimeZoneTypeDef = TypedDict(
    "_RequiredTimeZoneTypeDef",
    {
        "Name": str,
    },
)
_OptionalTimeZoneTypeDef = TypedDict(
    "_OptionalTimeZoneTypeDef",
    {
        "Offset": int,
    },
    total=False,
)

class TimeZoneTypeDef(_RequiredTimeZoneTypeDef, _OptionalTimeZoneTypeDef):
    pass

TrackingFilterGeometryTypeDef = TypedDict(
    "TrackingFilterGeometryTypeDef",
    {
        "Polygon": List[List[List[float]]],
    },
    total=False,
)

TruckDimensionsTypeDef = TypedDict(
    "TruckDimensionsTypeDef",
    {
        "Length": float,
        "Height": float,
        "Width": float,
        "Unit": DimensionUnitType,
    },
    total=False,
)

TruckWeightTypeDef = TypedDict(
    "TruckWeightTypeDef",
    {
        "Total": float,
        "Unit": VehicleWeightUnitType,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
    },
)
_OptionalUpdateGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateGeofenceCollectionRequestRequestTypeDef",
    {
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "Description": str,
    },
    total=False,
)

class UpdateGeofenceCollectionRequestRequestTypeDef(
    _RequiredUpdateGeofenceCollectionRequestRequestTypeDef,
    _OptionalUpdateGeofenceCollectionRequestRequestTypeDef,
):
    pass

UpdateGeofenceCollectionResponseTypeDef = TypedDict(
    "UpdateGeofenceCollectionResponseTypeDef",
    {
        "CollectionName": str,
        "CollectionArn": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateKeyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateKeyRequestRequestTypeDef",
    {
        "KeyName": str,
    },
)
_OptionalUpdateKeyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateKeyRequestRequestTypeDef",
    {
        "Description": str,
        "ExpireTime": Union[datetime, str],
        "NoExpiry": bool,
        "ForceUpdate": bool,
        "Restrictions": "ApiKeyRestrictionsTypeDef",
    },
    total=False,
)

class UpdateKeyRequestRequestTypeDef(
    _RequiredUpdateKeyRequestRequestTypeDef, _OptionalUpdateKeyRequestRequestTypeDef
):
    pass

UpdateKeyResponseTypeDef = TypedDict(
    "UpdateKeyResponseTypeDef",
    {
        "KeyArn": str,
        "KeyName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMapRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMapRequestRequestTypeDef",
    {
        "MapName": str,
    },
)
_OptionalUpdateMapRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMapRequestRequestTypeDef",
    {
        "PricingPlan": PricingPlanType,
        "Description": str,
        "ConfigurationUpdate": "MapConfigurationUpdateTypeDef",
    },
    total=False,
)

class UpdateMapRequestRequestTypeDef(
    _RequiredUpdateMapRequestRequestTypeDef, _OptionalUpdateMapRequestRequestTypeDef
):
    pass

UpdateMapResponseTypeDef = TypedDict(
    "UpdateMapResponseTypeDef",
    {
        "MapName": str,
        "MapArn": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePlaceIndexRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePlaceIndexRequestRequestTypeDef",
    {
        "IndexName": str,
    },
)
_OptionalUpdatePlaceIndexRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePlaceIndexRequestRequestTypeDef",
    {
        "PricingPlan": PricingPlanType,
        "Description": str,
        "DataSourceConfiguration": "DataSourceConfigurationTypeDef",
    },
    total=False,
)

class UpdatePlaceIndexRequestRequestTypeDef(
    _RequiredUpdatePlaceIndexRequestRequestTypeDef, _OptionalUpdatePlaceIndexRequestRequestTypeDef
):
    pass

UpdatePlaceIndexResponseTypeDef = TypedDict(
    "UpdatePlaceIndexResponseTypeDef",
    {
        "IndexName": str,
        "IndexArn": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRouteCalculatorRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
    },
)
_OptionalUpdateRouteCalculatorRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRouteCalculatorRequestRequestTypeDef",
    {
        "PricingPlan": PricingPlanType,
        "Description": str,
    },
    total=False,
)

class UpdateRouteCalculatorRequestRequestTypeDef(
    _RequiredUpdateRouteCalculatorRequestRequestTypeDef,
    _OptionalUpdateRouteCalculatorRequestRequestTypeDef,
):
    pass

UpdateRouteCalculatorResponseTypeDef = TypedDict(
    "UpdateRouteCalculatorResponseTypeDef",
    {
        "CalculatorName": str,
        "CalculatorArn": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTrackerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
    },
)
_OptionalUpdateTrackerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTrackerRequestRequestTypeDef",
    {
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "Description": str,
        "PositionFiltering": PositionFilteringType,
        "EventBridgeEnabled": bool,
        "KmsKeyEnableGeospatialQueries": bool,
    },
    total=False,
)

class UpdateTrackerRequestRequestTypeDef(
    _RequiredUpdateTrackerRequestRequestTypeDef, _OptionalUpdateTrackerRequestRequestTypeDef
):
    pass

UpdateTrackerResponseTypeDef = TypedDict(
    "UpdateTrackerResponseTypeDef",
    {
        "TrackerName": str,
        "TrackerArn": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredVerifyDevicePositionRequestRequestTypeDef = TypedDict(
    "_RequiredVerifyDevicePositionRequestRequestTypeDef",
    {
        "TrackerName": str,
        "DeviceState": "DeviceStateTypeDef",
    },
)
_OptionalVerifyDevicePositionRequestRequestTypeDef = TypedDict(
    "_OptionalVerifyDevicePositionRequestRequestTypeDef",
    {
        "DistanceUnit": DistanceUnitType,
    },
    total=False,
)

class VerifyDevicePositionRequestRequestTypeDef(
    _RequiredVerifyDevicePositionRequestRequestTypeDef,
    _OptionalVerifyDevicePositionRequestRequestTypeDef,
):
    pass

VerifyDevicePositionResponseTypeDef = TypedDict(
    "VerifyDevicePositionResponseTypeDef",
    {
        "InferredState": "InferredStateTypeDef",
        "DeviceId": str,
        "SampleTime": datetime,
        "ReceivedTime": datetime,
        "DistanceUnit": DistanceUnitType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WiFiAccessPointTypeDef = TypedDict(
    "WiFiAccessPointTypeDef",
    {
        "MacAddress": str,
        "Rss": int,
    },
)
