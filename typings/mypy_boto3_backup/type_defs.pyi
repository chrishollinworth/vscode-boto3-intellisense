"""
Main interface for backup service type definitions.

Usage::

    ```python
    from mypy_boto3_backup.type_defs import BackupJobTypeDef

    data: BackupJobTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BackupJobTypeDef",
    "BackupPlanTemplatesListMemberTypeDef",
    "BackupPlanTypeDef",
    "BackupPlansListMemberTypeDef",
    "BackupRuleInputTypeDef",
    "BackupRuleTypeDef",
    "BackupSelectionTypeDef",
    "BackupSelectionsListMemberTypeDef",
    "BackupVaultListMemberTypeDef",
    "CalculatedLifecycleTypeDef",
    "ConditionTypeDef",
    "CopyActionTypeDef",
    "CopyJobTypeDef",
    "LifecycleTypeDef",
    "ProtectedResourceTypeDef",
    "RecoveryPointByBackupVaultTypeDef",
    "RecoveryPointByResourceTypeDef",
    "RecoveryPointCreatorTypeDef",
    "RestoreJobsListMemberTypeDef",
    "BackupPlanInputTypeDef",
    "CreateBackupPlanOutputTypeDef",
    "CreateBackupSelectionOutputTypeDef",
    "CreateBackupVaultOutputTypeDef",
    "DeleteBackupPlanOutputTypeDef",
    "DescribeBackupJobOutputTypeDef",
    "DescribeBackupVaultOutputTypeDef",
    "DescribeCopyJobOutputTypeDef",
    "DescribeProtectedResourceOutputTypeDef",
    "DescribeRecoveryPointOutputTypeDef",
    "DescribeRegionSettingsOutputTypeDef",
    "DescribeRestoreJobOutputTypeDef",
    "ExportBackupPlanTemplateOutputTypeDef",
    "GetBackupPlanFromJSONOutputTypeDef",
    "GetBackupPlanFromTemplateOutputTypeDef",
    "GetBackupPlanOutputTypeDef",
    "GetBackupSelectionOutputTypeDef",
    "GetBackupVaultAccessPolicyOutputTypeDef",
    "GetBackupVaultNotificationsOutputTypeDef",
    "GetRecoveryPointRestoreMetadataOutputTypeDef",
    "GetSupportedResourceTypesOutputTypeDef",
    "ListBackupJobsOutputTypeDef",
    "ListBackupPlanTemplatesOutputTypeDef",
    "ListBackupPlanVersionsOutputTypeDef",
    "ListBackupPlansOutputTypeDef",
    "ListBackupSelectionsOutputTypeDef",
    "ListBackupVaultsOutputTypeDef",
    "ListCopyJobsOutputTypeDef",
    "ListProtectedResourcesOutputTypeDef",
    "ListRecoveryPointsByBackupVaultOutputTypeDef",
    "ListRecoveryPointsByResourceOutputTypeDef",
    "ListRestoreJobsOutputTypeDef",
    "ListTagsOutputTypeDef",
    "StartBackupJobOutputTypeDef",
    "StartCopyJobOutputTypeDef",
    "StartRestoreJobOutputTypeDef",
    "UpdateBackupPlanOutputTypeDef",
    "UpdateRecoveryPointLifecycleOutputTypeDef",
)

BackupJobTypeDef = TypedDict(
    "BackupJobTypeDef",
    {
        "AccountId": str,
        "BackupJobId": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "ResourceArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "State": Literal[
            "CREATED", "PENDING", "RUNNING", "ABORTING", "ABORTED", "COMPLETED", "FAILED", "EXPIRED"
        ],
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": "RecoveryPointCreatorTypeDef",
        "ExpectedCompletionDate": datetime,
        "StartBy": datetime,
        "ResourceType": str,
        "BytesTransferred": int,
    },
    total=False,
)

BackupPlanTemplatesListMemberTypeDef = TypedDict(
    "BackupPlanTemplatesListMemberTypeDef",
    {"BackupPlanTemplateId": str, "BackupPlanTemplateName": str},
    total=False,
)

BackupPlanTypeDef = TypedDict(
    "BackupPlanTypeDef", {"BackupPlanName": str, "Rules": List["BackupRuleTypeDef"]}
)

BackupPlansListMemberTypeDef = TypedDict(
    "BackupPlansListMemberTypeDef",
    {
        "BackupPlanArn": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "DeletionDate": datetime,
        "VersionId": str,
        "BackupPlanName": str,
        "CreatorRequestId": str,
        "LastExecutionDate": datetime,
    },
    total=False,
)

_RequiredBackupRuleInputTypeDef = TypedDict(
    "_RequiredBackupRuleInputTypeDef", {"RuleName": str, "TargetBackupVaultName": str}
)
_OptionalBackupRuleInputTypeDef = TypedDict(
    "_OptionalBackupRuleInputTypeDef",
    {
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": "LifecycleTypeDef",
        "RecoveryPointTags": Dict[str, str],
        "CopyActions": List["CopyActionTypeDef"],
    },
    total=False,
)


class BackupRuleInputTypeDef(_RequiredBackupRuleInputTypeDef, _OptionalBackupRuleInputTypeDef):
    pass


_RequiredBackupRuleTypeDef = TypedDict(
    "_RequiredBackupRuleTypeDef", {"RuleName": str, "TargetBackupVaultName": str}
)
_OptionalBackupRuleTypeDef = TypedDict(
    "_OptionalBackupRuleTypeDef",
    {
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": "LifecycleTypeDef",
        "RecoveryPointTags": Dict[str, str],
        "RuleId": str,
        "CopyActions": List["CopyActionTypeDef"],
    },
    total=False,
)


class BackupRuleTypeDef(_RequiredBackupRuleTypeDef, _OptionalBackupRuleTypeDef):
    pass


_RequiredBackupSelectionTypeDef = TypedDict(
    "_RequiredBackupSelectionTypeDef", {"SelectionName": str, "IamRoleArn": str}
)
_OptionalBackupSelectionTypeDef = TypedDict(
    "_OptionalBackupSelectionTypeDef",
    {"Resources": List[str], "ListOfTags": List["ConditionTypeDef"]},
    total=False,
)


class BackupSelectionTypeDef(_RequiredBackupSelectionTypeDef, _OptionalBackupSelectionTypeDef):
    pass


BackupSelectionsListMemberTypeDef = TypedDict(
    "BackupSelectionsListMemberTypeDef",
    {
        "SelectionId": str,
        "SelectionName": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "IamRoleArn": str,
    },
    total=False,
)

BackupVaultListMemberTypeDef = TypedDict(
    "BackupVaultListMemberTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "CreationDate": datetime,
        "EncryptionKeyArn": str,
        "CreatorRequestId": str,
        "NumberOfRecoveryPoints": int,
    },
    total=False,
)

CalculatedLifecycleTypeDef = TypedDict(
    "CalculatedLifecycleTypeDef",
    {"MoveToColdStorageAt": datetime, "DeleteAt": datetime},
    total=False,
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {"ConditionType": Literal["STRINGEQUALS"], "ConditionKey": str, "ConditionValue": str},
)

_RequiredCopyActionTypeDef = TypedDict(
    "_RequiredCopyActionTypeDef", {"DestinationBackupVaultArn": str}
)
_OptionalCopyActionTypeDef = TypedDict(
    "_OptionalCopyActionTypeDef", {"Lifecycle": "LifecycleTypeDef"}, total=False
)


class CopyActionTypeDef(_RequiredCopyActionTypeDef, _OptionalCopyActionTypeDef):
    pass


CopyJobTypeDef = TypedDict(
    "CopyJobTypeDef",
    {
        "AccountId": str,
        "CopyJobId": str,
        "SourceBackupVaultArn": str,
        "SourceRecoveryPointArn": str,
        "DestinationBackupVaultArn": str,
        "DestinationRecoveryPointArn": str,
        "ResourceArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "State": Literal["CREATED", "RUNNING", "COMPLETED", "FAILED"],
        "StatusMessage": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": "RecoveryPointCreatorTypeDef",
        "ResourceType": str,
    },
    total=False,
)

LifecycleTypeDef = TypedDict(
    "LifecycleTypeDef", {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int}, total=False
)

ProtectedResourceTypeDef = TypedDict(
    "ProtectedResourceTypeDef",
    {"ResourceArn": str, "ResourceType": str, "LastBackupTime": datetime},
    total=False,
)

RecoveryPointByBackupVaultTypeDef = TypedDict(
    "RecoveryPointByBackupVaultTypeDef",
    {
        "RecoveryPointArn": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "CreatedBy": "RecoveryPointCreatorTypeDef",
        "IamRoleArn": str,
        "Status": Literal["COMPLETED", "PARTIAL", "DELETING", "EXPIRED"],
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "BackupSizeInBytes": int,
        "CalculatedLifecycle": "CalculatedLifecycleTypeDef",
        "Lifecycle": "LifecycleTypeDef",
        "EncryptionKeyArn": str,
        "IsEncrypted": bool,
        "LastRestoreTime": datetime,
    },
    total=False,
)

RecoveryPointByResourceTypeDef = TypedDict(
    "RecoveryPointByResourceTypeDef",
    {
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "Status": Literal["COMPLETED", "PARTIAL", "DELETING", "EXPIRED"],
        "EncryptionKeyArn": str,
        "BackupSizeBytes": int,
        "BackupVaultName": str,
    },
    total=False,
)

RecoveryPointCreatorTypeDef = TypedDict(
    "RecoveryPointCreatorTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "BackupPlanVersion": str, "BackupRuleId": str},
    total=False,
)

RestoreJobsListMemberTypeDef = TypedDict(
    "RestoreJobsListMemberTypeDef",
    {
        "AccountId": str,
        "RestoreJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "Status": Literal["PENDING", "RUNNING", "COMPLETED", "ABORTED", "FAILED"],
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "ExpectedCompletionTimeMinutes": int,
        "CreatedResourceArn": str,
        "ResourceType": str,
    },
    total=False,
)

BackupPlanInputTypeDef = TypedDict(
    "BackupPlanInputTypeDef", {"BackupPlanName": str, "Rules": List["BackupRuleInputTypeDef"]}
)

CreateBackupPlanOutputTypeDef = TypedDict(
    "CreateBackupPlanOutputTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "CreationDate": datetime, "VersionId": str},
    total=False,
)

CreateBackupSelectionOutputTypeDef = TypedDict(
    "CreateBackupSelectionOutputTypeDef",
    {"SelectionId": str, "BackupPlanId": str, "CreationDate": datetime},
    total=False,
)

CreateBackupVaultOutputTypeDef = TypedDict(
    "CreateBackupVaultOutputTypeDef",
    {"BackupVaultName": str, "BackupVaultArn": str, "CreationDate": datetime},
    total=False,
)

DeleteBackupPlanOutputTypeDef = TypedDict(
    "DeleteBackupPlanOutputTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "DeletionDate": datetime, "VersionId": str},
    total=False,
)

DescribeBackupJobOutputTypeDef = TypedDict(
    "DescribeBackupJobOutputTypeDef",
    {
        "AccountId": str,
        "BackupJobId": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "ResourceArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "State": Literal[
            "CREATED", "PENDING", "RUNNING", "ABORTING", "ABORTED", "COMPLETED", "FAILED", "EXPIRED"
        ],
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": "RecoveryPointCreatorTypeDef",
        "ResourceType": str,
        "BytesTransferred": int,
        "ExpectedCompletionDate": datetime,
        "StartBy": datetime,
    },
    total=False,
)

DescribeBackupVaultOutputTypeDef = TypedDict(
    "DescribeBackupVaultOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "EncryptionKeyArn": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "NumberOfRecoveryPoints": int,
    },
    total=False,
)

DescribeCopyJobOutputTypeDef = TypedDict(
    "DescribeCopyJobOutputTypeDef", {"CopyJob": "CopyJobTypeDef"}, total=False
)

DescribeProtectedResourceOutputTypeDef = TypedDict(
    "DescribeProtectedResourceOutputTypeDef",
    {"ResourceArn": str, "ResourceType": str, "LastBackupTime": datetime},
    total=False,
)

DescribeRecoveryPointOutputTypeDef = TypedDict(
    "DescribeRecoveryPointOutputTypeDef",
    {
        "RecoveryPointArn": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "CreatedBy": "RecoveryPointCreatorTypeDef",
        "IamRoleArn": str,
        "Status": Literal["COMPLETED", "PARTIAL", "DELETING", "EXPIRED"],
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "BackupSizeInBytes": int,
        "CalculatedLifecycle": "CalculatedLifecycleTypeDef",
        "Lifecycle": "LifecycleTypeDef",
        "EncryptionKeyArn": str,
        "IsEncrypted": bool,
        "StorageClass": Literal["WARM", "COLD", "DELETED"],
        "LastRestoreTime": datetime,
    },
    total=False,
)

DescribeRegionSettingsOutputTypeDef = TypedDict(
    "DescribeRegionSettingsOutputTypeDef",
    {"ResourceTypeOptInPreference": Dict[str, bool]},
    total=False,
)

DescribeRestoreJobOutputTypeDef = TypedDict(
    "DescribeRestoreJobOutputTypeDef",
    {
        "AccountId": str,
        "RestoreJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "Status": Literal["PENDING", "RUNNING", "COMPLETED", "ABORTED", "FAILED"],
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "ExpectedCompletionTimeMinutes": int,
        "CreatedResourceArn": str,
        "ResourceType": str,
    },
    total=False,
)

ExportBackupPlanTemplateOutputTypeDef = TypedDict(
    "ExportBackupPlanTemplateOutputTypeDef", {"BackupPlanTemplateJson": str}, total=False
)

GetBackupPlanFromJSONOutputTypeDef = TypedDict(
    "GetBackupPlanFromJSONOutputTypeDef", {"BackupPlan": "BackupPlanTypeDef"}, total=False
)

GetBackupPlanFromTemplateOutputTypeDef = TypedDict(
    "GetBackupPlanFromTemplateOutputTypeDef",
    {"BackupPlanDocument": "BackupPlanTypeDef"},
    total=False,
)

GetBackupPlanOutputTypeDef = TypedDict(
    "GetBackupPlanOutputTypeDef",
    {
        "BackupPlan": "BackupPlanTypeDef",
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "VersionId": str,
        "CreatorRequestId": str,
        "CreationDate": datetime,
        "DeletionDate": datetime,
        "LastExecutionDate": datetime,
    },
    total=False,
)

GetBackupSelectionOutputTypeDef = TypedDict(
    "GetBackupSelectionOutputTypeDef",
    {
        "BackupSelection": "BackupSelectionTypeDef",
        "SelectionId": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
    },
    total=False,
)

GetBackupVaultAccessPolicyOutputTypeDef = TypedDict(
    "GetBackupVaultAccessPolicyOutputTypeDef",
    {"BackupVaultName": str, "BackupVaultArn": str, "Policy": str},
    total=False,
)

GetBackupVaultNotificationsOutputTypeDef = TypedDict(
    "GetBackupVaultNotificationsOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "SNSTopicArn": str,
        "BackupVaultEvents": List[
            Literal[
                "BACKUP_JOB_STARTED",
                "BACKUP_JOB_COMPLETED",
                "BACKUP_JOB_SUCCESSFUL",
                "BACKUP_JOB_FAILED",
                "BACKUP_JOB_EXPIRED",
                "RESTORE_JOB_STARTED",
                "RESTORE_JOB_COMPLETED",
                "RESTORE_JOB_SUCCESSFUL",
                "RESTORE_JOB_FAILED",
                "COPY_JOB_STARTED",
                "COPY_JOB_SUCCESSFUL",
                "COPY_JOB_FAILED",
                "RECOVERY_POINT_MODIFIED",
                "BACKUP_PLAN_CREATED",
                "BACKUP_PLAN_MODIFIED",
            ]
        ],
    },
    total=False,
)

GetRecoveryPointRestoreMetadataOutputTypeDef = TypedDict(
    "GetRecoveryPointRestoreMetadataOutputTypeDef",
    {"BackupVaultArn": str, "RecoveryPointArn": str, "RestoreMetadata": Dict[str, str]},
    total=False,
)

GetSupportedResourceTypesOutputTypeDef = TypedDict(
    "GetSupportedResourceTypesOutputTypeDef", {"ResourceTypes": List[str]}, total=False
)

ListBackupJobsOutputTypeDef = TypedDict(
    "ListBackupJobsOutputTypeDef",
    {"BackupJobs": List["BackupJobTypeDef"], "NextToken": str},
    total=False,
)

ListBackupPlanTemplatesOutputTypeDef = TypedDict(
    "ListBackupPlanTemplatesOutputTypeDef",
    {"NextToken": str, "BackupPlanTemplatesList": List["BackupPlanTemplatesListMemberTypeDef"]},
    total=False,
)

ListBackupPlanVersionsOutputTypeDef = TypedDict(
    "ListBackupPlanVersionsOutputTypeDef",
    {"NextToken": str, "BackupPlanVersionsList": List["BackupPlansListMemberTypeDef"]},
    total=False,
)

ListBackupPlansOutputTypeDef = TypedDict(
    "ListBackupPlansOutputTypeDef",
    {"NextToken": str, "BackupPlansList": List["BackupPlansListMemberTypeDef"]},
    total=False,
)

ListBackupSelectionsOutputTypeDef = TypedDict(
    "ListBackupSelectionsOutputTypeDef",
    {"NextToken": str, "BackupSelectionsList": List["BackupSelectionsListMemberTypeDef"]},
    total=False,
)

ListBackupVaultsOutputTypeDef = TypedDict(
    "ListBackupVaultsOutputTypeDef",
    {"BackupVaultList": List["BackupVaultListMemberTypeDef"], "NextToken": str},
    total=False,
)

ListCopyJobsOutputTypeDef = TypedDict(
    "ListCopyJobsOutputTypeDef", {"CopyJobs": List["CopyJobTypeDef"], "NextToken": str}, total=False
)

ListProtectedResourcesOutputTypeDef = TypedDict(
    "ListProtectedResourcesOutputTypeDef",
    {"Results": List["ProtectedResourceTypeDef"], "NextToken": str},
    total=False,
)

ListRecoveryPointsByBackupVaultOutputTypeDef = TypedDict(
    "ListRecoveryPointsByBackupVaultOutputTypeDef",
    {"NextToken": str, "RecoveryPoints": List["RecoveryPointByBackupVaultTypeDef"]},
    total=False,
)

ListRecoveryPointsByResourceOutputTypeDef = TypedDict(
    "ListRecoveryPointsByResourceOutputTypeDef",
    {"NextToken": str, "RecoveryPoints": List["RecoveryPointByResourceTypeDef"]},
    total=False,
)

ListRestoreJobsOutputTypeDef = TypedDict(
    "ListRestoreJobsOutputTypeDef",
    {"RestoreJobs": List["RestoreJobsListMemberTypeDef"], "NextToken": str},
    total=False,
)

ListTagsOutputTypeDef = TypedDict(
    "ListTagsOutputTypeDef", {"NextToken": str, "Tags": Dict[str, str]}, total=False
)

StartBackupJobOutputTypeDef = TypedDict(
    "StartBackupJobOutputTypeDef",
    {"BackupJobId": str, "RecoveryPointArn": str, "CreationDate": datetime},
    total=False,
)

StartCopyJobOutputTypeDef = TypedDict(
    "StartCopyJobOutputTypeDef", {"CopyJobId": str, "CreationDate": datetime}, total=False
)

StartRestoreJobOutputTypeDef = TypedDict(
    "StartRestoreJobOutputTypeDef", {"RestoreJobId": str}, total=False
)

UpdateBackupPlanOutputTypeDef = TypedDict(
    "UpdateBackupPlanOutputTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "CreationDate": datetime, "VersionId": str},
    total=False,
)

UpdateRecoveryPointLifecycleOutputTypeDef = TypedDict(
    "UpdateRecoveryPointLifecycleOutputTypeDef",
    {
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "Lifecycle": "LifecycleTypeDef",
        "CalculatedLifecycle": "CalculatedLifecycleTypeDef",
    },
    total=False,
)
