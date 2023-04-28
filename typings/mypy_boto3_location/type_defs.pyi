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
from typing import Any, Dict, List, Union

from .literals import (
    BatchItemErrorCodeType,
    DimensionUnitType,
    DistanceUnitType,
    IntendedUseType,
    PositionFilteringType,
    PricingPlanType,
    RouteMatrixErrorCodeType,
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
    "DisassociateTrackerConsumerRequestRequestTypeDef",
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
    "MapConfigurationTypeDef",
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
        "ConsumerArn": str,
        "TrackerName": str,
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
        "DeviceIds": List[str],
        "TrackerName": str,
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
        "Error": "BatchItemErrorTypeDef",
        "GeofenceId": str,
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
        "Error": "BatchItemErrorTypeDef",
        "SampleTime": datetime,
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
        "DeviceIds": List[str],
        "TrackerName": str,
    },
)

BatchGetDevicePositionResponseTypeDef = TypedDict(
    "BatchGetDevicePositionResponseTypeDef",
    {
        "DevicePositions": List["DevicePositionTypeDef"],
        "Errors": List["BatchGetDevicePositionErrorTypeDef"],
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
        "Error": "BatchItemErrorTypeDef",
        "GeofenceId": str,
    },
)

BatchPutGeofenceRequestEntryTypeDef = TypedDict(
    "BatchPutGeofenceRequestEntryTypeDef",
    {
        "GeofenceId": str,
        "Geometry": "GeofenceGeometryTypeDef",
    },
)

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
        "Errors": List["BatchPutGeofenceErrorTypeDef"],
        "Successes": List["BatchPutGeofenceSuccessTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPutGeofenceSuccessTypeDef = TypedDict(
    "BatchPutGeofenceSuccessTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "UpdateTime": datetime,
    },
)

