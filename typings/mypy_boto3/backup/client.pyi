"""
Type annotations for backup service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_backup.client import BackupClient

    session = Session()
    client: BackupClient = session.client("backup")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
from .type_defs import (
    CancelLegalHoldInputTypeDef,
    CreateBackupPlanInputTypeDef,
    CreateBackupPlanOutputTypeDef,
    CreateBackupSelectionInputTypeDef,
    CreateBackupSelectionOutputTypeDef,
    CreateBackupVaultInputTypeDef,
    CreateBackupVaultOutputTypeDef,
    CreateFrameworkInputTypeDef,
    CreateFrameworkOutputTypeDef,
    CreateLegalHoldInputTypeDef,
    CreateLegalHoldOutputTypeDef,
    CreateLogicallyAirGappedBackupVaultInputTypeDef,
    CreateLogicallyAirGappedBackupVaultOutputTypeDef,
    CreateReportPlanInputTypeDef,
    CreateReportPlanOutputTypeDef,
    CreateRestoreTestingPlanInputTypeDef,
    CreateRestoreTestingPlanOutputTypeDef,
    CreateRestoreTestingSelectionInputTypeDef,
    CreateRestoreTestingSelectionOutputTypeDef,
    DeleteBackupPlanInputTypeDef,
    DeleteBackupPlanOutputTypeDef,
    DeleteBackupSelectionInputTypeDef,
    DeleteBackupVaultAccessPolicyInputTypeDef,
    DeleteBackupVaultInputTypeDef,
    DeleteBackupVaultLockConfigurationInputTypeDef,
    DeleteBackupVaultNotificationsInputTypeDef,
    DeleteFrameworkInputTypeDef,
    DeleteRecoveryPointInputTypeDef,
    DeleteReportPlanInputTypeDef,
    DeleteRestoreTestingPlanInputTypeDef,
    DeleteRestoreTestingSelectionInputTypeDef,
    DescribeBackupJobInputTypeDef,
    DescribeBackupJobOutputTypeDef,
    DescribeBackupVaultInputTypeDef,
    DescribeBackupVaultOutputTypeDef,
    DescribeCopyJobInputTypeDef,
    DescribeCopyJobOutputTypeDef,
    DescribeFrameworkInputTypeDef,
    DescribeFrameworkOutputTypeDef,
    DescribeGlobalSettingsOutputTypeDef,
    DescribeProtectedResourceInputTypeDef,
    DescribeProtectedResourceOutputTypeDef,
    DescribeRecoveryPointInputTypeDef,
    DescribeRecoveryPointOutputTypeDef,
    DescribeRegionSettingsOutputTypeDef,
    DescribeReportJobInputTypeDef,
    DescribeReportJobOutputTypeDef,
    DescribeReportPlanInputTypeDef,
    DescribeReportPlanOutputTypeDef,
    DescribeRestoreJobInputTypeDef,
    DescribeRestoreJobOutputTypeDef,
    DisassociateRecoveryPointFromParentInputTypeDef,
    DisassociateRecoveryPointInputTypeDef,
    EmptyResponseMetadataTypeDef,
    ExportBackupPlanTemplateInputTypeDef,
    ExportBackupPlanTemplateOutputTypeDef,
    GetBackupPlanFromJSONInputTypeDef,
    GetBackupPlanFromJSONOutputTypeDef,
    GetBackupPlanFromTemplateInputTypeDef,
    GetBackupPlanFromTemplateOutputTypeDef,
    GetBackupPlanInputTypeDef,
    GetBackupPlanOutputTypeDef,
    GetBackupSelectionInputTypeDef,
    GetBackupSelectionOutputTypeDef,
    GetBackupVaultAccessPolicyInputTypeDef,
    GetBackupVaultAccessPolicyOutputTypeDef,
    GetBackupVaultNotificationsInputTypeDef,
    GetBackupVaultNotificationsOutputTypeDef,
    GetLegalHoldInputTypeDef,
    GetLegalHoldOutputTypeDef,
    GetRecoveryPointIndexDetailsInputTypeDef,
    GetRecoveryPointIndexDetailsOutputTypeDef,
    GetRecoveryPointRestoreMetadataInputTypeDef,
    GetRecoveryPointRestoreMetadataOutputTypeDef,
    GetRestoreJobMetadataInputTypeDef,
    GetRestoreJobMetadataOutputTypeDef,
    GetRestoreTestingInferredMetadataInputTypeDef,
    GetRestoreTestingInferredMetadataOutputTypeDef,
    GetRestoreTestingPlanInputTypeDef,
    GetRestoreTestingPlanOutputTypeDef,
    GetRestoreTestingSelectionInputTypeDef,
    GetRestoreTestingSelectionOutputTypeDef,
    GetSupportedResourceTypesOutputTypeDef,
    ListBackupJobsInputTypeDef,
    ListBackupJobsOutputTypeDef,
    ListBackupJobSummariesInputTypeDef,
    ListBackupJobSummariesOutputTypeDef,
    ListBackupPlansInputTypeDef,
    ListBackupPlansOutputTypeDef,
    ListBackupPlanTemplatesInputTypeDef,
    ListBackupPlanTemplatesOutputTypeDef,
    ListBackupPlanVersionsInputTypeDef,
    ListBackupPlanVersionsOutputTypeDef,
    ListBackupSelectionsInputTypeDef,
    ListBackupSelectionsOutputTypeDef,
    ListBackupVaultsInputTypeDef,
    ListBackupVaultsOutputTypeDef,
    ListCopyJobsInputTypeDef,
    ListCopyJobsOutputTypeDef,
    ListCopyJobSummariesInputTypeDef,
    ListCopyJobSummariesOutputTypeDef,
    ListFrameworksInputTypeDef,
    ListFrameworksOutputTypeDef,
    ListIndexedRecoveryPointsInputTypeDef,
    ListIndexedRecoveryPointsOutputTypeDef,
    ListLegalHoldsInputTypeDef,
    ListLegalHoldsOutputTypeDef,
    ListProtectedResourcesByBackupVaultInputTypeDef,
    ListProtectedResourcesByBackupVaultOutputTypeDef,
    ListProtectedResourcesInputTypeDef,
    ListProtectedResourcesOutputTypeDef,
    ListRecoveryPointsByBackupVaultInputTypeDef,
    ListRecoveryPointsByBackupVaultOutputTypeDef,
    ListRecoveryPointsByLegalHoldInputTypeDef,
    ListRecoveryPointsByLegalHoldOutputTypeDef,
    ListRecoveryPointsByResourceInputTypeDef,
    ListRecoveryPointsByResourceOutputTypeDef,
    ListReportJobsInputTypeDef,
    ListReportJobsOutputTypeDef,
    ListReportPlansInputTypeDef,
    ListReportPlansOutputTypeDef,
    ListRestoreJobsByProtectedResourceInputTypeDef,
    ListRestoreJobsByProtectedResourceOutputTypeDef,
    ListRestoreJobsInputTypeDef,
    ListRestoreJobsOutputTypeDef,
    ListRestoreJobSummariesInputTypeDef,
    ListRestoreJobSummariesOutputTypeDef,
    ListRestoreTestingPlansInputTypeDef,
    ListRestoreTestingPlansOutputTypeDef,
    ListRestoreTestingSelectionsInputTypeDef,
    ListRestoreTestingSelectionsOutputTypeDef,
    ListTagsInputTypeDef,
    ListTagsOutputTypeDef,
    PutBackupVaultAccessPolicyInputTypeDef,
    PutBackupVaultLockConfigurationInputTypeDef,
    PutBackupVaultNotificationsInputTypeDef,
    PutRestoreValidationResultInputTypeDef,
    StartBackupJobInputTypeDef,
    StartBackupJobOutputTypeDef,
    StartCopyJobInputTypeDef,
    StartCopyJobOutputTypeDef,
    StartReportJobInputTypeDef,
    StartReportJobOutputTypeDef,
    StartRestoreJobInputTypeDef,
    StartRestoreJobOutputTypeDef,
    StopBackupJobInputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateBackupPlanInputTypeDef,
    UpdateBackupPlanOutputTypeDef,
    UpdateFrameworkInputTypeDef,
    UpdateFrameworkOutputTypeDef,
    UpdateGlobalSettingsInputTypeDef,
    UpdateRecoveryPointIndexSettingsInputTypeDef,
    UpdateRecoveryPointIndexSettingsOutputTypeDef,
    UpdateRecoveryPointLifecycleInputTypeDef,
    UpdateRecoveryPointLifecycleOutputTypeDef,
    UpdateRegionSettingsInputTypeDef,
    UpdateReportPlanInputTypeDef,
    UpdateReportPlanOutputTypeDef,
    UpdateRestoreTestingPlanInputTypeDef,
    UpdateRestoreTestingPlanOutputTypeDef,
    UpdateRestoreTestingSelectionInputTypeDef,
    UpdateRestoreTestingSelectionOutputTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("BackupClient",)

class Exceptions(BaseClientExceptions):
    AlreadyExistsException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DependencyFailureException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidResourceStateException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MissingParameterValueException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]

class BackupClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BackupClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#generate_presigned_url)
        """

    def cancel_legal_hold(self, **kwargs: Unpack[CancelLegalHoldInputTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified legal hold on a recovery point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/cancel_legal_hold.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#cancel_legal_hold)
        """

    def create_backup_plan(
        self, **kwargs: Unpack[CreateBackupPlanInputTypeDef]
    ) -> CreateBackupPlanOutputTypeDef:
        """
        Creates a backup plan using a backup plan name and backup rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/create_backup_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#create_backup_plan)
        """

    def create_backup_selection(
        self, **kwargs: Unpack[CreateBackupSelectionInputTypeDef]
    ) -> CreateBackupSelectionOutputTypeDef:
        """
        Creates a JSON document that specifies a set of resources to assign to a backup
        plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/create_backup_selection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#create_backup_selection)
        """

    def create_backup_vault(
        self, **kwargs: Unpack[CreateBackupVaultInputTypeDef]
    ) -> CreateBackupVaultOutputTypeDef:
        """
        Creates a logical container where backups are stored.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/create_backup_vault.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#create_backup_vault)
        """

    def create_framework(
        self, **kwargs: Unpack[CreateFrameworkInputTypeDef]
    ) -> CreateFrameworkOutputTypeDef:
        """
        Creates a framework with one or more controls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/create_framework.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#create_framework)
        """

    def create_legal_hold(
        self, **kwargs: Unpack[CreateLegalHoldInputTypeDef]
    ) -> CreateLegalHoldOutputTypeDef:
        """
        Creates a legal hold on a recovery point (backup).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/create_legal_hold.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#create_legal_hold)
        """

    def create_logically_air_gapped_backup_vault(
        self, **kwargs: Unpack[CreateLogicallyAirGappedBackupVaultInputTypeDef]
    ) -> CreateLogicallyAirGappedBackupVaultOutputTypeDef:
        """
        Creates a logical container to where backups may be copied.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/create_logically_air_gapped_backup_vault.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#create_logically_air_gapped_backup_vault)
        """

    def create_report_plan(
        self, **kwargs: Unpack[CreateReportPlanInputTypeDef]
    ) -> CreateReportPlanOutputTypeDef:
        """
        Creates a report plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/create_report_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#create_report_plan)
        """

    def create_restore_testing_plan(
        self, **kwargs: Unpack[CreateRestoreTestingPlanInputTypeDef]
    ) -> CreateRestoreTestingPlanOutputTypeDef:
        """
        Creates a restore testing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/create_restore_testing_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#create_restore_testing_plan)
        """

    def create_restore_testing_selection(
        self, **kwargs: Unpack[CreateRestoreTestingSelectionInputTypeDef]
    ) -> CreateRestoreTestingSelectionOutputTypeDef:
        """
        This request can be sent after CreateRestoreTestingPlan request returns
        successfully.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/create_restore_testing_selection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#create_restore_testing_selection)
        """

    def delete_backup_plan(
        self, **kwargs: Unpack[DeleteBackupPlanInputTypeDef]
    ) -> DeleteBackupPlanOutputTypeDef:
        """
        Deletes a backup plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/delete_backup_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#delete_backup_plan)
        """

    def delete_backup_selection(
        self, **kwargs: Unpack[DeleteBackupSelectionInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the resource selection associated with a backup plan that is specified
        by the <code>SelectionId</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/delete_backup_selection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#delete_backup_selection)
        """

    def delete_backup_vault(
        self, **kwargs: Unpack[DeleteBackupVaultInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the backup vault identified by its name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/delete_backup_vault.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#delete_backup_vault)
        """

    def delete_backup_vault_access_policy(
        self, **kwargs: Unpack[DeleteBackupVaultAccessPolicyInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the policy document that manages permissions on a backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/delete_backup_vault_access_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#delete_backup_vault_access_policy)
        """

    def delete_backup_vault_lock_configuration(
        self, **kwargs: Unpack[DeleteBackupVaultLockConfigurationInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes Backup Vault Lock from a backup vault specified by a backup vault name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/delete_backup_vault_lock_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#delete_backup_vault_lock_configuration)
        """

    def delete_backup_vault_notifications(
        self, **kwargs: Unpack[DeleteBackupVaultNotificationsInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes event notifications for the specified backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/delete_backup_vault_notifications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#delete_backup_vault_notifications)
        """

    def delete_framework(
        self, **kwargs: Unpack[DeleteFrameworkInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the framework specified by a framework name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/delete_framework.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#delete_framework)
        """

    def delete_recovery_point(
        self, **kwargs: Unpack[DeleteRecoveryPointInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the recovery point specified by a recovery point ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/delete_recovery_point.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#delete_recovery_point)
        """

    def delete_report_plan(
        self, **kwargs: Unpack[DeleteReportPlanInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the report plan specified by a report plan name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/delete_report_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#delete_report_plan)
        """

    def delete_restore_testing_plan(
        self, **kwargs: Unpack[DeleteRestoreTestingPlanInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This request deletes the specified restore testing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/delete_restore_testing_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#delete_restore_testing_plan)
        """

    def delete_restore_testing_selection(
        self, **kwargs: Unpack[DeleteRestoreTestingSelectionInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Input the Restore Testing Plan name and Restore Testing Selection name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/delete_restore_testing_selection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#delete_restore_testing_selection)
        """

    def describe_backup_job(
        self, **kwargs: Unpack[DescribeBackupJobInputTypeDef]
    ) -> DescribeBackupJobOutputTypeDef:
        """
        Returns backup job details for the specified <code>BackupJobId</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/describe_backup_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#describe_backup_job)
        """

    def describe_backup_vault(
        self, **kwargs: Unpack[DescribeBackupVaultInputTypeDef]
    ) -> DescribeBackupVaultOutputTypeDef:
        """
        Returns metadata about a backup vault specified by its name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/describe_backup_vault.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#describe_backup_vault)
        """

    def describe_copy_job(
        self, **kwargs: Unpack[DescribeCopyJobInputTypeDef]
    ) -> DescribeCopyJobOutputTypeDef:
        """
        Returns metadata associated with creating a copy of a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/describe_copy_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#describe_copy_job)
        """

    def describe_framework(
        self, **kwargs: Unpack[DescribeFrameworkInputTypeDef]
    ) -> DescribeFrameworkOutputTypeDef:
        """
        Returns the framework details for the specified <code>FrameworkName</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/describe_framework.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#describe_framework)
        """

    def describe_global_settings(self) -> DescribeGlobalSettingsOutputTypeDef:
        """
        Describes whether the Amazon Web Services account is opted in to cross-account
        backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/describe_global_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#describe_global_settings)
        """

    def describe_protected_resource(
        self, **kwargs: Unpack[DescribeProtectedResourceInputTypeDef]
    ) -> DescribeProtectedResourceOutputTypeDef:
        """
        Returns information about a saved resource, including the last time it was
        backed up, its Amazon Resource Name (ARN), and the Amazon Web Services service
        type of the saved resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/describe_protected_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#describe_protected_resource)
        """

    def describe_recovery_point(
        self, **kwargs: Unpack[DescribeRecoveryPointInputTypeDef]
    ) -> DescribeRecoveryPointOutputTypeDef:
        """
        Returns metadata associated with a recovery point, including ID, status,
        encryption, and lifecycle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/describe_recovery_point.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#describe_recovery_point)
        """

    def describe_region_settings(self) -> DescribeRegionSettingsOutputTypeDef:
        """
        Returns the current service opt-in settings for the Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/describe_region_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#describe_region_settings)
        """

    def describe_report_job(
        self, **kwargs: Unpack[DescribeReportJobInputTypeDef]
    ) -> DescribeReportJobOutputTypeDef:
        """
        Returns the details associated with creating a report as specified by its
        <code>ReportJobId</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/describe_report_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#describe_report_job)
        """

    def describe_report_plan(
        self, **kwargs: Unpack[DescribeReportPlanInputTypeDef]
    ) -> DescribeReportPlanOutputTypeDef:
        """
        Returns a list of all report plans for an Amazon Web Services account and
        Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/describe_report_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#describe_report_plan)
        """

    def describe_restore_job(
        self, **kwargs: Unpack[DescribeRestoreJobInputTypeDef]
    ) -> DescribeRestoreJobOutputTypeDef:
        """
        Returns metadata associated with a restore job that is specified by a job ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/describe_restore_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#describe_restore_job)
        """

    def disassociate_recovery_point(
        self, **kwargs: Unpack[DisassociateRecoveryPointInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified continuous backup recovery point from Backup and releases
        control of that continuous backup to the source service, such as Amazon RDS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/disassociate_recovery_point.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#disassociate_recovery_point)
        """

    def disassociate_recovery_point_from_parent(
        self, **kwargs: Unpack[DisassociateRecoveryPointFromParentInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This action to a specific child (nested) recovery point removes the
        relationship between the specified recovery point and its parent (composite)
        recovery point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/disassociate_recovery_point_from_parent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#disassociate_recovery_point_from_parent)
        """

    def export_backup_plan_template(
        self, **kwargs: Unpack[ExportBackupPlanTemplateInputTypeDef]
    ) -> ExportBackupPlanTemplateOutputTypeDef:
        """
        Returns the backup plan that is specified by the plan ID as a backup template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/export_backup_plan_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#export_backup_plan_template)
        """

    def get_backup_plan(
        self, **kwargs: Unpack[GetBackupPlanInputTypeDef]
    ) -> GetBackupPlanOutputTypeDef:
        """
        Returns <code>BackupPlan</code> details for the specified
        <code>BackupPlanId</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_backup_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_backup_plan)
        """

    def get_backup_plan_from_json(
        self, **kwargs: Unpack[GetBackupPlanFromJSONInputTypeDef]
    ) -> GetBackupPlanFromJSONOutputTypeDef:
        """
        Returns a valid JSON document specifying a backup plan or an error.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_backup_plan_from_json.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_backup_plan_from_json)
        """

    def get_backup_plan_from_template(
        self, **kwargs: Unpack[GetBackupPlanFromTemplateInputTypeDef]
    ) -> GetBackupPlanFromTemplateOutputTypeDef:
        """
        Returns the template specified by its <code>templateId</code> as a backup plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_backup_plan_from_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_backup_plan_from_template)
        """

    def get_backup_selection(
        self, **kwargs: Unpack[GetBackupSelectionInputTypeDef]
    ) -> GetBackupSelectionOutputTypeDef:
        """
        Returns selection metadata and a document in JSON format that specifies a list
        of resources that are associated with a backup plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_backup_selection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_backup_selection)
        """

    def get_backup_vault_access_policy(
        self, **kwargs: Unpack[GetBackupVaultAccessPolicyInputTypeDef]
    ) -> GetBackupVaultAccessPolicyOutputTypeDef:
        """
        Returns the access policy document that is associated with the named backup
        vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_backup_vault_access_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_backup_vault_access_policy)
        """

    def get_backup_vault_notifications(
        self, **kwargs: Unpack[GetBackupVaultNotificationsInputTypeDef]
    ) -> GetBackupVaultNotificationsOutputTypeDef:
        """
        Returns event notifications for the specified backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_backup_vault_notifications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_backup_vault_notifications)
        """

    def get_legal_hold(
        self, **kwargs: Unpack[GetLegalHoldInputTypeDef]
    ) -> GetLegalHoldOutputTypeDef:
        """
        This action returns details for a specified legal hold.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_legal_hold.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_legal_hold)
        """

    def get_recovery_point_index_details(
        self, **kwargs: Unpack[GetRecoveryPointIndexDetailsInputTypeDef]
    ) -> GetRecoveryPointIndexDetailsOutputTypeDef:
        """
        This operation returns the metadata and details specific to the backup index
        associated with the specified recovery point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_recovery_point_index_details.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_recovery_point_index_details)
        """

    def get_recovery_point_restore_metadata(
        self, **kwargs: Unpack[GetRecoveryPointRestoreMetadataInputTypeDef]
    ) -> GetRecoveryPointRestoreMetadataOutputTypeDef:
        """
        Returns a set of metadata key-value pairs that were used to create the backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_recovery_point_restore_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_recovery_point_restore_metadata)
        """

    def get_restore_job_metadata(
        self, **kwargs: Unpack[GetRestoreJobMetadataInputTypeDef]
    ) -> GetRestoreJobMetadataOutputTypeDef:
        """
        This request returns the metadata for the specified restore job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_restore_job_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_restore_job_metadata)
        """

    def get_restore_testing_inferred_metadata(
        self, **kwargs: Unpack[GetRestoreTestingInferredMetadataInputTypeDef]
    ) -> GetRestoreTestingInferredMetadataOutputTypeDef:
        """
        This request returns the minimal required set of metadata needed to start a
        restore job with secure default settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_restore_testing_inferred_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_restore_testing_inferred_metadata)
        """

    def get_restore_testing_plan(
        self, **kwargs: Unpack[GetRestoreTestingPlanInputTypeDef]
    ) -> GetRestoreTestingPlanOutputTypeDef:
        """
        Returns <code>RestoreTestingPlan</code> details for the specified
        <code>RestoreTestingPlanName</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_restore_testing_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_restore_testing_plan)
        """

    def get_restore_testing_selection(
        self, **kwargs: Unpack[GetRestoreTestingSelectionInputTypeDef]
    ) -> GetRestoreTestingSelectionOutputTypeDef:
        """
        Returns RestoreTestingSelection, which displays resources and elements of the
        restore testing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_restore_testing_selection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_restore_testing_selection)
        """

    def get_supported_resource_types(self) -> GetSupportedResourceTypesOutputTypeDef:
        """
        Returns the Amazon Web Services resource types supported by Backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_supported_resource_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_supported_resource_types)
        """

    def list_backup_job_summaries(
        self, **kwargs: Unpack[ListBackupJobSummariesInputTypeDef]
    ) -> ListBackupJobSummariesOutputTypeDef:
        """
        This is a request for a summary of backup jobs created or running within the
        most recent 30 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_backup_job_summaries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_backup_job_summaries)
        """

    def list_backup_jobs(
        self, **kwargs: Unpack[ListBackupJobsInputTypeDef]
    ) -> ListBackupJobsOutputTypeDef:
        """
        Returns a list of existing backup jobs for an authenticated account for the
        last 30 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_backup_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_backup_jobs)
        """

    def list_backup_plan_templates(
        self, **kwargs: Unpack[ListBackupPlanTemplatesInputTypeDef]
    ) -> ListBackupPlanTemplatesOutputTypeDef:
        """
        Lists the backup plan templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_backup_plan_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_backup_plan_templates)
        """

    def list_backup_plan_versions(
        self, **kwargs: Unpack[ListBackupPlanVersionsInputTypeDef]
    ) -> ListBackupPlanVersionsOutputTypeDef:
        """
        Returns version metadata of your backup plans, including Amazon Resource Names
        (ARNs), backup plan IDs, creation and deletion dates, plan names, and version
        IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_backup_plan_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_backup_plan_versions)
        """

    def list_backup_plans(
        self, **kwargs: Unpack[ListBackupPlansInputTypeDef]
    ) -> ListBackupPlansOutputTypeDef:
        """
        Lists the active backup plans for the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_backup_plans.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_backup_plans)
        """

    def list_backup_selections(
        self, **kwargs: Unpack[ListBackupSelectionsInputTypeDef]
    ) -> ListBackupSelectionsOutputTypeDef:
        """
        Returns an array containing metadata of the resources associated with the
        target backup plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_backup_selections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_backup_selections)
        """

    def list_backup_vaults(
        self, **kwargs: Unpack[ListBackupVaultsInputTypeDef]
    ) -> ListBackupVaultsOutputTypeDef:
        """
        Returns a list of recovery point storage containers along with information
        about them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_backup_vaults.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_backup_vaults)
        """

    def list_copy_job_summaries(
        self, **kwargs: Unpack[ListCopyJobSummariesInputTypeDef]
    ) -> ListCopyJobSummariesOutputTypeDef:
        """
        This request obtains a list of copy jobs created or running within the the most
        recent 30 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_copy_job_summaries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_copy_job_summaries)
        """

    def list_copy_jobs(
        self, **kwargs: Unpack[ListCopyJobsInputTypeDef]
    ) -> ListCopyJobsOutputTypeDef:
        """
        Returns metadata about your copy jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_copy_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_copy_jobs)
        """

    def list_frameworks(
        self, **kwargs: Unpack[ListFrameworksInputTypeDef]
    ) -> ListFrameworksOutputTypeDef:
        """
        Returns a list of all frameworks for an Amazon Web Services account and Amazon
        Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_frameworks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_frameworks)
        """

    def list_indexed_recovery_points(
        self, **kwargs: Unpack[ListIndexedRecoveryPointsInputTypeDef]
    ) -> ListIndexedRecoveryPointsOutputTypeDef:
        """
        This operation returns a list of recovery points that have an associated index,
        belonging to the specified account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_indexed_recovery_points.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_indexed_recovery_points)
        """

    def list_legal_holds(
        self, **kwargs: Unpack[ListLegalHoldsInputTypeDef]
    ) -> ListLegalHoldsOutputTypeDef:
        """
        This action returns metadata about active and previous legal holds.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_legal_holds.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_legal_holds)
        """

    def list_protected_resources(
        self, **kwargs: Unpack[ListProtectedResourcesInputTypeDef]
    ) -> ListProtectedResourcesOutputTypeDef:
        """
        Returns an array of resources successfully backed up by Backup, including the
        time the resource was saved, an Amazon Resource Name (ARN) of the resource, and
        a resource type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_protected_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_protected_resources)
        """

    def list_protected_resources_by_backup_vault(
        self, **kwargs: Unpack[ListProtectedResourcesByBackupVaultInputTypeDef]
    ) -> ListProtectedResourcesByBackupVaultOutputTypeDef:
        """
        This request lists the protected resources corresponding to each backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_protected_resources_by_backup_vault.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_protected_resources_by_backup_vault)
        """

    def list_recovery_points_by_backup_vault(
        self, **kwargs: Unpack[ListRecoveryPointsByBackupVaultInputTypeDef]
    ) -> ListRecoveryPointsByBackupVaultOutputTypeDef:
        """
        Returns detailed information about the recovery points stored in a backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_recovery_points_by_backup_vault.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_recovery_points_by_backup_vault)
        """

    def list_recovery_points_by_legal_hold(
        self, **kwargs: Unpack[ListRecoveryPointsByLegalHoldInputTypeDef]
    ) -> ListRecoveryPointsByLegalHoldOutputTypeDef:
        """
        This action returns recovery point ARNs (Amazon Resource Names) of the
        specified legal hold.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_recovery_points_by_legal_hold.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_recovery_points_by_legal_hold)
        """

    def list_recovery_points_by_resource(
        self, **kwargs: Unpack[ListRecoveryPointsByResourceInputTypeDef]
    ) -> ListRecoveryPointsByResourceOutputTypeDef:
        """
        The information about the recovery points of the type specified by a resource
        Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_recovery_points_by_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_recovery_points_by_resource)
        """

    def list_report_jobs(
        self, **kwargs: Unpack[ListReportJobsInputTypeDef]
    ) -> ListReportJobsOutputTypeDef:
        """
        Returns details about your report jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_report_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_report_jobs)
        """

    def list_report_plans(
        self, **kwargs: Unpack[ListReportPlansInputTypeDef]
    ) -> ListReportPlansOutputTypeDef:
        """
        Returns a list of your report plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_report_plans.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_report_plans)
        """

    def list_restore_job_summaries(
        self, **kwargs: Unpack[ListRestoreJobSummariesInputTypeDef]
    ) -> ListRestoreJobSummariesOutputTypeDef:
        """
        This request obtains a summary of restore jobs created or running within the
        the most recent 30 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_restore_job_summaries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_restore_job_summaries)
        """

    def list_restore_jobs(
        self, **kwargs: Unpack[ListRestoreJobsInputTypeDef]
    ) -> ListRestoreJobsOutputTypeDef:
        """
        Returns a list of jobs that Backup initiated to restore a saved resource,
        including details about the recovery process.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_restore_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_restore_jobs)
        """

    def list_restore_jobs_by_protected_resource(
        self, **kwargs: Unpack[ListRestoreJobsByProtectedResourceInputTypeDef]
    ) -> ListRestoreJobsByProtectedResourceOutputTypeDef:
        """
        This returns restore jobs that contain the specified protected resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_restore_jobs_by_protected_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_restore_jobs_by_protected_resource)
        """

    def list_restore_testing_plans(
        self, **kwargs: Unpack[ListRestoreTestingPlansInputTypeDef]
    ) -> ListRestoreTestingPlansOutputTypeDef:
        """
        Returns a list of restore testing plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_restore_testing_plans.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_restore_testing_plans)
        """

    def list_restore_testing_selections(
        self, **kwargs: Unpack[ListRestoreTestingSelectionsInputTypeDef]
    ) -> ListRestoreTestingSelectionsOutputTypeDef:
        """
        Returns a list of restore testing selections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_restore_testing_selections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_restore_testing_selections)
        """

    def list_tags(self, **kwargs: Unpack[ListTagsInputTypeDef]) -> ListTagsOutputTypeDef:
        """
        Returns the tags assigned to the resource, such as a target recovery point,
        backup plan, or backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/list_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#list_tags)
        """

    def put_backup_vault_access_policy(
        self, **kwargs: Unpack[PutBackupVaultAccessPolicyInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sets a resource-based policy that is used to manage access permissions on the
        target backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/put_backup_vault_access_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#put_backup_vault_access_policy)
        """

    def put_backup_vault_lock_configuration(
        self, **kwargs: Unpack[PutBackupVaultLockConfigurationInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Applies Backup Vault Lock to a backup vault, preventing attempts to delete any
        recovery point stored in or created in a backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/put_backup_vault_lock_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#put_backup_vault_lock_configuration)
        """

    def put_backup_vault_notifications(
        self, **kwargs: Unpack[PutBackupVaultNotificationsInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Turns on notifications on a backup vault for the specified topic and events.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/put_backup_vault_notifications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#put_backup_vault_notifications)
        """

    def put_restore_validation_result(
        self, **kwargs: Unpack[PutRestoreValidationResultInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This request allows you to send your independent self-run restore test
        validation results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/put_restore_validation_result.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#put_restore_validation_result)
        """

    def start_backup_job(
        self, **kwargs: Unpack[StartBackupJobInputTypeDef]
    ) -> StartBackupJobOutputTypeDef:
        """
        Starts an on-demand backup job for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/start_backup_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#start_backup_job)
        """

    def start_copy_job(
        self, **kwargs: Unpack[StartCopyJobInputTypeDef]
    ) -> StartCopyJobOutputTypeDef:
        """
        Starts a job to create a one-time copy of the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/start_copy_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#start_copy_job)
        """

    def start_report_job(
        self, **kwargs: Unpack[StartReportJobInputTypeDef]
    ) -> StartReportJobOutputTypeDef:
        """
        Starts an on-demand report job for the specified report plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/start_report_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#start_report_job)
        """

    def start_restore_job(
        self, **kwargs: Unpack[StartRestoreJobInputTypeDef]
    ) -> StartRestoreJobOutputTypeDef:
        """
        Recovers the saved resource identified by an Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/start_restore_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#start_restore_job)
        """

    def stop_backup_job(
        self, **kwargs: Unpack[StopBackupJobInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Attempts to cancel a job to create a one-time backup of a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/stop_backup_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#stop_backup_job)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Assigns a set of key-value pairs to a recovery point, backup plan, or backup
        vault identified by an Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes a set of key-value pairs from a recovery point, backup plan, or backup
        vault identified by an Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#untag_resource)
        """

    def update_backup_plan(
        self, **kwargs: Unpack[UpdateBackupPlanInputTypeDef]
    ) -> UpdateBackupPlanOutputTypeDef:
        """
        Updates the specified backup plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/update_backup_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#update_backup_plan)
        """

    def update_framework(
        self, **kwargs: Unpack[UpdateFrameworkInputTypeDef]
    ) -> UpdateFrameworkOutputTypeDef:
        """
        Updates the specified framework.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/update_framework.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#update_framework)
        """

    def update_global_settings(
        self, **kwargs: Unpack[UpdateGlobalSettingsInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates whether the Amazon Web Services account is opted in to cross-account
        backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/update_global_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#update_global_settings)
        """

    def update_recovery_point_index_settings(
        self, **kwargs: Unpack[UpdateRecoveryPointIndexSettingsInputTypeDef]
    ) -> UpdateRecoveryPointIndexSettingsOutputTypeDef:
        """
        This operation updates the settings of a recovery point index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/update_recovery_point_index_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#update_recovery_point_index_settings)
        """

    def update_recovery_point_lifecycle(
        self, **kwargs: Unpack[UpdateRecoveryPointLifecycleInputTypeDef]
    ) -> UpdateRecoveryPointLifecycleOutputTypeDef:
        """
        Sets the transition lifecycle of a recovery point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/update_recovery_point_lifecycle.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#update_recovery_point_lifecycle)
        """

    def update_region_settings(
        self, **kwargs: Unpack[UpdateRegionSettingsInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the current service opt-in settings for the Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/update_region_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#update_region_settings)
        """

    def update_report_plan(
        self, **kwargs: Unpack[UpdateReportPlanInputTypeDef]
    ) -> UpdateReportPlanOutputTypeDef:
        """
        Updates the specified report plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/update_report_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#update_report_plan)
        """

    def update_restore_testing_plan(
        self, **kwargs: Unpack[UpdateRestoreTestingPlanInputTypeDef]
    ) -> UpdateRestoreTestingPlanOutputTypeDef:
        """
        This request will send changes to your specified restore testing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/update_restore_testing_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#update_restore_testing_plan)
        """

    def update_restore_testing_selection(
        self, **kwargs: Unpack[UpdateRestoreTestingSelectionInputTypeDef]
    ) -> UpdateRestoreTestingSelectionOutputTypeDef:
        """
        Updates the specified restore testing selection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/update_restore_testing_selection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#update_restore_testing_selection)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_backup_jobs"]
    ) -> ListBackupJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_backup_plan_templates"]
    ) -> ListBackupPlanTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_backup_plan_versions"]
    ) -> ListBackupPlanVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_backup_plans"]
    ) -> ListBackupPlansPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_backup_selections"]
    ) -> ListBackupSelectionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_backup_vaults"]
    ) -> ListBackupVaultsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_copy_jobs"]
    ) -> ListCopyJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_indexed_recovery_points"]
    ) -> ListIndexedRecoveryPointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_legal_holds"]
    ) -> ListLegalHoldsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_protected_resources_by_backup_vault"]
    ) -> ListProtectedResourcesByBackupVaultPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_protected_resources"]
    ) -> ListProtectedResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_recovery_points_by_backup_vault"]
    ) -> ListRecoveryPointsByBackupVaultPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_recovery_points_by_legal_hold"]
    ) -> ListRecoveryPointsByLegalHoldPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_recovery_points_by_resource"]
    ) -> ListRecoveryPointsByResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_restore_jobs_by_protected_resource"]
    ) -> ListRestoreJobsByProtectedResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_restore_jobs"]
    ) -> ListRestoreJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_restore_testing_plans"]
    ) -> ListRestoreTestingPlansPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_restore_testing_selections"]
    ) -> ListRestoreTestingSelectionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/client/#get_paginator)
        """
