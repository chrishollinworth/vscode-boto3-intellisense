"""
Type annotations for backup service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/literals.html)

Usage::

    ```python
    from mypy_boto3_backup.literals import BackupJobStateType

    data: BackupJobStateType = "ABORTED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BackupJobStateType",
    "BackupVaultEventType",
    "ConditionTypeType",
    "CopyJobStateType",
    "RecoveryPointStatusType",
    "RestoreJobStatusType",
    "StorageClassType",
)

BackupJobStateType = Literal[
    "ABORTED", "ABORTING", "COMPLETED", "CREATED", "EXPIRED", "FAILED", "PENDING", "RUNNING"
]
BackupVaultEventType = Literal[
    "BACKUP_JOB_COMPLETED",
    "BACKUP_JOB_EXPIRED",
    "BACKUP_JOB_FAILED",
    "BACKUP_JOB_STARTED",
    "BACKUP_JOB_SUCCESSFUL",
    "BACKUP_PLAN_CREATED",
    "BACKUP_PLAN_MODIFIED",
    "COPY_JOB_FAILED",
    "COPY_JOB_STARTED",
    "COPY_JOB_SUCCESSFUL",
    "RECOVERY_POINT_MODIFIED",
    "RESTORE_JOB_COMPLETED",
    "RESTORE_JOB_FAILED",
    "RESTORE_JOB_STARTED",
    "RESTORE_JOB_SUCCESSFUL",
]
ConditionTypeType = Literal["STRINGEQUALS"]
CopyJobStateType = Literal["COMPLETED", "CREATED", "FAILED", "RUNNING"]
RecoveryPointStatusType = Literal["COMPLETED", "DELETING", "EXPIRED", "PARTIAL"]
RestoreJobStatusType = Literal["ABORTED", "COMPLETED", "FAILED", "PENDING", "RUNNING"]
StorageClassType = Literal["COLD", "DELETED", "WARM"]
