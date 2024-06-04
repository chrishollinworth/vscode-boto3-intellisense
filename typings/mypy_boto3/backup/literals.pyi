"""
Type annotations for backup service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/literals.html)

Usage::

    ```python
    from mypy_boto3_backup.literals import AggregationPeriodType

    data: AggregationPeriodType = "FOURTEEN_DAYS"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AggregationPeriodType",
    "BackupJobStateType",
    "BackupJobStatusType",
    "BackupVaultEventType",
    "ConditionTypeType",
    "CopyJobStateType",
    "CopyJobStatusType",
    "LegalHoldStatusType",
    "ListBackupJobsPaginatorName",
    "ListBackupPlanTemplatesPaginatorName",
    "ListBackupPlanVersionsPaginatorName",
    "ListBackupPlansPaginatorName",
    "ListBackupSelectionsPaginatorName",
    "ListBackupVaultsPaginatorName",
    "ListCopyJobsPaginatorName",
    "ListLegalHoldsPaginatorName",
    "ListProtectedResourcesByBackupVaultPaginatorName",
    "ListProtectedResourcesPaginatorName",
    "ListRecoveryPointsByBackupVaultPaginatorName",
    "ListRecoveryPointsByLegalHoldPaginatorName",
    "ListRecoveryPointsByResourcePaginatorName",
    "ListRestoreJobsByProtectedResourcePaginatorName",
    "ListRestoreJobsPaginatorName",
    "ListRestoreTestingPlansPaginatorName",
    "ListRestoreTestingSelectionsPaginatorName",
    "RecoveryPointStatusType",
    "RestoreDeletionStatusType",
    "RestoreJobStateType",
    "RestoreJobStatusType",
    "RestoreTestingRecoveryPointSelectionAlgorithmType",
    "RestoreTestingRecoveryPointTypeType",
    "RestoreValidationStatusType",
    "StorageClassType",
    "VaultStateType",
    "VaultTypeType",
)

AggregationPeriodType = Literal["FOURTEEN_DAYS", "ONE_DAY", "SEVEN_DAYS"]
BackupJobStateType = Literal[
    "ABORTED",
    "ABORTING",
    "COMPLETED",
    "CREATED",
    "EXPIRED",
    "FAILED",
    "PARTIAL",
    "PENDING",
    "RUNNING",
]
BackupJobStatusType = Literal[
    "ABORTED",
    "ABORTING",
    "AGGREGATE_ALL",
    "ANY",
    "COMPLETED",
    "CREATED",
    "EXPIRED",
    "FAILED",
    "PARTIAL",
    "PENDING",
    "RUNNING",
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
    "S3_BACKUP_OBJECT_FAILED",
    "S3_RESTORE_OBJECT_FAILED",
]
ConditionTypeType = Literal["STRINGEQUALS"]
CopyJobStateType = Literal["COMPLETED", "CREATED", "FAILED", "PARTIAL", "RUNNING"]
CopyJobStatusType = Literal[
    "ABORTED",
    "ABORTING",
    "AGGREGATE_ALL",
    "ANY",
    "COMPLETED",
    "COMPLETING",
    "CREATED",
    "FAILED",
    "FAILING",
    "PARTIAL",
    "RUNNING",
]
LegalHoldStatusType = Literal["ACTIVE", "CANCELED", "CANCELING", "CREATING"]
ListBackupJobsPaginatorName = Literal["list_backup_jobs"]
ListBackupPlanTemplatesPaginatorName = Literal["list_backup_plan_templates"]
ListBackupPlanVersionsPaginatorName = Literal["list_backup_plan_versions"]
ListBackupPlansPaginatorName = Literal["list_backup_plans"]
ListBackupSelectionsPaginatorName = Literal["list_backup_selections"]
ListBackupVaultsPaginatorName = Literal["list_backup_vaults"]
ListCopyJobsPaginatorName = Literal["list_copy_jobs"]
ListLegalHoldsPaginatorName = Literal["list_legal_holds"]
ListProtectedResourcesByBackupVaultPaginatorName = Literal[
    "list_protected_resources_by_backup_vault"
]
ListProtectedResourcesPaginatorName = Literal["list_protected_resources"]
ListRecoveryPointsByBackupVaultPaginatorName = Literal["list_recovery_points_by_backup_vault"]
ListRecoveryPointsByLegalHoldPaginatorName = Literal["list_recovery_points_by_legal_hold"]
ListRecoveryPointsByResourcePaginatorName = Literal["list_recovery_points_by_resource"]
ListRestoreJobsByProtectedResourcePaginatorName = Literal["list_restore_jobs_by_protected_resource"]
ListRestoreJobsPaginatorName = Literal["list_restore_jobs"]
ListRestoreTestingPlansPaginatorName = Literal["list_restore_testing_plans"]
ListRestoreTestingSelectionsPaginatorName = Literal["list_restore_testing_selections"]
RecoveryPointStatusType = Literal["COMPLETED", "DELETING", "EXPIRED", "PARTIAL"]
RestoreDeletionStatusType = Literal["DELETING", "FAILED", "SUCCESSFUL"]
RestoreJobStateType = Literal[
    "ABORTED", "AGGREGATE_ALL", "ANY", "COMPLETED", "CREATED", "FAILED", "PENDING", "RUNNING"
]
RestoreJobStatusType = Literal["ABORTED", "COMPLETED", "FAILED", "PENDING", "RUNNING"]
RestoreTestingRecoveryPointSelectionAlgorithmType = Literal[
    "LATEST_WITHIN_WINDOW", "RANDOM_WITHIN_WINDOW"
]
RestoreTestingRecoveryPointTypeType = Literal["CONTINUOUS", "SNAPSHOT"]
RestoreValidationStatusType = Literal["FAILED", "SUCCESSFUL", "TIMED_OUT", "VALIDATING"]
StorageClassType = Literal["COLD", "DELETED", "WARM"]
VaultStateType = Literal["AVAILABLE", "CREATING", "FAILED"]
VaultTypeType = Literal["BACKUP_VAULT", "LOGICALLY_AIR_GAPPED_BACKUP_VAULT"]
