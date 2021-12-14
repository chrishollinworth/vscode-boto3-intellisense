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
    "CompressionTypeType",
    "DeviceStatusType",
    "DeviceTypeType",
    "InstanceTypeType",
    "JobEventTypeType",
    "JobPrimaryStatusType",
    "QuantumTaskStatusType",
    "SearchDevicesPaginatorName",
    "SearchJobsFilterOperatorType",
    "SearchJobsPaginatorName",
    "SearchQuantumTasksFilterOperatorType",
    "SearchQuantumTasksPaginatorName",
)

CancellationStatusType = Literal["CANCELLED", "CANCELLING"]
CompressionTypeType = Literal["GZIP", "NONE"]
DeviceStatusType = Literal["OFFLINE", "ONLINE", "RETIRED"]
DeviceTypeType = Literal["QPU", "SIMULATOR"]
InstanceTypeType = Literal[
    "ml.c4.2xlarge",
    "ml.c4.4xlarge",
    "ml.c4.8xlarge",
    "ml.c4.xlarge",
    "ml.c5.18xlarge",
    "ml.c5.2xlarge",
    "ml.c5.4xlarge",
    "ml.c5.9xlarge",
    "ml.c5.xlarge",
    "ml.c5n.18xlarge",
    "ml.c5n.2xlarge",
    "ml.c5n.4xlarge",
    "ml.c5n.9xlarge",
    "ml.c5n.xlarge",
    "ml.g4dn.12xlarge",
    "ml.g4dn.16xlarge",
    "ml.g4dn.2xlarge",
    "ml.g4dn.4xlarge",
    "ml.g4dn.8xlarge",
    "ml.g4dn.xlarge",
    "ml.m4.10xlarge",
    "ml.m4.16xlarge",
    "ml.m4.2xlarge",
    "ml.m4.4xlarge",
    "ml.m4.xlarge",
    "ml.m5.12xlarge",
    "ml.m5.24xlarge",
    "ml.m5.2xlarge",
    "ml.m5.4xlarge",
    "ml.m5.large",
    "ml.m5.xlarge",
    "ml.p2.16xlarge",
    "ml.p2.8xlarge",
    "ml.p2.xlarge",
    "ml.p3.16xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
    "ml.p3dn.24xlarge",
    "ml.p4d.24xlarge",
]
JobEventTypeType = Literal[
    "CANCELLED",
    "COMPLETED",
    "DEPRIORITIZED_DUE_TO_INACTIVITY",
    "DOWNLOADING_DATA",
    "FAILED",
    "MAX_RUNTIME_EXCEEDED",
    "QUEUED_FOR_EXECUTION",
    "RUNNING",
    "STARTING_INSTANCE",
    "UPLOADING_RESULTS",
    "WAITING_FOR_PRIORITY",
]
JobPrimaryStatusType = Literal[
    "CANCELLED", "CANCELLING", "COMPLETED", "FAILED", "QUEUED", "RUNNING"
]
QuantumTaskStatusType = Literal[
    "CANCELLED", "CANCELLING", "COMPLETED", "CREATED", "FAILED", "QUEUED", "RUNNING"
]
SearchDevicesPaginatorName = Literal["search_devices"]
SearchJobsFilterOperatorType = Literal["BETWEEN", "CONTAINS", "EQUAL", "GT", "GTE", "LT", "LTE"]
SearchJobsPaginatorName = Literal["search_jobs"]
SearchQuantumTasksFilterOperatorType = Literal["BETWEEN", "EQUAL", "GT", "GTE", "LT", "LTE"]
SearchQuantumTasksPaginatorName = Literal["search_quantum_tasks"]
