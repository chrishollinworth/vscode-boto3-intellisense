"""
Type annotations for timestream-write service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/literals.html)

Usage::

    ```python
    from mypy_boto3_timestream_write.literals import BatchLoadDataFormatType

    data: BatchLoadDataFormatType = "CSV"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BatchLoadDataFormatType",
    "BatchLoadStatusType",
    "DimensionValueTypeType",
    "MeasureValueTypeType",
    "PartitionKeyEnforcementLevelType",
    "PartitionKeyTypeType",
    "S3EncryptionOptionType",
    "ScalarMeasureValueTypeType",
    "TableStatusType",
    "TimeUnitType",
)

BatchLoadDataFormatType = Literal["CSV"]
BatchLoadStatusType = Literal[
    "CREATED", "FAILED", "IN_PROGRESS", "PENDING_RESUME", "PROGRESS_STOPPED", "SUCCEEDED"
]
DimensionValueTypeType = Literal["VARCHAR"]
MeasureValueTypeType = Literal["BIGINT", "BOOLEAN", "DOUBLE", "MULTI", "TIMESTAMP", "VARCHAR"]
PartitionKeyEnforcementLevelType = Literal["OPTIONAL", "REQUIRED"]
PartitionKeyTypeType = Literal["DIMENSION", "MEASURE"]
S3EncryptionOptionType = Literal["SSE_KMS", "SSE_S3"]
ScalarMeasureValueTypeType = Literal["BIGINT", "BOOLEAN", "DOUBLE", "TIMESTAMP", "VARCHAR"]
TableStatusType = Literal["ACTIVE", "DELETING", "RESTORING"]
TimeUnitType = Literal["MICROSECONDS", "MILLISECONDS", "NANOSECONDS", "SECONDS"]
