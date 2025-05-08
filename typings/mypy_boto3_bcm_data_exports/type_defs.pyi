"""
Type annotations for bcm-data-exports service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_bcm_data_exports.type_defs import ColumnTypeDef

    data: ColumnTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    CompressionOptionType,
    ExecutionStatusCodeType,
    ExecutionStatusReasonType,
    ExportStatusCodeType,
    FormatOptionType,
    OverwriteOptionType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ColumnTypeDef",
    "CreateExportRequestTypeDef",
    "CreateExportResponseTypeDef",
    "DataQueryOutputTypeDef",
    "DataQueryTypeDef",
    "DeleteExportRequestTypeDef",
    "DeleteExportResponseTypeDef",
    "DestinationConfigurationsTypeDef",
    "ExecutionReferenceTypeDef",
    "ExecutionStatusTypeDef",
    "ExportOutputTypeDef",
    "ExportReferenceTypeDef",
    "ExportStatusTypeDef",
    "ExportTypeDef",
    "ExportUnionTypeDef",
    "GetExecutionRequestTypeDef",
    "GetExecutionResponseTypeDef",
    "GetExportRequestTypeDef",
    "GetExportResponseTypeDef",
    "GetTableRequestTypeDef",
    "GetTableResponseTypeDef",
    "ListExecutionsRequestPaginateTypeDef",
    "ListExecutionsRequestTypeDef",
    "ListExecutionsResponseTypeDef",
    "ListExportsRequestPaginateTypeDef",
    "ListExportsRequestTypeDef",
    "ListExportsResponseTypeDef",
    "ListTablesRequestPaginateTypeDef",
    "ListTablesRequestTypeDef",
    "ListTablesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RefreshCadenceTypeDef",
    "ResourceTagTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationTypeDef",
    "S3OutputConfigurationsTypeDef",
    "TablePropertyDescriptionTypeDef",
    "TableTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateExportRequestTypeDef",
    "UpdateExportResponseTypeDef",
)

ColumnTypeDef = TypedDict(
    "ColumnTypeDef",
    {
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[str],
    },
)

class ResourceTagTypeDef(TypedDict):
    Key: str
    Value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DataQueryOutputTypeDef(TypedDict):
    QueryStatement: str
    TableConfigurations: NotRequired[Dict[str, Dict[str, str]]]

class DataQueryTypeDef(TypedDict):
    QueryStatement: str
    TableConfigurations: NotRequired[Mapping[str, Mapping[str, str]]]

class DeleteExportRequestTypeDef(TypedDict):
    ExportArn: str

class ExecutionStatusTypeDef(TypedDict):
    CompletedAt: NotRequired[datetime]
    CreatedAt: NotRequired[datetime]
    LastUpdatedAt: NotRequired[datetime]
    StatusCode: NotRequired[ExecutionStatusCodeType]
    StatusReason: NotRequired[ExecutionStatusReasonType]

class RefreshCadenceTypeDef(TypedDict):
    Frequency: Literal["SYNCHRONOUS"]

class ExportStatusTypeDef(TypedDict):
    CreatedAt: NotRequired[datetime]
    LastRefreshedAt: NotRequired[datetime]
    LastUpdatedAt: NotRequired[datetime]
    StatusCode: NotRequired[ExportStatusCodeType]
    StatusReason: NotRequired[ExecutionStatusReasonType]

class GetExecutionRequestTypeDef(TypedDict):
    ExecutionId: str
    ExportArn: str

class GetExportRequestTypeDef(TypedDict):
    ExportArn: str

class GetTableRequestTypeDef(TypedDict):
    TableName: str
    TableProperties: NotRequired[Mapping[str, str]]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListExecutionsRequestTypeDef(TypedDict):
    ExportArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListExportsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTablesRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class S3OutputConfigurationsTypeDef(TypedDict):
    Compression: CompressionOptionType
    Format: FormatOptionType
    OutputType: Literal["CUSTOM"]
    Overwrite: OverwriteOptionType

class TablePropertyDescriptionTypeDef(TypedDict):
    DefaultValue: NotRequired[str]
    Description: NotRequired[str]
    Name: NotRequired[str]
    ValidValues: NotRequired[List[str]]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    ResourceTagKeys: Sequence[str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    ResourceTags: Sequence[ResourceTagTypeDef]

class CreateExportResponseTypeDef(TypedDict):
    ExportArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteExportResponseTypeDef(TypedDict):
    ExportArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTableResponseTypeDef(TypedDict):
    Description: str
    Schema: List[ColumnTypeDef]
    TableName: str
    TableProperties: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    ResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateExportResponseTypeDef(TypedDict):
    ExportArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExecutionReferenceTypeDef(TypedDict):
    ExecutionId: str
    ExecutionStatus: ExecutionStatusTypeDef

class ExportReferenceTypeDef(TypedDict):
    ExportArn: str
    ExportName: str
    ExportStatus: ExportStatusTypeDef

class ListExecutionsRequestPaginateTypeDef(TypedDict):
    ExportArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListExportsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTablesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class S3DestinationTypeDef(TypedDict):
    S3Bucket: str
    S3OutputConfigurations: S3OutputConfigurationsTypeDef
    S3Prefix: str
    S3Region: str

class TableTypeDef(TypedDict):
    Description: NotRequired[str]
    TableName: NotRequired[str]
    TableProperties: NotRequired[List[TablePropertyDescriptionTypeDef]]

class ListExecutionsResponseTypeDef(TypedDict):
    Executions: List[ExecutionReferenceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListExportsResponseTypeDef(TypedDict):
    Exports: List[ExportReferenceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DestinationConfigurationsTypeDef(TypedDict):
    S3Destination: S3DestinationTypeDef

class ListTablesResponseTypeDef(TypedDict):
    Tables: List[TableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ExportOutputTypeDef(TypedDict):
    DataQuery: DataQueryOutputTypeDef
    DestinationConfigurations: DestinationConfigurationsTypeDef
    Name: str
    RefreshCadence: RefreshCadenceTypeDef
    Description: NotRequired[str]
    ExportArn: NotRequired[str]

class ExportTypeDef(TypedDict):
    DataQuery: DataQueryTypeDef
    DestinationConfigurations: DestinationConfigurationsTypeDef
    Name: str
    RefreshCadence: RefreshCadenceTypeDef
    Description: NotRequired[str]
    ExportArn: NotRequired[str]

class GetExecutionResponseTypeDef(TypedDict):
    ExecutionId: str
    ExecutionStatus: ExecutionStatusTypeDef
    Export: ExportOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetExportResponseTypeDef(TypedDict):
    Export: ExportOutputTypeDef
    ExportStatus: ExportStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

ExportUnionTypeDef = Union[ExportTypeDef, ExportOutputTypeDef]

class CreateExportRequestTypeDef(TypedDict):
    Export: ExportUnionTypeDef
    ResourceTags: NotRequired[Sequence[ResourceTagTypeDef]]

class UpdateExportRequestTypeDef(TypedDict):
    Export: ExportUnionTypeDef
    ExportArn: str
