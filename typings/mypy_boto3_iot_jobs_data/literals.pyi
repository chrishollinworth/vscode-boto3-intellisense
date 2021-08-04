"""
Type annotations for iot-jobs-data service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/literals.html)

Usage::

    ```python
    from mypy_boto3_iot_jobs_data.literals import JobExecutionStatusType

    data: JobExecutionStatusType = "CANCELED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("JobExecutionStatusType",)

JobExecutionStatusType = Literal[
    "CANCELED", "FAILED", "IN_PROGRESS", "QUEUED", "REJECTED", "REMOVED", "SUCCEEDED", "TIMED_OUT"
]