BatchUpdateDevicePositionErrorTypeDef = TypedDict(
    "BatchUpdateDevicePositionErrorTypeDef",
    {
        "DeviceId": str,
        "Error": "BatchItemErrorTypeDef",
        "SampleTime": datetime,
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
        "CarModeOptions": "CalculateRouteCarModeOptionsTypeDef",
        "DepartNow": bool,
        "DepartureTime": Union[datetime, str],
        "DistanceUnit": DistanceUnitType,
        "TravelMode": TravelModeType,
        "TruckModeOptions": "CalculateRouteTruckModeOptionsTypeDef",
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
        "DistanceUnit": DistanceUnitType,
        "ErrorCount": int,
        "RouteCount": int,
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
        "CarModeOptions": "CalculateRouteCarModeOptionsTypeDef",
        "DepartNow": bool,
        "DepartureTime": Union[datetime, str],
        "DistanceUnit": DistanceUnitType,
        "IncludeLegGeometry": bool,
        "TravelMode": TravelModeType,
        "TruckModeOptions": "CalculateRouteTruckModeOptionsTypeDef",
        "WaypointPositions": List[List[float]],
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
        "DataSource": str,
        "Distance": float,
        "DistanceUnit": DistanceUnitType,
        "DurationSeconds": float,
        "RouteBBox": List[float],
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
        "Description": str,
        "KmsKeyId": str,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "Tags": Dict[str, str],
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
        "CollectionArn": str,
        "CollectionName": str,
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
        "CreateTime": datetime,
        "Key": str,
        "KeyArn": str,
        "KeyName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMapRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMapRequestRequestTypeDef",
    {
        "Configuration": "MapConfigurationTypeDef",
        "MapName": str,
    },
)
_OptionalCreateMapRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMapRequestRequestTypeDef",
    {
        "Description": str,
        "PricingPlan": PricingPlanType,
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
        "CreateTime": datetime,
        "MapArn": str,
        "MapName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePlaceIndexRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePlaceIndexRequestRequestTypeDef",
    {
        "DataSource": str,
        "IndexName": str,
    },
)
_OptionalCreatePlaceIndexRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePlaceIndexRequestRequestTypeDef",
    {
        "DataSourceConfiguration": "DataSourceConfigurationTypeDef",
        "Description": str,
        "PricingPlan": PricingPlanType,
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
        "CreateTime": datetime,
        "IndexArn": str,
        "IndexName": str,
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
        "Description": str,
        "PricingPlan": PricingPlanType,
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
        "CalculatorArn": str,
        "CalculatorName": str,
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
        "Description": str,
        "KmsKeyId": str,
        "PositionFiltering": PositionFilteringType,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "Tags": Dict[str, str],
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
        "CreateTime": datetime,
        "TrackerArn": str,
        "TrackerName": str,
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

DeleteKeyRequestRequestTypeDef = TypedDict(
    "DeleteKeyRequestRequestTypeDef",
    {
        "KeyName": str,
    },
)

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
        "CollectionArn": str,
        "CollectionName": str,
        "CreateTime": datetime,
        "Description": str,
        "KmsKeyId": str,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
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
        "CreateTime": datetime,
        "Description": str,
        "ExpireTime": datetime,
        "Key": str,
        "KeyArn": str,
        "KeyName": str,
        "Restrictions": "ApiKeyRestrictionsTypeDef",
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
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
        "Configuration": "MapConfigurationTypeDef",
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "MapArn": str,
        "MapName": str,
        "PricingPlan": PricingPlanType,
        "Tags": Dict[str, str],
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
        "CreateTime": datetime,
        "DataSource": str,
        "DataSourceConfiguration": "DataSourceConfigurationTypeDef",
        "Description": str,
        "IndexArn": str,
        "IndexName": str,
        "PricingPlan": PricingPlanType,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
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
        "CalculatorArn": str,
        "CalculatorName": str,
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "PricingPlan": PricingPlanType,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
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
        "CreateTime": datetime,
        "Description": str,
        "KmsKeyId": str,
        "PositionFiltering": PositionFilteringType,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "Tags": Dict[str, str],
        "TrackerArn": str,
        "TrackerName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDevicePositionTypeDef = TypedDict(
    "_RequiredDevicePositionTypeDef",
    {
        "Position": List[float],
        "ReceivedTime": datetime,
        "SampleTime": datetime,
    },
)
_OptionalDevicePositionTypeDef = TypedDict(
    "_OptionalDevicePositionTypeDef",
    {
        "Accuracy": "PositionalAccuracyTypeDef",
        "DeviceId": str,
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
        "Position": List[float],
        "SampleTime": Union[datetime, str],
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

DisassociateTrackerConsumerRequestRequestTypeDef = TypedDict(
    "DisassociateTrackerConsumerRequestRequestTypeDef",
    {
        "ConsumerArn": str,
        "TrackerName": str,
    },
)

GeofenceGeometryTypeDef = TypedDict(
    "GeofenceGeometryTypeDef",
    {
        "Circle": "CircleTypeDef",
        "Polygon": List[List[List[float]]],
    },
    total=False,
)

_RequiredGetDevicePositionHistoryRequestRequestTypeDef = TypedDict(
    "_RequiredGetDevicePositionHistoryRequestRequestTypeDef",
    {
        "DeviceId": str,
        "TrackerName": str,
    },
)
_OptionalGetDevicePositionHistoryRequestRequestTypeDef = TypedDict(
    "_OptionalGetDevicePositionHistoryRequestRequestTypeDef",
    {
        "EndTimeExclusive": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
        "StartTimeInclusive": Union[datetime, str],
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
        "DeviceId": str,
        "TrackerName": str,
    },
)

GetDevicePositionResponseTypeDef = TypedDict(
    "GetDevicePositionResponseTypeDef",
    {
        "Accuracy": "PositionalAccuracyTypeDef",
        "DeviceId": str,
        "Position": List[float],
        "PositionProperties": Dict[str, str],
        "ReceivedTime": datetime,
        "SampleTime": datetime,
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
        "CreateTime": datetime,
        "GeofenceId": str,
        "Geometry": "GeofenceGeometryTypeDef",
        "Status": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMapGlyphsRequestRequestTypeDef = TypedDict(
    "_RequiredGetMapGlyphsRequestRequestTypeDef",
    {
        "FontStack": str,
        "FontUnicodeRange": str,
        "MapName": str,
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
        "CacheControl": str,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMapSpritesRequestRequestTypeDef = TypedDict(
    "_RequiredGetMapSpritesRequestRequestTypeDef",
    {
        "FileName": str,
        "MapName": str,
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
        "CacheControl": str,
        "ContentType": str,
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
        "CacheControl": str,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMapTileRequestRequestTypeDef = TypedDict(
    "_RequiredGetMapTileRequestRequestTypeDef",
    {
        "MapName": str,
        "X": str,
        "Y": str,
        "Z": str,
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
        "CacheControl": str,
        "ContentType": str,
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
        "Distance": float,
        "DurationSeconds": float,
        "EndPosition": List[float],
        "StartPosition": List[float],
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
        "Position": List[float],
        "SampleTime": datetime,
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
        "CreateTime": datetime,
        "Description": str,
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

ListGeofenceResponseEntryTypeDef = TypedDict(
    "ListGeofenceResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "Geometry": "GeofenceGeometryTypeDef",
        "Status": str,
        "UpdateTime": datetime,
    },
)

_RequiredListGeofencesRequestRequestTypeDef = TypedDict(
    "_RequiredListGeofencesRequestRequestTypeDef",
    {
        "CollectionName": str,
    },
)
_OptionalListGeofencesRequestRequestTypeDef = TypedDict(
    "_OptionalListGeofencesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
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
        "Filter": "ApiKeyFilterTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListKeysResponseEntryTypeDef = TypedDict(
    "_RequiredListKeysResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "ExpireTime": datetime,
        "KeyName": str,
        "Restrictions": "ApiKeyRestrictionsTypeDef",
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
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "MapName": str,
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
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "IndexName": str,
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
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
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
        "CreateTime": datetime,
        "Description": str,
        "TrackerName": str,
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

MapConfigurationTypeDef = TypedDict(
    "MapConfigurationTypeDef",
    {
        "Style": str,
    },
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
        "AddressNumber": str,
        "Country": str,
        "Interpolated": bool,
        "Label": str,
        "Municipality": str,
        "Neighborhood": str,
        "PostalCode": str,
        "Region": str,
        "Street": str,
        "SubRegion": str,
        "TimeZone": "TimeZoneTypeDef",
        "UnitNumber": str,
        "UnitType": str,
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

PutGeofenceRequestRequestTypeDef = TypedDict(
    "PutGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "GeofenceId": str,
        "Geometry": "GeofenceGeometryTypeDef",
    },
)

PutGeofenceResponseTypeDef = TypedDict(
    "PutGeofenceResponseTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
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
        "Distance": float,
        "Place": "PlaceTypeDef",
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
        "PlaceId": str,
        "Relevance": float,
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
        "Language": str,
        "MaxResults": int,
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
        "Results": List["SearchForPositionResultTypeDef"],
        "Summary": "SearchPlaceIndexForPositionSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchPlaceIndexForPositionSummaryTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForPositionSummaryTypeDef",
    {
        "DataSource": str,
        "Position": List[float],
    },
)
_OptionalSearchPlaceIndexForPositionSummaryTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForPositionSummaryTypeDef",
    {
        "Language": str,
        "MaxResults": int,
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
        "Language": str,
        "MaxResults": int,
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
        "Results": List["SearchForSuggestionsResultTypeDef"],
        "Summary": "SearchPlaceIndexForSuggestionsSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchPlaceIndexForSuggestionsSummaryTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForSuggestionsSummaryTypeDef",
    {
        "DataSource": str,
        "Text": str,
    },
)
_OptionalSearchPlaceIndexForSuggestionsSummaryTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForSuggestionsSummaryTypeDef",
    {
        "BiasPosition": List[float],
        "FilterBBox": List[float],
        "FilterCountries": List[str],
        "Language": str,
        "MaxResults": int,
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
        "Language": str,
        "MaxResults": int,
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
        "Results": List["SearchForTextResultTypeDef"],
        "Summary": "SearchPlaceIndexForTextSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchPlaceIndexForTextSummaryTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForTextSummaryTypeDef",
    {
        "DataSource": str,
        "Text": str,
    },
)
_OptionalSearchPlaceIndexForTextSummaryTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForTextSummaryTypeDef",
    {
        "BiasPosition": List[float],
        "FilterBBox": List[float],
        "FilterCountries": List[str],
        "Language": str,
        "MaxResults": int,
        "ResultBBox": List[float],
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
        "Distance": float,
        "DurationSeconds": float,
        "EndPosition": List[float],
        "StartPosition": List[float],
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

TruckDimensionsTypeDef = TypedDict(
    "TruckDimensionsTypeDef",
    {
        "Height": float,
        "Length": float,
        "Unit": DimensionUnitType,
        "Width": float,
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
        "Description": str,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
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
        "CollectionArn": str,
        "CollectionName": str,
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
        "ForceUpdate": bool,
        "NoExpiry": bool,
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
        "Description": str,
        "PricingPlan": PricingPlanType,
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
        "MapArn": str,
        "MapName": str,
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
        "DataSourceConfiguration": "DataSourceConfigurationTypeDef",
        "Description": str,
        "PricingPlan": PricingPlanType,
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
        "IndexArn": str,
        "IndexName": str,
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
        "Description": str,
        "PricingPlan": PricingPlanType,
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
        "CalculatorArn": str,
        "CalculatorName": str,
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
        "Description": str,
        "PositionFiltering": PositionFilteringType,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
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
        "TrackerArn": str,
        "TrackerName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
