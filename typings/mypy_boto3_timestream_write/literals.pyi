"""
Type annotations for timestream-write service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/literals.html)

Usage::

    ```python
    from mypy_boto3_timestream_write.literals import DimensionValueTypeType

    data: DimensionValueTypeType = "VARCHAR"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("DimensionValueTypeType", "MeasureValueTypeType", "TableStatusType", "TimeUnitType")

DimensionValueTypeType = Literal["VARCHAR"]
MeasureValueTypeType = Literal["BIGINT", "BOOLEAN", "DOUBLE", "VARCHAR"]
TableStatusType = Literal["ACTIVE", "DELETING"]
TimeUnitType = Literal["MICROSECONDS", "MILLISECONDS", "NANOSECONDS", "SECONDS"]
