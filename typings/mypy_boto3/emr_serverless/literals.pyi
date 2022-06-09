"""
Type annotations for emr-serverless service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/literals.html)

Usage::

    ```python
    from mypy_boto3_emr_serverless.literals import ApplicationStateType

    data: ApplicationStateType = "CREATED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ApplicationStateType",
    "JobRunStateType",
    "ListApplicationsPaginatorName",
    "ListJobRunsPaginatorName",
)

ApplicationStateType = Literal[
    "CREATED", "CREATING", "STARTED", "STARTING", "STOPPED", "STOPPING", "TERMINATED"
]
JobRunStateType = Literal[
    "CANCELLED", "CANCELLING", "FAILED", "PENDING", "RUNNING", "SCHEDULED", "SUBMITTED", "SUCCESS"
]
ListApplicationsPaginatorName = Literal["list_applications"]
ListJobRunsPaginatorName = Literal["list_job_runs"]
