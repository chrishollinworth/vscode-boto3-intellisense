"""
Main interface for backup service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
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
        ListIndexedRecoveryPointsPaginator,
        ListLegalHoldsPaginator,
        ListProtectedResourcesByBackupVaultPaginator,
        ListProtectedResourcesPaginator,
        ListRecoveryPointsByBackupVaultPaginator,
        ListRecoveryPointsByLegalHoldPaginator,
        ListRecoveryPointsByResourcePaginator,
        ListRestoreJobsByProtectedResourcePaginator,
        ListRestoreJobsPaginator,
        ListRestoreTestingPlansPaginator,
        ListRestoreTestingSelectionsPaginator,
    )

    session = Session()
    client: BackupClient = session.client("backup")

    list_backup_jobs_paginator: ListBackupJobsPaginator = client.get_paginator("list_backup_jobs")
    list_backup_plan_templates_paginator: ListBackupPlanTemplatesPaginator = client.get_paginator("list_backup_plan_templates")
    list_backup_plan_versions_paginator: ListBackupPlanVersionsPaginator = client.get_paginator("list_backup_plan_versions")
    list_backup_plans_paginator: ListBackupPlansPaginator = client.get_paginator("list_backup_plans")
    list_backup_selections_paginator: ListBackupSelectionsPaginator = client.get_paginator("list_backup_selections")
    list_backup_vaults_paginator: ListBackupVaultsPaginator = client.get_paginator("list_backup_vaults")
    list_copy_jobs_paginator: ListCopyJobsPaginator = client.get_paginator("list_copy_jobs")
    list_indexed_recovery_points_paginator: ListIndexedRecoveryPointsPaginator = client.get_paginator("list_indexed_recovery_points")
    list_legal_holds_paginator: ListLegalHoldsPaginator = client.get_paginator("list_legal_holds")
    list_protected_resources_by_backup_vault_paginator: ListProtectedResourcesByBackupVaultPaginator = client.get_paginator("list_protected_resources_by_backup_vault")
    list_protected_resources_paginator: ListProtectedResourcesPaginator = client.get_paginator("list_protected_resources")
    list_recovery_points_by_backup_vault_paginator: ListRecoveryPointsByBackupVaultPaginator = client.get_paginator("list_recovery_points_by_backup_vault")
    list_recovery_points_by_legal_hold_paginator: ListRecoveryPointsByLegalHoldPaginator = client.get_paginator("list_recovery_points_by_legal_hold")
    list_recovery_points_by_resource_paginator: ListRecoveryPointsByResourcePaginator = client.get_paginator("list_recovery_points_by_resource")
    list_restore_jobs_by_protected_resource_paginator: ListRestoreJobsByProtectedResourcePaginator = client.get_paginator("list_restore_jobs_by_protected_resource")
    list_restore_jobs_paginator: ListRestoreJobsPaginator = client.get_paginator("list_restore_jobs")
    list_restore_testing_plans_paginator: ListRestoreTestingPlansPaginator = client.get_paginator("list_restore_testing_plans")
    list_restore_testing_selections_paginator: ListRestoreTestingSelectionsPaginator = client.get_paginator("list_restore_testing_selections")
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
    ListIndexedRecoveryPointsPaginator,
    ListLegalHoldsPaginator,
    ListProtectedResourcesByBackupVaultPaginator,
    ListProtectedResourcesPaginator,
    ListRecoveryPointsByBackupVaultPaginator,
    ListRecoveryPointsByLegalHoldPaginator,
    ListRecoveryPointsByResourcePaginator,
    ListRestoreJobsByProtectedResourcePaginator,
    ListRestoreJobsPaginator,
    ListRestoreTestingPlansPaginator,
    ListRestoreTestingSelectionsPaginator,
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
    "ListIndexedRecoveryPointsPaginator",
    "ListLegalHoldsPaginator",
    "ListProtectedResourcesByBackupVaultPaginator",
    "ListProtectedResourcesPaginator",
    "ListRecoveryPointsByBackupVaultPaginator",
    "ListRecoveryPointsByLegalHoldPaginator",
    "ListRecoveryPointsByResourcePaginator",
    "ListRestoreJobsByProtectedResourcePaginator",
    "ListRestoreJobsPaginator",
    "ListRestoreTestingPlansPaginator",
    "ListRestoreTestingSelectionsPaginator",
)
