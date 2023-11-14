"""
Type annotations for sagemaker-geospatial service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_geospatial/literals.html)

Usage::

    ```python
    from mypy_boto3_sagemaker_geospatial.literals import AlgorithmNameCloudRemovalType

    data: AlgorithmNameCloudRemovalType = "INTERPOLATION"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AlgorithmNameCloudRemovalType",
    "AlgorithmNameGeoMosaicType",
    "AlgorithmNameResamplingType",
    "ComparisonOperatorType",
    "DataCollectionTypeType",
    "EarthObservationJobErrorTypeType",
    "EarthObservationJobExportStatusType",
    "EarthObservationJobStatusType",
    "ExportErrorTypeType",
    "GroupByType",
    "ListEarthObservationJobsPaginatorName",
    "ListRasterDataCollectionsPaginatorName",
    "ListVectorEnrichmentJobsPaginatorName",
    "LogicalOperatorType",
    "OutputTypeType",
    "PredefinedResolutionType",
    "SortOrderType",
    "TargetOptionsType",
    "TemporalStatisticsType",
    "UnitType",
    "VectorEnrichmentJobDocumentTypeType",
    "VectorEnrichmentJobErrorTypeType",
    "VectorEnrichmentJobExportErrorTypeType",
    "VectorEnrichmentJobExportStatusType",
    "VectorEnrichmentJobStatusType",
    "VectorEnrichmentJobTypeType",
    "ZonalStatisticsType",
)

AlgorithmNameCloudRemovalType = Literal["INTERPOLATION"]
AlgorithmNameGeoMosaicType = Literal[
    "AVERAGE",
    "BILINEAR",
    "CUBIC",
    "CUBICSPLINE",
    "LANCZOS",
    "MAX",
    "MED",
    "MIN",
    "MODE",
    "NEAR",
    "Q1",
    "Q3",
    "RMS",
    "SUM",
]
AlgorithmNameResamplingType = Literal[
    "AVERAGE",
    "BILINEAR",
    "CUBIC",
    "CUBICSPLINE",
    "LANCZOS",
    "MAX",
    "MED",
    "MIN",
    "MODE",
    "NEAR",
    "Q1",
    "Q3",
    "RMS",
    "SUM",
]
ComparisonOperatorType = Literal["EQUALS", "NOT_EQUALS", "STARTS_WITH"]
DataCollectionTypeType = Literal["PREMIUM", "PUBLIC", "USER"]
EarthObservationJobErrorTypeType = Literal["CLIENT_ERROR", "SERVER_ERROR"]
EarthObservationJobExportStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
EarthObservationJobStatusType = Literal[
    "COMPLETED",
    "DELETED",
    "DELETING",
    "FAILED",
    "INITIALIZING",
    "IN_PROGRESS",
    "STOPPED",
    "STOPPING",
]
ExportErrorTypeType = Literal["CLIENT_ERROR", "SERVER_ERROR"]
GroupByType = Literal["ALL", "YEARLY"]
ListEarthObservationJobsPaginatorName = Literal["list_earth_observation_jobs"]
ListRasterDataCollectionsPaginatorName = Literal["list_raster_data_collections"]
ListVectorEnrichmentJobsPaginatorName = Literal["list_vector_enrichment_jobs"]
LogicalOperatorType = Literal["AND"]
OutputTypeType = Literal["FLOAT32", "FLOAT64", "INT16", "INT32", "UINT16"]
PredefinedResolutionType = Literal["AVERAGE", "HIGHEST", "LOWEST"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
TargetOptionsType = Literal["INPUT", "OUTPUT"]
TemporalStatisticsType = Literal["MEAN", "MEDIAN", "STANDARD_DEVIATION"]
UnitType = Literal["METERS"]
VectorEnrichmentJobDocumentTypeType = Literal["CSV"]
VectorEnrichmentJobErrorTypeType = Literal["CLIENT_ERROR", "SERVER_ERROR"]
VectorEnrichmentJobExportErrorTypeType = Literal["CLIENT_ERROR", "SERVER_ERROR"]
VectorEnrichmentJobExportStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
VectorEnrichmentJobStatusType = Literal[
    "COMPLETED",
    "DELETED",
    "DELETING",
    "FAILED",
    "INITIALIZING",
    "IN_PROGRESS",
    "STOPPED",
    "STOPPING",
]
VectorEnrichmentJobTypeType = Literal["MAP_MATCHING", "REVERSE_GEOCODING"]
ZonalStatisticsType = Literal["MAX", "MEAN", "MEDIAN", "MIN", "STANDARD_DEVIATION", "SUM"]
