"""
Type annotations for deadline service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/literals.html)

Usage::

    ```python
    from mypy_boto3_deadline.literals import AcceleratorTypeType

    data: AcceleratorTypeType = "gpu"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AcceleratorTypeType",
    "AutoScalingModeType",
    "AutoScalingStatusType",
    "BudgetActionTypeType",
    "BudgetStatusType",
    "ComparisonOperatorType",
    "CompletedStatusType",
    "CpuArchitectureTypeType",
    "CreateJobTargetTaskRunStatusType",
    "CustomerManagedFleetOperatingSystemFamilyType",
    "DefaultQueueBudgetActionType",
    "DependencyConsumerResolutionStatusType",
    "DesiredWorkerStatusType",
    "Ec2MarketTypeType",
    "EnvironmentTemplateTypeType",
    "FileSystemLocationTypeType",
    "FleetActiveWaiterName",
    "FleetStatusType",
    "GetSessionsStatisticsAggregationPaginatorName",
    "JobAttachmentsFileSystemType",
    "JobCreateCompleteWaiterName",
    "JobEntityErrorCodeType",
    "JobLifecycleStatusType",
    "JobTargetTaskRunStatusType",
    "JobTemplateTypeType",
    "LicenseEndpointDeletedWaiterName",
    "LicenseEndpointStatusType",
    "LicenseEndpointValidWaiterName",
    "ListAvailableMeteredProductsPaginatorName",
    "ListBudgetsPaginatorName",
    "ListFarmMembersPaginatorName",
    "ListFarmsPaginatorName",
    "ListFleetMembersPaginatorName",
    "ListFleetsPaginatorName",
    "ListJobMembersPaginatorName",
    "ListJobsPaginatorName",
    "ListLicenseEndpointsPaginatorName",
    "ListMeteredProductsPaginatorName",
    "ListMonitorsPaginatorName",
    "ListQueueEnvironmentsPaginatorName",
    "ListQueueFleetAssociationsPaginatorName",
    "ListQueueMembersPaginatorName",
    "ListQueuesPaginatorName",
    "ListSessionActionsPaginatorName",
    "ListSessionsForWorkerPaginatorName",
    "ListSessionsPaginatorName",
    "ListStepConsumersPaginatorName",
    "ListStepDependenciesPaginatorName",
    "ListStepsPaginatorName",
    "ListStorageProfilesForQueuePaginatorName",
    "ListStorageProfilesPaginatorName",
    "ListTasksPaginatorName",
    "ListWorkersPaginatorName",
    "LogicalOperatorType",
    "MembershipLevelType",
    "PathFormatType",
    "PeriodType",
    "PrincipalTypeType",
    "QueueBlockedReasonType",
    "QueueFleetAssociationStatusType",
    "QueueFleetAssociationStoppedWaiterName",
    "QueueSchedulingBlockedWaiterName",
    "QueueSchedulingWaiterName",
    "QueueStatusType",
    "RunAsType",
    "ServiceManagedFleetOperatingSystemFamilyType",
    "SessionActionStatusType",
    "SessionLifecycleStatusType",
    "SessionLifecycleTargetStatusType",
    "SessionsStatisticsAggregationStatusType",
    "SortOrderType",
    "StepLifecycleStatusType",
    "StepParameterTypeType",
    "StepTargetTaskRunStatusType",
    "StorageProfileOperatingSystemFamilyType",
    "TaskRunStatusType",
    "TaskTargetRunStatusType",
    "UpdateJobLifecycleStatusType",
    "UpdateQueueFleetAssociationStatusType",
    "UpdatedWorkerStatusType",
    "UsageGroupByFieldType",
    "UsageStatisticType",
    "UsageTypeType",
    "WorkerStatusType",
)

AcceleratorTypeType = Literal["gpu"]
AutoScalingModeType = Literal["EVENT_BASED_AUTO_SCALING", "NO_SCALING"]
AutoScalingStatusType = Literal["GROWING", "SHRINKING", "STEADY"]
BudgetActionTypeType = Literal[
    "STOP_SCHEDULING_AND_CANCEL_TASKS", "STOP_SCHEDULING_AND_COMPLETE_TASKS"
]
BudgetStatusType = Literal["ACTIVE", "INACTIVE"]
ComparisonOperatorType = Literal[
    "EQUAL", "GREATER_THAN", "GREATER_THAN_EQUAL_TO", "LESS_THAN", "LESS_THAN_EQUAL_TO", "NOT_EQUAL"
]
CompletedStatusType = Literal["CANCELED", "FAILED", "INTERRUPTED", "NEVER_ATTEMPTED", "SUCCEEDED"]
CpuArchitectureTypeType = Literal["arm64", "x86_64"]
CreateJobTargetTaskRunStatusType = Literal["READY", "SUSPENDED"]
CustomerManagedFleetOperatingSystemFamilyType = Literal["LINUX", "MACOS", "WINDOWS"]
DefaultQueueBudgetActionType = Literal[
    "NONE", "STOP_SCHEDULING_AND_CANCEL_TASKS", "STOP_SCHEDULING_AND_COMPLETE_TASKS"
]
DependencyConsumerResolutionStatusType = Literal["RESOLVED", "UNRESOLVED"]
DesiredWorkerStatusType = Literal["STOPPED"]
Ec2MarketTypeType = Literal["on-demand", "spot"]
EnvironmentTemplateTypeType = Literal["JSON", "YAML"]
FileSystemLocationTypeType = Literal["LOCAL", "SHARED"]
FleetActiveWaiterName = Literal["fleet_active"]
FleetStatusType = Literal[
    "ACTIVE", "CREATE_FAILED", "CREATE_IN_PROGRESS", "UPDATE_FAILED", "UPDATE_IN_PROGRESS"
]
GetSessionsStatisticsAggregationPaginatorName = Literal["get_sessions_statistics_aggregation"]
JobAttachmentsFileSystemType = Literal["COPIED", "VIRTUAL"]
JobCreateCompleteWaiterName = Literal["job_create_complete"]
JobEntityErrorCodeType = Literal[
    "AccessDeniedException",
    "ConflictException",
    "InternalServerException",
    "MaxPayloadSizeExceeded",
    "ResourceNotFoundException",
    "ValidationException",
]
JobLifecycleStatusType = Literal[
    "ARCHIVED",
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCEEDED",
    "UPLOAD_FAILED",
    "UPLOAD_IN_PROGRESS",
]
JobTargetTaskRunStatusType = Literal[
    "CANCELED", "FAILED", "PENDING", "READY", "SUCCEEDED", "SUSPENDED"
]
JobTemplateTypeType = Literal["JSON", "YAML"]
LicenseEndpointDeletedWaiterName = Literal["license_endpoint_deleted"]
LicenseEndpointStatusType = Literal[
    "CREATE_IN_PROGRESS", "DELETE_IN_PROGRESS", "NOT_READY", "READY"
]
LicenseEndpointValidWaiterName = Literal["license_endpoint_valid"]
ListAvailableMeteredProductsPaginatorName = Literal["list_available_metered_products"]
ListBudgetsPaginatorName = Literal["list_budgets"]
ListFarmMembersPaginatorName = Literal["list_farm_members"]
ListFarmsPaginatorName = Literal["list_farms"]
ListFleetMembersPaginatorName = Literal["list_fleet_members"]
ListFleetsPaginatorName = Literal["list_fleets"]
ListJobMembersPaginatorName = Literal["list_job_members"]
ListJobsPaginatorName = Literal["list_jobs"]
ListLicenseEndpointsPaginatorName = Literal["list_license_endpoints"]
ListMeteredProductsPaginatorName = Literal["list_metered_products"]
ListMonitorsPaginatorName = Literal["list_monitors"]
ListQueueEnvironmentsPaginatorName = Literal["list_queue_environments"]
ListQueueFleetAssociationsPaginatorName = Literal["list_queue_fleet_associations"]
ListQueueMembersPaginatorName = Literal["list_queue_members"]
ListQueuesPaginatorName = Literal["list_queues"]
ListSessionActionsPaginatorName = Literal["list_session_actions"]
ListSessionsForWorkerPaginatorName = Literal["list_sessions_for_worker"]
ListSessionsPaginatorName = Literal["list_sessions"]
ListStepConsumersPaginatorName = Literal["list_step_consumers"]
ListStepDependenciesPaginatorName = Literal["list_step_dependencies"]
ListStepsPaginatorName = Literal["list_steps"]
ListStorageProfilesForQueuePaginatorName = Literal["list_storage_profiles_for_queue"]
ListStorageProfilesPaginatorName = Literal["list_storage_profiles"]
ListTasksPaginatorName = Literal["list_tasks"]
ListWorkersPaginatorName = Literal["list_workers"]
LogicalOperatorType = Literal["AND", "OR"]
MembershipLevelType = Literal["CONTRIBUTOR", "MANAGER", "OWNER", "VIEWER"]
PathFormatType = Literal["posix", "windows"]
PeriodType = Literal["DAILY", "HOURLY", "MONTHLY", "WEEKLY"]
PrincipalTypeType = Literal["GROUP", "USER"]
QueueBlockedReasonType = Literal["BUDGET_THRESHOLD_REACHED", "NO_BUDGET_CONFIGURED"]
QueueFleetAssociationStatusType = Literal[
    "ACTIVE", "STOPPED", "STOP_SCHEDULING_AND_CANCEL_TASKS", "STOP_SCHEDULING_AND_COMPLETE_TASKS"
]
QueueFleetAssociationStoppedWaiterName = Literal["queue_fleet_association_stopped"]
QueueSchedulingBlockedWaiterName = Literal["queue_scheduling_blocked"]
QueueSchedulingWaiterName = Literal["queue_scheduling"]
QueueStatusType = Literal["IDLE", "SCHEDULING", "SCHEDULING_BLOCKED"]
RunAsType = Literal["QUEUE_CONFIGURED_USER", "WORKER_AGENT_USER"]
ServiceManagedFleetOperatingSystemFamilyType = Literal["LINUX", "WINDOWS"]
SessionActionStatusType = Literal[
    "ASSIGNED",
    "CANCELED",
    "CANCELING",
    "FAILED",
    "INTERRUPTED",
    "NEVER_ATTEMPTED",
    "RECLAIMED",
    "RECLAIMING",
    "RUNNING",
    "SCHEDULED",
    "SUCCEEDED",
]
SessionLifecycleStatusType = Literal[
    "ENDED", "STARTED", "UPDATE_FAILED", "UPDATE_IN_PROGRESS", "UPDATE_SUCCEEDED"
]
SessionLifecycleTargetStatusType = Literal["ENDED"]
SessionsStatisticsAggregationStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "TIMEOUT"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
StepLifecycleStatusType = Literal[
    "CREATE_COMPLETE", "UPDATE_FAILED", "UPDATE_IN_PROGRESS", "UPDATE_SUCCEEDED"
]
StepParameterTypeType = Literal["FLOAT", "INT", "PATH", "STRING"]
StepTargetTaskRunStatusType = Literal[
    "CANCELED", "FAILED", "PENDING", "READY", "SUCCEEDED", "SUSPENDED"
]
StorageProfileOperatingSystemFamilyType = Literal["LINUX", "MACOS", "WINDOWS"]
TaskRunStatusType = Literal[
    "ASSIGNED",
    "CANCELED",
    "FAILED",
    "INTERRUPTING",
    "NOT_COMPATIBLE",
    "PENDING",
    "READY",
    "RUNNING",
    "SCHEDULED",
    "STARTING",
    "SUCCEEDED",
    "SUSPENDED",
]
TaskTargetRunStatusType = Literal[
    "CANCELED", "FAILED", "PENDING", "READY", "SUCCEEDED", "SUSPENDED"
]
UpdateJobLifecycleStatusType = Literal["ARCHIVED"]
UpdateQueueFleetAssociationStatusType = Literal[
    "ACTIVE", "STOP_SCHEDULING_AND_CANCEL_TASKS", "STOP_SCHEDULING_AND_COMPLETE_TASKS"
]
UpdatedWorkerStatusType = Literal["STARTED", "STOPPED", "STOPPING"]
UsageGroupByFieldType = Literal[
    "FLEET_ID", "INSTANCE_TYPE", "JOB_ID", "LICENSE_PRODUCT", "QUEUE_ID", "USAGE_TYPE", "USER_ID"
]
UsageStatisticType = Literal["AVG", "MAX", "MIN", "SUM"]
UsageTypeType = Literal["COMPUTE", "LICENSE"]
WorkerStatusType = Literal[
    "CREATED",
    "IDLE",
    "NOT_COMPATIBLE",
    "NOT_RESPONDING",
    "RUNNING",
    "STARTED",
    "STOPPED",
    "STOPPING",
]
