"""
Type annotations for lakeformation service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/literals.html)

Usage::

    ```python
    from mypy_boto3_lakeformation.literals import ComparisonOperatorType

    data: ComparisonOperatorType = "BEGINS_WITH"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ComparisonOperatorType",
    "DataLakeResourceTypeType",
    "FieldNameStringType",
    "GetWorkUnitsPaginatorName",
    "ListDataCellsFilterPaginatorName",
    "ListLFTagsPaginatorName",
    "OptimizerTypeType",
    "PermissionType",
    "PermissionTypeType",
    "QueryStateStringType",
    "ResourceShareTypeType",
    "ResourceTypeType",
    "SearchDatabasesByLFTagsPaginatorName",
    "SearchTablesByLFTagsPaginatorName",
    "TransactionStatusFilterType",
    "TransactionStatusType",
    "TransactionTypeType",
)

ComparisonOperatorType = Literal[
    "BEGINS_WITH", "BETWEEN", "CONTAINS", "EQ", "GE", "GT", "IN", "LE", "LT", "NE", "NOT_CONTAINS"
]
DataLakeResourceTypeType = Literal[
    "CATALOG",
    "DATABASE",
    "DATA_LOCATION",
    "LF_TAG",
    "LF_TAG_POLICY",
    "LF_TAG_POLICY_DATABASE",
    "LF_TAG_POLICY_TABLE",
    "TABLE",
]
FieldNameStringType = Literal["LAST_MODIFIED", "RESOURCE_ARN", "ROLE_ARN"]
GetWorkUnitsPaginatorName = Literal["get_work_units"]
ListDataCellsFilterPaginatorName = Literal["list_data_cells_filter"]
ListLFTagsPaginatorName = Literal["list_lf_tags"]
OptimizerTypeType = Literal["ALL", "COMPACTION", "GARBAGE_COLLECTION"]
PermissionType = Literal[
    "ALL",
    "ALTER",
    "ASSOCIATE",
    "CREATE_DATABASE",
    "CREATE_LF_TAG",
    "CREATE_TABLE",
    "DATA_LOCATION_ACCESS",
    "DELETE",
    "DESCRIBE",
    "DROP",
    "GRANT_WITH_LF_TAG_EXPRESSION",
    "INSERT",
    "SELECT",
]
PermissionTypeType = Literal[
    "CELL_FILTER_PERMISSION", "COLUMN_PERMISSION", "NESTED_CELL_PERMISSION", "NESTED_PERMISSION"
]
QueryStateStringType = Literal["ERROR", "EXPIRED", "FINISHED", "PENDING", "WORKUNITS_AVAILABLE"]
ResourceShareTypeType = Literal["ALL", "FOREIGN"]
ResourceTypeType = Literal["DATABASE", "TABLE"]
SearchDatabasesByLFTagsPaginatorName = Literal["search_databases_by_lf_tags"]
SearchTablesByLFTagsPaginatorName = Literal["search_tables_by_lf_tags"]
TransactionStatusFilterType = Literal["ABORTED", "ACTIVE", "ALL", "COMMITTED", "COMPLETED"]
TransactionStatusType = Literal["ABORTED", "ACTIVE", "COMMITTED", "COMMIT_IN_PROGRESS"]
TransactionTypeType = Literal["READ_AND_WRITE", "READ_ONLY"]
