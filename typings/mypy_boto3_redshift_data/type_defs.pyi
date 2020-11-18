"""
Main interface for redshift-data service type definitions.

Usage::

    ```python
    from mypy_boto3_redshift_data.type_defs import ColumnMetadataTypeDef

    data: ColumnMetadataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ColumnMetadataTypeDef",
    "FieldTypeDef",
    "ResponseMetadata",
    "StatementDataTypeDef",
    "TableMemberTypeDef",
    "CancelStatementResponseTypeDef",
    "DescribeStatementResponseTypeDef",
    "DescribeTableResponseTypeDef",
    "ExecuteStatementOutputTypeDef",
    "GetStatementResultResponseTypeDef",
    "ListDatabasesResponseTypeDef",
    "ListSchemasResponseTypeDef",
    "ListStatementsResponseTypeDef",
    "ListTablesResponseTypeDef",
    "PaginatorConfigTypeDef",
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

FieldTypeDef = TypedDict(
    "FieldTypeDef",
    {
        "blobValue": Union[bytes, IO[bytes]],
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
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

_RequiredStatementDataTypeDef = TypedDict("_RequiredStatementDataTypeDef", {"Id": str})
_OptionalStatementDataTypeDef = TypedDict(
    "_OptionalStatementDataTypeDef",
    {
        "CreatedAt": datetime,
        "QueryString": str,
        "SecretArn": str,
        "StatementName": str,
        "Status": Literal["ABORTED", "ALL", "FAILED", "FINISHED", "PICKED", "STARTED", "SUBMITTED"],
        "UpdatedAt": datetime,
    },
    total=False,
)


class StatementDataTypeDef(_RequiredStatementDataTypeDef, _OptionalStatementDataTypeDef):
    pass


TableMemberTypeDef = TypedDict(
    "TableMemberTypeDef", {"name": str, "schema": str, "type": str}, total=False
)

CancelStatementResponseTypeDef = TypedDict(
    "CancelStatementResponseTypeDef", {"Status": bool}, total=False
)

_RequiredDescribeStatementResponseTypeDef = TypedDict(
    "_RequiredDescribeStatementResponseTypeDef", {"Id": str}
)
_OptionalDescribeStatementResponseTypeDef = TypedDict(
    "_OptionalDescribeStatementResponseTypeDef",
    {
        "ClusterIdentifier": str,
        "CreatedAt": datetime,
        "Database": str,
        "DbUser": str,
        "Duration": int,
        "Error": str,
        "QueryString": str,
        "RedshiftPid": int,
        "RedshiftQueryId": int,
        "ResultRows": int,
        "ResultSize": int,
        "SecretArn": str,
        "Status": Literal["ABORTED", "ALL", "FAILED", "FINISHED", "PICKED", "STARTED", "SUBMITTED"],
        "UpdatedAt": datetime,
    },
    total=False,
)


class DescribeStatementResponseTypeDef(
    _RequiredDescribeStatementResponseTypeDef, _OptionalDescribeStatementResponseTypeDef
):
    pass


DescribeTableResponseTypeDef = TypedDict(
    "DescribeTableResponseTypeDef",
    {"ColumnList": List["ColumnMetadataTypeDef"], "NextToken": str, "TableName": str},
    total=False,
)

ExecuteStatementOutputTypeDef = TypedDict(
    "ExecuteStatementOutputTypeDef",
    {
        "ClusterIdentifier": str,
        "CreatedAt": datetime,
        "Database": str,
        "DbUser": str,
        "Id": str,
        "SecretArn": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredGetStatementResultResponseTypeDef = TypedDict(
    "_RequiredGetStatementResultResponseTypeDef", {"Records": List[List["FieldTypeDef"]]}
)
_OptionalGetStatementResultResponseTypeDef = TypedDict(
    "_OptionalGetStatementResultResponseTypeDef",
    {"ColumnMetadata": List["ColumnMetadataTypeDef"], "NextToken": str, "TotalNumRows": int},
    total=False,
)


class GetStatementResultResponseTypeDef(
    _RequiredGetStatementResultResponseTypeDef, _OptionalGetStatementResultResponseTypeDef
):
    pass


ListDatabasesResponseTypeDef = TypedDict(
    "ListDatabasesResponseTypeDef", {"Databases": List[str], "NextToken": str}, total=False
)

ListSchemasResponseTypeDef = TypedDict(
    "ListSchemasResponseTypeDef", {"NextToken": str, "Schemas": List[str]}, total=False
)

_RequiredListStatementsResponseTypeDef = TypedDict(
    "_RequiredListStatementsResponseTypeDef", {"Statements": List["StatementDataTypeDef"]}
)
_OptionalListStatementsResponseTypeDef = TypedDict(
    "_OptionalListStatementsResponseTypeDef", {"NextToken": str}, total=False
)


class ListStatementsResponseTypeDef(
    _RequiredListStatementsResponseTypeDef, _OptionalListStatementsResponseTypeDef
):
    pass


ListTablesResponseTypeDef = TypedDict(
    "ListTablesResponseTypeDef",
    {"NextToken": str, "Tables": List["TableMemberTypeDef"]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
