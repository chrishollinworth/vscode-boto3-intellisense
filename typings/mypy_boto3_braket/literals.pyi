"""
Type annotations for braket service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/literals.html)

Usage::

    ```python
    from mypy_boto3_braket.literals import CancellationStatusType

    data: CancellationStatusType = "CANCELLED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CancellationStatusType",
    "DeviceStatusType",
    "DeviceTypeType",
    "QuantumTaskStatusType",
    "SearchDevicesPaginatorName",
    "SearchQuantumTasksFilterOperatorType",
    "SearchQuantumTasksPaginatorName",
)

CancellationStatusType = Literal["CANCELLED", "CANCELLING"]
DeviceStatusType = Literal["OFFLINE", "ONLINE", "RETIRED"]
DeviceTypeType = Literal["QPU", "SIMULATOR"]
QuantumTaskStatusType = Literal[
    "CANCELLED", "CANCELLING", "COMPLETED", "CREATED", "FAILED", "QUEUED", "RUNNING"
]
SearchDevicesPaginatorName = Literal["search_devices"]
SearchQuantumTasksFilterOperatorType = Literal["BETWEEN", "EQUAL", "GT", "GTE", "LT", "LTE"]
SearchQuantumTasksPaginatorName = Literal["search_quantum_tasks"]
