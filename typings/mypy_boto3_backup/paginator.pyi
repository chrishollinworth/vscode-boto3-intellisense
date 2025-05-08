"""
Type annotations for backup service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_backup.client import BackupClient
    from mypy_boto3_backup.paginator import (
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListBackupJobsInputPaginateTypeDef,
    ListBackupJobsOutputTypeDef,
    ListBackupPlansInputPaginateTypeDef,
    ListBackupPlansOutputTypeDef,
    ListBackupPlanTemplatesInputPaginateTypeDef,
    ListBackupPlanTemplatesOutputTypeDef,
    ListBackupPlanVersionsInputPaginateTypeDef,
    ListBackupPlanVersionsOutputTypeDef,
    ListBackupSelectionsInputPaginateTypeDef,
    ListBackupSelectionsOutputTypeDef,
    ListBackupVaultsInputPaginateTypeDef,
    ListBackupVaultsOutputTypeDef,
    ListCopyJobsInputPaginateTypeDef,
    ListCopyJobsOutputTypeDef,
    ListIndexedRecoveryPointsInputPaginateTypeDef,
    ListIndexedRecoveryPointsOutputTypeDef,
    ListLegalHoldsInputPaginateTypeDef,
    ListLegalHoldsOutputTypeDef,
    ListProtectedResourcesByBackupVaultInputPaginateTypeDef,
    ListProtectedResourcesByBackupVaultOutputTypeDef,
    ListProtectedResourcesInputPaginateTypeDef,
    ListProtectedResourcesOutputTypeDef,
    ListRecoveryPointsByBackupVaultInputPaginateTypeDef,
    ListRecoveryPointsByBackupVaultOutputTypeDef,
    ListRecoveryPointsByLegalHoldInputPaginateTypeDef,
    ListRecoveryPointsByLegalHoldOutputTypeDef,
    ListRecoveryPointsByResourceInputPaginateTypeDef,
    ListRecoveryPointsByResourceOutputTypeDef,
    ListRestoreJobsByProtectedResourceInputPaginateTypeDef,
    ListRestoreJobsByProtectedResourceOutputTypeDef,
    ListRestoreJobsInputPaginateTypeDef,
    ListRestoreJobsOutputTypeDef,
    ListRestoreTestingPlansInputPaginateTypeDef,
    ListRestoreTestingPlansOutputTypeDef,
    ListRestoreTestingSelectionsInputPaginateTypeDef,
    ListRestoreTestingSelectionsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
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

if TYPE_CHECKING:
    _ListBackupJobsPaginatorBase = Paginator[ListBackupJobsOutputTypeDef]
else:
    _ListBackupJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBackupJobsPaginator(_ListBackupJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListBackupJobs.html#Backup.Paginator.ListBackupJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listbackupjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBackupJobsInputPaginateTypeDef]
    ) -> PageIterator[ListBackupJobsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListBackupJobs.html#Backup.Paginator.ListBackupJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listbackupjobspaginator)
        """

if TYPE_CHECKING:
    _ListBackupPlanTemplatesPaginatorBase = Paginator[ListBackupPlanTemplatesOutputTypeDef]
