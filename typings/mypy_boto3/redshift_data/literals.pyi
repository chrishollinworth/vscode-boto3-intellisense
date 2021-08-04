"""
Type annotations for redshift-data service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/literals.html)

Usage::

    ```python
    from mypy_boto3_redshift_data.literals import DescribeTablePaginatorName

    data: DescribeTablePaginatorName = "describe_table"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DescribeTablePaginatorName",
    "GetStatementResultPaginatorName",
    "ListDatabasesPaginatorName",
    "ListSchemasPaginatorName",
    "ListStatementsPaginatorName",
    "ListTablesPaginatorName",
    "StatementStatusStringType",
    "StatusStringType",
)

DescribeTablePaginatorName = Literal["describe_table"]
GetStatementResultPaginatorName = Literal["get_statement_result"]
ListDatabasesPaginatorName = Literal["list_databases"]
ListSchemasPaginatorName = Literal["list_schemas"]
ListStatementsPaginatorName = Literal["list_statements"]
ListTablesPaginatorName = Literal["list_tables"]
StatementStatusStringType = Literal[
    "ABORTED", "FAILED", "FINISHED", "PICKED", "STARTED", "SUBMITTED"
]
StatusStringType = Literal["ABORTED", "ALL", "FAILED", "FINISHED", "PICKED", "STARTED", "SUBMITTED"]
