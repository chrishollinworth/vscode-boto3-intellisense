"""
Type annotations for applicationcostprofiler service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_applicationcostprofiler.type_defs import DeleteReportDefinitionRequestTypeDef

    data: DeleteReportDefinitionRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import FormatType, ReportFrequencyType, S3BucketRegionType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
else:
    from typing import Dict, List
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "DeleteReportDefinitionRequestTypeDef",
    "DeleteReportDefinitionResultTypeDef",
    "GetReportDefinitionRequestTypeDef",
    "GetReportDefinitionResultTypeDef",
    "ImportApplicationUsageRequestTypeDef",
    "ImportApplicationUsageResultTypeDef",
    "ListReportDefinitionsRequestPaginateTypeDef",
    "ListReportDefinitionsRequestTypeDef",
    "ListReportDefinitionsResultTypeDef",
    "PaginatorConfigTypeDef",
    "PutReportDefinitionRequestTypeDef",
    "PutReportDefinitionResultTypeDef",
    "ReportDefinitionTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "SourceS3LocationTypeDef",
    "UpdateReportDefinitionRequestTypeDef",
    "UpdateReportDefinitionResultTypeDef",
)

class DeleteReportDefinitionRequestTypeDef(TypedDict):
    reportId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetReportDefinitionRequestTypeDef(TypedDict):
    reportId: str

class S3LocationTypeDef(TypedDict):
    bucket: str
    prefix: str

class SourceS3LocationTypeDef(TypedDict):
    bucket: str
    key: str
    region: NotRequired[S3BucketRegionType]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListReportDefinitionsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class DeleteReportDefinitionResultTypeDef(TypedDict):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportApplicationUsageResultTypeDef(TypedDict):
    importId: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutReportDefinitionResultTypeDef(TypedDict):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReportDefinitionResultTypeDef(TypedDict):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef

GetReportDefinitionResultTypeDef = TypedDict(
    "GetReportDefinitionResultTypeDef",
    {
        "reportId": str,
        "reportDescription": str,
        "reportFrequency": ReportFrequencyType,
        "format": FormatType,
        "destinationS3Location": S3LocationTypeDef,
        "createdAt": datetime,
        "lastUpdated": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutReportDefinitionRequestTypeDef = TypedDict(
    "PutReportDefinitionRequestTypeDef",
    {
        "reportId": str,
        "reportDescription": str,
        "reportFrequency": ReportFrequencyType,
        "format": FormatType,
        "destinationS3Location": S3LocationTypeDef,
    },
)
ReportDefinitionTypeDef = TypedDict(
    "ReportDefinitionTypeDef",
    {
        "reportId": NotRequired[str],
        "reportDescription": NotRequired[str],
        "reportFrequency": NotRequired[ReportFrequencyType],
        "format": NotRequired[FormatType],
        "destinationS3Location": NotRequired[S3LocationTypeDef],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
    },
)
UpdateReportDefinitionRequestTypeDef = TypedDict(
    "UpdateReportDefinitionRequestTypeDef",
    {
        "reportId": str,
        "reportDescription": str,
        "reportFrequency": ReportFrequencyType,
        "format": FormatType,
        "destinationS3Location": S3LocationTypeDef,
    },
)

class ImportApplicationUsageRequestTypeDef(TypedDict):
    sourceS3Location: SourceS3LocationTypeDef

class ListReportDefinitionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListReportDefinitionsResultTypeDef(TypedDict):
    reportDefinitions: List[ReportDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
