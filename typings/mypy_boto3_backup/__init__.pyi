"""
Main interface for backup service.

Usage::

    ```python
    import boto3
    from mypy_boto3_backup import (
        BackupClient,
        Client,
        ListBackupJobsPaginator,
        ListBackupPlanTemplatesPaginator,
        ListBackupPlanVersionsPaginator,
        ListBackupPlansPaginator,
        ListBackupSelectionsPaginator,
        ListBackupVaultsPaginator,
        ListCopyJobsPaginator,
        ListLegalHoldsPaginator,
        ListProtectedResourcesByBackupVaultPaginator,
        ListProtectedResourcesPaginator,
        ListRecoveryPointsByBackupVaultPaginator,
        ListRecoveryPointsByLegalHoldPaginator,
        ListRecoveryPointsByResourcePaginator,
        ListRestoreJobsPaginator,
    )

    session = boto3.Session()

    client: BackupClient = boto3.client("backup")
    session_client: BackupClient = session.client("backup")

    list_backup_jobs_paginator: ListBackupJobsPaginator = client.get_paginator("list_backup_jobs")
    list_backup_plan_templates_paginator: ListBackupPlanTemplatesPaginator = client.get_paginator("list_backup_plan_templates")
    list_backup_plan_versions_paginator: ListBackupPlanVersionsPaginator = client.get_paginator("list_backup_plan_versions")
    list_backup_plans_paginator: ListBackupPlansPaginator = client.get_paginator("list_backup_plans")
    list_backup_selections_paginator: ListBackupSelectionsPaginator = client.get_paginator("list_backup_selections")
    list_backup_vaults_paginator: ListBackupVaultsPaginator = client.get_paginator("list_backup_vaults")
    list_copy_jobs_paginator: ListCopyJobsPaginator = client.get_paginator("list_copy_jobs")
    list_legal_holds_paginator: ListLegalHoldsPaginator = client.get_paginator("list_legal_holds")
    list_protected_resources_paginator: ListProtectedResourcesPaginator = client.get_paginator("list_protected_resources")
    list_protected_resources_by_backup_vault_paginator: ListProtectedResourcesByBackupVaultPaginator = client.get_paginator("list_protected_resources_by_backup_vault")
    list_recovery_points_by_backup_vault_paginator: ListRecoveryPointsByBackupVaultPaginator = client.get_paginator("list_recovery_points_by_backup_vault")
    list_recovery_points_by_legal_hold_paginator: ListRecoveryPointsByLegalHoldPaginator = client.get_paginator("list_recovery_points_by_legal_hold")
    list_recovery_points_by_resource_paginator: ListRecoveryPointsByResourcePaginator = client.get_paginator("list_recovery_points_by_resource")
    list_restore_jobs_paginator: ListRestoreJobsPaginator = client.get_paginator("list_restore_jobs")
    ```
"""
from .client import BackupClient
from .paginator import (
    ListBackupJobsPaginator,
    ListBackupPlansPaginator,
    ListBackupPlanTemplatesPaginator,
    ListBackupPlanVersionsPaginator,
    ListBackupSelectionsPaginator,
    ListBackupVaultsPaginator,
    ListCopyJobsPaginator,
    ListLegalHoldsPaginator,
    ListProtectedResourcesByBackupVaultPaginator,
    ListProtectedResourcesPaginator,
    ListRecoveryPointsByBackupVaultPaginator,
    ListRecoveryPointsByLegalHoldPaginator,
    ListRecoveryPointsByResourcePaginator,
    ListRestoreJobsPaginator,
)

Client = BackupClient

__all__ = (
    "BackupClient",
    "Client",
    "ListBackupJobsPaginator",
    "ListBackupPlanTemplatesPaginator",
    "ListBackupPlanVersionsPaginator",
    "ListBackupPlansPaginator",
    "ListBackupSelectionsPaginator",
    "ListBackupVaultsPaginator",
    "ListCopyJobsPaginator",
    "ListLegalHoldsPaginator",
    "ListProtectedResourcesByBackupVaultPaginator",
    "ListProtectedResourcesPaginator",
    "ListRecoveryPointsByBackupVaultPaginator",
    "ListRecoveryPointsByLegalHoldPaginator",
    "ListRecoveryPointsByResourcePaginator",
    "ListRestoreJobsPaginator",
)
