"""
Type annotations for deadline service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/type_defs.html)

Usage::

    ```python
    from mypy_boto3_deadline.type_defs import AcceleratorCountRangeTypeDef

    data: AcceleratorCountRangeTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
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
    QueueStatusType,
    RunAsType,
    ServiceManagedFleetOperatingSystemFamilyType,
    SessionActionStatusType,
    SessionLifecycleStatusType,
    SessionsStatisticsAggregationStatusType,
    SortOrderType,
    StepLifecycleStatusType,
    StepParameterTypeType,
    StepTargetTaskRunStatusType,
    StorageProfileOperatingSystemFamilyType,
    TaskRunStatusType,
    TaskTargetRunStatusType,
    UpdatedWorkerStatusType,
    UpdateQueueFleetAssociationStatusType,
    UsageGroupByFieldType,
    UsageStatisticType,
    UsageTypeType,
    WorkerStatusType,
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
    "AcceleratorCountRangeTypeDef",
    "AcceleratorTotalMemoryMiBRangeTypeDef",
    "AssignedEnvironmentEnterSessionActionDefinitionTypeDef",
    "AssignedEnvironmentExitSessionActionDefinitionTypeDef",
    "AssignedSessionActionDefinitionTypeDef",
    "AssignedSessionActionTypeDef",
    "AssignedSessionTypeDef",
    "AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef",
    "AssignedTaskRunSessionActionDefinitionTypeDef",
    "AssociateMemberToFarmRequestRequestTypeDef",
    "AssociateMemberToFleetRequestRequestTypeDef",
    "AssociateMemberToJobRequestRequestTypeDef",
    "AssociateMemberToQueueRequestRequestTypeDef",
    "AssumeFleetRoleForReadRequestRequestTypeDef",
    "AssumeFleetRoleForReadResponseTypeDef",
    "AssumeFleetRoleForWorkerRequestRequestTypeDef",
    "AssumeFleetRoleForWorkerResponseTypeDef",
    "AssumeQueueRoleForReadRequestRequestTypeDef",
    "AssumeQueueRoleForReadResponseTypeDef",
    "AssumeQueueRoleForUserRequestRequestTypeDef",
    "AssumeQueueRoleForUserResponseTypeDef",
    "AssumeQueueRoleForWorkerRequestRequestTypeDef",
    "AssumeQueueRoleForWorkerResponseTypeDef",
    "AttachmentsTypeDef",
    "AwsCredentialsTypeDef",
    "BatchGetJobEntityRequestRequestTypeDef",
    "BatchGetJobEntityResponseTypeDef",
    "BudgetActionToAddTypeDef",
    "BudgetActionToRemoveTypeDef",
    "BudgetScheduleTypeDef",
    "BudgetSummaryTypeDef",
    "ConsumedUsagesTypeDef",
    "CopyJobTemplateRequestRequestTypeDef",
    "CopyJobTemplateResponseTypeDef",
    "CreateBudgetRequestRequestTypeDef",
    "CreateBudgetResponseTypeDef",
    "CreateFarmRequestRequestTypeDef",
    "CreateFarmResponseTypeDef",
    "CreateFleetRequestRequestTypeDef",
    "CreateFleetResponseTypeDef",
    "CreateJobRequestRequestTypeDef",
    "CreateJobResponseTypeDef",
    "CreateLicenseEndpointRequestRequestTypeDef",
    "CreateLicenseEndpointResponseTypeDef",
    "CreateMonitorRequestRequestTypeDef",
    "CreateMonitorResponseTypeDef",
    "CreateQueueEnvironmentRequestRequestTypeDef",
    "CreateQueueEnvironmentResponseTypeDef",
    "CreateQueueFleetAssociationRequestRequestTypeDef",
    "CreateQueueRequestRequestTypeDef",
    "CreateQueueResponseTypeDef",
    "CreateStorageProfileRequestRequestTypeDef",
    "CreateStorageProfileResponseTypeDef",
    "CreateWorkerRequestRequestTypeDef",
    "CreateWorkerResponseTypeDef",
    "CustomerManagedFleetConfigurationTypeDef",
    "CustomerManagedWorkerCapabilitiesTypeDef",
    "DateTimeFilterExpressionTypeDef",
    "DeleteBudgetRequestRequestTypeDef",
    "DeleteFarmRequestRequestTypeDef",
    "DeleteFleetRequestRequestTypeDef",
    "DeleteLicenseEndpointRequestRequestTypeDef",
    "DeleteMeteredProductRequestRequestTypeDef",
    "DeleteMonitorRequestRequestTypeDef",
    "DeleteQueueEnvironmentRequestRequestTypeDef",
    "DeleteQueueFleetAssociationRequestRequestTypeDef",
    "DeleteQueueRequestRequestTypeDef",
    "DeleteStorageProfileRequestRequestTypeDef",
    "DeleteWorkerRequestRequestTypeDef",
    "DependencyCountsTypeDef",
    "DisassociateMemberFromFarmRequestRequestTypeDef",
    "DisassociateMemberFromFleetRequestRequestTypeDef",
    "DisassociateMemberFromJobRequestRequestTypeDef",
    "DisassociateMemberFromQueueRequestRequestTypeDef",
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
    "FixedBudgetScheduleTypeDef",
    "FleetAmountCapabilityTypeDef",
    "FleetAttributeCapabilityTypeDef",
    "FleetCapabilitiesTypeDef",
    "FleetConfigurationTypeDef",
    "FleetMemberTypeDef",
    "FleetSummaryTypeDef",
    "GetBudgetRequestRequestTypeDef",
    "GetBudgetResponseTypeDef",
    "GetFarmRequestRequestTypeDef",
    "GetFarmResponseTypeDef",
    "GetFleetRequestRequestTypeDef",
    "GetFleetResponseTypeDef",
    "GetJobEntityErrorTypeDef",
    "GetJobRequestRequestTypeDef",
    "GetJobResponseTypeDef",
    "GetLicenseEndpointRequestRequestTypeDef",
    "GetLicenseEndpointResponseTypeDef",
    "GetMonitorRequestRequestTypeDef",
    "GetMonitorResponseTypeDef",
    "GetQueueEnvironmentRequestRequestTypeDef",
    "GetQueueEnvironmentResponseTypeDef",
    "GetQueueFleetAssociationRequestRequestTypeDef",
    "GetQueueFleetAssociationResponseTypeDef",
    "GetQueueRequestRequestTypeDef",
    "GetQueueResponseTypeDef",
    "GetSessionActionRequestRequestTypeDef",
    "GetSessionActionResponseTypeDef",
    "GetSessionRequestRequestTypeDef",
    "GetSessionResponseTypeDef",
    "GetSessionsStatisticsAggregationRequestRequestTypeDef",
    "GetSessionsStatisticsAggregationResponseTypeDef",
    "GetStepRequestRequestTypeDef",
    "GetStepResponseTypeDef",
    "GetStorageProfileForQueueRequestRequestTypeDef",
    "GetStorageProfileForQueueResponseTypeDef",
    "GetStorageProfileRequestRequestTypeDef",
    "GetStorageProfileResponseTypeDef",
    "GetTaskRequestRequestTypeDef",
    "GetTaskResponseTypeDef",
    "GetWorkerRequestRequestTypeDef",
    "GetWorkerResponseTypeDef",
    "HostPropertiesRequestTypeDef",
    "HostPropertiesResponseTypeDef",
    "IpAddressesTypeDef",
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
    "ListAvailableMeteredProductsRequestRequestTypeDef",
    "ListAvailableMeteredProductsResponseTypeDef",
    "ListBudgetsRequestRequestTypeDef",
    "ListBudgetsResponseTypeDef",
    "ListFarmMembersRequestRequestTypeDef",
    "ListFarmMembersResponseTypeDef",
    "ListFarmsRequestRequestTypeDef",
    "ListFarmsResponseTypeDef",
    "ListFleetMembersRequestRequestTypeDef",
    "ListFleetMembersResponseTypeDef",
    "ListFleetsRequestRequestTypeDef",
    "ListFleetsResponseTypeDef",
    "ListJobMembersRequestRequestTypeDef",
    "ListJobMembersResponseTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListJobsResponseTypeDef",
    "ListLicenseEndpointsRequestRequestTypeDef",
    "ListLicenseEndpointsResponseTypeDef",
    "ListMeteredProductsRequestRequestTypeDef",
    "ListMeteredProductsResponseTypeDef",
    "ListMonitorsRequestRequestTypeDef",
    "ListMonitorsResponseTypeDef",
    "ListQueueEnvironmentsRequestRequestTypeDef",
    "ListQueueEnvironmentsResponseTypeDef",
    "ListQueueFleetAssociationsRequestRequestTypeDef",
    "ListQueueFleetAssociationsResponseTypeDef",
    "ListQueueMembersRequestRequestTypeDef",
    "ListQueueMembersResponseTypeDef",
    "ListQueuesRequestRequestTypeDef",
    "ListQueuesResponseTypeDef",
    "ListSessionActionsRequestRequestTypeDef",
    "ListSessionActionsResponseTypeDef",
    "ListSessionsForWorkerRequestRequestTypeDef",
    "ListSessionsForWorkerResponseTypeDef",
    "ListSessionsRequestRequestTypeDef",
    "ListSessionsResponseTypeDef",
    "ListStepConsumersRequestRequestTypeDef",
    "ListStepConsumersResponseTypeDef",
    "ListStepDependenciesRequestRequestTypeDef",
    "ListStepDependenciesResponseTypeDef",
    "ListStepsRequestRequestTypeDef",
    "ListStepsResponseTypeDef",
    "ListStorageProfilesForQueueRequestRequestTypeDef",
    "ListStorageProfilesForQueueResponseTypeDef",
    "ListStorageProfilesRequestRequestTypeDef",
    "ListStorageProfilesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTasksRequestRequestTypeDef",
    "ListTasksResponseTypeDef",
    "ListWorkersRequestRequestTypeDef",
    "ListWorkersResponseTypeDef",
    "LogConfigurationTypeDef",
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
    "PutMeteredProductRequestRequestTypeDef",
    "QueueEnvironmentSummaryTypeDef",
    "QueueFleetAssociationSummaryTypeDef",
    "QueueMemberTypeDef",
    "QueueSummaryTypeDef",
    "ResponseBudgetActionTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "SearchFilterExpressionTypeDef",
    "SearchGroupedFilterExpressionsTypeDef",
    "SearchJobsRequestRequestTypeDef",
    "SearchJobsResponseTypeDef",
    "SearchSortExpressionTypeDef",
    "SearchStepsRequestRequestTypeDef",
    "SearchStepsResponseTypeDef",
    "SearchTasksRequestRequestTypeDef",
    "SearchTasksResponseTypeDef",
    "SearchTermFilterExpressionTypeDef",
    "SearchWorkersRequestRequestTypeDef",
    "SearchWorkersResponseTypeDef",
    "ServiceManagedEc2FleetConfigurationTypeDef",
    "ServiceManagedEc2InstanceCapabilitiesTypeDef",
    "ServiceManagedEc2InstanceMarketOptionsTypeDef",
    "SessionActionDefinitionSummaryTypeDef",
    "SessionActionDefinitionTypeDef",
    "SessionActionSummaryTypeDef",
    "SessionSummaryTypeDef",
    "SessionsStatisticsResourcesTypeDef",
    "StartSessionsStatisticsAggregationRequestRequestTypeDef",
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
    "TagResourceRequestRequestTypeDef",
    "TaskParameterValueTypeDef",
    "TaskRunSessionActionDefinitionSummaryTypeDef",
    "TaskRunSessionActionDefinitionTypeDef",
    "TaskSearchSummaryTypeDef",
    "TaskSummaryTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBudgetRequestRequestTypeDef",
    "UpdateFarmRequestRequestTypeDef",
    "UpdateFleetRequestRequestTypeDef",
    "UpdateJobRequestRequestTypeDef",
    "UpdateMonitorRequestRequestTypeDef",
    "UpdateQueueEnvironmentRequestRequestTypeDef",
    "UpdateQueueFleetAssociationRequestRequestTypeDef",
    "UpdateQueueRequestRequestTypeDef",
    "UpdateSessionRequestRequestTypeDef",
    "UpdateStepRequestRequestTypeDef",
    "UpdateStorageProfileRequestRequestTypeDef",
    "UpdateTaskRequestRequestTypeDef",
    "UpdateWorkerRequestRequestTypeDef",
    "UpdateWorkerResponseTypeDef",
    "UpdateWorkerScheduleRequestRequestTypeDef",
    "UpdateWorkerScheduleResponseTypeDef",
    "UpdatedSessionActionInfoTypeDef",
    "UsageTrackingResourceTypeDef",
    "UserJobsFirstTypeDef",
    "VCpuCountRangeTypeDef",
    "WaiterConfigTypeDef",
    "WindowsUserTypeDef",
    "WorkerAmountCapabilityTypeDef",
    "WorkerAttributeCapabilityTypeDef",
    "WorkerCapabilitiesTypeDef",
    "WorkerSearchSummaryTypeDef",
    "WorkerSessionSummaryTypeDef",
    "WorkerSummaryTypeDef",
)

_RequiredAcceleratorCountRangeTypeDef = TypedDict(
    "_RequiredAcceleratorCountRangeTypeDef",
    {
        "min": int,
    },
)
_OptionalAcceleratorCountRangeTypeDef = TypedDict(
    "_OptionalAcceleratorCountRangeTypeDef",
    {
        "max": int,
    },
    total=False,
)

class AcceleratorCountRangeTypeDef(
    _RequiredAcceleratorCountRangeTypeDef, _OptionalAcceleratorCountRangeTypeDef
):
    pass

_RequiredAcceleratorTotalMemoryMiBRangeTypeDef = TypedDict(
    "_RequiredAcceleratorTotalMemoryMiBRangeTypeDef",
    {
        "min": int,
    },
)
_OptionalAcceleratorTotalMemoryMiBRangeTypeDef = TypedDict(
    "_OptionalAcceleratorTotalMemoryMiBRangeTypeDef",
    {
        "max": int,
    },
    total=False,
)

class AcceleratorTotalMemoryMiBRangeTypeDef(
    _RequiredAcceleratorTotalMemoryMiBRangeTypeDef, _OptionalAcceleratorTotalMemoryMiBRangeTypeDef
):
    pass

AssignedEnvironmentEnterSessionActionDefinitionTypeDef = TypedDict(
    "AssignedEnvironmentEnterSessionActionDefinitionTypeDef",
    {
        "environmentId": str,
    },
)

AssignedEnvironmentExitSessionActionDefinitionTypeDef = TypedDict(
    "AssignedEnvironmentExitSessionActionDefinitionTypeDef",
    {
        "environmentId": str,
    },
)

AssignedSessionActionDefinitionTypeDef = TypedDict(
    "AssignedSessionActionDefinitionTypeDef",
    {
        "envEnter": "AssignedEnvironmentEnterSessionActionDefinitionTypeDef",
        "envExit": "AssignedEnvironmentExitSessionActionDefinitionTypeDef",
        "syncInputJobAttachments": "AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef",
        "taskRun": "AssignedTaskRunSessionActionDefinitionTypeDef",
    },
    total=False,
)

AssignedSessionActionTypeDef = TypedDict(
    "AssignedSessionActionTypeDef",
    {
        "definition": "AssignedSessionActionDefinitionTypeDef",
        "sessionActionId": str,
    },
)

AssignedSessionTypeDef = TypedDict(
    "AssignedSessionTypeDef",
    {
        "jobId": str,
        "logConfiguration": "LogConfigurationTypeDef",
        "queueId": str,
        "sessionActions": List["AssignedSessionActionTypeDef"],
    },
)

AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef = TypedDict(
    "AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef",
    {
        "stepId": str,
    },
    total=False,
)

AssignedTaskRunSessionActionDefinitionTypeDef = TypedDict(
    "AssignedTaskRunSessionActionDefinitionTypeDef",
    {
        "parameters": Dict[str, "TaskParameterValueTypeDef"],
        "stepId": str,
        "taskId": str,
    },
)

AssociateMemberToFarmRequestRequestTypeDef = TypedDict(
    "AssociateMemberToFarmRequestRequestTypeDef",
    {
        "farmId": str,
        "identityStoreId": str,
        "membershipLevel": MembershipLevelType,
        "principalId": str,
        "principalType": PrincipalTypeType,
    },
)

AssociateMemberToFleetRequestRequestTypeDef = TypedDict(
    "AssociateMemberToFleetRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "identityStoreId": str,
        "membershipLevel": MembershipLevelType,
        "principalId": str,
        "principalType": PrincipalTypeType,
    },
)

AssociateMemberToJobRequestRequestTypeDef = TypedDict(
    "AssociateMemberToJobRequestRequestTypeDef",
    {
        "farmId": str,
        "identityStoreId": str,
        "jobId": str,
        "membershipLevel": MembershipLevelType,
        "principalId": str,
        "principalType": PrincipalTypeType,
        "queueId": str,
    },
)

AssociateMemberToQueueRequestRequestTypeDef = TypedDict(
    "AssociateMemberToQueueRequestRequestTypeDef",
    {
        "farmId": str,
        "identityStoreId": str,
        "membershipLevel": MembershipLevelType,
        "principalId": str,
        "principalType": PrincipalTypeType,
        "queueId": str,
    },
)

AssumeFleetRoleForReadRequestRequestTypeDef = TypedDict(
    "AssumeFleetRoleForReadRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
    },
)

AssumeFleetRoleForReadResponseTypeDef = TypedDict(
    "AssumeFleetRoleForReadResponseTypeDef",
    {
        "credentials": "AwsCredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssumeFleetRoleForWorkerRequestRequestTypeDef = TypedDict(
    "AssumeFleetRoleForWorkerRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "workerId": str,
    },
)

AssumeFleetRoleForWorkerResponseTypeDef = TypedDict(
    "AssumeFleetRoleForWorkerResponseTypeDef",
    {
        "credentials": "AwsCredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssumeQueueRoleForReadRequestRequestTypeDef = TypedDict(
    "AssumeQueueRoleForReadRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
    },
)

AssumeQueueRoleForReadResponseTypeDef = TypedDict(
    "AssumeQueueRoleForReadResponseTypeDef",
    {
        "credentials": "AwsCredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssumeQueueRoleForUserRequestRequestTypeDef = TypedDict(
    "AssumeQueueRoleForUserRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
    },
)

AssumeQueueRoleForUserResponseTypeDef = TypedDict(
    "AssumeQueueRoleForUserResponseTypeDef",
    {
        "credentials": "AwsCredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssumeQueueRoleForWorkerRequestRequestTypeDef = TypedDict(
    "AssumeQueueRoleForWorkerRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "queueId": str,
        "workerId": str,
    },
)

AssumeQueueRoleForWorkerResponseTypeDef = TypedDict(
    "AssumeQueueRoleForWorkerResponseTypeDef",
    {
        "credentials": "AwsCredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAttachmentsTypeDef = TypedDict(
    "_RequiredAttachmentsTypeDef",
    {
        "manifests": List["ManifestPropertiesTypeDef"],
    },
)
_OptionalAttachmentsTypeDef = TypedDict(
    "_OptionalAttachmentsTypeDef",
    {
        "fileSystem": JobAttachmentsFileSystemType,
    },
    total=False,
)

class AttachmentsTypeDef(_RequiredAttachmentsTypeDef, _OptionalAttachmentsTypeDef):
    pass

AwsCredentialsTypeDef = TypedDict(
    "AwsCredentialsTypeDef",
    {
        "accessKeyId": str,
        "expiration": datetime,
        "secretAccessKey": str,
        "sessionToken": str,
    },
)

BatchGetJobEntityRequestRequestTypeDef = TypedDict(
    "BatchGetJobEntityRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "identifiers": List["JobEntityIdentifiersUnionTypeDef"],
        "workerId": str,
    },
)

BatchGetJobEntityResponseTypeDef = TypedDict(
    "BatchGetJobEntityResponseTypeDef",
    {
        "entities": List["JobEntityTypeDef"],
        "errors": List["GetJobEntityErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBudgetActionToAddTypeDef = TypedDict(
    "_RequiredBudgetActionToAddTypeDef",
    {
        "thresholdPercentage": float,
        "type": BudgetActionTypeType,
    },
)
_OptionalBudgetActionToAddTypeDef = TypedDict(
    "_OptionalBudgetActionToAddTypeDef",
    {
        "description": str,
    },
    total=False,
)

class BudgetActionToAddTypeDef(
    _RequiredBudgetActionToAddTypeDef, _OptionalBudgetActionToAddTypeDef
):
    pass

BudgetActionToRemoveTypeDef = TypedDict(
    "BudgetActionToRemoveTypeDef",
    {
        "thresholdPercentage": float,
        "type": BudgetActionTypeType,
    },
)

BudgetScheduleTypeDef = TypedDict(
    "BudgetScheduleTypeDef",
    {
        "fixed": "FixedBudgetScheduleTypeDef",
    },
    total=False,
)

_RequiredBudgetSummaryTypeDef = TypedDict(
    "_RequiredBudgetSummaryTypeDef",
    {
        "approximateDollarLimit": float,
        "budgetId": str,
        "createdAt": datetime,
        "createdBy": str,
        "displayName": str,
        "status": BudgetStatusType,
        "usageTrackingResource": "UsageTrackingResourceTypeDef",
        "usages": "ConsumedUsagesTypeDef",
    },
)
_OptionalBudgetSummaryTypeDef = TypedDict(
    "_OptionalBudgetSummaryTypeDef",
    {
        "description": str,
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

class BudgetSummaryTypeDef(_RequiredBudgetSummaryTypeDef, _OptionalBudgetSummaryTypeDef):
    pass

ConsumedUsagesTypeDef = TypedDict(
    "ConsumedUsagesTypeDef",
    {
        "approximateDollarUsage": float,
    },
)

CopyJobTemplateRequestRequestTypeDef = TypedDict(
    "CopyJobTemplateRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
        "targetS3Location": "S3LocationTypeDef",
    },
)

CopyJobTemplateResponseTypeDef = TypedDict(
    "CopyJobTemplateResponseTypeDef",
    {
        "templateType": JobTemplateTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBudgetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBudgetRequestRequestTypeDef",
    {
        "actions": List["BudgetActionToAddTypeDef"],
        "approximateDollarLimit": float,
        "displayName": str,
        "farmId": str,
        "schedule": "BudgetScheduleTypeDef",
        "usageTrackingResource": "UsageTrackingResourceTypeDef",
    },
)
_OptionalCreateBudgetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBudgetRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
    },
    total=False,
)

class CreateBudgetRequestRequestTypeDef(
    _RequiredCreateBudgetRequestRequestTypeDef, _OptionalCreateBudgetRequestRequestTypeDef
):
    pass

CreateBudgetResponseTypeDef = TypedDict(
    "CreateBudgetResponseTypeDef",
    {
        "budgetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFarmRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFarmRequestRequestTypeDef",
    {
        "displayName": str,
    },
)
_OptionalCreateFarmRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFarmRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "kmsKeyArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateFarmRequestRequestTypeDef(
    _RequiredCreateFarmRequestRequestTypeDef, _OptionalCreateFarmRequestRequestTypeDef
):
    pass

CreateFarmResponseTypeDef = TypedDict(
    "CreateFarmResponseTypeDef",
    {
        "farmId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFleetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFleetRequestRequestTypeDef",
    {
        "configuration": "FleetConfigurationTypeDef",
        "displayName": str,
        "farmId": str,
        "maxWorkerCount": int,
        "roleArn": str,
    },
)
_OptionalCreateFleetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFleetRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "minWorkerCount": int,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateFleetRequestRequestTypeDef(
    _RequiredCreateFleetRequestRequestTypeDef, _OptionalCreateFleetRequestRequestTypeDef
):
    pass

CreateFleetResponseTypeDef = TypedDict(
    "CreateFleetResponseTypeDef",
    {
        "fleetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateJobRequestRequestTypeDef",
    {
        "farmId": str,
        "priority": int,
        "queueId": str,
        "template": str,
        "templateType": JobTemplateTypeType,
    },
)
_OptionalCreateJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateJobRequestRequestTypeDef",
    {
        "attachments": "AttachmentsTypeDef",
        "clientToken": str,
        "maxFailedTasksCount": int,
        "maxRetriesPerTask": int,
        "parameters": Dict[str, "JobParameterTypeDef"],
        "storageProfileId": str,
        "targetTaskRunStatus": CreateJobTargetTaskRunStatusType,
    },
    total=False,
)

class CreateJobRequestRequestTypeDef(
    _RequiredCreateJobRequestRequestTypeDef, _OptionalCreateJobRequestRequestTypeDef
):
    pass

CreateJobResponseTypeDef = TypedDict(
    "CreateJobResponseTypeDef",
    {
        "jobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLicenseEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLicenseEndpointRequestRequestTypeDef",
    {
        "securityGroupIds": List[str],
        "subnetIds": List[str],
        "vpcId": str,
    },
)
_OptionalCreateLicenseEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLicenseEndpointRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateLicenseEndpointRequestRequestTypeDef(
    _RequiredCreateLicenseEndpointRequestRequestTypeDef,
    _OptionalCreateLicenseEndpointRequestRequestTypeDef,
):
    pass

CreateLicenseEndpointResponseTypeDef = TypedDict(
    "CreateLicenseEndpointResponseTypeDef",
    {
        "licenseEndpointId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMonitorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMonitorRequestRequestTypeDef",
    {
        "displayName": str,
        "identityCenterInstanceArn": str,
        "roleArn": str,
        "subdomain": str,
    },
)
_OptionalCreateMonitorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMonitorRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateMonitorRequestRequestTypeDef(
    _RequiredCreateMonitorRequestRequestTypeDef, _OptionalCreateMonitorRequestRequestTypeDef
):
    pass

CreateMonitorResponseTypeDef = TypedDict(
    "CreateMonitorResponseTypeDef",
    {
        "identityCenterApplicationArn": str,
        "monitorId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateQueueEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateQueueEnvironmentRequestRequestTypeDef",
    {
        "farmId": str,
        "priority": int,
        "queueId": str,
        "template": str,
        "templateType": EnvironmentTemplateTypeType,
    },
)
_OptionalCreateQueueEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateQueueEnvironmentRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateQueueEnvironmentRequestRequestTypeDef(
    _RequiredCreateQueueEnvironmentRequestRequestTypeDef,
    _OptionalCreateQueueEnvironmentRequestRequestTypeDef,
):
    pass

CreateQueueEnvironmentResponseTypeDef = TypedDict(
    "CreateQueueEnvironmentResponseTypeDef",
    {
        "queueEnvironmentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateQueueFleetAssociationRequestRequestTypeDef = TypedDict(
    "CreateQueueFleetAssociationRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "queueId": str,
    },
)

_RequiredCreateQueueRequestRequestTypeDef = TypedDict(
    "_RequiredCreateQueueRequestRequestTypeDef",
    {
        "displayName": str,
        "farmId": str,
    },
)
_OptionalCreateQueueRequestRequestTypeDef = TypedDict(
    "_OptionalCreateQueueRequestRequestTypeDef",
    {
        "allowedStorageProfileIds": List[str],
        "clientToken": str,
        "defaultBudgetAction": DefaultQueueBudgetActionType,
        "description": str,
        "jobAttachmentSettings": "JobAttachmentSettingsTypeDef",
        "jobRunAsUser": "JobRunAsUserTypeDef",
        "requiredFileSystemLocationNames": List[str],
        "roleArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateQueueRequestRequestTypeDef(
    _RequiredCreateQueueRequestRequestTypeDef, _OptionalCreateQueueRequestRequestTypeDef
):
    pass

CreateQueueResponseTypeDef = TypedDict(
    "CreateQueueResponseTypeDef",
    {
        "queueId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStorageProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStorageProfileRequestRequestTypeDef",
    {
        "displayName": str,
        "farmId": str,
        "osFamily": StorageProfileOperatingSystemFamilyType,
    },
)
_OptionalCreateStorageProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStorageProfileRequestRequestTypeDef",
    {
        "clientToken": str,
        "fileSystemLocations": List["FileSystemLocationTypeDef"],
    },
    total=False,
)

class CreateStorageProfileRequestRequestTypeDef(
    _RequiredCreateStorageProfileRequestRequestTypeDef,
    _OptionalCreateStorageProfileRequestRequestTypeDef,
):
    pass

CreateStorageProfileResponseTypeDef = TypedDict(
    "CreateStorageProfileResponseTypeDef",
    {
        "storageProfileId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorkerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorkerRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
    },
)
_OptionalCreateWorkerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorkerRequestRequestTypeDef",
    {
        "clientToken": str,
        "hostProperties": "HostPropertiesRequestTypeDef",
    },
    total=False,
)

class CreateWorkerRequestRequestTypeDef(
    _RequiredCreateWorkerRequestRequestTypeDef, _OptionalCreateWorkerRequestRequestTypeDef
):
    pass

CreateWorkerResponseTypeDef = TypedDict(
    "CreateWorkerResponseTypeDef",
    {
        "workerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCustomerManagedFleetConfigurationTypeDef = TypedDict(
    "_RequiredCustomerManagedFleetConfigurationTypeDef",
    {
        "mode": AutoScalingModeType,
        "workerCapabilities": "CustomerManagedWorkerCapabilitiesTypeDef",
    },
)
_OptionalCustomerManagedFleetConfigurationTypeDef = TypedDict(
    "_OptionalCustomerManagedFleetConfigurationTypeDef",
    {
        "storageProfileId": str,
    },
    total=False,
)

class CustomerManagedFleetConfigurationTypeDef(
    _RequiredCustomerManagedFleetConfigurationTypeDef,
    _OptionalCustomerManagedFleetConfigurationTypeDef,
):
    pass

_RequiredCustomerManagedWorkerCapabilitiesTypeDef = TypedDict(
    "_RequiredCustomerManagedWorkerCapabilitiesTypeDef",
    {
        "cpuArchitectureType": CpuArchitectureTypeType,
        "memoryMiB": "MemoryMiBRangeTypeDef",
        "osFamily": CustomerManagedFleetOperatingSystemFamilyType,
        "vCpuCount": "VCpuCountRangeTypeDef",
    },
)
_OptionalCustomerManagedWorkerCapabilitiesTypeDef = TypedDict(
    "_OptionalCustomerManagedWorkerCapabilitiesTypeDef",
    {
        "acceleratorCount": "AcceleratorCountRangeTypeDef",
        "acceleratorTotalMemoryMiB": "AcceleratorTotalMemoryMiBRangeTypeDef",
        "acceleratorTypes": List[Literal["gpu"]],
        "customAmounts": List["FleetAmountCapabilityTypeDef"],
        "customAttributes": List["FleetAttributeCapabilityTypeDef"],
    },
    total=False,
)

class CustomerManagedWorkerCapabilitiesTypeDef(
    _RequiredCustomerManagedWorkerCapabilitiesTypeDef,
    _OptionalCustomerManagedWorkerCapabilitiesTypeDef,
):
    pass

DateTimeFilterExpressionTypeDef = TypedDict(
    "DateTimeFilterExpressionTypeDef",
    {
        "dateTime": Union[datetime, str],
        "name": str,
        "operator": ComparisonOperatorType,
    },
)

DeleteBudgetRequestRequestTypeDef = TypedDict(
    "DeleteBudgetRequestRequestTypeDef",
    {
        "budgetId": str,
        "farmId": str,
    },
)

DeleteFarmRequestRequestTypeDef = TypedDict(
    "DeleteFarmRequestRequestTypeDef",
    {
        "farmId": str,
    },
)

_RequiredDeleteFleetRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteFleetRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
    },
)
_OptionalDeleteFleetRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteFleetRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteFleetRequestRequestTypeDef(
    _RequiredDeleteFleetRequestRequestTypeDef, _OptionalDeleteFleetRequestRequestTypeDef
):
    pass

DeleteLicenseEndpointRequestRequestTypeDef = TypedDict(
    "DeleteLicenseEndpointRequestRequestTypeDef",
    {
        "licenseEndpointId": str,
    },
)

DeleteMeteredProductRequestRequestTypeDef = TypedDict(
    "DeleteMeteredProductRequestRequestTypeDef",
    {
        "licenseEndpointId": str,
        "productId": str,
    },
)

DeleteMonitorRequestRequestTypeDef = TypedDict(
    "DeleteMonitorRequestRequestTypeDef",
    {
        "monitorId": str,
    },
)

DeleteQueueEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteQueueEnvironmentRequestRequestTypeDef",
    {
        "farmId": str,
        "queueEnvironmentId": str,
        "queueId": str,
    },
)

DeleteQueueFleetAssociationRequestRequestTypeDef = TypedDict(
    "DeleteQueueFleetAssociationRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "queueId": str,
    },
)

DeleteQueueRequestRequestTypeDef = TypedDict(
    "DeleteQueueRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
    },
)

DeleteStorageProfileRequestRequestTypeDef = TypedDict(
    "DeleteStorageProfileRequestRequestTypeDef",
    {
        "farmId": str,
        "storageProfileId": str,
    },
)

DeleteWorkerRequestRequestTypeDef = TypedDict(
    "DeleteWorkerRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "workerId": str,
    },
)

DependencyCountsTypeDef = TypedDict(
    "DependencyCountsTypeDef",
    {
        "consumersResolved": int,
        "consumersUnresolved": int,
        "dependenciesResolved": int,
        "dependenciesUnresolved": int,
    },
)

DisassociateMemberFromFarmRequestRequestTypeDef = TypedDict(
    "DisassociateMemberFromFarmRequestRequestTypeDef",
    {
        "farmId": str,
        "principalId": str,
    },
)

DisassociateMemberFromFleetRequestRequestTypeDef = TypedDict(
    "DisassociateMemberFromFleetRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "principalId": str,
    },
)

DisassociateMemberFromJobRequestRequestTypeDef = TypedDict(
    "DisassociateMemberFromJobRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "principalId": str,
        "queueId": str,
    },
)

DisassociateMemberFromQueueRequestRequestTypeDef = TypedDict(
    "DisassociateMemberFromQueueRequestRequestTypeDef",
    {
        "farmId": str,
        "principalId": str,
        "queueId": str,
    },
)

Ec2EbsVolumeTypeDef = TypedDict(
    "Ec2EbsVolumeTypeDef",
    {
        "iops": int,
        "sizeGiB": int,
        "throughputMiB": int,
    },
    total=False,
)

EnvironmentDetailsEntityTypeDef = TypedDict(
    "EnvironmentDetailsEntityTypeDef",
    {
        "environmentId": str,
        "jobId": str,
        "schemaVersion": str,
        "template": Dict[str, Any],
    },
)

EnvironmentDetailsErrorTypeDef = TypedDict(
    "EnvironmentDetailsErrorTypeDef",
    {
        "code": JobEntityErrorCodeType,
        "environmentId": str,
        "jobId": str,
        "message": str,
    },
)

EnvironmentDetailsIdentifiersTypeDef = TypedDict(
    "EnvironmentDetailsIdentifiersTypeDef",
    {
        "environmentId": str,
        "jobId": str,
    },
)

EnvironmentEnterSessionActionDefinitionSummaryTypeDef = TypedDict(
    "EnvironmentEnterSessionActionDefinitionSummaryTypeDef",
    {
        "environmentId": str,
    },
)

EnvironmentEnterSessionActionDefinitionTypeDef = TypedDict(
    "EnvironmentEnterSessionActionDefinitionTypeDef",
    {
        "environmentId": str,
    },
)

EnvironmentExitSessionActionDefinitionSummaryTypeDef = TypedDict(
    "EnvironmentExitSessionActionDefinitionSummaryTypeDef",
    {
        "environmentId": str,
    },
)

EnvironmentExitSessionActionDefinitionTypeDef = TypedDict(
    "EnvironmentExitSessionActionDefinitionTypeDef",
    {
        "environmentId": str,
    },
)

FarmMemberTypeDef = TypedDict(
    "FarmMemberTypeDef",
    {
        "farmId": str,
        "identityStoreId": str,
        "membershipLevel": MembershipLevelType,
        "principalId": str,
        "principalType": PrincipalTypeType,
    },
)

_RequiredFarmSummaryTypeDef = TypedDict(
    "_RequiredFarmSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "displayName": str,
        "farmId": str,
    },
)
_OptionalFarmSummaryTypeDef = TypedDict(
    "_OptionalFarmSummaryTypeDef",
    {
        "kmsKeyArn": str,
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

class FarmSummaryTypeDef(_RequiredFarmSummaryTypeDef, _OptionalFarmSummaryTypeDef):
    pass

FieldSortExpressionTypeDef = TypedDict(
    "FieldSortExpressionTypeDef",
    {
        "name": str,
        "sortOrder": SortOrderType,
    },
)

FileSystemLocationTypeDef = TypedDict(
    "FileSystemLocationTypeDef",
    {
        "name": str,
        "path": str,
        "type": FileSystemLocationTypeType,
    },
)

FixedBudgetScheduleTypeDef = TypedDict(
    "FixedBudgetScheduleTypeDef",
    {
        "endTime": Union[datetime, str],
        "startTime": Union[datetime, str],
    },
)

_RequiredFleetAmountCapabilityTypeDef = TypedDict(
    "_RequiredFleetAmountCapabilityTypeDef",
    {
        "min": float,
        "name": str,
    },
)
_OptionalFleetAmountCapabilityTypeDef = TypedDict(
    "_OptionalFleetAmountCapabilityTypeDef",
    {
        "max": float,
    },
    total=False,
)

class FleetAmountCapabilityTypeDef(
    _RequiredFleetAmountCapabilityTypeDef, _OptionalFleetAmountCapabilityTypeDef
):
    pass

FleetAttributeCapabilityTypeDef = TypedDict(
    "FleetAttributeCapabilityTypeDef",
    {
        "name": str,
        "values": List[str],
    },
)

FleetCapabilitiesTypeDef = TypedDict(
    "FleetCapabilitiesTypeDef",
    {
        "amounts": List["FleetAmountCapabilityTypeDef"],
        "attributes": List["FleetAttributeCapabilityTypeDef"],
    },
    total=False,
)

FleetConfigurationTypeDef = TypedDict(
    "FleetConfigurationTypeDef",
    {
        "customerManaged": "CustomerManagedFleetConfigurationTypeDef",
        "serviceManagedEc2": "ServiceManagedEc2FleetConfigurationTypeDef",
    },
    total=False,
)

FleetMemberTypeDef = TypedDict(
    "FleetMemberTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "identityStoreId": str,
        "membershipLevel": MembershipLevelType,
        "principalId": str,
        "principalType": PrincipalTypeType,
    },
)

_RequiredFleetSummaryTypeDef = TypedDict(
    "_RequiredFleetSummaryTypeDef",
    {
        "configuration": "FleetConfigurationTypeDef",
        "createdAt": datetime,
        "createdBy": str,
        "displayName": str,
        "farmId": str,
        "fleetId": str,
        "maxWorkerCount": int,
        "minWorkerCount": int,
        "status": FleetStatusType,
        "workerCount": int,
    },
)
_OptionalFleetSummaryTypeDef = TypedDict(
    "_OptionalFleetSummaryTypeDef",
    {
        "autoScalingStatus": AutoScalingStatusType,
        "targetWorkerCount": int,
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

class FleetSummaryTypeDef(_RequiredFleetSummaryTypeDef, _OptionalFleetSummaryTypeDef):
    pass

GetBudgetRequestRequestTypeDef = TypedDict(
    "GetBudgetRequestRequestTypeDef",
    {
        "budgetId": str,
        "farmId": str,
    },
)

GetBudgetResponseTypeDef = TypedDict(
    "GetBudgetResponseTypeDef",
    {
        "actions": List["ResponseBudgetActionTypeDef"],
        "approximateDollarLimit": float,
        "budgetId": str,
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "displayName": str,
        "queueStoppedAt": datetime,
        "schedule": "BudgetScheduleTypeDef",
        "status": BudgetStatusType,
        "updatedAt": datetime,
        "updatedBy": str,
        "usageTrackingResource": "UsageTrackingResourceTypeDef",
        "usages": "ConsumedUsagesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFarmRequestRequestTypeDef = TypedDict(
    "GetFarmRequestRequestTypeDef",
    {
        "farmId": str,
    },
)

GetFarmResponseTypeDef = TypedDict(
    "GetFarmResponseTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "displayName": str,
        "farmId": str,
        "kmsKeyArn": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFleetRequestRequestTypeDef = TypedDict(
    "GetFleetRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
    },
)

GetFleetResponseTypeDef = TypedDict(
    "GetFleetResponseTypeDef",
    {
        "autoScalingStatus": AutoScalingStatusType,
        "capabilities": "FleetCapabilitiesTypeDef",
        "configuration": "FleetConfigurationTypeDef",
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "displayName": str,
        "farmId": str,
        "fleetId": str,
        "maxWorkerCount": int,
        "minWorkerCount": int,
        "roleArn": str,
        "status": FleetStatusType,
        "targetWorkerCount": int,
        "updatedAt": datetime,
        "updatedBy": str,
        "workerCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobEntityErrorTypeDef = TypedDict(
    "GetJobEntityErrorTypeDef",
    {
        "environmentDetails": "EnvironmentDetailsErrorTypeDef",
        "jobAttachmentDetails": "JobAttachmentDetailsErrorTypeDef",
        "jobDetails": "JobDetailsErrorTypeDef",
        "stepDetails": "StepDetailsErrorTypeDef",
    },
    total=False,
)

GetJobRequestRequestTypeDef = TypedDict(
    "GetJobRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
    },
)

GetJobResponseTypeDef = TypedDict(
    "GetJobResponseTypeDef",
    {
        "attachments": "AttachmentsTypeDef",
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "endedAt": datetime,
        "jobId": str,
        "lifecycleStatus": JobLifecycleStatusType,
        "lifecycleStatusMessage": str,
        "maxFailedTasksCount": int,
        "maxRetriesPerTask": int,
        "name": str,
        "parameters": Dict[str, "JobParameterTypeDef"],
        "priority": int,
        "startedAt": datetime,
        "storageProfileId": str,
        "targetTaskRunStatus": JobTargetTaskRunStatusType,
        "taskRunStatus": TaskRunStatusType,
        "taskRunStatusCounts": Dict[TaskRunStatusType, int],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLicenseEndpointRequestRequestTypeDef = TypedDict(
    "GetLicenseEndpointRequestRequestTypeDef",
    {
        "licenseEndpointId": str,
    },
)

GetLicenseEndpointResponseTypeDef = TypedDict(
    "GetLicenseEndpointResponseTypeDef",
    {
        "dnsName": str,
        "licenseEndpointId": str,
        "securityGroupIds": List[str],
        "status": LicenseEndpointStatusType,
        "statusMessage": str,
        "subnetIds": List[str],
        "vpcId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMonitorRequestRequestTypeDef = TypedDict(
    "GetMonitorRequestRequestTypeDef",
    {
        "monitorId": str,
    },
)

GetMonitorResponseTypeDef = TypedDict(
    "GetMonitorResponseTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "displayName": str,
        "identityCenterApplicationArn": str,
        "identityCenterInstanceArn": str,
        "monitorId": str,
        "roleArn": str,
        "subdomain": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueueEnvironmentRequestRequestTypeDef = TypedDict(
    "GetQueueEnvironmentRequestRequestTypeDef",
    {
        "farmId": str,
        "queueEnvironmentId": str,
        "queueId": str,
    },
)

GetQueueEnvironmentResponseTypeDef = TypedDict(
    "GetQueueEnvironmentResponseTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "name": str,
        "priority": int,
        "queueEnvironmentId": str,
        "template": str,
        "templateType": EnvironmentTemplateTypeType,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueueFleetAssociationRequestRequestTypeDef = TypedDict(
    "GetQueueFleetAssociationRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "queueId": str,
    },
)

GetQueueFleetAssociationResponseTypeDef = TypedDict(
    "GetQueueFleetAssociationResponseTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "fleetId": str,
        "queueId": str,
        "status": QueueFleetAssociationStatusType,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueueRequestRequestTypeDef = TypedDict(
    "GetQueueRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
    },
)

GetQueueResponseTypeDef = TypedDict(
    "GetQueueResponseTypeDef",
    {
        "allowedStorageProfileIds": List[str],
        "blockedReason": QueueBlockedReasonType,
        "createdAt": datetime,
        "createdBy": str,
        "defaultBudgetAction": DefaultQueueBudgetActionType,
        "description": str,
        "displayName": str,
        "farmId": str,
        "jobAttachmentSettings": "JobAttachmentSettingsTypeDef",
        "jobRunAsUser": "JobRunAsUserTypeDef",
        "queueId": str,
        "requiredFileSystemLocationNames": List[str],
        "roleArn": str,
        "status": QueueStatusType,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSessionActionRequestRequestTypeDef = TypedDict(
    "GetSessionActionRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
        "sessionActionId": str,
    },
)

GetSessionActionResponseTypeDef = TypedDict(
    "GetSessionActionResponseTypeDef",
    {
        "definition": "SessionActionDefinitionTypeDef",
        "endedAt": datetime,
        "processExitCode": int,
        "progressMessage": str,
        "progressPercent": float,
        "sessionActionId": str,
        "sessionId": str,
        "startedAt": datetime,
        "status": SessionActionStatusType,
        "workerUpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSessionRequestRequestTypeDef = TypedDict(
    "GetSessionRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
        "sessionId": str,
    },
)

GetSessionResponseTypeDef = TypedDict(
    "GetSessionResponseTypeDef",
    {
        "endedAt": datetime,
        "fleetId": str,
        "hostProperties": "HostPropertiesResponseTypeDef",
        "lifecycleStatus": SessionLifecycleStatusType,
        "log": "LogConfigurationTypeDef",
        "sessionId": str,
        "startedAt": datetime,
        "targetLifecycleStatus": Literal["ENDED"],
        "updatedAt": datetime,
        "updatedBy": str,
        "workerId": str,
        "workerLog": "LogConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSessionsStatisticsAggregationRequestRequestTypeDef = TypedDict(
    "_RequiredGetSessionsStatisticsAggregationRequestRequestTypeDef",
    {
        "aggregationId": str,
        "farmId": str,
    },
)
_OptionalGetSessionsStatisticsAggregationRequestRequestTypeDef = TypedDict(
    "_OptionalGetSessionsStatisticsAggregationRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class GetSessionsStatisticsAggregationRequestRequestTypeDef(
    _RequiredGetSessionsStatisticsAggregationRequestRequestTypeDef,
    _OptionalGetSessionsStatisticsAggregationRequestRequestTypeDef,
):
    pass

GetSessionsStatisticsAggregationResponseTypeDef = TypedDict(
    "GetSessionsStatisticsAggregationResponseTypeDef",
    {
        "nextToken": str,
        "statistics": List["StatisticsTypeDef"],
        "status": SessionsStatisticsAggregationStatusType,
        "statusMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStepRequestRequestTypeDef = TypedDict(
    "GetStepRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
        "stepId": str,
    },
)

GetStepResponseTypeDef = TypedDict(
    "GetStepResponseTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "dependencyCounts": "DependencyCountsTypeDef",
        "description": str,
        "endedAt": datetime,
        "lifecycleStatus": StepLifecycleStatusType,
        "lifecycleStatusMessage": str,
        "name": str,
        "parameterSpace": "ParameterSpaceTypeDef",
        "requiredCapabilities": "StepRequiredCapabilitiesTypeDef",
        "startedAt": datetime,
        "stepId": str,
        "targetTaskRunStatus": StepTargetTaskRunStatusType,
        "taskRunStatus": TaskRunStatusType,
        "taskRunStatusCounts": Dict[TaskRunStatusType, int],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStorageProfileForQueueRequestRequestTypeDef = TypedDict(
    "GetStorageProfileForQueueRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "storageProfileId": str,
    },
)

GetStorageProfileForQueueResponseTypeDef = TypedDict(
    "GetStorageProfileForQueueResponseTypeDef",
    {
        "displayName": str,
        "fileSystemLocations": List["FileSystemLocationTypeDef"],
        "osFamily": StorageProfileOperatingSystemFamilyType,
        "storageProfileId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStorageProfileRequestRequestTypeDef = TypedDict(
    "GetStorageProfileRequestRequestTypeDef",
    {
        "farmId": str,
        "storageProfileId": str,
    },
)

GetStorageProfileResponseTypeDef = TypedDict(
    "GetStorageProfileResponseTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "displayName": str,
        "fileSystemLocations": List["FileSystemLocationTypeDef"],
        "osFamily": StorageProfileOperatingSystemFamilyType,
        "storageProfileId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTaskRequestRequestTypeDef = TypedDict(
    "GetTaskRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
        "stepId": str,
        "taskId": str,
    },
)

GetTaskResponseTypeDef = TypedDict(
    "GetTaskResponseTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "endedAt": datetime,
        "failureRetryCount": int,
        "latestSessionActionId": str,
        "parameters": Dict[str, "TaskParameterValueTypeDef"],
        "runStatus": TaskRunStatusType,
        "startedAt": datetime,
        "targetRunStatus": TaskTargetRunStatusType,
        "taskId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkerRequestRequestTypeDef = TypedDict(
    "GetWorkerRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "workerId": str,
    },
)

GetWorkerResponseTypeDef = TypedDict(
    "GetWorkerResponseTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "farmId": str,
        "fleetId": str,
        "hostProperties": "HostPropertiesResponseTypeDef",
        "log": "LogConfigurationTypeDef",
        "status": WorkerStatusType,
        "updatedAt": datetime,
        "updatedBy": str,
        "workerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HostPropertiesRequestTypeDef = TypedDict(
    "HostPropertiesRequestTypeDef",
    {
        "hostName": str,
        "ipAddresses": "IpAddressesTypeDef",
    },
    total=False,
)

HostPropertiesResponseTypeDef = TypedDict(
    "HostPropertiesResponseTypeDef",
    {
        "ec2InstanceArn": str,
        "ec2InstanceType": str,
        "hostName": str,
        "ipAddresses": "IpAddressesTypeDef",
    },
    total=False,
)

IpAddressesTypeDef = TypedDict(
    "IpAddressesTypeDef",
    {
        "ipV4Addresses": List[str],
        "ipV6Addresses": List[str],
    },
    total=False,
)

JobAttachmentDetailsEntityTypeDef = TypedDict(
    "JobAttachmentDetailsEntityTypeDef",
    {
        "attachments": "AttachmentsTypeDef",
        "jobId": str,
    },
)

JobAttachmentDetailsErrorTypeDef = TypedDict(
    "JobAttachmentDetailsErrorTypeDef",
    {
        "code": JobEntityErrorCodeType,
        "jobId": str,
        "message": str,
    },
)

JobAttachmentDetailsIdentifiersTypeDef = TypedDict(
    "JobAttachmentDetailsIdentifiersTypeDef",
    {
        "jobId": str,
    },
)

JobAttachmentSettingsTypeDef = TypedDict(
    "JobAttachmentSettingsTypeDef",
    {
        "rootPrefix": str,
        "s3BucketName": str,
    },
)

_RequiredJobDetailsEntityTypeDef = TypedDict(
    "_RequiredJobDetailsEntityTypeDef",
    {
        "jobId": str,
        "logGroupName": str,
        "schemaVersion": str,
    },
)
_OptionalJobDetailsEntityTypeDef = TypedDict(
    "_OptionalJobDetailsEntityTypeDef",
    {
        "jobAttachmentSettings": "JobAttachmentSettingsTypeDef",
        "jobRunAsUser": "JobRunAsUserTypeDef",
        "parameters": Dict[str, "JobParameterTypeDef"],
        "pathMappingRules": List["PathMappingRuleTypeDef"],
        "queueRoleArn": str,
    },
    total=False,
)

class JobDetailsEntityTypeDef(_RequiredJobDetailsEntityTypeDef, _OptionalJobDetailsEntityTypeDef):
    pass

JobDetailsErrorTypeDef = TypedDict(
    "JobDetailsErrorTypeDef",
    {
        "code": JobEntityErrorCodeType,
        "jobId": str,
        "message": str,
    },
)

JobDetailsIdentifiersTypeDef = TypedDict(
    "JobDetailsIdentifiersTypeDef",
    {
        "jobId": str,
    },
)

JobEntityIdentifiersUnionTypeDef = TypedDict(
    "JobEntityIdentifiersUnionTypeDef",
    {
        "environmentDetails": "EnvironmentDetailsIdentifiersTypeDef",
        "jobAttachmentDetails": "JobAttachmentDetailsIdentifiersTypeDef",
        "jobDetails": "JobDetailsIdentifiersTypeDef",
        "stepDetails": "StepDetailsIdentifiersTypeDef",
    },
    total=False,
)

JobEntityTypeDef = TypedDict(
    "JobEntityTypeDef",
    {
        "environmentDetails": "EnvironmentDetailsEntityTypeDef",
        "jobAttachmentDetails": "JobAttachmentDetailsEntityTypeDef",
        "jobDetails": "JobDetailsEntityTypeDef",
        "stepDetails": "StepDetailsEntityTypeDef",
    },
    total=False,
)

JobMemberTypeDef = TypedDict(
    "JobMemberTypeDef",
    {
        "farmId": str,
        "identityStoreId": str,
        "jobId": str,
        "membershipLevel": MembershipLevelType,
        "principalId": str,
        "principalType": PrincipalTypeType,
        "queueId": str,
    },
)

JobParameterTypeDef = TypedDict(
    "JobParameterTypeDef",
    {
        "float": str,
        "int": str,
        "path": str,
        "string": str,
    },
    total=False,
)

_RequiredJobRunAsUserTypeDef = TypedDict(
    "_RequiredJobRunAsUserTypeDef",
    {
        "runAs": RunAsType,
    },
)
_OptionalJobRunAsUserTypeDef = TypedDict(
    "_OptionalJobRunAsUserTypeDef",
    {
        "posix": "PosixUserTypeDef",
        "windows": "WindowsUserTypeDef",
    },
    total=False,
)

class JobRunAsUserTypeDef(_RequiredJobRunAsUserTypeDef, _OptionalJobRunAsUserTypeDef):
    pass

JobSearchSummaryTypeDef = TypedDict(
    "JobSearchSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "endedAt": datetime,
        "jobId": str,
        "jobParameters": Dict[str, "JobParameterTypeDef"],
        "lifecycleStatus": JobLifecycleStatusType,
        "lifecycleStatusMessage": str,
        "maxFailedTasksCount": int,
        "maxRetriesPerTask": int,
        "name": str,
        "priority": int,
        "queueId": str,
        "startedAt": datetime,
        "targetTaskRunStatus": JobTargetTaskRunStatusType,
        "taskRunStatus": TaskRunStatusType,
        "taskRunStatusCounts": Dict[TaskRunStatusType, int],
    },
    total=False,
)

_RequiredJobSummaryTypeDef = TypedDict(
    "_RequiredJobSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "jobId": str,
        "lifecycleStatus": JobLifecycleStatusType,
        "lifecycleStatusMessage": str,
        "name": str,
        "priority": int,
    },
)
_OptionalJobSummaryTypeDef = TypedDict(
    "_OptionalJobSummaryTypeDef",
    {
        "endedAt": datetime,
        "maxFailedTasksCount": int,
        "maxRetriesPerTask": int,
        "startedAt": datetime,
        "targetTaskRunStatus": JobTargetTaskRunStatusType,
        "taskRunStatus": TaskRunStatusType,
        "taskRunStatusCounts": Dict[TaskRunStatusType, int],
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

class JobSummaryTypeDef(_RequiredJobSummaryTypeDef, _OptionalJobSummaryTypeDef):
    pass

LicenseEndpointSummaryTypeDef = TypedDict(
    "LicenseEndpointSummaryTypeDef",
    {
        "licenseEndpointId": str,
        "status": LicenseEndpointStatusType,
        "statusMessage": str,
        "vpcId": str,
    },
    total=False,
)

ListAvailableMeteredProductsRequestRequestTypeDef = TypedDict(
    "ListAvailableMeteredProductsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListAvailableMeteredProductsResponseTypeDef = TypedDict(
    "ListAvailableMeteredProductsResponseTypeDef",
    {
        "meteredProducts": List["MeteredProductSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBudgetsRequestRequestTypeDef = TypedDict(
    "_RequiredListBudgetsRequestRequestTypeDef",
    {
        "farmId": str,
    },
)
_OptionalListBudgetsRequestRequestTypeDef = TypedDict(
    "_OptionalListBudgetsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "status": BudgetStatusType,
    },
    total=False,
)

class ListBudgetsRequestRequestTypeDef(
    _RequiredListBudgetsRequestRequestTypeDef, _OptionalListBudgetsRequestRequestTypeDef
):
    pass

ListBudgetsResponseTypeDef = TypedDict(
    "ListBudgetsResponseTypeDef",
    {
        "budgets": List["BudgetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFarmMembersRequestRequestTypeDef = TypedDict(
    "_RequiredListFarmMembersRequestRequestTypeDef",
    {
        "farmId": str,
    },
)
_OptionalListFarmMembersRequestRequestTypeDef = TypedDict(
    "_OptionalListFarmMembersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListFarmMembersRequestRequestTypeDef(
    _RequiredListFarmMembersRequestRequestTypeDef, _OptionalListFarmMembersRequestRequestTypeDef
):
    pass

ListFarmMembersResponseTypeDef = TypedDict(
    "ListFarmMembersResponseTypeDef",
    {
        "members": List["FarmMemberTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFarmsRequestRequestTypeDef = TypedDict(
    "ListFarmsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "principalId": str,
    },
    total=False,
)

ListFarmsResponseTypeDef = TypedDict(
    "ListFarmsResponseTypeDef",
    {
        "farms": List["FarmSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFleetMembersRequestRequestTypeDef = TypedDict(
    "_RequiredListFleetMembersRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
    },
)
_OptionalListFleetMembersRequestRequestTypeDef = TypedDict(
    "_OptionalListFleetMembersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListFleetMembersRequestRequestTypeDef(
    _RequiredListFleetMembersRequestRequestTypeDef, _OptionalListFleetMembersRequestRequestTypeDef
):
    pass

ListFleetMembersResponseTypeDef = TypedDict(
    "ListFleetMembersResponseTypeDef",
    {
        "members": List["FleetMemberTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFleetsRequestRequestTypeDef = TypedDict(
    "_RequiredListFleetsRequestRequestTypeDef",
    {
        "farmId": str,
    },
)
_OptionalListFleetsRequestRequestTypeDef = TypedDict(
    "_OptionalListFleetsRequestRequestTypeDef",
    {
        "displayName": str,
        "maxResults": int,
        "nextToken": str,
        "principalId": str,
        "status": FleetStatusType,
    },
    total=False,
)

class ListFleetsRequestRequestTypeDef(
    _RequiredListFleetsRequestRequestTypeDef, _OptionalListFleetsRequestRequestTypeDef
):
    pass

ListFleetsResponseTypeDef = TypedDict(
    "ListFleetsResponseTypeDef",
    {
        "fleets": List["FleetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListJobMembersRequestRequestTypeDef = TypedDict(
    "_RequiredListJobMembersRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
    },
)
_OptionalListJobMembersRequestRequestTypeDef = TypedDict(
    "_OptionalListJobMembersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListJobMembersRequestRequestTypeDef(
    _RequiredListJobMembersRequestRequestTypeDef, _OptionalListJobMembersRequestRequestTypeDef
):
    pass

ListJobMembersResponseTypeDef = TypedDict(
    "ListJobMembersResponseTypeDef",
    {
        "members": List["JobMemberTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListJobsRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
    },
)
_OptionalListJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListJobsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "principalId": str,
    },
    total=False,
)

class ListJobsRequestRequestTypeDef(
    _RequiredListJobsRequestRequestTypeDef, _OptionalListJobsRequestRequestTypeDef
):
    pass

ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef",
    {
        "jobs": List["JobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLicenseEndpointsRequestRequestTypeDef = TypedDict(
    "ListLicenseEndpointsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListLicenseEndpointsResponseTypeDef = TypedDict(
    "ListLicenseEndpointsResponseTypeDef",
    {
        "licenseEndpoints": List["LicenseEndpointSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMeteredProductsRequestRequestTypeDef = TypedDict(
    "_RequiredListMeteredProductsRequestRequestTypeDef",
    {
        "licenseEndpointId": str,
    },
)
_OptionalListMeteredProductsRequestRequestTypeDef = TypedDict(
    "_OptionalListMeteredProductsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListMeteredProductsRequestRequestTypeDef(
    _RequiredListMeteredProductsRequestRequestTypeDef,
    _OptionalListMeteredProductsRequestRequestTypeDef,
):
    pass

ListMeteredProductsResponseTypeDef = TypedDict(
    "ListMeteredProductsResponseTypeDef",
    {
        "meteredProducts": List["MeteredProductSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMonitorsRequestRequestTypeDef = TypedDict(
    "ListMonitorsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListMonitorsResponseTypeDef = TypedDict(
    "ListMonitorsResponseTypeDef",
    {
        "monitors": List["MonitorSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQueueEnvironmentsRequestRequestTypeDef = TypedDict(
    "_RequiredListQueueEnvironmentsRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
    },
)
_OptionalListQueueEnvironmentsRequestRequestTypeDef = TypedDict(
    "_OptionalListQueueEnvironmentsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListQueueEnvironmentsRequestRequestTypeDef(
    _RequiredListQueueEnvironmentsRequestRequestTypeDef,
    _OptionalListQueueEnvironmentsRequestRequestTypeDef,
):
    pass

ListQueueEnvironmentsResponseTypeDef = TypedDict(
    "ListQueueEnvironmentsResponseTypeDef",
    {
        "environments": List["QueueEnvironmentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQueueFleetAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListQueueFleetAssociationsRequestRequestTypeDef",
    {
        "farmId": str,
    },
)
_OptionalListQueueFleetAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListQueueFleetAssociationsRequestRequestTypeDef",
    {
        "fleetId": str,
        "maxResults": int,
        "nextToken": str,
        "queueId": str,
    },
    total=False,
)

class ListQueueFleetAssociationsRequestRequestTypeDef(
    _RequiredListQueueFleetAssociationsRequestRequestTypeDef,
    _OptionalListQueueFleetAssociationsRequestRequestTypeDef,
):
    pass

ListQueueFleetAssociationsResponseTypeDef = TypedDict(
    "ListQueueFleetAssociationsResponseTypeDef",
    {
        "nextToken": str,
        "queueFleetAssociations": List["QueueFleetAssociationSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQueueMembersRequestRequestTypeDef = TypedDict(
    "_RequiredListQueueMembersRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
    },
)
_OptionalListQueueMembersRequestRequestTypeDef = TypedDict(
    "_OptionalListQueueMembersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListQueueMembersRequestRequestTypeDef(
    _RequiredListQueueMembersRequestRequestTypeDef, _OptionalListQueueMembersRequestRequestTypeDef
):
    pass

ListQueueMembersResponseTypeDef = TypedDict(
    "ListQueueMembersResponseTypeDef",
    {
        "members": List["QueueMemberTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQueuesRequestRequestTypeDef = TypedDict(
    "_RequiredListQueuesRequestRequestTypeDef",
    {
        "farmId": str,
    },
)
_OptionalListQueuesRequestRequestTypeDef = TypedDict(
    "_OptionalListQueuesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "principalId": str,
        "status": QueueStatusType,
    },
    total=False,
)

class ListQueuesRequestRequestTypeDef(
    _RequiredListQueuesRequestRequestTypeDef, _OptionalListQueuesRequestRequestTypeDef
):
    pass

ListQueuesResponseTypeDef = TypedDict(
    "ListQueuesResponseTypeDef",
    {
        "nextToken": str,
        "queues": List["QueueSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSessionActionsRequestRequestTypeDef = TypedDict(
    "_RequiredListSessionActionsRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
    },
)
_OptionalListSessionActionsRequestRequestTypeDef = TypedDict(
    "_OptionalListSessionActionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "sessionId": str,
        "taskId": str,
    },
    total=False,
)

class ListSessionActionsRequestRequestTypeDef(
    _RequiredListSessionActionsRequestRequestTypeDef,
    _OptionalListSessionActionsRequestRequestTypeDef,
):
    pass

ListSessionActionsResponseTypeDef = TypedDict(
    "ListSessionActionsResponseTypeDef",
    {
        "nextToken": str,
        "sessionActions": List["SessionActionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSessionsForWorkerRequestRequestTypeDef = TypedDict(
    "_RequiredListSessionsForWorkerRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "workerId": str,
    },
)
_OptionalListSessionsForWorkerRequestRequestTypeDef = TypedDict(
    "_OptionalListSessionsForWorkerRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListSessionsForWorkerRequestRequestTypeDef(
    _RequiredListSessionsForWorkerRequestRequestTypeDef,
    _OptionalListSessionsForWorkerRequestRequestTypeDef,
):
    pass

ListSessionsForWorkerResponseTypeDef = TypedDict(
    "ListSessionsForWorkerResponseTypeDef",
    {
        "nextToken": str,
        "sessions": List["WorkerSessionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSessionsRequestRequestTypeDef = TypedDict(
    "_RequiredListSessionsRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
    },
)
_OptionalListSessionsRequestRequestTypeDef = TypedDict(
    "_OptionalListSessionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListSessionsRequestRequestTypeDef(
    _RequiredListSessionsRequestRequestTypeDef, _OptionalListSessionsRequestRequestTypeDef
):
    pass

ListSessionsResponseTypeDef = TypedDict(
    "ListSessionsResponseTypeDef",
    {
        "nextToken": str,
        "sessions": List["SessionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStepConsumersRequestRequestTypeDef = TypedDict(
    "_RequiredListStepConsumersRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
        "stepId": str,
    },
)
_OptionalListStepConsumersRequestRequestTypeDef = TypedDict(
    "_OptionalListStepConsumersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListStepConsumersRequestRequestTypeDef(
    _RequiredListStepConsumersRequestRequestTypeDef, _OptionalListStepConsumersRequestRequestTypeDef
):
    pass

ListStepConsumersResponseTypeDef = TypedDict(
    "ListStepConsumersResponseTypeDef",
    {
        "consumers": List["StepConsumerTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStepDependenciesRequestRequestTypeDef = TypedDict(
    "_RequiredListStepDependenciesRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
        "stepId": str,
    },
)
_OptionalListStepDependenciesRequestRequestTypeDef = TypedDict(
    "_OptionalListStepDependenciesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListStepDependenciesRequestRequestTypeDef(
    _RequiredListStepDependenciesRequestRequestTypeDef,
    _OptionalListStepDependenciesRequestRequestTypeDef,
):
    pass

ListStepDependenciesResponseTypeDef = TypedDict(
    "ListStepDependenciesResponseTypeDef",
    {
        "dependencies": List["StepDependencyTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStepsRequestRequestTypeDef = TypedDict(
    "_RequiredListStepsRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
    },
)
_OptionalListStepsRequestRequestTypeDef = TypedDict(
    "_OptionalListStepsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListStepsRequestRequestTypeDef(
    _RequiredListStepsRequestRequestTypeDef, _OptionalListStepsRequestRequestTypeDef
):
    pass

ListStepsResponseTypeDef = TypedDict(
    "ListStepsResponseTypeDef",
    {
        "nextToken": str,
        "steps": List["StepSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStorageProfilesForQueueRequestRequestTypeDef = TypedDict(
    "_RequiredListStorageProfilesForQueueRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
    },
)
_OptionalListStorageProfilesForQueueRequestRequestTypeDef = TypedDict(
    "_OptionalListStorageProfilesForQueueRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListStorageProfilesForQueueRequestRequestTypeDef(
    _RequiredListStorageProfilesForQueueRequestRequestTypeDef,
    _OptionalListStorageProfilesForQueueRequestRequestTypeDef,
):
    pass

ListStorageProfilesForQueueResponseTypeDef = TypedDict(
    "ListStorageProfilesForQueueResponseTypeDef",
    {
        "nextToken": str,
        "storageProfiles": List["StorageProfileSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStorageProfilesRequestRequestTypeDef = TypedDict(
    "_RequiredListStorageProfilesRequestRequestTypeDef",
    {
        "farmId": str,
    },
)
_OptionalListStorageProfilesRequestRequestTypeDef = TypedDict(
    "_OptionalListStorageProfilesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListStorageProfilesRequestRequestTypeDef(
    _RequiredListStorageProfilesRequestRequestTypeDef,
    _OptionalListStorageProfilesRequestRequestTypeDef,
):
    pass

ListStorageProfilesResponseTypeDef = TypedDict(
    "ListStorageProfilesResponseTypeDef",
    {
        "nextToken": str,
        "storageProfiles": List["StorageProfileSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTasksRequestRequestTypeDef = TypedDict(
    "_RequiredListTasksRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
        "stepId": str,
    },
)
_OptionalListTasksRequestRequestTypeDef = TypedDict(
    "_OptionalListTasksRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListTasksRequestRequestTypeDef(
    _RequiredListTasksRequestRequestTypeDef, _OptionalListTasksRequestRequestTypeDef
):
    pass

ListTasksResponseTypeDef = TypedDict(
    "ListTasksResponseTypeDef",
    {
        "nextToken": str,
        "tasks": List["TaskSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWorkersRequestRequestTypeDef = TypedDict(
    "_RequiredListWorkersRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
    },
)
_OptionalListWorkersRequestRequestTypeDef = TypedDict(
    "_OptionalListWorkersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListWorkersRequestRequestTypeDef(
    _RequiredListWorkersRequestRequestTypeDef, _OptionalListWorkersRequestRequestTypeDef
):
    pass

ListWorkersResponseTypeDef = TypedDict(
    "ListWorkersResponseTypeDef",
    {
        "nextToken": str,
        "workers": List["WorkerSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLogConfigurationTypeDef = TypedDict(
    "_RequiredLogConfigurationTypeDef",
    {
        "logDriver": str,
    },
)
_OptionalLogConfigurationTypeDef = TypedDict(
    "_OptionalLogConfigurationTypeDef",
    {
        "error": str,
        "options": Dict[str, str],
        "parameters": Dict[str, str],
    },
    total=False,
)

class LogConfigurationTypeDef(_RequiredLogConfigurationTypeDef, _OptionalLogConfigurationTypeDef):
    pass

_RequiredManifestPropertiesTypeDef = TypedDict(
    "_RequiredManifestPropertiesTypeDef",
    {
        "rootPath": str,
        "rootPathFormat": PathFormatType,
    },
)
_OptionalManifestPropertiesTypeDef = TypedDict(
    "_OptionalManifestPropertiesTypeDef",
    {
        "fileSystemLocationName": str,
        "inputManifestHash": str,
        "inputManifestPath": str,
        "outputRelativeDirectories": List[str],
    },
    total=False,
)

class ManifestPropertiesTypeDef(
    _RequiredManifestPropertiesTypeDef, _OptionalManifestPropertiesTypeDef
):
    pass

_RequiredMemoryMiBRangeTypeDef = TypedDict(
    "_RequiredMemoryMiBRangeTypeDef",
    {
        "min": int,
    },
)
_OptionalMemoryMiBRangeTypeDef = TypedDict(
    "_OptionalMemoryMiBRangeTypeDef",
    {
        "max": int,
    },
    total=False,
)

class MemoryMiBRangeTypeDef(_RequiredMemoryMiBRangeTypeDef, _OptionalMemoryMiBRangeTypeDef):
    pass

MeteredProductSummaryTypeDef = TypedDict(
    "MeteredProductSummaryTypeDef",
    {
        "family": str,
        "port": int,
        "productId": str,
        "vendor": str,
    },
)

_RequiredMonitorSummaryTypeDef = TypedDict(
    "_RequiredMonitorSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "displayName": str,
        "identityCenterApplicationArn": str,
        "identityCenterInstanceArn": str,
        "monitorId": str,
        "roleArn": str,
        "subdomain": str,
        "url": str,
    },
)
_OptionalMonitorSummaryTypeDef = TypedDict(
    "_OptionalMonitorSummaryTypeDef",
    {
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

class MonitorSummaryTypeDef(_RequiredMonitorSummaryTypeDef, _OptionalMonitorSummaryTypeDef):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ParameterFilterExpressionTypeDef = TypedDict(
    "ParameterFilterExpressionTypeDef",
    {
        "name": str,
        "operator": ComparisonOperatorType,
        "value": str,
    },
)

ParameterSortExpressionTypeDef = TypedDict(
    "ParameterSortExpressionTypeDef",
    {
        "name": str,
        "sortOrder": SortOrderType,
    },
)

_RequiredParameterSpaceTypeDef = TypedDict(
    "_RequiredParameterSpaceTypeDef",
    {
        "parameters": List["StepParameterTypeDef"],
    },
)
_OptionalParameterSpaceTypeDef = TypedDict(
    "_OptionalParameterSpaceTypeDef",
    {
        "combination": str,
    },
    total=False,
)

class ParameterSpaceTypeDef(_RequiredParameterSpaceTypeDef, _OptionalParameterSpaceTypeDef):
    pass

PathMappingRuleTypeDef = TypedDict(
    "PathMappingRuleTypeDef",
    {
        "destinationPath": str,
        "sourcePath": str,
        "sourcePathFormat": PathFormatType,
    },
)

PosixUserTypeDef = TypedDict(
    "PosixUserTypeDef",
    {
        "group": str,
        "user": str,
    },
)

PutMeteredProductRequestRequestTypeDef = TypedDict(
    "PutMeteredProductRequestRequestTypeDef",
    {
        "licenseEndpointId": str,
        "productId": str,
    },
)

QueueEnvironmentSummaryTypeDef = TypedDict(
    "QueueEnvironmentSummaryTypeDef",
    {
        "name": str,
        "priority": int,
        "queueEnvironmentId": str,
    },
)

_RequiredQueueFleetAssociationSummaryTypeDef = TypedDict(
    "_RequiredQueueFleetAssociationSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "fleetId": str,
        "queueId": str,
        "status": QueueFleetAssociationStatusType,
    },
)
_OptionalQueueFleetAssociationSummaryTypeDef = TypedDict(
    "_OptionalQueueFleetAssociationSummaryTypeDef",
    {
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

class QueueFleetAssociationSummaryTypeDef(
    _RequiredQueueFleetAssociationSummaryTypeDef, _OptionalQueueFleetAssociationSummaryTypeDef
):
    pass

QueueMemberTypeDef = TypedDict(
    "QueueMemberTypeDef",
    {
        "farmId": str,
        "identityStoreId": str,
        "membershipLevel": MembershipLevelType,
        "principalId": str,
        "principalType": PrincipalTypeType,
        "queueId": str,
    },
)

_RequiredQueueSummaryTypeDef = TypedDict(
    "_RequiredQueueSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "defaultBudgetAction": DefaultQueueBudgetActionType,
        "displayName": str,
        "farmId": str,
        "queueId": str,
        "status": QueueStatusType,
    },
)
_OptionalQueueSummaryTypeDef = TypedDict(
    "_OptionalQueueSummaryTypeDef",
    {
        "blockedReason": QueueBlockedReasonType,
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

class QueueSummaryTypeDef(_RequiredQueueSummaryTypeDef, _OptionalQueueSummaryTypeDef):
    pass

_RequiredResponseBudgetActionTypeDef = TypedDict(
    "_RequiredResponseBudgetActionTypeDef",
    {
        "thresholdPercentage": float,
        "type": BudgetActionTypeType,
    },
)
_OptionalResponseBudgetActionTypeDef = TypedDict(
    "_OptionalResponseBudgetActionTypeDef",
    {
        "description": str,
    },
    total=False,
)

class ResponseBudgetActionTypeDef(
    _RequiredResponseBudgetActionTypeDef, _OptionalResponseBudgetActionTypeDef
):
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

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucketName": str,
        "key": str,
    },
)

SearchFilterExpressionTypeDef = TypedDict(
    "SearchFilterExpressionTypeDef",
    {
        "dateTimeFilter": "DateTimeFilterExpressionTypeDef",
        "groupFilter": Dict[str, Any],
        "parameterFilter": "ParameterFilterExpressionTypeDef",
        "searchTermFilter": "SearchTermFilterExpressionTypeDef",
        "stringFilter": "StringFilterExpressionTypeDef",
    },
    total=False,
)

SearchGroupedFilterExpressionsTypeDef = TypedDict(
    "SearchGroupedFilterExpressionsTypeDef",
    {
        "filters": List[Dict[str, Any]],
        "operator": LogicalOperatorType,
    },
)

_RequiredSearchJobsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchJobsRequestRequestTypeDef",
    {
        "farmId": str,
        "itemOffset": int,
        "queueIds": List[str],
    },
)
_OptionalSearchJobsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchJobsRequestRequestTypeDef",
    {
        "filterExpressions": "SearchGroupedFilterExpressionsTypeDef",
        "pageSize": int,
        "sortExpressions": List["SearchSortExpressionTypeDef"],
    },
    total=False,
)

class SearchJobsRequestRequestTypeDef(
    _RequiredSearchJobsRequestRequestTypeDef, _OptionalSearchJobsRequestRequestTypeDef
):
    pass

SearchJobsResponseTypeDef = TypedDict(
    "SearchJobsResponseTypeDef",
    {
        "jobs": List["JobSearchSummaryTypeDef"],
        "nextItemOffset": int,
        "totalResults": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchSortExpressionTypeDef = TypedDict(
    "SearchSortExpressionTypeDef",
    {
        "fieldSort": "FieldSortExpressionTypeDef",
        "parameterSort": "ParameterSortExpressionTypeDef",
        "userJobsFirst": "UserJobsFirstTypeDef",
    },
    total=False,
)

_RequiredSearchStepsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchStepsRequestRequestTypeDef",
    {
        "farmId": str,
        "itemOffset": int,
        "queueIds": List[str],
    },
)
_OptionalSearchStepsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchStepsRequestRequestTypeDef",
    {
        "filterExpressions": "SearchGroupedFilterExpressionsTypeDef",
        "jobId": str,
        "pageSize": int,
        "sortExpressions": List["SearchSortExpressionTypeDef"],
    },
    total=False,
)

class SearchStepsRequestRequestTypeDef(
    _RequiredSearchStepsRequestRequestTypeDef, _OptionalSearchStepsRequestRequestTypeDef
):
    pass

SearchStepsResponseTypeDef = TypedDict(
    "SearchStepsResponseTypeDef",
    {
        "nextItemOffset": int,
        "steps": List["StepSearchSummaryTypeDef"],
        "totalResults": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchTasksRequestRequestTypeDef = TypedDict(
    "_RequiredSearchTasksRequestRequestTypeDef",
    {
        "farmId": str,
        "itemOffset": int,
        "queueIds": List[str],
    },
)
_OptionalSearchTasksRequestRequestTypeDef = TypedDict(
    "_OptionalSearchTasksRequestRequestTypeDef",
    {
        "filterExpressions": "SearchGroupedFilterExpressionsTypeDef",
        "jobId": str,
        "pageSize": int,
        "sortExpressions": List["SearchSortExpressionTypeDef"],
    },
    total=False,
)

class SearchTasksRequestRequestTypeDef(
    _RequiredSearchTasksRequestRequestTypeDef, _OptionalSearchTasksRequestRequestTypeDef
):
    pass

SearchTasksResponseTypeDef = TypedDict(
    "SearchTasksResponseTypeDef",
    {
        "nextItemOffset": int,
        "tasks": List["TaskSearchSummaryTypeDef"],
        "totalResults": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchTermFilterExpressionTypeDef = TypedDict(
    "SearchTermFilterExpressionTypeDef",
    {
        "searchTerm": str,
    },
)

_RequiredSearchWorkersRequestRequestTypeDef = TypedDict(
    "_RequiredSearchWorkersRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetIds": List[str],
        "itemOffset": int,
    },
)
_OptionalSearchWorkersRequestRequestTypeDef = TypedDict(
    "_OptionalSearchWorkersRequestRequestTypeDef",
    {
        "filterExpressions": "SearchGroupedFilterExpressionsTypeDef",
        "pageSize": int,
        "sortExpressions": List["SearchSortExpressionTypeDef"],
    },
    total=False,
)

class SearchWorkersRequestRequestTypeDef(
    _RequiredSearchWorkersRequestRequestTypeDef, _OptionalSearchWorkersRequestRequestTypeDef
):
    pass

SearchWorkersResponseTypeDef = TypedDict(
    "SearchWorkersResponseTypeDef",
    {
        "nextItemOffset": int,
        "totalResults": int,
        "workers": List["WorkerSearchSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceManagedEc2FleetConfigurationTypeDef = TypedDict(
    "ServiceManagedEc2FleetConfigurationTypeDef",
    {
        "instanceCapabilities": "ServiceManagedEc2InstanceCapabilitiesTypeDef",
        "instanceMarketOptions": "ServiceManagedEc2InstanceMarketOptionsTypeDef",
    },
)

_RequiredServiceManagedEc2InstanceCapabilitiesTypeDef = TypedDict(
    "_RequiredServiceManagedEc2InstanceCapabilitiesTypeDef",
    {
        "cpuArchitectureType": CpuArchitectureTypeType,
        "memoryMiB": "MemoryMiBRangeTypeDef",
        "osFamily": ServiceManagedFleetOperatingSystemFamilyType,
        "vCpuCount": "VCpuCountRangeTypeDef",
    },
)
_OptionalServiceManagedEc2InstanceCapabilitiesTypeDef = TypedDict(
    "_OptionalServiceManagedEc2InstanceCapabilitiesTypeDef",
    {
        "allowedInstanceTypes": List[str],
        "customAmounts": List["FleetAmountCapabilityTypeDef"],
        "customAttributes": List["FleetAttributeCapabilityTypeDef"],
        "excludedInstanceTypes": List[str],
        "rootEbsVolume": "Ec2EbsVolumeTypeDef",
    },
    total=False,
)

class ServiceManagedEc2InstanceCapabilitiesTypeDef(
    _RequiredServiceManagedEc2InstanceCapabilitiesTypeDef,
    _OptionalServiceManagedEc2InstanceCapabilitiesTypeDef,
):
    pass

ServiceManagedEc2InstanceMarketOptionsTypeDef = TypedDict(
    "ServiceManagedEc2InstanceMarketOptionsTypeDef",
    {
        "type": Ec2MarketTypeType,
    },
)

SessionActionDefinitionSummaryTypeDef = TypedDict(
    "SessionActionDefinitionSummaryTypeDef",
    {
        "envEnter": "EnvironmentEnterSessionActionDefinitionSummaryTypeDef",
        "envExit": "EnvironmentExitSessionActionDefinitionSummaryTypeDef",
        "syncInputJobAttachments": "SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef",
        "taskRun": "TaskRunSessionActionDefinitionSummaryTypeDef",
    },
    total=False,
)

SessionActionDefinitionTypeDef = TypedDict(
    "SessionActionDefinitionTypeDef",
    {
        "envEnter": "EnvironmentEnterSessionActionDefinitionTypeDef",
        "envExit": "EnvironmentExitSessionActionDefinitionTypeDef",
        "syncInputJobAttachments": "SyncInputJobAttachmentsSessionActionDefinitionTypeDef",
        "taskRun": "TaskRunSessionActionDefinitionTypeDef",
    },
    total=False,
)

_RequiredSessionActionSummaryTypeDef = TypedDict(
    "_RequiredSessionActionSummaryTypeDef",
    {
        "definition": "SessionActionDefinitionSummaryTypeDef",
        "sessionActionId": str,
        "status": SessionActionStatusType,
    },
)
_OptionalSessionActionSummaryTypeDef = TypedDict(
    "_OptionalSessionActionSummaryTypeDef",
    {
        "endedAt": datetime,
        "progressPercent": float,
        "startedAt": datetime,
        "workerUpdatedAt": datetime,
    },
    total=False,
)

class SessionActionSummaryTypeDef(
    _RequiredSessionActionSummaryTypeDef, _OptionalSessionActionSummaryTypeDef
):
    pass

_RequiredSessionSummaryTypeDef = TypedDict(
    "_RequiredSessionSummaryTypeDef",
    {
        "fleetId": str,
        "lifecycleStatus": SessionLifecycleStatusType,
        "sessionId": str,
        "startedAt": datetime,
        "workerId": str,
    },
)
_OptionalSessionSummaryTypeDef = TypedDict(
    "_OptionalSessionSummaryTypeDef",
    {
        "endedAt": datetime,
        "targetLifecycleStatus": Literal["ENDED"],
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

class SessionSummaryTypeDef(_RequiredSessionSummaryTypeDef, _OptionalSessionSummaryTypeDef):
    pass

SessionsStatisticsResourcesTypeDef = TypedDict(
    "SessionsStatisticsResourcesTypeDef",
    {
        "fleetIds": List[str],
        "queueIds": List[str],
    },
    total=False,
)

_RequiredStartSessionsStatisticsAggregationRequestRequestTypeDef = TypedDict(
    "_RequiredStartSessionsStatisticsAggregationRequestRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "farmId": str,
        "groupBy": List[UsageGroupByFieldType],
        "resourceIds": "SessionsStatisticsResourcesTypeDef",
        "startTime": Union[datetime, str],
        "statistics": List[UsageStatisticType],
    },
)
_OptionalStartSessionsStatisticsAggregationRequestRequestTypeDef = TypedDict(
    "_OptionalStartSessionsStatisticsAggregationRequestRequestTypeDef",
    {
        "period": PeriodType,
        "timezone": str,
    },
    total=False,
)

class StartSessionsStatisticsAggregationRequestRequestTypeDef(
    _RequiredStartSessionsStatisticsAggregationRequestRequestTypeDef,
    _OptionalStartSessionsStatisticsAggregationRequestRequestTypeDef,
):
    pass

StartSessionsStatisticsAggregationResponseTypeDef = TypedDict(
    "StartSessionsStatisticsAggregationResponseTypeDef",
    {
        "aggregationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStatisticsTypeDef = TypedDict(
    "_RequiredStatisticsTypeDef",
    {
        "costInUsd": "StatsTypeDef",
        "count": int,
        "runtimeInSeconds": "StatsTypeDef",
    },
)
_OptionalStatisticsTypeDef = TypedDict(
    "_OptionalStatisticsTypeDef",
    {
        "aggregationEndTime": datetime,
        "aggregationStartTime": datetime,
        "fleetId": str,
        "instanceType": str,
        "jobId": str,
        "jobName": str,
        "licenseProduct": str,
        "queueId": str,
        "usageType": UsageTypeType,
        "userId": str,
    },
    total=False,
)

class StatisticsTypeDef(_RequiredStatisticsTypeDef, _OptionalStatisticsTypeDef):
    pass

StatsTypeDef = TypedDict(
    "StatsTypeDef",
    {
        "avg": float,
        "max": float,
        "min": float,
        "sum": float,
    },
    total=False,
)

_RequiredStepAmountCapabilityTypeDef = TypedDict(
    "_RequiredStepAmountCapabilityTypeDef",
    {
        "name": str,
    },
)
_OptionalStepAmountCapabilityTypeDef = TypedDict(
    "_OptionalStepAmountCapabilityTypeDef",
    {
        "max": float,
        "min": float,
        "value": float,
    },
    total=False,
)

class StepAmountCapabilityTypeDef(
    _RequiredStepAmountCapabilityTypeDef, _OptionalStepAmountCapabilityTypeDef
):
    pass

_RequiredStepAttributeCapabilityTypeDef = TypedDict(
    "_RequiredStepAttributeCapabilityTypeDef",
    {
        "name": str,
    },
)
_OptionalStepAttributeCapabilityTypeDef = TypedDict(
    "_OptionalStepAttributeCapabilityTypeDef",
    {
        "allOf": List[str],
        "anyOf": List[str],
    },
    total=False,
)

class StepAttributeCapabilityTypeDef(
    _RequiredStepAttributeCapabilityTypeDef, _OptionalStepAttributeCapabilityTypeDef
):
    pass

StepConsumerTypeDef = TypedDict(
    "StepConsumerTypeDef",
    {
        "status": DependencyConsumerResolutionStatusType,
        "stepId": str,
    },
)

StepDependencyTypeDef = TypedDict(
    "StepDependencyTypeDef",
    {
        "status": DependencyConsumerResolutionStatusType,
        "stepId": str,
    },
)

StepDetailsEntityTypeDef = TypedDict(
    "StepDetailsEntityTypeDef",
    {
        "dependencies": List[str],
        "jobId": str,
        "schemaVersion": str,
        "stepId": str,
        "template": Dict[str, Any],
    },
)

StepDetailsErrorTypeDef = TypedDict(
    "StepDetailsErrorTypeDef",
    {
        "code": JobEntityErrorCodeType,
        "jobId": str,
        "message": str,
        "stepId": str,
    },
)

StepDetailsIdentifiersTypeDef = TypedDict(
    "StepDetailsIdentifiersTypeDef",
    {
        "jobId": str,
        "stepId": str,
    },
)

StepParameterTypeDef = TypedDict(
    "StepParameterTypeDef",
    {
        "name": str,
        "type": StepParameterTypeType,
    },
)

StepRequiredCapabilitiesTypeDef = TypedDict(
    "StepRequiredCapabilitiesTypeDef",
    {
        "amounts": List["StepAmountCapabilityTypeDef"],
        "attributes": List["StepAttributeCapabilityTypeDef"],
    },
)

StepSearchSummaryTypeDef = TypedDict(
    "StepSearchSummaryTypeDef",
    {
        "createdAt": datetime,
        "endedAt": datetime,
        "jobId": str,
        "lifecycleStatus": StepLifecycleStatusType,
        "lifecycleStatusMessage": str,
        "name": str,
        "parameterSpace": "ParameterSpaceTypeDef",
        "queueId": str,
        "startedAt": datetime,
        "stepId": str,
        "targetTaskRunStatus": StepTargetTaskRunStatusType,
        "taskRunStatus": TaskRunStatusType,
        "taskRunStatusCounts": Dict[TaskRunStatusType, int],
    },
    total=False,
)

_RequiredStepSummaryTypeDef = TypedDict(
    "_RequiredStepSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "lifecycleStatus": StepLifecycleStatusType,
        "name": str,
        "stepId": str,
        "taskRunStatus": TaskRunStatusType,
        "taskRunStatusCounts": Dict[TaskRunStatusType, int],
    },
)
_OptionalStepSummaryTypeDef = TypedDict(
    "_OptionalStepSummaryTypeDef",
    {
        "dependencyCounts": "DependencyCountsTypeDef",
        "endedAt": datetime,
        "lifecycleStatusMessage": str,
        "startedAt": datetime,
        "targetTaskRunStatus": StepTargetTaskRunStatusType,
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

class StepSummaryTypeDef(_RequiredStepSummaryTypeDef, _OptionalStepSummaryTypeDef):
    pass

StorageProfileSummaryTypeDef = TypedDict(
    "StorageProfileSummaryTypeDef",
    {
        "displayName": str,
        "osFamily": StorageProfileOperatingSystemFamilyType,
        "storageProfileId": str,
    },
)

StringFilterExpressionTypeDef = TypedDict(
    "StringFilterExpressionTypeDef",
    {
        "name": str,
        "operator": ComparisonOperatorType,
        "value": str,
    },
)

SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef = TypedDict(
    "SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef",
    {
        "stepId": str,
    },
    total=False,
)

SyncInputJobAttachmentsSessionActionDefinitionTypeDef = TypedDict(
    "SyncInputJobAttachmentsSessionActionDefinitionTypeDef",
    {
        "stepId": str,
    },
    total=False,
)

_RequiredTagResourceRequestRequestTypeDef = TypedDict(
    "_RequiredTagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalTagResourceRequestRequestTypeDef = TypedDict(
    "_OptionalTagResourceRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class TagResourceRequestRequestTypeDef(
    _RequiredTagResourceRequestRequestTypeDef, _OptionalTagResourceRequestRequestTypeDef
):
    pass

TaskParameterValueTypeDef = TypedDict(
    "TaskParameterValueTypeDef",
    {
        "float": str,
        "int": str,
        "path": str,
        "string": str,
    },
    total=False,
)

TaskRunSessionActionDefinitionSummaryTypeDef = TypedDict(
    "TaskRunSessionActionDefinitionSummaryTypeDef",
    {
        "stepId": str,
        "taskId": str,
    },
)

TaskRunSessionActionDefinitionTypeDef = TypedDict(
    "TaskRunSessionActionDefinitionTypeDef",
    {
        "parameters": Dict[str, "TaskParameterValueTypeDef"],
        "stepId": str,
        "taskId": str,
    },
)

TaskSearchSummaryTypeDef = TypedDict(
    "TaskSearchSummaryTypeDef",
    {
        "endedAt": datetime,
        "failureRetryCount": int,
        "jobId": str,
        "parameters": Dict[str, "TaskParameterValueTypeDef"],
        "queueId": str,
        "runStatus": TaskRunStatusType,
        "startedAt": datetime,
        "stepId": str,
        "targetRunStatus": TaskTargetRunStatusType,
        "taskId": str,
    },
    total=False,
)

_RequiredTaskSummaryTypeDef = TypedDict(
    "_RequiredTaskSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "runStatus": TaskRunStatusType,
        "taskId": str,
    },
)
_OptionalTaskSummaryTypeDef = TypedDict(
    "_OptionalTaskSummaryTypeDef",
    {
        "endedAt": datetime,
        "failureRetryCount": int,
        "latestSessionActionId": str,
        "parameters": Dict[str, "TaskParameterValueTypeDef"],
        "startedAt": datetime,
        "targetRunStatus": TaskTargetRunStatusType,
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

class TaskSummaryTypeDef(_RequiredTaskSummaryTypeDef, _OptionalTaskSummaryTypeDef):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateBudgetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBudgetRequestRequestTypeDef",
    {
        "budgetId": str,
        "farmId": str,
    },
)
_OptionalUpdateBudgetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBudgetRequestRequestTypeDef",
    {
        "actionsToAdd": List["BudgetActionToAddTypeDef"],
        "actionsToRemove": List["BudgetActionToRemoveTypeDef"],
        "approximateDollarLimit": float,
        "clientToken": str,
        "description": str,
        "displayName": str,
        "schedule": "BudgetScheduleTypeDef",
        "status": BudgetStatusType,
    },
    total=False,
)

class UpdateBudgetRequestRequestTypeDef(
    _RequiredUpdateBudgetRequestRequestTypeDef, _OptionalUpdateBudgetRequestRequestTypeDef
):
    pass

_RequiredUpdateFarmRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFarmRequestRequestTypeDef",
    {
        "farmId": str,
    },
)
_OptionalUpdateFarmRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFarmRequestRequestTypeDef",
    {
        "description": str,
        "displayName": str,
    },
    total=False,
)

class UpdateFarmRequestRequestTypeDef(
    _RequiredUpdateFarmRequestRequestTypeDef, _OptionalUpdateFarmRequestRequestTypeDef
):
    pass

_RequiredUpdateFleetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFleetRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
    },
)
_OptionalUpdateFleetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFleetRequestRequestTypeDef",
    {
        "clientToken": str,
        "configuration": "FleetConfigurationTypeDef",
        "description": str,
        "displayName": str,
        "maxWorkerCount": int,
        "minWorkerCount": int,
        "roleArn": str,
    },
    total=False,
)

class UpdateFleetRequestRequestTypeDef(
    _RequiredUpdateFleetRequestRequestTypeDef, _OptionalUpdateFleetRequestRequestTypeDef
):
    pass

_RequiredUpdateJobRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateJobRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
    },
)
_OptionalUpdateJobRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateJobRequestRequestTypeDef",
    {
        "clientToken": str,
        "lifecycleStatus": Literal["ARCHIVED"],
        "maxFailedTasksCount": int,
        "maxRetriesPerTask": int,
        "priority": int,
        "targetTaskRunStatus": JobTargetTaskRunStatusType,
    },
    total=False,
)

class UpdateJobRequestRequestTypeDef(
    _RequiredUpdateJobRequestRequestTypeDef, _OptionalUpdateJobRequestRequestTypeDef
):
    pass

_RequiredUpdateMonitorRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMonitorRequestRequestTypeDef",
    {
        "monitorId": str,
    },
)
_OptionalUpdateMonitorRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMonitorRequestRequestTypeDef",
    {
        "displayName": str,
        "roleArn": str,
        "subdomain": str,
    },
    total=False,
)

class UpdateMonitorRequestRequestTypeDef(
    _RequiredUpdateMonitorRequestRequestTypeDef, _OptionalUpdateMonitorRequestRequestTypeDef
):
    pass

_RequiredUpdateQueueEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateQueueEnvironmentRequestRequestTypeDef",
    {
        "farmId": str,
        "queueEnvironmentId": str,
        "queueId": str,
    },
)
_OptionalUpdateQueueEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateQueueEnvironmentRequestRequestTypeDef",
    {
        "clientToken": str,
        "priority": int,
        "template": str,
        "templateType": EnvironmentTemplateTypeType,
    },
    total=False,
)

class UpdateQueueEnvironmentRequestRequestTypeDef(
    _RequiredUpdateQueueEnvironmentRequestRequestTypeDef,
    _OptionalUpdateQueueEnvironmentRequestRequestTypeDef,
):
    pass

UpdateQueueFleetAssociationRequestRequestTypeDef = TypedDict(
    "UpdateQueueFleetAssociationRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "queueId": str,
        "status": UpdateQueueFleetAssociationStatusType,
    },
)

_RequiredUpdateQueueRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateQueueRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
    },
)
_OptionalUpdateQueueRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateQueueRequestRequestTypeDef",
    {
        "allowedStorageProfileIdsToAdd": List[str],
        "allowedStorageProfileIdsToRemove": List[str],
        "clientToken": str,
        "defaultBudgetAction": DefaultQueueBudgetActionType,
        "description": str,
        "displayName": str,
        "jobAttachmentSettings": "JobAttachmentSettingsTypeDef",
        "jobRunAsUser": "JobRunAsUserTypeDef",
        "requiredFileSystemLocationNamesToAdd": List[str],
        "requiredFileSystemLocationNamesToRemove": List[str],
        "roleArn": str,
    },
    total=False,
)

class UpdateQueueRequestRequestTypeDef(
    _RequiredUpdateQueueRequestRequestTypeDef, _OptionalUpdateQueueRequestRequestTypeDef
):
    pass

_RequiredUpdateSessionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSessionRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
        "sessionId": str,
        "targetLifecycleStatus": Literal["ENDED"],
    },
)
_OptionalUpdateSessionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSessionRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateSessionRequestRequestTypeDef(
    _RequiredUpdateSessionRequestRequestTypeDef, _OptionalUpdateSessionRequestRequestTypeDef
):
    pass

_RequiredUpdateStepRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStepRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
        "stepId": str,
        "targetTaskRunStatus": StepTargetTaskRunStatusType,
    },
)
_OptionalUpdateStepRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStepRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateStepRequestRequestTypeDef(
    _RequiredUpdateStepRequestRequestTypeDef, _OptionalUpdateStepRequestRequestTypeDef
):
    pass

_RequiredUpdateStorageProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStorageProfileRequestRequestTypeDef",
    {
        "farmId": str,
        "storageProfileId": str,
    },
)
_OptionalUpdateStorageProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStorageProfileRequestRequestTypeDef",
    {
        "clientToken": str,
        "displayName": str,
        "fileSystemLocationsToAdd": List["FileSystemLocationTypeDef"],
        "fileSystemLocationsToRemove": List["FileSystemLocationTypeDef"],
        "osFamily": StorageProfileOperatingSystemFamilyType,
    },
    total=False,
)

class UpdateStorageProfileRequestRequestTypeDef(
    _RequiredUpdateStorageProfileRequestRequestTypeDef,
    _OptionalUpdateStorageProfileRequestRequestTypeDef,
):
    pass

_RequiredUpdateTaskRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTaskRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
        "stepId": str,
        "targetRunStatus": TaskTargetRunStatusType,
        "taskId": str,
    },
)
_OptionalUpdateTaskRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTaskRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateTaskRequestRequestTypeDef(
    _RequiredUpdateTaskRequestRequestTypeDef, _OptionalUpdateTaskRequestRequestTypeDef
):
    pass

_RequiredUpdateWorkerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkerRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "workerId": str,
    },
)
_OptionalUpdateWorkerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkerRequestRequestTypeDef",
    {
        "capabilities": "WorkerCapabilitiesTypeDef",
        "hostProperties": "HostPropertiesRequestTypeDef",
        "status": UpdatedWorkerStatusType,
    },
    total=False,
)

class UpdateWorkerRequestRequestTypeDef(
    _RequiredUpdateWorkerRequestRequestTypeDef, _OptionalUpdateWorkerRequestRequestTypeDef
):
    pass

UpdateWorkerResponseTypeDef = TypedDict(
    "UpdateWorkerResponseTypeDef",
    {
        "log": "LogConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWorkerScheduleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkerScheduleRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "workerId": str,
    },
)
_OptionalUpdateWorkerScheduleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkerScheduleRequestRequestTypeDef",
    {
        "updatedSessionActions": Dict[str, "UpdatedSessionActionInfoTypeDef"],
    },
    total=False,
)

class UpdateWorkerScheduleRequestRequestTypeDef(
    _RequiredUpdateWorkerScheduleRequestRequestTypeDef,
    _OptionalUpdateWorkerScheduleRequestRequestTypeDef,
):
    pass

UpdateWorkerScheduleResponseTypeDef = TypedDict(
    "UpdateWorkerScheduleResponseTypeDef",
    {
        "assignedSessions": Dict[str, "AssignedSessionTypeDef"],
        "cancelSessionActions": Dict[str, List[str]],
        "desiredWorkerStatus": Literal["STOPPED"],
        "updateIntervalSeconds": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatedSessionActionInfoTypeDef = TypedDict(
    "UpdatedSessionActionInfoTypeDef",
    {
        "completedStatus": CompletedStatusType,
        "endedAt": Union[datetime, str],
        "processExitCode": int,
        "progressMessage": str,
        "progressPercent": float,
        "startedAt": Union[datetime, str],
        "updatedAt": Union[datetime, str],
    },
    total=False,
)

UsageTrackingResourceTypeDef = TypedDict(
    "UsageTrackingResourceTypeDef",
    {
        "queueId": str,
    },
    total=False,
)

UserJobsFirstTypeDef = TypedDict(
    "UserJobsFirstTypeDef",
    {
        "userIdentityId": str,
    },
)

_RequiredVCpuCountRangeTypeDef = TypedDict(
    "_RequiredVCpuCountRangeTypeDef",
    {
        "min": int,
    },
)
_OptionalVCpuCountRangeTypeDef = TypedDict(
    "_OptionalVCpuCountRangeTypeDef",
    {
        "max": int,
    },
    total=False,
)

class VCpuCountRangeTypeDef(_RequiredVCpuCountRangeTypeDef, _OptionalVCpuCountRangeTypeDef):
    pass

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

WindowsUserTypeDef = TypedDict(
    "WindowsUserTypeDef",
    {
        "passwordArn": str,
        "user": str,
    },
)

WorkerAmountCapabilityTypeDef = TypedDict(
    "WorkerAmountCapabilityTypeDef",
    {
        "name": str,
        "value": float,
    },
)

WorkerAttributeCapabilityTypeDef = TypedDict(
    "WorkerAttributeCapabilityTypeDef",
    {
        "name": str,
        "values": List[str],
    },
)

WorkerCapabilitiesTypeDef = TypedDict(
    "WorkerCapabilitiesTypeDef",
    {
        "amounts": List["WorkerAmountCapabilityTypeDef"],
        "attributes": List["WorkerAttributeCapabilityTypeDef"],
    },
)

WorkerSearchSummaryTypeDef = TypedDict(
    "WorkerSearchSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "fleetId": str,
        "hostProperties": "HostPropertiesResponseTypeDef",
        "status": WorkerStatusType,
        "updatedAt": datetime,
        "updatedBy": str,
        "workerId": str,
    },
    total=False,
)

_RequiredWorkerSessionSummaryTypeDef = TypedDict(
    "_RequiredWorkerSessionSummaryTypeDef",
    {
        "jobId": str,
        "lifecycleStatus": SessionLifecycleStatusType,
        "queueId": str,
        "sessionId": str,
        "startedAt": datetime,
    },
)
_OptionalWorkerSessionSummaryTypeDef = TypedDict(
    "_OptionalWorkerSessionSummaryTypeDef",
    {
        "endedAt": datetime,
        "targetLifecycleStatus": Literal["ENDED"],
    },
    total=False,
)

class WorkerSessionSummaryTypeDef(
    _RequiredWorkerSessionSummaryTypeDef, _OptionalWorkerSessionSummaryTypeDef
):
    pass

_RequiredWorkerSummaryTypeDef = TypedDict(
    "_RequiredWorkerSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "farmId": str,
        "fleetId": str,
        "status": WorkerStatusType,
        "workerId": str,
    },
)
_OptionalWorkerSummaryTypeDef = TypedDict(
    "_OptionalWorkerSummaryTypeDef",
    {
        "hostProperties": "HostPropertiesResponseTypeDef",
        "log": "LogConfigurationTypeDef",
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

class WorkerSummaryTypeDef(_RequiredWorkerSummaryTypeDef, _OptionalWorkerSummaryTypeDef):
    pass
