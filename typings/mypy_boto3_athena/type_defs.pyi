"""
Main interface for athena service type definitions.

Usage::

    ```python
    from mypy_boto3_athena.type_defs import ColumnInfoTypeDef

    data: ColumnInfoTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ColumnInfoTypeDef",
    "ColumnTypeDef",
    "DataCatalogSummaryTypeDef",
    "DataCatalogTypeDef",
    "DatabaseTypeDef",
    "DatumTypeDef",
    "EncryptionConfigurationTypeDef",
    "NamedQueryTypeDef",
    "QueryExecutionContextTypeDef",
    "QueryExecutionStatisticsTypeDef",
    "QueryExecutionStatusTypeDef",
    "QueryExecutionTypeDef",
    "ResponseMetadata",
    "ResultConfigurationTypeDef",
    "ResultConfigurationUpdatesTypeDef",
    "ResultSetMetadataTypeDef",
    "ResultSetTypeDef",
    "RowTypeDef",
    "TableMetadataTypeDef",
    "TagTypeDef",
    "UnprocessedNamedQueryIdTypeDef",
    "UnprocessedQueryExecutionIdTypeDef",
    "WorkGroupConfigurationTypeDef",
    "WorkGroupSummaryTypeDef",
    "WorkGroupTypeDef",
    "BatchGetNamedQueryOutputTypeDef",
    "BatchGetQueryExecutionOutputTypeDef",
    "CreateNamedQueryOutputTypeDef",
    "GetDataCatalogOutputTypeDef",
    "GetDatabaseOutputTypeDef",
    "GetNamedQueryOutputTypeDef",
    "GetQueryExecutionOutputTypeDef",
    "GetQueryResultsOutputTypeDef",
    "GetTableMetadataOutputTypeDef",
    "GetWorkGroupOutputTypeDef",
    "ListDataCatalogsOutputTypeDef",
    "ListDatabasesOutputTypeDef",
    "ListNamedQueriesOutputTypeDef",
    "ListQueryExecutionsOutputTypeDef",
    "ListTableMetadataOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListWorkGroupsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "StartQueryExecutionOutputTypeDef",
    "WorkGroupConfigurationUpdatesTypeDef",
)

_RequiredColumnInfoTypeDef = TypedDict("_RequiredColumnInfoTypeDef", {"Name": str, "Type": str})
_OptionalColumnInfoTypeDef = TypedDict(
    "_OptionalColumnInfoTypeDef",
    {
        "CatalogName": str,
        "SchemaName": str,
        "TableName": str,
        "Label": str,
        "Precision": int,
        "Scale": int,
        "Nullable": Literal["NOT_NULL", "NULLABLE", "UNKNOWN"],
        "CaseSensitive": bool,
    },
    total=False,
)


class ColumnInfoTypeDef(_RequiredColumnInfoTypeDef, _OptionalColumnInfoTypeDef):
    pass


_RequiredColumnTypeDef = TypedDict("_RequiredColumnTypeDef", {"Name": str})
_OptionalColumnTypeDef = TypedDict(
    "_OptionalColumnTypeDef", {"Type": str, "Comment": str}, total=False
)


class ColumnTypeDef(_RequiredColumnTypeDef, _OptionalColumnTypeDef):
    pass


DataCatalogSummaryTypeDef = TypedDict(
    "DataCatalogSummaryTypeDef",
    {"CatalogName": str, "Type": Literal["LAMBDA", "GLUE", "HIVE"]},
    total=False,
)

_RequiredDataCatalogTypeDef = TypedDict(
    "_RequiredDataCatalogTypeDef", {"Name": str, "Type": Literal["LAMBDA", "GLUE", "HIVE"]}
)
_OptionalDataCatalogTypeDef = TypedDict(
    "_OptionalDataCatalogTypeDef", {"Description": str, "Parameters": Dict[str, str]}, total=False
)


class DataCatalogTypeDef(_RequiredDataCatalogTypeDef, _OptionalDataCatalogTypeDef):
    pass


_RequiredDatabaseTypeDef = TypedDict("_RequiredDatabaseTypeDef", {"Name": str})
_OptionalDatabaseTypeDef = TypedDict(
    "_OptionalDatabaseTypeDef", {"Description": str, "Parameters": Dict[str, str]}, total=False
)


class DatabaseTypeDef(_RequiredDatabaseTypeDef, _OptionalDatabaseTypeDef):
    pass


DatumTypeDef = TypedDict("DatumTypeDef", {"VarCharValue": str}, total=False)

_RequiredEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredEncryptionConfigurationTypeDef",
    {"EncryptionOption": Literal["SSE_S3", "SSE_KMS", "CSE_KMS"]},
)
_OptionalEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalEncryptionConfigurationTypeDef", {"KmsKey": str}, total=False
)


class EncryptionConfigurationTypeDef(
    _RequiredEncryptionConfigurationTypeDef, _OptionalEncryptionConfigurationTypeDef
):
    pass


_RequiredNamedQueryTypeDef = TypedDict(
    "_RequiredNamedQueryTypeDef", {"Name": str, "Database": str, "QueryString": str}
)
_OptionalNamedQueryTypeDef = TypedDict(
    "_OptionalNamedQueryTypeDef",
    {"Description": str, "NamedQueryId": str, "WorkGroup": str},
    total=False,
)


class NamedQueryTypeDef(_RequiredNamedQueryTypeDef, _OptionalNamedQueryTypeDef):
    pass


QueryExecutionContextTypeDef = TypedDict(
    "QueryExecutionContextTypeDef", {"Database": str, "Catalog": str}, total=False
)

QueryExecutionStatisticsTypeDef = TypedDict(
    "QueryExecutionStatisticsTypeDef",
    {
        "EngineExecutionTimeInMillis": int,
        "DataScannedInBytes": int,
        "DataManifestLocation": str,
        "TotalExecutionTimeInMillis": int,
        "QueryQueueTimeInMillis": int,
        "QueryPlanningTimeInMillis": int,
        "ServiceProcessingTimeInMillis": int,
    },
    total=False,
)

QueryExecutionStatusTypeDef = TypedDict(
    "QueryExecutionStatusTypeDef",
    {
        "State": Literal["QUEUED", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"],
        "StateChangeReason": str,
        "SubmissionDateTime": datetime,
        "CompletionDateTime": datetime,
    },
    total=False,
)

QueryExecutionTypeDef = TypedDict(
    "QueryExecutionTypeDef",
    {
        "QueryExecutionId": str,
        "Query": str,
        "StatementType": Literal["DDL", "DML", "UTILITY"],
        "ResultConfiguration": "ResultConfigurationTypeDef",
        "QueryExecutionContext": "QueryExecutionContextTypeDef",
        "Status": "QueryExecutionStatusTypeDef",
        "Statistics": "QueryExecutionStatisticsTypeDef",
        "WorkGroup": str,
    },
    total=False,
)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

ResultConfigurationTypeDef = TypedDict(
    "ResultConfigurationTypeDef",
    {"OutputLocation": str, "EncryptionConfiguration": "EncryptionConfigurationTypeDef"},
    total=False,
)

ResultConfigurationUpdatesTypeDef = TypedDict(
    "ResultConfigurationUpdatesTypeDef",
    {
        "OutputLocation": str,
        "RemoveOutputLocation": bool,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "RemoveEncryptionConfiguration": bool,
    },
    total=False,
)

ResultSetMetadataTypeDef = TypedDict(
    "ResultSetMetadataTypeDef", {"ColumnInfo": List["ColumnInfoTypeDef"]}, total=False
)

ResultSetTypeDef = TypedDict(
    "ResultSetTypeDef",
    {"Rows": List["RowTypeDef"], "ResultSetMetadata": "ResultSetMetadataTypeDef"},
    total=False,
)

RowTypeDef = TypedDict("RowTypeDef", {"Data": List["DatumTypeDef"]}, total=False)

_RequiredTableMetadataTypeDef = TypedDict("_RequiredTableMetadataTypeDef", {"Name": str})
_OptionalTableMetadataTypeDef = TypedDict(
    "_OptionalTableMetadataTypeDef",
    {
        "CreateTime": datetime,
        "LastAccessTime": datetime,
        "TableType": str,
        "Columns": List["ColumnTypeDef"],
        "PartitionKeys": List["ColumnTypeDef"],
        "Parameters": Dict[str, str],
    },
    total=False,
)


class TableMetadataTypeDef(_RequiredTableMetadataTypeDef, _OptionalTableMetadataTypeDef):
    pass


TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

UnprocessedNamedQueryIdTypeDef = TypedDict(
    "UnprocessedNamedQueryIdTypeDef",
    {"NamedQueryId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

UnprocessedQueryExecutionIdTypeDef = TypedDict(
    "UnprocessedQueryExecutionIdTypeDef",
    {"QueryExecutionId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

WorkGroupConfigurationTypeDef = TypedDict(
    "WorkGroupConfigurationTypeDef",
    {
        "ResultConfiguration": "ResultConfigurationTypeDef",
        "EnforceWorkGroupConfiguration": bool,
        "PublishCloudWatchMetricsEnabled": bool,
        "BytesScannedCutoffPerQuery": int,
        "RequesterPaysEnabled": bool,
    },
    total=False,
)

WorkGroupSummaryTypeDef = TypedDict(
    "WorkGroupSummaryTypeDef",
    {
        "Name": str,
        "State": Literal["ENABLED", "DISABLED"],
        "Description": str,
        "CreationTime": datetime,
    },
    total=False,
)

_RequiredWorkGroupTypeDef = TypedDict("_RequiredWorkGroupTypeDef", {"Name": str})
_OptionalWorkGroupTypeDef = TypedDict(
    "_OptionalWorkGroupTypeDef",
    {
        "State": Literal["ENABLED", "DISABLED"],
        "Configuration": "WorkGroupConfigurationTypeDef",
        "Description": str,
        "CreationTime": datetime,
    },
    total=False,
)


class WorkGroupTypeDef(_RequiredWorkGroupTypeDef, _OptionalWorkGroupTypeDef):
    pass


BatchGetNamedQueryOutputTypeDef = TypedDict(
    "BatchGetNamedQueryOutputTypeDef",
    {
        "NamedQueries": List["NamedQueryTypeDef"],
        "UnprocessedNamedQueryIds": List["UnprocessedNamedQueryIdTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

BatchGetQueryExecutionOutputTypeDef = TypedDict(
    "BatchGetQueryExecutionOutputTypeDef",
    {
        "QueryExecutions": List["QueryExecutionTypeDef"],
        "UnprocessedQueryExecutionIds": List["UnprocessedQueryExecutionIdTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

CreateNamedQueryOutputTypeDef = TypedDict(
    "CreateNamedQueryOutputTypeDef",
    {"NamedQueryId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetDataCatalogOutputTypeDef = TypedDict(
    "GetDataCatalogOutputTypeDef",
    {"DataCatalog": "DataCatalogTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetDatabaseOutputTypeDef = TypedDict(
    "GetDatabaseOutputTypeDef",
    {"Database": "DatabaseTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetNamedQueryOutputTypeDef = TypedDict(
    "GetNamedQueryOutputTypeDef",
    {"NamedQuery": "NamedQueryTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetQueryExecutionOutputTypeDef = TypedDict(
    "GetQueryExecutionOutputTypeDef",
    {"QueryExecution": "QueryExecutionTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetQueryResultsOutputTypeDef = TypedDict(
    "GetQueryResultsOutputTypeDef",
    {
        "UpdateCount": int,
        "ResultSet": "ResultSetTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetTableMetadataOutputTypeDef = TypedDict(
    "GetTableMetadataOutputTypeDef",
    {"TableMetadata": "TableMetadataTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetWorkGroupOutputTypeDef = TypedDict(
    "GetWorkGroupOutputTypeDef",
    {"WorkGroup": "WorkGroupTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListDataCatalogsOutputTypeDef = TypedDict(
    "ListDataCatalogsOutputTypeDef",
    {
        "DataCatalogsSummary": List["DataCatalogSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListDatabasesOutputTypeDef = TypedDict(
    "ListDatabasesOutputTypeDef",
    {
        "DatabaseList": List["DatabaseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListNamedQueriesOutputTypeDef = TypedDict(
    "ListNamedQueriesOutputTypeDef",
    {"NamedQueryIds": List[str], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListQueryExecutionsOutputTypeDef = TypedDict(
    "ListQueryExecutionsOutputTypeDef",
    {"QueryExecutionIds": List[str], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListTableMetadataOutputTypeDef = TypedDict(
    "ListTableMetadataOutputTypeDef",
    {
        "TableMetadataList": List["TableMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {"Tags": List["TagTypeDef"], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListWorkGroupsOutputTypeDef = TypedDict(
    "ListWorkGroupsOutputTypeDef",
    {
        "WorkGroups": List["WorkGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

StartQueryExecutionOutputTypeDef = TypedDict(
    "StartQueryExecutionOutputTypeDef",
    {"QueryExecutionId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

WorkGroupConfigurationUpdatesTypeDef = TypedDict(
    "WorkGroupConfigurationUpdatesTypeDef",
    {
        "EnforceWorkGroupConfiguration": bool,
        "ResultConfigurationUpdates": "ResultConfigurationUpdatesTypeDef",
        "PublishCloudWatchMetricsEnabled": bool,
        "BytesScannedCutoffPerQuery": int,
        "RemoveBytesScannedCutoffPerQuery": bool,
        "RequesterPaysEnabled": bool,
    },
    total=False,
)
