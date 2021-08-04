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
from datetime import datetime
from typing import Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta

from .literals import (
    BackupJobStateType,
    BackupVaultEventType,
    CopyJobStateType,
    RestoreJobStatusType,
)
from .type_defs import (
    BackupPlanInputTypeDef,
    BackupSelectionTypeDef,
    CreateBackupPlanOutputTypeDef,
    CreateBackupSelectionOutputTypeDef,
    CreateBackupVaultOutputTypeDef,
    DeleteBackupPlanOutputTypeDef,
    DescribeBackupJobOutputTypeDef,
    DescribeBackupVaultOutputTypeDef,
    DescribeCopyJobOutputTypeDef,
    DescribeGlobalSettingsOutputTypeDef,
    DescribeProtectedResourceOutputTypeDef,
    DescribeRecoveryPointOutputTypeDef,
    DescribeRegionSettingsOutputTypeDef,
    DescribeRestoreJobOutputTypeDef,
    ExportBackupPlanTemplateOutputTypeDef,
    GetBackupPlanFromJSONOutputTypeDef,
    GetBackupPlanFromTemplateOutputTypeDef,
    GetBackupPlanOutputTypeDef,
    GetBackupSelectionOutputTypeDef,
    GetBackupVaultAccessPolicyOutputTypeDef,
    GetBackupVaultNotificationsOutputTypeDef,
    GetRecoveryPointRestoreMetadataOutputTypeDef,
    GetSupportedResourceTypesOutputTypeDef,
    LifecycleTypeDef,
    ListBackupJobsOutputTypeDef,
    ListBackupPlansOutputTypeDef,
    ListBackupPlanTemplatesOutputTypeDef,
    ListBackupPlanVersionsOutputTypeDef,
    ListBackupSelectionsOutputTypeDef,
    ListBackupVaultsOutputTypeDef,
    ListCopyJobsOutputTypeDef,
    ListProtectedResourcesOutputTypeDef,
    ListRecoveryPointsByBackupVaultOutputTypeDef,
    ListRecoveryPointsByResourceOutputTypeDef,
    ListRestoreJobsOutputTypeDef,
    ListTagsOutputTypeDef,
    StartBackupJobOutputTypeDef,
    StartCopyJobOutputTypeDef,
    StartRestoreJobOutputTypeDef,
    UpdateBackupPlanOutputTypeDef,
    UpdateRecoveryPointLifecycleOutputTypeDef,
)

