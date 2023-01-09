"""
Type annotations for sagemaker-geospatial service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_geospatial/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sagemaker_geospatial.type_defs import AreaOfInterestGeometryTypeDef

    data: AreaOfInterestGeometryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from botocore.response import StreamingBody

from .literals import (
    AlgorithmNameGeoMosaicType,
    AlgorithmNameResamplingType,
    ComparisonOperatorType,
    DataCollectionTypeType,
    EarthObservationJobErrorTypeType,
    EarthObservationJobExportStatusType,
    EarthObservationJobStatusType,
    ExportErrorTypeType,
    GroupByType,
    OutputTypeType,
    PredefinedResolutionType,
    SortOrderType,
    TargetOptionsType,
    TemporalStatisticsType,
    VectorEnrichmentJobErrorTypeType,
    VectorEnrichmentJobExportErrorTypeType,
    VectorEnrichmentJobExportStatusType,
    VectorEnrichmentJobStatusType,
    VectorEnrichmentJobTypeType,
    ZonalStatisticsType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AreaOfInterestGeometryTypeDef",
    "AreaOfInterestTypeDef",
    "AssetValueTypeDef",
    "BandMathConfigInputTypeDef",
    "CloudRemovalConfigInputTypeDef",
    "CustomIndicesInputTypeDef",
    "DeleteEarthObservationJobInputRequestTypeDef",
    "DeleteVectorEnrichmentJobInputRequestTypeDef",
    "EarthObservationJobErrorDetailsTypeDef",
    "EoCloudCoverInputTypeDef",
    "EojDataSourceConfigInputTypeDef",
    "ExportEarthObservationJobInputRequestTypeDef",
    "ExportEarthObservationJobOutputTypeDef",
    "ExportErrorDetailsOutputTypeDef",
    "ExportErrorDetailsTypeDef",
    "ExportS3DataInputTypeDef",
    "ExportVectorEnrichmentJobInputRequestTypeDef",
    "ExportVectorEnrichmentJobOutputConfigTypeDef",
    "ExportVectorEnrichmentJobOutputTypeDef",
    "FilterTypeDef",
    "GeoMosaicConfigInputTypeDef",
    "GeometryTypeDef",
    "GetEarthObservationJobInputRequestTypeDef",
    "GetEarthObservationJobOutputTypeDef",
    "GetRasterDataCollectionInputRequestTypeDef",
    "GetRasterDataCollectionOutputTypeDef",
    "GetTileInputRequestTypeDef",
    "GetTileOutputTypeDef",
    "GetVectorEnrichmentJobInputRequestTypeDef",
    "GetVectorEnrichmentJobOutputTypeDef",
    "InputConfigInputTypeDef",
    "InputConfigOutputTypeDef",
    "ItemSourceTypeDef",
    "JobConfigInputTypeDef",
    "LandsatCloudCoverLandInputTypeDef",
    "ListEarthObservationJobInputRequestTypeDef",
    "ListEarthObservationJobOutputConfigTypeDef",
    "ListEarthObservationJobOutputTypeDef",
    "ListRasterDataCollectionsInputRequestTypeDef",
    "ListRasterDataCollectionsOutputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVectorEnrichmentJobInputRequestTypeDef",
    "ListVectorEnrichmentJobOutputConfigTypeDef",
    "ListVectorEnrichmentJobOutputTypeDef",
    "MapMatchingConfigTypeDef",
    "MultiPolygonGeometryInputTypeDef",
    "OperationTypeDef",
    "OutputBandTypeDef",
    "OutputConfigInputTypeDef",
    "OutputResolutionResamplingInputTypeDef",
    "OutputResolutionStackInputTypeDef",
    "PaginatorConfigTypeDef",
    "PlatformInputTypeDef",
    "PolygonGeometryInputTypeDef",
    "PropertiesTypeDef",
    "PropertyFilterTypeDef",
    "PropertyFiltersTypeDef",
    "PropertyTypeDef",
    "RasterDataCollectionMetadataTypeDef",
    "RasterDataCollectionQueryInputTypeDef",
    "RasterDataCollectionQueryOutputTypeDef",
    "RasterDataCollectionQueryWithBandFilterInputTypeDef",
    "ResamplingConfigInputTypeDef",
    "ResponseMetadataTypeDef",
    "ReverseGeocodingConfigTypeDef",
    "S3DataInputTypeDef",
    "SearchRasterDataCollectionInputRequestTypeDef",
    "SearchRasterDataCollectionOutputTypeDef",
    "StackConfigInputTypeDef",
    "StartEarthObservationJobInputRequestTypeDef",
    "StartEarthObservationJobOutputTypeDef",
    "StartVectorEnrichmentJobInputRequestTypeDef",
    "StartVectorEnrichmentJobOutputTypeDef",
    "StopEarthObservationJobInputRequestTypeDef",
    "StopVectorEnrichmentJobInputRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TemporalStatisticsConfigInputTypeDef",
    "TimeRangeFilterInputTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UserDefinedTypeDef",
    "VectorEnrichmentJobConfigTypeDef",
    "VectorEnrichmentJobDataSourceConfigInputTypeDef",
    "VectorEnrichmentJobErrorDetailsTypeDef",
    "VectorEnrichmentJobExportErrorDetailsTypeDef",
    "VectorEnrichmentJobInputConfigTypeDef",
    "VectorEnrichmentJobS3DataTypeDef",
    "ViewOffNadirInputTypeDef",
    "ViewSunAzimuthInputTypeDef",
    "ViewSunElevationInputTypeDef",
    "ZonalStatisticsConfigInputTypeDef",
)

AreaOfInterestGeometryTypeDef = TypedDict(
    "AreaOfInterestGeometryTypeDef",
    {
        "MultiPolygonGeometry": "MultiPolygonGeometryInputTypeDef",
        "PolygonGeometry": "PolygonGeometryInputTypeDef",
    },
    total=False,
)

AreaOfInterestTypeDef = TypedDict(
    "AreaOfInterestTypeDef",
    {
        "AreaOfInterestGeometry": "AreaOfInterestGeometryTypeDef",
    },
    total=False,
)

AssetValueTypeDef = TypedDict(
    "AssetValueTypeDef",
    {
        "Href": str,
    },
    total=False,
)

BandMathConfigInputTypeDef = TypedDict(
    "BandMathConfigInputTypeDef",
    {
        "CustomIndices": "CustomIndicesInputTypeDef",
        "PredefinedIndices": List[str],
    },
    total=False,
)

CloudRemovalConfigInputTypeDef = TypedDict(
    "CloudRemovalConfigInputTypeDef",
    {
        "AlgorithmName": Literal["INTERPOLATION"],
        "InterpolationValue": str,
        "TargetBands": List[str],
    },
    total=False,
)

CustomIndicesInputTypeDef = TypedDict(
    "CustomIndicesInputTypeDef",
    {
        "Operations": List["OperationTypeDef"],
    },
    total=False,
)

DeleteEarthObservationJobInputRequestTypeDef = TypedDict(
    "DeleteEarthObservationJobInputRequestTypeDef",
    {
        "Arn": str,
    },
)

DeleteVectorEnrichmentJobInputRequestTypeDef = TypedDict(
    "DeleteVectorEnrichmentJobInputRequestTypeDef",
    {
        "Arn": str,
    },
)

EarthObservationJobErrorDetailsTypeDef = TypedDict(
    "EarthObservationJobErrorDetailsTypeDef",
    {
        "Message": str,
        "Type": EarthObservationJobErrorTypeType,
    },
    total=False,
)

EoCloudCoverInputTypeDef = TypedDict(
    "EoCloudCoverInputTypeDef",
    {
        "LowerBound": float,
        "UpperBound": float,
    },
)

EojDataSourceConfigInputTypeDef = TypedDict(
    "EojDataSourceConfigInputTypeDef",
    {
        "S3Data": "S3DataInputTypeDef",
    },
    total=False,
)

_RequiredExportEarthObservationJobInputRequestTypeDef = TypedDict(
    "_RequiredExportEarthObservationJobInputRequestTypeDef",
    {
        "Arn": str,
        "ExecutionRoleArn": str,
        "OutputConfig": "OutputConfigInputTypeDef",
    },
)
_OptionalExportEarthObservationJobInputRequestTypeDef = TypedDict(
    "_OptionalExportEarthObservationJobInputRequestTypeDef",
    {
        "ExportSourceImages": bool,
    },
    total=False,
)

class ExportEarthObservationJobInputRequestTypeDef(
    _RequiredExportEarthObservationJobInputRequestTypeDef,
    _OptionalExportEarthObservationJobInputRequestTypeDef,
):
    pass

ExportEarthObservationJobOutputTypeDef = TypedDict(
    "ExportEarthObservationJobOutputTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "ExecutionRoleArn": str,
        "ExportSourceImages": bool,
        "ExportStatus": EarthObservationJobExportStatusType,
        "OutputConfig": "OutputConfigInputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportErrorDetailsOutputTypeDef = TypedDict(
    "ExportErrorDetailsOutputTypeDef",
    {
        "Message": str,
        "Type": ExportErrorTypeType,
    },
    total=False,
)

ExportErrorDetailsTypeDef = TypedDict(
    "ExportErrorDetailsTypeDef",
    {
        "ExportResults": "ExportErrorDetailsOutputTypeDef",
        "ExportSourceImages": "ExportErrorDetailsOutputTypeDef",
    },
    total=False,
)

_RequiredExportS3DataInputTypeDef = TypedDict(
    "_RequiredExportS3DataInputTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalExportS3DataInputTypeDef = TypedDict(
    "_OptionalExportS3DataInputTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

class ExportS3DataInputTypeDef(
    _RequiredExportS3DataInputTypeDef, _OptionalExportS3DataInputTypeDef
):
    pass

ExportVectorEnrichmentJobInputRequestTypeDef = TypedDict(
    "ExportVectorEnrichmentJobInputRequestTypeDef",
    {
        "Arn": str,
        "ExecutionRoleArn": str,
        "OutputConfig": "ExportVectorEnrichmentJobOutputConfigTypeDef",
    },
)

ExportVectorEnrichmentJobOutputConfigTypeDef = TypedDict(
    "ExportVectorEnrichmentJobOutputConfigTypeDef",
    {
        "S3Data": "VectorEnrichmentJobS3DataTypeDef",
    },
)

ExportVectorEnrichmentJobOutputTypeDef = TypedDict(
    "ExportVectorEnrichmentJobOutputTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "ExecutionRoleArn": str,
        "ExportStatus": VectorEnrichmentJobExportStatusType,
        "OutputConfig": "ExportVectorEnrichmentJobOutputConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFilterTypeDef = TypedDict(
    "_RequiredFilterTypeDef",
    {
        "Name": str,
        "Type": str,
    },
)
_OptionalFilterTypeDef = TypedDict(
    "_OptionalFilterTypeDef",
    {
        "Maximum": float,
        "Minimum": float,
    },
    total=False,
)

class FilterTypeDef(_RequiredFilterTypeDef, _OptionalFilterTypeDef):
    pass

GeoMosaicConfigInputTypeDef = TypedDict(
    "GeoMosaicConfigInputTypeDef",
    {
        "AlgorithmName": AlgorithmNameGeoMosaicType,
        "TargetBands": List[str],
    },
    total=False,
)

GeometryTypeDef = TypedDict(
    "GeometryTypeDef",
    {
        "Coordinates": List[List[List[float]]],
        "Type": str,
    },
)

GetEarthObservationJobInputRequestTypeDef = TypedDict(
    "GetEarthObservationJobInputRequestTypeDef",
    {
        "Arn": str,
    },
)

GetEarthObservationJobOutputTypeDef = TypedDict(
    "GetEarthObservationJobOutputTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "DurationInSeconds": int,
        "ErrorDetails": "EarthObservationJobErrorDetailsTypeDef",
        "ExecutionRoleArn": str,
        "ExportErrorDetails": "ExportErrorDetailsTypeDef",
        "ExportStatus": EarthObservationJobExportStatusType,
        "InputConfig": "InputConfigOutputTypeDef",
        "JobConfig": "JobConfigInputTypeDef",
        "KmsKeyId": str,
        "Name": str,
        "OutputBands": List["OutputBandTypeDef"],
        "Status": EarthObservationJobStatusType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRasterDataCollectionInputRequestTypeDef = TypedDict(
    "GetRasterDataCollectionInputRequestTypeDef",
    {
        "Arn": str,
    },
)

GetRasterDataCollectionOutputTypeDef = TypedDict(
    "GetRasterDataCollectionOutputTypeDef",
    {
        "Arn": str,
        "Description": str,
        "DescriptionPageUrl": str,
        "ImageSourceBands": List[str],
        "Name": str,
        "SupportedFilters": List["FilterTypeDef"],
        "Tags": Dict[str, str],
        "Type": DataCollectionTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTileInputRequestTypeDef = TypedDict(
    "_RequiredGetTileInputRequestTypeDef",
    {
        "Arn": str,
        "ImageAssets": List[str],
        "Target": TargetOptionsType,
        "x": int,
        "y": int,
        "z": int,
    },
)
_OptionalGetTileInputRequestTypeDef = TypedDict(
    "_OptionalGetTileInputRequestTypeDef",
    {
        "ImageMask": bool,
        "OutputDataType": OutputTypeType,
        "OutputFormat": str,
        "PropertyFilters": str,
        "TimeRangeFilter": str,
    },
    total=False,
)

class GetTileInputRequestTypeDef(
    _RequiredGetTileInputRequestTypeDef, _OptionalGetTileInputRequestTypeDef
):
    pass

GetTileOutputTypeDef = TypedDict(
    "GetTileOutputTypeDef",
    {
        "BinaryFile": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVectorEnrichmentJobInputRequestTypeDef = TypedDict(
    "GetVectorEnrichmentJobInputRequestTypeDef",
    {
        "Arn": str,
    },
)

GetVectorEnrichmentJobOutputTypeDef = TypedDict(
    "GetVectorEnrichmentJobOutputTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "DurationInSeconds": int,
        "ErrorDetails": "VectorEnrichmentJobErrorDetailsTypeDef",
        "ExecutionRoleArn": str,
        "ExportErrorDetails": "VectorEnrichmentJobExportErrorDetailsTypeDef",
        "ExportStatus": VectorEnrichmentJobExportStatusType,
        "InputConfig": "VectorEnrichmentJobInputConfigTypeDef",
        "JobConfig": "VectorEnrichmentJobConfigTypeDef",
        "KmsKeyId": str,
        "Name": str,
        "Status": VectorEnrichmentJobStatusType,
        "Tags": Dict[str, str],
        "Type": VectorEnrichmentJobTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputConfigInputTypeDef = TypedDict(
    "InputConfigInputTypeDef",
    {
        "DataSourceConfig": "EojDataSourceConfigInputTypeDef",
        "PreviousEarthObservationJobArn": str,
        "RasterDataCollectionQuery": "RasterDataCollectionQueryInputTypeDef",
    },
    total=False,
)

InputConfigOutputTypeDef = TypedDict(
    "InputConfigOutputTypeDef",
    {
        "DataSourceConfig": "EojDataSourceConfigInputTypeDef",
        "PreviousEarthObservationJobArn": str,
        "RasterDataCollectionQuery": "RasterDataCollectionQueryOutputTypeDef",
    },
    total=False,
)

_RequiredItemSourceTypeDef = TypedDict(
    "_RequiredItemSourceTypeDef",
    {
        "DateTime": datetime,
        "Geometry": "GeometryTypeDef",
        "Id": str,
    },
)
_OptionalItemSourceTypeDef = TypedDict(
    "_OptionalItemSourceTypeDef",
    {
        "Assets": Dict[str, "AssetValueTypeDef"],
        "Properties": "PropertiesTypeDef",
    },
    total=False,
)

class ItemSourceTypeDef(_RequiredItemSourceTypeDef, _OptionalItemSourceTypeDef):
    pass

JobConfigInputTypeDef = TypedDict(
    "JobConfigInputTypeDef",
    {
        "BandMathConfig": "BandMathConfigInputTypeDef",
        "CloudMaskingConfig": Dict[str, Any],
        "CloudRemovalConfig": "CloudRemovalConfigInputTypeDef",
        "GeoMosaicConfig": "GeoMosaicConfigInputTypeDef",
        "LandCoverSegmentationConfig": Dict[str, Any],
        "ResamplingConfig": "ResamplingConfigInputTypeDef",
        "StackConfig": "StackConfigInputTypeDef",
        "TemporalStatisticsConfig": "TemporalStatisticsConfigInputTypeDef",
        "ZonalStatisticsConfig": "ZonalStatisticsConfigInputTypeDef",
    },
    total=False,
)

LandsatCloudCoverLandInputTypeDef = TypedDict(
    "LandsatCloudCoverLandInputTypeDef",
    {
        "LowerBound": float,
        "UpperBound": float,
    },
)

ListEarthObservationJobInputRequestTypeDef = TypedDict(
    "ListEarthObservationJobInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "SortBy": str,
        "SortOrder": SortOrderType,
        "StatusEquals": EarthObservationJobStatusType,
    },
    total=False,
)

_RequiredListEarthObservationJobOutputConfigTypeDef = TypedDict(
    "_RequiredListEarthObservationJobOutputConfigTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "DurationInSeconds": int,
        "Name": str,
        "OperationType": str,
        "Status": EarthObservationJobStatusType,
    },
)
_OptionalListEarthObservationJobOutputConfigTypeDef = TypedDict(
    "_OptionalListEarthObservationJobOutputConfigTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class ListEarthObservationJobOutputConfigTypeDef(
    _RequiredListEarthObservationJobOutputConfigTypeDef,
    _OptionalListEarthObservationJobOutputConfigTypeDef,
):
    pass

ListEarthObservationJobOutputTypeDef = TypedDict(
    "ListEarthObservationJobOutputTypeDef",
    {
        "EarthObservationJobSummaries": List["ListEarthObservationJobOutputConfigTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRasterDataCollectionsInputRequestTypeDef = TypedDict(
    "ListRasterDataCollectionsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListRasterDataCollectionsOutputTypeDef = TypedDict(
    "ListRasterDataCollectionsOutputTypeDef",
    {
        "NextToken": str,
        "RasterDataCollectionSummaries": List["RasterDataCollectionMetadataTypeDef"],
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

ListVectorEnrichmentJobInputRequestTypeDef = TypedDict(
    "ListVectorEnrichmentJobInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "SortBy": str,
        "SortOrder": SortOrderType,
        "StatusEquals": str,
    },
    total=False,
)

_RequiredListVectorEnrichmentJobOutputConfigTypeDef = TypedDict(
    "_RequiredListVectorEnrichmentJobOutputConfigTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "DurationInSeconds": int,
        "Name": str,
        "Status": VectorEnrichmentJobStatusType,
        "Type": VectorEnrichmentJobTypeType,
    },
)
_OptionalListVectorEnrichmentJobOutputConfigTypeDef = TypedDict(
    "_OptionalListVectorEnrichmentJobOutputConfigTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class ListVectorEnrichmentJobOutputConfigTypeDef(
    _RequiredListVectorEnrichmentJobOutputConfigTypeDef,
    _OptionalListVectorEnrichmentJobOutputConfigTypeDef,
):
    pass

ListVectorEnrichmentJobOutputTypeDef = TypedDict(
    "ListVectorEnrichmentJobOutputTypeDef",
    {
        "NextToken": str,
        "VectorEnrichmentJobSummaries": List["ListVectorEnrichmentJobOutputConfigTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MapMatchingConfigTypeDef = TypedDict(
    "MapMatchingConfigTypeDef",
    {
        "IdAttributeName": str,
        "TimestampAttributeName": str,
        "XAttributeName": str,
        "YAttributeName": str,
    },
)

MultiPolygonGeometryInputTypeDef = TypedDict(
    "MultiPolygonGeometryInputTypeDef",
    {
        "Coordinates": List[List[List[List[float]]]],
    },
)

_RequiredOperationTypeDef = TypedDict(
    "_RequiredOperationTypeDef",
    {
        "Equation": str,
        "Name": str,
    },
)
_OptionalOperationTypeDef = TypedDict(
    "_OptionalOperationTypeDef",
    {
        "OutputType": OutputTypeType,
    },
    total=False,
)

class OperationTypeDef(_RequiredOperationTypeDef, _OptionalOperationTypeDef):
    pass

OutputBandTypeDef = TypedDict(
    "OutputBandTypeDef",
    {
        "BandName": str,
        "OutputDataType": OutputTypeType,
    },
)

OutputConfigInputTypeDef = TypedDict(
    "OutputConfigInputTypeDef",
    {
        "S3Data": "ExportS3DataInputTypeDef",
    },
)

OutputResolutionResamplingInputTypeDef = TypedDict(
    "OutputResolutionResamplingInputTypeDef",
    {
        "UserDefined": "UserDefinedTypeDef",
    },
)

OutputResolutionStackInputTypeDef = TypedDict(
    "OutputResolutionStackInputTypeDef",
    {
        "Predefined": PredefinedResolutionType,
        "UserDefined": "UserDefinedTypeDef",
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

_RequiredPlatformInputTypeDef = TypedDict(
    "_RequiredPlatformInputTypeDef",
    {
        "Value": str,
    },
)
_OptionalPlatformInputTypeDef = TypedDict(
    "_OptionalPlatformInputTypeDef",
    {
        "ComparisonOperator": ComparisonOperatorType,
    },
    total=False,
)

class PlatformInputTypeDef(_RequiredPlatformInputTypeDef, _OptionalPlatformInputTypeDef):
    pass

PolygonGeometryInputTypeDef = TypedDict(
    "PolygonGeometryInputTypeDef",
    {
        "Coordinates": List[List[List[float]]],
    },
)

PropertiesTypeDef = TypedDict(
    "PropertiesTypeDef",
    {
        "EoCloudCover": float,
        "LandsatCloudCoverLand": float,
        "Platform": str,
        "ViewOffNadir": float,
        "ViewSunAzimuth": float,
        "ViewSunElevation": float,
    },
    total=False,
)

PropertyFilterTypeDef = TypedDict(
    "PropertyFilterTypeDef",
    {
        "Property": "PropertyTypeDef",
    },
)

PropertyFiltersTypeDef = TypedDict(
    "PropertyFiltersTypeDef",
    {
        "LogicalOperator": Literal["AND"],
        "Properties": List["PropertyFilterTypeDef"],
    },
    total=False,
)

PropertyTypeDef = TypedDict(
    "PropertyTypeDef",
    {
        "EoCloudCover": "EoCloudCoverInputTypeDef",
        "LandsatCloudCoverLand": "LandsatCloudCoverLandInputTypeDef",
        "Platform": "PlatformInputTypeDef",
        "ViewOffNadir": "ViewOffNadirInputTypeDef",
        "ViewSunAzimuth": "ViewSunAzimuthInputTypeDef",
        "ViewSunElevation": "ViewSunElevationInputTypeDef",
    },
    total=False,
)

_RequiredRasterDataCollectionMetadataTypeDef = TypedDict(
    "_RequiredRasterDataCollectionMetadataTypeDef",
    {
        "Arn": str,
        "Description": str,
        "Name": str,
        "SupportedFilters": List["FilterTypeDef"],
        "Type": DataCollectionTypeType,
    },
)
_OptionalRasterDataCollectionMetadataTypeDef = TypedDict(
    "_OptionalRasterDataCollectionMetadataTypeDef",
    {
        "DescriptionPageUrl": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class RasterDataCollectionMetadataTypeDef(
    _RequiredRasterDataCollectionMetadataTypeDef, _OptionalRasterDataCollectionMetadataTypeDef
):
    pass

_RequiredRasterDataCollectionQueryInputTypeDef = TypedDict(
    "_RequiredRasterDataCollectionQueryInputTypeDef",
    {
        "RasterDataCollectionArn": str,
        "TimeRangeFilter": "TimeRangeFilterInputTypeDef",
    },
)
_OptionalRasterDataCollectionQueryInputTypeDef = TypedDict(
    "_OptionalRasterDataCollectionQueryInputTypeDef",
    {
        "AreaOfInterest": "AreaOfInterestTypeDef",
        "PropertyFilters": "PropertyFiltersTypeDef",
    },
    total=False,
)

class RasterDataCollectionQueryInputTypeDef(
    _RequiredRasterDataCollectionQueryInputTypeDef, _OptionalRasterDataCollectionQueryInputTypeDef
):
    pass

_RequiredRasterDataCollectionQueryOutputTypeDef = TypedDict(
    "_RequiredRasterDataCollectionQueryOutputTypeDef",
    {
        "RasterDataCollectionArn": str,
        "RasterDataCollectionName": str,
        "TimeRangeFilter": "TimeRangeFilterInputTypeDef",
    },
)
_OptionalRasterDataCollectionQueryOutputTypeDef = TypedDict(
    "_OptionalRasterDataCollectionQueryOutputTypeDef",
    {
        "AreaOfInterest": "AreaOfInterestTypeDef",
        "PropertyFilters": "PropertyFiltersTypeDef",
    },
    total=False,
)

class RasterDataCollectionQueryOutputTypeDef(
    _RequiredRasterDataCollectionQueryOutputTypeDef, _OptionalRasterDataCollectionQueryOutputTypeDef
):
    pass

_RequiredRasterDataCollectionQueryWithBandFilterInputTypeDef = TypedDict(
    "_RequiredRasterDataCollectionQueryWithBandFilterInputTypeDef",
    {
        "TimeRangeFilter": "TimeRangeFilterInputTypeDef",
    },
)
_OptionalRasterDataCollectionQueryWithBandFilterInputTypeDef = TypedDict(
    "_OptionalRasterDataCollectionQueryWithBandFilterInputTypeDef",
    {
        "AreaOfInterest": "AreaOfInterestTypeDef",
        "BandFilter": List[str],
        "PropertyFilters": "PropertyFiltersTypeDef",
    },
    total=False,
)

class RasterDataCollectionQueryWithBandFilterInputTypeDef(
    _RequiredRasterDataCollectionQueryWithBandFilterInputTypeDef,
    _OptionalRasterDataCollectionQueryWithBandFilterInputTypeDef,
):
    pass

_RequiredResamplingConfigInputTypeDef = TypedDict(
    "_RequiredResamplingConfigInputTypeDef",
    {
        "OutputResolution": "OutputResolutionResamplingInputTypeDef",
    },
)
_OptionalResamplingConfigInputTypeDef = TypedDict(
    "_OptionalResamplingConfigInputTypeDef",
    {
        "AlgorithmName": AlgorithmNameResamplingType,
        "TargetBands": List[str],
    },
    total=False,
)

class ResamplingConfigInputTypeDef(
    _RequiredResamplingConfigInputTypeDef, _OptionalResamplingConfigInputTypeDef
):
    pass

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

ReverseGeocodingConfigTypeDef = TypedDict(
    "ReverseGeocodingConfigTypeDef",
    {
        "XAttributeName": str,
        "YAttributeName": str,
    },
)

_RequiredS3DataInputTypeDef = TypedDict(
    "_RequiredS3DataInputTypeDef",
    {
        "MetadataProvider": Literal["PLANET_ORDER"],
        "S3Uri": str,
    },
)
_OptionalS3DataInputTypeDef = TypedDict(
    "_OptionalS3DataInputTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

class S3DataInputTypeDef(_RequiredS3DataInputTypeDef, _OptionalS3DataInputTypeDef):
    pass

_RequiredSearchRasterDataCollectionInputRequestTypeDef = TypedDict(
    "_RequiredSearchRasterDataCollectionInputRequestTypeDef",
    {
        "Arn": str,
        "RasterDataCollectionQuery": "RasterDataCollectionQueryWithBandFilterInputTypeDef",
    },
)
_OptionalSearchRasterDataCollectionInputRequestTypeDef = TypedDict(
    "_OptionalSearchRasterDataCollectionInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class SearchRasterDataCollectionInputRequestTypeDef(
    _RequiredSearchRasterDataCollectionInputRequestTypeDef,
    _OptionalSearchRasterDataCollectionInputRequestTypeDef,
):
    pass

SearchRasterDataCollectionOutputTypeDef = TypedDict(
    "SearchRasterDataCollectionOutputTypeDef",
    {
        "ApproximateResultCount": int,
        "Items": List["ItemSourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StackConfigInputTypeDef = TypedDict(
    "StackConfigInputTypeDef",
    {
        "OutputResolution": "OutputResolutionStackInputTypeDef",
        "TargetBands": List[str],
    },
    total=False,
)

_RequiredStartEarthObservationJobInputRequestTypeDef = TypedDict(
    "_RequiredStartEarthObservationJobInputRequestTypeDef",
    {
        "InputConfig": "InputConfigInputTypeDef",
        "JobConfig": "JobConfigInputTypeDef",
        "Name": str,
    },
)
_OptionalStartEarthObservationJobInputRequestTypeDef = TypedDict(
    "_OptionalStartEarthObservationJobInputRequestTypeDef",
    {
        "ClientToken": str,
        "ExecutionRoleArn": str,
        "KmsKeyId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class StartEarthObservationJobInputRequestTypeDef(
    _RequiredStartEarthObservationJobInputRequestTypeDef,
    _OptionalStartEarthObservationJobInputRequestTypeDef,
):
    pass

StartEarthObservationJobOutputTypeDef = TypedDict(
    "StartEarthObservationJobOutputTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "DurationInSeconds": int,
        "ExecutionRoleArn": str,
        "InputConfig": "InputConfigOutputTypeDef",
        "JobConfig": "JobConfigInputTypeDef",
        "KmsKeyId": str,
        "Name": str,
        "Status": EarthObservationJobStatusType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartVectorEnrichmentJobInputRequestTypeDef = TypedDict(
    "_RequiredStartVectorEnrichmentJobInputRequestTypeDef",
    {
        "ExecutionRoleArn": str,
        "InputConfig": "VectorEnrichmentJobInputConfigTypeDef",
        "JobConfig": "VectorEnrichmentJobConfigTypeDef",
        "Name": str,
    },
)
_OptionalStartVectorEnrichmentJobInputRequestTypeDef = TypedDict(
    "_OptionalStartVectorEnrichmentJobInputRequestTypeDef",
    {
        "ClientToken": str,
        "KmsKeyId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class StartVectorEnrichmentJobInputRequestTypeDef(
    _RequiredStartVectorEnrichmentJobInputRequestTypeDef,
    _OptionalStartVectorEnrichmentJobInputRequestTypeDef,
):
    pass

StartVectorEnrichmentJobOutputTypeDef = TypedDict(
    "StartVectorEnrichmentJobOutputTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "DurationInSeconds": int,
        "ExecutionRoleArn": str,
        "InputConfig": "VectorEnrichmentJobInputConfigTypeDef",
        "JobConfig": "VectorEnrichmentJobConfigTypeDef",
        "KmsKeyId": str,
        "Name": str,
        "Status": VectorEnrichmentJobStatusType,
        "Tags": Dict[str, str],
        "Type": VectorEnrichmentJobTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopEarthObservationJobInputRequestTypeDef = TypedDict(
    "StopEarthObservationJobInputRequestTypeDef",
    {
        "Arn": str,
    },
)

StopVectorEnrichmentJobInputRequestTypeDef = TypedDict(
    "StopVectorEnrichmentJobInputRequestTypeDef",
    {
        "Arn": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

_RequiredTemporalStatisticsConfigInputTypeDef = TypedDict(
    "_RequiredTemporalStatisticsConfigInputTypeDef",
    {
        "Statistics": List[TemporalStatisticsType],
    },
)
_OptionalTemporalStatisticsConfigInputTypeDef = TypedDict(
    "_OptionalTemporalStatisticsConfigInputTypeDef",
    {
        "GroupBy": GroupByType,
        "TargetBands": List[str],
    },
    total=False,
)

class TemporalStatisticsConfigInputTypeDef(
    _RequiredTemporalStatisticsConfigInputTypeDef, _OptionalTemporalStatisticsConfigInputTypeDef
):
    pass

TimeRangeFilterInputTypeDef = TypedDict(
    "TimeRangeFilterInputTypeDef",
    {
        "EndTime": datetime,
        "StartTime": datetime,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UserDefinedTypeDef = TypedDict(
    "UserDefinedTypeDef",
    {
        "Unit": Literal["METERS"],
        "Value": float,
    },
)

VectorEnrichmentJobConfigTypeDef = TypedDict(
    "VectorEnrichmentJobConfigTypeDef",
    {
        "MapMatchingConfig": "MapMatchingConfigTypeDef",
        "ReverseGeocodingConfig": "ReverseGeocodingConfigTypeDef",
    },
    total=False,
)

VectorEnrichmentJobDataSourceConfigInputTypeDef = TypedDict(
    "VectorEnrichmentJobDataSourceConfigInputTypeDef",
    {
        "S3Data": "VectorEnrichmentJobS3DataTypeDef",
    },
    total=False,
)

VectorEnrichmentJobErrorDetailsTypeDef = TypedDict(
    "VectorEnrichmentJobErrorDetailsTypeDef",
    {
        "ErrorMessage": str,
        "ErrorType": VectorEnrichmentJobErrorTypeType,
    },
    total=False,
)

VectorEnrichmentJobExportErrorDetailsTypeDef = TypedDict(
    "VectorEnrichmentJobExportErrorDetailsTypeDef",
    {
        "Message": str,
        "Type": VectorEnrichmentJobExportErrorTypeType,
    },
    total=False,
)

VectorEnrichmentJobInputConfigTypeDef = TypedDict(
    "VectorEnrichmentJobInputConfigTypeDef",
    {
        "DataSourceConfig": "VectorEnrichmentJobDataSourceConfigInputTypeDef",
        "DocumentType": Literal["CSV"],
    },
)

_RequiredVectorEnrichmentJobS3DataTypeDef = TypedDict(
    "_RequiredVectorEnrichmentJobS3DataTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalVectorEnrichmentJobS3DataTypeDef = TypedDict(
    "_OptionalVectorEnrichmentJobS3DataTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

class VectorEnrichmentJobS3DataTypeDef(
    _RequiredVectorEnrichmentJobS3DataTypeDef, _OptionalVectorEnrichmentJobS3DataTypeDef
):
    pass

ViewOffNadirInputTypeDef = TypedDict(
    "ViewOffNadirInputTypeDef",
    {
        "LowerBound": float,
        "UpperBound": float,
    },
)

ViewSunAzimuthInputTypeDef = TypedDict(
    "ViewSunAzimuthInputTypeDef",
    {
        "LowerBound": float,
        "UpperBound": float,
    },
)

ViewSunElevationInputTypeDef = TypedDict(
    "ViewSunElevationInputTypeDef",
    {
        "LowerBound": float,
        "UpperBound": float,
    },
)

_RequiredZonalStatisticsConfigInputTypeDef = TypedDict(
    "_RequiredZonalStatisticsConfigInputTypeDef",
    {
        "Statistics": List[ZonalStatisticsType],
        "ZoneS3Path": str,
    },
)
_OptionalZonalStatisticsConfigInputTypeDef = TypedDict(
    "_OptionalZonalStatisticsConfigInputTypeDef",
    {
        "TargetBands": List[str],
    },
    total=False,
)

class ZonalStatisticsConfigInputTypeDef(
    _RequiredZonalStatisticsConfigInputTypeDef, _OptionalZonalStatisticsConfigInputTypeDef
):
    pass
