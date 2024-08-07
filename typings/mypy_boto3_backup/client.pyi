"""
Type annotations for backup service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_backup import BackupClient

    client: BackupClient = boto3.client("backup")
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AggregationPeriodType,
    BackupJobStateType,
    BackupJobStatusType,
    BackupVaultEventType,
    CopyJobStateType,
    CopyJobStatusType,
    RestoreJobStateType,
    RestoreJobStatusType,
    RestoreValidationStatusType,
    VaultTypeType,
)
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
    ListRestoreJobsByProtectedResourcePaginator,
    ListRestoreJobsPaginator,
    ListRestoreTestingPlansPaginator,
    ListRestoreTestingSelectionsPaginator,
)
from .type_defs import (
    BackupPlanInputTypeDef,
    BackupSelectionTypeDef,
    CreateBackupPlanOutputTypeDef,
    CreateBackupSelectionOutputTypeDef,
    CreateBackupVaultOutputTypeDef,
    CreateFrameworkOutputTypeDef,
    CreateLegalHoldOutputTypeDef,
    CreateLogicallyAirGappedBackupVaultOutputTypeDef,
    CreateReportPlanOutputTypeDef,
    CreateRestoreTestingPlanOutputTypeDef,
    CreateRestoreTestingSelectionOutputTypeDef,
    DeleteBackupPlanOutputTypeDef,
    DescribeBackupJobOutputTypeDef,
    DescribeBackupVaultOutputTypeDef,
    DescribeCopyJobOutputTypeDef,
    DescribeFrameworkOutputTypeDef,
    DescribeGlobalSettingsOutputTypeDef,
    DescribeProtectedResourceOutputTypeDef,
    DescribeRecoveryPointOutputTypeDef,
    DescribeRegionSettingsOutputTypeDef,
    DescribeReportJobOutputTypeDef,
    DescribeReportPlanOutputTypeDef,
    DescribeRestoreJobOutputTypeDef,
    ExportBackupPlanTemplateOutputTypeDef,
    FrameworkControlTypeDef,
    GetBackupPlanFromJSONOutputTypeDef,
    GetBackupPlanFromTemplateOutputTypeDef,
    GetBackupPlanOutputTypeDef,
    GetBackupSelectionOutputTypeDef,
    GetBackupVaultAccessPolicyOutputTypeDef,
    GetBackupVaultNotificationsOutputTypeDef,
    GetLegalHoldOutputTypeDef,
    GetRecoveryPointRestoreMetadataOutputTypeDef,
    GetRestoreJobMetadataOutputTypeDef,
    GetRestoreTestingInferredMetadataOutputTypeDef,
    GetRestoreTestingPlanOutputTypeDef,
    GetRestoreTestingSelectionOutputTypeDef,
    GetSupportedResourceTypesOutputTypeDef,
    LifecycleTypeDef,
    ListBackupJobsOutputTypeDef,
    ListBackupJobSummariesOutputTypeDef,
    ListBackupPlansOutputTypeDef,
    ListBackupPlanTemplatesOutputTypeDef,
    ListBackupPlanVersionsOutputTypeDef,
    ListBackupSelectionsOutputTypeDef,
    ListBackupVaultsOutputTypeDef,
    ListCopyJobsOutputTypeDef,
    ListCopyJobSummariesOutputTypeDef,
    ListFrameworksOutputTypeDef,
    ListLegalHoldsOutputTypeDef,
    ListProtectedResourcesByBackupVaultOutputTypeDef,
    ListProtectedResourcesOutputTypeDef,
    ListRecoveryPointsByBackupVaultOutputTypeDef,
    ListRecoveryPointsByLegalHoldOutputTypeDef,
    ListRecoveryPointsByResourceOutputTypeDef,
    ListReportJobsOutputTypeDef,
    ListReportPlansOutputTypeDef,
    ListRestoreJobsByProtectedResourceOutputTypeDef,
    ListRestoreJobsOutputTypeDef,
    ListRestoreJobSummariesOutputTypeDef,
    ListRestoreTestingPlansOutputTypeDef,
    ListRestoreTestingSelectionsOutputTypeDef,
    ListTagsOutputTypeDef,
    RecoveryPointSelectionTypeDef,
    ReportDeliveryChannelTypeDef,
    ReportSettingTypeDef,
    RestoreTestingPlanForCreateTypeDef,
    RestoreTestingPlanForUpdateTypeDef,
    RestoreTestingSelectionForCreateTypeDef,
    RestoreTestingSelectionForUpdateTypeDef,
    StartBackupJobOutputTypeDef,
    StartCopyJobOutputTypeDef,
    StartReportJobOutputTypeDef,
    StartRestoreJobOutputTypeDef,
    UpdateBackupPlanOutputTypeDef,
    UpdateFrameworkOutputTypeDef,
    UpdateRecoveryPointLifecycleOutputTypeDef,
    UpdateReportPlanOutputTypeDef,
    UpdateRestoreTestingPlanOutputTypeDef,
    UpdateRestoreTestingSelectionOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("BackupClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BackupClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#can_paginate)
        """

    def cancel_legal_hold(
        self, *, LegalHoldId: str, CancelDescription: str, RetainRecordInDays: int = None
    ) -> Dict[str, Any]:
        """
        This action removes the specified legal hold on a recovery point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.cancel_legal_hold)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#cancel_legal_hold)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#close)
        """

    def create_backup_plan(
        self,
        *,
        BackupPlan: "BackupPlanInputTypeDef",
        BackupPlanTags: Dict[str, str] = None,
        CreatorRequestId: str = None
    ) -> CreateBackupPlanOutputTypeDef:
        """
        Creates a backup plan using a backup plan name and backup rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.create_backup_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#create_backup_plan)
        """

    def create_backup_selection(
        self,
        *,
        BackupPlanId: str,
        BackupSelection: "BackupSelectionTypeDef",
        CreatorRequestId: str = None
    ) -> CreateBackupSelectionOutputTypeDef:
        """
        Creates a JSON document that specifies a set of resources to assign to a backup
        plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.create_backup_selection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#create_backup_selection)
        """

    def create_backup_vault(
        self,
        *,
        BackupVaultName: str,
        BackupVaultTags: Dict[str, str] = None,
        EncryptionKeyArn: str = None,
        CreatorRequestId: str = None
    ) -> CreateBackupVaultOutputTypeDef:
        """
        Creates a logical container where backups are stored.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.create_backup_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#create_backup_vault)
        """

    def create_framework(
        self,
        *,
        FrameworkName: str,
        FrameworkControls: List["FrameworkControlTypeDef"],
        FrameworkDescription: str = None,
        IdempotencyToken: str = None,
        FrameworkTags: Dict[str, str] = None
    ) -> CreateFrameworkOutputTypeDef:
        """
        Creates a framework with one or more controls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.create_framework)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#create_framework)
        """

    def create_legal_hold(
        self,
        *,
        Title: str,
        Description: str,
        IdempotencyToken: str = None,
        RecoveryPointSelection: "RecoveryPointSelectionTypeDef" = None,
        Tags: Dict[str, str] = None
    ) -> CreateLegalHoldOutputTypeDef:
        """
        This action creates a legal hold on a recovery point (backup).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.create_legal_hold)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#create_legal_hold)
        """

    def create_logically_air_gapped_backup_vault(
        self,
        *,
        BackupVaultName: str,
        MinRetentionDays: int,
        MaxRetentionDays: int,
        BackupVaultTags: Dict[str, str] = None,
        CreatorRequestId: str = None
    ) -> CreateLogicallyAirGappedBackupVaultOutputTypeDef:
        """
        This request creates a logical container to where backups may be copied.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.create_logically_air_gapped_backup_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#create_logically_air_gapped_backup_vault)
        """

    def create_report_plan(
        self,
        *,
        ReportPlanName: str,
        ReportDeliveryChannel: "ReportDeliveryChannelTypeDef",
        ReportSetting: "ReportSettingTypeDef",
        ReportPlanDescription: str = None,
        ReportPlanTags: Dict[str, str] = None,
        IdempotencyToken: str = None
    ) -> CreateReportPlanOutputTypeDef:
        """
        Creates a report plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.create_report_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#create_report_plan)
        """

    def create_restore_testing_plan(
        self,
        *,
        RestoreTestingPlan: "RestoreTestingPlanForCreateTypeDef",
        CreatorRequestId: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateRestoreTestingPlanOutputTypeDef:
        """
        This is the first of two steps to create a restore testing plan; once this
        request is successful, finish the procedure with request
        CreateRestoreTestingSelection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.create_restore_testing_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#create_restore_testing_plan)
        """

    def create_restore_testing_selection(
        self,
        *,
        RestoreTestingPlanName: str,
        RestoreTestingSelection: "RestoreTestingSelectionForCreateTypeDef",
        CreatorRequestId: str = None
    ) -> CreateRestoreTestingSelectionOutputTypeDef:
        """
        This request can be sent after CreateRestoreTestingPlan request returns
        successfully.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.create_restore_testing_selection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#create_restore_testing_selection)
        """

    def delete_backup_plan(self, *, BackupPlanId: str) -> DeleteBackupPlanOutputTypeDef:
        """
        Deletes a backup plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.delete_backup_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete_backup_plan)
        """

    def delete_backup_selection(self, *, BackupPlanId: str, SelectionId: str) -> None:
        """
        Deletes the resource selection associated with a backup plan that is specified
        by the `SelectionId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.delete_backup_selection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete_backup_selection)
        """

    def delete_backup_vault(self, *, BackupVaultName: str) -> None:
        """
        Deletes the backup vault identified by its name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.delete_backup_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete_backup_vault)
        """

    def delete_backup_vault_access_policy(self, *, BackupVaultName: str) -> None:
        """
        Deletes the policy document that manages permissions on a backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.delete_backup_vault_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete_backup_vault_access_policy)
        """

    def delete_backup_vault_lock_configuration(self, *, BackupVaultName: str) -> None:
        """
        Deletes Backup Vault Lock from a backup vault specified by a backup vault name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.delete_backup_vault_lock_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete_backup_vault_lock_configuration)
        """

    def delete_backup_vault_notifications(self, *, BackupVaultName: str) -> None:
        """
        Deletes event notifications for the specified backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.delete_backup_vault_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete_backup_vault_notifications)
        """

    def delete_framework(self, *, FrameworkName: str) -> None:
        """
        Deletes the framework specified by a framework name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.delete_framework)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete_framework)
        """

    def delete_recovery_point(self, *, BackupVaultName: str, RecoveryPointArn: str) -> None:
        """
        Deletes the recovery point specified by a recovery point ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.delete_recovery_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete_recovery_point)
        """

    def delete_report_plan(self, *, ReportPlanName: str) -> None:
        """
        Deletes the report plan specified by a report plan name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.delete_report_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete_report_plan)
        """

    def delete_restore_testing_plan(self, *, RestoreTestingPlanName: str) -> None:
        """
        This request deletes the specified restore testing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.delete_restore_testing_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete_restore_testing_plan)
        """

    def delete_restore_testing_selection(
        self, *, RestoreTestingPlanName: str, RestoreTestingSelectionName: str
    ) -> None:
        """
        Input the Restore Testing Plan name and Restore Testing Selection name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.delete_restore_testing_selection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete_restore_testing_selection)
        """

    def describe_backup_job(self, *, BackupJobId: str) -> DescribeBackupJobOutputTypeDef:
        """
        Returns backup job details for the specified `BackupJobId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.describe_backup_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe_backup_job)
        """

    def describe_backup_vault(
        self, *, BackupVaultName: str, BackupVaultAccountId: str = None
    ) -> DescribeBackupVaultOutputTypeDef:
        """
        Returns metadata about a backup vault specified by its name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.describe_backup_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe_backup_vault)
        """

    def describe_copy_job(self, *, CopyJobId: str) -> DescribeCopyJobOutputTypeDef:
        """
        Returns metadata associated with creating a copy of a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.describe_copy_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe_copy_job)
        """

    def describe_framework(self, *, FrameworkName: str) -> DescribeFrameworkOutputTypeDef:
        """
        Returns the framework details for the specified `FrameworkName`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.describe_framework)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe_framework)
        """

    def describe_global_settings(self) -> DescribeGlobalSettingsOutputTypeDef:
        """
        Describes whether the Amazon Web Services account is opted in to cross-account
        backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.describe_global_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe_global_settings)
        """

    def describe_protected_resource(
        self, *, ResourceArn: str
    ) -> DescribeProtectedResourceOutputTypeDef:
        """
        Returns information about a saved resource, including the last time it was
        backed up, its Amazon Resource Name (ARN), and the Amazon Web Services service
        type of the saved resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.describe_protected_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe_protected_resource)
        """

    def describe_recovery_point(
        self, *, BackupVaultName: str, RecoveryPointArn: str, BackupVaultAccountId: str = None
    ) -> DescribeRecoveryPointOutputTypeDef:
        """
        Returns metadata associated with a recovery point, including ID, status,
        encryption, and lifecycle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.describe_recovery_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe_recovery_point)
        """

    def describe_region_settings(self) -> DescribeRegionSettingsOutputTypeDef:
        """
        Returns the current service opt-in settings for the Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.describe_region_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe_region_settings)
        """

    def describe_report_job(self, *, ReportJobId: str) -> DescribeReportJobOutputTypeDef:
        """
        Returns the details associated with creating a report as specified by its
        `ReportJobId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.describe_report_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe_report_job)
        """

    def describe_report_plan(self, *, ReportPlanName: str) -> DescribeReportPlanOutputTypeDef:
        """
        Returns a list of all report plans for an Amazon Web Services account and Amazon
        Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.describe_report_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe_report_plan)
        """

    def describe_restore_job(self, *, RestoreJobId: str) -> DescribeRestoreJobOutputTypeDef:
        """
        Returns metadata associated with a restore job that is specified by a job ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.describe_restore_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe_restore_job)
        """

    def disassociate_recovery_point(self, *, BackupVaultName: str, RecoveryPointArn: str) -> None:
        """
        Deletes the specified continuous backup recovery point from Backup and releases
        control of that continuous backup to the source service, such as Amazon RDS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.disassociate_recovery_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#disassociate_recovery_point)
        """

    def disassociate_recovery_point_from_parent(
        self, *, BackupVaultName: str, RecoveryPointArn: str
    ) -> None:
        """
        This action to a specific child (nested) recovery point removes the relationship
        between the specified recovery point and its parent (composite) recovery point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.disassociate_recovery_point_from_parent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#disassociate_recovery_point_from_parent)
        """

    def export_backup_plan_template(
        self, *, BackupPlanId: str
    ) -> ExportBackupPlanTemplateOutputTypeDef:
        """
        Returns the backup plan that is specified by the plan ID as a backup template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.export_backup_plan_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#export_backup_plan_template)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#generate_presigned_url)
        """

    def get_backup_plan(
        self, *, BackupPlanId: str, VersionId: str = None
    ) -> GetBackupPlanOutputTypeDef:
        """
        Returns `BackupPlan` details for the specified `BackupPlanId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.get_backup_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_backup_plan)
        """

    def get_backup_plan_from_json(
        self, *, BackupPlanTemplateJson: str
    ) -> GetBackupPlanFromJSONOutputTypeDef:
        """
        Returns a valid JSON document specifying a backup plan or an error.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.get_backup_plan_from_json)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_backup_plan_from_json)
        """

    def get_backup_plan_from_template(
        self, *, BackupPlanTemplateId: str
    ) -> GetBackupPlanFromTemplateOutputTypeDef:
        """
        Returns the template specified by its `templateId` as a backup plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.get_backup_plan_from_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_backup_plan_from_template)
        """

    def get_backup_selection(
        self, *, BackupPlanId: str, SelectionId: str
    ) -> GetBackupSelectionOutputTypeDef:
        """
        Returns selection metadata and a document in JSON format that specifies a list
        of resources that are associated with a backup plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.get_backup_selection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_backup_selection)
        """

    def get_backup_vault_access_policy(
        self, *, BackupVaultName: str
    ) -> GetBackupVaultAccessPolicyOutputTypeDef:
        """
        Returns the access policy document that is associated with the named backup
        vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.get_backup_vault_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_backup_vault_access_policy)
        """

    def get_backup_vault_notifications(
        self, *, BackupVaultName: str
    ) -> GetBackupVaultNotificationsOutputTypeDef:
        """
        Returns event notifications for the specified backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.get_backup_vault_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_backup_vault_notifications)
        """

    def get_legal_hold(self, *, LegalHoldId: str) -> GetLegalHoldOutputTypeDef:
        """
        This action returns details for a specified legal hold.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.get_legal_hold)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_legal_hold)
        """

    def get_recovery_point_restore_metadata(
        self, *, BackupVaultName: str, RecoveryPointArn: str, BackupVaultAccountId: str = None
    ) -> GetRecoveryPointRestoreMetadataOutputTypeDef:
        """
        Returns a set of metadata key-value pairs that were used to create the backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.get_recovery_point_restore_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_recovery_point_restore_metadata)
        """

    def get_restore_job_metadata(self, *, RestoreJobId: str) -> GetRestoreJobMetadataOutputTypeDef:
        """
        This request returns the metadata for the specified restore job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.get_restore_job_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_restore_job_metadata)
        """

    def get_restore_testing_inferred_metadata(
        self, *, BackupVaultName: str, RecoveryPointArn: str, BackupVaultAccountId: str = None
    ) -> GetRestoreTestingInferredMetadataOutputTypeDef:
        """
        This request returns the minimal required set of metadata needed to start a
        restore job with secure default settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.get_restore_testing_inferred_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_restore_testing_inferred_metadata)
        """

    def get_restore_testing_plan(
        self, *, RestoreTestingPlanName: str
    ) -> GetRestoreTestingPlanOutputTypeDef:
        """
        Returns `RestoreTestingPlan` details for the specified `RestoreTestingPlanName`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.get_restore_testing_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_restore_testing_plan)
        """

    def get_restore_testing_selection(
        self, *, RestoreTestingPlanName: str, RestoreTestingSelectionName: str
    ) -> GetRestoreTestingSelectionOutputTypeDef:
        """
        Returns RestoreTestingSelection, which displays resources and elements of the
        restore testing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.get_restore_testing_selection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_restore_testing_selection)
        """

    def get_supported_resource_types(self) -> GetSupportedResourceTypesOutputTypeDef:
        """
        Returns the Amazon Web Services resource types supported by Backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.get_supported_resource_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_supported_resource_types)
        """

    def list_backup_job_summaries(
        self,
        *,
        AccountId: str = None,
        State: BackupJobStatusType = None,
        ResourceType: str = None,
        MessageCategory: str = None,
        AggregationPeriod: AggregationPeriodType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListBackupJobSummariesOutputTypeDef:
        """
        This is a request for a summary of backup jobs created or running within the
        most recent 30 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_backup_job_summaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_backup_job_summaries)
        """

    def list_backup_jobs(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
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
        ByMessageCategory: str = None
    ) -> ListBackupJobsOutputTypeDef:
        """
        Returns a list of existing backup jobs for an authenticated account for the last
        30 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_backup_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_backup_jobs)
        """

    def list_backup_plan_templates(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListBackupPlanTemplatesOutputTypeDef:
        """
        Returns metadata of your saved backup plan templates, including the template ID,
        name, and the creation and deletion dates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_backup_plan_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_backup_plan_templates)
        """

    def list_backup_plan_versions(
        self, *, BackupPlanId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListBackupPlanVersionsOutputTypeDef:
        """
        Returns version metadata of your backup plans, including Amazon Resource Names
        (ARNs), backup plan IDs, creation and deletion dates, plan names, and version
        IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_backup_plan_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_backup_plan_versions)
        """

    def list_backup_plans(
        self, *, NextToken: str = None, MaxResults: int = None, IncludeDeleted: bool = None
    ) -> ListBackupPlansOutputTypeDef:
        """
        Returns a list of all active backup plans for an authenticated account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_backup_plans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_backup_plans)
        """

    def list_backup_selections(
        self, *, BackupPlanId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListBackupSelectionsOutputTypeDef:
        """
        Returns an array containing metadata of the resources associated with the target
        backup plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_backup_selections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_backup_selections)
        """

    def list_backup_vaults(
        self,
        *,
        ByVaultType: VaultTypeType = None,
        ByShared: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListBackupVaultsOutputTypeDef:
        """
        Returns a list of recovery point storage containers along with information about
        them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_backup_vaults)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_backup_vaults)
        """

    def list_copy_job_summaries(
        self,
        *,
        AccountId: str = None,
        State: CopyJobStatusType = None,
        ResourceType: str = None,
        MessageCategory: str = None,
        AggregationPeriod: AggregationPeriodType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListCopyJobSummariesOutputTypeDef:
        """
        This request obtains a list of copy jobs created or running within the the most
        recent 30 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_copy_job_summaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_copy_job_summaries)
        """

    def list_copy_jobs(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
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
        ByMessageCategory: str = None
    ) -> ListCopyJobsOutputTypeDef:
        """
        Returns metadata about your copy jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_copy_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_copy_jobs)
        """

    def list_frameworks(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListFrameworksOutputTypeDef:
        """
        Returns a list of all frameworks for an Amazon Web Services account and Amazon
        Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_frameworks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_frameworks)
        """

    def list_legal_holds(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListLegalHoldsOutputTypeDef:
        """
        This action returns metadata about active and previous legal holds.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_legal_holds)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_legal_holds)
        """

    def list_protected_resources(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListProtectedResourcesOutputTypeDef:
        """
        Returns an array of resources successfully backed up by Backup, including the
        time the resource was saved, an Amazon Resource Name (ARN) of the resource, and
        a resource type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_protected_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_protected_resources)
        """

    def list_protected_resources_by_backup_vault(
        self,
        *,
        BackupVaultName: str,
        BackupVaultAccountId: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListProtectedResourcesByBackupVaultOutputTypeDef:
        """
        This request lists the protected resources corresponding to each backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_protected_resources_by_backup_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_protected_resources_by_backup_vault)
        """

    def list_recovery_points_by_backup_vault(
        self,
        *,
        BackupVaultName: str,
        BackupVaultAccountId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        ByResourceArn: str = None,
        ByResourceType: str = None,
        ByBackupPlanId: str = None,
        ByCreatedBefore: Union[datetime, str] = None,
        ByCreatedAfter: Union[datetime, str] = None,
        ByParentRecoveryPointArn: str = None
    ) -> ListRecoveryPointsByBackupVaultOutputTypeDef:
        """
        Returns detailed information about the recovery points stored in a backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_recovery_points_by_backup_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_recovery_points_by_backup_vault)
        """

    def list_recovery_points_by_legal_hold(
        self, *, LegalHoldId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListRecoveryPointsByLegalHoldOutputTypeDef:
        """
        This action returns recovery point ARNs (Amazon Resource Names) of the specified
        legal hold.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_recovery_points_by_legal_hold)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_recovery_points_by_legal_hold)
        """

    def list_recovery_points_by_resource(
        self,
        *,
        ResourceArn: str,
        NextToken: str = None,
        MaxResults: int = None,
        ManagedByAWSBackupOnly: bool = None
    ) -> ListRecoveryPointsByResourceOutputTypeDef:
        """
        Returns detailed information about all the recovery points of the type specified
        by a resource Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_recovery_points_by_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_recovery_points_by_resource)
        """

    def list_report_jobs(
        self,
        *,
        ByReportPlanName: str = None,
        ByCreationBefore: Union[datetime, str] = None,
        ByCreationAfter: Union[datetime, str] = None,
        ByStatus: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListReportJobsOutputTypeDef:
        """
        Returns details about your report jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_report_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_report_jobs)
        """

    def list_report_plans(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListReportPlansOutputTypeDef:
        """
        Returns a list of your report plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_report_plans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_report_plans)
        """

    def list_restore_job_summaries(
        self,
        *,
        AccountId: str = None,
        State: RestoreJobStateType = None,
        ResourceType: str = None,
        AggregationPeriod: AggregationPeriodType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListRestoreJobSummariesOutputTypeDef:
        """
        This request obtains a summary of restore jobs created or running within the the
        most recent 30 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_restore_job_summaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_restore_job_summaries)
        """

    def list_restore_jobs(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        ByAccountId: str = None,
        ByResourceType: str = None,
        ByCreatedBefore: Union[datetime, str] = None,
        ByCreatedAfter: Union[datetime, str] = None,
        ByStatus: RestoreJobStatusType = None,
        ByCompleteBefore: Union[datetime, str] = None,
        ByCompleteAfter: Union[datetime, str] = None,
        ByRestoreTestingPlanArn: str = None
    ) -> ListRestoreJobsOutputTypeDef:
        """
        Returns a list of jobs that Backup initiated to restore a saved resource,
        including details about the recovery process.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_restore_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_restore_jobs)
        """

    def list_restore_jobs_by_protected_resource(
        self,
        *,
        ResourceArn: str,
        ByStatus: RestoreJobStatusType = None,
        ByRecoveryPointCreationDateAfter: Union[datetime, str] = None,
        ByRecoveryPointCreationDateBefore: Union[datetime, str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListRestoreJobsByProtectedResourceOutputTypeDef:
        """
        This returns restore jobs that contain the specified protected resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_restore_jobs_by_protected_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_restore_jobs_by_protected_resource)
        """

    def list_restore_testing_plans(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListRestoreTestingPlansOutputTypeDef:
        """
        Returns a list of restore testing plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_restore_testing_plans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_restore_testing_plans)
        """

    def list_restore_testing_selections(
        self, *, RestoreTestingPlanName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListRestoreTestingSelectionsOutputTypeDef:
        """
        Returns a list of restore testing selections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_restore_testing_selections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_restore_testing_selections)
        """

    def list_tags(
        self, *, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsOutputTypeDef:
        """
        Returns a list of key-value pairs assigned to a target recovery point, backup
        plan, or backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.list_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_tags)
        """

    def put_backup_vault_access_policy(self, *, BackupVaultName: str, Policy: str = None) -> None:
        """
        Sets a resource-based policy that is used to manage access permissions on the
        target backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.put_backup_vault_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#put_backup_vault_access_policy)
        """

    def put_backup_vault_lock_configuration(
        self,
        *,
        BackupVaultName: str,
        MinRetentionDays: int = None,
        MaxRetentionDays: int = None,
        ChangeableForDays: int = None
    ) -> None:
        """
        Applies Backup Vault Lock to a backup vault, preventing attempts to delete any
        recovery point stored in or created in a backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.put_backup_vault_lock_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#put_backup_vault_lock_configuration)
        """

    def put_backup_vault_notifications(
        self,
        *,
        BackupVaultName: str,
        SNSTopicArn: str,
        BackupVaultEvents: List[BackupVaultEventType]
    ) -> None:
        """
        Turns on notifications on a backup vault for the specified topic and events.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.put_backup_vault_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#put_backup_vault_notifications)
        """

    def put_restore_validation_result(
        self,
        *,
        RestoreJobId: str,
        ValidationStatus: RestoreValidationStatusType,
        ValidationStatusMessage: str = None
    ) -> None:
        """
        This request allows you to send your independent self-run restore test
        validation results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.put_restore_validation_result)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#put_restore_validation_result)
        """

    def start_backup_job(
        self,
        *,
        BackupVaultName: str,
        ResourceArn: str,
        IamRoleArn: str,
        IdempotencyToken: str = None,
        StartWindowMinutes: int = None,
        CompleteWindowMinutes: int = None,
        Lifecycle: "LifecycleTypeDef" = None,
        RecoveryPointTags: Dict[str, str] = None,
        BackupOptions: Dict[str, str] = None
    ) -> StartBackupJobOutputTypeDef:
        """
        Starts an on-demand backup job for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.start_backup_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#start_backup_job)
        """

    def start_copy_job(
        self,
        *,
        RecoveryPointArn: str,
        SourceBackupVaultName: str,
        DestinationBackupVaultArn: str,
        IamRoleArn: str,
        IdempotencyToken: str = None,
        Lifecycle: "LifecycleTypeDef" = None
    ) -> StartCopyJobOutputTypeDef:
        """
        Starts a job to create a one-time copy of the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.start_copy_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#start_copy_job)
        """

    def start_report_job(
        self, *, ReportPlanName: str, IdempotencyToken: str = None
    ) -> StartReportJobOutputTypeDef:
        """
        Starts an on-demand report job for the specified report plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.start_report_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#start_report_job)
        """

    def start_restore_job(
        self,
        *,
        RecoveryPointArn: str,
        Metadata: Dict[str, str],
        IamRoleArn: str = None,
        IdempotencyToken: str = None,
        ResourceType: str = None,
        CopySourceTagsToRestoredResource: bool = None
    ) -> StartRestoreJobOutputTypeDef:
        """
        Recovers the saved resource identified by an Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.start_restore_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#start_restore_job)
        """

    def stop_backup_job(self, *, BackupJobId: str) -> None:
        """
        Attempts to cancel a job to create a one-time backup of a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.stop_backup_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#stop_backup_job)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        Assigns a set of key-value pairs to a recovery point, backup plan, or backup
        vault identified by an Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeyList: List[str]) -> None:
        """
        Removes a set of key-value pairs from a recovery point, backup plan, or backup
        vault identified by an Amazon Resource Name (ARN) See also: `AWS API
        Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/UntagResource>`_
        **Request Syntax** response = client.untag_resou...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#untag_resource)
        """

    def update_backup_plan(
        self, *, BackupPlanId: str, BackupPlan: "BackupPlanInputTypeDef"
    ) -> UpdateBackupPlanOutputTypeDef:
        """
        Updates an existing backup plan identified by its `backupPlanId` with the input
        document in JSON format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.update_backup_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#update_backup_plan)
        """

    def update_framework(
        self,
        *,
        FrameworkName: str,
        FrameworkDescription: str = None,
        FrameworkControls: List["FrameworkControlTypeDef"] = None,
        IdempotencyToken: str = None
    ) -> UpdateFrameworkOutputTypeDef:
        """
        Updates an existing framework identified by its `FrameworkName` with the input
        document in JSON format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.update_framework)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#update_framework)
        """

    def update_global_settings(self, *, GlobalSettings: Dict[str, str] = None) -> None:
        """
        Updates whether the Amazon Web Services account is opted in to cross-account
        backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.update_global_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#update_global_settings)
        """

    def update_recovery_point_lifecycle(
        self, *, BackupVaultName: str, RecoveryPointArn: str, Lifecycle: "LifecycleTypeDef" = None
    ) -> UpdateRecoveryPointLifecycleOutputTypeDef:
        """
        Sets the transition lifecycle of a recovery point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.update_recovery_point_lifecycle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#update_recovery_point_lifecycle)
        """

    def update_region_settings(
        self,
        *,
        ResourceTypeOptInPreference: Dict[str, bool] = None,
        ResourceTypeManagementPreference: Dict[str, bool] = None
    ) -> None:
        """
        Updates the current service opt-in settings for the Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.update_region_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#update_region_settings)
        """

    def update_report_plan(
        self,
        *,
        ReportPlanName: str,
        ReportPlanDescription: str = None,
        ReportDeliveryChannel: "ReportDeliveryChannelTypeDef" = None,
        ReportSetting: "ReportSettingTypeDef" = None,
        IdempotencyToken: str = None
    ) -> UpdateReportPlanOutputTypeDef:
        """
        Updates an existing report plan identified by its `ReportPlanName` with the
        input document in JSON format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.update_report_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#update_report_plan)
        """

    def update_restore_testing_plan(
        self,
        *,
        RestoreTestingPlan: "RestoreTestingPlanForUpdateTypeDef",
        RestoreTestingPlanName: str
    ) -> UpdateRestoreTestingPlanOutputTypeDef:
        """
        This request will send changes to your specified restore testing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.update_restore_testing_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#update_restore_testing_plan)
        """

    def update_restore_testing_selection(
        self,
        *,
        RestoreTestingPlanName: str,
        RestoreTestingSelection: "RestoreTestingSelectionForUpdateTypeDef",
        RestoreTestingSelectionName: str
    ) -> UpdateRestoreTestingSelectionOutputTypeDef:
        """
        Most elements except the `RestoreTestingSelectionName` can be updated with this
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Client.update_restore_testing_selection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#update_restore_testing_selection)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_backup_jobs"]) -> ListBackupJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListBackupJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listbackupjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_backup_plan_templates"]
    ) -> ListBackupPlanTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListBackupPlanTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listbackupplantemplatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_backup_plan_versions"]
    ) -> ListBackupPlanVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListBackupPlanVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listbackupplanversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_backup_plans"]
    ) -> ListBackupPlansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListBackupPlans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listbackupplanspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_backup_selections"]
    ) -> ListBackupSelectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListBackupSelections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listbackupselectionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_backup_vaults"]
    ) -> ListBackupVaultsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListBackupVaults)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listbackupvaultspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_copy_jobs"]) -> ListCopyJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListCopyJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listcopyjobspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_legal_holds"]) -> ListLegalHoldsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListLegalHolds)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listlegalholdspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_protected_resources"]
    ) -> ListProtectedResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListProtectedResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listprotectedresourcespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_protected_resources_by_backup_vault"]
    ) -> ListProtectedResourcesByBackupVaultPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListProtectedResourcesByBackupVault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listprotectedresourcesbybackupvaultpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_recovery_points_by_backup_vault"]
    ) -> ListRecoveryPointsByBackupVaultPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRecoveryPointsByBackupVault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrecoverypointsbybackupvaultpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_recovery_points_by_legal_hold"]
    ) -> ListRecoveryPointsByLegalHoldPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRecoveryPointsByLegalHold)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrecoverypointsbylegalholdpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_recovery_points_by_resource"]
    ) -> ListRecoveryPointsByResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRecoveryPointsByResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrecoverypointsbyresourcepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_restore_jobs"]
    ) -> ListRestoreJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRestoreJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrestorejobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_restore_jobs_by_protected_resource"]
    ) -> ListRestoreJobsByProtectedResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRestoreJobsByProtectedResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrestorejobsbyprotectedresourcepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_restore_testing_plans"]
    ) -> ListRestoreTestingPlansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRestoreTestingPlans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrestoretestingplanspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_restore_testing_selections"]
    ) -> ListRestoreTestingSelectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/backup.html#Backup.Paginator.ListRestoreTestingSelections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/paginators.html#listrestoretestingselectionspaginator)
        """
