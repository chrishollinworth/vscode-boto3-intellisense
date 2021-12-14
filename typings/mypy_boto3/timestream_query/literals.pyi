"""
Type annotations for timestream-query service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/literals.html)

Usage::

    ```python
    from mypy_boto3_timestream_query.literals import DimensionValueTypeType

    data: DimensionValueTypeType = "VARCHAR"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DimensionValueTypeType",
    "ListScheduledQueriesPaginatorName",
    "ListTagsForResourcePaginatorName",
    "MeasureValueTypeType",
    "QueryPaginatorName",
    "S3EncryptionOptionType",
    "ScalarMeasureValueTypeType",
    "ScalarTypeType",
    "ScheduledQueryRunStatusType",
    "ScheduledQueryStateType",
)

DimensionValueTypeType = Literal["VARCHAR"]
ListScheduledQueriesPaginatorName = Literal["list_scheduled_queries"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
MeasureValueTypeType = Literal["BIGINT", "BOOLEAN", "DOUBLE", "MULTI", "VARCHAR"]
QueryPaginatorName = Literal["query"]
S3EncryptionOptionType = Literal["SSE_KMS", "SSE_S3"]
ScalarMeasureValueTypeType = Literal["BIGINT", "BOOLEAN", "DOUBLE", "VARCHAR"]
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
ScheduledQueryRunStatusType = Literal[
    "AUTO_TRIGGER_FAILURE",
    "AUTO_TRIGGER_SUCCESS",
    "MANUAL_TRIGGER_FAILURE",
    "MANUAL_TRIGGER_SUCCESS",
]
ScheduledQueryStateType = Literal["DISABLED", "ENABLED"]
