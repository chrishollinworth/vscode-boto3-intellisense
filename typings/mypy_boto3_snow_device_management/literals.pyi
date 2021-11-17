"""
Type annotations for snow-device-management service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/literals.html)

Usage::

    ```python
    from mypy_boto3_snow_device_management.literals import AttachmentStatusType

    data: AttachmentStatusType = "ATTACHED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AttachmentStatusType",
    "ExecutionStateType",
    "InstanceStateNameType",
    "IpAddressAssignmentType",
    "ListDeviceResourcesPaginatorName",
    "ListDevicesPaginatorName",
    "ListExecutionsPaginatorName",
    "ListTasksPaginatorName",
    "PhysicalConnectorTypeType",
    "TaskStateType",
    "UnlockStateType",
)

AttachmentStatusType = Literal["ATTACHED", "ATTACHING", "DETACHED", "DETACHING"]
ExecutionStateType = Literal[
    "CANCELED", "FAILED", "IN_PROGRESS", "QUEUED", "REJECTED", "SUCCEEDED", "TIMED_OUT"
]
InstanceStateNameType = Literal[
    "PENDING", "RUNNING", "SHUTTING_DOWN", "STOPPED", "STOPPING", "TERMINATED"
]
IpAddressAssignmentType = Literal["DHCP", "STATIC"]
ListDeviceResourcesPaginatorName = Literal["list_device_resources"]
ListDevicesPaginatorName = Literal["list_devices"]
ListExecutionsPaginatorName = Literal["list_executions"]
ListTasksPaginatorName = Literal["list_tasks"]
PhysicalConnectorTypeType = Literal["QSFP", "RJ45", "RJ45_2", "SFP_PLUS", "WIFI"]
TaskStateType = Literal["CANCELED", "COMPLETED", "IN_PROGRESS"]
UnlockStateType = Literal["LOCKED", "UNLOCKED", "UNLOCKING"]
