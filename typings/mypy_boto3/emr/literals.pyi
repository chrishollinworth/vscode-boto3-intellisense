"""
Type annotations for emr service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/literals.html)

Usage::

    ```python
    from mypy_boto3_emr.literals import ActionOnFailureType

    data: ActionOnFailureType = "CANCEL_AND_WAIT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionOnFailureType",
    "AdjustmentTypeType",
    "AuthModeType",
    "AutoScalingPolicyStateChangeReasonCodeType",
    "AutoScalingPolicyStateType",
    "CancelStepsRequestStatusType",
    "ClusterRunningWaiterName",
    "ClusterStateChangeReasonCodeType",
    "ClusterStateType",
    "ClusterTerminatedWaiterName",
    "ComparisonOperatorType",
    "ComputeLimitsUnitTypeType",
    "ExecutionEngineTypeType",
    "IdentityTypeType",
    "InstanceCollectionTypeType",
    "InstanceFleetStateChangeReasonCodeType",
    "InstanceFleetStateType",
    "InstanceFleetTypeType",
    "InstanceGroupStateChangeReasonCodeType",
    "InstanceGroupStateType",
    "InstanceGroupTypeType",
    "InstanceRoleTypeType",
    "InstanceStateChangeReasonCodeType",
    "InstanceStateType",
    "JobFlowExecutionStateType",
    "ListBootstrapActionsPaginatorName",
    "ListClustersPaginatorName",
    "ListInstanceFleetsPaginatorName",
    "ListInstanceGroupsPaginatorName",
    "ListInstancesPaginatorName",
    "ListNotebookExecutionsPaginatorName",
    "ListSecurityConfigurationsPaginatorName",
    "ListStepsPaginatorName",
    "ListStudioSessionMappingsPaginatorName",
    "ListStudiosPaginatorName",
    "MarketTypeType",
    "NotebookExecutionStatusType",
    "OnDemandCapacityReservationPreferenceType",
    "OnDemandCapacityReservationUsageStrategyType",
    "OnDemandProvisioningAllocationStrategyType",
    "PlacementGroupStrategyType",
    "RepoUpgradeOnBootType",
    "ScaleDownBehaviorType",
    "SpotProvisioningAllocationStrategyType",
    "SpotProvisioningTimeoutActionType",
    "StatisticType",
    "StepCancellationOptionType",
    "StepCompleteWaiterName",
    "StepExecutionStateType",
    "StepStateChangeReasonCodeType",
    "StepStateType",
    "UnitType",
)

ActionOnFailureType = Literal[
    "CANCEL_AND_WAIT", "CONTINUE", "TERMINATE_CLUSTER", "TERMINATE_JOB_FLOW"
]
AdjustmentTypeType = Literal["CHANGE_IN_CAPACITY", "EXACT_CAPACITY", "PERCENT_CHANGE_IN_CAPACITY"]
AuthModeType = Literal["IAM", "SSO"]
AutoScalingPolicyStateChangeReasonCodeType = Literal[
    "CLEANUP_FAILURE", "PROVISION_FAILURE", "USER_REQUEST"
]
AutoScalingPolicyStateType = Literal[
    "ATTACHED", "ATTACHING", "DETACHED", "DETACHING", "FAILED", "PENDING"
]
CancelStepsRequestStatusType = Literal["FAILED", "SUBMITTED"]
ClusterRunningWaiterName = Literal["cluster_running"]
ClusterStateChangeReasonCodeType = Literal[
    "ALL_STEPS_COMPLETED",
    "BOOTSTRAP_FAILURE",
    "INSTANCE_FAILURE",
    "INSTANCE_FLEET_TIMEOUT",
    "INTERNAL_ERROR",
    "STEP_FAILURE",
    "USER_REQUEST",
    "VALIDATION_ERROR",
]
ClusterStateType = Literal[
    "BOOTSTRAPPING",
    "RUNNING",
    "STARTING",
    "TERMINATED",
    "TERMINATED_WITH_ERRORS",
    "TERMINATING",
    "WAITING",
]
ClusterTerminatedWaiterName = Literal["cluster_terminated"]
ComparisonOperatorType = Literal[
    "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL"
]
ComputeLimitsUnitTypeType = Literal["InstanceFleetUnits", "Instances", "VCPU"]
ExecutionEngineTypeType = Literal["EMR"]
IdentityTypeType = Literal["GROUP", "USER"]
InstanceCollectionTypeType = Literal["INSTANCE_FLEET", "INSTANCE_GROUP"]
InstanceFleetStateChangeReasonCodeType = Literal[
    "CLUSTER_TERMINATED", "INSTANCE_FAILURE", "INTERNAL_ERROR", "VALIDATION_ERROR"
]
InstanceFleetStateType = Literal[
    "BOOTSTRAPPING", "PROVISIONING", "RESIZING", "RUNNING", "SUSPENDED", "TERMINATED", "TERMINATING"
]
InstanceFleetTypeType = Literal["CORE", "MASTER", "TASK"]
InstanceGroupStateChangeReasonCodeType = Literal[
    "CLUSTER_TERMINATED", "INSTANCE_FAILURE", "INTERNAL_ERROR", "VALIDATION_ERROR"
]
InstanceGroupStateType = Literal[
    "ARRESTED",
    "BOOTSTRAPPING",
    "ENDED",
    "PROVISIONING",
    "RECONFIGURING",
    "RESIZING",
    "RUNNING",
    "SHUTTING_DOWN",
    "SUSPENDED",
    "TERMINATED",
    "TERMINATING",
]
InstanceGroupTypeType = Literal["CORE", "MASTER", "TASK"]
InstanceRoleTypeType = Literal["CORE", "MASTER", "TASK"]
InstanceStateChangeReasonCodeType = Literal[
    "BOOTSTRAP_FAILURE",
    "CLUSTER_TERMINATED",
    "INSTANCE_FAILURE",
    "INTERNAL_ERROR",
    "VALIDATION_ERROR",
]
InstanceStateType = Literal[
    "AWAITING_FULFILLMENT", "BOOTSTRAPPING", "PROVISIONING", "RUNNING", "TERMINATED"
]
JobFlowExecutionStateType = Literal[
    "BOOTSTRAPPING",
    "COMPLETED",
    "FAILED",
    "RUNNING",
    "SHUTTING_DOWN",
    "STARTING",
    "TERMINATED",
    "WAITING",
]
ListBootstrapActionsPaginatorName = Literal["list_bootstrap_actions"]
ListClustersPaginatorName = Literal["list_clusters"]
ListInstanceFleetsPaginatorName = Literal["list_instance_fleets"]
ListInstanceGroupsPaginatorName = Literal["list_instance_groups"]
ListInstancesPaginatorName = Literal["list_instances"]
ListNotebookExecutionsPaginatorName = Literal["list_notebook_executions"]
ListSecurityConfigurationsPaginatorName = Literal["list_security_configurations"]
ListStepsPaginatorName = Literal["list_steps"]
ListStudioSessionMappingsPaginatorName = Literal["list_studio_session_mappings"]
ListStudiosPaginatorName = Literal["list_studios"]
MarketTypeType = Literal["ON_DEMAND", "SPOT"]
NotebookExecutionStatusType = Literal[
    "FAILED",
    "FAILING",
    "FINISHED",
    "FINISHING",
    "RUNNING",
    "STARTING",
    "START_PENDING",
    "STOPPED",
    "STOPPING",
    "STOP_PENDING",
]
OnDemandCapacityReservationPreferenceType = Literal["none", "open"]
OnDemandCapacityReservationUsageStrategyType = Literal["use-capacity-reservations-first"]
OnDemandProvisioningAllocationStrategyType = Literal["lowest-price"]
PlacementGroupStrategyType = Literal["CLUSTER", "NONE", "PARTITION", "SPREAD"]
RepoUpgradeOnBootType = Literal["NONE", "SECURITY"]
ScaleDownBehaviorType = Literal["TERMINATE_AT_INSTANCE_HOUR", "TERMINATE_AT_TASK_COMPLETION"]
SpotProvisioningAllocationStrategyType = Literal["capacity-optimized"]
SpotProvisioningTimeoutActionType = Literal["SWITCH_TO_ON_DEMAND", "TERMINATE_CLUSTER"]
StatisticType = Literal["AVERAGE", "MAXIMUM", "MINIMUM", "SAMPLE_COUNT", "SUM"]
StepCancellationOptionType = Literal["SEND_INTERRUPT", "TERMINATE_PROCESS"]
StepCompleteWaiterName = Literal["step_complete"]
StepExecutionStateType = Literal[
    "CANCELLED", "COMPLETED", "CONTINUE", "FAILED", "INTERRUPTED", "PENDING", "RUNNING"
]
StepStateChangeReasonCodeType = Literal["NONE"]
StepStateType = Literal[
    "CANCELLED", "CANCEL_PENDING", "COMPLETED", "FAILED", "INTERRUPTED", "PENDING", "RUNNING"
]
UnitType = Literal[
    "BITS",
    "BITS_PER_SECOND",
    "BYTES",
    "BYTES_PER_SECOND",
    "COUNT",
    "COUNT_PER_SECOND",
    "GIGA_BITS",
    "GIGA_BITS_PER_SECOND",
    "GIGA_BYTES",
    "GIGA_BYTES_PER_SECOND",
    "KILO_BITS",
    "KILO_BITS_PER_SECOND",
    "KILO_BYTES",
    "KILO_BYTES_PER_SECOND",
    "MEGA_BITS",
    "MEGA_BITS_PER_SECOND",
    "MEGA_BYTES",
    "MEGA_BYTES_PER_SECOND",
    "MICRO_SECONDS",
    "MILLI_SECONDS",
    "NONE",
    "PERCENT",
    "SECONDS",
    "TERA_BITS",
    "TERA_BITS_PER_SECOND",
    "TERA_BYTES",
    "TERA_BYTES_PER_SECOND",
]
