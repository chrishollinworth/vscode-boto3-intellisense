"""
Type annotations for timestream-query service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/literals.html)

Usage::

    ```python
    from mypy_boto3_timestream_query.literals import QueryPaginatorName

    data: QueryPaginatorName = "query"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("QueryPaginatorName", "ScalarTypeType")

QueryPaginatorName = Literal["query"]
ScalarTypeType = Literal[
    "BIGINT",
    "BOOLEAN",
    "DATE",
    "DOUBLE",
    "INTEGER",
    "INTERVAL_DAY_TO_SECOND",
    "INTERVAL_YEAR_TO_MONTH",
    "TIME",
    "TIMESTAMP",
    "UNKNOWN",
    "VARCHAR",
]