__all__ = ("BackupClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AlreadyExistsException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#can_paginate)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.create_backup_plan)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.create_backup_selection)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.create_backup_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#create_backup_vault)
        """
    def delete_backup_plan(self, *, BackupPlanId: str) -> DeleteBackupPlanOutputTypeDef:
        """
        Deletes a backup plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.delete_backup_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete_backup_plan)
        """
    def delete_backup_selection(self, *, BackupPlanId: str, SelectionId: str) -> None:
        """
        Deletes the resource selection associated with a backup plan that is specified
        by the `SelectionId` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.delete_backup_selection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete_backup_selection)
        """
    def delete_backup_vault(self, *, BackupVaultName: str) -> None:
        """
        Deletes the backup vault identified by its name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.delete_backup_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete_backup_vault)
        """
    def delete_backup_vault_access_policy(self, *, BackupVaultName: str) -> None:
        """
        Deletes the policy document that manages permissions on a backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.delete_backup_vault_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete_backup_vault_access_policy)
        """
    def delete_backup_vault_notifications(self, *, BackupVaultName: str) -> None:
        """
        Deletes event notifications for the specified backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.delete_backup_vault_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete_backup_vault_notifications)
        """
    def delete_recovery_point(self, *, BackupVaultName: str, RecoveryPointArn: str) -> None:
        """
        Deletes the recovery point specified by a recovery point ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.delete_recovery_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#delete_recovery_point)
        """
    def describe_backup_job(self, *, BackupJobId: str) -> DescribeBackupJobOutputTypeDef:
        """
        Returns backup job details for the specified `BackupJobId` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.describe_backup_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe_backup_job)
        """
    def describe_backup_vault(self, *, BackupVaultName: str) -> DescribeBackupVaultOutputTypeDef:
        """
        Returns metadata about a backup vault specified by its name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.describe_backup_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe_backup_vault)
        """
    def describe_copy_job(self, *, CopyJobId: str) -> DescribeCopyJobOutputTypeDef:
        """
        Returns metadata associated with creating a copy of a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.describe_copy_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe_copy_job)
        """
    def describe_global_settings(self) -> DescribeGlobalSettingsOutputTypeDef:
        """
        Describes the global settings of the AWS account, including whether it is opted
        in to cross-account backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.describe_global_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe_global_settings)
        """
    def describe_protected_resource(
        self, *, ResourceArn: str
    ) -> DescribeProtectedResourceOutputTypeDef:
        """
        Returns information about a saved resource, including the last time it was
        backed up, its Amazon Resource Name (ARN), and the AWS service type of the saved
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.describe_protected_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe_protected_resource)
        """
    def describe_recovery_point(
        self, *, BackupVaultName: str, RecoveryPointArn: str
    ) -> DescribeRecoveryPointOutputTypeDef:
        """
        Returns metadata associated with a recovery point, including ID, status,
        encryption, and lifecycle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.describe_recovery_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe_recovery_point)
        """
    def describe_region_settings(self) -> DescribeRegionSettingsOutputTypeDef:
        """
        Returns the current service opt-in settings for the Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.describe_region_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe_region_settings)
        """
    def describe_restore_job(self, *, RestoreJobId: str) -> DescribeRestoreJobOutputTypeDef:
        """
        Returns metadata associated with a restore job that is specified by a job ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.describe_restore_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#describe_restore_job)
        """
    def disassociate_recovery_point(self, *, BackupVaultName: str, RecoveryPointArn: str) -> None:
        """
        Deletes the specified continuous backup recovery point from AWS Backup and
        releases control of that continuous backup to the source service, such as Amazon
        RDS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.disassociate_recovery_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#disassociate_recovery_point)
        """
    def export_backup_plan_template(
        self, *, BackupPlanId: str
    ) -> ExportBackupPlanTemplateOutputTypeDef:
        """
        Returns the backup plan that is specified by the plan ID as a backup template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.export_backup_plan_template)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#generate_presigned_url)
        """
    def get_backup_plan(
        self, *, BackupPlanId: str, VersionId: str = None
    ) -> GetBackupPlanOutputTypeDef:
        """
        Returns `BackupPlan` details for the specified `BackupPlanId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.get_backup_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_backup_plan)
        """
    def get_backup_plan_from_json(
        self, *, BackupPlanTemplateJson: str
    ) -> GetBackupPlanFromJSONOutputTypeDef:
        """
        Returns a valid JSON document specifying a backup plan or an error.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.get_backup_plan_from_json)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_backup_plan_from_json)
        """
    def get_backup_plan_from_template(
        self, *, BackupPlanTemplateId: str
    ) -> GetBackupPlanFromTemplateOutputTypeDef:
        """
        Returns the template specified by its `templateId` as a backup plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.get_backup_plan_from_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_backup_plan_from_template)
        """
    def get_backup_selection(
        self, *, BackupPlanId: str, SelectionId: str
    ) -> GetBackupSelectionOutputTypeDef:
        """
        Returns selection metadata and a document in JSON format that specifies a list
        of resources that are associated with a backup plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.get_backup_selection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_backup_selection)
        """
    def get_backup_vault_access_policy(
        self, *, BackupVaultName: str
    ) -> GetBackupVaultAccessPolicyOutputTypeDef:
        """
        Returns the access policy document that is associated with the named backup
        vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.get_backup_vault_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_backup_vault_access_policy)
        """
    def get_backup_vault_notifications(
        self, *, BackupVaultName: str
    ) -> GetBackupVaultNotificationsOutputTypeDef:
        """
        Returns event notifications for the specified backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.get_backup_vault_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_backup_vault_notifications)
        """
    def get_recovery_point_restore_metadata(
        self, *, BackupVaultName: str, RecoveryPointArn: str
    ) -> GetRecoveryPointRestoreMetadataOutputTypeDef:
        """
        Returns a set of metadata key-value pairs that were used to create the backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.get_recovery_point_restore_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_recovery_point_restore_metadata)
        """
    def get_supported_resource_types(self) -> GetSupportedResourceTypesOutputTypeDef:
        """
        Returns the AWS resource types supported by AWS Backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.get_supported_resource_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#get_supported_resource_types)
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
        ByAccountId: str = None
    ) -> ListBackupJobsOutputTypeDef:
        """
        Returns a list of existing backup jobs for an authenticated account for the last
        30 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.list_backup_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_backup_jobs)
        """
    def list_backup_plan_templates(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListBackupPlanTemplatesOutputTypeDef:
        """
        Returns metadata of your saved backup plan templates, including the template ID,
        name, and the creation and deletion dates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.list_backup_plan_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_backup_plan_templates)
        """
    def list_backup_plan_versions(
        self, *, BackupPlanId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListBackupPlanVersionsOutputTypeDef:
        """
        Returns version metadata of your backup plans, including Amazon Resource Names
        (ARNs), backup plan IDs, creation and deletion dates, plan names, and version
        IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.list_backup_plan_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_backup_plan_versions)
        """
    def list_backup_plans(
        self, *, NextToken: str = None, MaxResults: int = None, IncludeDeleted: bool = None
    ) -> ListBackupPlansOutputTypeDef:
        """
        Returns a list of existing backup plans for an authenticated account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.list_backup_plans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_backup_plans)
        """
    def list_backup_selections(
        self, *, BackupPlanId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListBackupSelectionsOutputTypeDef:
        """
        Returns an array containing metadata of the resources associated with the target
        backup plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.list_backup_selections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_backup_selections)
        """
    def list_backup_vaults(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListBackupVaultsOutputTypeDef:
        """
        Returns a list of recovery point storage containers along with information about
        them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.list_backup_vaults)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_backup_vaults)
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
        ByAccountId: str = None
    ) -> ListCopyJobsOutputTypeDef:
        """
        Returns metadata about your copy jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.list_copy_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_copy_jobs)
        """
    def list_protected_resources(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListProtectedResourcesOutputTypeDef:
        """
        Returns an array of resources successfully backed up by AWS Backup, including
        the time the resource was saved, an Amazon Resource Name (ARN) of the resource,
        and a resource type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.list_protected_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_protected_resources)
        """
    def list_recovery_points_by_backup_vault(
        self,
        *,
        BackupVaultName: str,
        NextToken: str = None,
        MaxResults: int = None,
        ByResourceArn: str = None,
        ByResourceType: str = None,
        ByBackupPlanId: str = None,
        ByCreatedBefore: Union[datetime, str] = None,
        ByCreatedAfter: Union[datetime, str] = None
    ) -> ListRecoveryPointsByBackupVaultOutputTypeDef:
        """
        Returns detailed information about the recovery points stored in a backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.list_recovery_points_by_backup_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_recovery_points_by_backup_vault)
        """
    def list_recovery_points_by_resource(
        self, *, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListRecoveryPointsByResourceOutputTypeDef:
        """
        Returns detailed information about recovery points of the type specified by a
        resource Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.list_recovery_points_by_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_recovery_points_by_resource)
        """
    def list_restore_jobs(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        ByAccountId: str = None,
        ByCreatedBefore: Union[datetime, str] = None,
        ByCreatedAfter: Union[datetime, str] = None,
        ByStatus: RestoreJobStatusType = None
    ) -> ListRestoreJobsOutputTypeDef:
        """
        Returns a list of jobs that AWS Backup initiated to restore a saved resource,
        including metadata about the recovery process.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.list_restore_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_restore_jobs)
        """
    def list_tags(
        self, *, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsOutputTypeDef:
        """
        Returns a list of key-value pairs assigned to a target recovery point, backup
        plan, or backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.list_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#list_tags)
        """
    def put_backup_vault_access_policy(self, *, BackupVaultName: str, Policy: str = None) -> None:
        """
        Sets a resource-based policy that is used to manage access permissions on the
        target backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.put_backup_vault_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#put_backup_vault_access_policy)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.put_backup_vault_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#put_backup_vault_notifications)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.start_backup_job)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.start_copy_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#start_copy_job)
        """
    def start_restore_job(
        self,
        *,
        RecoveryPointArn: str,
        Metadata: Dict[str, str],
        IamRoleArn: str,
        IdempotencyToken: str = None,
        ResourceType: str = None
    ) -> StartRestoreJobOutputTypeDef:
        """
        Recovers the saved resource identified by an Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.start_restore_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#start_restore_job)
        """
    def stop_backup_job(self, *, BackupJobId: str) -> None:
        """
        Attempts to cancel a job to create a one-time backup of a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.stop_backup_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#stop_backup_job)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        Assigns a set of key-value pairs to a recovery point, backup plan, or backup
        vault identified by an Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeyList: List[str]) -> None:
        """
        Removes a set of key-value pairs from a recovery point, backup plan, or backup
        vault identified by an Amazon Resource Name (ARN) See also: `AWS API
        Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/UntagResource>`_
        **Request Syntax** response = client.untag_reso...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#untag_resource)
        """
    def update_backup_plan(
        self, *, BackupPlanId: str, BackupPlan: "BackupPlanInputTypeDef"
    ) -> UpdateBackupPlanOutputTypeDef:
        """
        Updates an existing backup plan identified by its `backupPlanId` with the input
        document in JSON format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.update_backup_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#update_backup_plan)
        """
    def update_global_settings(self, *, GlobalSettings: Dict[str, str] = None) -> None:
        """
        Updates the current global settings for the AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.update_global_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#update_global_settings)
        """
    def update_recovery_point_lifecycle(
        self, *, BackupVaultName: str, RecoveryPointArn: str, Lifecycle: "LifecycleTypeDef" = None
    ) -> UpdateRecoveryPointLifecycleOutputTypeDef:
        """
        Sets the transition lifecycle of a recovery point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.update_recovery_point_lifecycle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#update_recovery_point_lifecycle)
        """
    def update_region_settings(
        self, *, ResourceTypeOptInPreference: Dict[str, bool] = None
    ) -> None:
        """
        Updates the current service opt-in settings for the Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/backup.html#Backup.Client.update_region_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/client.html#update_region_settings)
        """
