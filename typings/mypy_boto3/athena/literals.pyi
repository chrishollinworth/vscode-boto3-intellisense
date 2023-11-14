"""
Type annotations for athena service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/literals.html)

Usage::

    ```python
    from mypy_boto3_athena.literals import CalculationExecutionStateType

    data: CalculationExecutionStateType = "CANCELED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CalculationExecutionStateType",
    "CapacityAllocationStatusType",
    "CapacityReservationStatusType",
    "ColumnNullableType",
    "DataCatalogTypeType",
    "EncryptionOptionType",
    "ExecutorStateType",
    "ExecutorTypeType",
    "GetQueryResultsPaginatorName",
    "ListDataCatalogsPaginatorName",
    "ListDatabasesPaginatorName",
    "ListNamedQueriesPaginatorName",
    "ListQueryExecutionsPaginatorName",
    "ListTableMetadataPaginatorName",
    "ListTagsForResourcePaginatorName",
    "NotebookTypeType",
    "QueryExecutionStateType",
    "S3AclOptionType",
    "SessionStateType",
    "StatementTypeType",
    "WorkGroupStateType",
)

CalculationExecutionStateType = Literal[
    "CANCELED", "CANCELING", "COMPLETED", "CREATED", "CREATING", "FAILED", "QUEUED", "RUNNING"
]
CapacityAllocationStatusType = Literal["FAILED", "PENDING", "SUCCEEDED"]
CapacityReservationStatusType = Literal[
    "ACTIVE", "CANCELLED", "CANCELLING", "FAILED", "PENDING", "UPDATE_PENDING"
]
ColumnNullableType = Literal["NOT_NULL", "NULLABLE", "UNKNOWN"]
DataCatalogTypeType = Literal["GLUE", "HIVE", "LAMBDA"]
EncryptionOptionType = Literal["CSE_KMS", "SSE_KMS", "SSE_S3"]
ExecutorStateType = Literal[
    "CREATED", "CREATING", "FAILED", "REGISTERED", "TERMINATED", "TERMINATING"
]
ExecutorTypeType = Literal["COORDINATOR", "GATEWAY", "WORKER"]
GetQueryResultsPaginatorName = Literal["get_query_results"]
ListDataCatalogsPaginatorName = Literal["list_data_catalogs"]
ListDatabasesPaginatorName = Literal["list_databases"]
ListNamedQueriesPaginatorName = Literal["list_named_queries"]
ListQueryExecutionsPaginatorName = Literal["list_query_executions"]
ListTableMetadataPaginatorName = Literal["list_table_metadata"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
NotebookTypeType = Literal["IPYNB"]
QueryExecutionStateType = Literal["CANCELLED", "FAILED", "QUEUED", "RUNNING", "SUCCEEDED"]
S3AclOptionType = Literal["BUCKET_OWNER_FULL_CONTROL"]
SessionStateType = Literal[
    "BUSY", "CREATED", "CREATING", "DEGRADED", "FAILED", "IDLE", "TERMINATED", "TERMINATING"
]
StatementTypeType = Literal["DDL", "DML", "UTILITY"]
WorkGroupStateType = Literal["DISABLED", "ENABLED"]
