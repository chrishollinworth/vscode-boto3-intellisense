"""
Type annotations for backup service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/type_defs.html)

Usage::

    ```python
    from mypy_boto3_backup.type_defs import AdvancedBackupSettingTypeDef

    data: AdvancedBackupSettingTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AggregationPeriodType,
    BackupJobStateType,
    BackupJobStatusType,
    BackupVaultEventType,
    CopyJobStateType,
    CopyJobStatusType,
    LegalHoldStatusType,
    RecoveryPointStatusType,
    RestoreJobStateType,
    RestoreJobStatusType,
    StorageClassType,
    VaultStateType,
    VaultTypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AdvancedBackupSettingTypeDef",
    "BackupJobSummaryTypeDef",
    "BackupJobTypeDef",
    "BackupPlanInputTypeDef",
    "BackupPlanTemplatesListMemberTypeDef",
    "BackupPlanTypeDef",
    "BackupPlansListMemberTypeDef",
    "BackupRuleInputTypeDef",
    "BackupRuleTypeDef",
    "BackupSelectionTypeDef",
    "BackupSelectionsListMemberTypeDef",
    "BackupVaultListMemberTypeDef",
    "CalculatedLifecycleTypeDef",
    "CancelLegalHoldInputRequestTypeDef",
    "ConditionParameterTypeDef",
    "ConditionTypeDef",
    "ConditionsTypeDef",
    "ControlInputParameterTypeDef",
    "ControlScopeTypeDef",
    "CopyActionTypeDef",
    "CopyJobSummaryTypeDef",
    "CopyJobTypeDef",
    "CreateBackupPlanInputRequestTypeDef",
    "CreateBackupPlanOutputTypeDef",
    "CreateBackupSelectionInputRequestTypeDef",
    "CreateBackupSelectionOutputTypeDef",
    "CreateBackupVaultInputRequestTypeDef",
    "CreateBackupVaultOutputTypeDef",
    "CreateFrameworkInputRequestTypeDef",
    "CreateFrameworkOutputTypeDef",
    "CreateLegalHoldInputRequestTypeDef",
    "CreateLegalHoldOutputTypeDef",
    "CreateLogicallyAirGappedBackupVaultInputRequestTypeDef",
    "CreateLogicallyAirGappedBackupVaultOutputTypeDef",
    "CreateReportPlanInputRequestTypeDef",
    "CreateReportPlanOutputTypeDef",
    "DateRangeTypeDef",
    "DeleteBackupPlanInputRequestTypeDef",
    "DeleteBackupPlanOutputTypeDef",
    "DeleteBackupSelectionInputRequestTypeDef",
    "DeleteBackupVaultAccessPolicyInputRequestTypeDef",
    "DeleteBackupVaultInputRequestTypeDef",
    "DeleteBackupVaultLockConfigurationInputRequestTypeDef",
    "DeleteBackupVaultNotificationsInputRequestTypeDef",
    "DeleteFrameworkInputRequestTypeDef",
    "DeleteRecoveryPointInputRequestTypeDef",
    "DeleteReportPlanInputRequestTypeDef",
    "DescribeBackupJobInputRequestTypeDef",
    "DescribeBackupJobOutputTypeDef",
    "DescribeBackupVaultInputRequestTypeDef",
    "DescribeBackupVaultOutputTypeDef",
    "DescribeCopyJobInputRequestTypeDef",
    "DescribeCopyJobOutputTypeDef",
    "DescribeFrameworkInputRequestTypeDef",
    "DescribeFrameworkOutputTypeDef",
    "DescribeGlobalSettingsOutputTypeDef",
    "DescribeProtectedResourceInputRequestTypeDef",
    "DescribeProtectedResourceOutputTypeDef",
    "DescribeRecoveryPointInputRequestTypeDef",
    "DescribeRecoveryPointOutputTypeDef",
    "DescribeRegionSettingsOutputTypeDef",
    "DescribeReportJobInputRequestTypeDef",
    "DescribeReportJobOutputTypeDef",
    "DescribeReportPlanInputRequestTypeDef",
    "DescribeReportPlanOutputTypeDef",
    "DescribeRestoreJobInputRequestTypeDef",
    "DescribeRestoreJobOutputTypeDef",
    "DisassociateRecoveryPointFromParentInputRequestTypeDef",
    "DisassociateRecoveryPointInputRequestTypeDef",
    "ExportBackupPlanTemplateInputRequestTypeDef",
    "ExportBackupPlanTemplateOutputTypeDef",
    "FrameworkControlTypeDef",
    "FrameworkTypeDef",
    "GetBackupPlanFromJSONInputRequestTypeDef",
    "GetBackupPlanFromJSONOutputTypeDef",
    "GetBackupPlanFromTemplateInputRequestTypeDef",
    "GetBackupPlanFromTemplateOutputTypeDef",
    "GetBackupPlanInputRequestTypeDef",
    "GetBackupPlanOutputTypeDef",
    "GetBackupSelectionInputRequestTypeDef",
    "GetBackupSelectionOutputTypeDef",
    "GetBackupVaultAccessPolicyInputRequestTypeDef",
    "GetBackupVaultAccessPolicyOutputTypeDef",
    "GetBackupVaultNotificationsInputRequestTypeDef",
    "GetBackupVaultNotificationsOutputTypeDef",
    "GetLegalHoldInputRequestTypeDef",
    "GetLegalHoldOutputTypeDef",
    "GetRecoveryPointRestoreMetadataInputRequestTypeDef",
    "GetRecoveryPointRestoreMetadataOutputTypeDef",
    "GetSupportedResourceTypesOutputTypeDef",
    "LegalHoldTypeDef",
    "LifecycleTypeDef",
    "ListBackupJobSummariesInputRequestTypeDef",
    "ListBackupJobSummariesOutputTypeDef",
    "ListBackupJobsInputRequestTypeDef",
    "ListBackupJobsOutputTypeDef",
    "ListBackupPlanTemplatesInputRequestTypeDef",
    "ListBackupPlanTemplatesOutputTypeDef",
    "ListBackupPlanVersionsInputRequestTypeDef",
    "ListBackupPlanVersionsOutputTypeDef",
    "ListBackupPlansInputRequestTypeDef",
    "ListBackupPlansOutputTypeDef",
    "ListBackupSelectionsInputRequestTypeDef",
    "ListBackupSelectionsOutputTypeDef",
    "ListBackupVaultsInputRequestTypeDef",
    "ListBackupVaultsOutputTypeDef",
    "ListCopyJobSummariesInputRequestTypeDef",
    "ListCopyJobSummariesOutputTypeDef",
    "ListCopyJobsInputRequestTypeDef",
    "ListCopyJobsOutputTypeDef",
    "ListFrameworksInputRequestTypeDef",
    "ListFrameworksOutputTypeDef",
    "ListLegalHoldsInputRequestTypeDef",
    "ListLegalHoldsOutputTypeDef",
    "ListProtectedResourcesByBackupVaultInputRequestTypeDef",
    "ListProtectedResourcesByBackupVaultOutputTypeDef",
    "ListProtectedResourcesInputRequestTypeDef",
    "ListProtectedResourcesOutputTypeDef",
    "ListRecoveryPointsByBackupVaultInputRequestTypeDef",
    "ListRecoveryPointsByBackupVaultOutputTypeDef",
    "ListRecoveryPointsByLegalHoldInputRequestTypeDef",
    "ListRecoveryPointsByLegalHoldOutputTypeDef",
    "ListRecoveryPointsByResourceInputRequestTypeDef",
    "ListRecoveryPointsByResourceOutputTypeDef",
    "ListReportJobsInputRequestTypeDef",
    "ListReportJobsOutputTypeDef",
    "ListReportPlansInputRequestTypeDef",
    "ListReportPlansOutputTypeDef",
    "ListRestoreJobSummariesInputRequestTypeDef",
    "ListRestoreJobSummariesOutputTypeDef",
    "ListRestoreJobsInputRequestTypeDef",
    "ListRestoreJobsOutputTypeDef",
    "ListTagsInputRequestTypeDef",
    "ListTagsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ProtectedResourceTypeDef",
    "PutBackupVaultAccessPolicyInputRequestTypeDef",
    "PutBackupVaultLockConfigurationInputRequestTypeDef",
    "PutBackupVaultNotificationsInputRequestTypeDef",
    "RecoveryPointByBackupVaultTypeDef",
    "RecoveryPointByResourceTypeDef",
    "RecoveryPointCreatorTypeDef",
    "RecoveryPointMemberTypeDef",
    "RecoveryPointSelectionTypeDef",
    "ReportDeliveryChannelTypeDef",
    "ReportDestinationTypeDef",
    "ReportJobTypeDef",
    "ReportPlanTypeDef",
    "ReportSettingTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreJobSummaryTypeDef",
    "RestoreJobsListMemberTypeDef",
    "StartBackupJobInputRequestTypeDef",
    "StartBackupJobOutputTypeDef",
    "StartCopyJobInputRequestTypeDef",
    "StartCopyJobOutputTypeDef",
    "StartReportJobInputRequestTypeDef",
    "StartReportJobOutputTypeDef",
    "StartRestoreJobInputRequestTypeDef",
    "StartRestoreJobOutputTypeDef",
    "StopBackupJobInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateBackupPlanInputRequestTypeDef",
    "UpdateBackupPlanOutputTypeDef",
    "UpdateFrameworkInputRequestTypeDef",
    "UpdateFrameworkOutputTypeDef",
    "UpdateGlobalSettingsInputRequestTypeDef",
    "UpdateRecoveryPointLifecycleInputRequestTypeDef",
    "UpdateRecoveryPointLifecycleOutputTypeDef",
    "UpdateRegionSettingsInputRequestTypeDef",
    "UpdateReportPlanInputRequestTypeDef",
    "UpdateReportPlanOutputTypeDef",
)

AdvancedBackupSettingTypeDef = TypedDict(
    "AdvancedBackupSettingTypeDef",
    {
        "ResourceType": str,
        "BackupOptions": Dict[str, str],
    },
    total=False,
)

BackupJobSummaryTypeDef = TypedDict(
    "BackupJobSummaryTypeDef",
    {
        "Region": str,
        "AccountId": str,
        "State": BackupJobStatusType,
        "ResourceType": str,
        "MessageCategory": str,
        "Count": int,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
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
        "State": BackupJobStateType,
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": "RecoveryPointCreatorTypeDef",
        "ExpectedCompletionDate": datetime,
        "StartBy": datetime,
        "ResourceType": str,
        "BytesTransferred": int,
        "BackupOptions": Dict[str, str],
        "BackupType": str,
        "ParentJobId": str,
        "IsParent": bool,
        "ResourceName": str,
        "MessageCategory": str,
    },
    total=False,
)

_RequiredBackupPlanInputTypeDef = TypedDict(
    "_RequiredBackupPlanInputTypeDef",
    {
        "BackupPlanName": str,
        "Rules": List["BackupRuleInputTypeDef"],
    },
)
_OptionalBackupPlanInputTypeDef = TypedDict(
    "_OptionalBackupPlanInputTypeDef",
    {
        "AdvancedBackupSettings": List["AdvancedBackupSettingTypeDef"],
    },
    total=False,
)

class BackupPlanInputTypeDef(_RequiredBackupPlanInputTypeDef, _OptionalBackupPlanInputTypeDef):
    pass

BackupPlanTemplatesListMemberTypeDef = TypedDict(
    "BackupPlanTemplatesListMemberTypeDef",
    {
        "BackupPlanTemplateId": str,
        "BackupPlanTemplateName": str,
    },
    total=False,
)

_RequiredBackupPlanTypeDef = TypedDict(
    "_RequiredBackupPlanTypeDef",
    {
        "BackupPlanName": str,
        "Rules": List["BackupRuleTypeDef"],
    },
)
_OptionalBackupPlanTypeDef = TypedDict(
    "_OptionalBackupPlanTypeDef",
    {
        "AdvancedBackupSettings": List["AdvancedBackupSettingTypeDef"],
    },
    total=False,
)

class BackupPlanTypeDef(_RequiredBackupPlanTypeDef, _OptionalBackupPlanTypeDef):
    pass

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
        "AdvancedBackupSettings": List["AdvancedBackupSettingTypeDef"],
    },
    total=False,
)

_RequiredBackupRuleInputTypeDef = TypedDict(
    "_RequiredBackupRuleInputTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
    },
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
        "EnableContinuousBackup": bool,
        "ScheduleExpressionTimezone": str,
    },
    total=False,
)

class BackupRuleInputTypeDef(_RequiredBackupRuleInputTypeDef, _OptionalBackupRuleInputTypeDef):
    pass

_RequiredBackupRuleTypeDef = TypedDict(
    "_RequiredBackupRuleTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
    },
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
        "EnableContinuousBackup": bool,
        "ScheduleExpressionTimezone": str,
    },
    total=False,
)

class BackupRuleTypeDef(_RequiredBackupRuleTypeDef, _OptionalBackupRuleTypeDef):
    pass

_RequiredBackupSelectionTypeDef = TypedDict(
    "_RequiredBackupSelectionTypeDef",
    {
        "SelectionName": str,
        "IamRoleArn": str,
    },
)
_OptionalBackupSelectionTypeDef = TypedDict(
    "_OptionalBackupSelectionTypeDef",
    {
        "Resources": List[str],
        "ListOfTags": List["ConditionTypeDef"],
        "NotResources": List[str],
        "Conditions": "ConditionsTypeDef",
    },
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
        "Locked": bool,
        "MinRetentionDays": int,
        "MaxRetentionDays": int,
        "LockDate": datetime,
    },
    total=False,
)

CalculatedLifecycleTypeDef = TypedDict(
    "CalculatedLifecycleTypeDef",
    {
        "MoveToColdStorageAt": datetime,
        "DeleteAt": datetime,
    },
    total=False,
)

_RequiredCancelLegalHoldInputRequestTypeDef = TypedDict(
    "_RequiredCancelLegalHoldInputRequestTypeDef",
    {
        "LegalHoldId": str,
        "CancelDescription": str,
    },
)
_OptionalCancelLegalHoldInputRequestTypeDef = TypedDict(
    "_OptionalCancelLegalHoldInputRequestTypeDef",
    {
        "RetainRecordInDays": int,
    },
    total=False,
)

class CancelLegalHoldInputRequestTypeDef(
    _RequiredCancelLegalHoldInputRequestTypeDef, _OptionalCancelLegalHoldInputRequestTypeDef
):
    pass

ConditionParameterTypeDef = TypedDict(
    "ConditionParameterTypeDef",
    {
        "ConditionKey": str,
        "ConditionValue": str,
    },
    total=False,
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "ConditionType": Literal["STRINGEQUALS"],
        "ConditionKey": str,
        "ConditionValue": str,
    },
)

ConditionsTypeDef = TypedDict(
    "ConditionsTypeDef",
    {
        "StringEquals": List["ConditionParameterTypeDef"],
        "StringNotEquals": List["ConditionParameterTypeDef"],
        "StringLike": List["ConditionParameterTypeDef"],
        "StringNotLike": List["ConditionParameterTypeDef"],
    },
    total=False,
)

ControlInputParameterTypeDef = TypedDict(
    "ControlInputParameterTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
    },
    total=False,
)

ControlScopeTypeDef = TypedDict(
    "ControlScopeTypeDef",
    {
        "ComplianceResourceIds": List[str],
        "ComplianceResourceTypes": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredCopyActionTypeDef = TypedDict(
    "_RequiredCopyActionTypeDef",
    {
        "DestinationBackupVaultArn": str,
    },
)
_OptionalCopyActionTypeDef = TypedDict(
    "_OptionalCopyActionTypeDef",
    {
        "Lifecycle": "LifecycleTypeDef",
    },
    total=False,
)

class CopyActionTypeDef(_RequiredCopyActionTypeDef, _OptionalCopyActionTypeDef):
    pass

CopyJobSummaryTypeDef = TypedDict(
    "CopyJobSummaryTypeDef",
    {
        "Region": str,
        "AccountId": str,
        "State": CopyJobStatusType,
        "ResourceType": str,
        "MessageCategory": str,
        "Count": int,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

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
        "State": CopyJobStateType,
        "StatusMessage": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": "RecoveryPointCreatorTypeDef",
        "ResourceType": str,
        "ParentJobId": str,
        "IsParent": bool,
        "CompositeMemberIdentifier": str,
        "NumberOfChildJobs": int,
        "ChildJobsInState": Dict[CopyJobStateType, int],
        "ResourceName": str,
        "MessageCategory": str,
    },
    total=False,
)

_RequiredCreateBackupPlanInputRequestTypeDef = TypedDict(
    "_RequiredCreateBackupPlanInputRequestTypeDef",
    {
        "BackupPlan": "BackupPlanInputTypeDef",
    },
)
_OptionalCreateBackupPlanInputRequestTypeDef = TypedDict(
    "_OptionalCreateBackupPlanInputRequestTypeDef",
    {
        "BackupPlanTags": Dict[str, str],
        "CreatorRequestId": str,
    },
    total=False,
)

class CreateBackupPlanInputRequestTypeDef(
    _RequiredCreateBackupPlanInputRequestTypeDef, _OptionalCreateBackupPlanInputRequestTypeDef
):
    pass

CreateBackupPlanOutputTypeDef = TypedDict(
    "CreateBackupPlanOutputTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "CreationDate": datetime,
        "VersionId": str,
        "AdvancedBackupSettings": List["AdvancedBackupSettingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBackupSelectionInputRequestTypeDef = TypedDict(
    "_RequiredCreateBackupSelectionInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "BackupSelection": "BackupSelectionTypeDef",
    },
)
_OptionalCreateBackupSelectionInputRequestTypeDef = TypedDict(
    "_OptionalCreateBackupSelectionInputRequestTypeDef",
    {
        "CreatorRequestId": str,
    },
    total=False,
)

class CreateBackupSelectionInputRequestTypeDef(
    _RequiredCreateBackupSelectionInputRequestTypeDef,
    _OptionalCreateBackupSelectionInputRequestTypeDef,
):
    pass

CreateBackupSelectionOutputTypeDef = TypedDict(
    "CreateBackupSelectionOutputTypeDef",
    {
        "SelectionId": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBackupVaultInputRequestTypeDef = TypedDict(
    "_RequiredCreateBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)
_OptionalCreateBackupVaultInputRequestTypeDef = TypedDict(
    "_OptionalCreateBackupVaultInputRequestTypeDef",
    {
        "BackupVaultTags": Dict[str, str],
        "EncryptionKeyArn": str,
        "CreatorRequestId": str,
    },
    total=False,
)

class CreateBackupVaultInputRequestTypeDef(
    _RequiredCreateBackupVaultInputRequestTypeDef, _OptionalCreateBackupVaultInputRequestTypeDef
):
    pass

CreateBackupVaultOutputTypeDef = TypedDict(
    "CreateBackupVaultOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "CreationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFrameworkInputRequestTypeDef = TypedDict(
    "_RequiredCreateFrameworkInputRequestTypeDef",
    {
        "FrameworkName": str,
        "FrameworkControls": List["FrameworkControlTypeDef"],
    },
)
_OptionalCreateFrameworkInputRequestTypeDef = TypedDict(
    "_OptionalCreateFrameworkInputRequestTypeDef",
    {
        "FrameworkDescription": str,
        "IdempotencyToken": str,
        "FrameworkTags": Dict[str, str],
    },
    total=False,
)

class CreateFrameworkInputRequestTypeDef(
    _RequiredCreateFrameworkInputRequestTypeDef, _OptionalCreateFrameworkInputRequestTypeDef
):
    pass

CreateFrameworkOutputTypeDef = TypedDict(
    "CreateFrameworkOutputTypeDef",
    {
        "FrameworkName": str,
        "FrameworkArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLegalHoldInputRequestTypeDef = TypedDict(
    "_RequiredCreateLegalHoldInputRequestTypeDef",
    {
        "Title": str,
        "Description": str,
    },
)
_OptionalCreateLegalHoldInputRequestTypeDef = TypedDict(
    "_OptionalCreateLegalHoldInputRequestTypeDef",
    {
        "IdempotencyToken": str,
        "RecoveryPointSelection": "RecoveryPointSelectionTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateLegalHoldInputRequestTypeDef(
    _RequiredCreateLegalHoldInputRequestTypeDef, _OptionalCreateLegalHoldInputRequestTypeDef
):
    pass

CreateLegalHoldOutputTypeDef = TypedDict(
    "CreateLegalHoldOutputTypeDef",
    {
        "Title": str,
        "Status": LegalHoldStatusType,
        "Description": str,
        "LegalHoldId": str,
        "LegalHoldArn": str,
        "CreationDate": datetime,
        "RecoveryPointSelection": "RecoveryPointSelectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLogicallyAirGappedBackupVaultInputRequestTypeDef = TypedDict(
    "_RequiredCreateLogicallyAirGappedBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "MinRetentionDays": int,
        "MaxRetentionDays": int,
    },
)
_OptionalCreateLogicallyAirGappedBackupVaultInputRequestTypeDef = TypedDict(
    "_OptionalCreateLogicallyAirGappedBackupVaultInputRequestTypeDef",
    {
        "BackupVaultTags": Dict[str, str],
        "CreatorRequestId": str,
    },
    total=False,
)

class CreateLogicallyAirGappedBackupVaultInputRequestTypeDef(
    _RequiredCreateLogicallyAirGappedBackupVaultInputRequestTypeDef,
    _OptionalCreateLogicallyAirGappedBackupVaultInputRequestTypeDef,
):
    pass

CreateLogicallyAirGappedBackupVaultOutputTypeDef = TypedDict(
    "CreateLogicallyAirGappedBackupVaultOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "CreationDate": datetime,
        "VaultState": VaultStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReportPlanInputRequestTypeDef = TypedDict(
    "_RequiredCreateReportPlanInputRequestTypeDef",
    {
        "ReportPlanName": str,
        "ReportDeliveryChannel": "ReportDeliveryChannelTypeDef",
        "ReportSetting": "ReportSettingTypeDef",
    },
)
_OptionalCreateReportPlanInputRequestTypeDef = TypedDict(
    "_OptionalCreateReportPlanInputRequestTypeDef",
    {
        "ReportPlanDescription": str,
        "ReportPlanTags": Dict[str, str],
        "IdempotencyToken": str,
    },
    total=False,
)

class CreateReportPlanInputRequestTypeDef(
    _RequiredCreateReportPlanInputRequestTypeDef, _OptionalCreateReportPlanInputRequestTypeDef
):
    pass

CreateReportPlanOutputTypeDef = TypedDict(
    "CreateReportPlanOutputTypeDef",
    {
        "ReportPlanName": str,
        "ReportPlanArn": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DateRangeTypeDef = TypedDict(
    "DateRangeTypeDef",
    {
        "FromDate": Union[datetime, str],
        "ToDate": Union[datetime, str],
    },
)

DeleteBackupPlanInputRequestTypeDef = TypedDict(
    "DeleteBackupPlanInputRequestTypeDef",
    {
        "BackupPlanId": str,
    },
)

DeleteBackupPlanOutputTypeDef = TypedDict(
    "DeleteBackupPlanOutputTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "DeletionDate": datetime,
        "VersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackupSelectionInputRequestTypeDef = TypedDict(
    "DeleteBackupSelectionInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "SelectionId": str,
    },
)

DeleteBackupVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "DeleteBackupVaultAccessPolicyInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

DeleteBackupVaultInputRequestTypeDef = TypedDict(
    "DeleteBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

DeleteBackupVaultLockConfigurationInputRequestTypeDef = TypedDict(
    "DeleteBackupVaultLockConfigurationInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

DeleteBackupVaultNotificationsInputRequestTypeDef = TypedDict(
    "DeleteBackupVaultNotificationsInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

DeleteFrameworkInputRequestTypeDef = TypedDict(
    "DeleteFrameworkInputRequestTypeDef",
    {
        "FrameworkName": str,
    },
)

DeleteRecoveryPointInputRequestTypeDef = TypedDict(
    "DeleteRecoveryPointInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)

DeleteReportPlanInputRequestTypeDef = TypedDict(
    "DeleteReportPlanInputRequestTypeDef",
    {
        "ReportPlanName": str,
    },
)

DescribeBackupJobInputRequestTypeDef = TypedDict(
    "DescribeBackupJobInputRequestTypeDef",
    {
        "BackupJobId": str,
    },
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
        "State": BackupJobStateType,
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": "RecoveryPointCreatorTypeDef",
        "ResourceType": str,
        "BytesTransferred": int,
        "ExpectedCompletionDate": datetime,
        "StartBy": datetime,
        "BackupOptions": Dict[str, str],
        "BackupType": str,
        "ParentJobId": str,
        "IsParent": bool,
        "NumberOfChildJobs": int,
        "ChildJobsInState": Dict[BackupJobStateType, int],
        "ResourceName": str,
        "MessageCategory": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeBackupVaultInputRequestTypeDef = TypedDict(
    "_RequiredDescribeBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)
_OptionalDescribeBackupVaultInputRequestTypeDef = TypedDict(
    "_OptionalDescribeBackupVaultInputRequestTypeDef",
    {
        "BackupVaultAccountId": str,
    },
    total=False,
)

class DescribeBackupVaultInputRequestTypeDef(
    _RequiredDescribeBackupVaultInputRequestTypeDef, _OptionalDescribeBackupVaultInputRequestTypeDef
):
    pass

DescribeBackupVaultOutputTypeDef = TypedDict(
    "DescribeBackupVaultOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "VaultType": VaultTypeType,
        "EncryptionKeyArn": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "NumberOfRecoveryPoints": int,
        "Locked": bool,
        "MinRetentionDays": int,
        "MaxRetentionDays": int,
        "LockDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCopyJobInputRequestTypeDef = TypedDict(
    "DescribeCopyJobInputRequestTypeDef",
    {
        "CopyJobId": str,
    },
)

DescribeCopyJobOutputTypeDef = TypedDict(
    "DescribeCopyJobOutputTypeDef",
    {
        "CopyJob": "CopyJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFrameworkInputRequestTypeDef = TypedDict(
    "DescribeFrameworkInputRequestTypeDef",
    {
        "FrameworkName": str,
    },
)

DescribeFrameworkOutputTypeDef = TypedDict(
    "DescribeFrameworkOutputTypeDef",
    {
        "FrameworkName": str,
        "FrameworkArn": str,
        "FrameworkDescription": str,
        "FrameworkControls": List["FrameworkControlTypeDef"],
        "CreationTime": datetime,
        "DeploymentStatus": str,
        "FrameworkStatus": str,
        "IdempotencyToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGlobalSettingsOutputTypeDef = TypedDict(
    "DescribeGlobalSettingsOutputTypeDef",
    {
        "GlobalSettings": Dict[str, str],
        "LastUpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProtectedResourceInputRequestTypeDef = TypedDict(
    "DescribeProtectedResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeProtectedResourceOutputTypeDef = TypedDict(
    "DescribeProtectedResourceOutputTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": str,
        "LastBackupTime": datetime,
        "ResourceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRecoveryPointInputRequestTypeDef = TypedDict(
    "_RequiredDescribeRecoveryPointInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)
_OptionalDescribeRecoveryPointInputRequestTypeDef = TypedDict(
    "_OptionalDescribeRecoveryPointInputRequestTypeDef",
    {
        "BackupVaultAccountId": str,
    },
    total=False,
)

class DescribeRecoveryPointInputRequestTypeDef(
    _RequiredDescribeRecoveryPointInputRequestTypeDef,
    _OptionalDescribeRecoveryPointInputRequestTypeDef,
):
    pass

DescribeRecoveryPointOutputTypeDef = TypedDict(
    "DescribeRecoveryPointOutputTypeDef",
    {
        "RecoveryPointArn": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "SourceBackupVaultArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "CreatedBy": "RecoveryPointCreatorTypeDef",
        "IamRoleArn": str,
        "Status": RecoveryPointStatusType,
        "StatusMessage": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "BackupSizeInBytes": int,
        "CalculatedLifecycle": "CalculatedLifecycleTypeDef",
        "Lifecycle": "LifecycleTypeDef",
        "EncryptionKeyArn": str,
        "IsEncrypted": bool,
        "StorageClass": StorageClassType,
        "LastRestoreTime": datetime,
        "ParentRecoveryPointArn": str,
        "CompositeMemberIdentifier": str,
        "IsParent": bool,
        "ResourceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRegionSettingsOutputTypeDef = TypedDict(
    "DescribeRegionSettingsOutputTypeDef",
    {
        "ResourceTypeOptInPreference": Dict[str, bool],
        "ResourceTypeManagementPreference": Dict[str, bool],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReportJobInputRequestTypeDef = TypedDict(
    "DescribeReportJobInputRequestTypeDef",
    {
        "ReportJobId": str,
    },
)

DescribeReportJobOutputTypeDef = TypedDict(
    "DescribeReportJobOutputTypeDef",
    {
        "ReportJob": "ReportJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReportPlanInputRequestTypeDef = TypedDict(
    "DescribeReportPlanInputRequestTypeDef",
    {
        "ReportPlanName": str,
    },
)

DescribeReportPlanOutputTypeDef = TypedDict(
    "DescribeReportPlanOutputTypeDef",
    {
        "ReportPlan": "ReportPlanTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRestoreJobInputRequestTypeDef = TypedDict(
    "DescribeRestoreJobInputRequestTypeDef",
    {
        "RestoreJobId": str,
    },
)

DescribeRestoreJobOutputTypeDef = TypedDict(
    "DescribeRestoreJobOutputTypeDef",
    {
        "AccountId": str,
        "RestoreJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "Status": RestoreJobStatusType,
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "ExpectedCompletionTimeMinutes": int,
        "CreatedResourceArn": str,
        "ResourceType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateRecoveryPointFromParentInputRequestTypeDef = TypedDict(
    "DisassociateRecoveryPointFromParentInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)

DisassociateRecoveryPointInputRequestTypeDef = TypedDict(
    "DisassociateRecoveryPointInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)

ExportBackupPlanTemplateInputRequestTypeDef = TypedDict(
    "ExportBackupPlanTemplateInputRequestTypeDef",
    {
        "BackupPlanId": str,
    },
)

ExportBackupPlanTemplateOutputTypeDef = TypedDict(
    "ExportBackupPlanTemplateOutputTypeDef",
    {
        "BackupPlanTemplateJson": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFrameworkControlTypeDef = TypedDict(
    "_RequiredFrameworkControlTypeDef",
    {
        "ControlName": str,
    },
)
_OptionalFrameworkControlTypeDef = TypedDict(
    "_OptionalFrameworkControlTypeDef",
    {
        "ControlInputParameters": List["ControlInputParameterTypeDef"],
        "ControlScope": "ControlScopeTypeDef",
    },
    total=False,
)

class FrameworkControlTypeDef(_RequiredFrameworkControlTypeDef, _OptionalFrameworkControlTypeDef):
    pass

FrameworkTypeDef = TypedDict(
    "FrameworkTypeDef",
    {
        "FrameworkName": str,
        "FrameworkArn": str,
        "FrameworkDescription": str,
        "NumberOfControls": int,
        "CreationTime": datetime,
        "DeploymentStatus": str,
    },
    total=False,
)

GetBackupPlanFromJSONInputRequestTypeDef = TypedDict(
    "GetBackupPlanFromJSONInputRequestTypeDef",
    {
        "BackupPlanTemplateJson": str,
    },
)

GetBackupPlanFromJSONOutputTypeDef = TypedDict(
    "GetBackupPlanFromJSONOutputTypeDef",
    {
        "BackupPlan": "BackupPlanTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackupPlanFromTemplateInputRequestTypeDef = TypedDict(
    "GetBackupPlanFromTemplateInputRequestTypeDef",
    {
        "BackupPlanTemplateId": str,
    },
)

GetBackupPlanFromTemplateOutputTypeDef = TypedDict(
    "GetBackupPlanFromTemplateOutputTypeDef",
    {
        "BackupPlanDocument": "BackupPlanTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBackupPlanInputRequestTypeDef = TypedDict(
    "_RequiredGetBackupPlanInputRequestTypeDef",
    {
        "BackupPlanId": str,
    },
)
_OptionalGetBackupPlanInputRequestTypeDef = TypedDict(
    "_OptionalGetBackupPlanInputRequestTypeDef",
    {
        "VersionId": str,
    },
    total=False,
)

class GetBackupPlanInputRequestTypeDef(
    _RequiredGetBackupPlanInputRequestTypeDef, _OptionalGetBackupPlanInputRequestTypeDef
):
    pass

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
        "AdvancedBackupSettings": List["AdvancedBackupSettingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackupSelectionInputRequestTypeDef = TypedDict(
    "GetBackupSelectionInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "SelectionId": str,
    },
)

GetBackupSelectionOutputTypeDef = TypedDict(
    "GetBackupSelectionOutputTypeDef",
    {
        "BackupSelection": "BackupSelectionTypeDef",
        "SelectionId": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackupVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "GetBackupVaultAccessPolicyInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

GetBackupVaultAccessPolicyOutputTypeDef = TypedDict(
    "GetBackupVaultAccessPolicyOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackupVaultNotificationsInputRequestTypeDef = TypedDict(
    "GetBackupVaultNotificationsInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

GetBackupVaultNotificationsOutputTypeDef = TypedDict(
    "GetBackupVaultNotificationsOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "SNSTopicArn": str,
        "BackupVaultEvents": List[BackupVaultEventType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLegalHoldInputRequestTypeDef = TypedDict(
    "GetLegalHoldInputRequestTypeDef",
    {
        "LegalHoldId": str,
    },
)

GetLegalHoldOutputTypeDef = TypedDict(
    "GetLegalHoldOutputTypeDef",
    {
        "Title": str,
        "Status": LegalHoldStatusType,
        "Description": str,
        "CancelDescription": str,
        "LegalHoldId": str,
        "LegalHoldArn": str,
        "CreationDate": datetime,
        "CancellationDate": datetime,
        "RetainRecordUntil": datetime,
        "RecoveryPointSelection": "RecoveryPointSelectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRecoveryPointRestoreMetadataInputRequestTypeDef = TypedDict(
    "_RequiredGetRecoveryPointRestoreMetadataInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)
_OptionalGetRecoveryPointRestoreMetadataInputRequestTypeDef = TypedDict(
    "_OptionalGetRecoveryPointRestoreMetadataInputRequestTypeDef",
    {
        "BackupVaultAccountId": str,
    },
    total=False,
)

class GetRecoveryPointRestoreMetadataInputRequestTypeDef(
    _RequiredGetRecoveryPointRestoreMetadataInputRequestTypeDef,
    _OptionalGetRecoveryPointRestoreMetadataInputRequestTypeDef,
):
    pass

GetRecoveryPointRestoreMetadataOutputTypeDef = TypedDict(
    "GetRecoveryPointRestoreMetadataOutputTypeDef",
    {
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "RestoreMetadata": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSupportedResourceTypesOutputTypeDef = TypedDict(
    "GetSupportedResourceTypesOutputTypeDef",
    {
        "ResourceTypes": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LegalHoldTypeDef = TypedDict(
    "LegalHoldTypeDef",
    {
        "Title": str,
        "Status": LegalHoldStatusType,
        "Description": str,
        "LegalHoldId": str,
        "LegalHoldArn": str,
        "CreationDate": datetime,
        "CancellationDate": datetime,
    },
    total=False,
)

LifecycleTypeDef = TypedDict(
    "LifecycleTypeDef",
    {
        "MoveToColdStorageAfterDays": int,
        "DeleteAfterDays": int,
    },
    total=False,
)

ListBackupJobSummariesInputRequestTypeDef = TypedDict(
    "ListBackupJobSummariesInputRequestTypeDef",
    {
        "AccountId": str,
        "State": BackupJobStatusType,
        "ResourceType": str,
        "MessageCategory": str,
        "AggregationPeriod": AggregationPeriodType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListBackupJobSummariesOutputTypeDef = TypedDict(
    "ListBackupJobSummariesOutputTypeDef",
    {
        "BackupJobSummaries": List["BackupJobSummaryTypeDef"],
        "AggregationPeriod": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackupJobsInputRequestTypeDef = TypedDict(
    "ListBackupJobsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ByResourceArn": str,
        "ByState": BackupJobStateType,
        "ByBackupVaultName": str,
        "ByCreatedBefore": Union[datetime, str],
        "ByCreatedAfter": Union[datetime, str],
        "ByResourceType": str,
        "ByAccountId": str,
        "ByCompleteAfter": Union[datetime, str],
        "ByCompleteBefore": Union[datetime, str],
        "ByParentJobId": str,
        "ByMessageCategory": str,
    },
    total=False,
)

ListBackupJobsOutputTypeDef = TypedDict(
    "ListBackupJobsOutputTypeDef",
    {
        "BackupJobs": List["BackupJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackupPlanTemplatesInputRequestTypeDef = TypedDict(
    "ListBackupPlanTemplatesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListBackupPlanTemplatesOutputTypeDef = TypedDict(
    "ListBackupPlanTemplatesOutputTypeDef",
    {
        "NextToken": str,
        "BackupPlanTemplatesList": List["BackupPlanTemplatesListMemberTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBackupPlanVersionsInputRequestTypeDef = TypedDict(
    "_RequiredListBackupPlanVersionsInputRequestTypeDef",
    {
        "BackupPlanId": str,
    },
)
_OptionalListBackupPlanVersionsInputRequestTypeDef = TypedDict(
    "_OptionalListBackupPlanVersionsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListBackupPlanVersionsInputRequestTypeDef(
    _RequiredListBackupPlanVersionsInputRequestTypeDef,
    _OptionalListBackupPlanVersionsInputRequestTypeDef,
):
    pass

ListBackupPlanVersionsOutputTypeDef = TypedDict(
    "ListBackupPlanVersionsOutputTypeDef",
    {
        "NextToken": str,
        "BackupPlanVersionsList": List["BackupPlansListMemberTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackupPlansInputRequestTypeDef = TypedDict(
    "ListBackupPlansInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "IncludeDeleted": bool,
    },
    total=False,
)

ListBackupPlansOutputTypeDef = TypedDict(
    "ListBackupPlansOutputTypeDef",
    {
        "NextToken": str,
        "BackupPlansList": List["BackupPlansListMemberTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBackupSelectionsInputRequestTypeDef = TypedDict(
    "_RequiredListBackupSelectionsInputRequestTypeDef",
    {
        "BackupPlanId": str,
    },
)
_OptionalListBackupSelectionsInputRequestTypeDef = TypedDict(
    "_OptionalListBackupSelectionsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListBackupSelectionsInputRequestTypeDef(
    _RequiredListBackupSelectionsInputRequestTypeDef,
    _OptionalListBackupSelectionsInputRequestTypeDef,
):
    pass

ListBackupSelectionsOutputTypeDef = TypedDict(
    "ListBackupSelectionsOutputTypeDef",
    {
        "NextToken": str,
        "BackupSelectionsList": List["BackupSelectionsListMemberTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackupVaultsInputRequestTypeDef = TypedDict(
    "ListBackupVaultsInputRequestTypeDef",
    {
        "ByVaultType": VaultTypeType,
        "ByShared": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListBackupVaultsOutputTypeDef = TypedDict(
    "ListBackupVaultsOutputTypeDef",
    {
        "BackupVaultList": List["BackupVaultListMemberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCopyJobSummariesInputRequestTypeDef = TypedDict(
    "ListCopyJobSummariesInputRequestTypeDef",
    {
        "AccountId": str,
        "State": CopyJobStatusType,
        "ResourceType": str,
        "MessageCategory": str,
        "AggregationPeriod": AggregationPeriodType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListCopyJobSummariesOutputTypeDef = TypedDict(
    "ListCopyJobSummariesOutputTypeDef",
    {
        "CopyJobSummaries": List["CopyJobSummaryTypeDef"],
        "AggregationPeriod": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCopyJobsInputRequestTypeDef = TypedDict(
    "ListCopyJobsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ByResourceArn": str,
        "ByState": CopyJobStateType,
        "ByCreatedBefore": Union[datetime, str],
        "ByCreatedAfter": Union[datetime, str],
        "ByResourceType": str,
        "ByDestinationVaultArn": str,
        "ByAccountId": str,
        "ByCompleteBefore": Union[datetime, str],
        "ByCompleteAfter": Union[datetime, str],
        "ByParentJobId": str,
        "ByMessageCategory": str,
    },
    total=False,
)

ListCopyJobsOutputTypeDef = TypedDict(
    "ListCopyJobsOutputTypeDef",
    {
        "CopyJobs": List["CopyJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFrameworksInputRequestTypeDef = TypedDict(
    "ListFrameworksInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListFrameworksOutputTypeDef = TypedDict(
    "ListFrameworksOutputTypeDef",
    {
        "Frameworks": List["FrameworkTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLegalHoldsInputRequestTypeDef = TypedDict(
    "ListLegalHoldsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListLegalHoldsOutputTypeDef = TypedDict(
    "ListLegalHoldsOutputTypeDef",
    {
        "NextToken": str,
        "LegalHolds": List["LegalHoldTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProtectedResourcesByBackupVaultInputRequestTypeDef = TypedDict(
    "_RequiredListProtectedResourcesByBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)
_OptionalListProtectedResourcesByBackupVaultInputRequestTypeDef = TypedDict(
    "_OptionalListProtectedResourcesByBackupVaultInputRequestTypeDef",
    {
        "BackupVaultAccountId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListProtectedResourcesByBackupVaultInputRequestTypeDef(
    _RequiredListProtectedResourcesByBackupVaultInputRequestTypeDef,
    _OptionalListProtectedResourcesByBackupVaultInputRequestTypeDef,
):
    pass

ListProtectedResourcesByBackupVaultOutputTypeDef = TypedDict(
    "ListProtectedResourcesByBackupVaultOutputTypeDef",
    {
        "Results": List["ProtectedResourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProtectedResourcesInputRequestTypeDef = TypedDict(
    "ListProtectedResourcesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListProtectedResourcesOutputTypeDef = TypedDict(
    "ListProtectedResourcesOutputTypeDef",
    {
        "Results": List["ProtectedResourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRecoveryPointsByBackupVaultInputRequestTypeDef = TypedDict(
    "_RequiredListRecoveryPointsByBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)
_OptionalListRecoveryPointsByBackupVaultInputRequestTypeDef = TypedDict(
    "_OptionalListRecoveryPointsByBackupVaultInputRequestTypeDef",
    {
        "BackupVaultAccountId": str,
        "NextToken": str,
        "MaxResults": int,
        "ByResourceArn": str,
        "ByResourceType": str,
        "ByBackupPlanId": str,
        "ByCreatedBefore": Union[datetime, str],
        "ByCreatedAfter": Union[datetime, str],
        "ByParentRecoveryPointArn": str,
    },
    total=False,
)

class ListRecoveryPointsByBackupVaultInputRequestTypeDef(
    _RequiredListRecoveryPointsByBackupVaultInputRequestTypeDef,
    _OptionalListRecoveryPointsByBackupVaultInputRequestTypeDef,
):
    pass

ListRecoveryPointsByBackupVaultOutputTypeDef = TypedDict(
    "ListRecoveryPointsByBackupVaultOutputTypeDef",
    {
        "NextToken": str,
        "RecoveryPoints": List["RecoveryPointByBackupVaultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRecoveryPointsByLegalHoldInputRequestTypeDef = TypedDict(
    "_RequiredListRecoveryPointsByLegalHoldInputRequestTypeDef",
    {
        "LegalHoldId": str,
    },
)
_OptionalListRecoveryPointsByLegalHoldInputRequestTypeDef = TypedDict(
    "_OptionalListRecoveryPointsByLegalHoldInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListRecoveryPointsByLegalHoldInputRequestTypeDef(
    _RequiredListRecoveryPointsByLegalHoldInputRequestTypeDef,
    _OptionalListRecoveryPointsByLegalHoldInputRequestTypeDef,
):
    pass

ListRecoveryPointsByLegalHoldOutputTypeDef = TypedDict(
    "ListRecoveryPointsByLegalHoldOutputTypeDef",
    {
        "RecoveryPoints": List["RecoveryPointMemberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRecoveryPointsByResourceInputRequestTypeDef = TypedDict(
    "_RequiredListRecoveryPointsByResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListRecoveryPointsByResourceInputRequestTypeDef = TypedDict(
    "_OptionalListRecoveryPointsByResourceInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListRecoveryPointsByResourceInputRequestTypeDef(
    _RequiredListRecoveryPointsByResourceInputRequestTypeDef,
    _OptionalListRecoveryPointsByResourceInputRequestTypeDef,
):
    pass

ListRecoveryPointsByResourceOutputTypeDef = TypedDict(
    "ListRecoveryPointsByResourceOutputTypeDef",
    {
        "NextToken": str,
        "RecoveryPoints": List["RecoveryPointByResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReportJobsInputRequestTypeDef = TypedDict(
    "ListReportJobsInputRequestTypeDef",
    {
        "ByReportPlanName": str,
        "ByCreationBefore": Union[datetime, str],
        "ByCreationAfter": Union[datetime, str],
        "ByStatus": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListReportJobsOutputTypeDef = TypedDict(
    "ListReportJobsOutputTypeDef",
    {
        "ReportJobs": List["ReportJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReportPlansInputRequestTypeDef = TypedDict(
    "ListReportPlansInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListReportPlansOutputTypeDef = TypedDict(
    "ListReportPlansOutputTypeDef",
    {
        "ReportPlans": List["ReportPlanTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRestoreJobSummariesInputRequestTypeDef = TypedDict(
    "ListRestoreJobSummariesInputRequestTypeDef",
    {
        "AccountId": str,
        "State": RestoreJobStateType,
        "ResourceType": str,
        "AggregationPeriod": AggregationPeriodType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListRestoreJobSummariesOutputTypeDef = TypedDict(
    "ListRestoreJobSummariesOutputTypeDef",
    {
        "RestoreJobSummaries": List["RestoreJobSummaryTypeDef"],
        "AggregationPeriod": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRestoreJobsInputRequestTypeDef = TypedDict(
    "ListRestoreJobsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ByAccountId": str,
        "ByCreatedBefore": Union[datetime, str],
        "ByCreatedAfter": Union[datetime, str],
        "ByStatus": RestoreJobStatusType,
        "ByCompleteBefore": Union[datetime, str],
        "ByCompleteAfter": Union[datetime, str],
    },
    total=False,
)

ListRestoreJobsOutputTypeDef = TypedDict(
    "ListRestoreJobsOutputTypeDef",
    {
        "RestoreJobs": List["RestoreJobsListMemberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsInputRequestTypeDef = TypedDict(
    "_RequiredListTagsInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsInputRequestTypeDef = TypedDict(
    "_OptionalListTagsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListTagsInputRequestTypeDef(
    _RequiredListTagsInputRequestTypeDef, _OptionalListTagsInputRequestTypeDef
):
    pass

ListTagsOutputTypeDef = TypedDict(
    "ListTagsOutputTypeDef",
    {
        "NextToken": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ProtectedResourceTypeDef = TypedDict(
    "ProtectedResourceTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": str,
        "LastBackupTime": datetime,
        "ResourceName": str,
    },
    total=False,
)

_RequiredPutBackupVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "_RequiredPutBackupVaultAccessPolicyInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)
_OptionalPutBackupVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "_OptionalPutBackupVaultAccessPolicyInputRequestTypeDef",
    {
        "Policy": str,
    },
    total=False,
)

class PutBackupVaultAccessPolicyInputRequestTypeDef(
    _RequiredPutBackupVaultAccessPolicyInputRequestTypeDef,
    _OptionalPutBackupVaultAccessPolicyInputRequestTypeDef,
):
    pass

_RequiredPutBackupVaultLockConfigurationInputRequestTypeDef = TypedDict(
    "_RequiredPutBackupVaultLockConfigurationInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)
_OptionalPutBackupVaultLockConfigurationInputRequestTypeDef = TypedDict(
    "_OptionalPutBackupVaultLockConfigurationInputRequestTypeDef",
    {
        "MinRetentionDays": int,
        "MaxRetentionDays": int,
        "ChangeableForDays": int,
    },
    total=False,
)

class PutBackupVaultLockConfigurationInputRequestTypeDef(
    _RequiredPutBackupVaultLockConfigurationInputRequestTypeDef,
    _OptionalPutBackupVaultLockConfigurationInputRequestTypeDef,
):
    pass

PutBackupVaultNotificationsInputRequestTypeDef = TypedDict(
    "PutBackupVaultNotificationsInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "SNSTopicArn": str,
        "BackupVaultEvents": List[BackupVaultEventType],
    },
)

RecoveryPointByBackupVaultTypeDef = TypedDict(
    "RecoveryPointByBackupVaultTypeDef",
    {
        "RecoveryPointArn": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "SourceBackupVaultArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "CreatedBy": "RecoveryPointCreatorTypeDef",
        "IamRoleArn": str,
        "Status": RecoveryPointStatusType,
        "StatusMessage": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "BackupSizeInBytes": int,
        "CalculatedLifecycle": "CalculatedLifecycleTypeDef",
        "Lifecycle": "LifecycleTypeDef",
        "EncryptionKeyArn": str,
        "IsEncrypted": bool,
        "LastRestoreTime": datetime,
        "ParentRecoveryPointArn": str,
        "CompositeMemberIdentifier": str,
        "IsParent": bool,
        "ResourceName": str,
    },
    total=False,
)

RecoveryPointByResourceTypeDef = TypedDict(
    "RecoveryPointByResourceTypeDef",
    {
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "Status": RecoveryPointStatusType,
        "StatusMessage": str,
        "EncryptionKeyArn": str,
        "BackupSizeBytes": int,
        "BackupVaultName": str,
        "IsParent": bool,
        "ParentRecoveryPointArn": str,
        "ResourceName": str,
    },
    total=False,
)

RecoveryPointCreatorTypeDef = TypedDict(
    "RecoveryPointCreatorTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "BackupPlanVersion": str,
        "BackupRuleId": str,
    },
    total=False,
)

RecoveryPointMemberTypeDef = TypedDict(
    "RecoveryPointMemberTypeDef",
    {
        "RecoveryPointArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "BackupVaultName": str,
    },
    total=False,
)

RecoveryPointSelectionTypeDef = TypedDict(
    "RecoveryPointSelectionTypeDef",
    {
        "VaultNames": List[str],
        "ResourceIdentifiers": List[str],
        "DateRange": "DateRangeTypeDef",
    },
    total=False,
)

_RequiredReportDeliveryChannelTypeDef = TypedDict(
    "_RequiredReportDeliveryChannelTypeDef",
    {
        "S3BucketName": str,
    },
)
_OptionalReportDeliveryChannelTypeDef = TypedDict(
    "_OptionalReportDeliveryChannelTypeDef",
    {
        "S3KeyPrefix": str,
        "Formats": List[str],
    },
    total=False,
)

class ReportDeliveryChannelTypeDef(
    _RequiredReportDeliveryChannelTypeDef, _OptionalReportDeliveryChannelTypeDef
):
    pass

ReportDestinationTypeDef = TypedDict(
    "ReportDestinationTypeDef",
    {
        "S3BucketName": str,
        "S3Keys": List[str],
    },
    total=False,
)

ReportJobTypeDef = TypedDict(
    "ReportJobTypeDef",
    {
        "ReportJobId": str,
        "ReportPlanArn": str,
        "ReportTemplate": str,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "Status": str,
        "StatusMessage": str,
        "ReportDestination": "ReportDestinationTypeDef",
    },
    total=False,
)

ReportPlanTypeDef = TypedDict(
    "ReportPlanTypeDef",
    {
        "ReportPlanArn": str,
        "ReportPlanName": str,
        "ReportPlanDescription": str,
        "ReportSetting": "ReportSettingTypeDef",
        "ReportDeliveryChannel": "ReportDeliveryChannelTypeDef",
        "DeploymentStatus": str,
        "CreationTime": datetime,
        "LastAttemptedExecutionTime": datetime,
        "LastSuccessfulExecutionTime": datetime,
    },
    total=False,
)

_RequiredReportSettingTypeDef = TypedDict(
    "_RequiredReportSettingTypeDef",
    {
        "ReportTemplate": str,
    },
)
_OptionalReportSettingTypeDef = TypedDict(
    "_OptionalReportSettingTypeDef",
    {
        "FrameworkArns": List[str],
        "NumberOfFrameworks": int,
        "Accounts": List[str],
        "OrganizationUnits": List[str],
        "Regions": List[str],
    },
    total=False,
)

class ReportSettingTypeDef(_RequiredReportSettingTypeDef, _OptionalReportSettingTypeDef):
    pass

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RestoreJobSummaryTypeDef = TypedDict(
    "RestoreJobSummaryTypeDef",
    {
        "Region": str,
        "AccountId": str,
        "State": RestoreJobStateType,
        "ResourceType": str,
        "Count": int,
        "StartTime": datetime,
        "EndTime": datetime,
    },
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
        "Status": RestoreJobStatusType,
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

_RequiredStartBackupJobInputRequestTypeDef = TypedDict(
    "_RequiredStartBackupJobInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "ResourceArn": str,
        "IamRoleArn": str,
    },
)
_OptionalStartBackupJobInputRequestTypeDef = TypedDict(
    "_OptionalStartBackupJobInputRequestTypeDef",
    {
        "IdempotencyToken": str,
        "StartWindowMinutes": int,
        "CompleteWindowMinutes": int,
        "Lifecycle": "LifecycleTypeDef",
        "RecoveryPointTags": Dict[str, str],
        "BackupOptions": Dict[str, str],
    },
    total=False,
)

class StartBackupJobInputRequestTypeDef(
    _RequiredStartBackupJobInputRequestTypeDef, _OptionalStartBackupJobInputRequestTypeDef
):
    pass

StartBackupJobOutputTypeDef = TypedDict(
    "StartBackupJobOutputTypeDef",
    {
        "BackupJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "IsParent": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartCopyJobInputRequestTypeDef = TypedDict(
    "_RequiredStartCopyJobInputRequestTypeDef",
    {
        "RecoveryPointArn": str,
        "SourceBackupVaultName": str,
        "DestinationBackupVaultArn": str,
        "IamRoleArn": str,
    },
)
_OptionalStartCopyJobInputRequestTypeDef = TypedDict(
    "_OptionalStartCopyJobInputRequestTypeDef",
    {
        "IdempotencyToken": str,
        "Lifecycle": "LifecycleTypeDef",
    },
    total=False,
)

class StartCopyJobInputRequestTypeDef(
    _RequiredStartCopyJobInputRequestTypeDef, _OptionalStartCopyJobInputRequestTypeDef
):
    pass

StartCopyJobOutputTypeDef = TypedDict(
    "StartCopyJobOutputTypeDef",
    {
        "CopyJobId": str,
        "CreationDate": datetime,
        "IsParent": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartReportJobInputRequestTypeDef = TypedDict(
    "_RequiredStartReportJobInputRequestTypeDef",
    {
        "ReportPlanName": str,
    },
)
_OptionalStartReportJobInputRequestTypeDef = TypedDict(
    "_OptionalStartReportJobInputRequestTypeDef",
    {
        "IdempotencyToken": str,
    },
    total=False,
)

class StartReportJobInputRequestTypeDef(
    _RequiredStartReportJobInputRequestTypeDef, _OptionalStartReportJobInputRequestTypeDef
):
    pass

StartReportJobOutputTypeDef = TypedDict(
    "StartReportJobOutputTypeDef",
    {
        "ReportJobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartRestoreJobInputRequestTypeDef = TypedDict(
    "_RequiredStartRestoreJobInputRequestTypeDef",
    {
        "RecoveryPointArn": str,
        "Metadata": Dict[str, str],
    },
)
_OptionalStartRestoreJobInputRequestTypeDef = TypedDict(
    "_OptionalStartRestoreJobInputRequestTypeDef",
    {
        "IamRoleArn": str,
        "IdempotencyToken": str,
        "ResourceType": str,
        "CopySourceTagsToRestoredResource": bool,
    },
    total=False,
)

class StartRestoreJobInputRequestTypeDef(
    _RequiredStartRestoreJobInputRequestTypeDef, _OptionalStartRestoreJobInputRequestTypeDef
):
    pass

StartRestoreJobOutputTypeDef = TypedDict(
    "StartRestoreJobOutputTypeDef",
    {
        "RestoreJobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopBackupJobInputRequestTypeDef = TypedDict(
    "StopBackupJobInputRequestTypeDef",
    {
        "BackupJobId": str,
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeyList": List[str],
    },
)

UpdateBackupPlanInputRequestTypeDef = TypedDict(
    "UpdateBackupPlanInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlan": "BackupPlanInputTypeDef",
    },
)

UpdateBackupPlanOutputTypeDef = TypedDict(
    "UpdateBackupPlanOutputTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "CreationDate": datetime,
        "VersionId": str,
        "AdvancedBackupSettings": List["AdvancedBackupSettingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFrameworkInputRequestTypeDef = TypedDict(
    "_RequiredUpdateFrameworkInputRequestTypeDef",
    {
        "FrameworkName": str,
    },
)
_OptionalUpdateFrameworkInputRequestTypeDef = TypedDict(
    "_OptionalUpdateFrameworkInputRequestTypeDef",
    {
        "FrameworkDescription": str,
        "FrameworkControls": List["FrameworkControlTypeDef"],
        "IdempotencyToken": str,
    },
    total=False,
)

class UpdateFrameworkInputRequestTypeDef(
    _RequiredUpdateFrameworkInputRequestTypeDef, _OptionalUpdateFrameworkInputRequestTypeDef
):
    pass

UpdateFrameworkOutputTypeDef = TypedDict(
    "UpdateFrameworkOutputTypeDef",
    {
        "FrameworkName": str,
        "FrameworkArn": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGlobalSettingsInputRequestTypeDef = TypedDict(
    "UpdateGlobalSettingsInputRequestTypeDef",
    {
        "GlobalSettings": Dict[str, str],
    },
    total=False,
)

_RequiredUpdateRecoveryPointLifecycleInputRequestTypeDef = TypedDict(
    "_RequiredUpdateRecoveryPointLifecycleInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)
_OptionalUpdateRecoveryPointLifecycleInputRequestTypeDef = TypedDict(
    "_OptionalUpdateRecoveryPointLifecycleInputRequestTypeDef",
    {
        "Lifecycle": "LifecycleTypeDef",
    },
    total=False,
)

class UpdateRecoveryPointLifecycleInputRequestTypeDef(
    _RequiredUpdateRecoveryPointLifecycleInputRequestTypeDef,
    _OptionalUpdateRecoveryPointLifecycleInputRequestTypeDef,
):
    pass

UpdateRecoveryPointLifecycleOutputTypeDef = TypedDict(
    "UpdateRecoveryPointLifecycleOutputTypeDef",
    {
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "Lifecycle": "LifecycleTypeDef",
        "CalculatedLifecycle": "CalculatedLifecycleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRegionSettingsInputRequestTypeDef = TypedDict(
    "UpdateRegionSettingsInputRequestTypeDef",
    {
        "ResourceTypeOptInPreference": Dict[str, bool],
        "ResourceTypeManagementPreference": Dict[str, bool],
    },
    total=False,
)

_RequiredUpdateReportPlanInputRequestTypeDef = TypedDict(
    "_RequiredUpdateReportPlanInputRequestTypeDef",
    {
        "ReportPlanName": str,
    },
)
_OptionalUpdateReportPlanInputRequestTypeDef = TypedDict(
    "_OptionalUpdateReportPlanInputRequestTypeDef",
    {
        "ReportPlanDescription": str,
        "ReportDeliveryChannel": "ReportDeliveryChannelTypeDef",
        "ReportSetting": "ReportSettingTypeDef",
        "IdempotencyToken": str,
    },
    total=False,
)

class UpdateReportPlanInputRequestTypeDef(
    _RequiredUpdateReportPlanInputRequestTypeDef, _OptionalUpdateReportPlanInputRequestTypeDef
):
    pass

UpdateReportPlanOutputTypeDef = TypedDict(
    "UpdateReportPlanOutputTypeDef",
    {
        "ReportPlanName": str,
        "ReportPlanArn": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
