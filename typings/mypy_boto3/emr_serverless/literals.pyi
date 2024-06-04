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
    "ArchitectureType",
    "JobRunModeType",
    "JobRunStateType",
    "ListApplicationsPaginatorName",
    "ListJobRunAttemptsPaginatorName",
    "ListJobRunsPaginatorName",
)

ApplicationStateType = Literal[
    "CREATED", "CREATING", "STARTED", "STARTING", "STOPPED", "STOPPING", "TERMINATED"
]
ArchitectureType = Literal["ARM64", "X86_64"]
JobRunModeType = Literal["BATCH", "STREAMING"]
JobRunStateType = Literal[
    "CANCELLED", "CANCELLING", "FAILED", "PENDING", "RUNNING", "SCHEDULED", "SUBMITTED", "SUCCESS"
]
ListApplicationsPaginatorName = Literal["list_applications"]
ListJobRunAttemptsPaginatorName = Literal["list_job_run_attempts"]
ListJobRunsPaginatorName = Literal["list_job_runs"]
