"""
Type annotations for backup service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_backup import BackupClient
    from mypy_boto3_backup.paginator import (
        ListBackupJobsPaginator,
        ListBackupPlanTemplatesPaginator,
        ListBackupPlanVersionsPaginator,
        ListBackupPlansPaginator,
        ListBackupSelectionsPaginator,
        ListBackupVaultsPaginator,
        ListCopyJobsPaginator,
        ListLegalHoldsPaginator,
        ListProtectedResourcesPaginator,
        ListProtectedResourcesByBackupVaultPaginator,
        ListRecoveryPointsByBackupVaultPaginator,
        ListRecoveryPointsByLegalHoldPaginator,
        ListRecoveryPointsByResourcePaginator,
        ListRestoreJobsPaginator,
        ListRestoreJobsByProtectedResourcePaginator,
        ListRestoreTestingPlansPaginator,
        ListRestoreTestingSelectionsPaginator,
    )

    client: BackupClient = boto3.client("backup")

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
    list_restore_jobs_by_protected_resource_paginator: ListRestoreJobsByProtectedResourcePaginator = client.get_paginator("list_restore_jobs_by_protected_resource")
    list_restore_testing_plans_paginator: ListRestoreTestingPlansPaginator = client.get_paginator("list_restore_testing_plans")
    list_restore_testing_selections_paginator: ListRestoreTestingSelectionsPaginator = client.get_paginator("list_restore_testing_selections")
    ```
"""

from datetime import datetime
from typing import Iterator, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import BackupJobStateType, CopyJobStateType, RestoreJobStatusType, VaultTypeType
from .type_defs import (
    ListBackupJobsOutputTypeDef,
    ListBackupPlansOutputTypeDef,
    ListBackupPlanTemplatesOutputTypeDef,
    ListBackupPlanVersionsOutputTypeDef,
    ListBackupSelectionsOutputTypeDef,
    ListBackupVaultsOutputTypeDef,
    ListCopyJobsOutputTypeDef,
    ListLegalHoldsOutputTypeDef,
    ListProtectedResourcesByBackupVaultOutputTypeDef,
    ListProtectedResourcesOutputTypeDef,
    ListRecoveryPointsByBackupVaultOutputTypeDef,
    ListRecoveryPointsByLegalHoldOutputTypeDef,
    ListRecoveryPointsByResourceOutputTypeDef,
    ListRestoreJobsByProtectedResourceOutputTypeDef,
    ListRestoreJobsOutputTypeDef,
    ListRestoreTestingPlansOutputTypeDef,
    ListRestoreTestingSelectionsOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListBackupJobsPaginator",
    "ListBackupPlanTemplatesPaginator",
    "ListBackupPlanVersionsPaginator",
    "ListBackupPlansPaginator",
    "ListBackupSelectionsPaginator",
    "ListBackupVaultsPaginator",
    "ListCopyJobsPaginator",
    "ListLegalHoldsPaginator",
    "ListProtectedResourcesPaginator",
    "ListProtectedResourcesByBackupVaultPaginator",
    "ListRecoveryPointsByBackupVaultPaginator",
    "ListRecoveryPointsByLegalHoldPaginator",
    "ListRecoveryPointsByResourcePaginator",
    "ListRestoreJobsPaginator",
    "ListRestoreJobsByProtectedResourcePaginator",
    "ListRestoreTestingPlansPaginator",
    "ListRestoreTestingSelectionsPaginator",
)

class ListBackupJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListBackupJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listbackupjobspaginator)
    """

    def paginate(
        self,
        *,
        ByResourceArn: str = None,
        ByState: BackupJobStateType = None,
        ByBackupVaultName: str = None,
        ByCreatedBefore: Union[datetime, str] = None,
        ByCreatedAfter: Union[datetime, str] = None,
        ByResourceType: str = None,
        ByAccountId: str = None,
        ByCompleteAfter: Union[datetime, str] = None,
        ByCompleteBefore: Union[datetime, str] = None,
        ByParentJobId: str = None,
        ByMessageCategory: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBackupJobsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListBackupJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listbackupjobspaginator)
        """

class ListBackupPlanTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListBackupPlanTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listbackupplantemplatespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBackupPlanTemplatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListBackupPlanTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listbackupplantemplatespaginator)
        """

class ListBackupPlanVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListBackupPlanVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listbackupplanversionspaginator)
    """

    def paginate(
        self, *, BackupPlanId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBackupPlanVersionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListBackupPlanVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listbackupplanversionspaginator)
        """

class ListBackupPlansPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListBackupPlans)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listbackupplanspaginator)
    """

    def paginate(
        self, *, IncludeDeleted: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBackupPlansOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListBackupPlans.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listbackupplanspaginator)
        """

class ListBackupSelectionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListBackupSelections)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listbackupselectionspaginator)
    """

    def paginate(
        self, *, BackupPlanId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBackupSelectionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListBackupSelections.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listbackupselectionspaginator)
        """

class ListBackupVaultsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListBackupVaults)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listbackupvaultspaginator)
    """

    def paginate(
        self,
        *,
        ByVaultType: VaultTypeType = None,
        ByShared: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBackupVaultsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListBackupVaults.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listbackupvaultspaginator)
        """

class ListCopyJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListCopyJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listcopyjobspaginator)
    """

    def paginate(
        self,
        *,
        ByResourceArn: str = None,
        ByState: CopyJobStateType = None,
        ByCreatedBefore: Union[datetime, str] = None,
        ByCreatedAfter: Union[datetime, str] = None,
        ByResourceType: str = None,
        ByDestinationVaultArn: str = None,
        ByAccountId: str = None,
        ByCompleteBefore: Union[datetime, str] = None,
        ByCompleteAfter: Union[datetime, str] = None,
        ByParentJobId: str = None,
        ByMessageCategory: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCopyJobsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListCopyJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listcopyjobspaginator)
        """

class ListLegalHoldsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListLegalHolds)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listlegalholdspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLegalHoldsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListLegalHolds.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listlegalholdspaginator)
        """

class ListProtectedResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListProtectedResources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listprotectedresourcespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProtectedResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListProtectedResources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listprotectedresourcespaginator)
        """

class ListProtectedResourcesByBackupVaultPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListProtectedResourcesByBackupVault)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listprotectedresourcesbybackupvaultpaginator)
    """

    def paginate(
        self,
        *,
        BackupVaultName: str,
        BackupVaultAccountId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProtectedResourcesByBackupVaultOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListProtectedResourcesByBackupVault.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listprotectedresourcesbybackupvaultpaginator)
        """

class ListRecoveryPointsByBackupVaultPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRecoveryPointsByBackupVault)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrecoverypointsbybackupvaultpaginator)
    """

    def paginate(
        self,
        *,
        BackupVaultName: str,
        BackupVaultAccountId: str = None,
        ByResourceArn: str = None,
        ByResourceType: str = None,
        ByBackupPlanId: str = None,
        ByCreatedBefore: Union[datetime, str] = None,
        ByCreatedAfter: Union[datetime, str] = None,
        ByParentRecoveryPointArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecoveryPointsByBackupVaultOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRecoveryPointsByBackupVault.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrecoverypointsbybackupvaultpaginator)
        """

class ListRecoveryPointsByLegalHoldPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRecoveryPointsByLegalHold)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrecoverypointsbylegalholdpaginator)
    """

    def paginate(
        self, *, LegalHoldId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecoveryPointsByLegalHoldOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRecoveryPointsByLegalHold.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrecoverypointsbylegalholdpaginator)
        """

class ListRecoveryPointsByResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRecoveryPointsByResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrecoverypointsbyresourcepaginator)
    """

    def paginate(
        self,
        *,
        ResourceArn: str,
        ManagedByAWSBackupOnly: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecoveryPointsByResourceOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRecoveryPointsByResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrecoverypointsbyresourcepaginator)
        """

class ListRestoreJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRestoreJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrestorejobspaginator)
    """

    def paginate(
        self,
        *,
        ByAccountId: str = None,
        ByResourceType: str = None,
        ByCreatedBefore: Union[datetime, str] = None,
        ByCreatedAfter: Union[datetime, str] = None,
        ByStatus: RestoreJobStatusType = None,
        ByCompleteBefore: Union[datetime, str] = None,
        ByCompleteAfter: Union[datetime, str] = None,
        ByRestoreTestingPlanArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRestoreJobsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRestoreJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrestorejobspaginator)
        """

class ListRestoreJobsByProtectedResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRestoreJobsByProtectedResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrestorejobsbyprotectedresourcepaginator)
    """

    def paginate(
        self,
        *,
        ResourceArn: str,
        ByStatus: RestoreJobStatusType = None,
        ByRecoveryPointCreationDateAfter: Union[datetime, str] = None,
        ByRecoveryPointCreationDateBefore: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRestoreJobsByProtectedResourceOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRestoreJobsByProtectedResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrestorejobsbyprotectedresourcepaginator)
        """

class ListRestoreTestingPlansPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRestoreTestingPlans)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrestoretestingplanspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRestoreTestingPlansOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRestoreTestingPlans.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrestoretestingplanspaginator)
        """

class ListRestoreTestingSelectionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRestoreTestingSelections)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrestoretestingselectionspaginator)
    """

    def paginate(
        self, *, RestoreTestingPlanName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRestoreTestingSelectionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRestoreTestingSelections.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrestoretestingselectionspaginator)
        """
