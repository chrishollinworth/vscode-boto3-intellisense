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

from .literals import DecimalReturnTypeType, LongReturnTypeType, RecordsFormatTypeType, TypeHintType

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
        "booleanValues": List[bool],
        "longValues": List[int],
        "doubleValues": List[float],
        "stringValues": List[str],
        "arrayValues": List[Dict[str, Any]],
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
        "schema": str,
        "parameterSets": List[List["SqlParameterTypeDef"]],
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
        "name": str,
        "type": int,
        "typeName": str,
        "label": str,
        "schemaName": str,
        "tableName": str,
        "isAutoIncrement": bool,
        "isSigned": bool,
        "isCurrency": bool,
        "isCaseSensitive": bool,
        "nullable": int,
        "precision": int,
        "scale": int,
        "arrayBaseColumnType": int,
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
        "dbClusterOrInstanceArn": str,
        "awsSecretStoreArn": str,
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
        "database": str,
        "schema": str,
        "parameters": List["SqlParameterTypeDef"],
        "transactionId": str,
        "includeResultMetadata": bool,
        "continueAfterTimeout": bool,
        "resultSetOptions": "ResultSetOptionsTypeDef",
        "formatRecordsAs": RecordsFormatTypeType,
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
        "records": List[List["FieldTypeDef"]],
        "columnMetadata": List["ColumnMetadataTypeDef"],
        "numberOfRecordsUpdated": int,
        "generatedFields": List["FieldTypeDef"],
        "formattedRecords": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FieldTypeDef = TypedDict(
    "FieldTypeDef",
    {
        "isNull": bool,
        "booleanValue": bool,
        "longValue": int,
        "doubleValue": float,
        "stringValue": str,
        "blobValue": Union[bytes, IO[bytes], StreamingBody],
        "arrayValue": "ArrayValueTypeDef",
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
        "resultSetMetadata": "ResultSetMetadataTypeDef",
        "records": List["RecordTypeDef"],
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
        "longReturnType": LongReturnTypeType,
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
        "value": "FieldTypeDef",
        "typeHint": TypeHintType,
    },
    total=False,
)

SqlStatementResultTypeDef = TypedDict(
    "SqlStatementResultTypeDef",
    {
        "resultFrame": "ResultFrameTypeDef",
        "numberOfRecordsUpdated": int,
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
        "isNull": bool,
        "bitValue": bool,
        "bigIntValue": int,
        "intValue": int,
        "doubleValue": float,
        "realValue": float,
        "stringValue": str,
        "blobValue": bytes,
        "arrayValues": List[Dict[str, Any]],
        "structValue": Dict[str, Any],
    },
    total=False,
)
