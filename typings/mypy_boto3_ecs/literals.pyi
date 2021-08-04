"""
Type annotations for ecs service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/literals.html)

Usage::

    ```python
    from mypy_boto3_ecs.literals import AgentUpdateStatusType

    data: AgentUpdateStatusType = "FAILED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AgentUpdateStatusType",
    "AssignPublicIpType",
    "CapacityProviderFieldType",
    "CapacityProviderStatusType",
    "CapacityProviderUpdateStatusType",
    "ClusterFieldType",
    "ClusterSettingNameType",
    "CompatibilityType",
    "ConnectivityType",
    "ContainerConditionType",
    "ContainerInstanceFieldType",
    "ContainerInstanceStatusType",
    "DeploymentControllerTypeType",
    "DeploymentRolloutStateType",
    "DesiredStatusType",
    "DeviceCgroupPermissionType",
    "EFSAuthorizationConfigIAMType",
    "EFSTransitEncryptionType",
    "EnvironmentFileTypeType",
    "ExecuteCommandLoggingType",
    "FirelensConfigurationTypeType",
    "HealthStatusType",
    "IpcModeType",
    "LaunchTypeType",
    "ListAccountSettingsPaginatorName",
    "ListAttributesPaginatorName",
    "ListClustersPaginatorName",
    "ListContainerInstancesPaginatorName",
    "ListServicesPaginatorName",
    "ListTaskDefinitionFamiliesPaginatorName",
    "ListTaskDefinitionsPaginatorName",
    "ListTasksPaginatorName",
    "LogDriverType",
    "ManagedAgentNameType",
    "ManagedScalingStatusType",
    "ManagedTerminationProtectionType",
    "NetworkModeType",
    "PidModeType",
    "PlacementConstraintTypeType",
    "PlacementStrategyTypeType",
    "PlatformDeviceTypeType",
    "PropagateTagsType",
    "ProxyConfigurationTypeType",
    "ResourceTypeType",
    "ScaleUnitType",
    "SchedulingStrategyType",
    "ScopeType",
    "ServiceFieldType",
    "ServicesInactiveWaiterName",
    "ServicesStableWaiterName",
    "SettingNameType",
    "SortOrderType",
    "StabilityStatusType",
    "TargetTypeType",
    "TaskDefinitionFamilyStatusType",
    "TaskDefinitionFieldType",
    "TaskDefinitionPlacementConstraintTypeType",
    "TaskDefinitionStatusType",
    "TaskFieldType",
    "TaskSetFieldType",
    "TaskStopCodeType",
    "TasksRunningWaiterName",
    "TasksStoppedWaiterName",
    "TransportProtocolType",
    "UlimitNameType",
)

AgentUpdateStatusType = Literal["FAILED", "PENDING", "STAGED", "STAGING", "UPDATED", "UPDATING"]
AssignPublicIpType = Literal["DISABLED", "ENABLED"]
CapacityProviderFieldType = Literal["TAGS"]
CapacityProviderStatusType = Literal["ACTIVE", "INACTIVE"]
CapacityProviderUpdateStatusType = Literal[
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
ClusterFieldType = Literal["ATTACHMENTS", "CONFIGURATIONS", "SETTINGS", "STATISTICS", "TAGS"]
ClusterSettingNameType = Literal["containerInsights"]
CompatibilityType = Literal["EC2", "EXTERNAL", "FARGATE"]
ConnectivityType = Literal["CONNECTED", "DISCONNECTED"]
ContainerConditionType = Literal["COMPLETE", "HEALTHY", "START", "SUCCESS"]
ContainerInstanceFieldType = Literal["TAGS"]
ContainerInstanceStatusType = Literal[
    "ACTIVE", "DEREGISTERING", "DRAINING", "REGISTERING", "REGISTRATION_FAILED"
]
DeploymentControllerTypeType = Literal["CODE_DEPLOY", "ECS", "EXTERNAL"]
DeploymentRolloutStateType = Literal["COMPLETED", "FAILED", "IN_PROGRESS"]
DesiredStatusType = Literal["PENDING", "RUNNING", "STOPPED"]
DeviceCgroupPermissionType = Literal["mknod", "read", "write"]
EFSAuthorizationConfigIAMType = Literal["DISABLED", "ENABLED"]
EFSTransitEncryptionType = Literal["DISABLED", "ENABLED"]
EnvironmentFileTypeType = Literal["s3"]
ExecuteCommandLoggingType = Literal["DEFAULT", "NONE", "OVERRIDE"]
FirelensConfigurationTypeType = Literal["fluentbit", "fluentd"]
HealthStatusType = Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]
IpcModeType = Literal["host", "none", "task"]
LaunchTypeType = Literal["EC2", "EXTERNAL", "FARGATE"]
ListAccountSettingsPaginatorName = Literal["list_account_settings"]
ListAttributesPaginatorName = Literal["list_attributes"]
ListClustersPaginatorName = Literal["list_clusters"]
ListContainerInstancesPaginatorName = Literal["list_container_instances"]
ListServicesPaginatorName = Literal["list_services"]
ListTaskDefinitionFamiliesPaginatorName = Literal["list_task_definition_families"]
ListTaskDefinitionsPaginatorName = Literal["list_task_definitions"]
ListTasksPaginatorName = Literal["list_tasks"]
LogDriverType = Literal[
    "awsfirelens", "awslogs", "fluentd", "gelf", "journald", "json-file", "splunk", "syslog"
]
ManagedAgentNameType = Literal["ExecuteCommandAgent"]
ManagedScalingStatusType = Literal["DISABLED", "ENABLED"]
ManagedTerminationProtectionType = Literal["DISABLED", "ENABLED"]
NetworkModeType = Literal["awsvpc", "bridge", "host", "none"]
PidModeType = Literal["host", "task"]
PlacementConstraintTypeType = Literal["distinctInstance", "memberOf"]
PlacementStrategyTypeType = Literal["binpack", "random", "spread"]
PlatformDeviceTypeType = Literal["GPU"]
PropagateTagsType = Literal["SERVICE", "TASK_DEFINITION"]
ProxyConfigurationTypeType = Literal["APPMESH"]
ResourceTypeType = Literal["GPU", "InferenceAccelerator"]
ScaleUnitType = Literal["PERCENT"]
SchedulingStrategyType = Literal["DAEMON", "REPLICA"]
ScopeType = Literal["shared", "task"]
ServiceFieldType = Literal["TAGS"]
ServicesInactiveWaiterName = Literal["services_inactive"]
ServicesStableWaiterName = Literal["services_stable"]
SettingNameType = Literal[
    "awsvpcTrunking",
    "containerInsights",
    "containerInstanceLongArnFormat",
    "serviceLongArnFormat",
    "taskLongArnFormat",
]
SortOrderType = Literal["ASC", "DESC"]
StabilityStatusType = Literal["STABILIZING", "STEADY_STATE"]
TargetTypeType = Literal["container-instance"]
TaskDefinitionFamilyStatusType = Literal["ACTIVE", "ALL", "INACTIVE"]
TaskDefinitionFieldType = Literal["TAGS"]
TaskDefinitionPlacementConstraintTypeType = Literal["memberOf"]
TaskDefinitionStatusType = Literal["ACTIVE", "INACTIVE"]
TaskFieldType = Literal["TAGS"]
TaskSetFieldType = Literal["TAGS"]
TaskStopCodeType = Literal["EssentialContainerExited", "TaskFailedToStart", "UserInitiated"]
TasksRunningWaiterName = Literal["tasks_running"]
TasksStoppedWaiterName = Literal["tasks_stopped"]
TransportProtocolType = Literal["tcp", "udp"]
UlimitNameType = Literal[
    "core",
    "cpu",
    "data",
    "fsize",
    "locks",
    "memlock",
    "msgqueue",
    "nice",
    "nofile",
    "nproc",
    "rss",
    "rtprio",
    "rttime",
    "sigpending",
    "stack",
]
