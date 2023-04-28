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
    "ApplicationProtocolType",
    "AssignPublicIpType",
    "CPUArchitectureType",
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
    "InstanceHealthCheckStateType",
    "InstanceHealthCheckTypeType",
    "IpcModeType",
    "LaunchTypeType",
    "ListAccountSettingsPaginatorName",
    "ListAttributesPaginatorName",
    "ListClustersPaginatorName",
    "ListContainerInstancesPaginatorName",
    "ListServicesByNamespacePaginatorName",
    "ListServicesPaginatorName",
    "ListTaskDefinitionFamiliesPaginatorName",
    "ListTaskDefinitionsPaginatorName",
    "ListTasksPaginatorName",
    "LogDriverType",
    "ManagedAgentNameType",
    "ManagedScalingStatusType",
    "ManagedTerminationProtectionType",
    "NetworkModeType",
    "OSFamilyType",
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
ApplicationProtocolType = Literal["grpc", "http", "http2"]
AssignPublicIpType = Literal["DISABLED", "ENABLED"]
CPUArchitectureType = Literal["ARM64", "X86_64"]
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
ContainerInstanceFieldType = Literal["CONTAINER_INSTANCE_HEALTH", "TAGS"]
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
InstanceHealthCheckStateType = Literal["IMPAIRED", "INITIALIZING", "INSUFFICIENT_DATA", "OK"]
InstanceHealthCheckTypeType = Literal["CONTAINER_RUNTIME"]
IpcModeType = Literal["host", "none", "task"]
LaunchTypeType = Literal["EC2", "EXTERNAL", "FARGATE"]
ListAccountSettingsPaginatorName = Literal["list_account_settings"]
ListAttributesPaginatorName = Literal["list_attributes"]
ListClustersPaginatorName = Literal["list_clusters"]
ListContainerInstancesPaginatorName = Literal["list_container_instances"]
ListServicesByNamespacePaginatorName = Literal["list_services_by_namespace"]
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
OSFamilyType = Literal[
    "LINUX",
    "WINDOWS_SERVER_2004_CORE",
    "WINDOWS_SERVER_2016_FULL",
    "WINDOWS_SERVER_2019_CORE",
    "WINDOWS_SERVER_2019_FULL",
    "WINDOWS_SERVER_2022_CORE",
    "WINDOWS_SERVER_2022_FULL",
    "WINDOWS_SERVER_20H2_CORE",
]
PidModeType = Literal["host", "task"]
PlacementConstraintTypeType = Literal["distinctInstance", "memberOf"]
PlacementStrategyTypeType = Literal["binpack", "random", "spread"]
PlatformDeviceTypeType = Literal["GPU"]
PropagateTagsType = Literal["NONE", "SERVICE", "TASK_DEFINITION"]
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
    "fargateFIPSMode",
    "serviceLongArnFormat",
    "tagResourceAuthorization",
    "taskLongArnFormat",
]
SortOrderType = Literal["ASC", "DESC"]
StabilityStatusType = Literal["STABILIZING", "STEADY_STATE"]
TargetTypeType = Literal["container-instance"]
TaskDefinitionFamilyStatusType = Literal["ACTIVE", "ALL", "INACTIVE"]
TaskDefinitionFieldType = Literal["TAGS"]
TaskDefinitionPlacementConstraintTypeType = Literal["memberOf"]
TaskDefinitionStatusType = Literal["ACTIVE", "DELETE_IN_PROGRESS", "INACTIVE"]
TaskFieldType = Literal["TAGS"]
TaskSetFieldType = Literal["TAGS"]
TaskStopCodeType = Literal[
    "EssentialContainerExited",
    "ServiceSchedulerInitiated",
    "SpotInterruption",
    "TaskFailedToStart",
    "TerminationNotice",
    "UserInitiated",
]
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
