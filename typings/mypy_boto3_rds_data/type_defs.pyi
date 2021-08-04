"""
Type annotations for rds-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_rds_data.type_defs import ArrayValueTypeDef

    data: ArrayValueTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import DecimalReturnTypeType, TypeHintType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ArrayValueTypeDef",
    "BatchExecuteStatementRequestRequestTypeDef",
    "BatchExecuteStatementResponseTypeDef",
    "BeginTransactionRequestRequestTypeDef",
    "BeginTransactionResponseTypeDef",
    "ColumnMetadataTypeDef",
    "CommitTransactionRequestRequestTypeDef",
    "CommitTransactionResponseTypeDef",
    "ExecuteSqlRequestRequestTypeDef",
    "ExecuteSqlResponseTypeDef",
    "ExecuteStatementRequestRequestTypeDef",
    "ExecuteStatementResponseTypeDef",
    "FieldTypeDef",
    "RecordTypeDef",
    "ResponseMetadataTypeDef",
    "ResultFrameTypeDef",
    "ResultSetMetadataTypeDef",
    "ResultSetOptionsTypeDef",
    "RollbackTransactionRequestRequestTypeDef",
    "RollbackTransactionResponseTypeDef",
    "SqlParameterTypeDef",
    "SqlStatementResultTypeDef",
    "StructValueTypeDef",
    "UpdateResultTypeDef",
    "ValueTypeDef",
)

ArrayValueTypeDef = TypedDict(
    "ArrayValueTypeDef",
    {
        "arrayValues": List[Dict[str, Any]],
        "booleanValues": List[bool],
        "doubleValues": List[float],
        "longValues": List[int],
        "stringValues": List[str],
    },
    total=False,
)

_RequiredBatchExecuteStatementRequestRequestTypeDef = TypedDict(
    "_RequiredBatchExecuteStatementRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "sql": str,
    },
)
_OptionalBatchExecuteStatementRequestRequestTypeDef = TypedDict(
    "_OptionalBatchExecuteStatementRequestRequestTypeDef",
    {
        "database": str,
        "parameterSets": List[List["SqlParameterTypeDef"]],
        "schema": str,
        "transactionId": str,
    },
    total=False,
)

class BatchExecuteStatementRequestRequestTypeDef(
    _RequiredBatchExecuteStatementRequestRequestTypeDef,
    _OptionalBatchExecuteStatementRequestRequestTypeDef,
):
    pass

BatchExecuteStatementResponseTypeDef = TypedDict(
    "BatchExecuteStatementResponseTypeDef",
    {
        "updateResults": List["UpdateResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBeginTransactionRequestRequestTypeDef = TypedDict(
    "_RequiredBeginTransactionRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
    },
)
_OptionalBeginTransactionRequestRequestTypeDef = TypedDict(
    "_OptionalBeginTransactionRequestRequestTypeDef",
    {
        "database": str,
        "schema": str,
    },
    total=False,
)

class BeginTransactionRequestRequestTypeDef(
    _RequiredBeginTransactionRequestRequestTypeDef, _OptionalBeginTransactionRequestRequestTypeDef
):
    pass

BeginTransactionResponseTypeDef = TypedDict(
    "BeginTransactionResponseTypeDef",
    {
        "transactionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ColumnMetadataTypeDef = TypedDict(
    "ColumnMetadataTypeDef",
    {
        "arrayBaseColumnType": int,
        "isAutoIncrement": bool,
        "isCaseSensitive": bool,
        "isCurrency": bool,
        "isSigned": bool,
        "label": str,
        "name": str,
        "nullable": int,
        "precision": int,
        "scale": int,
        "schemaName": str,
        "tableName": str,
        "type": int,
        "typeName": str,
    },
    total=False,
)

CommitTransactionRequestRequestTypeDef = TypedDict(
    "CommitTransactionRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "transactionId": str,
    },
)

CommitTransactionResponseTypeDef = TypedDict(
    "CommitTransactionResponseTypeDef",
    {
        "transactionStatus": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExecuteSqlRequestRequestTypeDef = TypedDict(
    "_RequiredExecuteSqlRequestRequestTypeDef",
    {
        "awsSecretStoreArn": str,
        "dbClusterOrInstanceArn": str,
        "sqlStatements": str,
    },
)
_OptionalExecuteSqlRequestRequestTypeDef = TypedDict(
    "_OptionalExecuteSqlRequestRequestTypeDef",
    {
        "database": str,
        "schema": str,
    },
    total=False,
)

class ExecuteSqlRequestRequestTypeDef(
    _RequiredExecuteSqlRequestRequestTypeDef, _OptionalExecuteSqlRequestRequestTypeDef
):
    pass

ExecuteSqlResponseTypeDef = TypedDict(
    "ExecuteSqlResponseTypeDef",
    {
        "sqlStatementResults": List["SqlStatementResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExecuteStatementRequestRequestTypeDef = TypedDict(
    "_RequiredExecuteStatementRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "sql": str,
    },
)
_OptionalExecuteStatementRequestRequestTypeDef = TypedDict(
    "_OptionalExecuteStatementRequestRequestTypeDef",
    {
        "continueAfterTimeout": bool,
        "database": str,
        "includeResultMetadata": bool,
        "parameters": List["SqlParameterTypeDef"],
        "resultSetOptions": "ResultSetOptionsTypeDef",
        "schema": str,
        "transactionId": str,
    },
    total=False,
)

class ExecuteStatementRequestRequestTypeDef(
    _RequiredExecuteStatementRequestRequestTypeDef, _OptionalExecuteStatementRequestRequestTypeDef
):
    pass

ExecuteStatementResponseTypeDef = TypedDict(
    "ExecuteStatementResponseTypeDef",
    {
        "columnMetadata": List["ColumnMetadataTypeDef"],
        "generatedFields": List["FieldTypeDef"],
        "numberOfRecordsUpdated": int,
        "records": List[List["FieldTypeDef"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FieldTypeDef = TypedDict(
    "FieldTypeDef",
    {
        "arrayValue": "ArrayValueTypeDef",
        "blobValue": Union[bytes, IO[bytes], StreamingBody],
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "values": List["ValueTypeDef"],
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

ResultFrameTypeDef = TypedDict(
    "ResultFrameTypeDef",
    {
        "records": List["RecordTypeDef"],
        "resultSetMetadata": "ResultSetMetadataTypeDef",
    },
    total=False,
)

ResultSetMetadataTypeDef = TypedDict(
    "ResultSetMetadataTypeDef",
    {
        "columnCount": int,
        "columnMetadata": List["ColumnMetadataTypeDef"],
    },
    total=False,
)

ResultSetOptionsTypeDef = TypedDict(
    "ResultSetOptionsTypeDef",
    {
        "decimalReturnType": DecimalReturnTypeType,
    },
    total=False,
)

RollbackTransactionRequestRequestTypeDef = TypedDict(
    "RollbackTransactionRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "transactionId": str,
    },
)

RollbackTransactionResponseTypeDef = TypedDict(
    "RollbackTransactionResponseTypeDef",
    {
        "transactionStatus": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SqlParameterTypeDef = TypedDict(
    "SqlParameterTypeDef",
    {
        "name": str,
        "typeHint": TypeHintType,
        "value": "FieldTypeDef",
    },
    total=False,
)

SqlStatementResultTypeDef = TypedDict(
    "SqlStatementResultTypeDef",
    {
        "numberOfRecordsUpdated": int,
        "resultFrame": "ResultFrameTypeDef",
    },
    total=False,
)

StructValueTypeDef = TypedDict(
    "StructValueTypeDef",
    {
        "attributes": List["ValueTypeDef"],
    },
    total=False,
)

UpdateResultTypeDef = TypedDict(
    "UpdateResultTypeDef",
    {
        "generatedFields": List["FieldTypeDef"],
    },
    total=False,
)

ValueTypeDef = TypedDict(
    "ValueTypeDef",
    {
        "arrayValues": List[Dict[str, Any]],
        "bigIntValue": int,
        "bitValue": bool,
        "blobValue": bytes,
        "doubleValue": float,
        "intValue": int,
        "isNull": bool,
        "realValue": float,
        "stringValue": str,
        "structValue": Dict[str, Any],
    },
    total=False,
)
