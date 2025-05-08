"""
Type annotations for backup service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_backup.type_defs import AdvancedBackupSettingOutputTypeDef

    data: AdvancedBackupSettingOutputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AggregationPeriodType,
    BackupJobStateType,
    BackupJobStatusType,
    BackupVaultEventType,
    CopyJobStateType,
    CopyJobStatusType,
    IndexStatusType,
    IndexType,
    LegalHoldStatusType,
    RecoveryPointStatusType,
    RestoreDeletionStatusType,
    RestoreJobStateType,
    RestoreJobStatusType,
    RestoreTestingRecoveryPointSelectionAlgorithmType,
    RestoreTestingRecoveryPointTypeType,
    RestoreValidationStatusType,
    StorageClassType,
    VaultStateType,
    VaultTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AdvancedBackupSettingOutputTypeDef",
    "AdvancedBackupSettingTypeDef",
    "AdvancedBackupSettingUnionTypeDef",
    "BackupJobSummaryTypeDef",
    "BackupJobTypeDef",
    "BackupPlanInputTypeDef",
    "BackupPlanTemplatesListMemberTypeDef",
    "BackupPlanTypeDef",
    "BackupPlansListMemberTypeDef",
    "BackupRuleInputTypeDef",
    "BackupRuleTypeDef",
    "BackupSelectionOutputTypeDef",
    "BackupSelectionTypeDef",
    "BackupSelectionUnionTypeDef",
    "BackupSelectionsListMemberTypeDef",
    "BackupVaultListMemberTypeDef",
    "CalculatedLifecycleTypeDef",
    "CancelLegalHoldInputTypeDef",
    "ConditionParameterTypeDef",
    "ConditionTypeDef",
    "ConditionsOutputTypeDef",
    "ConditionsTypeDef",
    "ControlInputParameterTypeDef",
    "ControlScopeOutputTypeDef",
    "ControlScopeTypeDef",
    "ControlScopeUnionTypeDef",
    "CopyActionTypeDef",
    "CopyJobSummaryTypeDef",
    "CopyJobTypeDef",
    "CreateBackupPlanInputTypeDef",
    "CreateBackupPlanOutputTypeDef",
    "CreateBackupSelectionInputTypeDef",
    "CreateBackupSelectionOutputTypeDef",
    "CreateBackupVaultInputTypeDef",
    "CreateBackupVaultOutputTypeDef",
    "CreateFrameworkInputTypeDef",
    "CreateFrameworkOutputTypeDef",
    "CreateLegalHoldInputTypeDef",
    "CreateLegalHoldOutputTypeDef",
    "CreateLogicallyAirGappedBackupVaultInputTypeDef",
    "CreateLogicallyAirGappedBackupVaultOutputTypeDef",
    "CreateReportPlanInputTypeDef",
    "CreateReportPlanOutputTypeDef",
    "CreateRestoreTestingPlanInputTypeDef",
    "CreateRestoreTestingPlanOutputTypeDef",
    "CreateRestoreTestingSelectionInputTypeDef",
    "CreateRestoreTestingSelectionOutputTypeDef",
    "DateRangeOutputTypeDef",
    "DateRangeTypeDef",
    "DeleteBackupPlanInputTypeDef",
    "DeleteBackupPlanOutputTypeDef",
    "DeleteBackupSelectionInputTypeDef",
    "DeleteBackupVaultAccessPolicyInputTypeDef",
    "DeleteBackupVaultInputTypeDef",
    "DeleteBackupVaultLockConfigurationInputTypeDef",
    "DeleteBackupVaultNotificationsInputTypeDef",
    "DeleteFrameworkInputTypeDef",
    "DeleteRecoveryPointInputTypeDef",
    "DeleteReportPlanInputTypeDef",
    "DeleteRestoreTestingPlanInputTypeDef",
    "DeleteRestoreTestingSelectionInputTypeDef",
    "DescribeBackupJobInputTypeDef",
    "DescribeBackupJobOutputTypeDef",
    "DescribeBackupVaultInputTypeDef",
    "DescribeBackupVaultOutputTypeDef",
    "DescribeCopyJobInputTypeDef",
    "DescribeCopyJobOutputTypeDef",
    "DescribeFrameworkInputTypeDef",
    "DescribeFrameworkOutputTypeDef",
    "DescribeGlobalSettingsOutputTypeDef",
    "DescribeProtectedResourceInputTypeDef",
    "DescribeProtectedResourceOutputTypeDef",
    "DescribeRecoveryPointInputTypeDef",
    "DescribeRecoveryPointOutputTypeDef",
    "DescribeRegionSettingsOutputTypeDef",
    "DescribeReportJobInputTypeDef",
    "DescribeReportJobOutputTypeDef",
    "DescribeReportPlanInputTypeDef",
    "DescribeReportPlanOutputTypeDef",
    "DescribeRestoreJobInputTypeDef",
    "DescribeRestoreJobOutputTypeDef",
    "DisassociateRecoveryPointFromParentInputTypeDef",
    "DisassociateRecoveryPointInputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExportBackupPlanTemplateInputTypeDef",
    "ExportBackupPlanTemplateOutputTypeDef",
    "FrameworkControlOutputTypeDef",
    "FrameworkControlTypeDef",
    "FrameworkControlUnionTypeDef",
    "FrameworkTypeDef",
    "GetBackupPlanFromJSONInputTypeDef",
    "GetBackupPlanFromJSONOutputTypeDef",
    "GetBackupPlanFromTemplateInputTypeDef",
    "GetBackupPlanFromTemplateOutputTypeDef",
    "GetBackupPlanInputTypeDef",
    "GetBackupPlanOutputTypeDef",
    "GetBackupSelectionInputTypeDef",
    "GetBackupSelectionOutputTypeDef",
    "GetBackupVaultAccessPolicyInputTypeDef",
    "GetBackupVaultAccessPolicyOutputTypeDef",
    "GetBackupVaultNotificationsInputTypeDef",
    "GetBackupVaultNotificationsOutputTypeDef",
    "GetLegalHoldInputTypeDef",
    "GetLegalHoldOutputTypeDef",
    "GetRecoveryPointIndexDetailsInputTypeDef",
    "GetRecoveryPointIndexDetailsOutputTypeDef",
    "GetRecoveryPointRestoreMetadataInputTypeDef",
    "GetRecoveryPointRestoreMetadataOutputTypeDef",
    "GetRestoreJobMetadataInputTypeDef",
    "GetRestoreJobMetadataOutputTypeDef",
    "GetRestoreTestingInferredMetadataInputTypeDef",
    "GetRestoreTestingInferredMetadataOutputTypeDef",
    "GetRestoreTestingPlanInputTypeDef",
    "GetRestoreTestingPlanOutputTypeDef",
    "GetRestoreTestingSelectionInputTypeDef",
    "GetRestoreTestingSelectionOutputTypeDef",
    "GetSupportedResourceTypesOutputTypeDef",
    "IndexActionOutputTypeDef",
    "IndexActionTypeDef",
    "IndexActionUnionTypeDef",
    "IndexedRecoveryPointTypeDef",
    "KeyValueTypeDef",
    "LegalHoldTypeDef",
    "LifecycleTypeDef",
    "ListBackupJobSummariesInputTypeDef",
    "ListBackupJobSummariesOutputTypeDef",
    "ListBackupJobsInputPaginateTypeDef",
    "ListBackupJobsInputTypeDef",
    "ListBackupJobsOutputTypeDef",
    "ListBackupPlanTemplatesInputPaginateTypeDef",
    "ListBackupPlanTemplatesInputTypeDef",
    "ListBackupPlanTemplatesOutputTypeDef",
    "ListBackupPlanVersionsInputPaginateTypeDef",
    "ListBackupPlanVersionsInputTypeDef",
    "ListBackupPlanVersionsOutputTypeDef",
    "ListBackupPlansInputPaginateTypeDef",
    "ListBackupPlansInputTypeDef",
    "ListBackupPlansOutputTypeDef",
    "ListBackupSelectionsInputPaginateTypeDef",
    "ListBackupSelectionsInputTypeDef",
    "ListBackupSelectionsOutputTypeDef",
    "ListBackupVaultsInputPaginateTypeDef",
    "ListBackupVaultsInputTypeDef",
    "ListBackupVaultsOutputTypeDef",
    "ListCopyJobSummariesInputTypeDef",
    "ListCopyJobSummariesOutputTypeDef",
    "ListCopyJobsInputPaginateTypeDef",
    "ListCopyJobsInputTypeDef",
    "ListCopyJobsOutputTypeDef",
    "ListFrameworksInputTypeDef",
    "ListFrameworksOutputTypeDef",
    "ListIndexedRecoveryPointsInputPaginateTypeDef",
    "ListIndexedRecoveryPointsInputTypeDef",
    "ListIndexedRecoveryPointsOutputTypeDef",
    "ListLegalHoldsInputPaginateTypeDef",
    "ListLegalHoldsInputTypeDef",
    "ListLegalHoldsOutputTypeDef",
    "ListProtectedResourcesByBackupVaultInputPaginateTypeDef",
    "ListProtectedResourcesByBackupVaultInputTypeDef",
    "ListProtectedResourcesByBackupVaultOutputTypeDef",
    "ListProtectedResourcesInputPaginateTypeDef",
    "ListProtectedResourcesInputTypeDef",
    "ListProtectedResourcesOutputTypeDef",
    "ListRecoveryPointsByBackupVaultInputPaginateTypeDef",
    "ListRecoveryPointsByBackupVaultInputTypeDef",
    "ListRecoveryPointsByBackupVaultOutputTypeDef",
    "ListRecoveryPointsByLegalHoldInputPaginateTypeDef",
    "ListRecoveryPointsByLegalHoldInputTypeDef",
    "ListRecoveryPointsByLegalHoldOutputTypeDef",
    "ListRecoveryPointsByResourceInputPaginateTypeDef",
    "ListRecoveryPointsByResourceInputTypeDef",
    "ListRecoveryPointsByResourceOutputTypeDef",
    "ListReportJobsInputTypeDef",
    "ListReportJobsOutputTypeDef",
    "ListReportPlansInputTypeDef",
    "ListReportPlansOutputTypeDef",
    "ListRestoreJobSummariesInputTypeDef",
    "ListRestoreJobSummariesOutputTypeDef",
    "ListRestoreJobsByProtectedResourceInputPaginateTypeDef",
    "ListRestoreJobsByProtectedResourceInputTypeDef",
    "ListRestoreJobsByProtectedResourceOutputTypeDef",
    "ListRestoreJobsInputPaginateTypeDef",
    "ListRestoreJobsInputTypeDef",
    "ListRestoreJobsOutputTypeDef",
    "ListRestoreTestingPlansInputPaginateTypeDef",
    "ListRestoreTestingPlansInputTypeDef",
    "ListRestoreTestingPlansOutputTypeDef",
    "ListRestoreTestingSelectionsInputPaginateTypeDef",
    "ListRestoreTestingSelectionsInputTypeDef",
    "ListRestoreTestingSelectionsOutputTypeDef",
    "ListTagsInputTypeDef",
    "ListTagsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ProtectedResourceConditionsOutputTypeDef",
    "ProtectedResourceConditionsTypeDef",
    "ProtectedResourceConditionsUnionTypeDef",
    "ProtectedResourceTypeDef",
    "PutBackupVaultAccessPolicyInputTypeDef",
    "PutBackupVaultLockConfigurationInputTypeDef",
    "PutBackupVaultNotificationsInputTypeDef",
    "PutRestoreValidationResultInputTypeDef",
    "RecoveryPointByBackupVaultTypeDef",
    "RecoveryPointByResourceTypeDef",
    "RecoveryPointCreatorTypeDef",
    "RecoveryPointMemberTypeDef",
    "RecoveryPointSelectionOutputTypeDef",
    "RecoveryPointSelectionTypeDef",
    "RecoveryPointSelectionUnionTypeDef",
    "ReportDeliveryChannelOutputTypeDef",
    "ReportDeliveryChannelTypeDef",
    "ReportDeliveryChannelUnionTypeDef",
    "ReportDestinationTypeDef",
    "ReportJobTypeDef",
    "ReportPlanTypeDef",
    "ReportSettingOutputTypeDef",
    "ReportSettingTypeDef",
    "ReportSettingUnionTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreJobCreatorTypeDef",
    "RestoreJobSummaryTypeDef",
    "RestoreJobsListMemberTypeDef",
    "RestoreTestingPlanForCreateTypeDef",
    "RestoreTestingPlanForGetTypeDef",
    "RestoreTestingPlanForListTypeDef",
    "RestoreTestingPlanForUpdateTypeDef",
    "RestoreTestingRecoveryPointSelectionOutputTypeDef",
    "RestoreTestingRecoveryPointSelectionTypeDef",
    "RestoreTestingRecoveryPointSelectionUnionTypeDef",
    "RestoreTestingSelectionForCreateTypeDef",
    "RestoreTestingSelectionForGetTypeDef",
    "RestoreTestingSelectionForListTypeDef",
    "RestoreTestingSelectionForUpdateTypeDef",
    "StartBackupJobInputTypeDef",
    "StartBackupJobOutputTypeDef",
    "StartCopyJobInputTypeDef",
    "StartCopyJobOutputTypeDef",
    "StartReportJobInputTypeDef",
    "StartReportJobOutputTypeDef",
    "StartRestoreJobInputTypeDef",
    "StartRestoreJobOutputTypeDef",
    "StopBackupJobInputTypeDef",
    "TagResourceInputTypeDef",
    "TimestampTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateBackupPlanInputTypeDef",
    "UpdateBackupPlanOutputTypeDef",
    "UpdateFrameworkInputTypeDef",
    "UpdateFrameworkOutputTypeDef",
    "UpdateGlobalSettingsInputTypeDef",
    "UpdateRecoveryPointIndexSettingsInputTypeDef",
    "UpdateRecoveryPointIndexSettingsOutputTypeDef",
    "UpdateRecoveryPointLifecycleInputTypeDef",
    "UpdateRecoveryPointLifecycleOutputTypeDef",
    "UpdateRegionSettingsInputTypeDef",
    "UpdateReportPlanInputTypeDef",
    "UpdateReportPlanOutputTypeDef",
    "UpdateRestoreTestingPlanInputTypeDef",
    "UpdateRestoreTestingPlanOutputTypeDef",
    "UpdateRestoreTestingSelectionInputTypeDef",
    "UpdateRestoreTestingSelectionOutputTypeDef",
)

class AdvancedBackupSettingOutputTypeDef(TypedDict):
    ResourceType: NotRequired[str]
    BackupOptions: NotRequired[Dict[str, str]]

class AdvancedBackupSettingTypeDef(TypedDict):
    ResourceType: NotRequired[str]
    BackupOptions: NotRequired[Mapping[str, str]]

class BackupJobSummaryTypeDef(TypedDict):
    Region: NotRequired[str]
    AccountId: NotRequired[str]
    State: NotRequired[BackupJobStatusType]
    ResourceType: NotRequired[str]
    MessageCategory: NotRequired[str]
    Count: NotRequired[int]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]

class RecoveryPointCreatorTypeDef(TypedDict):
    BackupPlanId: NotRequired[str]
    BackupPlanArn: NotRequired[str]
    BackupPlanVersion: NotRequired[str]
    BackupRuleId: NotRequired[str]

class BackupPlanTemplatesListMemberTypeDef(TypedDict):
    BackupPlanTemplateId: NotRequired[str]
    BackupPlanTemplateName: NotRequired[str]

class LifecycleTypeDef(TypedDict):
    MoveToColdStorageAfterDays: NotRequired[int]
    DeleteAfterDays: NotRequired[int]
    OptInToArchiveForSupportedResources: NotRequired[bool]

class IndexActionOutputTypeDef(TypedDict):
    ResourceTypes: NotRequired[List[str]]

class ConditionTypeDef(TypedDict):
    ConditionType: Literal["STRINGEQUALS"]
    ConditionKey: str
    ConditionValue: str

class BackupSelectionsListMemberTypeDef(TypedDict):
    SelectionId: NotRequired[str]
    SelectionName: NotRequired[str]
    BackupPlanId: NotRequired[str]
    CreationDate: NotRequired[datetime]
    CreatorRequestId: NotRequired[str]
    IamRoleArn: NotRequired[str]

class BackupVaultListMemberTypeDef(TypedDict):
    BackupVaultName: NotRequired[str]
    BackupVaultArn: NotRequired[str]
    VaultType: NotRequired[VaultTypeType]
    VaultState: NotRequired[VaultStateType]
    CreationDate: NotRequired[datetime]
    EncryptionKeyArn: NotRequired[str]
    CreatorRequestId: NotRequired[str]
    NumberOfRecoveryPoints: NotRequired[int]
    Locked: NotRequired[bool]
    MinRetentionDays: NotRequired[int]
    MaxRetentionDays: NotRequired[int]
    LockDate: NotRequired[datetime]

class CalculatedLifecycleTypeDef(TypedDict):
    MoveToColdStorageAt: NotRequired[datetime]
    DeleteAt: NotRequired[datetime]

class CancelLegalHoldInputTypeDef(TypedDict):
    LegalHoldId: str
    CancelDescription: str
    RetainRecordInDays: NotRequired[int]

class ConditionParameterTypeDef(TypedDict):
    ConditionKey: NotRequired[str]
    ConditionValue: NotRequired[str]

class ControlInputParameterTypeDef(TypedDict):
    ParameterName: NotRequired[str]
    ParameterValue: NotRequired[str]

class ControlScopeOutputTypeDef(TypedDict):
    ComplianceResourceIds: NotRequired[List[str]]
    ComplianceResourceTypes: NotRequired[List[str]]
    Tags: NotRequired[Dict[str, str]]

class ControlScopeTypeDef(TypedDict):
    ComplianceResourceIds: NotRequired[Sequence[str]]
    ComplianceResourceTypes: NotRequired[Sequence[str]]
    Tags: NotRequired[Mapping[str, str]]

class CopyJobSummaryTypeDef(TypedDict):
    Region: NotRequired[str]
    AccountId: NotRequired[str]
    State: NotRequired[CopyJobStatusType]
    ResourceType: NotRequired[str]
    MessageCategory: NotRequired[str]
    Count: NotRequired[int]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateBackupVaultInputTypeDef(TypedDict):
    BackupVaultName: str
    BackupVaultTags: NotRequired[Mapping[str, str]]
    EncryptionKeyArn: NotRequired[str]
    CreatorRequestId: NotRequired[str]

class CreateLogicallyAirGappedBackupVaultInputTypeDef(TypedDict):
    BackupVaultName: str
    MinRetentionDays: int
    MaxRetentionDays: int
    BackupVaultTags: NotRequired[Mapping[str, str]]
    CreatorRequestId: NotRequired[str]

class DateRangeOutputTypeDef(TypedDict):
    FromDate: datetime
    ToDate: datetime

TimestampTypeDef = Union[datetime, str]

class DeleteBackupPlanInputTypeDef(TypedDict):
    BackupPlanId: str

class DeleteBackupSelectionInputTypeDef(TypedDict):
    BackupPlanId: str
    SelectionId: str

class DeleteBackupVaultAccessPolicyInputTypeDef(TypedDict):
    BackupVaultName: str

class DeleteBackupVaultInputTypeDef(TypedDict):
    BackupVaultName: str

class DeleteBackupVaultLockConfigurationInputTypeDef(TypedDict):
    BackupVaultName: str

class DeleteBackupVaultNotificationsInputTypeDef(TypedDict):
    BackupVaultName: str

class DeleteFrameworkInputTypeDef(TypedDict):
    FrameworkName: str

class DeleteRecoveryPointInputTypeDef(TypedDict):
    BackupVaultName: str
    RecoveryPointArn: str

class DeleteReportPlanInputTypeDef(TypedDict):
    ReportPlanName: str

class DeleteRestoreTestingPlanInputTypeDef(TypedDict):
    RestoreTestingPlanName: str

class DeleteRestoreTestingSelectionInputTypeDef(TypedDict):
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str

class DescribeBackupJobInputTypeDef(TypedDict):
    BackupJobId: str

class DescribeBackupVaultInputTypeDef(TypedDict):
    BackupVaultName: str
    BackupVaultAccountId: NotRequired[str]

class DescribeCopyJobInputTypeDef(TypedDict):
    CopyJobId: str

class DescribeFrameworkInputTypeDef(TypedDict):
    FrameworkName: str

class DescribeProtectedResourceInputTypeDef(TypedDict):
    ResourceArn: str

class DescribeRecoveryPointInputTypeDef(TypedDict):
    BackupVaultName: str
    RecoveryPointArn: str
    BackupVaultAccountId: NotRequired[str]

class DescribeReportJobInputTypeDef(TypedDict):
    ReportJobId: str

class DescribeReportPlanInputTypeDef(TypedDict):
    ReportPlanName: str

class DescribeRestoreJobInputTypeDef(TypedDict):
    RestoreJobId: str

class RestoreJobCreatorTypeDef(TypedDict):
    RestoreTestingPlanArn: NotRequired[str]

class DisassociateRecoveryPointFromParentInputTypeDef(TypedDict):
    BackupVaultName: str
    RecoveryPointArn: str

class DisassociateRecoveryPointInputTypeDef(TypedDict):
    BackupVaultName: str
    RecoveryPointArn: str

class ExportBackupPlanTemplateInputTypeDef(TypedDict):
    BackupPlanId: str

class FrameworkTypeDef(TypedDict):
    FrameworkName: NotRequired[str]
    FrameworkArn: NotRequired[str]
    FrameworkDescription: NotRequired[str]
    NumberOfControls: NotRequired[int]
    CreationTime: NotRequired[datetime]
    DeploymentStatus: NotRequired[str]

class GetBackupPlanFromJSONInputTypeDef(TypedDict):
    BackupPlanTemplateJson: str

class GetBackupPlanFromTemplateInputTypeDef(TypedDict):
    BackupPlanTemplateId: str

class GetBackupPlanInputTypeDef(TypedDict):
    BackupPlanId: str
    VersionId: NotRequired[str]

class GetBackupSelectionInputTypeDef(TypedDict):
    BackupPlanId: str
    SelectionId: str

class GetBackupVaultAccessPolicyInputTypeDef(TypedDict):
    BackupVaultName: str

class GetBackupVaultNotificationsInputTypeDef(TypedDict):
    BackupVaultName: str

class GetLegalHoldInputTypeDef(TypedDict):
    LegalHoldId: str

class GetRecoveryPointIndexDetailsInputTypeDef(TypedDict):
    BackupVaultName: str
    RecoveryPointArn: str

class GetRecoveryPointRestoreMetadataInputTypeDef(TypedDict):
    BackupVaultName: str
    RecoveryPointArn: str
    BackupVaultAccountId: NotRequired[str]

class GetRestoreJobMetadataInputTypeDef(TypedDict):
    RestoreJobId: str

class GetRestoreTestingInferredMetadataInputTypeDef(TypedDict):
    BackupVaultName: str
    RecoveryPointArn: str
    BackupVaultAccountId: NotRequired[str]

class GetRestoreTestingPlanInputTypeDef(TypedDict):
    RestoreTestingPlanName: str

class GetRestoreTestingSelectionInputTypeDef(TypedDict):
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str

class IndexActionTypeDef(TypedDict):
    ResourceTypes: NotRequired[Sequence[str]]

class IndexedRecoveryPointTypeDef(TypedDict):
    RecoveryPointArn: NotRequired[str]
    SourceResourceArn: NotRequired[str]
    IamRoleArn: NotRequired[str]
    BackupCreationDate: NotRequired[datetime]
    ResourceType: NotRequired[str]
    IndexCreationDate: NotRequired[datetime]
    IndexStatus: NotRequired[IndexStatusType]
    IndexStatusMessage: NotRequired[str]
    BackupVaultArn: NotRequired[str]

class KeyValueTypeDef(TypedDict):
    Key: str
    Value: str

class LegalHoldTypeDef(TypedDict):
    Title: NotRequired[str]
    Status: NotRequired[LegalHoldStatusType]
    Description: NotRequired[str]
    LegalHoldId: NotRequired[str]
    LegalHoldArn: NotRequired[str]
    CreationDate: NotRequired[datetime]
    CancellationDate: NotRequired[datetime]

class ListBackupJobSummariesInputTypeDef(TypedDict):
    AccountId: NotRequired[str]
    State: NotRequired[BackupJobStatusType]
    ResourceType: NotRequired[str]
    MessageCategory: NotRequired[str]
    AggregationPeriod: NotRequired[AggregationPeriodType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListBackupPlanTemplatesInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListBackupPlanVersionsInputTypeDef(TypedDict):
    BackupPlanId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListBackupPlansInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    IncludeDeleted: NotRequired[bool]

class ListBackupSelectionsInputTypeDef(TypedDict):
    BackupPlanId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListBackupVaultsInputTypeDef(TypedDict):
    ByVaultType: NotRequired[VaultTypeType]
    ByShared: NotRequired[bool]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListCopyJobSummariesInputTypeDef(TypedDict):
    AccountId: NotRequired[str]
    State: NotRequired[CopyJobStatusType]
    ResourceType: NotRequired[str]
    MessageCategory: NotRequired[str]
    AggregationPeriod: NotRequired[AggregationPeriodType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListFrameworksInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListLegalHoldsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListProtectedResourcesByBackupVaultInputTypeDef(TypedDict):
    BackupVaultName: str
    BackupVaultAccountId: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ProtectedResourceTypeDef(TypedDict):
    ResourceArn: NotRequired[str]
    ResourceType: NotRequired[str]
    LastBackupTime: NotRequired[datetime]
    ResourceName: NotRequired[str]
    LastBackupVaultArn: NotRequired[str]
    LastRecoveryPointArn: NotRequired[str]

class ListProtectedResourcesInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListRecoveryPointsByLegalHoldInputTypeDef(TypedDict):
    LegalHoldId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class RecoveryPointMemberTypeDef(TypedDict):
    RecoveryPointArn: NotRequired[str]
    ResourceArn: NotRequired[str]
    ResourceType: NotRequired[str]
    BackupVaultName: NotRequired[str]

class ListRecoveryPointsByResourceInputTypeDef(TypedDict):
    ResourceArn: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ManagedByAWSBackupOnly: NotRequired[bool]

class RecoveryPointByResourceTypeDef(TypedDict):
    RecoveryPointArn: NotRequired[str]
    CreationDate: NotRequired[datetime]
    Status: NotRequired[RecoveryPointStatusType]
    StatusMessage: NotRequired[str]
    EncryptionKeyArn: NotRequired[str]
    BackupSizeBytes: NotRequired[int]
    BackupVaultName: NotRequired[str]
    IsParent: NotRequired[bool]
    ParentRecoveryPointArn: NotRequired[str]
    ResourceName: NotRequired[str]
    VaultType: NotRequired[VaultTypeType]
    IndexStatus: NotRequired[IndexStatusType]
    IndexStatusMessage: NotRequired[str]

class ListReportPlansInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListRestoreJobSummariesInputTypeDef(TypedDict):
    AccountId: NotRequired[str]
    State: NotRequired[RestoreJobStateType]
    ResourceType: NotRequired[str]
    AggregationPeriod: NotRequired[AggregationPeriodType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class RestoreJobSummaryTypeDef(TypedDict):
    Region: NotRequired[str]
    AccountId: NotRequired[str]
    State: NotRequired[RestoreJobStateType]
    ResourceType: NotRequired[str]
    Count: NotRequired[int]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]

class ListRestoreTestingPlansInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class RestoreTestingPlanForListTypeDef(TypedDict):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    ScheduleExpression: str
    LastExecutionTime: NotRequired[datetime]
    LastUpdateTime: NotRequired[datetime]
    ScheduleExpressionTimezone: NotRequired[str]
    StartWindowHours: NotRequired[int]

class ListRestoreTestingSelectionsInputTypeDef(TypedDict):
    RestoreTestingPlanName: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class RestoreTestingSelectionForListTypeDef(TypedDict):
    CreationTime: datetime
    IamRoleArn: str
    ProtectedResourceType: str
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str
    ValidationWindowHours: NotRequired[int]

class ListTagsInputTypeDef(TypedDict):
    ResourceArn: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class PutBackupVaultAccessPolicyInputTypeDef(TypedDict):
    BackupVaultName: str
    Policy: NotRequired[str]

class PutBackupVaultLockConfigurationInputTypeDef(TypedDict):
    BackupVaultName: str
    MinRetentionDays: NotRequired[int]
    MaxRetentionDays: NotRequired[int]
    ChangeableForDays: NotRequired[int]

class PutBackupVaultNotificationsInputTypeDef(TypedDict):
    BackupVaultName: str
    SNSTopicArn: str
    BackupVaultEvents: Sequence[BackupVaultEventType]

class PutRestoreValidationResultInputTypeDef(TypedDict):
    RestoreJobId: str
    ValidationStatus: RestoreValidationStatusType
    ValidationStatusMessage: NotRequired[str]

class ReportDeliveryChannelOutputTypeDef(TypedDict):
    S3BucketName: str
    S3KeyPrefix: NotRequired[str]
    Formats: NotRequired[List[str]]

class ReportDeliveryChannelTypeDef(TypedDict):
    S3BucketName: str
    S3KeyPrefix: NotRequired[str]
    Formats: NotRequired[Sequence[str]]

class ReportDestinationTypeDef(TypedDict):
    S3BucketName: NotRequired[str]
    S3Keys: NotRequired[List[str]]

class ReportSettingOutputTypeDef(TypedDict):
    ReportTemplate: str
    FrameworkArns: NotRequired[List[str]]
    NumberOfFrameworks: NotRequired[int]
    Accounts: NotRequired[List[str]]
    OrganizationUnits: NotRequired[List[str]]
    Regions: NotRequired[List[str]]

class ReportSettingTypeDef(TypedDict):
    ReportTemplate: str
    FrameworkArns: NotRequired[Sequence[str]]
    NumberOfFrameworks: NotRequired[int]
    Accounts: NotRequired[Sequence[str]]
    OrganizationUnits: NotRequired[Sequence[str]]
    Regions: NotRequired[Sequence[str]]

class RestoreTestingRecoveryPointSelectionOutputTypeDef(TypedDict):
    Algorithm: NotRequired[RestoreTestingRecoveryPointSelectionAlgorithmType]
    ExcludeVaults: NotRequired[List[str]]
    IncludeVaults: NotRequired[List[str]]
    RecoveryPointTypes: NotRequired[List[RestoreTestingRecoveryPointTypeType]]
    SelectionWindowDays: NotRequired[int]

class RestoreTestingRecoveryPointSelectionTypeDef(TypedDict):
    Algorithm: NotRequired[RestoreTestingRecoveryPointSelectionAlgorithmType]
    ExcludeVaults: NotRequired[Sequence[str]]
    IncludeVaults: NotRequired[Sequence[str]]
    RecoveryPointTypes: NotRequired[Sequence[RestoreTestingRecoveryPointTypeType]]
    SelectionWindowDays: NotRequired[int]

class StartReportJobInputTypeDef(TypedDict):
    ReportPlanName: str
    IdempotencyToken: NotRequired[str]

class StartRestoreJobInputTypeDef(TypedDict):
    RecoveryPointArn: str
    Metadata: Mapping[str, str]
    IamRoleArn: NotRequired[str]
    IdempotencyToken: NotRequired[str]
    ResourceType: NotRequired[str]
    CopySourceTagsToRestoredResource: NotRequired[bool]

class StopBackupJobInputTypeDef(TypedDict):
    BackupJobId: str

class TagResourceInputTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceInputTypeDef(TypedDict):
    ResourceArn: str
    TagKeyList: Sequence[str]

class UpdateGlobalSettingsInputTypeDef(TypedDict):
    GlobalSettings: NotRequired[Mapping[str, str]]

class UpdateRecoveryPointIndexSettingsInputTypeDef(TypedDict):
    BackupVaultName: str
    RecoveryPointArn: str
    Index: IndexType
    IamRoleArn: NotRequired[str]

class UpdateRegionSettingsInputTypeDef(TypedDict):
    ResourceTypeOptInPreference: NotRequired[Mapping[str, bool]]
    ResourceTypeManagementPreference: NotRequired[Mapping[str, bool]]

class BackupPlansListMemberTypeDef(TypedDict):
    BackupPlanArn: NotRequired[str]
    BackupPlanId: NotRequired[str]
    CreationDate: NotRequired[datetime]
    DeletionDate: NotRequired[datetime]
    VersionId: NotRequired[str]
    BackupPlanName: NotRequired[str]
    CreatorRequestId: NotRequired[str]
    LastExecutionDate: NotRequired[datetime]
    AdvancedBackupSettings: NotRequired[List[AdvancedBackupSettingOutputTypeDef]]

AdvancedBackupSettingUnionTypeDef = Union[
    AdvancedBackupSettingTypeDef, AdvancedBackupSettingOutputTypeDef
]

class BackupJobTypeDef(TypedDict):
    AccountId: NotRequired[str]
    BackupJobId: NotRequired[str]
    BackupVaultName: NotRequired[str]
    BackupVaultArn: NotRequired[str]
    RecoveryPointArn: NotRequired[str]
    ResourceArn: NotRequired[str]
    CreationDate: NotRequired[datetime]
    CompletionDate: NotRequired[datetime]
    State: NotRequired[BackupJobStateType]
    StatusMessage: NotRequired[str]
    PercentDone: NotRequired[str]
    BackupSizeInBytes: NotRequired[int]
    IamRoleArn: NotRequired[str]
    CreatedBy: NotRequired[RecoveryPointCreatorTypeDef]
    ExpectedCompletionDate: NotRequired[datetime]
    StartBy: NotRequired[datetime]
    ResourceType: NotRequired[str]
    BytesTransferred: NotRequired[int]
    BackupOptions: NotRequired[Dict[str, str]]
    BackupType: NotRequired[str]
    ParentJobId: NotRequired[str]
    IsParent: NotRequired[bool]
    ResourceName: NotRequired[str]
    InitiationDate: NotRequired[datetime]
    MessageCategory: NotRequired[str]

class CopyJobTypeDef(TypedDict):
    AccountId: NotRequired[str]
    CopyJobId: NotRequired[str]
    SourceBackupVaultArn: NotRequired[str]
    SourceRecoveryPointArn: NotRequired[str]
    DestinationBackupVaultArn: NotRequired[str]
    DestinationRecoveryPointArn: NotRequired[str]
    ResourceArn: NotRequired[str]
    CreationDate: NotRequired[datetime]
    CompletionDate: NotRequired[datetime]
    State: NotRequired[CopyJobStateType]
    StatusMessage: NotRequired[str]
    BackupSizeInBytes: NotRequired[int]
    IamRoleArn: NotRequired[str]
    CreatedBy: NotRequired[RecoveryPointCreatorTypeDef]
    ResourceType: NotRequired[str]
    ParentJobId: NotRequired[str]
    IsParent: NotRequired[bool]
    CompositeMemberIdentifier: NotRequired[str]
    NumberOfChildJobs: NotRequired[int]
    ChildJobsInState: NotRequired[Dict[CopyJobStateType, int]]
    ResourceName: NotRequired[str]
    MessageCategory: NotRequired[str]

class CopyActionTypeDef(TypedDict):
    DestinationBackupVaultArn: str
    Lifecycle: NotRequired[LifecycleTypeDef]

class StartBackupJobInputTypeDef(TypedDict):
    BackupVaultName: str
    ResourceArn: str
    IamRoleArn: str
    IdempotencyToken: NotRequired[str]
    StartWindowMinutes: NotRequired[int]
    CompleteWindowMinutes: NotRequired[int]
    Lifecycle: NotRequired[LifecycleTypeDef]
    RecoveryPointTags: NotRequired[Mapping[str, str]]
    BackupOptions: NotRequired[Mapping[str, str]]
    Index: NotRequired[IndexType]

class StartCopyJobInputTypeDef(TypedDict):
    RecoveryPointArn: str
    SourceBackupVaultName: str
    DestinationBackupVaultArn: str
    IamRoleArn: str
    IdempotencyToken: NotRequired[str]
    Lifecycle: NotRequired[LifecycleTypeDef]

class UpdateRecoveryPointLifecycleInputTypeDef(TypedDict):
    BackupVaultName: str
    RecoveryPointArn: str
    Lifecycle: NotRequired[LifecycleTypeDef]

class RecoveryPointByBackupVaultTypeDef(TypedDict):
    RecoveryPointArn: NotRequired[str]
    BackupVaultName: NotRequired[str]
    BackupVaultArn: NotRequired[str]
    SourceBackupVaultArn: NotRequired[str]
    ResourceArn: NotRequired[str]
    ResourceType: NotRequired[str]
    CreatedBy: NotRequired[RecoveryPointCreatorTypeDef]
    IamRoleArn: NotRequired[str]
    Status: NotRequired[RecoveryPointStatusType]
    StatusMessage: NotRequired[str]
    CreationDate: NotRequired[datetime]
    CompletionDate: NotRequired[datetime]
    BackupSizeInBytes: NotRequired[int]
    CalculatedLifecycle: NotRequired[CalculatedLifecycleTypeDef]
    Lifecycle: NotRequired[LifecycleTypeDef]
    EncryptionKeyArn: NotRequired[str]
    IsEncrypted: NotRequired[bool]
    LastRestoreTime: NotRequired[datetime]
    ParentRecoveryPointArn: NotRequired[str]
    CompositeMemberIdentifier: NotRequired[str]
    IsParent: NotRequired[bool]
    ResourceName: NotRequired[str]
    VaultType: NotRequired[VaultTypeType]
    IndexStatus: NotRequired[IndexStatusType]
    IndexStatusMessage: NotRequired[str]

class ConditionsOutputTypeDef(TypedDict):
    StringEquals: NotRequired[List[ConditionParameterTypeDef]]
    StringNotEquals: NotRequired[List[ConditionParameterTypeDef]]
    StringLike: NotRequired[List[ConditionParameterTypeDef]]
    StringNotLike: NotRequired[List[ConditionParameterTypeDef]]

class ConditionsTypeDef(TypedDict):
    StringEquals: NotRequired[Sequence[ConditionParameterTypeDef]]
    StringNotEquals: NotRequired[Sequence[ConditionParameterTypeDef]]
    StringLike: NotRequired[Sequence[ConditionParameterTypeDef]]
    StringNotLike: NotRequired[Sequence[ConditionParameterTypeDef]]

class FrameworkControlOutputTypeDef(TypedDict):
    ControlName: str
    ControlInputParameters: NotRequired[List[ControlInputParameterTypeDef]]
    ControlScope: NotRequired[ControlScopeOutputTypeDef]

ControlScopeUnionTypeDef = Union[ControlScopeTypeDef, ControlScopeOutputTypeDef]

class CreateBackupPlanOutputTypeDef(TypedDict):
    BackupPlanId: str
    BackupPlanArn: str
    CreationDate: datetime
    VersionId: str
    AdvancedBackupSettings: List[AdvancedBackupSettingOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackupSelectionOutputTypeDef(TypedDict):
    SelectionId: str
    BackupPlanId: str
    CreationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackupVaultOutputTypeDef(TypedDict):
    BackupVaultName: str
    BackupVaultArn: str
    CreationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFrameworkOutputTypeDef(TypedDict):
    FrameworkName: str
    FrameworkArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLogicallyAirGappedBackupVaultOutputTypeDef(TypedDict):
    BackupVaultName: str
    BackupVaultArn: str
    CreationDate: datetime
    VaultState: VaultStateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReportPlanOutputTypeDef(TypedDict):
    ReportPlanName: str
    ReportPlanArn: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRestoreTestingPlanOutputTypeDef(TypedDict):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRestoreTestingSelectionOutputTypeDef(TypedDict):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBackupPlanOutputTypeDef(TypedDict):
    BackupPlanId: str
    BackupPlanArn: str
    DeletionDate: datetime
    VersionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBackupJobOutputTypeDef(TypedDict):
    AccountId: str
    BackupJobId: str
    BackupVaultName: str
    BackupVaultArn: str
    RecoveryPointArn: str
    ResourceArn: str
    CreationDate: datetime
    CompletionDate: datetime
    State: BackupJobStateType
    StatusMessage: str
    PercentDone: str
    BackupSizeInBytes: int
    IamRoleArn: str
    CreatedBy: RecoveryPointCreatorTypeDef
    ResourceType: str
    BytesTransferred: int
    ExpectedCompletionDate: datetime
    StartBy: datetime
    BackupOptions: Dict[str, str]
    BackupType: str
    ParentJobId: str
    IsParent: bool
    NumberOfChildJobs: int
    ChildJobsInState: Dict[BackupJobStateType, int]
    ResourceName: str
    InitiationDate: datetime
    MessageCategory: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBackupVaultOutputTypeDef(TypedDict):
    BackupVaultName: str
    BackupVaultArn: str
    VaultType: VaultTypeType
    VaultState: VaultStateType
    EncryptionKeyArn: str
    CreationDate: datetime
    CreatorRequestId: str
    NumberOfRecoveryPoints: int
    Locked: bool
    MinRetentionDays: int
    MaxRetentionDays: int
    LockDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGlobalSettingsOutputTypeDef(TypedDict):
    GlobalSettings: Dict[str, str]
    LastUpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProtectedResourceOutputTypeDef(TypedDict):
    ResourceArn: str
    ResourceType: str
    LastBackupTime: datetime
    ResourceName: str
    LastBackupVaultArn: str
    LastRecoveryPointArn: str
    LatestRestoreExecutionTimeMinutes: int
    LatestRestoreJobCreationDate: datetime
    LatestRestoreRecoveryPointCreationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRecoveryPointOutputTypeDef(TypedDict):
    RecoveryPointArn: str
    BackupVaultName: str
    BackupVaultArn: str
    SourceBackupVaultArn: str
    ResourceArn: str
    ResourceType: str
    CreatedBy: RecoveryPointCreatorTypeDef
    IamRoleArn: str
    Status: RecoveryPointStatusType
    StatusMessage: str
    CreationDate: datetime
    CompletionDate: datetime
    BackupSizeInBytes: int
    CalculatedLifecycle: CalculatedLifecycleTypeDef
    Lifecycle: LifecycleTypeDef
    EncryptionKeyArn: str
    IsEncrypted: bool
    StorageClass: StorageClassType
    LastRestoreTime: datetime
    ParentRecoveryPointArn: str
    CompositeMemberIdentifier: str
    IsParent: bool
    ResourceName: str
    VaultType: VaultTypeType
    IndexStatus: IndexStatusType
    IndexStatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRegionSettingsOutputTypeDef(TypedDict):
    ResourceTypeOptInPreference: Dict[str, bool]
    ResourceTypeManagementPreference: Dict[str, bool]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportBackupPlanTemplateOutputTypeDef(TypedDict):
    BackupPlanTemplateJson: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBackupVaultAccessPolicyOutputTypeDef(TypedDict):
    BackupVaultName: str
    BackupVaultArn: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBackupVaultNotificationsOutputTypeDef(TypedDict):
    BackupVaultName: str
    BackupVaultArn: str
    SNSTopicArn: str
    BackupVaultEvents: List[BackupVaultEventType]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecoveryPointIndexDetailsOutputTypeDef(TypedDict):
    RecoveryPointArn: str
    BackupVaultArn: str
    SourceResourceArn: str
    IndexCreationDate: datetime
    IndexDeletionDate: datetime
    IndexCompletionDate: datetime
    IndexStatus: IndexStatusType
    IndexStatusMessage: str
    TotalItemsIndexed: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecoveryPointRestoreMetadataOutputTypeDef(TypedDict):
    BackupVaultArn: str
    RecoveryPointArn: str
    RestoreMetadata: Dict[str, str]
    ResourceType: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRestoreJobMetadataOutputTypeDef(TypedDict):
    RestoreJobId: str
    Metadata: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRestoreTestingInferredMetadataOutputTypeDef(TypedDict):
    InferredMetadata: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSupportedResourceTypesOutputTypeDef(TypedDict):
    ResourceTypes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupJobSummariesOutputTypeDef(TypedDict):
    BackupJobSummaries: List[BackupJobSummaryTypeDef]
    AggregationPeriod: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListBackupPlanTemplatesOutputTypeDef(TypedDict):
    BackupPlanTemplatesList: List[BackupPlanTemplatesListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListBackupSelectionsOutputTypeDef(TypedDict):
    BackupSelectionsList: List[BackupSelectionsListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListBackupVaultsOutputTypeDef(TypedDict):
    BackupVaultList: List[BackupVaultListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListCopyJobSummariesOutputTypeDef(TypedDict):
    CopyJobSummaries: List[CopyJobSummaryTypeDef]
    AggregationPeriod: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsOutputTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class StartBackupJobOutputTypeDef(TypedDict):
    BackupJobId: str
    RecoveryPointArn: str
    CreationDate: datetime
    IsParent: bool
    ResponseMetadata: ResponseMetadataTypeDef

class StartCopyJobOutputTypeDef(TypedDict):
    CopyJobId: str
    CreationDate: datetime
    IsParent: bool
    ResponseMetadata: ResponseMetadataTypeDef

class StartReportJobOutputTypeDef(TypedDict):
    ReportJobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartRestoreJobOutputTypeDef(TypedDict):
    RestoreJobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBackupPlanOutputTypeDef(TypedDict):
    BackupPlanId: str
    BackupPlanArn: str
    CreationDate: datetime
    VersionId: str
    AdvancedBackupSettings: List[AdvancedBackupSettingOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFrameworkOutputTypeDef(TypedDict):
    FrameworkName: str
    FrameworkArn: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRecoveryPointIndexSettingsOutputTypeDef(TypedDict):
    BackupVaultName: str
    RecoveryPointArn: str
    IndexStatus: IndexStatusType
    Index: IndexType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRecoveryPointLifecycleOutputTypeDef(TypedDict):
    BackupVaultArn: str
    RecoveryPointArn: str
    Lifecycle: LifecycleTypeDef
    CalculatedLifecycle: CalculatedLifecycleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReportPlanOutputTypeDef(TypedDict):
    ReportPlanName: str
    ReportPlanArn: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRestoreTestingPlanOutputTypeDef(TypedDict):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRestoreTestingSelectionOutputTypeDef(TypedDict):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class RecoveryPointSelectionOutputTypeDef(TypedDict):
    VaultNames: NotRequired[List[str]]
    ResourceIdentifiers: NotRequired[List[str]]
    DateRange: NotRequired[DateRangeOutputTypeDef]

class DateRangeTypeDef(TypedDict):
    FromDate: TimestampTypeDef
    ToDate: TimestampTypeDef

class ListBackupJobsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ByResourceArn: NotRequired[str]
    ByState: NotRequired[BackupJobStateType]
    ByBackupVaultName: NotRequired[str]
    ByCreatedBefore: NotRequired[TimestampTypeDef]
    ByCreatedAfter: NotRequired[TimestampTypeDef]
    ByResourceType: NotRequired[str]
    ByAccountId: NotRequired[str]
    ByCompleteAfter: NotRequired[TimestampTypeDef]
    ByCompleteBefore: NotRequired[TimestampTypeDef]
    ByParentJobId: NotRequired[str]
    ByMessageCategory: NotRequired[str]

class ListCopyJobsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ByResourceArn: NotRequired[str]
    ByState: NotRequired[CopyJobStateType]
    ByCreatedBefore: NotRequired[TimestampTypeDef]
    ByCreatedAfter: NotRequired[TimestampTypeDef]
    ByResourceType: NotRequired[str]
    ByDestinationVaultArn: NotRequired[str]
    ByAccountId: NotRequired[str]
    ByCompleteBefore: NotRequired[TimestampTypeDef]
    ByCompleteAfter: NotRequired[TimestampTypeDef]
    ByParentJobId: NotRequired[str]
    ByMessageCategory: NotRequired[str]

class ListIndexedRecoveryPointsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SourceResourceArn: NotRequired[str]
    CreatedBefore: NotRequired[TimestampTypeDef]
    CreatedAfter: NotRequired[TimestampTypeDef]
    ResourceType: NotRequired[str]
    IndexStatus: NotRequired[IndexStatusType]

class ListRecoveryPointsByBackupVaultInputTypeDef(TypedDict):
    BackupVaultName: str
    BackupVaultAccountId: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ByResourceArn: NotRequired[str]
    ByResourceType: NotRequired[str]
    ByBackupPlanId: NotRequired[str]
    ByCreatedBefore: NotRequired[TimestampTypeDef]
    ByCreatedAfter: NotRequired[TimestampTypeDef]
    ByParentRecoveryPointArn: NotRequired[str]

class ListReportJobsInputTypeDef(TypedDict):
    ByReportPlanName: NotRequired[str]
    ByCreationBefore: NotRequired[TimestampTypeDef]
    ByCreationAfter: NotRequired[TimestampTypeDef]
    ByStatus: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListRestoreJobsByProtectedResourceInputTypeDef(TypedDict):
    ResourceArn: str
    ByStatus: NotRequired[RestoreJobStatusType]
    ByRecoveryPointCreationDateAfter: NotRequired[TimestampTypeDef]
    ByRecoveryPointCreationDateBefore: NotRequired[TimestampTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListRestoreJobsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ByAccountId: NotRequired[str]
    ByResourceType: NotRequired[str]
    ByCreatedBefore: NotRequired[TimestampTypeDef]
    ByCreatedAfter: NotRequired[TimestampTypeDef]
    ByStatus: NotRequired[RestoreJobStatusType]
    ByCompleteBefore: NotRequired[TimestampTypeDef]
    ByCompleteAfter: NotRequired[TimestampTypeDef]
    ByRestoreTestingPlanArn: NotRequired[str]

class DescribeRestoreJobOutputTypeDef(TypedDict):
    AccountId: str
    RestoreJobId: str
    RecoveryPointArn: str
    CreationDate: datetime
    CompletionDate: datetime
    Status: RestoreJobStatusType
    StatusMessage: str
    PercentDone: str
    BackupSizeInBytes: int
    IamRoleArn: str
    ExpectedCompletionTimeMinutes: int
    CreatedResourceArn: str
    ResourceType: str
    RecoveryPointCreationDate: datetime
    CreatedBy: RestoreJobCreatorTypeDef
    ValidationStatus: RestoreValidationStatusType
    ValidationStatusMessage: str
    DeletionStatus: RestoreDeletionStatusType
    DeletionStatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreJobsListMemberTypeDef(TypedDict):
    AccountId: NotRequired[str]
    RestoreJobId: NotRequired[str]
    RecoveryPointArn: NotRequired[str]
    CreationDate: NotRequired[datetime]
    CompletionDate: NotRequired[datetime]
    Status: NotRequired[RestoreJobStatusType]
    StatusMessage: NotRequired[str]
    PercentDone: NotRequired[str]
    BackupSizeInBytes: NotRequired[int]
    IamRoleArn: NotRequired[str]
    ExpectedCompletionTimeMinutes: NotRequired[int]
    CreatedResourceArn: NotRequired[str]
    ResourceType: NotRequired[str]
    RecoveryPointCreationDate: NotRequired[datetime]
    CreatedBy: NotRequired[RestoreJobCreatorTypeDef]
    ValidationStatus: NotRequired[RestoreValidationStatusType]
    ValidationStatusMessage: NotRequired[str]
    DeletionStatus: NotRequired[RestoreDeletionStatusType]
    DeletionStatusMessage: NotRequired[str]

class ListFrameworksOutputTypeDef(TypedDict):
    Frameworks: List[FrameworkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

IndexActionUnionTypeDef = Union[IndexActionTypeDef, IndexActionOutputTypeDef]

class ListIndexedRecoveryPointsOutputTypeDef(TypedDict):
    IndexedRecoveryPoints: List[IndexedRecoveryPointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ProtectedResourceConditionsOutputTypeDef(TypedDict):
    StringEquals: NotRequired[List[KeyValueTypeDef]]
    StringNotEquals: NotRequired[List[KeyValueTypeDef]]

class ProtectedResourceConditionsTypeDef(TypedDict):
    StringEquals: NotRequired[Sequence[KeyValueTypeDef]]
    StringNotEquals: NotRequired[Sequence[KeyValueTypeDef]]

class ListLegalHoldsOutputTypeDef(TypedDict):
    LegalHolds: List[LegalHoldTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListBackupJobsInputPaginateTypeDef(TypedDict):
    ByResourceArn: NotRequired[str]
    ByState: NotRequired[BackupJobStateType]
    ByBackupVaultName: NotRequired[str]
    ByCreatedBefore: NotRequired[TimestampTypeDef]
    ByCreatedAfter: NotRequired[TimestampTypeDef]
    ByResourceType: NotRequired[str]
    ByAccountId: NotRequired[str]
    ByCompleteAfter: NotRequired[TimestampTypeDef]
    ByCompleteBefore: NotRequired[TimestampTypeDef]
    ByParentJobId: NotRequired[str]
    ByMessageCategory: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBackupPlanTemplatesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBackupPlanVersionsInputPaginateTypeDef(TypedDict):
    BackupPlanId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBackupPlansInputPaginateTypeDef(TypedDict):
    IncludeDeleted: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBackupSelectionsInputPaginateTypeDef(TypedDict):
    BackupPlanId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBackupVaultsInputPaginateTypeDef(TypedDict):
    ByVaultType: NotRequired[VaultTypeType]
    ByShared: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCopyJobsInputPaginateTypeDef(TypedDict):
    ByResourceArn: NotRequired[str]
    ByState: NotRequired[CopyJobStateType]
    ByCreatedBefore: NotRequired[TimestampTypeDef]
    ByCreatedAfter: NotRequired[TimestampTypeDef]
    ByResourceType: NotRequired[str]
    ByDestinationVaultArn: NotRequired[str]
    ByAccountId: NotRequired[str]
    ByCompleteBefore: NotRequired[TimestampTypeDef]
    ByCompleteAfter: NotRequired[TimestampTypeDef]
    ByParentJobId: NotRequired[str]
    ByMessageCategory: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIndexedRecoveryPointsInputPaginateTypeDef(TypedDict):
    SourceResourceArn: NotRequired[str]
    CreatedBefore: NotRequired[TimestampTypeDef]
    CreatedAfter: NotRequired[TimestampTypeDef]
    ResourceType: NotRequired[str]
    IndexStatus: NotRequired[IndexStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLegalHoldsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProtectedResourcesByBackupVaultInputPaginateTypeDef(TypedDict):
    BackupVaultName: str
    BackupVaultAccountId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProtectedResourcesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRecoveryPointsByBackupVaultInputPaginateTypeDef(TypedDict):
    BackupVaultName: str
    BackupVaultAccountId: NotRequired[str]
    ByResourceArn: NotRequired[str]
    ByResourceType: NotRequired[str]
    ByBackupPlanId: NotRequired[str]
    ByCreatedBefore: NotRequired[TimestampTypeDef]
    ByCreatedAfter: NotRequired[TimestampTypeDef]
    ByParentRecoveryPointArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRecoveryPointsByLegalHoldInputPaginateTypeDef(TypedDict):
    LegalHoldId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRecoveryPointsByResourceInputPaginateTypeDef(TypedDict):
    ResourceArn: str
    ManagedByAWSBackupOnly: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRestoreJobsByProtectedResourceInputPaginateTypeDef(TypedDict):
    ResourceArn: str
    ByStatus: NotRequired[RestoreJobStatusType]
    ByRecoveryPointCreationDateAfter: NotRequired[TimestampTypeDef]
    ByRecoveryPointCreationDateBefore: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRestoreJobsInputPaginateTypeDef(TypedDict):
    ByAccountId: NotRequired[str]
    ByResourceType: NotRequired[str]
    ByCreatedBefore: NotRequired[TimestampTypeDef]
    ByCreatedAfter: NotRequired[TimestampTypeDef]
    ByStatus: NotRequired[RestoreJobStatusType]
    ByCompleteBefore: NotRequired[TimestampTypeDef]
    ByCompleteAfter: NotRequired[TimestampTypeDef]
    ByRestoreTestingPlanArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRestoreTestingPlansInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRestoreTestingSelectionsInputPaginateTypeDef(TypedDict):
    RestoreTestingPlanName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProtectedResourcesByBackupVaultOutputTypeDef(TypedDict):
    Results: List[ProtectedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListProtectedResourcesOutputTypeDef(TypedDict):
    Results: List[ProtectedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRecoveryPointsByLegalHoldOutputTypeDef(TypedDict):
    RecoveryPoints: List[RecoveryPointMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRecoveryPointsByResourceOutputTypeDef(TypedDict):
    RecoveryPoints: List[RecoveryPointByResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRestoreJobSummariesOutputTypeDef(TypedDict):
    RestoreJobSummaries: List[RestoreJobSummaryTypeDef]
    AggregationPeriod: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRestoreTestingPlansOutputTypeDef(TypedDict):
    RestoreTestingPlans: List[RestoreTestingPlanForListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRestoreTestingSelectionsOutputTypeDef(TypedDict):
    RestoreTestingSelections: List[RestoreTestingSelectionForListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

ReportDeliveryChannelUnionTypeDef = Union[
    ReportDeliveryChannelTypeDef, ReportDeliveryChannelOutputTypeDef
]

class ReportJobTypeDef(TypedDict):
    ReportJobId: NotRequired[str]
    ReportPlanArn: NotRequired[str]
    ReportTemplate: NotRequired[str]
    CreationTime: NotRequired[datetime]
    CompletionTime: NotRequired[datetime]
    Status: NotRequired[str]
    StatusMessage: NotRequired[str]
    ReportDestination: NotRequired[ReportDestinationTypeDef]

class ReportPlanTypeDef(TypedDict):
    ReportPlanArn: NotRequired[str]
    ReportPlanName: NotRequired[str]
    ReportPlanDescription: NotRequired[str]
    ReportSetting: NotRequired[ReportSettingOutputTypeDef]
    ReportDeliveryChannel: NotRequired[ReportDeliveryChannelOutputTypeDef]
    DeploymentStatus: NotRequired[str]
    CreationTime: NotRequired[datetime]
    LastAttemptedExecutionTime: NotRequired[datetime]
    LastSuccessfulExecutionTime: NotRequired[datetime]

ReportSettingUnionTypeDef = Union[ReportSettingTypeDef, ReportSettingOutputTypeDef]

class RestoreTestingPlanForGetTypeDef(TypedDict):
    CreationTime: datetime
    RecoveryPointSelection: RestoreTestingRecoveryPointSelectionOutputTypeDef
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    ScheduleExpression: str
    CreatorRequestId: NotRequired[str]
    LastExecutionTime: NotRequired[datetime]
    LastUpdateTime: NotRequired[datetime]
    ScheduleExpressionTimezone: NotRequired[str]
    StartWindowHours: NotRequired[int]

RestoreTestingRecoveryPointSelectionUnionTypeDef = Union[
    RestoreTestingRecoveryPointSelectionTypeDef, RestoreTestingRecoveryPointSelectionOutputTypeDef
]

class ListBackupPlanVersionsOutputTypeDef(TypedDict):
    BackupPlanVersionsList: List[BackupPlansListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListBackupPlansOutputTypeDef(TypedDict):
    BackupPlansList: List[BackupPlansListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListBackupJobsOutputTypeDef(TypedDict):
    BackupJobs: List[BackupJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeCopyJobOutputTypeDef(TypedDict):
    CopyJob: CopyJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCopyJobsOutputTypeDef(TypedDict):
    CopyJobs: List[CopyJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BackupRuleTypeDef(TypedDict):
    RuleName: str
    TargetBackupVaultName: str
    ScheduleExpression: NotRequired[str]
    StartWindowMinutes: NotRequired[int]
    CompletionWindowMinutes: NotRequired[int]
    Lifecycle: NotRequired[LifecycleTypeDef]
    RecoveryPointTags: NotRequired[Dict[str, str]]
    RuleId: NotRequired[str]
    CopyActions: NotRequired[List[CopyActionTypeDef]]
    EnableContinuousBackup: NotRequired[bool]
    ScheduleExpressionTimezone: NotRequired[str]
    IndexActions: NotRequired[List[IndexActionOutputTypeDef]]

class ListRecoveryPointsByBackupVaultOutputTypeDef(TypedDict):
    RecoveryPoints: List[RecoveryPointByBackupVaultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BackupSelectionOutputTypeDef(TypedDict):
    SelectionName: str
    IamRoleArn: str
    Resources: NotRequired[List[str]]
    ListOfTags: NotRequired[List[ConditionTypeDef]]
    NotResources: NotRequired[List[str]]
    Conditions: NotRequired[ConditionsOutputTypeDef]

class BackupSelectionTypeDef(TypedDict):
    SelectionName: str
    IamRoleArn: str
    Resources: NotRequired[Sequence[str]]
    ListOfTags: NotRequired[Sequence[ConditionTypeDef]]
    NotResources: NotRequired[Sequence[str]]
    Conditions: NotRequired[ConditionsTypeDef]

class DescribeFrameworkOutputTypeDef(TypedDict):
    FrameworkName: str
    FrameworkArn: str
    FrameworkDescription: str
    FrameworkControls: List[FrameworkControlOutputTypeDef]
    CreationTime: datetime
    DeploymentStatus: str
    FrameworkStatus: str
    IdempotencyToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FrameworkControlTypeDef(TypedDict):
    ControlName: str
    ControlInputParameters: NotRequired[Sequence[ControlInputParameterTypeDef]]
    ControlScope: NotRequired[ControlScopeUnionTypeDef]

class CreateLegalHoldOutputTypeDef(TypedDict):
    Title: str
    Status: LegalHoldStatusType
    Description: str
    LegalHoldId: str
    LegalHoldArn: str
    CreationDate: datetime
    RecoveryPointSelection: RecoveryPointSelectionOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLegalHoldOutputTypeDef(TypedDict):
    Title: str
    Status: LegalHoldStatusType
    Description: str
    CancelDescription: str
    LegalHoldId: str
    LegalHoldArn: str
    CreationDate: datetime
    CancellationDate: datetime
    RetainRecordUntil: datetime
    RecoveryPointSelection: RecoveryPointSelectionOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RecoveryPointSelectionTypeDef(TypedDict):
    VaultNames: NotRequired[Sequence[str]]
    ResourceIdentifiers: NotRequired[Sequence[str]]
    DateRange: NotRequired[DateRangeTypeDef]

class ListRestoreJobsByProtectedResourceOutputTypeDef(TypedDict):
    RestoreJobs: List[RestoreJobsListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRestoreJobsOutputTypeDef(TypedDict):
    RestoreJobs: List[RestoreJobsListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BackupRuleInputTypeDef(TypedDict):
    RuleName: str
    TargetBackupVaultName: str
    ScheduleExpression: NotRequired[str]
    StartWindowMinutes: NotRequired[int]
    CompletionWindowMinutes: NotRequired[int]
    Lifecycle: NotRequired[LifecycleTypeDef]
    RecoveryPointTags: NotRequired[Mapping[str, str]]
    CopyActions: NotRequired[Sequence[CopyActionTypeDef]]
    EnableContinuousBackup: NotRequired[bool]
    ScheduleExpressionTimezone: NotRequired[str]
    IndexActions: NotRequired[Sequence[IndexActionUnionTypeDef]]

class RestoreTestingSelectionForGetTypeDef(TypedDict):
    CreationTime: datetime
    IamRoleArn: str
    ProtectedResourceType: str
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str
    CreatorRequestId: NotRequired[str]
    ProtectedResourceArns: NotRequired[List[str]]
    ProtectedResourceConditions: NotRequired[ProtectedResourceConditionsOutputTypeDef]
    RestoreMetadataOverrides: NotRequired[Dict[str, str]]
    ValidationWindowHours: NotRequired[int]

ProtectedResourceConditionsUnionTypeDef = Union[
    ProtectedResourceConditionsTypeDef, ProtectedResourceConditionsOutputTypeDef
]

class DescribeReportJobOutputTypeDef(TypedDict):
    ReportJob: ReportJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListReportJobsOutputTypeDef(TypedDict):
    ReportJobs: List[ReportJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeReportPlanOutputTypeDef(TypedDict):
    ReportPlan: ReportPlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListReportPlansOutputTypeDef(TypedDict):
    ReportPlans: List[ReportPlanTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateReportPlanInputTypeDef(TypedDict):
    ReportPlanName: str
    ReportDeliveryChannel: ReportDeliveryChannelUnionTypeDef
    ReportSetting: ReportSettingUnionTypeDef
    ReportPlanDescription: NotRequired[str]
    ReportPlanTags: NotRequired[Mapping[str, str]]
    IdempotencyToken: NotRequired[str]

class UpdateReportPlanInputTypeDef(TypedDict):
    ReportPlanName: str
    ReportPlanDescription: NotRequired[str]
    ReportDeliveryChannel: NotRequired[ReportDeliveryChannelUnionTypeDef]
    ReportSetting: NotRequired[ReportSettingUnionTypeDef]
    IdempotencyToken: NotRequired[str]

class GetRestoreTestingPlanOutputTypeDef(TypedDict):
    RestoreTestingPlan: RestoreTestingPlanForGetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreTestingPlanForCreateTypeDef(TypedDict):
    RecoveryPointSelection: RestoreTestingRecoveryPointSelectionUnionTypeDef
    RestoreTestingPlanName: str
    ScheduleExpression: str
    ScheduleExpressionTimezone: NotRequired[str]
    StartWindowHours: NotRequired[int]

class RestoreTestingPlanForUpdateTypeDef(TypedDict):
    RecoveryPointSelection: NotRequired[RestoreTestingRecoveryPointSelectionUnionTypeDef]
    ScheduleExpression: NotRequired[str]
    ScheduleExpressionTimezone: NotRequired[str]
    StartWindowHours: NotRequired[int]

class BackupPlanTypeDef(TypedDict):
    BackupPlanName: str
    Rules: List[BackupRuleTypeDef]
    AdvancedBackupSettings: NotRequired[List[AdvancedBackupSettingOutputTypeDef]]

class GetBackupSelectionOutputTypeDef(TypedDict):
    BackupSelection: BackupSelectionOutputTypeDef
    SelectionId: str
    BackupPlanId: str
    CreationDate: datetime
    CreatorRequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

BackupSelectionUnionTypeDef = Union[BackupSelectionTypeDef, BackupSelectionOutputTypeDef]
FrameworkControlUnionTypeDef = Union[FrameworkControlTypeDef, FrameworkControlOutputTypeDef]
RecoveryPointSelectionUnionTypeDef = Union[
    RecoveryPointSelectionTypeDef, RecoveryPointSelectionOutputTypeDef
]

class BackupPlanInputTypeDef(TypedDict):
    BackupPlanName: str
    Rules: Sequence[BackupRuleInputTypeDef]
    AdvancedBackupSettings: NotRequired[Sequence[AdvancedBackupSettingUnionTypeDef]]

class GetRestoreTestingSelectionOutputTypeDef(TypedDict):
    RestoreTestingSelection: RestoreTestingSelectionForGetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreTestingSelectionForCreateTypeDef(TypedDict):
    IamRoleArn: str
    ProtectedResourceType: str
    RestoreTestingSelectionName: str
    ProtectedResourceArns: NotRequired[Sequence[str]]
    ProtectedResourceConditions: NotRequired[ProtectedResourceConditionsUnionTypeDef]
    RestoreMetadataOverrides: NotRequired[Mapping[str, str]]
    ValidationWindowHours: NotRequired[int]

class RestoreTestingSelectionForUpdateTypeDef(TypedDict):
    IamRoleArn: NotRequired[str]
    ProtectedResourceArns: NotRequired[Sequence[str]]
    ProtectedResourceConditions: NotRequired[ProtectedResourceConditionsUnionTypeDef]
    RestoreMetadataOverrides: NotRequired[Mapping[str, str]]
    ValidationWindowHours: NotRequired[int]

class CreateRestoreTestingPlanInputTypeDef(TypedDict):
    RestoreTestingPlan: RestoreTestingPlanForCreateTypeDef
    CreatorRequestId: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class UpdateRestoreTestingPlanInputTypeDef(TypedDict):
    RestoreTestingPlan: RestoreTestingPlanForUpdateTypeDef
    RestoreTestingPlanName: str

class GetBackupPlanFromJSONOutputTypeDef(TypedDict):
    BackupPlan: BackupPlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBackupPlanFromTemplateOutputTypeDef(TypedDict):
    BackupPlanDocument: BackupPlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBackupPlanOutputTypeDef(TypedDict):
    BackupPlan: BackupPlanTypeDef
    BackupPlanId: str
    BackupPlanArn: str
    VersionId: str
    CreatorRequestId: str
    CreationDate: datetime
    DeletionDate: datetime
    LastExecutionDate: datetime
    AdvancedBackupSettings: List[AdvancedBackupSettingOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackupSelectionInputTypeDef(TypedDict):
    BackupPlanId: str
    BackupSelection: BackupSelectionUnionTypeDef
    CreatorRequestId: NotRequired[str]

class CreateFrameworkInputTypeDef(TypedDict):
    FrameworkName: str
    FrameworkControls: Sequence[FrameworkControlUnionTypeDef]
    FrameworkDescription: NotRequired[str]
    IdempotencyToken: NotRequired[str]
    FrameworkTags: NotRequired[Mapping[str, str]]

class UpdateFrameworkInputTypeDef(TypedDict):
    FrameworkName: str
    FrameworkDescription: NotRequired[str]
    FrameworkControls: NotRequired[Sequence[FrameworkControlUnionTypeDef]]
    IdempotencyToken: NotRequired[str]

class CreateLegalHoldInputTypeDef(TypedDict):
    Title: str
    Description: str
    IdempotencyToken: NotRequired[str]
    RecoveryPointSelection: NotRequired[RecoveryPointSelectionUnionTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class CreateBackupPlanInputTypeDef(TypedDict):
    BackupPlan: BackupPlanInputTypeDef
    BackupPlanTags: NotRequired[Mapping[str, str]]
    CreatorRequestId: NotRequired[str]

class UpdateBackupPlanInputTypeDef(TypedDict):
    BackupPlanId: str
    BackupPlan: BackupPlanInputTypeDef

class CreateRestoreTestingSelectionInputTypeDef(TypedDict):
    RestoreTestingPlanName: str
    RestoreTestingSelection: RestoreTestingSelectionForCreateTypeDef
    CreatorRequestId: NotRequired[str]

class UpdateRestoreTestingSelectionInputTypeDef(TypedDict):
    RestoreTestingPlanName: str
    RestoreTestingSelection: RestoreTestingSelectionForUpdateTypeDef
    RestoreTestingSelectionName: str
