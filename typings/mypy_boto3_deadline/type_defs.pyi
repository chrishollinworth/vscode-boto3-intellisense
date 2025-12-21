"""
Type annotations for deadline service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_deadline.type_defs import AcceleratorCountRangeTypeDef

    data: AcceleratorCountRangeTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    AcceleratorNameType,
    AutoScalingModeType,
    AutoScalingStatusType,
    BudgetActionTypeType,
    BudgetStatusType,
    ComparisonOperatorType,
    CompletedStatusType,
    CpuArchitectureTypeType,
    CreateJobTargetTaskRunStatusType,
    CustomerManagedFleetOperatingSystemFamilyType,
    DefaultQueueBudgetActionType,
    DependencyConsumerResolutionStatusType,
    Ec2MarketTypeType,
    EnvironmentTemplateTypeType,
    FileSystemLocationTypeType,
    FleetStatusType,
    JobAttachmentsFileSystemType,
    JobEntityErrorCodeType,
    JobLifecycleStatusType,
    JobTargetTaskRunStatusType,
    JobTemplateTypeType,
    LicenseEndpointStatusType,
    LogicalOperatorType,
    MembershipLevelType,
    PathFormatType,
    PeriodType,
    PrincipalTypeType,
    QueueBlockedReasonType,
    QueueFleetAssociationStatusType,
    QueueLimitAssociationStatusType,
    QueueStatusType,
    RunAsType,
    SearchTermMatchingTypeType,
    ServiceManagedFleetOperatingSystemFamilyType,
    SessionActionStatusType,
    SessionLifecycleStatusType,
    SessionsStatisticsAggregationStatusType,
    SortOrderType,
    StepLifecycleStatusType,
    StepParameterTypeType,
    StepTargetTaskRunStatusType,
    StorageProfileOperatingSystemFamilyType,
    TagPropagationModeType,
    TaskRunStatusType,
    TaskTargetRunStatusType,
    UpdatedWorkerStatusType,
    UpdateQueueFleetAssociationStatusType,
    UpdateQueueLimitAssociationStatusType,
    UsageGroupByFieldType,
    UsageStatisticType,
    UsageTypeType,
    WorkerStatusType,
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
    "AcceleratorCapabilitiesOutputTypeDef",
    "AcceleratorCapabilitiesTypeDef",
    "AcceleratorCountRangeTypeDef",
    "AcceleratorSelectionTypeDef",
    "AcceleratorTotalMemoryMiBRangeTypeDef",
    "AcquiredLimitTypeDef",
    "AssignedEnvironmentEnterSessionActionDefinitionTypeDef",
    "AssignedEnvironmentExitSessionActionDefinitionTypeDef",
    "AssignedSessionActionDefinitionTypeDef",
    "AssignedSessionActionTypeDef",
    "AssignedSessionTypeDef",
    "AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef",
    "AssignedTaskRunSessionActionDefinitionTypeDef",
    "AssociateMemberToFarmRequestTypeDef",
    "AssociateMemberToFleetRequestTypeDef",
    "AssociateMemberToJobRequestTypeDef",
    "AssociateMemberToQueueRequestTypeDef",
    "AssumeFleetRoleForReadRequestTypeDef",
    "AssumeFleetRoleForReadResponseTypeDef",
    "AssumeFleetRoleForWorkerRequestTypeDef",
    "AssumeFleetRoleForWorkerResponseTypeDef",
    "AssumeQueueRoleForReadRequestTypeDef",
    "AssumeQueueRoleForReadResponseTypeDef",
    "AssumeQueueRoleForUserRequestTypeDef",
    "AssumeQueueRoleForUserResponseTypeDef",
    "AssumeQueueRoleForWorkerRequestTypeDef",
    "AssumeQueueRoleForWorkerResponseTypeDef",
    "AttachmentsOutputTypeDef",
    "AttachmentsTypeDef",
    "AttachmentsUnionTypeDef",
    "AwsCredentialsTypeDef",
    "BatchGetJobEntityRequestTypeDef",
    "BatchGetJobEntityResponseTypeDef",
    "BudgetActionToAddTypeDef",
    "BudgetActionToRemoveTypeDef",
    "BudgetScheduleOutputTypeDef",
    "BudgetScheduleTypeDef",
    "BudgetScheduleUnionTypeDef",
    "BudgetSummaryTypeDef",
    "ConsumedUsagesTypeDef",
    "CopyJobTemplateRequestTypeDef",
    "CopyJobTemplateResponseTypeDef",
    "CreateBudgetRequestTypeDef",
    "CreateBudgetResponseTypeDef",
    "CreateFarmRequestTypeDef",
    "CreateFarmResponseTypeDef",
    "CreateFleetRequestTypeDef",
    "CreateFleetResponseTypeDef",
    "CreateJobRequestTypeDef",
    "CreateJobResponseTypeDef",
    "CreateLicenseEndpointRequestTypeDef",
    "CreateLicenseEndpointResponseTypeDef",
    "CreateLimitRequestTypeDef",
    "CreateLimitResponseTypeDef",
    "CreateMonitorRequestTypeDef",
    "CreateMonitorResponseTypeDef",
    "CreateQueueEnvironmentRequestTypeDef",
    "CreateQueueEnvironmentResponseTypeDef",
    "CreateQueueFleetAssociationRequestTypeDef",
    "CreateQueueLimitAssociationRequestTypeDef",
    "CreateQueueRequestTypeDef",
    "CreateQueueResponseTypeDef",
    "CreateStorageProfileRequestTypeDef",
    "CreateStorageProfileResponseTypeDef",
    "CreateWorkerRequestTypeDef",
    "CreateWorkerResponseTypeDef",
    "CustomerManagedFleetConfigurationOutputTypeDef",
    "CustomerManagedFleetConfigurationTypeDef",
    "CustomerManagedWorkerCapabilitiesOutputTypeDef",
    "CustomerManagedWorkerCapabilitiesTypeDef",
    "DateTimeFilterExpressionTypeDef",
    "DeleteBudgetRequestTypeDef",
    "DeleteFarmRequestTypeDef",
    "DeleteFleetRequestTypeDef",
    "DeleteLicenseEndpointRequestTypeDef",
    "DeleteLimitRequestTypeDef",
    "DeleteMeteredProductRequestTypeDef",
    "DeleteMonitorRequestTypeDef",
    "DeleteQueueEnvironmentRequestTypeDef",
    "DeleteQueueFleetAssociationRequestTypeDef",
    "DeleteQueueLimitAssociationRequestTypeDef",
    "DeleteQueueRequestTypeDef",
    "DeleteStorageProfileRequestTypeDef",
    "DeleteWorkerRequestTypeDef",
    "DependencyCountsTypeDef",
    "DisassociateMemberFromFarmRequestTypeDef",
    "DisassociateMemberFromFleetRequestTypeDef",
    "DisassociateMemberFromJobRequestTypeDef",
    "DisassociateMemberFromQueueRequestTypeDef",
    "Ec2EbsVolumeTypeDef",
    "EnvironmentDetailsEntityTypeDef",
    "EnvironmentDetailsErrorTypeDef",
    "EnvironmentDetailsIdentifiersTypeDef",
    "EnvironmentEnterSessionActionDefinitionSummaryTypeDef",
    "EnvironmentEnterSessionActionDefinitionTypeDef",
    "EnvironmentExitSessionActionDefinitionSummaryTypeDef",
    "EnvironmentExitSessionActionDefinitionTypeDef",
    "FarmMemberTypeDef",
    "FarmSummaryTypeDef",
    "FieldSortExpressionTypeDef",
    "FileSystemLocationTypeDef",
    "FixedBudgetScheduleOutputTypeDef",
    "FixedBudgetScheduleTypeDef",
    "FleetAmountCapabilityTypeDef",
    "FleetAttributeCapabilityOutputTypeDef",
    "FleetAttributeCapabilityTypeDef",
    "FleetCapabilitiesTypeDef",
    "FleetConfigurationOutputTypeDef",
    "FleetConfigurationTypeDef",
    "FleetConfigurationUnionTypeDef",
    "FleetMemberTypeDef",
    "FleetSummaryTypeDef",
    "GetBudgetRequestTypeDef",
    "GetBudgetResponseTypeDef",
    "GetFarmRequestTypeDef",
    "GetFarmResponseTypeDef",
    "GetFleetRequestTypeDef",
    "GetFleetRequestWaitTypeDef",
    "GetFleetResponseTypeDef",
    "GetJobEntityErrorTypeDef",
    "GetJobRequestTypeDef",
    "GetJobRequestWaitTypeDef",
    "GetJobResponseTypeDef",
    "GetLicenseEndpointRequestTypeDef",
    "GetLicenseEndpointRequestWaitExtraTypeDef",
    "GetLicenseEndpointRequestWaitTypeDef",
    "GetLicenseEndpointResponseTypeDef",
    "GetLimitRequestTypeDef",
    "GetLimitResponseTypeDef",
    "GetMonitorRequestTypeDef",
    "GetMonitorResponseTypeDef",
    "GetQueueEnvironmentRequestTypeDef",
    "GetQueueEnvironmentResponseTypeDef",
    "GetQueueFleetAssociationRequestTypeDef",
    "GetQueueFleetAssociationRequestWaitTypeDef",
    "GetQueueFleetAssociationResponseTypeDef",
    "GetQueueLimitAssociationRequestTypeDef",
    "GetQueueLimitAssociationRequestWaitTypeDef",
    "GetQueueLimitAssociationResponseTypeDef",
    "GetQueueRequestTypeDef",
    "GetQueueRequestWaitExtraTypeDef",
    "GetQueueRequestWaitTypeDef",
    "GetQueueResponseTypeDef",
    "GetSessionActionRequestTypeDef",
    "GetSessionActionResponseTypeDef",
    "GetSessionRequestTypeDef",
    "GetSessionResponseTypeDef",
    "GetSessionsStatisticsAggregationRequestPaginateTypeDef",
    "GetSessionsStatisticsAggregationRequestTypeDef",
    "GetSessionsStatisticsAggregationResponseTypeDef",
    "GetStepRequestTypeDef",
    "GetStepResponseTypeDef",
    "GetStorageProfileForQueueRequestTypeDef",
    "GetStorageProfileForQueueResponseTypeDef",
    "GetStorageProfileRequestTypeDef",
    "GetStorageProfileResponseTypeDef",
    "GetTaskRequestTypeDef",
    "GetTaskResponseTypeDef",
    "GetWorkerRequestTypeDef",
    "GetWorkerResponseTypeDef",
    "HostConfigurationTypeDef",
    "HostPropertiesRequestTypeDef",
    "HostPropertiesResponseTypeDef",
    "IpAddressesOutputTypeDef",
    "IpAddressesTypeDef",
    "IpAddressesUnionTypeDef",
    "JobAttachmentDetailsEntityTypeDef",
    "JobAttachmentDetailsErrorTypeDef",
    "JobAttachmentDetailsIdentifiersTypeDef",
    "JobAttachmentSettingsTypeDef",
    "JobDetailsEntityTypeDef",
    "JobDetailsErrorTypeDef",
    "JobDetailsIdentifiersTypeDef",
    "JobEntityIdentifiersUnionTypeDef",
    "JobEntityTypeDef",
    "JobMemberTypeDef",
    "JobParameterTypeDef",
    "JobRunAsUserTypeDef",
    "JobSearchSummaryTypeDef",
    "JobSummaryTypeDef",
    "LicenseEndpointSummaryTypeDef",
    "LimitSummaryTypeDef",
    "ListAvailableMeteredProductsRequestPaginateTypeDef",
    "ListAvailableMeteredProductsRequestTypeDef",
    "ListAvailableMeteredProductsResponseTypeDef",
    "ListBudgetsRequestPaginateTypeDef",
    "ListBudgetsRequestTypeDef",
    "ListBudgetsResponseTypeDef",
    "ListFarmMembersRequestPaginateTypeDef",
    "ListFarmMembersRequestTypeDef",
    "ListFarmMembersResponseTypeDef",
    "ListFarmsRequestPaginateTypeDef",
    "ListFarmsRequestTypeDef",
    "ListFarmsResponseTypeDef",
    "ListFleetMembersRequestPaginateTypeDef",
    "ListFleetMembersRequestTypeDef",
    "ListFleetMembersResponseTypeDef",
    "ListFleetsRequestPaginateTypeDef",
    "ListFleetsRequestTypeDef",
    "ListFleetsResponseTypeDef",
    "ListJobMembersRequestPaginateTypeDef",
    "ListJobMembersRequestTypeDef",
    "ListJobMembersResponseTypeDef",
    "ListJobParameterDefinitionsRequestPaginateTypeDef",
    "ListJobParameterDefinitionsRequestTypeDef",
    "ListJobParameterDefinitionsResponseTypeDef",
    "ListJobsRequestPaginateTypeDef",
    "ListJobsRequestTypeDef",
    "ListJobsResponseTypeDef",
    "ListLicenseEndpointsRequestPaginateTypeDef",
    "ListLicenseEndpointsRequestTypeDef",
    "ListLicenseEndpointsResponseTypeDef",
    "ListLimitsRequestPaginateTypeDef",
    "ListLimitsRequestTypeDef",
    "ListLimitsResponseTypeDef",
    "ListMeteredProductsRequestPaginateTypeDef",
    "ListMeteredProductsRequestTypeDef",
    "ListMeteredProductsResponseTypeDef",
    "ListMonitorsRequestPaginateTypeDef",
    "ListMonitorsRequestTypeDef",
    "ListMonitorsResponseTypeDef",
    "ListQueueEnvironmentsRequestPaginateTypeDef",
    "ListQueueEnvironmentsRequestTypeDef",
    "ListQueueEnvironmentsResponseTypeDef",
    "ListQueueFleetAssociationsRequestPaginateTypeDef",
    "ListQueueFleetAssociationsRequestTypeDef",
    "ListQueueFleetAssociationsResponseTypeDef",
    "ListQueueLimitAssociationsRequestPaginateTypeDef",
    "ListQueueLimitAssociationsRequestTypeDef",
    "ListQueueLimitAssociationsResponseTypeDef",
    "ListQueueMembersRequestPaginateTypeDef",
    "ListQueueMembersRequestTypeDef",
    "ListQueueMembersResponseTypeDef",
    "ListQueuesRequestPaginateTypeDef",
    "ListQueuesRequestTypeDef",
    "ListQueuesResponseTypeDef",
    "ListSessionActionsRequestPaginateTypeDef",
    "ListSessionActionsRequestTypeDef",
    "ListSessionActionsResponseTypeDef",
    "ListSessionsForWorkerRequestPaginateTypeDef",
    "ListSessionsForWorkerRequestTypeDef",
    "ListSessionsForWorkerResponseTypeDef",
    "ListSessionsRequestPaginateTypeDef",
    "ListSessionsRequestTypeDef",
    "ListSessionsResponseTypeDef",
    "ListStepConsumersRequestPaginateTypeDef",
    "ListStepConsumersRequestTypeDef",
    "ListStepConsumersResponseTypeDef",
    "ListStepDependenciesRequestPaginateTypeDef",
    "ListStepDependenciesRequestTypeDef",
    "ListStepDependenciesResponseTypeDef",
    "ListStepsRequestPaginateTypeDef",
    "ListStepsRequestTypeDef",
    "ListStepsResponseTypeDef",
    "ListStorageProfilesForQueueRequestPaginateTypeDef",
    "ListStorageProfilesForQueueRequestTypeDef",
    "ListStorageProfilesForQueueResponseTypeDef",
    "ListStorageProfilesRequestPaginateTypeDef",
    "ListStorageProfilesRequestTypeDef",
    "ListStorageProfilesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTasksRequestPaginateTypeDef",
    "ListTasksRequestTypeDef",
    "ListTasksResponseTypeDef",
    "ListWorkersRequestPaginateTypeDef",
    "ListWorkersRequestTypeDef",
    "ListWorkersResponseTypeDef",
    "LogConfigurationTypeDef",
    "ManifestPropertiesOutputTypeDef",
    "ManifestPropertiesTypeDef",
    "MemoryMiBRangeTypeDef",
    "MeteredProductSummaryTypeDef",
    "MonitorSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterFilterExpressionTypeDef",
    "ParameterSortExpressionTypeDef",
    "ParameterSpaceTypeDef",
    "PathMappingRuleTypeDef",
    "PosixUserTypeDef",
    "PutMeteredProductRequestTypeDef",
    "QueueEnvironmentSummaryTypeDef",
    "QueueFleetAssociationSummaryTypeDef",
    "QueueLimitAssociationSummaryTypeDef",
    "QueueMemberTypeDef",
    "QueueSummaryTypeDef",
    "ResponseBudgetActionTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "SearchFilterExpressionTypeDef",
    "SearchGroupedFilterExpressionsTypeDef",
    "SearchJobsRequestTypeDef",
    "SearchJobsResponseTypeDef",
    "SearchSortExpressionTypeDef",
    "SearchStepsRequestTypeDef",
    "SearchStepsResponseTypeDef",
    "SearchTasksRequestTypeDef",
    "SearchTasksResponseTypeDef",
    "SearchTermFilterExpressionTypeDef",
    "SearchWorkersRequestTypeDef",
    "SearchWorkersResponseTypeDef",
    "ServiceManagedEc2FleetConfigurationOutputTypeDef",
    "ServiceManagedEc2FleetConfigurationTypeDef",
    "ServiceManagedEc2InstanceCapabilitiesOutputTypeDef",
    "ServiceManagedEc2InstanceCapabilitiesTypeDef",
    "ServiceManagedEc2InstanceMarketOptionsTypeDef",
    "SessionActionDefinitionSummaryTypeDef",
    "SessionActionDefinitionTypeDef",
    "SessionActionSummaryTypeDef",
    "SessionSummaryTypeDef",
    "SessionsStatisticsResourcesTypeDef",
    "StartSessionsStatisticsAggregationRequestTypeDef",
    "StartSessionsStatisticsAggregationResponseTypeDef",
    "StatisticsTypeDef",
    "StatsTypeDef",
    "StepAmountCapabilityTypeDef",
    "StepAttributeCapabilityTypeDef",
    "StepConsumerTypeDef",
    "StepDependencyTypeDef",
    "StepDetailsEntityTypeDef",
    "StepDetailsErrorTypeDef",
    "StepDetailsIdentifiersTypeDef",
    "StepParameterTypeDef",
    "StepRequiredCapabilitiesTypeDef",
    "StepSearchSummaryTypeDef",
    "StepSummaryTypeDef",
    "StorageProfileSummaryTypeDef",
    "StringFilterExpressionTypeDef",
    "SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef",
    "SyncInputJobAttachmentsSessionActionDefinitionTypeDef",
    "TagResourceRequestTypeDef",
    "TaskParameterValueTypeDef",
    "TaskRunManifestPropertiesRequestTypeDef",
    "TaskRunManifestPropertiesResponseTypeDef",
    "TaskRunSessionActionDefinitionSummaryTypeDef",
    "TaskRunSessionActionDefinitionTypeDef",
    "TaskSearchSummaryTypeDef",
    "TaskSummaryTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateBudgetRequestTypeDef",
    "UpdateFarmRequestTypeDef",
    "UpdateFleetRequestTypeDef",
    "UpdateJobRequestTypeDef",
    "UpdateLimitRequestTypeDef",
    "UpdateMonitorRequestTypeDef",
    "UpdateQueueEnvironmentRequestTypeDef",
    "UpdateQueueFleetAssociationRequestTypeDef",
    "UpdateQueueLimitAssociationRequestTypeDef",
    "UpdateQueueRequestTypeDef",
    "UpdateSessionRequestTypeDef",
    "UpdateStepRequestTypeDef",
    "UpdateStorageProfileRequestTypeDef",
    "UpdateTaskRequestTypeDef",
    "UpdateWorkerRequestTypeDef",
    "UpdateWorkerResponseTypeDef",
    "UpdateWorkerScheduleRequestTypeDef",
    "UpdateWorkerScheduleResponseTypeDef",
    "UpdatedSessionActionInfoTypeDef",
    "UsageTrackingResourceTypeDef",
    "UserJobsFirstTypeDef",
    "VCpuCountRangeTypeDef",
    "VpcConfigurationOutputTypeDef",
    "VpcConfigurationTypeDef",
    "WaiterConfigTypeDef",
    "WindowsUserTypeDef",
    "WorkerAmountCapabilityTypeDef",
    "WorkerAttributeCapabilityTypeDef",
    "WorkerCapabilitiesTypeDef",
    "WorkerSearchSummaryTypeDef",
    "WorkerSessionSummaryTypeDef",
    "WorkerSummaryTypeDef",
)

AcceleratorCountRangeTypeDef = TypedDict(
    "AcceleratorCountRangeTypeDef",
    {
        "min": int,
        "max": NotRequired[int],
    },
)

class AcceleratorSelectionTypeDef(TypedDict):
    name: AcceleratorNameType
    runtime: NotRequired[str]

AcceleratorTotalMemoryMiBRangeTypeDef = TypedDict(
    "AcceleratorTotalMemoryMiBRangeTypeDef",
    {
        "min": int,
        "max": NotRequired[int],
    },
)

class AcquiredLimitTypeDef(TypedDict):
    limitId: str
    count: int

class AssignedEnvironmentEnterSessionActionDefinitionTypeDef(TypedDict):
    environmentId: str

class AssignedEnvironmentExitSessionActionDefinitionTypeDef(TypedDict):
    environmentId: str

class AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef(TypedDict):
    stepId: NotRequired[str]

class LogConfigurationTypeDef(TypedDict):
    logDriver: str
    options: NotRequired[Dict[str, str]]
    parameters: NotRequired[Dict[str, str]]
    error: NotRequired[str]

TaskParameterValueTypeDef = TypedDict(
    "TaskParameterValueTypeDef",
    {
        "int": NotRequired[str],
        "float": NotRequired[str],
        "string": NotRequired[str],
        "path": NotRequired[str],
        "chunkInt": NotRequired[str],
    },
)

class AssociateMemberToFarmRequestTypeDef(TypedDict):
    farmId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType

class AssociateMemberToFleetRequestTypeDef(TypedDict):
    farmId: str
    fleetId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType

class AssociateMemberToJobRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType

class AssociateMemberToQueueRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType

class AssumeFleetRoleForReadRequestTypeDef(TypedDict):
    farmId: str
    fleetId: str

class AwsCredentialsTypeDef(TypedDict):
    accessKeyId: str
    secretAccessKey: str
    sessionToken: str
    expiration: datetime

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AssumeFleetRoleForWorkerRequestTypeDef(TypedDict):
    farmId: str
    fleetId: str
    workerId: str

class AssumeQueueRoleForReadRequestTypeDef(TypedDict):
    farmId: str
    queueId: str

class AssumeQueueRoleForUserRequestTypeDef(TypedDict):
    farmId: str
    queueId: str

class AssumeQueueRoleForWorkerRequestTypeDef(TypedDict):
    farmId: str
    fleetId: str
    workerId: str
    queueId: str

class ManifestPropertiesOutputTypeDef(TypedDict):
    rootPath: str
    rootPathFormat: PathFormatType
    fileSystemLocationName: NotRequired[str]
    outputRelativeDirectories: NotRequired[List[str]]
    inputManifestPath: NotRequired[str]
    inputManifestHash: NotRequired[str]

class ManifestPropertiesTypeDef(TypedDict):
    rootPath: str
    rootPathFormat: PathFormatType
    fileSystemLocationName: NotRequired[str]
    outputRelativeDirectories: NotRequired[Sequence[str]]
    inputManifestPath: NotRequired[str]
    inputManifestHash: NotRequired[str]

BudgetActionToAddTypeDef = TypedDict(
    "BudgetActionToAddTypeDef",
    {
        "type": BudgetActionTypeType,
        "thresholdPercentage": float,
        "description": NotRequired[str],
    },
)
BudgetActionToRemoveTypeDef = TypedDict(
    "BudgetActionToRemoveTypeDef",
    {
        "type": BudgetActionTypeType,
        "thresholdPercentage": float,
    },
)

class FixedBudgetScheduleOutputTypeDef(TypedDict):
    startTime: datetime
    endTime: datetime

class ConsumedUsagesTypeDef(TypedDict):
    approximateDollarUsage: float

class UsageTrackingResourceTypeDef(TypedDict):
    queueId: NotRequired[str]

class S3LocationTypeDef(TypedDict):
    bucketName: str
    key: str

class CreateFarmRequestTypeDef(TypedDict):
    displayName: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    kmsKeyArn: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class HostConfigurationTypeDef(TypedDict):
    scriptBody: str
    scriptTimeoutSeconds: NotRequired[int]

JobParameterTypeDef = TypedDict(
    "JobParameterTypeDef",
    {
        "int": NotRequired[str],
        "float": NotRequired[str],
        "string": NotRequired[str],
        "path": NotRequired[str],
    },
)

class CreateLicenseEndpointRequestTypeDef(TypedDict):
    vpcId: str
    subnetIds: Sequence[str]
    securityGroupIds: Sequence[str]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateLimitRequestTypeDef(TypedDict):
    displayName: str
    amountRequirementName: str
    maxCount: int
    farmId: str
    clientToken: NotRequired[str]
    description: NotRequired[str]

class CreateMonitorRequestTypeDef(TypedDict):
    displayName: str
    identityCenterInstanceArn: str
    subdomain: str
    roleArn: str
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateQueueEnvironmentRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    priority: int
    templateType: EnvironmentTemplateTypeType
    template: str
    clientToken: NotRequired[str]

class CreateQueueFleetAssociationRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    fleetId: str

class CreateQueueLimitAssociationRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    limitId: str

class JobAttachmentSettingsTypeDef(TypedDict):
    s3BucketName: str
    rootPrefix: str

FileSystemLocationTypeDef = TypedDict(
    "FileSystemLocationTypeDef",
    {
        "name": str,
        "path": str,
        "type": FileSystemLocationTypeType,
    },
)
FleetAmountCapabilityTypeDef = TypedDict(
    "FleetAmountCapabilityTypeDef",
    {
        "name": str,
        "min": float,
        "max": NotRequired[float],
    },
)

class FleetAttributeCapabilityOutputTypeDef(TypedDict):
    name: str
    values: List[str]

MemoryMiBRangeTypeDef = TypedDict(
    "MemoryMiBRangeTypeDef",
    {
        "min": int,
        "max": NotRequired[int],
    },
)
VCpuCountRangeTypeDef = TypedDict(
    "VCpuCountRangeTypeDef",
    {
        "min": int,
        "max": NotRequired[int],
    },
)

class FleetAttributeCapabilityTypeDef(TypedDict):
    name: str
    values: Sequence[str]

TimestampTypeDef = Union[datetime, str]

class DeleteBudgetRequestTypeDef(TypedDict):
    farmId: str
    budgetId: str

class DeleteFarmRequestTypeDef(TypedDict):
    farmId: str

class DeleteFleetRequestTypeDef(TypedDict):
    farmId: str
    fleetId: str
    clientToken: NotRequired[str]

class DeleteLicenseEndpointRequestTypeDef(TypedDict):
    licenseEndpointId: str

class DeleteLimitRequestTypeDef(TypedDict):
    farmId: str
    limitId: str

class DeleteMeteredProductRequestTypeDef(TypedDict):
    licenseEndpointId: str
    productId: str

class DeleteMonitorRequestTypeDef(TypedDict):
    monitorId: str

class DeleteQueueEnvironmentRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    queueEnvironmentId: str

class DeleteQueueFleetAssociationRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    fleetId: str

class DeleteQueueLimitAssociationRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    limitId: str

class DeleteQueueRequestTypeDef(TypedDict):
    farmId: str
    queueId: str

class DeleteStorageProfileRequestTypeDef(TypedDict):
    farmId: str
    storageProfileId: str

class DeleteWorkerRequestTypeDef(TypedDict):
    farmId: str
    fleetId: str
    workerId: str

class DependencyCountsTypeDef(TypedDict):
    dependenciesResolved: int
    dependenciesUnresolved: int
    consumersResolved: int
    consumersUnresolved: int

class DisassociateMemberFromFarmRequestTypeDef(TypedDict):
    farmId: str
    principalId: str

class DisassociateMemberFromFleetRequestTypeDef(TypedDict):
    farmId: str
    fleetId: str
    principalId: str

class DisassociateMemberFromJobRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    principalId: str

class DisassociateMemberFromQueueRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    principalId: str

class Ec2EbsVolumeTypeDef(TypedDict):
    sizeGiB: NotRequired[int]
    iops: NotRequired[int]
    throughputMiB: NotRequired[int]

class EnvironmentDetailsEntityTypeDef(TypedDict):
    jobId: str
    environmentId: str
    schemaVersion: str
    template: Dict[str, Any]

class EnvironmentDetailsErrorTypeDef(TypedDict):
    jobId: str
    environmentId: str
    code: JobEntityErrorCodeType
    message: str

class EnvironmentDetailsIdentifiersTypeDef(TypedDict):
    jobId: str
    environmentId: str

class EnvironmentEnterSessionActionDefinitionSummaryTypeDef(TypedDict):
    environmentId: str

class EnvironmentEnterSessionActionDefinitionTypeDef(TypedDict):
    environmentId: str

class EnvironmentExitSessionActionDefinitionSummaryTypeDef(TypedDict):
    environmentId: str

class EnvironmentExitSessionActionDefinitionTypeDef(TypedDict):
    environmentId: str

class FarmMemberTypeDef(TypedDict):
    farmId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType

class FarmSummaryTypeDef(TypedDict):
    farmId: str
    displayName: str
    createdAt: datetime
    createdBy: str
    kmsKeyArn: NotRequired[str]
    updatedAt: NotRequired[datetime]
    updatedBy: NotRequired[str]

class FieldSortExpressionTypeDef(TypedDict):
    sortOrder: SortOrderType
    name: str

class FleetMemberTypeDef(TypedDict):
    farmId: str
    fleetId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType

class GetBudgetRequestTypeDef(TypedDict):
    farmId: str
    budgetId: str

ResponseBudgetActionTypeDef = TypedDict(
    "ResponseBudgetActionTypeDef",
    {
        "type": BudgetActionTypeType,
        "thresholdPercentage": float,
        "description": NotRequired[str],
    },
)

class GetFarmRequestTypeDef(TypedDict):
    farmId: str

class GetFleetRequestTypeDef(TypedDict):
    farmId: str
    fleetId: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class JobAttachmentDetailsErrorTypeDef(TypedDict):
    jobId: str
    code: JobEntityErrorCodeType
    message: str

class JobDetailsErrorTypeDef(TypedDict):
    jobId: str
    code: JobEntityErrorCodeType
    message: str

class StepDetailsErrorTypeDef(TypedDict):
    jobId: str
    stepId: str
    code: JobEntityErrorCodeType
    message: str

class GetJobRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str

class GetLicenseEndpointRequestTypeDef(TypedDict):
    licenseEndpointId: str

class GetLimitRequestTypeDef(TypedDict):
    farmId: str
    limitId: str

class GetMonitorRequestTypeDef(TypedDict):
    monitorId: str

class GetQueueEnvironmentRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    queueEnvironmentId: str

class GetQueueFleetAssociationRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    fleetId: str

class GetQueueLimitAssociationRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    limitId: str

class GetQueueRequestTypeDef(TypedDict):
    farmId: str
    queueId: str

class GetSessionActionRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    sessionActionId: str

class TaskRunManifestPropertiesResponseTypeDef(TypedDict):
    outputManifestPath: NotRequired[str]
    outputManifestHash: NotRequired[str]

class GetSessionRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    sessionId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetSessionsStatisticsAggregationRequestTypeDef(TypedDict):
    farmId: str
    aggregationId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class GetStepRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    stepId: str

class GetStorageProfileForQueueRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    storageProfileId: str

class GetStorageProfileRequestTypeDef(TypedDict):
    farmId: str
    storageProfileId: str

class GetTaskRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    taskId: str

class GetWorkerRequestTypeDef(TypedDict):
    farmId: str
    fleetId: str
    workerId: str

class IpAddressesOutputTypeDef(TypedDict):
    ipV4Addresses: NotRequired[List[str]]
    ipV6Addresses: NotRequired[List[str]]

class IpAddressesTypeDef(TypedDict):
    ipV4Addresses: NotRequired[Sequence[str]]
    ipV6Addresses: NotRequired[Sequence[str]]

class JobAttachmentDetailsIdentifiersTypeDef(TypedDict):
    jobId: str

class PathMappingRuleTypeDef(TypedDict):
    sourcePathFormat: PathFormatType
    sourcePath: str
    destinationPath: str

class JobDetailsIdentifiersTypeDef(TypedDict):
    jobId: str

class StepDetailsIdentifiersTypeDef(TypedDict):
    jobId: str
    stepId: str

class StepDetailsEntityTypeDef(TypedDict):
    jobId: str
    stepId: str
    schemaVersion: str
    template: Dict[str, Any]
    dependencies: List[str]

class JobMemberTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType

class PosixUserTypeDef(TypedDict):
    user: str
    group: str

class WindowsUserTypeDef(TypedDict):
    user: str
    passwordArn: str

class JobSummaryTypeDef(TypedDict):
    jobId: str
    name: str
    lifecycleStatus: JobLifecycleStatusType
    lifecycleStatusMessage: str
    priority: int
    createdAt: datetime
    createdBy: str
    updatedAt: NotRequired[datetime]
    updatedBy: NotRequired[str]
    startedAt: NotRequired[datetime]
    endedAt: NotRequired[datetime]
    taskRunStatus: NotRequired[TaskRunStatusType]
    targetTaskRunStatus: NotRequired[JobTargetTaskRunStatusType]
    taskRunStatusCounts: NotRequired[Dict[TaskRunStatusType, int]]
    taskFailureRetryCount: NotRequired[int]
    maxFailedTasksCount: NotRequired[int]
    maxRetriesPerTask: NotRequired[int]
    maxWorkerCount: NotRequired[int]
    sourceJobId: NotRequired[str]

class LicenseEndpointSummaryTypeDef(TypedDict):
    licenseEndpointId: NotRequired[str]
    status: NotRequired[LicenseEndpointStatusType]
    statusMessage: NotRequired[str]
    vpcId: NotRequired[str]

class LimitSummaryTypeDef(TypedDict):
    displayName: str
    amountRequirementName: str
    maxCount: int
    createdAt: datetime
    createdBy: str
    farmId: str
    limitId: str
    currentCount: int
    updatedAt: NotRequired[datetime]
    updatedBy: NotRequired[str]

class ListAvailableMeteredProductsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class MeteredProductSummaryTypeDef(TypedDict):
    productId: str
    family: str
    vendor: str
    port: int

class ListBudgetsRequestTypeDef(TypedDict):
    farmId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    status: NotRequired[BudgetStatusType]

class ListFarmMembersRequestTypeDef(TypedDict):
    farmId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListFarmsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    principalId: NotRequired[str]
    maxResults: NotRequired[int]

class ListFleetMembersRequestTypeDef(TypedDict):
    farmId: str
    fleetId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListFleetsRequestTypeDef(TypedDict):
    farmId: str
    principalId: NotRequired[str]
    displayName: NotRequired[str]
    status: NotRequired[FleetStatusType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListJobMembersRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListJobParameterDefinitionsRequestTypeDef(TypedDict):
    farmId: str
    jobId: str
    queueId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListJobsRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    principalId: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListLicenseEndpointsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListLimitsRequestTypeDef(TypedDict):
    farmId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListMeteredProductsRequestTypeDef(TypedDict):
    licenseEndpointId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListMonitorsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class MonitorSummaryTypeDef(TypedDict):
    monitorId: str
    displayName: str
    subdomain: str
    url: str
    roleArn: str
    identityCenterInstanceArn: str
    identityCenterApplicationArn: str
    createdAt: datetime
    createdBy: str
    updatedAt: NotRequired[datetime]
    updatedBy: NotRequired[str]

class ListQueueEnvironmentsRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class QueueEnvironmentSummaryTypeDef(TypedDict):
    queueEnvironmentId: str
    name: str
    priority: int

class ListQueueFleetAssociationsRequestTypeDef(TypedDict):
    farmId: str
    queueId: NotRequired[str]
    fleetId: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class QueueFleetAssociationSummaryTypeDef(TypedDict):
    queueId: str
    fleetId: str
    status: QueueFleetAssociationStatusType
    createdAt: datetime
    createdBy: str
    updatedAt: NotRequired[datetime]
    updatedBy: NotRequired[str]

class ListQueueLimitAssociationsRequestTypeDef(TypedDict):
    farmId: str
    queueId: NotRequired[str]
    limitId: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class QueueLimitAssociationSummaryTypeDef(TypedDict):
    createdAt: datetime
    createdBy: str
    queueId: str
    limitId: str
    status: QueueLimitAssociationStatusType
    updatedAt: NotRequired[datetime]
    updatedBy: NotRequired[str]

class ListQueueMembersRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class QueueMemberTypeDef(TypedDict):
    farmId: str
    queueId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType

class ListQueuesRequestTypeDef(TypedDict):
    farmId: str
    principalId: NotRequired[str]
    status: NotRequired[QueueStatusType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class QueueSummaryTypeDef(TypedDict):
    farmId: str
    queueId: str
    displayName: str
    status: QueueStatusType
    defaultBudgetAction: DefaultQueueBudgetActionType
    createdAt: datetime
    createdBy: str
    blockedReason: NotRequired[QueueBlockedReasonType]
    updatedAt: NotRequired[datetime]
    updatedBy: NotRequired[str]

class ListSessionActionsRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    sessionId: NotRequired[str]
    taskId: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListSessionsForWorkerRequestTypeDef(TypedDict):
    farmId: str
    fleetId: str
    workerId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class WorkerSessionSummaryTypeDef(TypedDict):
    sessionId: str
    queueId: str
    jobId: str
    startedAt: datetime
    lifecycleStatus: SessionLifecycleStatusType
    endedAt: NotRequired[datetime]
    targetLifecycleStatus: NotRequired[Literal["ENDED"]]

class ListSessionsRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class SessionSummaryTypeDef(TypedDict):
    sessionId: str
    fleetId: str
    workerId: str
    startedAt: datetime
    lifecycleStatus: SessionLifecycleStatusType
    endedAt: NotRequired[datetime]
    updatedAt: NotRequired[datetime]
    updatedBy: NotRequired[str]
    targetLifecycleStatus: NotRequired[Literal["ENDED"]]

class ListStepConsumersRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class StepConsumerTypeDef(TypedDict):
    stepId: str
    status: DependencyConsumerResolutionStatusType

class ListStepDependenciesRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class StepDependencyTypeDef(TypedDict):
    stepId: str
    status: DependencyConsumerResolutionStatusType

class ListStepsRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListStorageProfilesForQueueRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class StorageProfileSummaryTypeDef(TypedDict):
    storageProfileId: str
    displayName: str
    osFamily: StorageProfileOperatingSystemFamilyType

class ListStorageProfilesRequestTypeDef(TypedDict):
    farmId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListTasksRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListWorkersRequestTypeDef(TypedDict):
    farmId: str
    fleetId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

ParameterFilterExpressionTypeDef = TypedDict(
    "ParameterFilterExpressionTypeDef",
    {
        "name": str,
        "operator": ComparisonOperatorType,
        "value": str,
    },
)

class ParameterSortExpressionTypeDef(TypedDict):
    sortOrder: SortOrderType
    name: str

StepParameterTypeDef = TypedDict(
    "StepParameterTypeDef",
    {
        "name": str,
        "type": StepParameterTypeType,
    },
)

class PutMeteredProductRequestTypeDef(TypedDict):
    licenseEndpointId: str
    productId: str

class SearchTermFilterExpressionTypeDef(TypedDict):
    searchTerm: str
    matchType: NotRequired[SearchTermMatchingTypeType]

StringFilterExpressionTypeDef = TypedDict(
    "StringFilterExpressionTypeDef",
    {
        "name": str,
        "operator": ComparisonOperatorType,
        "value": str,
    },
)

class UserJobsFirstTypeDef(TypedDict):
    userIdentityId: str

ServiceManagedEc2InstanceMarketOptionsTypeDef = TypedDict(
    "ServiceManagedEc2InstanceMarketOptionsTypeDef",
    {
        "type": Ec2MarketTypeType,
    },
)

class VpcConfigurationOutputTypeDef(TypedDict):
    resourceConfigurationArns: NotRequired[List[str]]

class VpcConfigurationTypeDef(TypedDict):
    resourceConfigurationArns: NotRequired[Sequence[str]]

class SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef(TypedDict):
    stepId: NotRequired[str]

class SyncInputJobAttachmentsSessionActionDefinitionTypeDef(TypedDict):
    stepId: NotRequired[str]

class SessionsStatisticsResourcesTypeDef(TypedDict):
    queueIds: NotRequired[Sequence[str]]
    fleetIds: NotRequired[Sequence[str]]

StatsTypeDef = TypedDict(
    "StatsTypeDef",
    {
        "min": NotRequired[float],
        "max": NotRequired[float],
        "avg": NotRequired[float],
        "sum": NotRequired[float],
    },
)
StepAmountCapabilityTypeDef = TypedDict(
    "StepAmountCapabilityTypeDef",
    {
        "name": str,
        "min": NotRequired[float],
        "max": NotRequired[float],
        "value": NotRequired[float],
    },
)

class StepAttributeCapabilityTypeDef(TypedDict):
    name: str
    anyOf: NotRequired[List[str]]
    allOf: NotRequired[List[str]]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: NotRequired[Mapping[str, str]]

class TaskRunManifestPropertiesRequestTypeDef(TypedDict):
    outputManifestPath: NotRequired[str]
    outputManifestHash: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateFarmRequestTypeDef(TypedDict):
    farmId: str
    displayName: NotRequired[str]
    description: NotRequired[str]

class UpdateJobRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    clientToken: NotRequired[str]
    targetTaskRunStatus: NotRequired[JobTargetTaskRunStatusType]
    priority: NotRequired[int]
    maxFailedTasksCount: NotRequired[int]
    maxRetriesPerTask: NotRequired[int]
    lifecycleStatus: NotRequired[Literal["ARCHIVED"]]
    maxWorkerCount: NotRequired[int]

class UpdateLimitRequestTypeDef(TypedDict):
    farmId: str
    limitId: str
    displayName: NotRequired[str]
    description: NotRequired[str]
    maxCount: NotRequired[int]

class UpdateMonitorRequestTypeDef(TypedDict):
    monitorId: str
    subdomain: NotRequired[str]
    displayName: NotRequired[str]
    roleArn: NotRequired[str]

class UpdateQueueEnvironmentRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    queueEnvironmentId: str
    clientToken: NotRequired[str]
    priority: NotRequired[int]
    templateType: NotRequired[EnvironmentTemplateTypeType]
    template: NotRequired[str]

class UpdateQueueFleetAssociationRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    fleetId: str
    status: UpdateQueueFleetAssociationStatusType

class UpdateQueueLimitAssociationRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    limitId: str
    status: UpdateQueueLimitAssociationStatusType

class UpdateSessionRequestTypeDef(TypedDict):
    targetLifecycleStatus: Literal["ENDED"]
    farmId: str
    queueId: str
    jobId: str
    sessionId: str
    clientToken: NotRequired[str]

class UpdateStepRequestTypeDef(TypedDict):
    targetTaskRunStatus: StepTargetTaskRunStatusType
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    clientToken: NotRequired[str]

class UpdateTaskRequestTypeDef(TypedDict):
    targetRunStatus: TaskTargetRunStatusType
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    taskId: str
    clientToken: NotRequired[str]

class WorkerAmountCapabilityTypeDef(TypedDict):
    name: str
    value: float

class WorkerAttributeCapabilityTypeDef(TypedDict):
    name: str
    values: Sequence[str]

class AcceleratorCapabilitiesOutputTypeDef(TypedDict):
    selections: List[AcceleratorSelectionTypeDef]
    count: NotRequired[AcceleratorCountRangeTypeDef]

class AcceleratorCapabilitiesTypeDef(TypedDict):
    selections: Sequence[AcceleratorSelectionTypeDef]
    count: NotRequired[AcceleratorCountRangeTypeDef]

class AssignedTaskRunSessionActionDefinitionTypeDef(TypedDict):
    stepId: str
    parameters: Dict[str, TaskParameterValueTypeDef]
    taskId: NotRequired[str]

class TaskRunSessionActionDefinitionSummaryTypeDef(TypedDict):
    stepId: str
    taskId: NotRequired[str]
    parameters: NotRequired[Dict[str, TaskParameterValueTypeDef]]

class TaskRunSessionActionDefinitionTypeDef(TypedDict):
    stepId: str
    parameters: Dict[str, TaskParameterValueTypeDef]
    taskId: NotRequired[str]

class TaskSearchSummaryTypeDef(TypedDict):
    taskId: NotRequired[str]
    stepId: NotRequired[str]
    jobId: NotRequired[str]
    queueId: NotRequired[str]
    runStatus: NotRequired[TaskRunStatusType]
    targetRunStatus: NotRequired[TaskTargetRunStatusType]
    parameters: NotRequired[Dict[str, TaskParameterValueTypeDef]]
    failureRetryCount: NotRequired[int]
    startedAt: NotRequired[datetime]
    endedAt: NotRequired[datetime]
    updatedAt: NotRequired[datetime]
    updatedBy: NotRequired[str]

class TaskSummaryTypeDef(TypedDict):
    taskId: str
    createdAt: datetime
    createdBy: str
    runStatus: TaskRunStatusType
    targetRunStatus: NotRequired[TaskTargetRunStatusType]
    failureRetryCount: NotRequired[int]
    parameters: NotRequired[Dict[str, TaskParameterValueTypeDef]]
    startedAt: NotRequired[datetime]
    endedAt: NotRequired[datetime]
    updatedAt: NotRequired[datetime]
    updatedBy: NotRequired[str]
    latestSessionActionId: NotRequired[str]

class AssumeFleetRoleForReadResponseTypeDef(TypedDict):
    credentials: AwsCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssumeFleetRoleForWorkerResponseTypeDef(TypedDict):
    credentials: AwsCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssumeQueueRoleForReadResponseTypeDef(TypedDict):
    credentials: AwsCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssumeQueueRoleForUserResponseTypeDef(TypedDict):
    credentials: AwsCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssumeQueueRoleForWorkerResponseTypeDef(TypedDict):
    credentials: AwsCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CopyJobTemplateResponseTypeDef(TypedDict):
    templateType: JobTemplateTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBudgetResponseTypeDef(TypedDict):
    budgetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFarmResponseTypeDef(TypedDict):
    farmId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetResponseTypeDef(TypedDict):
    fleetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobResponseTypeDef(TypedDict):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLicenseEndpointResponseTypeDef(TypedDict):
    licenseEndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLimitResponseTypeDef(TypedDict):
    limitId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMonitorResponseTypeDef(TypedDict):
    monitorId: str
    identityCenterApplicationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQueueEnvironmentResponseTypeDef(TypedDict):
    queueEnvironmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQueueResponseTypeDef(TypedDict):
    queueId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStorageProfileResponseTypeDef(TypedDict):
    storageProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkerResponseTypeDef(TypedDict):
    workerId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFarmResponseTypeDef(TypedDict):
    farmId: str
    displayName: str
    description: str
    kmsKeyArn: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLicenseEndpointResponseTypeDef(TypedDict):
    licenseEndpointId: str
    status: LicenseEndpointStatusType
    statusMessage: str
    vpcId: str
    dnsName: str
    subnetIds: List[str]
    securityGroupIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetLimitResponseTypeDef(TypedDict):
    displayName: str
    amountRequirementName: str
    maxCount: int
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    farmId: str
    limitId: str
    currentCount: int
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMonitorResponseTypeDef(TypedDict):
    monitorId: str
    displayName: str
    subdomain: str
    url: str
    roleArn: str
    identityCenterInstanceArn: str
    identityCenterApplicationArn: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueueEnvironmentResponseTypeDef(TypedDict):
    queueEnvironmentId: str
    name: str
    priority: int
    templateType: EnvironmentTemplateTypeType
    template: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueueFleetAssociationResponseTypeDef(TypedDict):
    queueId: str
    fleetId: str
    status: QueueFleetAssociationStatusType
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueueLimitAssociationResponseTypeDef(TypedDict):
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    queueId: str
    limitId: str
    status: QueueLimitAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetTaskResponseTypeDef(TypedDict):
    taskId: str
    createdAt: datetime
    createdBy: str
    runStatus: TaskRunStatusType
    targetRunStatus: TaskTargetRunStatusType
    failureRetryCount: int
    parameters: Dict[str, TaskParameterValueTypeDef]
    startedAt: datetime
    endedAt: datetime
    updatedAt: datetime
    updatedBy: str
    latestSessionActionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobParameterDefinitionsResponseTypeDef(TypedDict):
    jobParameterDefinitions: List[Dict[str, Any]]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartSessionsStatisticsAggregationResponseTypeDef(TypedDict):
    aggregationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AttachmentsOutputTypeDef(TypedDict):
    manifests: List[ManifestPropertiesOutputTypeDef]
    fileSystem: NotRequired[JobAttachmentsFileSystemType]

class AttachmentsTypeDef(TypedDict):
    manifests: Sequence[ManifestPropertiesTypeDef]
    fileSystem: NotRequired[JobAttachmentsFileSystemType]

class BudgetScheduleOutputTypeDef(TypedDict):
    fixed: NotRequired[FixedBudgetScheduleOutputTypeDef]

class BudgetSummaryTypeDef(TypedDict):
    budgetId: str
    usageTrackingResource: UsageTrackingResourceTypeDef
    status: BudgetStatusType
    displayName: str
    approximateDollarLimit: float
    usages: ConsumedUsagesTypeDef
    createdBy: str
    createdAt: datetime
    description: NotRequired[str]
    updatedBy: NotRequired[str]
    updatedAt: NotRequired[datetime]

class CopyJobTemplateRequestTypeDef(TypedDict):
    farmId: str
    jobId: str
    queueId: str
    targetS3Location: S3LocationTypeDef

class UpdateWorkerResponseTypeDef(TypedDict):
    log: LogConfigurationTypeDef
    hostConfiguration: HostConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JobSearchSummaryTypeDef(TypedDict):
    jobId: NotRequired[str]
    queueId: NotRequired[str]
    name: NotRequired[str]
    lifecycleStatus: NotRequired[JobLifecycleStatusType]
    lifecycleStatusMessage: NotRequired[str]
    taskRunStatus: NotRequired[TaskRunStatusType]
    targetTaskRunStatus: NotRequired[JobTargetTaskRunStatusType]
    taskRunStatusCounts: NotRequired[Dict[TaskRunStatusType, int]]
    taskFailureRetryCount: NotRequired[int]
    priority: NotRequired[int]
    maxFailedTasksCount: NotRequired[int]
    maxRetriesPerTask: NotRequired[int]
    createdBy: NotRequired[str]
    createdAt: NotRequired[datetime]
    endedAt: NotRequired[datetime]
    startedAt: NotRequired[datetime]
    updatedAt: NotRequired[datetime]
    updatedBy: NotRequired[str]
    jobParameters: NotRequired[Dict[str, JobParameterTypeDef]]
    maxWorkerCount: NotRequired[int]
    sourceJobId: NotRequired[str]

class CreateStorageProfileRequestTypeDef(TypedDict):
    farmId: str
    displayName: str
    osFamily: StorageProfileOperatingSystemFamilyType
    clientToken: NotRequired[str]
    fileSystemLocations: NotRequired[Sequence[FileSystemLocationTypeDef]]

class GetStorageProfileForQueueResponseTypeDef(TypedDict):
    storageProfileId: str
    displayName: str
    osFamily: StorageProfileOperatingSystemFamilyType
    fileSystemLocations: List[FileSystemLocationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetStorageProfileResponseTypeDef(TypedDict):
    storageProfileId: str
    displayName: str
    osFamily: StorageProfileOperatingSystemFamilyType
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    fileSystemLocations: List[FileSystemLocationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStorageProfileRequestTypeDef(TypedDict):
    farmId: str
    storageProfileId: str
    clientToken: NotRequired[str]
    displayName: NotRequired[str]
    osFamily: NotRequired[StorageProfileOperatingSystemFamilyType]
    fileSystemLocationsToAdd: NotRequired[Sequence[FileSystemLocationTypeDef]]
    fileSystemLocationsToRemove: NotRequired[Sequence[FileSystemLocationTypeDef]]

class FleetCapabilitiesTypeDef(TypedDict):
    amounts: NotRequired[List[FleetAmountCapabilityTypeDef]]
    attributes: NotRequired[List[FleetAttributeCapabilityOutputTypeDef]]

class CustomerManagedWorkerCapabilitiesOutputTypeDef(TypedDict):
    vCpuCount: VCpuCountRangeTypeDef
    memoryMiB: MemoryMiBRangeTypeDef
    osFamily: CustomerManagedFleetOperatingSystemFamilyType
    cpuArchitectureType: CpuArchitectureTypeType
    acceleratorTypes: NotRequired[List[Literal["gpu"]]]
    acceleratorCount: NotRequired[AcceleratorCountRangeTypeDef]
    acceleratorTotalMemoryMiB: NotRequired[AcceleratorTotalMemoryMiBRangeTypeDef]
    customAmounts: NotRequired[List[FleetAmountCapabilityTypeDef]]
    customAttributes: NotRequired[List[FleetAttributeCapabilityOutputTypeDef]]

class CustomerManagedWorkerCapabilitiesTypeDef(TypedDict):
    vCpuCount: VCpuCountRangeTypeDef
    memoryMiB: MemoryMiBRangeTypeDef
    osFamily: CustomerManagedFleetOperatingSystemFamilyType
    cpuArchitectureType: CpuArchitectureTypeType
    acceleratorTypes: NotRequired[Sequence[Literal["gpu"]]]
    acceleratorCount: NotRequired[AcceleratorCountRangeTypeDef]
    acceleratorTotalMemoryMiB: NotRequired[AcceleratorTotalMemoryMiBRangeTypeDef]
    customAmounts: NotRequired[Sequence[FleetAmountCapabilityTypeDef]]
    customAttributes: NotRequired[Sequence[FleetAttributeCapabilityTypeDef]]

DateTimeFilterExpressionTypeDef = TypedDict(
    "DateTimeFilterExpressionTypeDef",
    {
        "name": str,
        "operator": ComparisonOperatorType,
        "dateTime": TimestampTypeDef,
    },
)

class FixedBudgetScheduleTypeDef(TypedDict):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef

class StepSummaryTypeDef(TypedDict):
    stepId: str
    name: str
    lifecycleStatus: StepLifecycleStatusType
    taskRunStatus: TaskRunStatusType
    taskRunStatusCounts: Dict[TaskRunStatusType, int]
    createdAt: datetime
    createdBy: str
    lifecycleStatusMessage: NotRequired[str]
    taskFailureRetryCount: NotRequired[int]
    targetTaskRunStatus: NotRequired[StepTargetTaskRunStatusType]
    updatedAt: NotRequired[datetime]
    updatedBy: NotRequired[str]
    startedAt: NotRequired[datetime]
    endedAt: NotRequired[datetime]
    dependencyCounts: NotRequired[DependencyCountsTypeDef]

class ListFarmMembersResponseTypeDef(TypedDict):
    members: List[FarmMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListFarmsResponseTypeDef(TypedDict):
    farms: List[FarmSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListFleetMembersResponseTypeDef(TypedDict):
    members: List[FleetMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetFleetRequestWaitTypeDef(TypedDict):
    farmId: str
    fleetId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetJobRequestWaitTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetLicenseEndpointRequestWaitExtraTypeDef(TypedDict):
    licenseEndpointId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetLicenseEndpointRequestWaitTypeDef(TypedDict):
    licenseEndpointId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetQueueFleetAssociationRequestWaitTypeDef(TypedDict):
    farmId: str
    queueId: str
    fleetId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetQueueLimitAssociationRequestWaitTypeDef(TypedDict):
    farmId: str
    queueId: str
    limitId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetQueueRequestWaitExtraTypeDef(TypedDict):
    farmId: str
    queueId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetQueueRequestWaitTypeDef(TypedDict):
    farmId: str
    queueId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetJobEntityErrorTypeDef(TypedDict):
    jobDetails: NotRequired[JobDetailsErrorTypeDef]
    jobAttachmentDetails: NotRequired[JobAttachmentDetailsErrorTypeDef]
    stepDetails: NotRequired[StepDetailsErrorTypeDef]
    environmentDetails: NotRequired[EnvironmentDetailsErrorTypeDef]

class GetSessionsStatisticsAggregationRequestPaginateTypeDef(TypedDict):
    farmId: str
    aggregationId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAvailableMeteredProductsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBudgetsRequestPaginateTypeDef(TypedDict):
    farmId: str
    status: NotRequired[BudgetStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFarmMembersRequestPaginateTypeDef(TypedDict):
    farmId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFarmsRequestPaginateTypeDef(TypedDict):
    principalId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFleetMembersRequestPaginateTypeDef(TypedDict):
    farmId: str
    fleetId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFleetsRequestPaginateTypeDef(TypedDict):
    farmId: str
    principalId: NotRequired[str]
    displayName: NotRequired[str]
    status: NotRequired[FleetStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListJobMembersRequestPaginateTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListJobParameterDefinitionsRequestPaginateTypeDef(TypedDict):
    farmId: str
    jobId: str
    queueId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListJobsRequestPaginateTypeDef(TypedDict):
    farmId: str
    queueId: str
    principalId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLicenseEndpointsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLimitsRequestPaginateTypeDef(TypedDict):
    farmId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMeteredProductsRequestPaginateTypeDef(TypedDict):
    licenseEndpointId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMonitorsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQueueEnvironmentsRequestPaginateTypeDef(TypedDict):
    farmId: str
    queueId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQueueFleetAssociationsRequestPaginateTypeDef(TypedDict):
    farmId: str
    queueId: NotRequired[str]
    fleetId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQueueLimitAssociationsRequestPaginateTypeDef(TypedDict):
    farmId: str
    queueId: NotRequired[str]
    limitId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQueueMembersRequestPaginateTypeDef(TypedDict):
    farmId: str
    queueId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQueuesRequestPaginateTypeDef(TypedDict):
    farmId: str
    principalId: NotRequired[str]
    status: NotRequired[QueueStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSessionActionsRequestPaginateTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    sessionId: NotRequired[str]
    taskId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSessionsForWorkerRequestPaginateTypeDef(TypedDict):
    farmId: str
    fleetId: str
    workerId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSessionsRequestPaginateTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStepConsumersRequestPaginateTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStepDependenciesRequestPaginateTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStepsRequestPaginateTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStorageProfilesForQueueRequestPaginateTypeDef(TypedDict):
    farmId: str
    queueId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStorageProfilesRequestPaginateTypeDef(TypedDict):
    farmId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTasksRequestPaginateTypeDef(TypedDict):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkersRequestPaginateTypeDef(TypedDict):
    farmId: str
    fleetId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class HostPropertiesResponseTypeDef(TypedDict):
    ipAddresses: NotRequired[IpAddressesOutputTypeDef]
    hostName: NotRequired[str]
    ec2InstanceArn: NotRequired[str]
    ec2InstanceType: NotRequired[str]

IpAddressesUnionTypeDef = Union[IpAddressesTypeDef, IpAddressesOutputTypeDef]

class JobEntityIdentifiersUnionTypeDef(TypedDict):
    jobDetails: NotRequired[JobDetailsIdentifiersTypeDef]
    jobAttachmentDetails: NotRequired[JobAttachmentDetailsIdentifiersTypeDef]
    stepDetails: NotRequired[StepDetailsIdentifiersTypeDef]
    environmentDetails: NotRequired[EnvironmentDetailsIdentifiersTypeDef]

class ListJobMembersResponseTypeDef(TypedDict):
    members: List[JobMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class JobRunAsUserTypeDef(TypedDict):
    runAs: RunAsType
    posix: NotRequired[PosixUserTypeDef]
    windows: NotRequired[WindowsUserTypeDef]

class ListJobsResponseTypeDef(TypedDict):
    jobs: List[JobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListLicenseEndpointsResponseTypeDef(TypedDict):
    licenseEndpoints: List[LicenseEndpointSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListLimitsResponseTypeDef(TypedDict):
    limits: List[LimitSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAvailableMeteredProductsResponseTypeDef(TypedDict):
    meteredProducts: List[MeteredProductSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListMeteredProductsResponseTypeDef(TypedDict):
    meteredProducts: List[MeteredProductSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListMonitorsResponseTypeDef(TypedDict):
    monitors: List[MonitorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListQueueEnvironmentsResponseTypeDef(TypedDict):
    environments: List[QueueEnvironmentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListQueueFleetAssociationsResponseTypeDef(TypedDict):
    queueFleetAssociations: List[QueueFleetAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListQueueLimitAssociationsResponseTypeDef(TypedDict):
    queueLimitAssociations: List[QueueLimitAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListQueueMembersResponseTypeDef(TypedDict):
    members: List[QueueMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListQueuesResponseTypeDef(TypedDict):
    queues: List[QueueSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSessionsForWorkerResponseTypeDef(TypedDict):
    sessions: List[WorkerSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSessionsResponseTypeDef(TypedDict):
    sessions: List[SessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListStepConsumersResponseTypeDef(TypedDict):
    consumers: List[StepConsumerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListStepDependenciesResponseTypeDef(TypedDict):
    dependencies: List[StepDependencyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListStorageProfilesForQueueResponseTypeDef(TypedDict):
    storageProfiles: List[StorageProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListStorageProfilesResponseTypeDef(TypedDict):
    storageProfiles: List[StorageProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ParameterSpaceTypeDef(TypedDict):
    parameters: List[StepParameterTypeDef]
    combination: NotRequired[str]

class SearchSortExpressionTypeDef(TypedDict):
    userJobsFirst: NotRequired[UserJobsFirstTypeDef]
    fieldSort: NotRequired[FieldSortExpressionTypeDef]
    parameterSort: NotRequired[ParameterSortExpressionTypeDef]

class StartSessionsStatisticsAggregationRequestTypeDef(TypedDict):
    farmId: str
    resourceIds: SessionsStatisticsResourcesTypeDef
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    groupBy: Sequence[UsageGroupByFieldType]
    statistics: Sequence[UsageStatisticType]
    timezone: NotRequired[str]
    period: NotRequired[PeriodType]

class StatisticsTypeDef(TypedDict):
    count: int
    costInUsd: StatsTypeDef
    runtimeInSeconds: StatsTypeDef
    queueId: NotRequired[str]
    fleetId: NotRequired[str]
    jobId: NotRequired[str]
    jobName: NotRequired[str]
    userId: NotRequired[str]
    usageType: NotRequired[UsageTypeType]
    licenseProduct: NotRequired[str]
    instanceType: NotRequired[str]
    aggregationStartTime: NotRequired[datetime]
    aggregationEndTime: NotRequired[datetime]

class StepRequiredCapabilitiesTypeDef(TypedDict):
    attributes: List[StepAttributeCapabilityTypeDef]
    amounts: List[StepAmountCapabilityTypeDef]

class UpdatedSessionActionInfoTypeDef(TypedDict):
    completedStatus: NotRequired[CompletedStatusType]
    processExitCode: NotRequired[int]
    progressMessage: NotRequired[str]
    startedAt: NotRequired[TimestampTypeDef]
    endedAt: NotRequired[TimestampTypeDef]
    updatedAt: NotRequired[TimestampTypeDef]
    progressPercent: NotRequired[float]
    manifests: NotRequired[Sequence[TaskRunManifestPropertiesRequestTypeDef]]

class WorkerCapabilitiesTypeDef(TypedDict):
    amounts: Sequence[WorkerAmountCapabilityTypeDef]
    attributes: Sequence[WorkerAttributeCapabilityTypeDef]

class ServiceManagedEc2InstanceCapabilitiesOutputTypeDef(TypedDict):
    vCpuCount: VCpuCountRangeTypeDef
    memoryMiB: MemoryMiBRangeTypeDef
    osFamily: ServiceManagedFleetOperatingSystemFamilyType
    cpuArchitectureType: CpuArchitectureTypeType
    rootEbsVolume: NotRequired[Ec2EbsVolumeTypeDef]
    acceleratorCapabilities: NotRequired[AcceleratorCapabilitiesOutputTypeDef]
    allowedInstanceTypes: NotRequired[List[str]]
    excludedInstanceTypes: NotRequired[List[str]]
    customAmounts: NotRequired[List[FleetAmountCapabilityTypeDef]]
    customAttributes: NotRequired[List[FleetAttributeCapabilityOutputTypeDef]]

class ServiceManagedEc2InstanceCapabilitiesTypeDef(TypedDict):
    vCpuCount: VCpuCountRangeTypeDef
    memoryMiB: MemoryMiBRangeTypeDef
    osFamily: ServiceManagedFleetOperatingSystemFamilyType
    cpuArchitectureType: CpuArchitectureTypeType
    rootEbsVolume: NotRequired[Ec2EbsVolumeTypeDef]
    acceleratorCapabilities: NotRequired[AcceleratorCapabilitiesTypeDef]
    allowedInstanceTypes: NotRequired[Sequence[str]]
    excludedInstanceTypes: NotRequired[Sequence[str]]
    customAmounts: NotRequired[Sequence[FleetAmountCapabilityTypeDef]]
    customAttributes: NotRequired[Sequence[FleetAttributeCapabilityTypeDef]]

class AssignedSessionActionDefinitionTypeDef(TypedDict):
    envEnter: NotRequired[AssignedEnvironmentEnterSessionActionDefinitionTypeDef]
    envExit: NotRequired[AssignedEnvironmentExitSessionActionDefinitionTypeDef]
    taskRun: NotRequired[AssignedTaskRunSessionActionDefinitionTypeDef]
    syncInputJobAttachments: NotRequired[
        AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef
    ]

class SessionActionDefinitionSummaryTypeDef(TypedDict):
    envEnter: NotRequired[EnvironmentEnterSessionActionDefinitionSummaryTypeDef]
    envExit: NotRequired[EnvironmentExitSessionActionDefinitionSummaryTypeDef]
    taskRun: NotRequired[TaskRunSessionActionDefinitionSummaryTypeDef]
    syncInputJobAttachments: NotRequired[
        SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef
    ]

class SessionActionDefinitionTypeDef(TypedDict):
    envEnter: NotRequired[EnvironmentEnterSessionActionDefinitionTypeDef]
    envExit: NotRequired[EnvironmentExitSessionActionDefinitionTypeDef]
    taskRun: NotRequired[TaskRunSessionActionDefinitionTypeDef]
    syncInputJobAttachments: NotRequired[SyncInputJobAttachmentsSessionActionDefinitionTypeDef]

class SearchTasksResponseTypeDef(TypedDict):
    tasks: List[TaskSearchSummaryTypeDef]
    nextItemOffset: int
    totalResults: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListTasksResponseTypeDef(TypedDict):
    tasks: List[TaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetJobResponseTypeDef(TypedDict):
    jobId: str
    name: str
    lifecycleStatus: JobLifecycleStatusType
    lifecycleStatusMessage: str
    priority: int
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    startedAt: datetime
    endedAt: datetime
    taskRunStatus: TaskRunStatusType
    targetTaskRunStatus: JobTargetTaskRunStatusType
    taskRunStatusCounts: Dict[TaskRunStatusType, int]
    taskFailureRetryCount: int
    storageProfileId: str
    maxFailedTasksCount: int
    maxRetriesPerTask: int
    parameters: Dict[str, JobParameterTypeDef]
    attachments: AttachmentsOutputTypeDef
    description: str
    maxWorkerCount: int
    sourceJobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class JobAttachmentDetailsEntityTypeDef(TypedDict):
    jobId: str
    attachments: AttachmentsOutputTypeDef

AttachmentsUnionTypeDef = Union[AttachmentsTypeDef, AttachmentsOutputTypeDef]

class GetBudgetResponseTypeDef(TypedDict):
    budgetId: str
    usageTrackingResource: UsageTrackingResourceTypeDef
    status: BudgetStatusType
    displayName: str
    description: str
    approximateDollarLimit: float
    usages: ConsumedUsagesTypeDef
    actions: List[ResponseBudgetActionTypeDef]
    schedule: BudgetScheduleOutputTypeDef
    createdBy: str
    createdAt: datetime
    updatedBy: str
    updatedAt: datetime
    queueStoppedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListBudgetsResponseTypeDef(TypedDict):
    budgets: List[BudgetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SearchJobsResponseTypeDef(TypedDict):
    jobs: List[JobSearchSummaryTypeDef]
    nextItemOffset: int
    totalResults: int
    ResponseMetadata: ResponseMetadataTypeDef

class CustomerManagedFleetConfigurationOutputTypeDef(TypedDict):
    mode: AutoScalingModeType
    workerCapabilities: CustomerManagedWorkerCapabilitiesOutputTypeDef
    storageProfileId: NotRequired[str]
    tagPropagationMode: NotRequired[TagPropagationModeType]

class CustomerManagedFleetConfigurationTypeDef(TypedDict):
    mode: AutoScalingModeType
    workerCapabilities: CustomerManagedWorkerCapabilitiesTypeDef
    storageProfileId: NotRequired[str]
    tagPropagationMode: NotRequired[TagPropagationModeType]

class SearchFilterExpressionTypeDef(TypedDict):
    dateTimeFilter: NotRequired[DateTimeFilterExpressionTypeDef]
    parameterFilter: NotRequired[ParameterFilterExpressionTypeDef]
    searchTermFilter: NotRequired[SearchTermFilterExpressionTypeDef]
    stringFilter: NotRequired[StringFilterExpressionTypeDef]
    groupFilter: NotRequired[Mapping[str, Any]]

class BudgetScheduleTypeDef(TypedDict):
    fixed: NotRequired[FixedBudgetScheduleTypeDef]

class ListStepsResponseTypeDef(TypedDict):
    steps: List[StepSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetSessionResponseTypeDef(TypedDict):
    sessionId: str
    fleetId: str
    workerId: str
    startedAt: datetime
    log: LogConfigurationTypeDef
    lifecycleStatus: SessionLifecycleStatusType
    endedAt: datetime
    updatedAt: datetime
    updatedBy: str
    targetLifecycleStatus: Literal["ENDED"]
    hostProperties: HostPropertiesResponseTypeDef
    workerLog: LogConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkerResponseTypeDef(TypedDict):
    farmId: str
    fleetId: str
    workerId: str
    hostProperties: HostPropertiesResponseTypeDef
    status: WorkerStatusType
    log: LogConfigurationTypeDef
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class WorkerSearchSummaryTypeDef(TypedDict):
    fleetId: NotRequired[str]
    workerId: NotRequired[str]
    status: NotRequired[WorkerStatusType]
    hostProperties: NotRequired[HostPropertiesResponseTypeDef]
    createdBy: NotRequired[str]
    createdAt: NotRequired[datetime]
    updatedBy: NotRequired[str]
    updatedAt: NotRequired[datetime]

class WorkerSummaryTypeDef(TypedDict):
    workerId: str
    farmId: str
    fleetId: str
    status: WorkerStatusType
    createdAt: datetime
    createdBy: str
    hostProperties: NotRequired[HostPropertiesResponseTypeDef]
    log: NotRequired[LogConfigurationTypeDef]
    updatedAt: NotRequired[datetime]
    updatedBy: NotRequired[str]

class HostPropertiesRequestTypeDef(TypedDict):
    ipAddresses: NotRequired[IpAddressesUnionTypeDef]
    hostName: NotRequired[str]

class BatchGetJobEntityRequestTypeDef(TypedDict):
    farmId: str
    fleetId: str
    workerId: str
    identifiers: Sequence[JobEntityIdentifiersUnionTypeDef]

class CreateQueueRequestTypeDef(TypedDict):
    farmId: str
    displayName: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    defaultBudgetAction: NotRequired[DefaultQueueBudgetActionType]
    jobAttachmentSettings: NotRequired[JobAttachmentSettingsTypeDef]
    roleArn: NotRequired[str]
    jobRunAsUser: NotRequired[JobRunAsUserTypeDef]
    requiredFileSystemLocationNames: NotRequired[Sequence[str]]
    allowedStorageProfileIds: NotRequired[Sequence[str]]
    tags: NotRequired[Mapping[str, str]]

class GetQueueResponseTypeDef(TypedDict):
    queueId: str
    displayName: str
    description: str
    farmId: str
    status: QueueStatusType
    defaultBudgetAction: DefaultQueueBudgetActionType
    blockedReason: QueueBlockedReasonType
    jobAttachmentSettings: JobAttachmentSettingsTypeDef
    roleArn: str
    requiredFileSystemLocationNames: List[str]
    allowedStorageProfileIds: List[str]
    jobRunAsUser: JobRunAsUserTypeDef
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class JobDetailsEntityTypeDef(TypedDict):
    jobId: str
    logGroupName: str
    schemaVersion: str
    jobAttachmentSettings: NotRequired[JobAttachmentSettingsTypeDef]
    jobRunAsUser: NotRequired[JobRunAsUserTypeDef]
    queueRoleArn: NotRequired[str]
    parameters: NotRequired[Dict[str, JobParameterTypeDef]]
    pathMappingRules: NotRequired[List[PathMappingRuleTypeDef]]

class UpdateQueueRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    clientToken: NotRequired[str]
    displayName: NotRequired[str]
    description: NotRequired[str]
    defaultBudgetAction: NotRequired[DefaultQueueBudgetActionType]
    jobAttachmentSettings: NotRequired[JobAttachmentSettingsTypeDef]
    roleArn: NotRequired[str]
    jobRunAsUser: NotRequired[JobRunAsUserTypeDef]
    requiredFileSystemLocationNamesToAdd: NotRequired[Sequence[str]]
    requiredFileSystemLocationNamesToRemove: NotRequired[Sequence[str]]
    allowedStorageProfileIdsToAdd: NotRequired[Sequence[str]]
    allowedStorageProfileIdsToRemove: NotRequired[Sequence[str]]

class StepSearchSummaryTypeDef(TypedDict):
    stepId: NotRequired[str]
    jobId: NotRequired[str]
    queueId: NotRequired[str]
    name: NotRequired[str]
    lifecycleStatus: NotRequired[StepLifecycleStatusType]
    lifecycleStatusMessage: NotRequired[str]
    taskRunStatus: NotRequired[TaskRunStatusType]
    targetTaskRunStatus: NotRequired[StepTargetTaskRunStatusType]
    taskRunStatusCounts: NotRequired[Dict[TaskRunStatusType, int]]
    taskFailureRetryCount: NotRequired[int]
    createdAt: NotRequired[datetime]
    createdBy: NotRequired[str]
    startedAt: NotRequired[datetime]
    endedAt: NotRequired[datetime]
    updatedAt: NotRequired[datetime]
    updatedBy: NotRequired[str]
    parameterSpace: NotRequired[ParameterSpaceTypeDef]

class GetSessionsStatisticsAggregationResponseTypeDef(TypedDict):
    statistics: List[StatisticsTypeDef]
    status: SessionsStatisticsAggregationStatusType
    statusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetStepResponseTypeDef(TypedDict):
    stepId: str
    name: str
    lifecycleStatus: StepLifecycleStatusType
    lifecycleStatusMessage: str
    taskRunStatus: TaskRunStatusType
    taskRunStatusCounts: Dict[TaskRunStatusType, int]
    taskFailureRetryCount: int
    targetTaskRunStatus: StepTargetTaskRunStatusType
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    startedAt: datetime
    endedAt: datetime
    dependencyCounts: DependencyCountsTypeDef
    requiredCapabilities: StepRequiredCapabilitiesTypeDef
    parameterSpace: ParameterSpaceTypeDef
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkerScheduleRequestTypeDef(TypedDict):
    farmId: str
    fleetId: str
    workerId: str
    updatedSessionActions: NotRequired[Mapping[str, UpdatedSessionActionInfoTypeDef]]

class ServiceManagedEc2FleetConfigurationOutputTypeDef(TypedDict):
    instanceCapabilities: ServiceManagedEc2InstanceCapabilitiesOutputTypeDef
    instanceMarketOptions: ServiceManagedEc2InstanceMarketOptionsTypeDef
    vpcConfiguration: NotRequired[VpcConfigurationOutputTypeDef]
    storageProfileId: NotRequired[str]

class ServiceManagedEc2FleetConfigurationTypeDef(TypedDict):
    instanceCapabilities: ServiceManagedEc2InstanceCapabilitiesTypeDef
    instanceMarketOptions: ServiceManagedEc2InstanceMarketOptionsTypeDef
    vpcConfiguration: NotRequired[VpcConfigurationTypeDef]
    storageProfileId: NotRequired[str]

class AssignedSessionActionTypeDef(TypedDict):
    sessionActionId: str
    definition: AssignedSessionActionDefinitionTypeDef

class SessionActionSummaryTypeDef(TypedDict):
    sessionActionId: str
    status: SessionActionStatusType
    definition: SessionActionDefinitionSummaryTypeDef
    startedAt: NotRequired[datetime]
    endedAt: NotRequired[datetime]
    workerUpdatedAt: NotRequired[datetime]
    progressPercent: NotRequired[float]
    manifests: NotRequired[List[TaskRunManifestPropertiesResponseTypeDef]]

class GetSessionActionResponseTypeDef(TypedDict):
    sessionActionId: str
    status: SessionActionStatusType
    startedAt: datetime
    endedAt: datetime
    workerUpdatedAt: datetime
    progressPercent: float
    sessionId: str
    processExitCode: int
    progressMessage: str
    definition: SessionActionDefinitionTypeDef
    acquiredLimits: List[AcquiredLimitTypeDef]
    manifests: List[TaskRunManifestPropertiesResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobRequestTypeDef(TypedDict):
    farmId: str
    queueId: str
    priority: int
    clientToken: NotRequired[str]
    template: NotRequired[str]
    templateType: NotRequired[JobTemplateTypeType]
    parameters: NotRequired[Mapping[str, JobParameterTypeDef]]
    attachments: NotRequired[AttachmentsUnionTypeDef]
    storageProfileId: NotRequired[str]
    targetTaskRunStatus: NotRequired[CreateJobTargetTaskRunStatusType]
    maxFailedTasksCount: NotRequired[int]
    maxRetriesPerTask: NotRequired[int]
    maxWorkerCount: NotRequired[int]
    sourceJobId: NotRequired[str]

SearchGroupedFilterExpressionsTypeDef = TypedDict(
    "SearchGroupedFilterExpressionsTypeDef",
    {
        "filters": Sequence[SearchFilterExpressionTypeDef],
        "operator": LogicalOperatorType,
    },
)
BudgetScheduleUnionTypeDef = Union[BudgetScheduleTypeDef, BudgetScheduleOutputTypeDef]

class SearchWorkersResponseTypeDef(TypedDict):
    workers: List[WorkerSearchSummaryTypeDef]
    nextItemOffset: int
    totalResults: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkersResponseTypeDef(TypedDict):
    workers: List[WorkerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateWorkerRequestTypeDef(TypedDict):
    farmId: str
    fleetId: str
    hostProperties: NotRequired[HostPropertiesRequestTypeDef]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateWorkerRequestTypeDef(TypedDict):
    farmId: str
    fleetId: str
    workerId: str
    status: NotRequired[UpdatedWorkerStatusType]
    capabilities: NotRequired[WorkerCapabilitiesTypeDef]
    hostProperties: NotRequired[HostPropertiesRequestTypeDef]

class JobEntityTypeDef(TypedDict):
    jobDetails: NotRequired[JobDetailsEntityTypeDef]
    jobAttachmentDetails: NotRequired[JobAttachmentDetailsEntityTypeDef]
    stepDetails: NotRequired[StepDetailsEntityTypeDef]
    environmentDetails: NotRequired[EnvironmentDetailsEntityTypeDef]

class SearchStepsResponseTypeDef(TypedDict):
    steps: List[StepSearchSummaryTypeDef]
    nextItemOffset: int
    totalResults: int
    ResponseMetadata: ResponseMetadataTypeDef

class FleetConfigurationOutputTypeDef(TypedDict):
    customerManaged: NotRequired[CustomerManagedFleetConfigurationOutputTypeDef]
    serviceManagedEc2: NotRequired[ServiceManagedEc2FleetConfigurationOutputTypeDef]

class FleetConfigurationTypeDef(TypedDict):
    customerManaged: NotRequired[CustomerManagedFleetConfigurationTypeDef]
    serviceManagedEc2: NotRequired[ServiceManagedEc2FleetConfigurationTypeDef]

class AssignedSessionTypeDef(TypedDict):
    queueId: str
    jobId: str
    sessionActions: List[AssignedSessionActionTypeDef]
    logConfiguration: LogConfigurationTypeDef

class ListSessionActionsResponseTypeDef(TypedDict):
    sessionActions: List[SessionActionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SearchJobsRequestTypeDef(TypedDict):
    farmId: str
    queueIds: Sequence[str]
    itemOffset: int
    filterExpressions: NotRequired[SearchGroupedFilterExpressionsTypeDef]
    sortExpressions: NotRequired[Sequence[SearchSortExpressionTypeDef]]
    pageSize: NotRequired[int]

class SearchStepsRequestTypeDef(TypedDict):
    farmId: str
    queueIds: Sequence[str]
    itemOffset: int
    jobId: NotRequired[str]
    filterExpressions: NotRequired[SearchGroupedFilterExpressionsTypeDef]
    sortExpressions: NotRequired[Sequence[SearchSortExpressionTypeDef]]
    pageSize: NotRequired[int]

class SearchTasksRequestTypeDef(TypedDict):
    farmId: str
    queueIds: Sequence[str]
    itemOffset: int
    jobId: NotRequired[str]
    filterExpressions: NotRequired[SearchGroupedFilterExpressionsTypeDef]
    sortExpressions: NotRequired[Sequence[SearchSortExpressionTypeDef]]
    pageSize: NotRequired[int]

class SearchWorkersRequestTypeDef(TypedDict):
    farmId: str
    fleetIds: Sequence[str]
    itemOffset: int
    filterExpressions: NotRequired[SearchGroupedFilterExpressionsTypeDef]
    sortExpressions: NotRequired[Sequence[SearchSortExpressionTypeDef]]
    pageSize: NotRequired[int]

class CreateBudgetRequestTypeDef(TypedDict):
    farmId: str
    usageTrackingResource: UsageTrackingResourceTypeDef
    displayName: str
    approximateDollarLimit: float
    actions: Sequence[BudgetActionToAddTypeDef]
    schedule: BudgetScheduleUnionTypeDef
    clientToken: NotRequired[str]
    description: NotRequired[str]

class UpdateBudgetRequestTypeDef(TypedDict):
    farmId: str
    budgetId: str
    clientToken: NotRequired[str]
    displayName: NotRequired[str]
    description: NotRequired[str]
    status: NotRequired[BudgetStatusType]
    approximateDollarLimit: NotRequired[float]
    actionsToAdd: NotRequired[Sequence[BudgetActionToAddTypeDef]]
    actionsToRemove: NotRequired[Sequence[BudgetActionToRemoveTypeDef]]
    schedule: NotRequired[BudgetScheduleUnionTypeDef]

class BatchGetJobEntityResponseTypeDef(TypedDict):
    entities: List[JobEntityTypeDef]
    errors: List[GetJobEntityErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FleetSummaryTypeDef(TypedDict):
    fleetId: str
    farmId: str
    displayName: str
    status: FleetStatusType
    workerCount: int
    minWorkerCount: int
    maxWorkerCount: int
    configuration: FleetConfigurationOutputTypeDef
    createdAt: datetime
    createdBy: str
    statusMessage: NotRequired[str]
    autoScalingStatus: NotRequired[AutoScalingStatusType]
    targetWorkerCount: NotRequired[int]
    updatedAt: NotRequired[datetime]
    updatedBy: NotRequired[str]

class GetFleetResponseTypeDef(TypedDict):
    fleetId: str
    farmId: str
    displayName: str
    description: str
    status: FleetStatusType
    statusMessage: str
    autoScalingStatus: AutoScalingStatusType
    targetWorkerCount: int
    workerCount: int
    minWorkerCount: int
    maxWorkerCount: int
    configuration: FleetConfigurationOutputTypeDef
    hostConfiguration: HostConfigurationTypeDef
    capabilities: FleetCapabilitiesTypeDef
    roleArn: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

FleetConfigurationUnionTypeDef = Union[FleetConfigurationTypeDef, FleetConfigurationOutputTypeDef]

class UpdateWorkerScheduleResponseTypeDef(TypedDict):
    assignedSessions: Dict[str, AssignedSessionTypeDef]
    cancelSessionActions: Dict[str, List[str]]
    desiredWorkerStatus: Literal["STOPPED"]
    updateIntervalSeconds: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListFleetsResponseTypeDef(TypedDict):
    fleets: List[FleetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateFleetRequestTypeDef(TypedDict):
    farmId: str
    displayName: str
    roleArn: str
    maxWorkerCount: int
    configuration: FleetConfigurationUnionTypeDef
    clientToken: NotRequired[str]
    description: NotRequired[str]
    minWorkerCount: NotRequired[int]
    tags: NotRequired[Mapping[str, str]]
    hostConfiguration: NotRequired[HostConfigurationTypeDef]

class UpdateFleetRequestTypeDef(TypedDict):
    farmId: str
    fleetId: str
    clientToken: NotRequired[str]
    displayName: NotRequired[str]
    description: NotRequired[str]
    roleArn: NotRequired[str]
    minWorkerCount: NotRequired[int]
    maxWorkerCount: NotRequired[int]
    configuration: NotRequired[FleetConfigurationUnionTypeDef]
    hostConfiguration: NotRequired[HostConfigurationTypeDef]