else:
    _ListBackupPlanTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListBackupPlanTemplatesPaginator(_ListBackupPlanTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListBackupPlanTemplates.html#Backup.Paginator.ListBackupPlanTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listbackupplantemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBackupPlanTemplatesInputPaginateTypeDef]
    ) -> PageIterator[ListBackupPlanTemplatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListBackupPlanTemplates.html#Backup.Paginator.ListBackupPlanTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listbackupplantemplatespaginator)
        """

if TYPE_CHECKING:
    _ListBackupPlanVersionsPaginatorBase = Paginator[ListBackupPlanVersionsOutputTypeDef]
else:
    _ListBackupPlanVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBackupPlanVersionsPaginator(_ListBackupPlanVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListBackupPlanVersions.html#Backup.Paginator.ListBackupPlanVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listbackupplanversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBackupPlanVersionsInputPaginateTypeDef]
    ) -> PageIterator[ListBackupPlanVersionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListBackupPlanVersions.html#Backup.Paginator.ListBackupPlanVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listbackupplanversionspaginator)
        """

if TYPE_CHECKING:
    _ListBackupPlansPaginatorBase = Paginator[ListBackupPlansOutputTypeDef]
else:
    _ListBackupPlansPaginatorBase = Paginator  # type: ignore[assignment]

class ListBackupPlansPaginator(_ListBackupPlansPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListBackupPlans.html#Backup.Paginator.ListBackupPlans)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listbackupplanspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBackupPlansInputPaginateTypeDef]
    ) -> PageIterator[ListBackupPlansOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListBackupPlans.html#Backup.Paginator.ListBackupPlans.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listbackupplanspaginator)
        """

if TYPE_CHECKING:
    _ListBackupSelectionsPaginatorBase = Paginator[ListBackupSelectionsOutputTypeDef]
else:
    _ListBackupSelectionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBackupSelectionsPaginator(_ListBackupSelectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListBackupSelections.html#Backup.Paginator.ListBackupSelections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listbackupselectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBackupSelectionsInputPaginateTypeDef]
    ) -> PageIterator[ListBackupSelectionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListBackupSelections.html#Backup.Paginator.ListBackupSelections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listbackupselectionspaginator)
        """

if TYPE_CHECKING:
    _ListBackupVaultsPaginatorBase = Paginator[ListBackupVaultsOutputTypeDef]
else:
    _ListBackupVaultsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBackupVaultsPaginator(_ListBackupVaultsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListBackupVaults.html#Backup.Paginator.ListBackupVaults)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listbackupvaultspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBackupVaultsInputPaginateTypeDef]
    ) -> PageIterator[ListBackupVaultsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListBackupVaults.html#Backup.Paginator.ListBackupVaults.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listbackupvaultspaginator)
        """

if TYPE_CHECKING:
    _ListCopyJobsPaginatorBase = Paginator[ListCopyJobsOutputTypeDef]
else:
    _ListCopyJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCopyJobsPaginator(_ListCopyJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListCopyJobs.html#Backup.Paginator.ListCopyJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listcopyjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCopyJobsInputPaginateTypeDef]
    ) -> PageIterator[ListCopyJobsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListCopyJobs.html#Backup.Paginator.ListCopyJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listcopyjobspaginator)
        """

if TYPE_CHECKING:
    _ListIndexedRecoveryPointsPaginatorBase = Paginator[ListIndexedRecoveryPointsOutputTypeDef]
else:
    _ListIndexedRecoveryPointsPaginatorBase = Paginator  # type: ignore[assignment]

class ListIndexedRecoveryPointsPaginator(_ListIndexedRecoveryPointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListIndexedRecoveryPoints.html#Backup.Paginator.ListIndexedRecoveryPoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listindexedrecoverypointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIndexedRecoveryPointsInputPaginateTypeDef]
    ) -> PageIterator[ListIndexedRecoveryPointsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListIndexedRecoveryPoints.html#Backup.Paginator.ListIndexedRecoveryPoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listindexedrecoverypointspaginator)
        """

if TYPE_CHECKING:
    _ListLegalHoldsPaginatorBase = Paginator[ListLegalHoldsOutputTypeDef]
else:
    _ListLegalHoldsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLegalHoldsPaginator(_ListLegalHoldsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListLegalHolds.html#Backup.Paginator.ListLegalHolds)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listlegalholdspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLegalHoldsInputPaginateTypeDef]
    ) -> PageIterator[ListLegalHoldsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListLegalHolds.html#Backup.Paginator.ListLegalHolds.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listlegalholdspaginator)
        """

if TYPE_CHECKING:
    _ListProtectedResourcesByBackupVaultPaginatorBase = Paginator[
        ListProtectedResourcesByBackupVaultOutputTypeDef
    ]
else:
    _ListProtectedResourcesByBackupVaultPaginatorBase = Paginator  # type: ignore[assignment]

class ListProtectedResourcesByBackupVaultPaginator(
    _ListProtectedResourcesByBackupVaultPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListProtectedResourcesByBackupVault.html#Backup.Paginator.ListProtectedResourcesByBackupVault)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listprotectedresourcesbybackupvaultpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProtectedResourcesByBackupVaultInputPaginateTypeDef]
    ) -> PageIterator[ListProtectedResourcesByBackupVaultOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListProtectedResourcesByBackupVault.html#Backup.Paginator.ListProtectedResourcesByBackupVault.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listprotectedresourcesbybackupvaultpaginator)
        """

if TYPE_CHECKING:
    _ListProtectedResourcesPaginatorBase = Paginator[ListProtectedResourcesOutputTypeDef]
else:
    _ListProtectedResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListProtectedResourcesPaginator(_ListProtectedResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListProtectedResources.html#Backup.Paginator.ListProtectedResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listprotectedresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProtectedResourcesInputPaginateTypeDef]
    ) -> PageIterator[ListProtectedResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListProtectedResources.html#Backup.Paginator.ListProtectedResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listprotectedresourcespaginator)
        """

if TYPE_CHECKING:
    _ListRecoveryPointsByBackupVaultPaginatorBase = Paginator[
        ListRecoveryPointsByBackupVaultOutputTypeDef
    ]
else:
    _ListRecoveryPointsByBackupVaultPaginatorBase = Paginator  # type: ignore[assignment]

class ListRecoveryPointsByBackupVaultPaginator(_ListRecoveryPointsByBackupVaultPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListRecoveryPointsByBackupVault.html#Backup.Paginator.ListRecoveryPointsByBackupVault)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listrecoverypointsbybackupvaultpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRecoveryPointsByBackupVaultInputPaginateTypeDef]
    ) -> PageIterator[ListRecoveryPointsByBackupVaultOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListRecoveryPointsByBackupVault.html#Backup.Paginator.ListRecoveryPointsByBackupVault.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listrecoverypointsbybackupvaultpaginator)
        """

if TYPE_CHECKING:
    _ListRecoveryPointsByLegalHoldPaginatorBase = Paginator[
        ListRecoveryPointsByLegalHoldOutputTypeDef
    ]
else:
    _ListRecoveryPointsByLegalHoldPaginatorBase = Paginator  # type: ignore[assignment]

class ListRecoveryPointsByLegalHoldPaginator(_ListRecoveryPointsByLegalHoldPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListRecoveryPointsByLegalHold.html#Backup.Paginator.ListRecoveryPointsByLegalHold)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listrecoverypointsbylegalholdpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRecoveryPointsByLegalHoldInputPaginateTypeDef]
    ) -> PageIterator[ListRecoveryPointsByLegalHoldOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListRecoveryPointsByLegalHold.html#Backup.Paginator.ListRecoveryPointsByLegalHold.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listrecoverypointsbylegalholdpaginator)
        """

if TYPE_CHECKING:
    _ListRecoveryPointsByResourcePaginatorBase = Paginator[
        ListRecoveryPointsByResourceOutputTypeDef
    ]
else:
    _ListRecoveryPointsByResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListRecoveryPointsByResourcePaginator(_ListRecoveryPointsByResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListRecoveryPointsByResource.html#Backup.Paginator.ListRecoveryPointsByResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listrecoverypointsbyresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRecoveryPointsByResourceInputPaginateTypeDef]
    ) -> PageIterator[ListRecoveryPointsByResourceOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListRecoveryPointsByResource.html#Backup.Paginator.ListRecoveryPointsByResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listrecoverypointsbyresourcepaginator)
        """

if TYPE_CHECKING:
    _ListRestoreJobsByProtectedResourcePaginatorBase = Paginator[
        ListRestoreJobsByProtectedResourceOutputTypeDef
    ]
else:
    _ListRestoreJobsByProtectedResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListRestoreJobsByProtectedResourcePaginator(_ListRestoreJobsByProtectedResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListRestoreJobsByProtectedResource.html#Backup.Paginator.ListRestoreJobsByProtectedResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listrestorejobsbyprotectedresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRestoreJobsByProtectedResourceInputPaginateTypeDef]
    ) -> PageIterator[ListRestoreJobsByProtectedResourceOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListRestoreJobsByProtectedResource.html#Backup.Paginator.ListRestoreJobsByProtectedResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listrestorejobsbyprotectedresourcepaginator)
        """

if TYPE_CHECKING:
    _ListRestoreJobsPaginatorBase = Paginator[ListRestoreJobsOutputTypeDef]
else:
    _ListRestoreJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRestoreJobsPaginator(_ListRestoreJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListRestoreJobs.html#Backup.Paginator.ListRestoreJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listrestorejobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRestoreJobsInputPaginateTypeDef]
    ) -> PageIterator[ListRestoreJobsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListRestoreJobs.html#Backup.Paginator.ListRestoreJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listrestorejobspaginator)
        """

if TYPE_CHECKING:
    _ListRestoreTestingPlansPaginatorBase = Paginator[ListRestoreTestingPlansOutputTypeDef]
else:
    _ListRestoreTestingPlansPaginatorBase = Paginator  # type: ignore[assignment]

class ListRestoreTestingPlansPaginator(_ListRestoreTestingPlansPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListRestoreTestingPlans.html#Backup.Paginator.ListRestoreTestingPlans)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listrestoretestingplanspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRestoreTestingPlansInputPaginateTypeDef]
    ) -> PageIterator[ListRestoreTestingPlansOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListRestoreTestingPlans.html#Backup.Paginator.ListRestoreTestingPlans.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listrestoretestingplanspaginator)
        """

if TYPE_CHECKING:
    _ListRestoreTestingSelectionsPaginatorBase = Paginator[
        ListRestoreTestingSelectionsOutputTypeDef
    ]
else:
    _ListRestoreTestingSelectionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRestoreTestingSelectionsPaginator(_ListRestoreTestingSelectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListRestoreTestingSelections.html#Backup.Paginator.ListRestoreTestingSelections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listrestoretestingselectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRestoreTestingSelectionsInputPaginateTypeDef]
    ) -> PageIterator[ListRestoreTestingSelectionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/paginator/ListRestoreTestingSelections.html#Backup.Paginator.ListRestoreTestingSelections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators/#listrestoretestingselectionspaginator)
        """
