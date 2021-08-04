"""
Type annotations for redshift-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_redshift_data.type_defs import BatchExecuteStatementInputRequestTypeDef

    data: BatchExecuteStatementInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import StatementStatusStringType, StatusStringType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BatchExecuteStatementInputRequestTypeDef",
    "BatchExecuteStatementOutputTypeDef",
    "CancelStatementRequestRequestTypeDef",
    "CancelStatementResponseTypeDef",
    "ColumnMetadataTypeDef",
    "DescribeStatementRequestRequestTypeDef",
    "DescribeStatementResponseTypeDef",
    "DescribeTableRequestRequestTypeDef",
    "DescribeTableResponseTypeDef",
    "ExecuteStatementInputRequestTypeDef",
    "ExecuteStatementOutputTypeDef",
    "FieldTypeDef",
    "GetStatementResultRequestRequestTypeDef",
    "GetStatementResultResponseTypeDef",
    "ListDatabasesRequestRequestTypeDef",
    "ListDatabasesResponseTypeDef",
    "ListSchemasRequestRequestTypeDef",
    "ListSchemasResponseTypeDef",
    "ListStatementsRequestRequestTypeDef",
    "ListStatementsResponseTypeDef",
    "ListTablesRequestRequestTypeDef",
    "ListTablesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SqlParameterTypeDef",
    "StatementDataTypeDef",
    "SubStatementDataTypeDef",
    "TableMemberTypeDef",
)

_RequiredBatchExecuteStatementInputRequestTypeDef = TypedDict(
    "_RequiredBatchExecuteStatementInputRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "Database": str,
        "Sqls": List[str],
    },
)
_OptionalBatchExecuteStatementInputRequestTypeDef = TypedDict(
    "_OptionalBatchExecuteStatementInputRequestTypeDef",
    {
        "DbUser": str,
        "SecretArn": str,
        "StatementName": str,
        "WithEvent": bool,
    },
    total=False,
)

class BatchExecuteStatementInputRequestTypeDef(
    _RequiredBatchExecuteStatementInputRequestTypeDef,
    _OptionalBatchExecuteStatementInputRequestTypeDef,
):
    pass

BatchExecuteStatementOutputTypeDef = TypedDict(
    "BatchExecuteStatementOutputTypeDef",
    {
        "ClusterIdentifier": str,
        "CreatedAt": datetime,
        "Database": str,
        "DbUser": str,
        "Id": str,
        "SecretArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelStatementRequestRequestTypeDef = TypedDict(
    "CancelStatementRequestRequestTypeDef",
    {
        "Id": str,
    },
)

CancelStatementResponseTypeDef = TypedDict(
    "CancelStatementResponseTypeDef",
    {
        "Status": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ColumnMetadataTypeDef = TypedDict(
    "ColumnMetadataTypeDef",
    {
        "columnDefault": str,
        "isCaseSensitive": bool,
        "isCurrency": bool,
        "isSigned": bool,
        "label": str,
        "length": int,
        "name": str,
        "nullable": int,
        "precision": int,
        "scale": int,
        "schemaName": str,
        "tableName": str,
        "typeName": str,
    },
    total=False,
)

DescribeStatementRequestRequestTypeDef = TypedDict(
    "DescribeStatementRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeStatementResponseTypeDef = TypedDict(
    "DescribeStatementResponseTypeDef",
    {
        "ClusterIdentifier": str,
        "CreatedAt": datetime,
        "Database": str,
        "DbUser": str,
        "Duration": int,
        "Error": str,
        "HasResultSet": bool,
        "Id": str,
        "QueryParameters": List["SqlParameterTypeDef"],
        "QueryString": str,
        "RedshiftPid": int,
        "RedshiftQueryId": int,
        "ResultRows": int,
        "ResultSize": int,
        "SecretArn": str,
        "Status": StatusStringType,
        "SubStatements": List["SubStatementDataTypeDef"],
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTableRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeTableRequestRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "Database": str,
    },
)
_OptionalDescribeTableRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeTableRequestRequestTypeDef",
    {
        "ConnectedDatabase": str,
        "DbUser": str,
        "MaxResults": int,
        "NextToken": str,
        "Schema": str,
        "SecretArn": str,
        "Table": str,
    },
    total=False,
)

class DescribeTableRequestRequestTypeDef(
    _RequiredDescribeTableRequestRequestTypeDef, _OptionalDescribeTableRequestRequestTypeDef
):
    pass

DescribeTableResponseTypeDef = TypedDict(
    "DescribeTableResponseTypeDef",
    {
        "ColumnList": List["ColumnMetadataTypeDef"],
        "NextToken": str,
        "TableName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExecuteStatementInputRequestTypeDef = TypedDict(
    "_RequiredExecuteStatementInputRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "Database": str,
        "Sql": str,
    },
)
_OptionalExecuteStatementInputRequestTypeDef = TypedDict(
    "_OptionalExecuteStatementInputRequestTypeDef",
    {
        "DbUser": str,
        "Parameters": List["SqlParameterTypeDef"],
        "SecretArn": str,
        "StatementName": str,
        "WithEvent": bool,
    },
    total=False,
)

class ExecuteStatementInputRequestTypeDef(
    _RequiredExecuteStatementInputRequestTypeDef, _OptionalExecuteStatementInputRequestTypeDef
):
    pass

ExecuteStatementOutputTypeDef = TypedDict(
    "ExecuteStatementOutputTypeDef",
    {
        "ClusterIdentifier": str,
        "CreatedAt": datetime,
        "Database": str,
        "DbUser": str,
        "Id": str,
        "SecretArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FieldTypeDef = TypedDict(
    "FieldTypeDef",
    {
        "blobValue": bytes,
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)

_RequiredGetStatementResultRequestRequestTypeDef = TypedDict(
    "_RequiredGetStatementResultRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalGetStatementResultRequestRequestTypeDef = TypedDict(
    "_OptionalGetStatementResultRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class GetStatementResultRequestRequestTypeDef(
    _RequiredGetStatementResultRequestRequestTypeDef,
    _OptionalGetStatementResultRequestRequestTypeDef,
):
    pass

GetStatementResultResponseTypeDef = TypedDict(
    "GetStatementResultResponseTypeDef",
    {
        "ColumnMetadata": List["ColumnMetadataTypeDef"],
        "NextToken": str,
        "Records": List[List["FieldTypeDef"]],
        "TotalNumRows": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDatabasesRequestRequestTypeDef = TypedDict(
    "_RequiredListDatabasesRequestRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "Database": str,
    },
)
_OptionalListDatabasesRequestRequestTypeDef = TypedDict(
    "_OptionalListDatabasesRequestRequestTypeDef",
    {
        "DbUser": str,
        "MaxResults": int,
        "NextToken": str,
        "SecretArn": str,
    },
    total=False,
)

class ListDatabasesRequestRequestTypeDef(
    _RequiredListDatabasesRequestRequestTypeDef, _OptionalListDatabasesRequestRequestTypeDef
):
    pass

ListDatabasesResponseTypeDef = TypedDict(
    "ListDatabasesResponseTypeDef",
    {
        "Databases": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSchemasRequestRequestTypeDef = TypedDict(
    "_RequiredListSchemasRequestRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "Database": str,
    },
)
_OptionalListSchemasRequestRequestTypeDef = TypedDict(
    "_OptionalListSchemasRequestRequestTypeDef",
    {
        "ConnectedDatabase": str,
        "DbUser": str,
        "MaxResults": int,
        "NextToken": str,
        "SchemaPattern": str,
        "SecretArn": str,
    },
    total=False,
)

class ListSchemasRequestRequestTypeDef(
    _RequiredListSchemasRequestRequestTypeDef, _OptionalListSchemasRequestRequestTypeDef
):
    pass

ListSchemasResponseTypeDef = TypedDict(
    "ListSchemasResponseTypeDef",
    {
        "NextToken": str,
        "Schemas": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStatementsRequestRequestTypeDef = TypedDict(
    "ListStatementsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "RoleLevel": bool,
        "StatementName": str,
        "Status": StatusStringType,
    },
    total=False,
)

ListStatementsResponseTypeDef = TypedDict(
    "ListStatementsResponseTypeDef",
    {
        "NextToken": str,
        "Statements": List["StatementDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTablesRequestRequestTypeDef = TypedDict(
    "_RequiredListTablesRequestRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "Database": str,
    },
)
_OptionalListTablesRequestRequestTypeDef = TypedDict(
    "_OptionalListTablesRequestRequestTypeDef",
    {
        "ConnectedDatabase": str,
        "DbUser": str,
        "MaxResults": int,
        "NextToken": str,
        "SchemaPattern": str,
        "SecretArn": str,
        "TablePattern": str,
    },
    total=False,
)

class ListTablesRequestRequestTypeDef(
    _RequiredListTablesRequestRequestTypeDef, _OptionalListTablesRequestRequestTypeDef
):
    pass

ListTablesResponseTypeDef = TypedDict(
    "ListTablesResponseTypeDef",
    {
        "NextToken": str,
        "Tables": List["TableMemberTypeDef"],
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

SqlParameterTypeDef = TypedDict(
    "SqlParameterTypeDef",
    {
        "name": str,
        "value": str,
    },
)

_RequiredStatementDataTypeDef = TypedDict(
    "_RequiredStatementDataTypeDef",
    {
        "Id": str,
    },
)
_OptionalStatementDataTypeDef = TypedDict(
    "_OptionalStatementDataTypeDef",
    {
        "CreatedAt": datetime,
        "IsBatchStatement": bool,
        "QueryParameters": List["SqlParameterTypeDef"],
        "QueryString": str,
        "QueryStrings": List[str],
        "SecretArn": str,
        "StatementName": str,
        "Status": StatusStringType,
        "UpdatedAt": datetime,
    },
    total=False,
)

class StatementDataTypeDef(_RequiredStatementDataTypeDef, _OptionalStatementDataTypeDef):
    pass

_RequiredSubStatementDataTypeDef = TypedDict(
    "_RequiredSubStatementDataTypeDef",
    {
        "Id": str,
    },
)
_OptionalSubStatementDataTypeDef = TypedDict(
    "_OptionalSubStatementDataTypeDef",
    {
        "CreatedAt": datetime,
        "Duration": int,
        "Error": str,
        "HasResultSet": bool,
        "QueryString": str,
        "RedshiftQueryId": int,
        "ResultRows": int,
        "ResultSize": int,
        "Status": StatementStatusStringType,
        "UpdatedAt": datetime,
    },
    total=False,
)

class SubStatementDataTypeDef(_RequiredSubStatementDataTypeDef, _OptionalSubStatementDataTypeDef):
    pass

TableMemberTypeDef = TypedDict(
    "TableMemberTypeDef",
    {
        "name": str,
        "schema": str,
        "type": str,
    },
    total=False,
)
