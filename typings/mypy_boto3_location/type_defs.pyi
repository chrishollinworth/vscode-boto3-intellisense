"""
Type annotations for location service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/type_defs.html)

Usage::

    ```python
    from mypy_boto3_location.type_defs import AssociateTrackerConsumerRequestRequestTypeDef

    data: AssociateTrackerConsumerRequestRequestTypeDef = {...}
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
    PricingPlanType,
    TravelModeType,
    VehicleWeightUnitType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
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
    "CalculateRouteRequestRequestTypeDef",
    "CalculateRouteResponseTypeDef",
    "CalculateRouteSummaryTypeDef",
    "CalculateRouteTruckModeOptionsTypeDef",
    "CreateGeofenceCollectionRequestRequestTypeDef",
    "CreateGeofenceCollectionResponseTypeDef",
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
    "DeleteMapRequestRequestTypeDef",
    "DeletePlaceIndexRequestRequestTypeDef",
    "DeleteRouteCalculatorRequestRequestTypeDef",
    "DeleteTrackerRequestRequestTypeDef",
    "DescribeGeofenceCollectionRequestRequestTypeDef",
    "DescribeGeofenceCollectionResponseTypeDef",
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
    "PutGeofenceRequestRequestTypeDef",
    "PutGeofenceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SearchForPositionResultTypeDef",
    "SearchForTextResultTypeDef",
    "SearchPlaceIndexForPositionRequestRequestTypeDef",
    "SearchPlaceIndexForPositionResponseTypeDef",
    "SearchPlaceIndexForPositionSummaryTypeDef",
    "SearchPlaceIndexForTextRequestRequestTypeDef",
    "SearchPlaceIndexForTextResponseTypeDef",
    "SearchPlaceIndexForTextSummaryTypeDef",
    "StepTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TruckDimensionsTypeDef",
    "TruckWeightTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateGeofenceCollectionRequestRequestTypeDef",
    "UpdateGeofenceCollectionResponseTypeDef",
    "UpdateMapRequestRequestTypeDef",
    "UpdateMapResponseTypeDef",
    "UpdatePlaceIndexRequestRequestTypeDef",
    "UpdatePlaceIndexResponseTypeDef",
    "UpdateRouteCalculatorRequestRequestTypeDef",
    "UpdateRouteCalculatorResponseTypeDef",
    "UpdateTrackerRequestRequestTypeDef",
    "UpdateTrackerResponseTypeDef",
)

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

_RequiredCreateGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
        "PricingPlan": PricingPlanType,
    },
)
_OptionalCreateGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGeofenceCollectionRequestRequestTypeDef",
    {
        "Description": str,
        "KmsKeyId": str,
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

_RequiredCreateMapRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMapRequestRequestTypeDef",
    {
        "Configuration": "MapConfigurationTypeDef",
        "MapName": str,
        "PricingPlan": PricingPlanType,
    },
)
_OptionalCreateMapRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMapRequestRequestTypeDef",
    {
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
        "PricingPlan": PricingPlanType,
    },
)
_OptionalCreatePlaceIndexRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePlaceIndexRequestRequestTypeDef",
    {
        "DataSourceConfiguration": "DataSourceConfigurationTypeDef",
        "Description": str,
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
        "PricingPlan": PricingPlanType,
    },
)
_OptionalCreateRouteCalculatorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRouteCalculatorRequestRequestTypeDef",
    {
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
        "CalculatorArn": str,
        "CalculatorName": str,
        "CreateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrackerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrackerRequestRequestTypeDef",
    {
        "PricingPlan": PricingPlanType,
        "TrackerName": str,
    },
)
_OptionalCreateTrackerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrackerRequestRequestTypeDef",
    {
        "Description": str,
        "KmsKeyId": str,
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
        "DeviceId": str,
    },
    total=False,
)

class DevicePositionTypeDef(_RequiredDevicePositionTypeDef, _OptionalDevicePositionTypeDef):
    pass

DevicePositionUpdateTypeDef = TypedDict(
    "DevicePositionUpdateTypeDef",
    {
        "DeviceId": str,
        "Position": List[float],
        "SampleTime": Union[datetime, str],
    },
)

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
        "DeviceId": str,
        "Position": List[float],
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

GetMapGlyphsRequestRequestTypeDef = TypedDict(
    "GetMapGlyphsRequestRequestTypeDef",
    {
        "FontStack": str,
        "FontUnicodeRange": str,
        "MapName": str,
    },
)

GetMapGlyphsResponseTypeDef = TypedDict(
    "GetMapGlyphsResponseTypeDef",
    {
        "Blob": bytes,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMapSpritesRequestRequestTypeDef = TypedDict(
    "GetMapSpritesRequestRequestTypeDef",
    {
        "FileName": str,
        "MapName": str,
    },
)

GetMapSpritesResponseTypeDef = TypedDict(
    "GetMapSpritesResponseTypeDef",
    {
        "Blob": bytes,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMapStyleDescriptorRequestRequestTypeDef = TypedDict(
    "GetMapStyleDescriptorRequestRequestTypeDef",
    {
        "MapName": str,
    },
)

GetMapStyleDescriptorResponseTypeDef = TypedDict(
    "GetMapStyleDescriptorResponseTypeDef",
    {
        "Blob": bytes,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMapTileRequestRequestTypeDef = TypedDict(
    "GetMapTileRequestRequestTypeDef",
    {
        "MapName": str,
        "X": str,
        "Y": str,
        "Z": str,
    },
)

GetMapTileResponseTypeDef = TypedDict(
    "GetMapTileResponseTypeDef",
    {
        "Blob": bytes,
        "ContentType": str,
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

ListDevicePositionsResponseEntryTypeDef = TypedDict(
    "ListDevicePositionsResponseEntryTypeDef",
    {
        "DeviceId": str,
        "Position": List[float],
        "SampleTime": datetime,
    },
)

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
        "PricingPlan": PricingPlanType,
        "UpdateTime": datetime,
    },
)
_OptionalListGeofenceCollectionsResponseEntryTypeDef = TypedDict(
    "_OptionalListGeofenceCollectionsResponseEntryTypeDef",
    {
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

ListMapsRequestRequestTypeDef = TypedDict(
    "ListMapsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListMapsResponseEntryTypeDef = TypedDict(
    "ListMapsResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "MapName": str,
        "PricingPlan": PricingPlanType,
        "UpdateTime": datetime,
    },
)

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

ListPlaceIndexesResponseEntryTypeDef = TypedDict(
    "ListPlaceIndexesResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "IndexName": str,
        "PricingPlan": PricingPlanType,
        "UpdateTime": datetime,
    },
)

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

ListRouteCalculatorsResponseEntryTypeDef = TypedDict(
    "ListRouteCalculatorsResponseEntryTypeDef",
    {
        "CalculatorName": str,
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "PricingPlan": PricingPlanType,
        "UpdateTime": datetime,
    },
)

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
        "PricingPlan": PricingPlanType,
        "TrackerName": str,
        "UpdateTime": datetime,
    },
)
_OptionalListTrackersResponseEntryTypeDef = TypedDict(
    "_OptionalListTrackersResponseEntryTypeDef",
    {
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
        "Label": str,
        "Municipality": str,
        "Neighborhood": str,
        "PostalCode": str,
        "Region": str,
        "Street": str,
        "SubRegion": str,
    },
    total=False,
)

class PlaceTypeDef(_RequiredPlaceTypeDef, _OptionalPlaceTypeDef):
    pass

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

SearchForPositionResultTypeDef = TypedDict(
    "SearchForPositionResultTypeDef",
    {
        "Place": "PlaceTypeDef",
    },
)

SearchForTextResultTypeDef = TypedDict(
    "SearchForTextResultTypeDef",
    {
        "Place": "PlaceTypeDef",
    },
)

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
        "MaxResults": int,
    },
    total=False,
)

class SearchPlaceIndexForPositionSummaryTypeDef(
    _RequiredSearchPlaceIndexForPositionSummaryTypeDef,
    _OptionalSearchPlaceIndexForPositionSummaryTypeDef,
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
