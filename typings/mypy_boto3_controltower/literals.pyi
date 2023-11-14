"""
Type annotations for controltower service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/literals.html)

Usage::

    ```python
    from mypy_boto3_controltower.literals import ControlOperationStatusType

    data: ControlOperationStatusType = "FAILED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ControlOperationStatusType",
    "ControlOperationTypeType",
    "DriftStatusType",
    "EnablementStatusType",
    "ListEnabledControlsPaginatorName",
)

ControlOperationStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
ControlOperationTypeType = Literal["DISABLE_CONTROL", "ENABLE_CONTROL"]
DriftStatusType = Literal["DRIFTED", "IN_SYNC", "NOT_CHECKING", "UNKNOWN"]
EnablementStatusType = Literal["FAILED", "SUCCEEDED", "UNDER_CHANGE"]
ListEnabledControlsPaginatorName = Literal["list_enabled_controls"]
