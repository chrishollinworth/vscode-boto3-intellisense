"""
Main interface for location service type definitions.

Usage::

    ```python
    from mypy_boto3_location.type_defs import BatchDeleteGeofenceErrorTypeDef

    data: BatchDeleteGeofenceErrorTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchDeleteGeofenceErrorTypeDef",
    "BatchEvaluateGeofencesErrorTypeDef",
    "BatchGetDevicePositionErrorTypeDef",
    "BatchItemErrorTypeDef",
    "BatchPutGeofenceErrorTypeDef",
    "BatchPutGeofenceSuccessTypeDef",
    "BatchUpdateDevicePositionErrorTypeDef",
    "DataSourceConfigurationTypeDef",
    "DevicePositionTypeDef",
    "GeofenceGeometryTypeDef",
    "ListGeofenceCollectionsResponseEntryTypeDef",
    "ListGeofenceResponseEntryTypeDef",
    "ListMapsResponseEntryTypeDef",
    "ListPlaceIndexesResponseEntryTypeDef",
    "ListTrackersResponseEntryTypeDef",
    "MapConfigurationTypeDef",
    "PlaceGeometryTypeDef",
    "PlaceTypeDef",
    "SearchForPositionResultTypeDef",
    "SearchForTextResultTypeDef",
    "SearchPlaceIndexForPositionSummaryTypeDef",
    "SearchPlaceIndexForTextSummaryTypeDef",
    "BatchDeleteGeofenceResponseTypeDef",
    "BatchEvaluateGeofencesResponseTypeDef",
    "BatchGetDevicePositionResponseTypeDef",
    "BatchPutGeofenceRequestEntryTypeDef",
    "BatchPutGeofenceResponseTypeDef",
    "BatchUpdateDevicePositionResponseTypeDef",
    "CreateGeofenceCollectionResponseTypeDef",
    "CreateMapResponseTypeDef",
    "CreatePlaceIndexResponseTypeDef",
    "CreateTrackerResponseTypeDef",
    "DescribeGeofenceCollectionResponseTypeDef",
    "DescribeMapResponseTypeDef",
    "DescribePlaceIndexResponseTypeDef",
    "DescribeTrackerResponseTypeDef",
    "DevicePositionUpdateTypeDef",
    "GetDevicePositionHistoryResponseTypeDef",
    "GetDevicePositionResponseTypeDef",
    "GetGeofenceResponseTypeDef",
    "GetMapGlyphsResponseTypeDef",
    "GetMapSpritesResponseTypeDef",
    "GetMapStyleDescriptorResponseTypeDef",
    "GetMapTileResponseTypeDef",
    "ListGeofenceCollectionsResponseTypeDef",
    "ListGeofencesResponseTypeDef",
    "ListMapsResponseTypeDef",
    "ListPlaceIndexesResponseTypeDef",
    "ListTrackerConsumersResponseTypeDef",
    "ListTrackersResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutGeofenceResponseTypeDef",
    "SearchPlaceIndexForPositionResponseTypeDef",
    "SearchPlaceIndexForTextResponseTypeDef",
)

BatchDeleteGeofenceErrorTypeDef = TypedDict(
    "BatchDeleteGeofenceErrorTypeDef", {"Error": "BatchItemErrorTypeDef", "GeofenceId": str}
)

BatchEvaluateGeofencesErrorTypeDef = TypedDict(
    "BatchEvaluateGeofencesErrorTypeDef",
    {"DeviceId": str, "Error": "BatchItemErrorTypeDef", "SampleTime": datetime},
)

BatchGetDevicePositionErrorTypeDef = TypedDict(
    "BatchGetDevicePositionErrorTypeDef", {"DeviceId": str, "Error": "BatchItemErrorTypeDef"}
)

BatchItemErrorTypeDef = TypedDict(
    "BatchItemErrorTypeDef",
    {
        "Code": Literal[
            "AccessDeniedError",
            "ConflictError",
            "InternalServerError",
            "ResourceNotFoundError",
            "ThrottlingError",
            "ValidationError",
        ],
        "Message": str,
    },
    total=False,
)

BatchPutGeofenceErrorTypeDef = TypedDict(
    "BatchPutGeofenceErrorTypeDef", {"Error": "BatchItemErrorTypeDef", "GeofenceId": str}
)

BatchPutGeofenceSuccessTypeDef = TypedDict(
    "BatchPutGeofenceSuccessTypeDef",
    {"CreateTime": datetime, "GeofenceId": str, "UpdateTime": datetime},
)

BatchUpdateDevicePositionErrorTypeDef = TypedDict(
    "BatchUpdateDevicePositionErrorTypeDef",
    {"DeviceId": str, "Error": "BatchItemErrorTypeDef", "SampleTime": datetime},
)

DataSourceConfigurationTypeDef = TypedDict(
    "DataSourceConfigurationTypeDef", {"IntendedUse": Literal["SingleUse", "Storage"]}, total=False
)

_RequiredDevicePositionTypeDef = TypedDict(
    "_RequiredDevicePositionTypeDef",
    {"Position": List[float], "ReceivedTime": datetime, "SampleTime": datetime},
)
_OptionalDevicePositionTypeDef = TypedDict(
    "_OptionalDevicePositionTypeDef", {"DeviceId": str}, total=False
)


class DevicePositionTypeDef(_RequiredDevicePositionTypeDef, _OptionalDevicePositionTypeDef):
    pass


GeofenceGeometryTypeDef = TypedDict(
    "GeofenceGeometryTypeDef", {"Polygon": List[List[List[float]]]}, total=False
)

ListGeofenceCollectionsResponseEntryTypeDef = TypedDict(
    "ListGeofenceCollectionsResponseEntryTypeDef",
    {"CollectionName": str, "CreateTime": datetime, "Description": str, "UpdateTime": datetime},
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

ListMapsResponseEntryTypeDef = TypedDict(
    "ListMapsResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "MapName": str,
        "UpdateTime": datetime,
    },
)

ListPlaceIndexesResponseEntryTypeDef = TypedDict(
    "ListPlaceIndexesResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "IndexName": str,
        "UpdateTime": datetime,
    },
)

ListTrackersResponseEntryTypeDef = TypedDict(
    "ListTrackersResponseEntryTypeDef",
    {"CreateTime": datetime, "Description": str, "TrackerName": str, "UpdateTime": datetime},
)

MapConfigurationTypeDef = TypedDict("MapConfigurationTypeDef", {"Style": str})

PlaceGeometryTypeDef = TypedDict("PlaceGeometryTypeDef", {"Point": List[float]}, total=False)

_RequiredPlaceTypeDef = TypedDict("_RequiredPlaceTypeDef", {"Geometry": "PlaceGeometryTypeDef"})
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


SearchForPositionResultTypeDef = TypedDict(
    "SearchForPositionResultTypeDef", {"Place": "PlaceTypeDef"}
)

SearchForTextResultTypeDef = TypedDict("SearchForTextResultTypeDef", {"Place": "PlaceTypeDef"})

_RequiredSearchPlaceIndexForPositionSummaryTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForPositionSummaryTypeDef",
    {"DataSource": str, "Position": List[float]},
)
_OptionalSearchPlaceIndexForPositionSummaryTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForPositionSummaryTypeDef", {"MaxResults": int}, total=False
)


class SearchPlaceIndexForPositionSummaryTypeDef(
    _RequiredSearchPlaceIndexForPositionSummaryTypeDef,
    _OptionalSearchPlaceIndexForPositionSummaryTypeDef,
):
    pass


_RequiredSearchPlaceIndexForTextSummaryTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForTextSummaryTypeDef", {"DataSource": str, "Text": str}
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


BatchDeleteGeofenceResponseTypeDef = TypedDict(
    "BatchDeleteGeofenceResponseTypeDef", {"Errors": List["BatchDeleteGeofenceErrorTypeDef"]}
)

BatchEvaluateGeofencesResponseTypeDef = TypedDict(
    "BatchEvaluateGeofencesResponseTypeDef", {"Errors": List["BatchEvaluateGeofencesErrorTypeDef"]}
)

BatchGetDevicePositionResponseTypeDef = TypedDict(
    "BatchGetDevicePositionResponseTypeDef",
    {
        "DevicePositions": List["DevicePositionTypeDef"],
        "Errors": List["BatchGetDevicePositionErrorTypeDef"],
    },
)

BatchPutGeofenceRequestEntryTypeDef = TypedDict(
    "BatchPutGeofenceRequestEntryTypeDef",
    {"GeofenceId": str, "Geometry": "GeofenceGeometryTypeDef"},
)

BatchPutGeofenceResponseTypeDef = TypedDict(
    "BatchPutGeofenceResponseTypeDef",
    {
        "Errors": List["BatchPutGeofenceErrorTypeDef"],
        "Successes": List["BatchPutGeofenceSuccessTypeDef"],
    },
)

BatchUpdateDevicePositionResponseTypeDef = TypedDict(
    "BatchUpdateDevicePositionResponseTypeDef",
    {"Errors": List["BatchUpdateDevicePositionErrorTypeDef"]},
)

CreateGeofenceCollectionResponseTypeDef = TypedDict(
    "CreateGeofenceCollectionResponseTypeDef",
    {"CollectionArn": str, "CollectionName": str, "CreateTime": datetime},
)

CreateMapResponseTypeDef = TypedDict(
    "CreateMapResponseTypeDef", {"CreateTime": datetime, "MapArn": str, "MapName": str}
)

CreatePlaceIndexResponseTypeDef = TypedDict(
    "CreatePlaceIndexResponseTypeDef", {"CreateTime": datetime, "IndexArn": str, "IndexName": str}
)

CreateTrackerResponseTypeDef = TypedDict(
    "CreateTrackerResponseTypeDef", {"CreateTime": datetime, "TrackerArn": str, "TrackerName": str}
)

DescribeGeofenceCollectionResponseTypeDef = TypedDict(
    "DescribeGeofenceCollectionResponseTypeDef",
    {
        "CollectionArn": str,
        "CollectionName": str,
        "CreateTime": datetime,
        "Description": str,
        "UpdateTime": datetime,
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
        "UpdateTime": datetime,
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
        "UpdateTime": datetime,
    },
)

DescribeTrackerResponseTypeDef = TypedDict(
    "DescribeTrackerResponseTypeDef",
    {
        "CreateTime": datetime,
        "Description": str,
        "TrackerArn": str,
        "TrackerName": str,
        "UpdateTime": datetime,
    },
)

DevicePositionUpdateTypeDef = TypedDict(
    "DevicePositionUpdateTypeDef",
    {"DeviceId": str, "Position": List[float], "SampleTime": datetime},
)

_RequiredGetDevicePositionHistoryResponseTypeDef = TypedDict(
    "_RequiredGetDevicePositionHistoryResponseTypeDef",
    {"DevicePositions": List["DevicePositionTypeDef"]},
)
_OptionalGetDevicePositionHistoryResponseTypeDef = TypedDict(
    "_OptionalGetDevicePositionHistoryResponseTypeDef", {"NextToken": str}, total=False
)


class GetDevicePositionHistoryResponseTypeDef(
    _RequiredGetDevicePositionHistoryResponseTypeDef,
    _OptionalGetDevicePositionHistoryResponseTypeDef,
):
    pass


_RequiredGetDevicePositionResponseTypeDef = TypedDict(
    "_RequiredGetDevicePositionResponseTypeDef",
    {"Position": List[float], "ReceivedTime": datetime, "SampleTime": datetime},
)
_OptionalGetDevicePositionResponseTypeDef = TypedDict(
    "_OptionalGetDevicePositionResponseTypeDef", {"DeviceId": str}, total=False
)


class GetDevicePositionResponseTypeDef(
    _RequiredGetDevicePositionResponseTypeDef, _OptionalGetDevicePositionResponseTypeDef
):
    pass


GetGeofenceResponseTypeDef = TypedDict(
    "GetGeofenceResponseTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "Geometry": "GeofenceGeometryTypeDef",
        "Status": str,
        "UpdateTime": datetime,
    },
)

GetMapGlyphsResponseTypeDef = TypedDict(
    "GetMapGlyphsResponseTypeDef",
    {"Blob": Union[bytes, IO[bytes]], "ContentType": str},
    total=False,
)

GetMapSpritesResponseTypeDef = TypedDict(
    "GetMapSpritesResponseTypeDef",
    {"Blob": Union[bytes, IO[bytes]], "ContentType": str},
    total=False,
)

GetMapStyleDescriptorResponseTypeDef = TypedDict(
    "GetMapStyleDescriptorResponseTypeDef",
    {"Blob": Union[bytes, IO[bytes]], "ContentType": str},
    total=False,
)

GetMapTileResponseTypeDef = TypedDict(
    "GetMapTileResponseTypeDef", {"Blob": Union[bytes, IO[bytes]], "ContentType": str}, total=False
)

_RequiredListGeofenceCollectionsResponseTypeDef = TypedDict(
    "_RequiredListGeofenceCollectionsResponseTypeDef",
    {"Entries": List["ListGeofenceCollectionsResponseEntryTypeDef"]},
)
_OptionalListGeofenceCollectionsResponseTypeDef = TypedDict(
    "_OptionalListGeofenceCollectionsResponseTypeDef", {"NextToken": str}, total=False
)


class ListGeofenceCollectionsResponseTypeDef(
    _RequiredListGeofenceCollectionsResponseTypeDef, _OptionalListGeofenceCollectionsResponseTypeDef
):
    pass


_RequiredListGeofencesResponseTypeDef = TypedDict(
    "_RequiredListGeofencesResponseTypeDef", {"Entries": List["ListGeofenceResponseEntryTypeDef"]}
)
_OptionalListGeofencesResponseTypeDef = TypedDict(
    "_OptionalListGeofencesResponseTypeDef", {"NextToken": str}, total=False
)


class ListGeofencesResponseTypeDef(
    _RequiredListGeofencesResponseTypeDef, _OptionalListGeofencesResponseTypeDef
):
    pass


_RequiredListMapsResponseTypeDef = TypedDict(
    "_RequiredListMapsResponseTypeDef", {"Entries": List["ListMapsResponseEntryTypeDef"]}
)
_OptionalListMapsResponseTypeDef = TypedDict(
    "_OptionalListMapsResponseTypeDef", {"NextToken": str}, total=False
)


class ListMapsResponseTypeDef(_RequiredListMapsResponseTypeDef, _OptionalListMapsResponseTypeDef):
    pass


_RequiredListPlaceIndexesResponseTypeDef = TypedDict(
    "_RequiredListPlaceIndexesResponseTypeDef",
    {"Entries": List["ListPlaceIndexesResponseEntryTypeDef"]},
)
_OptionalListPlaceIndexesResponseTypeDef = TypedDict(
    "_OptionalListPlaceIndexesResponseTypeDef", {"NextToken": str}, total=False
)


class ListPlaceIndexesResponseTypeDef(
    _RequiredListPlaceIndexesResponseTypeDef, _OptionalListPlaceIndexesResponseTypeDef
):
    pass


_RequiredListTrackerConsumersResponseTypeDef = TypedDict(
    "_RequiredListTrackerConsumersResponseTypeDef", {"ConsumerArns": List[str]}
)
_OptionalListTrackerConsumersResponseTypeDef = TypedDict(
    "_OptionalListTrackerConsumersResponseTypeDef", {"NextToken": str}, total=False
)


class ListTrackerConsumersResponseTypeDef(
    _RequiredListTrackerConsumersResponseTypeDef, _OptionalListTrackerConsumersResponseTypeDef
):
    pass


_RequiredListTrackersResponseTypeDef = TypedDict(
    "_RequiredListTrackersResponseTypeDef", {"Entries": List["ListTrackersResponseEntryTypeDef"]}
)
_OptionalListTrackersResponseTypeDef = TypedDict(
    "_OptionalListTrackersResponseTypeDef", {"NextToken": str}, total=False
)


class ListTrackersResponseTypeDef(
    _RequiredListTrackersResponseTypeDef, _OptionalListTrackersResponseTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutGeofenceResponseTypeDef = TypedDict(
    "PutGeofenceResponseTypeDef",
    {"CreateTime": datetime, "GeofenceId": str, "UpdateTime": datetime},
)

SearchPlaceIndexForPositionResponseTypeDef = TypedDict(
    "SearchPlaceIndexForPositionResponseTypeDef",
    {
        "Results": List["SearchForPositionResultTypeDef"],
        "Summary": "SearchPlaceIndexForPositionSummaryTypeDef",
    },
)

SearchPlaceIndexForTextResponseTypeDef = TypedDict(
    "SearchPlaceIndexForTextResponseTypeDef",
    {
        "Results": List["SearchForTextResultTypeDef"],
        "Summary": "SearchPlaceIndexForTextSummaryTypeDef",
    },
)
