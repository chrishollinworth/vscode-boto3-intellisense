"""
Type annotations for bcm-data-exports service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/type_defs.html)

Usage::

    ```python
    from mypy_boto3_bcm_data_exports.type_defs import ColumnTypeDef

    data: ColumnTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    CompressionOptionType,
    ExecutionStatusCodeType,
    ExecutionStatusReasonType,
    ExportStatusCodeType,
    FormatOptionType,
    OverwriteOptionType,
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
    "ColumnTypeDef",
    "CreateExportRequestRequestTypeDef",
    "CreateExportResponseTypeDef",
    "DataQueryTypeDef",
    "DeleteExportRequestRequestTypeDef",
    "DeleteExportResponseTypeDef",
    "DestinationConfigurationsTypeDef",
    "ExecutionReferenceTypeDef",
    "ExecutionStatusTypeDef",
    "ExportReferenceTypeDef",
    "ExportStatusTypeDef",
    "ExportTypeDef",
    "GetExecutionRequestRequestTypeDef",
    "GetExecutionResponseTypeDef",
    "GetExportRequestRequestTypeDef",
    "GetExportResponseTypeDef",
    "GetTableRequestRequestTypeDef",
    "GetTableResponseTypeDef",
    "ListExecutionsRequestRequestTypeDef",
    "ListExecutionsResponseTypeDef",
    "ListExportsRequestRequestTypeDef",
    "ListExportsResponseTypeDef",
    "ListTablesRequestRequestTypeDef",
    "ListTablesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RefreshCadenceTypeDef",
    "ResourceTagTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationTypeDef",
    "S3OutputConfigurationsTypeDef",
    "TablePropertyDescriptionTypeDef",
    "TableTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateExportRequestRequestTypeDef",
    "UpdateExportResponseTypeDef",
)

ColumnTypeDef = TypedDict(
    "ColumnTypeDef",
    {
        "Description": str,
        "Name": str,
        "Type": str,
    },
    total=False,
)

_RequiredCreateExportRequestRequestTypeDef = TypedDict(
    "_RequiredCreateExportRequestRequestTypeDef",
    {
        "Export": "ExportTypeDef",
    },
)
_OptionalCreateExportRequestRequestTypeDef = TypedDict(
    "_OptionalCreateExportRequestRequestTypeDef",
    {
        "ResourceTags": List["ResourceTagTypeDef"],
    },
    total=False,
)

class CreateExportRequestRequestTypeDef(
    _RequiredCreateExportRequestRequestTypeDef, _OptionalCreateExportRequestRequestTypeDef
):
    pass

CreateExportResponseTypeDef = TypedDict(
    "CreateExportResponseTypeDef",
    {
        "ExportArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDataQueryTypeDef = TypedDict(
    "_RequiredDataQueryTypeDef",
    {
        "QueryStatement": str,
    },
)
_OptionalDataQueryTypeDef = TypedDict(
    "_OptionalDataQueryTypeDef",
    {
        "TableConfigurations": Dict[str, Dict[str, str]],
    },
    total=False,
)

class DataQueryTypeDef(_RequiredDataQueryTypeDef, _OptionalDataQueryTypeDef):
    pass

DeleteExportRequestRequestTypeDef = TypedDict(
    "DeleteExportRequestRequestTypeDef",
    {
        "ExportArn": str,
    },
)

DeleteExportResponseTypeDef = TypedDict(
    "DeleteExportResponseTypeDef",
    {
        "ExportArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationConfigurationsTypeDef = TypedDict(
    "DestinationConfigurationsTypeDef",
    {
        "S3Destination": "S3DestinationTypeDef",
    },
)

ExecutionReferenceTypeDef = TypedDict(
    "ExecutionReferenceTypeDef",
    {
        "ExecutionId": str,
        "ExecutionStatus": "ExecutionStatusTypeDef",
    },
)

ExecutionStatusTypeDef = TypedDict(
    "ExecutionStatusTypeDef",
    {
        "CompletedAt": datetime,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "StatusCode": ExecutionStatusCodeType,
        "StatusReason": ExecutionStatusReasonType,
    },
    total=False,
)

ExportReferenceTypeDef = TypedDict(
    "ExportReferenceTypeDef",
    {
        "ExportArn": str,
        "ExportName": str,
        "ExportStatus": "ExportStatusTypeDef",
    },
)

ExportStatusTypeDef = TypedDict(
    "ExportStatusTypeDef",
    {
        "CreatedAt": datetime,
        "LastRefreshedAt": datetime,
        "LastUpdatedAt": datetime,
        "StatusCode": ExportStatusCodeType,
        "StatusReason": ExecutionStatusReasonType,
    },
    total=False,
)

_RequiredExportTypeDef = TypedDict(
    "_RequiredExportTypeDef",
    {
        "DataQuery": "DataQueryTypeDef",
        "DestinationConfigurations": "DestinationConfigurationsTypeDef",
        "Name": str,
        "RefreshCadence": "RefreshCadenceTypeDef",
    },
)
_OptionalExportTypeDef = TypedDict(
    "_OptionalExportTypeDef",
    {
        "Description": str,
        "ExportArn": str,
    },
    total=False,
)

class ExportTypeDef(_RequiredExportTypeDef, _OptionalExportTypeDef):
    pass

GetExecutionRequestRequestTypeDef = TypedDict(
    "GetExecutionRequestRequestTypeDef",
    {
        "ExecutionId": str,
        "ExportArn": str,
    },
)

GetExecutionResponseTypeDef = TypedDict(
    "GetExecutionResponseTypeDef",
    {
        "ExecutionId": str,
        "ExecutionStatus": "ExecutionStatusTypeDef",
        "Export": "ExportTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExportRequestRequestTypeDef = TypedDict(
    "GetExportRequestRequestTypeDef",
    {
        "ExportArn": str,
    },
)

GetExportResponseTypeDef = TypedDict(
    "GetExportResponseTypeDef",
    {
        "Export": "ExportTypeDef",
        "ExportStatus": "ExportStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTableRequestRequestTypeDef = TypedDict(
    "_RequiredGetTableRequestRequestTypeDef",
    {
        "TableName": str,
    },
)
_OptionalGetTableRequestRequestTypeDef = TypedDict(
    "_OptionalGetTableRequestRequestTypeDef",
    {
        "TableProperties": Dict[str, str],
    },
    total=False,
)

class GetTableRequestRequestTypeDef(
    _RequiredGetTableRequestRequestTypeDef, _OptionalGetTableRequestRequestTypeDef
):
    pass

GetTableResponseTypeDef = TypedDict(
    "GetTableResponseTypeDef",
    {
        "Description": str,
        "Schema": List["ColumnTypeDef"],
        "TableName": str,
        "TableProperties": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredListExecutionsRequestRequestTypeDef",
    {
        "ExportArn": str,
    },
)
_OptionalListExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalListExecutionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListExecutionsRequestRequestTypeDef(
    _RequiredListExecutionsRequestRequestTypeDef, _OptionalListExecutionsRequestRequestTypeDef
):
    pass

ListExecutionsResponseTypeDef = TypedDict(
    "ListExecutionsResponseTypeDef",
    {
        "Executions": List["ExecutionReferenceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExportsRequestRequestTypeDef = TypedDict(
    "ListExportsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListExportsResponseTypeDef = TypedDict(
    "ListExportsResponseTypeDef",
    {
        "Exports": List["ExportReferenceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTablesRequestRequestTypeDef = TypedDict(
    "ListTablesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListTablesResponseTypeDef = TypedDict(
    "ListTablesResponseTypeDef",
    {
        "NextToken": str,
        "Tables": List["TableTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "NextToken": str,
        "ResourceTags": List["ResourceTagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

RefreshCadenceTypeDef = TypedDict(
    "RefreshCadenceTypeDef",
    {
        "Frequency": Literal["SYNCHRONOUS"],
    },
)

ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef",
    {
        "Key": str,
        "Value": str,
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

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "S3Bucket": str,
        "S3OutputConfigurations": "S3OutputConfigurationsTypeDef",
        "S3Prefix": str,
        "S3Region": str,
    },
)

S3OutputConfigurationsTypeDef = TypedDict(
    "S3OutputConfigurationsTypeDef",
    {
        "Compression": CompressionOptionType,
        "Format": FormatOptionType,
        "OutputType": Literal["CUSTOM"],
        "Overwrite": OverwriteOptionType,
    },
)

TablePropertyDescriptionTypeDef = TypedDict(
    "TablePropertyDescriptionTypeDef",
    {
        "DefaultValue": str,
        "Description": str,
        "Name": str,
        "ValidValues": List[str],
    },
    total=False,
)

TableTypeDef = TypedDict(
    "TableTypeDef",
    {
        "Description": str,
        "TableName": str,
        "TableProperties": List["TablePropertyDescriptionTypeDef"],
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "ResourceTags": List["ResourceTagTypeDef"],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "ResourceTagKeys": List[str],
    },
)

UpdateExportRequestRequestTypeDef = TypedDict(
    "UpdateExportRequestRequestTypeDef",
    {
        "Export": "ExportTypeDef",
        "ExportArn": str,
    },
)

UpdateExportResponseTypeDef = TypedDict(
    "UpdateExportResponseTypeDef",
    {
        "ExportArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
