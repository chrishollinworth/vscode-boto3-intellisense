"""
Type annotations for athena service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/type_defs.html)

Usage::

    ```python
    from mypy_boto3_athena.type_defs import BatchGetNamedQueryInputRequestTypeDef

    data: BatchGetNamedQueryInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ColumnNullableType,
    DataCatalogTypeType,
    EncryptionOptionType,
    QueryExecutionStateType,
    StatementTypeType,
    WorkGroupStateType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BatchGetNamedQueryInputRequestTypeDef",
    "BatchGetNamedQueryOutputTypeDef",
    "BatchGetQueryExecutionInputRequestTypeDef",
    "BatchGetQueryExecutionOutputTypeDef",
    "ColumnInfoTypeDef",
    "ColumnTypeDef",
    "CreateDataCatalogInputRequestTypeDef",
    "CreateNamedQueryInputRequestTypeDef",
    "CreateNamedQueryOutputTypeDef",
    "CreatePreparedStatementInputRequestTypeDef",
    "CreateWorkGroupInputRequestTypeDef",
    "DataCatalogSummaryTypeDef",
    "DataCatalogTypeDef",
    "DatabaseTypeDef",
    "DatumTypeDef",
    "DeleteDataCatalogInputRequestTypeDef",
    "DeleteNamedQueryInputRequestTypeDef",
    "DeletePreparedStatementInputRequestTypeDef",
    "DeleteWorkGroupInputRequestTypeDef",
    "EncryptionConfigurationTypeDef",
    "EngineVersionTypeDef",
    "GetDataCatalogInputRequestTypeDef",
    "GetDataCatalogOutputTypeDef",
    "GetDatabaseInputRequestTypeDef",
    "GetDatabaseOutputTypeDef",
    "GetNamedQueryInputRequestTypeDef",
    "GetNamedQueryOutputTypeDef",
    "GetPreparedStatementInputRequestTypeDef",
    "GetPreparedStatementOutputTypeDef",
    "GetQueryExecutionInputRequestTypeDef",
    "GetQueryExecutionOutputTypeDef",
    "GetQueryResultsInputRequestTypeDef",
    "GetQueryResultsOutputTypeDef",
    "GetTableMetadataInputRequestTypeDef",
    "GetTableMetadataOutputTypeDef",
    "GetWorkGroupInputRequestTypeDef",
    "GetWorkGroupOutputTypeDef",
    "ListDataCatalogsInputRequestTypeDef",
    "ListDataCatalogsOutputTypeDef",
    "ListDatabasesInputRequestTypeDef",
    "ListDatabasesOutputTypeDef",
    "ListEngineVersionsInputRequestTypeDef",
    "ListEngineVersionsOutputTypeDef",
    "ListNamedQueriesInputRequestTypeDef",
    "ListNamedQueriesOutputTypeDef",
    "ListPreparedStatementsInputRequestTypeDef",
    "ListPreparedStatementsOutputTypeDef",
    "ListQueryExecutionsInputRequestTypeDef",
    "ListQueryExecutionsOutputTypeDef",
    "ListTableMetadataInputRequestTypeDef",
    "ListTableMetadataOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListWorkGroupsInputRequestTypeDef",
    "ListWorkGroupsOutputTypeDef",
    "NamedQueryTypeDef",
    "PaginatorConfigTypeDef",
    "PreparedStatementSummaryTypeDef",
    "PreparedStatementTypeDef",
    "QueryExecutionContextTypeDef",
    "QueryExecutionStatisticsTypeDef",
    "QueryExecutionStatusTypeDef",
    "QueryExecutionTypeDef",
    "ResponseMetadataTypeDef",
    "ResultConfigurationTypeDef",
    "ResultConfigurationUpdatesTypeDef",
    "ResultSetMetadataTypeDef",
    "ResultSetTypeDef",
    "RowTypeDef",
    "StartQueryExecutionInputRequestTypeDef",
    "StartQueryExecutionOutputTypeDef",
    "StopQueryExecutionInputRequestTypeDef",
    "TableMetadataTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "UnprocessedNamedQueryIdTypeDef",
    "UnprocessedQueryExecutionIdTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateDataCatalogInputRequestTypeDef",
    "UpdatePreparedStatementInputRequestTypeDef",
    "UpdateWorkGroupInputRequestTypeDef",
    "WorkGroupConfigurationTypeDef",
    "WorkGroupConfigurationUpdatesTypeDef",
    "WorkGroupSummaryTypeDef",
    "WorkGroupTypeDef",
)

BatchGetNamedQueryInputRequestTypeDef = TypedDict(
    "BatchGetNamedQueryInputRequestTypeDef",
    {
        "NamedQueryIds": List[str],
    },
)

BatchGetNamedQueryOutputTypeDef = TypedDict(
    "BatchGetNamedQueryOutputTypeDef",
    {
        "NamedQueries": List["NamedQueryTypeDef"],
        "UnprocessedNamedQueryIds": List["UnprocessedNamedQueryIdTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetQueryExecutionInputRequestTypeDef = TypedDict(
    "BatchGetQueryExecutionInputRequestTypeDef",
    {
        "QueryExecutionIds": List[str],
    },
)

BatchGetQueryExecutionOutputTypeDef = TypedDict(
    "BatchGetQueryExecutionOutputTypeDef",
    {
        "QueryExecutions": List["QueryExecutionTypeDef"],
        "UnprocessedQueryExecutionIds": List["UnprocessedQueryExecutionIdTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredColumnInfoTypeDef = TypedDict(
    "_RequiredColumnInfoTypeDef",
    {
        "Name": str,
        "Type": str,
    },
)
_OptionalColumnInfoTypeDef = TypedDict(
    "_OptionalColumnInfoTypeDef",
    {
        "CatalogName": str,
        "SchemaName": str,
        "TableName": str,
        "Label": str,
        "Precision": int,
        "Scale": int,
        "Nullable": ColumnNullableType,
        "CaseSensitive": bool,
    },
    total=False,
)

class ColumnInfoTypeDef(_RequiredColumnInfoTypeDef, _OptionalColumnInfoTypeDef):
    pass

_RequiredColumnTypeDef = TypedDict(
    "_RequiredColumnTypeDef",
    {
        "Name": str,
    },
)
_OptionalColumnTypeDef = TypedDict(
    "_OptionalColumnTypeDef",
    {
        "Type": str,
        "Comment": str,
    },
    total=False,
)

class ColumnTypeDef(_RequiredColumnTypeDef, _OptionalColumnTypeDef):
    pass

_RequiredCreateDataCatalogInputRequestTypeDef = TypedDict(
    "_RequiredCreateDataCatalogInputRequestTypeDef",
    {
        "Name": str,
        "Type": DataCatalogTypeType,
    },
)
_OptionalCreateDataCatalogInputRequestTypeDef = TypedDict(
    "_OptionalCreateDataCatalogInputRequestTypeDef",
    {
        "Description": str,
        "Parameters": Dict[str, str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDataCatalogInputRequestTypeDef(
    _RequiredCreateDataCatalogInputRequestTypeDef, _OptionalCreateDataCatalogInputRequestTypeDef
):
    pass

_RequiredCreateNamedQueryInputRequestTypeDef = TypedDict(
    "_RequiredCreateNamedQueryInputRequestTypeDef",
    {
        "Name": str,
        "Database": str,
        "QueryString": str,
    },
)
_OptionalCreateNamedQueryInputRequestTypeDef = TypedDict(
    "_OptionalCreateNamedQueryInputRequestTypeDef",
    {
        "Description": str,
        "ClientRequestToken": str,
        "WorkGroup": str,
    },
    total=False,
)

class CreateNamedQueryInputRequestTypeDef(
    _RequiredCreateNamedQueryInputRequestTypeDef, _OptionalCreateNamedQueryInputRequestTypeDef
):
    pass

CreateNamedQueryOutputTypeDef = TypedDict(
    "CreateNamedQueryOutputTypeDef",
    {
        "NamedQueryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePreparedStatementInputRequestTypeDef = TypedDict(
    "_RequiredCreatePreparedStatementInputRequestTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
        "QueryStatement": str,
    },
)
_OptionalCreatePreparedStatementInputRequestTypeDef = TypedDict(
    "_OptionalCreatePreparedStatementInputRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class CreatePreparedStatementInputRequestTypeDef(
    _RequiredCreatePreparedStatementInputRequestTypeDef,
    _OptionalCreatePreparedStatementInputRequestTypeDef,
):
    pass

_RequiredCreateWorkGroupInputRequestTypeDef = TypedDict(
    "_RequiredCreateWorkGroupInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateWorkGroupInputRequestTypeDef = TypedDict(
    "_OptionalCreateWorkGroupInputRequestTypeDef",
    {
        "Configuration": "WorkGroupConfigurationTypeDef",
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateWorkGroupInputRequestTypeDef(
    _RequiredCreateWorkGroupInputRequestTypeDef, _OptionalCreateWorkGroupInputRequestTypeDef
):
    pass

DataCatalogSummaryTypeDef = TypedDict(
    "DataCatalogSummaryTypeDef",
    {
        "CatalogName": str,
        "Type": DataCatalogTypeType,
    },
    total=False,
)

_RequiredDataCatalogTypeDef = TypedDict(
    "_RequiredDataCatalogTypeDef",
    {
        "Name": str,
        "Type": DataCatalogTypeType,
    },
)
_OptionalDataCatalogTypeDef = TypedDict(
    "_OptionalDataCatalogTypeDef",
    {
        "Description": str,
        "Parameters": Dict[str, str],
    },
    total=False,
)

class DataCatalogTypeDef(_RequiredDataCatalogTypeDef, _OptionalDataCatalogTypeDef):
    pass

_RequiredDatabaseTypeDef = TypedDict(
    "_RequiredDatabaseTypeDef",
    {
        "Name": str,
    },
)
_OptionalDatabaseTypeDef = TypedDict(
    "_OptionalDatabaseTypeDef",
    {
        "Description": str,
        "Parameters": Dict[str, str],
    },
    total=False,
)

class DatabaseTypeDef(_RequiredDatabaseTypeDef, _OptionalDatabaseTypeDef):
    pass

DatumTypeDef = TypedDict(
    "DatumTypeDef",
    {
        "VarCharValue": str,
    },
    total=False,
)

DeleteDataCatalogInputRequestTypeDef = TypedDict(
    "DeleteDataCatalogInputRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteNamedQueryInputRequestTypeDef = TypedDict(
    "DeleteNamedQueryInputRequestTypeDef",
    {
        "NamedQueryId": str,
    },
)

DeletePreparedStatementInputRequestTypeDef = TypedDict(
    "DeletePreparedStatementInputRequestTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
    },
)

_RequiredDeleteWorkGroupInputRequestTypeDef = TypedDict(
    "_RequiredDeleteWorkGroupInputRequestTypeDef",
    {
        "WorkGroup": str,
    },
)
_OptionalDeleteWorkGroupInputRequestTypeDef = TypedDict(
    "_OptionalDeleteWorkGroupInputRequestTypeDef",
    {
        "RecursiveDeleteOption": bool,
    },
    total=False,
)

class DeleteWorkGroupInputRequestTypeDef(
    _RequiredDeleteWorkGroupInputRequestTypeDef, _OptionalDeleteWorkGroupInputRequestTypeDef
):
    pass

_RequiredEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredEncryptionConfigurationTypeDef",
    {
        "EncryptionOption": EncryptionOptionType,
    },
)
_OptionalEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalEncryptionConfigurationTypeDef",
    {
        "KmsKey": str,
    },
    total=False,
)

class EncryptionConfigurationTypeDef(
    _RequiredEncryptionConfigurationTypeDef, _OptionalEncryptionConfigurationTypeDef
):
    pass

EngineVersionTypeDef = TypedDict(
    "EngineVersionTypeDef",
    {
        "SelectedEngineVersion": str,
        "EffectiveEngineVersion": str,
    },
    total=False,
)

GetDataCatalogInputRequestTypeDef = TypedDict(
    "GetDataCatalogInputRequestTypeDef",
    {
        "Name": str,
    },
)

GetDataCatalogOutputTypeDef = TypedDict(
    "GetDataCatalogOutputTypeDef",
    {
        "DataCatalog": "DataCatalogTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDatabaseInputRequestTypeDef = TypedDict(
    "GetDatabaseInputRequestTypeDef",
    {
        "CatalogName": str,
        "DatabaseName": str,
    },
)

GetDatabaseOutputTypeDef = TypedDict(
    "GetDatabaseOutputTypeDef",
    {
        "Database": "DatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNamedQueryInputRequestTypeDef = TypedDict(
    "GetNamedQueryInputRequestTypeDef",
    {
        "NamedQueryId": str,
    },
)

GetNamedQueryOutputTypeDef = TypedDict(
    "GetNamedQueryOutputTypeDef",
    {
        "NamedQuery": "NamedQueryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPreparedStatementInputRequestTypeDef = TypedDict(
    "GetPreparedStatementInputRequestTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
    },
)

GetPreparedStatementOutputTypeDef = TypedDict(
    "GetPreparedStatementOutputTypeDef",
    {
        "PreparedStatement": "PreparedStatementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryExecutionInputRequestTypeDef = TypedDict(
    "GetQueryExecutionInputRequestTypeDef",
    {
        "QueryExecutionId": str,
    },
)

GetQueryExecutionOutputTypeDef = TypedDict(
    "GetQueryExecutionOutputTypeDef",
    {
        "QueryExecution": "QueryExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetQueryResultsInputRequestTypeDef = TypedDict(
    "_RequiredGetQueryResultsInputRequestTypeDef",
    {
        "QueryExecutionId": str,
    },
)
_OptionalGetQueryResultsInputRequestTypeDef = TypedDict(
    "_OptionalGetQueryResultsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetQueryResultsInputRequestTypeDef(
    _RequiredGetQueryResultsInputRequestTypeDef, _OptionalGetQueryResultsInputRequestTypeDef
):
    pass

GetQueryResultsOutputTypeDef = TypedDict(
    "GetQueryResultsOutputTypeDef",
    {
        "UpdateCount": int,
        "ResultSet": "ResultSetTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTableMetadataInputRequestTypeDef = TypedDict(
    "GetTableMetadataInputRequestTypeDef",
    {
        "CatalogName": str,
        "DatabaseName": str,
        "TableName": str,
    },
)

GetTableMetadataOutputTypeDef = TypedDict(
    "GetTableMetadataOutputTypeDef",
    {
        "TableMetadata": "TableMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkGroupInputRequestTypeDef = TypedDict(
    "GetWorkGroupInputRequestTypeDef",
    {
        "WorkGroup": str,
    },
)

GetWorkGroupOutputTypeDef = TypedDict(
    "GetWorkGroupOutputTypeDef",
    {
        "WorkGroup": "WorkGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataCatalogsInputRequestTypeDef = TypedDict(
    "ListDataCatalogsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDataCatalogsOutputTypeDef = TypedDict(
    "ListDataCatalogsOutputTypeDef",
    {
        "DataCatalogsSummary": List["DataCatalogSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDatabasesInputRequestTypeDef = TypedDict(
    "_RequiredListDatabasesInputRequestTypeDef",
    {
        "CatalogName": str,
    },
)
_OptionalListDatabasesInputRequestTypeDef = TypedDict(
    "_OptionalListDatabasesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListDatabasesInputRequestTypeDef(
    _RequiredListDatabasesInputRequestTypeDef, _OptionalListDatabasesInputRequestTypeDef
):
    pass

ListDatabasesOutputTypeDef = TypedDict(
    "ListDatabasesOutputTypeDef",
    {
        "DatabaseList": List["DatabaseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEngineVersionsInputRequestTypeDef = TypedDict(
    "ListEngineVersionsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEngineVersionsOutputTypeDef = TypedDict(
    "ListEngineVersionsOutputTypeDef",
    {
        "EngineVersions": List["EngineVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNamedQueriesInputRequestTypeDef = TypedDict(
    "ListNamedQueriesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "WorkGroup": str,
    },
    total=False,
)

ListNamedQueriesOutputTypeDef = TypedDict(
    "ListNamedQueriesOutputTypeDef",
    {
        "NamedQueryIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPreparedStatementsInputRequestTypeDef = TypedDict(
    "_RequiredListPreparedStatementsInputRequestTypeDef",
    {
        "WorkGroup": str,
    },
)
_OptionalListPreparedStatementsInputRequestTypeDef = TypedDict(
    "_OptionalListPreparedStatementsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListPreparedStatementsInputRequestTypeDef(
    _RequiredListPreparedStatementsInputRequestTypeDef,
    _OptionalListPreparedStatementsInputRequestTypeDef,
):
    pass

ListPreparedStatementsOutputTypeDef = TypedDict(
    "ListPreparedStatementsOutputTypeDef",
    {
        "PreparedStatements": List["PreparedStatementSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQueryExecutionsInputRequestTypeDef = TypedDict(
    "ListQueryExecutionsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "WorkGroup": str,
    },
    total=False,
)

ListQueryExecutionsOutputTypeDef = TypedDict(
    "ListQueryExecutionsOutputTypeDef",
    {
        "QueryExecutionIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTableMetadataInputRequestTypeDef = TypedDict(
    "_RequiredListTableMetadataInputRequestTypeDef",
    {
        "CatalogName": str,
        "DatabaseName": str,
    },
)
_OptionalListTableMetadataInputRequestTypeDef = TypedDict(
    "_OptionalListTableMetadataInputRequestTypeDef",
    {
        "Expression": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListTableMetadataInputRequestTypeDef(
    _RequiredListTableMetadataInputRequestTypeDef, _OptionalListTableMetadataInputRequestTypeDef
):
    pass

ListTableMetadataOutputTypeDef = TypedDict(
    "ListTableMetadataOutputTypeDef",
    {
        "TableMetadataList": List["TableMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceInputRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalListTagsForResourceInputRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListTagsForResourceInputRequestTypeDef(
    _RequiredListTagsForResourceInputRequestTypeDef, _OptionalListTagsForResourceInputRequestTypeDef
):
    pass

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkGroupsInputRequestTypeDef = TypedDict(
    "ListWorkGroupsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListWorkGroupsOutputTypeDef = TypedDict(
    "ListWorkGroupsOutputTypeDef",
    {
        "WorkGroups": List["WorkGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredNamedQueryTypeDef = TypedDict(
    "_RequiredNamedQueryTypeDef",
    {
        "Name": str,
        "Database": str,
        "QueryString": str,
    },
)
_OptionalNamedQueryTypeDef = TypedDict(
    "_OptionalNamedQueryTypeDef",
    {
        "Description": str,
        "NamedQueryId": str,
        "WorkGroup": str,
    },
    total=False,
)

class NamedQueryTypeDef(_RequiredNamedQueryTypeDef, _OptionalNamedQueryTypeDef):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PreparedStatementSummaryTypeDef = TypedDict(
    "PreparedStatementSummaryTypeDef",
    {
        "StatementName": str,
        "LastModifiedTime": datetime,
    },
    total=False,
)

PreparedStatementTypeDef = TypedDict(
    "PreparedStatementTypeDef",
    {
        "StatementName": str,
        "QueryStatement": str,
        "WorkGroupName": str,
        "Description": str,
        "LastModifiedTime": datetime,
    },
    total=False,
)

QueryExecutionContextTypeDef = TypedDict(
    "QueryExecutionContextTypeDef",
    {
        "Database": str,
        "Catalog": str,
    },
    total=False,
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
        "State": QueryExecutionStateType,
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
        "StatementType": StatementTypeType,
        "ResultConfiguration": "ResultConfigurationTypeDef",
        "QueryExecutionContext": "QueryExecutionContextTypeDef",
        "Status": "QueryExecutionStatusTypeDef",
        "Statistics": "QueryExecutionStatisticsTypeDef",
        "WorkGroup": str,
        "EngineVersion": "EngineVersionTypeDef",
    },
    total=False,
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

ResultConfigurationTypeDef = TypedDict(
    "ResultConfigurationTypeDef",
    {
        "OutputLocation": str,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
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
    "ResultSetMetadataTypeDef",
    {
        "ColumnInfo": List["ColumnInfoTypeDef"],
    },
    total=False,
)

ResultSetTypeDef = TypedDict(
    "ResultSetTypeDef",
    {
        "Rows": List["RowTypeDef"],
        "ResultSetMetadata": "ResultSetMetadataTypeDef",
    },
    total=False,
)

RowTypeDef = TypedDict(
    "RowTypeDef",
    {
        "Data": List["DatumTypeDef"],
    },
    total=False,
)

_RequiredStartQueryExecutionInputRequestTypeDef = TypedDict(
    "_RequiredStartQueryExecutionInputRequestTypeDef",
    {
        "QueryString": str,
    },
)
_OptionalStartQueryExecutionInputRequestTypeDef = TypedDict(
    "_OptionalStartQueryExecutionInputRequestTypeDef",
    {
        "ClientRequestToken": str,
        "QueryExecutionContext": "QueryExecutionContextTypeDef",
        "ResultConfiguration": "ResultConfigurationTypeDef",
        "WorkGroup": str,
    },
    total=False,
)

class StartQueryExecutionInputRequestTypeDef(
    _RequiredStartQueryExecutionInputRequestTypeDef, _OptionalStartQueryExecutionInputRequestTypeDef
):
    pass

StartQueryExecutionOutputTypeDef = TypedDict(
    "StartQueryExecutionOutputTypeDef",
    {
        "QueryExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopQueryExecutionInputRequestTypeDef = TypedDict(
    "StopQueryExecutionInputRequestTypeDef",
    {
        "QueryExecutionId": str,
    },
)

_RequiredTableMetadataTypeDef = TypedDict(
    "_RequiredTableMetadataTypeDef",
    {
        "Name": str,
    },
)
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

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

UnprocessedNamedQueryIdTypeDef = TypedDict(
    "UnprocessedNamedQueryIdTypeDef",
    {
        "NamedQueryId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

UnprocessedQueryExecutionIdTypeDef = TypedDict(
    "UnprocessedQueryExecutionIdTypeDef",
    {
        "QueryExecutionId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateDataCatalogInputRequestTypeDef = TypedDict(
    "_RequiredUpdateDataCatalogInputRequestTypeDef",
    {
        "Name": str,
        "Type": DataCatalogTypeType,
    },
)
_OptionalUpdateDataCatalogInputRequestTypeDef = TypedDict(
    "_OptionalUpdateDataCatalogInputRequestTypeDef",
    {
        "Description": str,
        "Parameters": Dict[str, str],
    },
    total=False,
)

class UpdateDataCatalogInputRequestTypeDef(
    _RequiredUpdateDataCatalogInputRequestTypeDef, _OptionalUpdateDataCatalogInputRequestTypeDef
):
    pass

_RequiredUpdatePreparedStatementInputRequestTypeDef = TypedDict(
    "_RequiredUpdatePreparedStatementInputRequestTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
        "QueryStatement": str,
    },
)
_OptionalUpdatePreparedStatementInputRequestTypeDef = TypedDict(
    "_OptionalUpdatePreparedStatementInputRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdatePreparedStatementInputRequestTypeDef(
    _RequiredUpdatePreparedStatementInputRequestTypeDef,
    _OptionalUpdatePreparedStatementInputRequestTypeDef,
):
    pass

_RequiredUpdateWorkGroupInputRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkGroupInputRequestTypeDef",
    {
        "WorkGroup": str,
    },
)
_OptionalUpdateWorkGroupInputRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkGroupInputRequestTypeDef",
    {
        "Description": str,
        "ConfigurationUpdates": "WorkGroupConfigurationUpdatesTypeDef",
        "State": WorkGroupStateType,
    },
    total=False,
)

class UpdateWorkGroupInputRequestTypeDef(
    _RequiredUpdateWorkGroupInputRequestTypeDef, _OptionalUpdateWorkGroupInputRequestTypeDef
):
    pass

WorkGroupConfigurationTypeDef = TypedDict(
    "WorkGroupConfigurationTypeDef",
    {
        "ResultConfiguration": "ResultConfigurationTypeDef",
        "EnforceWorkGroupConfiguration": bool,
        "PublishCloudWatchMetricsEnabled": bool,
        "BytesScannedCutoffPerQuery": int,
        "RequesterPaysEnabled": bool,
        "EngineVersion": "EngineVersionTypeDef",
    },
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
        "EngineVersion": "EngineVersionTypeDef",
    },
    total=False,
)

WorkGroupSummaryTypeDef = TypedDict(
    "WorkGroupSummaryTypeDef",
    {
        "Name": str,
        "State": WorkGroupStateType,
        "Description": str,
        "CreationTime": datetime,
        "EngineVersion": "EngineVersionTypeDef",
    },
    total=False,
)

_RequiredWorkGroupTypeDef = TypedDict(
    "_RequiredWorkGroupTypeDef",
    {
        "Name": str,
    },
)
_OptionalWorkGroupTypeDef = TypedDict(
    "_OptionalWorkGroupTypeDef",
    {
        "State": WorkGroupStateType,
        "Configuration": "WorkGroupConfigurationTypeDef",
        "Description": str,
        "CreationTime": datetime,
    },
    total=False,
)

class WorkGroupTypeDef(_RequiredWorkGroupTypeDef, _OptionalWorkGroupTypeDef):
    pass
