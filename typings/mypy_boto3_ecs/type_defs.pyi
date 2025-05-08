"""
Type annotations for ecs service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_ecs.type_defs import AttachmentStateChangeTypeDef

    data: AttachmentStateChangeTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AgentUpdateStatusType,
    ApplicationProtocolType,
    AssignPublicIpType,
    AvailabilityZoneRebalancingType,
    CapacityProviderStatusType,
    CapacityProviderUpdateStatusType,
    ClusterFieldType,
    CompatibilityType,
    ConnectivityType,
    ContainerConditionType,
    ContainerInstanceFieldType,
    ContainerInstanceStatusType,
    CPUArchitectureType,
    DeploymentControllerTypeType,
    DeploymentRolloutStateType,
    DesiredStatusType,
    DeviceCgroupPermissionType,
    EFSAuthorizationConfigIAMType,
    EFSTransitEncryptionType,
    ExecuteCommandLoggingType,
    FirelensConfigurationTypeType,
    HealthStatusType,
    InstanceHealthCheckStateType,
    IpcModeType,
    LaunchTypeType,
    LogDriverType,
    ManagedDrainingType,
    ManagedScalingStatusType,
    ManagedTerminationProtectionType,
    NetworkModeType,
    OSFamilyType,
    PidModeType,
    PlacementConstraintTypeType,
    PlacementStrategyTypeType,
    PropagateTagsType,
    ResourceTypeType,
    SchedulingStrategyType,
    ScopeType,
    ServiceDeploymentRollbackMonitorsStatusType,
    ServiceDeploymentStatusType,
    SettingNameType,
    SettingTypeType,
    SortOrderType,
    StabilityStatusType,
    StopServiceDeploymentStopTypeType,
    TaskDefinitionFamilyStatusType,
    TaskDefinitionStatusType,
    TaskFilesystemTypeType,
    TaskStopCodeType,
    TransportProtocolType,
    UlimitNameType,
    VersionConsistencyType,
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
    "AttachmentStateChangeTypeDef",
    "AttachmentTypeDef",
    "AttributeTypeDef",
    "AutoScalingGroupProviderTypeDef",
    "AutoScalingGroupProviderUpdateTypeDef",
    "AwsVpcConfigurationOutputTypeDef",
    "AwsVpcConfigurationTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "CapacityProviderTypeDef",
    "ClusterConfigurationTypeDef",
    "ClusterServiceConnectDefaultsRequestTypeDef",
    "ClusterServiceConnectDefaultsTypeDef",
    "ClusterSettingTypeDef",
    "ClusterTypeDef",
    "ContainerDefinitionOutputTypeDef",
    "ContainerDefinitionTypeDef",
    "ContainerDefinitionUnionTypeDef",
    "ContainerDependencyTypeDef",
    "ContainerImageTypeDef",
    "ContainerInstanceHealthStatusTypeDef",
    "ContainerInstanceTypeDef",
    "ContainerOverrideOutputTypeDef",
    "ContainerOverrideTypeDef",
    "ContainerRestartPolicyOutputTypeDef",
    "ContainerRestartPolicyTypeDef",
    "ContainerRestartPolicyUnionTypeDef",
    "ContainerStateChangeTypeDef",
    "ContainerTypeDef",
    "CreateCapacityProviderRequestTypeDef",
    "CreateCapacityProviderResponseTypeDef",
    "CreateClusterRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateServiceRequestTypeDef",
    "CreateServiceResponseTypeDef",
    "CreateTaskSetRequestTypeDef",
    "CreateTaskSetResponseTypeDef",
    "CreatedAtTypeDef",
    "DeleteAccountSettingRequestTypeDef",
    "DeleteAccountSettingResponseTypeDef",
    "DeleteAttributesRequestTypeDef",
    "DeleteAttributesResponseTypeDef",
    "DeleteCapacityProviderRequestTypeDef",
    "DeleteCapacityProviderResponseTypeDef",
    "DeleteClusterRequestTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteServiceRequestTypeDef",
    "DeleteServiceResponseTypeDef",
    "DeleteTaskDefinitionsRequestTypeDef",
    "DeleteTaskDefinitionsResponseTypeDef",
    "DeleteTaskSetRequestTypeDef",
    "DeleteTaskSetResponseTypeDef",
    "DeploymentAlarmsOutputTypeDef",
    "DeploymentAlarmsTypeDef",
    "DeploymentCircuitBreakerTypeDef",
    "DeploymentConfigurationOutputTypeDef",
    "DeploymentConfigurationTypeDef",
    "DeploymentConfigurationUnionTypeDef",
    "DeploymentControllerTypeDef",
    "DeploymentEphemeralStorageTypeDef",
    "DeploymentTypeDef",
    "DeregisterContainerInstanceRequestTypeDef",
    "DeregisterContainerInstanceResponseTypeDef",
    "DeregisterTaskDefinitionRequestTypeDef",
    "DeregisterTaskDefinitionResponseTypeDef",
    "DescribeCapacityProvidersRequestTypeDef",
    "DescribeCapacityProvidersResponseTypeDef",
    "DescribeClustersRequestTypeDef",
    "DescribeClustersResponseTypeDef",
    "DescribeContainerInstancesRequestTypeDef",
    "DescribeContainerInstancesResponseTypeDef",
    "DescribeServiceDeploymentsRequestTypeDef",
    "DescribeServiceDeploymentsResponseTypeDef",
    "DescribeServiceRevisionsRequestTypeDef",
    "DescribeServiceRevisionsResponseTypeDef",
    "DescribeServicesRequestTypeDef",
    "DescribeServicesRequestWaitExtraTypeDef",
    "DescribeServicesRequestWaitTypeDef",
    "DescribeServicesResponseTypeDef",
    "DescribeTaskDefinitionRequestTypeDef",
    "DescribeTaskDefinitionResponseTypeDef",
    "DescribeTaskSetsRequestTypeDef",
    "DescribeTaskSetsResponseTypeDef",
    "DescribeTasksRequestTypeDef",
    "DescribeTasksRequestWaitExtraTypeDef",
    "DescribeTasksRequestWaitTypeDef",
    "DescribeTasksResponseTypeDef",
    "DeviceOutputTypeDef",
    "DeviceTypeDef",
    "DeviceUnionTypeDef",
    "DiscoverPollEndpointRequestTypeDef",
    "DiscoverPollEndpointResponseTypeDef",
    "DockerVolumeConfigurationOutputTypeDef",
    "DockerVolumeConfigurationTypeDef",
    "DockerVolumeConfigurationUnionTypeDef",
    "EBSTagSpecificationOutputTypeDef",
    "EBSTagSpecificationTypeDef",
    "EBSTagSpecificationUnionTypeDef",
    "EFSAuthorizationConfigTypeDef",
    "EFSVolumeConfigurationTypeDef",
    "EnvironmentFileTypeDef",
    "EphemeralStorageTypeDef",
    "ExecuteCommandConfigurationTypeDef",
    "ExecuteCommandLogConfigurationTypeDef",
    "ExecuteCommandRequestTypeDef",
    "ExecuteCommandResponseTypeDef",
    "FSxWindowsFileServerAuthorizationConfigTypeDef",
    "FSxWindowsFileServerVolumeConfigurationTypeDef",
    "FailureTypeDef",
    "FirelensConfigurationOutputTypeDef",
    "FirelensConfigurationTypeDef",
    "FirelensConfigurationUnionTypeDef",
    "GetTaskProtectionRequestTypeDef",
    "GetTaskProtectionResponseTypeDef",
    "HealthCheckOutputTypeDef",
    "HealthCheckTypeDef",
    "HealthCheckUnionTypeDef",
    "HostEntryTypeDef",
    "HostVolumePropertiesTypeDef",
    "InferenceAcceleratorOverrideTypeDef",
    "InferenceAcceleratorTypeDef",
    "InstanceHealthCheckResultTypeDef",
    "KernelCapabilitiesOutputTypeDef",
    "KernelCapabilitiesTypeDef",
    "KernelCapabilitiesUnionTypeDef",
    "KeyValuePairTypeDef",
    "LinuxParametersOutputTypeDef",
    "LinuxParametersTypeDef",
    "LinuxParametersUnionTypeDef",
    "ListAccountSettingsRequestPaginateTypeDef",
    "ListAccountSettingsRequestTypeDef",
    "ListAccountSettingsResponseTypeDef",
    "ListAttributesRequestPaginateTypeDef",
    "ListAttributesRequestTypeDef",
    "ListAttributesResponseTypeDef",
    "ListClustersRequestPaginateTypeDef",
    "ListClustersRequestTypeDef",
    "ListClustersResponseTypeDef",
    "ListContainerInstancesRequestPaginateTypeDef",
    "ListContainerInstancesRequestTypeDef",
    "ListContainerInstancesResponseTypeDef",
    "ListServiceDeploymentsRequestTypeDef",
    "ListServiceDeploymentsResponseTypeDef",
    "ListServicesByNamespaceRequestPaginateTypeDef",
    "ListServicesByNamespaceRequestTypeDef",
    "ListServicesByNamespaceResponseTypeDef",
    "ListServicesRequestPaginateTypeDef",
    "ListServicesRequestTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTaskDefinitionFamiliesRequestPaginateTypeDef",
    "ListTaskDefinitionFamiliesRequestTypeDef",
    "ListTaskDefinitionFamiliesResponseTypeDef",
    "ListTaskDefinitionsRequestPaginateTypeDef",
    "ListTaskDefinitionsRequestTypeDef",
    "ListTaskDefinitionsResponseTypeDef",
    "ListTasksRequestPaginateTypeDef",
    "ListTasksRequestTypeDef",
    "ListTasksResponseTypeDef",
    "LoadBalancerTypeDef",
    "LogConfigurationOutputTypeDef",
    "LogConfigurationTypeDef",
    "LogConfigurationUnionTypeDef",
    "ManagedAgentStateChangeTypeDef",
    "ManagedAgentTypeDef",
    "ManagedScalingTypeDef",
    "ManagedStorageConfigurationTypeDef",
    "MountPointTypeDef",
    "NetworkBindingTypeDef",
    "NetworkConfigurationOutputTypeDef",
    "NetworkConfigurationTypeDef",
    "NetworkConfigurationUnionTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "PlatformDeviceTypeDef",
    "PortMappingTypeDef",
    "ProtectedTaskTypeDef",
    "ProxyConfigurationOutputTypeDef",
    "ProxyConfigurationTypeDef",
    "ProxyConfigurationUnionTypeDef",
    "PutAccountSettingDefaultRequestTypeDef",
    "PutAccountSettingDefaultResponseTypeDef",
    "PutAccountSettingRequestTypeDef",
    "PutAccountSettingResponseTypeDef",
    "PutAttributesRequestTypeDef",
    "PutAttributesResponseTypeDef",
    "PutClusterCapacityProvidersRequestTypeDef",
    "PutClusterCapacityProvidersResponseTypeDef",
    "RegisterContainerInstanceRequestTypeDef",
    "RegisterContainerInstanceResponseTypeDef",
    "RegisterTaskDefinitionRequestTypeDef",
    "RegisterTaskDefinitionResponseTypeDef",
    "RepositoryCredentialsTypeDef",
    "ResourceOutputTypeDef",
    "ResourceRequirementTypeDef",
    "ResourceTypeDef",
    "ResourceUnionTypeDef",
    "ResponseMetadataTypeDef",
    "RollbackTypeDef",
    "RunTaskRequestTypeDef",
    "RunTaskResponseTypeDef",
    "RuntimePlatformTypeDef",
    "ScaleTypeDef",
    "SecretTypeDef",
    "ServiceConnectClientAliasTypeDef",
    "ServiceConnectConfigurationOutputTypeDef",
    "ServiceConnectConfigurationTypeDef",
    "ServiceConnectConfigurationUnionTypeDef",
    "ServiceConnectServiceOutputTypeDef",
    "ServiceConnectServiceResourceTypeDef",
    "ServiceConnectServiceTypeDef",
    "ServiceConnectTlsCertificateAuthorityTypeDef",
    "ServiceConnectTlsConfigurationTypeDef",
    "ServiceDeploymentAlarmsTypeDef",
    "ServiceDeploymentBriefTypeDef",
    "ServiceDeploymentCircuitBreakerTypeDef",
    "ServiceDeploymentTypeDef",
    "ServiceEventTypeDef",
    "ServiceManagedEBSVolumeConfigurationOutputTypeDef",
    "ServiceManagedEBSVolumeConfigurationTypeDef",
    "ServiceManagedEBSVolumeConfigurationUnionTypeDef",
    "ServiceRegistryTypeDef",
    "ServiceRevisionSummaryTypeDef",
    "ServiceRevisionTypeDef",
    "ServiceTypeDef",
    "ServiceVolumeConfigurationOutputTypeDef",
    "ServiceVolumeConfigurationTypeDef",
    "ServiceVolumeConfigurationUnionTypeDef",
    "SessionTypeDef",
    "SettingTypeDef",
    "StartTaskRequestTypeDef",
    "StartTaskResponseTypeDef",
    "StopServiceDeploymentRequestTypeDef",
    "StopServiceDeploymentResponseTypeDef",
    "StopTaskRequestTypeDef",
    "StopTaskResponseTypeDef",
    "SubmitAttachmentStateChangesRequestTypeDef",
    "SubmitAttachmentStateChangesResponseTypeDef",
    "SubmitContainerStateChangeRequestTypeDef",
    "SubmitContainerStateChangeResponseTypeDef",
    "SubmitTaskStateChangeRequestTypeDef",
    "SubmitTaskStateChangeResponseTypeDef",
    "SystemControlTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TaskDefinitionPlacementConstraintTypeDef",
    "TaskDefinitionTypeDef",
    "TaskEphemeralStorageTypeDef",
    "TaskManagedEBSVolumeConfigurationTypeDef",
    "TaskManagedEBSVolumeTerminationPolicyTypeDef",
    "TaskOverrideOutputTypeDef",
    "TaskOverrideTypeDef",
    "TaskOverrideUnionTypeDef",
    "TaskSetTypeDef",
    "TaskTypeDef",
    "TaskVolumeConfigurationTypeDef",
    "TimeoutConfigurationTypeDef",
    "TimestampTypeDef",
    "TmpfsOutputTypeDef",
    "TmpfsTypeDef",
    "TmpfsUnionTypeDef",
    "UlimitTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateCapacityProviderRequestTypeDef",
    "UpdateCapacityProviderResponseTypeDef",
    "UpdateClusterRequestTypeDef",
    "UpdateClusterResponseTypeDef",
    "UpdateClusterSettingsRequestTypeDef",
    "UpdateClusterSettingsResponseTypeDef",
    "UpdateContainerAgentRequestTypeDef",
    "UpdateContainerAgentResponseTypeDef",
    "UpdateContainerInstancesStateRequestTypeDef",
    "UpdateContainerInstancesStateResponseTypeDef",
    "UpdateServicePrimaryTaskSetRequestTypeDef",
    "UpdateServicePrimaryTaskSetResponseTypeDef",
    "UpdateServiceRequestTypeDef",
    "UpdateServiceResponseTypeDef",
    "UpdateTaskProtectionRequestTypeDef",
    "UpdateTaskProtectionResponseTypeDef",
    "UpdateTaskSetRequestTypeDef",
    "UpdateTaskSetResponseTypeDef",
    "VersionInfoTypeDef",
    "VolumeFromTypeDef",
    "VolumeOutputTypeDef",
    "VolumeTypeDef",
    "VolumeUnionTypeDef",
    "VpcLatticeConfigurationTypeDef",
    "WaiterConfigTypeDef",
)

class AttachmentStateChangeTypeDef(TypedDict):
    attachmentArn: str
    status: str

class KeyValuePairTypeDef(TypedDict):
    name: NotRequired[str]
    value: NotRequired[str]

class AttributeTypeDef(TypedDict):
    name: str
    value: NotRequired[str]
    targetType: NotRequired[Literal["container-instance"]]
    targetId: NotRequired[str]

class ManagedScalingTypeDef(TypedDict):
    status: NotRequired[ManagedScalingStatusType]
    targetCapacity: NotRequired[int]
    minimumScalingStepSize: NotRequired[int]
    maximumScalingStepSize: NotRequired[int]
    instanceWarmupPeriod: NotRequired[int]

class AwsVpcConfigurationOutputTypeDef(TypedDict):
    subnets: List[str]
    securityGroups: NotRequired[List[str]]
    assignPublicIp: NotRequired[AssignPublicIpType]

class AwsVpcConfigurationTypeDef(TypedDict):
    subnets: Sequence[str]
    securityGroups: NotRequired[Sequence[str]]
    assignPublicIp: NotRequired[AssignPublicIpType]

class CapacityProviderStrategyItemTypeDef(TypedDict):
    capacityProvider: str
    weight: NotRequired[int]
    base: NotRequired[int]

class TagTypeDef(TypedDict):
    key: NotRequired[str]
    value: NotRequired[str]

class ManagedStorageConfigurationTypeDef(TypedDict):
    kmsKeyId: NotRequired[str]
    fargateEphemeralStorageKmsKeyId: NotRequired[str]

class ClusterServiceConnectDefaultsRequestTypeDef(TypedDict):
    namespace: str

class ClusterServiceConnectDefaultsTypeDef(TypedDict):
    namespace: NotRequired[str]

class ClusterSettingTypeDef(TypedDict):
    name: NotRequired[Literal["containerInsights"]]
    value: NotRequired[str]

class ContainerDependencyTypeDef(TypedDict):
    containerName: str
    condition: ContainerConditionType

class ContainerRestartPolicyOutputTypeDef(TypedDict):
    enabled: bool
    ignoredExitCodes: NotRequired[List[int]]
    restartAttemptPeriod: NotRequired[int]

EnvironmentFileTypeDef = TypedDict(
    "EnvironmentFileTypeDef",
    {
        "value": str,
        "type": Literal["s3"],
    },
)
FirelensConfigurationOutputTypeDef = TypedDict(
    "FirelensConfigurationOutputTypeDef",
    {
        "type": FirelensConfigurationTypeType,
        "options": NotRequired[Dict[str, str]],
    },
)

class HealthCheckOutputTypeDef(TypedDict):
    command: List[str]
    interval: NotRequired[int]
    timeout: NotRequired[int]
    retries: NotRequired[int]
    startPeriod: NotRequired[int]

class HostEntryTypeDef(TypedDict):
    hostname: str
    ipAddress: str

class MountPointTypeDef(TypedDict):
    sourceVolume: NotRequired[str]
    containerPath: NotRequired[str]
    readOnly: NotRequired[bool]

class PortMappingTypeDef(TypedDict):
    containerPort: NotRequired[int]
    hostPort: NotRequired[int]
    protocol: NotRequired[TransportProtocolType]
    name: NotRequired[str]
    appProtocol: NotRequired[ApplicationProtocolType]
    containerPortRange: NotRequired[str]

class RepositoryCredentialsTypeDef(TypedDict):
    credentialsParameter: str

ResourceRequirementTypeDef = TypedDict(
    "ResourceRequirementTypeDef",
    {
        "value": str,
        "type": ResourceTypeType,
    },
)

class SecretTypeDef(TypedDict):
    name: str
    valueFrom: str

class SystemControlTypeDef(TypedDict):
    namespace: NotRequired[str]
    value: NotRequired[str]

class UlimitTypeDef(TypedDict):
    name: UlimitNameType
    softLimit: int
    hardLimit: int

class VolumeFromTypeDef(TypedDict):
    sourceContainer: NotRequired[str]
    readOnly: NotRequired[bool]

class ContainerImageTypeDef(TypedDict):
    containerName: NotRequired[str]
    imageDigest: NotRequired[str]
    image: NotRequired[str]

InstanceHealthCheckResultTypeDef = TypedDict(
    "InstanceHealthCheckResultTypeDef",
    {
        "type": NotRequired[Literal["CONTAINER_RUNTIME"]],
        "status": NotRequired[InstanceHealthCheckStateType],
        "lastUpdated": NotRequired[datetime],
        "lastStatusChange": NotRequired[datetime],
    },
)
ResourceOutputTypeDef = TypedDict(
    "ResourceOutputTypeDef",
    {
        "name": NotRequired[str],
        "type": NotRequired[str],
        "doubleValue": NotRequired[float],
        "longValue": NotRequired[int],
        "integerValue": NotRequired[int],
        "stringSetValue": NotRequired[List[str]],
    },
)

class VersionInfoTypeDef(TypedDict):
    agentVersion: NotRequired[str]
    agentHash: NotRequired[str]
    dockerVersion: NotRequired[str]

class ContainerRestartPolicyTypeDef(TypedDict):
    enabled: bool
    ignoredExitCodes: NotRequired[Sequence[int]]
    restartAttemptPeriod: NotRequired[int]

class NetworkBindingTypeDef(TypedDict):
    bindIP: NotRequired[str]
    containerPort: NotRequired[int]
    hostPort: NotRequired[int]
    protocol: NotRequired[TransportProtocolType]
    containerPortRange: NotRequired[str]
    hostPortRange: NotRequired[str]

class ManagedAgentTypeDef(TypedDict):
    lastStartedAt: NotRequired[datetime]
    name: NotRequired[Literal["ExecuteCommandAgent"]]
    reason: NotRequired[str]
    lastStatus: NotRequired[str]

class NetworkInterfaceTypeDef(TypedDict):
    attachmentId: NotRequired[str]
    privateIpv4Address: NotRequired[str]
    ipv6Address: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

DeploymentControllerTypeDef = TypedDict(
    "DeploymentControllerTypeDef",
    {
        "type": DeploymentControllerTypeType,
    },
)

class LoadBalancerTypeDef(TypedDict):
    targetGroupArn: NotRequired[str]
    loadBalancerName: NotRequired[str]
    containerName: NotRequired[str]
    containerPort: NotRequired[int]

PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef",
    {
        "type": NotRequired[PlacementConstraintTypeType],
        "expression": NotRequired[str],
    },
)
PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef",
    {
        "type": NotRequired[PlacementStrategyTypeType],
        "field": NotRequired[str],
    },
)

class ServiceRegistryTypeDef(TypedDict):
    registryArn: NotRequired[str]
    port: NotRequired[int]
    containerName: NotRequired[str]
    containerPort: NotRequired[int]

class VpcLatticeConfigurationTypeDef(TypedDict):
    roleArn: str
    targetGroupArn: str
    portName: str

class ScaleTypeDef(TypedDict):
    value: NotRequired[float]
    unit: NotRequired[Literal["PERCENT"]]

TimestampTypeDef = Union[datetime, str]

class DeleteAccountSettingRequestTypeDef(TypedDict):
    name: SettingNameType
    principalArn: NotRequired[str]

SettingTypeDef = TypedDict(
    "SettingTypeDef",
    {
        "name": NotRequired[SettingNameType],
        "value": NotRequired[str],
        "principalArn": NotRequired[str],
        "type": NotRequired[SettingTypeType],
    },
)

class DeleteCapacityProviderRequestTypeDef(TypedDict):
    capacityProvider: str

class DeleteClusterRequestTypeDef(TypedDict):
    cluster: str

class DeleteServiceRequestTypeDef(TypedDict):
    service: str
    cluster: NotRequired[str]
    force: NotRequired[bool]

class DeleteTaskDefinitionsRequestTypeDef(TypedDict):
    taskDefinitions: Sequence[str]

class FailureTypeDef(TypedDict):
    arn: NotRequired[str]
    reason: NotRequired[str]
    detail: NotRequired[str]

class DeleteTaskSetRequestTypeDef(TypedDict):
    cluster: str
    service: str
    taskSet: str
    force: NotRequired[bool]

class DeploymentAlarmsOutputTypeDef(TypedDict):
    alarmNames: List[str]
    rollback: bool
    enable: bool

class DeploymentAlarmsTypeDef(TypedDict):
    alarmNames: Sequence[str]
    rollback: bool
    enable: bool

class DeploymentCircuitBreakerTypeDef(TypedDict):
    enable: bool
    rollback: bool

class DeploymentEphemeralStorageTypeDef(TypedDict):
    kmsKeyId: NotRequired[str]

class ServiceConnectServiceResourceTypeDef(TypedDict):
    discoveryName: NotRequired[str]
    discoveryArn: NotRequired[str]

class DeregisterContainerInstanceRequestTypeDef(TypedDict):
    containerInstance: str
    cluster: NotRequired[str]
    force: NotRequired[bool]

class DeregisterTaskDefinitionRequestTypeDef(TypedDict):
    taskDefinition: str

class DescribeCapacityProvidersRequestTypeDef(TypedDict):
    capacityProviders: NotRequired[Sequence[str]]
    include: NotRequired[Sequence[Literal["TAGS"]]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class DescribeClustersRequestTypeDef(TypedDict):
    clusters: NotRequired[Sequence[str]]
    include: NotRequired[Sequence[ClusterFieldType]]

class DescribeContainerInstancesRequestTypeDef(TypedDict):
    containerInstances: Sequence[str]
    cluster: NotRequired[str]
    include: NotRequired[Sequence[ContainerInstanceFieldType]]

class DescribeServiceDeploymentsRequestTypeDef(TypedDict):
    serviceDeploymentArns: Sequence[str]

class DescribeServiceRevisionsRequestTypeDef(TypedDict):
    serviceRevisionArns: Sequence[str]

class DescribeServicesRequestTypeDef(TypedDict):
    services: Sequence[str]
    cluster: NotRequired[str]
    include: NotRequired[Sequence[Literal["TAGS"]]]

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class DescribeTaskDefinitionRequestTypeDef(TypedDict):
    taskDefinition: str
    include: NotRequired[Sequence[Literal["TAGS"]]]

class DescribeTaskSetsRequestTypeDef(TypedDict):
    cluster: str
    service: str
    taskSets: NotRequired[Sequence[str]]
    include: NotRequired[Sequence[Literal["TAGS"]]]

class DescribeTasksRequestTypeDef(TypedDict):
    tasks: Sequence[str]
    cluster: NotRequired[str]
    include: NotRequired[Sequence[Literal["TAGS"]]]

class DeviceOutputTypeDef(TypedDict):
    hostPath: str
    containerPath: NotRequired[str]
    permissions: NotRequired[List[DeviceCgroupPermissionType]]

class DeviceTypeDef(TypedDict):
    hostPath: str
    containerPath: NotRequired[str]
    permissions: NotRequired[Sequence[DeviceCgroupPermissionType]]

class DiscoverPollEndpointRequestTypeDef(TypedDict):
    containerInstance: NotRequired[str]
    cluster: NotRequired[str]

class DockerVolumeConfigurationOutputTypeDef(TypedDict):
    scope: NotRequired[ScopeType]
    autoprovision: NotRequired[bool]
    driver: NotRequired[str]
    driverOpts: NotRequired[Dict[str, str]]
    labels: NotRequired[Dict[str, str]]

class DockerVolumeConfigurationTypeDef(TypedDict):
    scope: NotRequired[ScopeType]
    autoprovision: NotRequired[bool]
    driver: NotRequired[str]
    driverOpts: NotRequired[Mapping[str, str]]
    labels: NotRequired[Mapping[str, str]]

class EFSAuthorizationConfigTypeDef(TypedDict):
    accessPointId: NotRequired[str]
    iam: NotRequired[EFSAuthorizationConfigIAMType]

class EphemeralStorageTypeDef(TypedDict):
    sizeInGiB: int

class ExecuteCommandLogConfigurationTypeDef(TypedDict):
    cloudWatchLogGroupName: NotRequired[str]
    cloudWatchEncryptionEnabled: NotRequired[bool]
    s3BucketName: NotRequired[str]
    s3EncryptionEnabled: NotRequired[bool]
    s3KeyPrefix: NotRequired[str]

class ExecuteCommandRequestTypeDef(TypedDict):
    command: str
    interactive: bool
    task: str
    cluster: NotRequired[str]
    container: NotRequired[str]

class SessionTypeDef(TypedDict):
    sessionId: NotRequired[str]
    streamUrl: NotRequired[str]
    tokenValue: NotRequired[str]

class FSxWindowsFileServerAuthorizationConfigTypeDef(TypedDict):
    credentialsParameter: str
    domain: str

FirelensConfigurationTypeDef = TypedDict(
    "FirelensConfigurationTypeDef",
    {
        "type": FirelensConfigurationTypeType,
        "options": NotRequired[Mapping[str, str]],
    },
)

class GetTaskProtectionRequestTypeDef(TypedDict):
    cluster: str
    tasks: NotRequired[Sequence[str]]

class ProtectedTaskTypeDef(TypedDict):
    taskArn: NotRequired[str]
    protectionEnabled: NotRequired[bool]
    expirationDate: NotRequired[datetime]

class HealthCheckTypeDef(TypedDict):
    command: Sequence[str]
    interval: NotRequired[int]
    timeout: NotRequired[int]
    retries: NotRequired[int]
    startPeriod: NotRequired[int]

class HostVolumePropertiesTypeDef(TypedDict):
    sourcePath: NotRequired[str]

class InferenceAcceleratorOverrideTypeDef(TypedDict):
    deviceName: NotRequired[str]
    deviceType: NotRequired[str]

class InferenceAcceleratorTypeDef(TypedDict):
    deviceName: str
    deviceType: str

class KernelCapabilitiesOutputTypeDef(TypedDict):
    add: NotRequired[List[str]]
    drop: NotRequired[List[str]]

class KernelCapabilitiesTypeDef(TypedDict):
    add: NotRequired[Sequence[str]]
    drop: NotRequired[Sequence[str]]

class TmpfsOutputTypeDef(TypedDict):
    containerPath: str
    size: int
    mountOptions: NotRequired[List[str]]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAccountSettingsRequestTypeDef(TypedDict):
    name: NotRequired[SettingNameType]
    value: NotRequired[str]
    principalArn: NotRequired[str]
    effectiveSettings: NotRequired[bool]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListAttributesRequestTypeDef(TypedDict):
    targetType: Literal["container-instance"]
    cluster: NotRequired[str]
    attributeName: NotRequired[str]
    attributeValue: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListClustersRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

ListContainerInstancesRequestTypeDef = TypedDict(
    "ListContainerInstancesRequestTypeDef",
    {
        "cluster": NotRequired[str],
        "filter": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "status": NotRequired[ContainerInstanceStatusType],
    },
)

class ServiceDeploymentBriefTypeDef(TypedDict):
    serviceDeploymentArn: NotRequired[str]
    serviceArn: NotRequired[str]
    clusterArn: NotRequired[str]
    startedAt: NotRequired[datetime]
    createdAt: NotRequired[datetime]
    finishedAt: NotRequired[datetime]
    targetServiceRevisionArn: NotRequired[str]
    status: NotRequired[ServiceDeploymentStatusType]
    statusReason: NotRequired[str]

class ListServicesByNamespaceRequestTypeDef(TypedDict):
    namespace: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListServicesRequestTypeDef(TypedDict):
    cluster: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    launchType: NotRequired[LaunchTypeType]
    schedulingStrategy: NotRequired[SchedulingStrategyType]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListTaskDefinitionFamiliesRequestTypeDef(TypedDict):
    familyPrefix: NotRequired[str]
    status: NotRequired[TaskDefinitionFamilyStatusType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListTaskDefinitionsRequestTypeDef(TypedDict):
    familyPrefix: NotRequired[str]
    status: NotRequired[TaskDefinitionStatusType]
    sort: NotRequired[SortOrderType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListTasksRequestTypeDef(TypedDict):
    cluster: NotRequired[str]
    containerInstance: NotRequired[str]
    family: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    startedBy: NotRequired[str]
    serviceName: NotRequired[str]
    desiredStatus: NotRequired[DesiredStatusType]
    launchType: NotRequired[LaunchTypeType]

class ManagedAgentStateChangeTypeDef(TypedDict):
    containerName: str
    managedAgentName: Literal["ExecuteCommandAgent"]
    status: str
    reason: NotRequired[str]

PlatformDeviceTypeDef = TypedDict(
    "PlatformDeviceTypeDef",
    {
        "id": str,
        "type": Literal["GPU"],
    },
)

class PutAccountSettingDefaultRequestTypeDef(TypedDict):
    name: SettingNameType
    value: str

class PutAccountSettingRequestTypeDef(TypedDict):
    name: SettingNameType
    value: str
    principalArn: NotRequired[str]

class RuntimePlatformTypeDef(TypedDict):
    cpuArchitecture: NotRequired[CPUArchitectureType]
    operatingSystemFamily: NotRequired[OSFamilyType]

TaskDefinitionPlacementConstraintTypeDef = TypedDict(
    "TaskDefinitionPlacementConstraintTypeDef",
    {
        "type": NotRequired[Literal["memberOf"]],
        "expression": NotRequired[str],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "name": NotRequired[str],
        "type": NotRequired[str],
        "doubleValue": NotRequired[float],
        "longValue": NotRequired[int],
        "integerValue": NotRequired[int],
        "stringSetValue": NotRequired[Sequence[str]],
    },
)

class RollbackTypeDef(TypedDict):
    reason: NotRequired[str]
    startedAt: NotRequired[datetime]
    serviceRevisionArn: NotRequired[str]

class ServiceConnectClientAliasTypeDef(TypedDict):
    port: int
    dnsName: NotRequired[str]

class TimeoutConfigurationTypeDef(TypedDict):
    idleTimeoutSeconds: NotRequired[int]
    perRequestTimeoutSeconds: NotRequired[int]

class ServiceConnectTlsCertificateAuthorityTypeDef(TypedDict):
    awsPcaAuthorityArn: NotRequired[str]

class ServiceDeploymentAlarmsTypeDef(TypedDict):
    status: NotRequired[ServiceDeploymentRollbackMonitorsStatusType]
    alarmNames: NotRequired[List[str]]
    triggeredAlarmNames: NotRequired[List[str]]

class ServiceDeploymentCircuitBreakerTypeDef(TypedDict):
    status: NotRequired[ServiceDeploymentRollbackMonitorsStatusType]
    failureCount: NotRequired[int]
    threshold: NotRequired[int]

class ServiceRevisionSummaryTypeDef(TypedDict):
    arn: NotRequired[str]
    requestedTaskCount: NotRequired[int]
    runningTaskCount: NotRequired[int]
    pendingTaskCount: NotRequired[int]

ServiceEventTypeDef = TypedDict(
    "ServiceEventTypeDef",
    {
        "id": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "message": NotRequired[str],
    },
)

class StopServiceDeploymentRequestTypeDef(TypedDict):
    serviceDeploymentArn: str
    stopType: NotRequired[StopServiceDeploymentStopTypeType]

class StopTaskRequestTypeDef(TypedDict):
    task: str
    cluster: NotRequired[str]
    reason: NotRequired[str]

class TaskEphemeralStorageTypeDef(TypedDict):
    sizeInGiB: NotRequired[int]
    kmsKeyId: NotRequired[str]

class TaskManagedEBSVolumeTerminationPolicyTypeDef(TypedDict):
    deleteOnTermination: bool

class TmpfsTypeDef(TypedDict):
    containerPath: str
    size: int
    mountOptions: NotRequired[Sequence[str]]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateContainerAgentRequestTypeDef(TypedDict):
    containerInstance: str
    cluster: NotRequired[str]

class UpdateContainerInstancesStateRequestTypeDef(TypedDict):
    containerInstances: Sequence[str]
    status: ContainerInstanceStatusType
    cluster: NotRequired[str]

class UpdateServicePrimaryTaskSetRequestTypeDef(TypedDict):
    cluster: str
    service: str
    primaryTaskSet: str

class UpdateTaskProtectionRequestTypeDef(TypedDict):
    cluster: str
    tasks: Sequence[str]
    protectionEnabled: bool
    expiresInMinutes: NotRequired[int]

class SubmitAttachmentStateChangesRequestTypeDef(TypedDict):
    attachments: Sequence[AttachmentStateChangeTypeDef]
    cluster: NotRequired[str]

AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef",
    {
        "id": NotRequired[str],
        "type": NotRequired[str],
        "status": NotRequired[str],
        "details": NotRequired[List[KeyValuePairTypeDef]],
    },
)
ProxyConfigurationOutputTypeDef = TypedDict(
    "ProxyConfigurationOutputTypeDef",
    {
        "containerName": str,
        "type": NotRequired[Literal["APPMESH"]],
        "properties": NotRequired[List[KeyValuePairTypeDef]],
    },
)
ProxyConfigurationTypeDef = TypedDict(
    "ProxyConfigurationTypeDef",
    {
        "containerName": str,
        "type": NotRequired[Literal["APPMESH"]],
        "properties": NotRequired[Sequence[KeyValuePairTypeDef]],
    },
)

class DeleteAttributesRequestTypeDef(TypedDict):
    attributes: Sequence[AttributeTypeDef]
    cluster: NotRequired[str]

class PutAttributesRequestTypeDef(TypedDict):
    attributes: Sequence[AttributeTypeDef]
    cluster: NotRequired[str]

class AutoScalingGroupProviderTypeDef(TypedDict):
    autoScalingGroupArn: str
    managedScaling: NotRequired[ManagedScalingTypeDef]
    managedTerminationProtection: NotRequired[ManagedTerminationProtectionType]
    managedDraining: NotRequired[ManagedDrainingType]

class AutoScalingGroupProviderUpdateTypeDef(TypedDict):
    managedScaling: NotRequired[ManagedScalingTypeDef]
    managedTerminationProtection: NotRequired[ManagedTerminationProtectionType]
    managedDraining: NotRequired[ManagedDrainingType]

class NetworkConfigurationOutputTypeDef(TypedDict):
    awsvpcConfiguration: NotRequired[AwsVpcConfigurationOutputTypeDef]

class NetworkConfigurationTypeDef(TypedDict):
    awsvpcConfiguration: NotRequired[AwsVpcConfigurationTypeDef]

class PutClusterCapacityProvidersRequestTypeDef(TypedDict):
    cluster: str
    capacityProviders: Sequence[str]
    defaultCapacityProviderStrategy: Sequence[CapacityProviderStrategyItemTypeDef]

class EBSTagSpecificationOutputTypeDef(TypedDict):
    resourceType: Literal["volume"]
    tags: NotRequired[List[TagTypeDef]]
    propagateTags: NotRequired[PropagateTagsType]

class EBSTagSpecificationTypeDef(TypedDict):
    resourceType: Literal["volume"]
    tags: NotRequired[Sequence[TagTypeDef]]
    propagateTags: NotRequired[PropagateTagsType]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class UpdateClusterSettingsRequestTypeDef(TypedDict):
    cluster: str
    settings: Sequence[ClusterSettingTypeDef]

class ContainerOverrideOutputTypeDef(TypedDict):
    name: NotRequired[str]
    command: NotRequired[List[str]]
    environment: NotRequired[List[KeyValuePairTypeDef]]
    environmentFiles: NotRequired[List[EnvironmentFileTypeDef]]
    cpu: NotRequired[int]
    memory: NotRequired[int]
    memoryReservation: NotRequired[int]
    resourceRequirements: NotRequired[List[ResourceRequirementTypeDef]]

class ContainerOverrideTypeDef(TypedDict):
    name: NotRequired[str]
    command: NotRequired[Sequence[str]]
    environment: NotRequired[Sequence[KeyValuePairTypeDef]]
    environmentFiles: NotRequired[Sequence[EnvironmentFileTypeDef]]
    cpu: NotRequired[int]
    memory: NotRequired[int]
    memoryReservation: NotRequired[int]
    resourceRequirements: NotRequired[Sequence[ResourceRequirementTypeDef]]

class LogConfigurationOutputTypeDef(TypedDict):
    logDriver: LogDriverType
    options: NotRequired[Dict[str, str]]
    secretOptions: NotRequired[List[SecretTypeDef]]

class LogConfigurationTypeDef(TypedDict):
    logDriver: LogDriverType
    options: NotRequired[Mapping[str, str]]
    secretOptions: NotRequired[Sequence[SecretTypeDef]]

class ContainerInstanceHealthStatusTypeDef(TypedDict):
    overallStatus: NotRequired[InstanceHealthCheckStateType]
    details: NotRequired[List[InstanceHealthCheckResultTypeDef]]

ContainerRestartPolicyUnionTypeDef = Union[
    ContainerRestartPolicyTypeDef, ContainerRestartPolicyOutputTypeDef
]

class ContainerStateChangeTypeDef(TypedDict):
    containerName: NotRequired[str]
    imageDigest: NotRequired[str]
    runtimeId: NotRequired[str]
    exitCode: NotRequired[int]
    networkBindings: NotRequired[Sequence[NetworkBindingTypeDef]]
    reason: NotRequired[str]
    status: NotRequired[str]

class SubmitContainerStateChangeRequestTypeDef(TypedDict):
    cluster: NotRequired[str]
    task: NotRequired[str]
    containerName: NotRequired[str]
    runtimeId: NotRequired[str]
    status: NotRequired[str]
    exitCode: NotRequired[int]
    reason: NotRequired[str]
    networkBindings: NotRequired[Sequence[NetworkBindingTypeDef]]

class ContainerTypeDef(TypedDict):
    containerArn: NotRequired[str]
    taskArn: NotRequired[str]
    name: NotRequired[str]
    image: NotRequired[str]
    imageDigest: NotRequired[str]
    runtimeId: NotRequired[str]
    lastStatus: NotRequired[str]
    exitCode: NotRequired[int]
    reason: NotRequired[str]
    networkBindings: NotRequired[List[NetworkBindingTypeDef]]
    networkInterfaces: NotRequired[List[NetworkInterfaceTypeDef]]
    healthStatus: NotRequired[HealthStatusType]
    managedAgents: NotRequired[List[ManagedAgentTypeDef]]
    cpu: NotRequired[str]
    memory: NotRequired[str]
    memoryReservation: NotRequired[str]
    gpuIds: NotRequired[List[str]]

class DeleteAttributesResponseTypeDef(TypedDict):
    attributes: List[AttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DiscoverPollEndpointResponseTypeDef(TypedDict):
    endpoint: str
    telemetryEndpoint: str
    serviceConnectEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttributesResponseTypeDef(TypedDict):
    attributes: List[AttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListClustersResponseTypeDef(TypedDict):
    clusterArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListContainerInstancesResponseTypeDef(TypedDict):
    containerInstanceArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListServicesByNamespaceResponseTypeDef(TypedDict):
    serviceArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListServicesResponseTypeDef(TypedDict):
    serviceArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTaskDefinitionFamiliesResponseTypeDef(TypedDict):
    families: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTaskDefinitionsResponseTypeDef(TypedDict):
    taskDefinitionArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTasksResponseTypeDef(TypedDict):
    taskArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PutAttributesResponseTypeDef(TypedDict):
    attributes: List[AttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StopServiceDeploymentResponseTypeDef(TypedDict):
    serviceDeploymentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubmitAttachmentStateChangesResponseTypeDef(TypedDict):
    acknowledgment: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubmitContainerStateChangeResponseTypeDef(TypedDict):
    acknowledgment: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubmitTaskStateChangeResponseTypeDef(TypedDict):
    acknowledgment: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTaskSetRequestTypeDef(TypedDict):
    cluster: str
    service: str
    taskSet: str
    scale: ScaleTypeDef

class CreatedAtTypeDef(TypedDict):
    before: NotRequired[TimestampTypeDef]
    after: NotRequired[TimestampTypeDef]

class DeleteAccountSettingResponseTypeDef(TypedDict):
    setting: SettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountSettingsResponseTypeDef(TypedDict):
    settings: List[SettingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PutAccountSettingDefaultResponseTypeDef(TypedDict):
    setting: SettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutAccountSettingResponseTypeDef(TypedDict):
    setting: SettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentConfigurationOutputTypeDef(TypedDict):
    deploymentCircuitBreaker: NotRequired[DeploymentCircuitBreakerTypeDef]
    maximumPercent: NotRequired[int]
    minimumHealthyPercent: NotRequired[int]
    alarms: NotRequired[DeploymentAlarmsOutputTypeDef]

class DeploymentConfigurationTypeDef(TypedDict):
    deploymentCircuitBreaker: NotRequired[DeploymentCircuitBreakerTypeDef]
    maximumPercent: NotRequired[int]
    minimumHealthyPercent: NotRequired[int]
    alarms: NotRequired[DeploymentAlarmsTypeDef]

class DescribeServicesRequestWaitExtraTypeDef(TypedDict):
    services: Sequence[str]
    cluster: NotRequired[str]
    include: NotRequired[Sequence[Literal["TAGS"]]]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeServicesRequestWaitTypeDef(TypedDict):
    services: Sequence[str]
    cluster: NotRequired[str]
    include: NotRequired[Sequence[Literal["TAGS"]]]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeTasksRequestWaitExtraTypeDef(TypedDict):
    tasks: Sequence[str]
    cluster: NotRequired[str]
    include: NotRequired[Sequence[Literal["TAGS"]]]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeTasksRequestWaitTypeDef(TypedDict):
    tasks: Sequence[str]
    cluster: NotRequired[str]
    include: NotRequired[Sequence[Literal["TAGS"]]]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

DeviceUnionTypeDef = Union[DeviceTypeDef, DeviceOutputTypeDef]
DockerVolumeConfigurationUnionTypeDef = Union[
    DockerVolumeConfigurationTypeDef, DockerVolumeConfigurationOutputTypeDef
]

class EFSVolumeConfigurationTypeDef(TypedDict):
    fileSystemId: str
    rootDirectory: NotRequired[str]
    transitEncryption: NotRequired[EFSTransitEncryptionType]
    transitEncryptionPort: NotRequired[int]
    authorizationConfig: NotRequired[EFSAuthorizationConfigTypeDef]

class ExecuteCommandConfigurationTypeDef(TypedDict):
    kmsKeyId: NotRequired[str]
    logging: NotRequired[ExecuteCommandLoggingType]
    logConfiguration: NotRequired[ExecuteCommandLogConfigurationTypeDef]

class ExecuteCommandResponseTypeDef(TypedDict):
    clusterArn: str
    containerArn: str
    containerName: str
    interactive: bool
    session: SessionTypeDef
    taskArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class FSxWindowsFileServerVolumeConfigurationTypeDef(TypedDict):
    fileSystemId: str
    rootDirectory: str
    authorizationConfig: FSxWindowsFileServerAuthorizationConfigTypeDef

FirelensConfigurationUnionTypeDef = Union[
    FirelensConfigurationTypeDef, FirelensConfigurationOutputTypeDef
]

class GetTaskProtectionResponseTypeDef(TypedDict):
    protectedTasks: List[ProtectedTaskTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTaskProtectionResponseTypeDef(TypedDict):
    protectedTasks: List[ProtectedTaskTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

HealthCheckUnionTypeDef = Union[HealthCheckTypeDef, HealthCheckOutputTypeDef]
KernelCapabilitiesUnionTypeDef = Union[KernelCapabilitiesTypeDef, KernelCapabilitiesOutputTypeDef]

class LinuxParametersOutputTypeDef(TypedDict):
    capabilities: NotRequired[KernelCapabilitiesOutputTypeDef]
    devices: NotRequired[List[DeviceOutputTypeDef]]
    initProcessEnabled: NotRequired[bool]
    sharedMemorySize: NotRequired[int]
    tmpfs: NotRequired[List[TmpfsOutputTypeDef]]
    maxSwap: NotRequired[int]
    swappiness: NotRequired[int]

class ListAccountSettingsRequestPaginateTypeDef(TypedDict):
    name: NotRequired[SettingNameType]
    value: NotRequired[str]
    principalArn: NotRequired[str]
    effectiveSettings: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAttributesRequestPaginateTypeDef(TypedDict):
    targetType: Literal["container-instance"]
    cluster: NotRequired[str]
    attributeName: NotRequired[str]
    attributeValue: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListClustersRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListContainerInstancesRequestPaginateTypeDef = TypedDict(
    "ListContainerInstancesRequestPaginateTypeDef",
    {
        "cluster": NotRequired[str],
        "filter": NotRequired[str],
        "status": NotRequired[ContainerInstanceStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListServicesByNamespaceRequestPaginateTypeDef(TypedDict):
    namespace: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServicesRequestPaginateTypeDef(TypedDict):
    cluster: NotRequired[str]
    launchType: NotRequired[LaunchTypeType]
    schedulingStrategy: NotRequired[SchedulingStrategyType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTaskDefinitionFamiliesRequestPaginateTypeDef(TypedDict):
    familyPrefix: NotRequired[str]
    status: NotRequired[TaskDefinitionFamilyStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTaskDefinitionsRequestPaginateTypeDef(TypedDict):
    familyPrefix: NotRequired[str]
    status: NotRequired[TaskDefinitionStatusType]
    sort: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTasksRequestPaginateTypeDef(TypedDict):
    cluster: NotRequired[str]
    containerInstance: NotRequired[str]
    family: NotRequired[str]
    startedBy: NotRequired[str]
    serviceName: NotRequired[str]
    desiredStatus: NotRequired[DesiredStatusType]
    launchType: NotRequired[LaunchTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceDeploymentsResponseTypeDef(TypedDict):
    serviceDeployments: List[ServiceDeploymentBriefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ResourceUnionTypeDef = Union[ResourceTypeDef, ResourceOutputTypeDef]

class ServiceConnectTlsConfigurationTypeDef(TypedDict):
    issuerCertificateAuthority: ServiceConnectTlsCertificateAuthorityTypeDef
    kmsKey: NotRequired[str]
    roleArn: NotRequired[str]

TmpfsUnionTypeDef = Union[TmpfsTypeDef, TmpfsOutputTypeDef]
ProxyConfigurationUnionTypeDef = Union[ProxyConfigurationTypeDef, ProxyConfigurationOutputTypeDef]

class CapacityProviderTypeDef(TypedDict):
    capacityProviderArn: NotRequired[str]
    name: NotRequired[str]
    status: NotRequired[CapacityProviderStatusType]
    autoScalingGroupProvider: NotRequired[AutoScalingGroupProviderTypeDef]
    updateStatus: NotRequired[CapacityProviderUpdateStatusType]
    updateStatusReason: NotRequired[str]
    tags: NotRequired[List[TagTypeDef]]

class CreateCapacityProviderRequestTypeDef(TypedDict):
    name: str
    autoScalingGroupProvider: AutoScalingGroupProviderTypeDef
    tags: NotRequired[Sequence[TagTypeDef]]

class UpdateCapacityProviderRequestTypeDef(TypedDict):
    name: str
    autoScalingGroupProvider: AutoScalingGroupProviderUpdateTypeDef

TaskSetTypeDef = TypedDict(
    "TaskSetTypeDef",
    {
        "id": NotRequired[str],
        "taskSetArn": NotRequired[str],
        "serviceArn": NotRequired[str],
        "clusterArn": NotRequired[str],
        "startedBy": NotRequired[str],
        "externalId": NotRequired[str],
        "status": NotRequired[str],
        "taskDefinition": NotRequired[str],
        "computedDesiredCount": NotRequired[int],
        "pendingCount": NotRequired[int],
        "runningCount": NotRequired[int],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "launchType": NotRequired[LaunchTypeType],
        "capacityProviderStrategy": NotRequired[List[CapacityProviderStrategyItemTypeDef]],
        "platformVersion": NotRequired[str],
        "platformFamily": NotRequired[str],
        "networkConfiguration": NotRequired[NetworkConfigurationOutputTypeDef],
        "loadBalancers": NotRequired[List[LoadBalancerTypeDef]],
        "serviceRegistries": NotRequired[List[ServiceRegistryTypeDef]],
        "scale": NotRequired[ScaleTypeDef],
        "stabilityStatus": NotRequired[StabilityStatusType],
        "stabilityStatusAt": NotRequired[datetime],
        "tags": NotRequired[List[TagTypeDef]],
        "fargateEphemeralStorage": NotRequired[DeploymentEphemeralStorageTypeDef],
    },
)
NetworkConfigurationUnionTypeDef = Union[
    NetworkConfigurationTypeDef, NetworkConfigurationOutputTypeDef
]

class ServiceManagedEBSVolumeConfigurationOutputTypeDef(TypedDict):
    roleArn: str
    encrypted: NotRequired[bool]
    kmsKeyId: NotRequired[str]
    volumeType: NotRequired[str]
    sizeInGiB: NotRequired[int]
    snapshotId: NotRequired[str]
    iops: NotRequired[int]
    throughput: NotRequired[int]
    tagSpecifications: NotRequired[List[EBSTagSpecificationOutputTypeDef]]
    filesystemType: NotRequired[TaskFilesystemTypeType]

EBSTagSpecificationUnionTypeDef = Union[
    EBSTagSpecificationTypeDef, EBSTagSpecificationOutputTypeDef
]

class TaskOverrideOutputTypeDef(TypedDict):
    containerOverrides: NotRequired[List[ContainerOverrideOutputTypeDef]]
    cpu: NotRequired[str]
    inferenceAcceleratorOverrides: NotRequired[List[InferenceAcceleratorOverrideTypeDef]]
    executionRoleArn: NotRequired[str]
    memory: NotRequired[str]
    taskRoleArn: NotRequired[str]
    ephemeralStorage: NotRequired[EphemeralStorageTypeDef]

class TaskOverrideTypeDef(TypedDict):
    containerOverrides: NotRequired[Sequence[ContainerOverrideTypeDef]]
    cpu: NotRequired[str]
    inferenceAcceleratorOverrides: NotRequired[Sequence[InferenceAcceleratorOverrideTypeDef]]
    executionRoleArn: NotRequired[str]
    memory: NotRequired[str]
    taskRoleArn: NotRequired[str]
    ephemeralStorage: NotRequired[EphemeralStorageTypeDef]

LogConfigurationUnionTypeDef = Union[LogConfigurationTypeDef, LogConfigurationOutputTypeDef]

class ContainerInstanceTypeDef(TypedDict):
    containerInstanceArn: NotRequired[str]
    ec2InstanceId: NotRequired[str]
    capacityProviderName: NotRequired[str]
    version: NotRequired[int]
    versionInfo: NotRequired[VersionInfoTypeDef]
    remainingResources: NotRequired[List[ResourceOutputTypeDef]]
    registeredResources: NotRequired[List[ResourceOutputTypeDef]]
    status: NotRequired[str]
    statusReason: NotRequired[str]
    agentConnected: NotRequired[bool]
    runningTasksCount: NotRequired[int]
    pendingTasksCount: NotRequired[int]
    agentUpdateStatus: NotRequired[AgentUpdateStatusType]
    attributes: NotRequired[List[AttributeTypeDef]]
    registeredAt: NotRequired[datetime]
    attachments: NotRequired[List[AttachmentTypeDef]]
    tags: NotRequired[List[TagTypeDef]]
    healthStatus: NotRequired[ContainerInstanceHealthStatusTypeDef]

class SubmitTaskStateChangeRequestTypeDef(TypedDict):
    cluster: NotRequired[str]
    task: NotRequired[str]
    status: NotRequired[str]
    reason: NotRequired[str]
    containers: NotRequired[Sequence[ContainerStateChangeTypeDef]]
    attachments: NotRequired[Sequence[AttachmentStateChangeTypeDef]]
    managedAgents: NotRequired[Sequence[ManagedAgentStateChangeTypeDef]]
    pullStartedAt: NotRequired[TimestampTypeDef]
    pullStoppedAt: NotRequired[TimestampTypeDef]
    executionStoppedAt: NotRequired[TimestampTypeDef]

class ListServiceDeploymentsRequestTypeDef(TypedDict):
    service: str
    cluster: NotRequired[str]
    status: NotRequired[Sequence[ServiceDeploymentStatusType]]
    createdAt: NotRequired[CreatedAtTypeDef]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ServiceDeploymentTypeDef(TypedDict):
    serviceDeploymentArn: NotRequired[str]
    serviceArn: NotRequired[str]
    clusterArn: NotRequired[str]
    createdAt: NotRequired[datetime]
    startedAt: NotRequired[datetime]
    finishedAt: NotRequired[datetime]
    stoppedAt: NotRequired[datetime]
    updatedAt: NotRequired[datetime]
    sourceServiceRevisions: NotRequired[List[ServiceRevisionSummaryTypeDef]]
    targetServiceRevision: NotRequired[ServiceRevisionSummaryTypeDef]
    status: NotRequired[ServiceDeploymentStatusType]
    statusReason: NotRequired[str]
    deploymentConfiguration: NotRequired[DeploymentConfigurationOutputTypeDef]
    rollback: NotRequired[RollbackTypeDef]
    deploymentCircuitBreaker: NotRequired[ServiceDeploymentCircuitBreakerTypeDef]
    alarms: NotRequired[ServiceDeploymentAlarmsTypeDef]

DeploymentConfigurationUnionTypeDef = Union[
    DeploymentConfigurationTypeDef, DeploymentConfigurationOutputTypeDef
]

class ClusterConfigurationTypeDef(TypedDict):
    executeCommandConfiguration: NotRequired[ExecuteCommandConfigurationTypeDef]
    managedStorageConfiguration: NotRequired[ManagedStorageConfigurationTypeDef]

class VolumeOutputTypeDef(TypedDict):
    name: NotRequired[str]
    host: NotRequired[HostVolumePropertiesTypeDef]
    dockerVolumeConfiguration: NotRequired[DockerVolumeConfigurationOutputTypeDef]
    efsVolumeConfiguration: NotRequired[EFSVolumeConfigurationTypeDef]
    fsxWindowsFileServerVolumeConfiguration: NotRequired[
        FSxWindowsFileServerVolumeConfigurationTypeDef
    ]
    configuredAtLaunch: NotRequired[bool]

class VolumeTypeDef(TypedDict):
    name: NotRequired[str]
    host: NotRequired[HostVolumePropertiesTypeDef]
    dockerVolumeConfiguration: NotRequired[DockerVolumeConfigurationUnionTypeDef]
    efsVolumeConfiguration: NotRequired[EFSVolumeConfigurationTypeDef]
    fsxWindowsFileServerVolumeConfiguration: NotRequired[
        FSxWindowsFileServerVolumeConfigurationTypeDef
    ]
    configuredAtLaunch: NotRequired[bool]

class ContainerDefinitionOutputTypeDef(TypedDict):
    name: NotRequired[str]
    image: NotRequired[str]
    repositoryCredentials: NotRequired[RepositoryCredentialsTypeDef]
    cpu: NotRequired[int]
    memory: NotRequired[int]
    memoryReservation: NotRequired[int]
    links: NotRequired[List[str]]
    portMappings: NotRequired[List[PortMappingTypeDef]]
    essential: NotRequired[bool]
    restartPolicy: NotRequired[ContainerRestartPolicyOutputTypeDef]
    entryPoint: NotRequired[List[str]]
    command: NotRequired[List[str]]
    environment: NotRequired[List[KeyValuePairTypeDef]]
    environmentFiles: NotRequired[List[EnvironmentFileTypeDef]]
    mountPoints: NotRequired[List[MountPointTypeDef]]
    volumesFrom: NotRequired[List[VolumeFromTypeDef]]
    linuxParameters: NotRequired[LinuxParametersOutputTypeDef]
    secrets: NotRequired[List[SecretTypeDef]]
    dependsOn: NotRequired[List[ContainerDependencyTypeDef]]
    startTimeout: NotRequired[int]
    stopTimeout: NotRequired[int]
    versionConsistency: NotRequired[VersionConsistencyType]
    hostname: NotRequired[str]
    user: NotRequired[str]
    workingDirectory: NotRequired[str]
    disableNetworking: NotRequired[bool]
    privileged: NotRequired[bool]
    readonlyRootFilesystem: NotRequired[bool]
    dnsServers: NotRequired[List[str]]
    dnsSearchDomains: NotRequired[List[str]]
    extraHosts: NotRequired[List[HostEntryTypeDef]]
    dockerSecurityOptions: NotRequired[List[str]]
    interactive: NotRequired[bool]
    pseudoTerminal: NotRequired[bool]
    dockerLabels: NotRequired[Dict[str, str]]
    ulimits: NotRequired[List[UlimitTypeDef]]
    logConfiguration: NotRequired[LogConfigurationOutputTypeDef]
    healthCheck: NotRequired[HealthCheckOutputTypeDef]
    systemControls: NotRequired[List[SystemControlTypeDef]]
    resourceRequirements: NotRequired[List[ResourceRequirementTypeDef]]
    firelensConfiguration: NotRequired[FirelensConfigurationOutputTypeDef]
    credentialSpecs: NotRequired[List[str]]

class RegisterContainerInstanceRequestTypeDef(TypedDict):
    cluster: NotRequired[str]
    instanceIdentityDocument: NotRequired[str]
    instanceIdentityDocumentSignature: NotRequired[str]
    totalResources: NotRequired[Sequence[ResourceUnionTypeDef]]
    versionInfo: NotRequired[VersionInfoTypeDef]
    containerInstanceArn: NotRequired[str]
    attributes: NotRequired[Sequence[AttributeTypeDef]]
    platformDevices: NotRequired[Sequence[PlatformDeviceTypeDef]]
    tags: NotRequired[Sequence[TagTypeDef]]

class ServiceConnectServiceOutputTypeDef(TypedDict):
    portName: str
    discoveryName: NotRequired[str]
    clientAliases: NotRequired[List[ServiceConnectClientAliasTypeDef]]
    ingressPortOverride: NotRequired[int]
    timeout: NotRequired[TimeoutConfigurationTypeDef]
    tls: NotRequired[ServiceConnectTlsConfigurationTypeDef]

class ServiceConnectServiceTypeDef(TypedDict):
    portName: str
    discoveryName: NotRequired[str]
    clientAliases: NotRequired[Sequence[ServiceConnectClientAliasTypeDef]]
    ingressPortOverride: NotRequired[int]
    timeout: NotRequired[TimeoutConfigurationTypeDef]
    tls: NotRequired[ServiceConnectTlsConfigurationTypeDef]

class LinuxParametersTypeDef(TypedDict):
    capabilities: NotRequired[KernelCapabilitiesUnionTypeDef]
    devices: NotRequired[Sequence[DeviceUnionTypeDef]]
    initProcessEnabled: NotRequired[bool]
    sharedMemorySize: NotRequired[int]
    tmpfs: NotRequired[Sequence[TmpfsUnionTypeDef]]
    maxSwap: NotRequired[int]
    swappiness: NotRequired[int]

class CreateCapacityProviderResponseTypeDef(TypedDict):
    capacityProvider: CapacityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCapacityProviderResponseTypeDef(TypedDict):
    capacityProvider: CapacityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCapacityProvidersResponseTypeDef(TypedDict):
    capacityProviders: List[CapacityProviderTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateCapacityProviderResponseTypeDef(TypedDict):
    capacityProvider: CapacityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTaskSetResponseTypeDef(TypedDict):
    taskSet: TaskSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTaskSetResponseTypeDef(TypedDict):
    taskSet: TaskSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTaskSetsResponseTypeDef(TypedDict):
    taskSets: List[TaskSetTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServicePrimaryTaskSetResponseTypeDef(TypedDict):
    taskSet: TaskSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTaskSetResponseTypeDef(TypedDict):
    taskSet: TaskSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTaskSetRequestTypeDef(TypedDict):
    service: str
    cluster: str
    taskDefinition: str
    externalId: NotRequired[str]
    networkConfiguration: NotRequired[NetworkConfigurationUnionTypeDef]
    loadBalancers: NotRequired[Sequence[LoadBalancerTypeDef]]
    serviceRegistries: NotRequired[Sequence[ServiceRegistryTypeDef]]
    launchType: NotRequired[LaunchTypeType]
    capacityProviderStrategy: NotRequired[Sequence[CapacityProviderStrategyItemTypeDef]]
    platformVersion: NotRequired[str]
    scale: NotRequired[ScaleTypeDef]
    clientToken: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class ServiceVolumeConfigurationOutputTypeDef(TypedDict):
    name: str
    managedEBSVolume: NotRequired[ServiceManagedEBSVolumeConfigurationOutputTypeDef]

class ServiceManagedEBSVolumeConfigurationTypeDef(TypedDict):
    roleArn: str
    encrypted: NotRequired[bool]
    kmsKeyId: NotRequired[str]
    volumeType: NotRequired[str]
    sizeInGiB: NotRequired[int]
    snapshotId: NotRequired[str]
    iops: NotRequired[int]
    throughput: NotRequired[int]
    tagSpecifications: NotRequired[Sequence[EBSTagSpecificationUnionTypeDef]]
    filesystemType: NotRequired[TaskFilesystemTypeType]

class TaskManagedEBSVolumeConfigurationTypeDef(TypedDict):
    roleArn: str
    encrypted: NotRequired[bool]
    kmsKeyId: NotRequired[str]
    volumeType: NotRequired[str]
    sizeInGiB: NotRequired[int]
    snapshotId: NotRequired[str]
    iops: NotRequired[int]
    throughput: NotRequired[int]
    tagSpecifications: NotRequired[Sequence[EBSTagSpecificationUnionTypeDef]]
    terminationPolicy: NotRequired[TaskManagedEBSVolumeTerminationPolicyTypeDef]
    filesystemType: NotRequired[TaskFilesystemTypeType]

class TaskTypeDef(TypedDict):
    attachments: NotRequired[List[AttachmentTypeDef]]
    attributes: NotRequired[List[AttributeTypeDef]]
    availabilityZone: NotRequired[str]
    capacityProviderName: NotRequired[str]
    clusterArn: NotRequired[str]
    connectivity: NotRequired[ConnectivityType]
    connectivityAt: NotRequired[datetime]
    containerInstanceArn: NotRequired[str]
    containers: NotRequired[List[ContainerTypeDef]]
    cpu: NotRequired[str]
    createdAt: NotRequired[datetime]
    desiredStatus: NotRequired[str]
    enableExecuteCommand: NotRequired[bool]
    executionStoppedAt: NotRequired[datetime]
    group: NotRequired[str]
    healthStatus: NotRequired[HealthStatusType]
    inferenceAccelerators: NotRequired[List[InferenceAcceleratorTypeDef]]
    lastStatus: NotRequired[str]
    launchType: NotRequired[LaunchTypeType]
    memory: NotRequired[str]
    overrides: NotRequired[TaskOverrideOutputTypeDef]
    platformVersion: NotRequired[str]
    platformFamily: NotRequired[str]
    pullStartedAt: NotRequired[datetime]
    pullStoppedAt: NotRequired[datetime]
    startedAt: NotRequired[datetime]
    startedBy: NotRequired[str]
    stopCode: NotRequired[TaskStopCodeType]
    stoppedAt: NotRequired[datetime]
    stoppedReason: NotRequired[str]
    stoppingAt: NotRequired[datetime]
    tags: NotRequired[List[TagTypeDef]]
    taskArn: NotRequired[str]
    taskDefinitionArn: NotRequired[str]
    version: NotRequired[int]
    ephemeralStorage: NotRequired[EphemeralStorageTypeDef]
    fargateEphemeralStorage: NotRequired[TaskEphemeralStorageTypeDef]

TaskOverrideUnionTypeDef = Union[TaskOverrideTypeDef, TaskOverrideOutputTypeDef]

class DeregisterContainerInstanceResponseTypeDef(TypedDict):
    containerInstance: ContainerInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeContainerInstancesResponseTypeDef(TypedDict):
    containerInstances: List[ContainerInstanceTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterContainerInstanceResponseTypeDef(TypedDict):
    containerInstance: ContainerInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContainerAgentResponseTypeDef(TypedDict):
    containerInstance: ContainerInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContainerInstancesStateResponseTypeDef(TypedDict):
    containerInstances: List[ContainerInstanceTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServiceDeploymentsResponseTypeDef(TypedDict):
    serviceDeployments: List[ServiceDeploymentTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterTypeDef(TypedDict):
    clusterArn: NotRequired[str]
    clusterName: NotRequired[str]
    configuration: NotRequired[ClusterConfigurationTypeDef]
    status: NotRequired[str]
    registeredContainerInstancesCount: NotRequired[int]
    runningTasksCount: NotRequired[int]
    pendingTasksCount: NotRequired[int]
    activeServicesCount: NotRequired[int]
    statistics: NotRequired[List[KeyValuePairTypeDef]]
    tags: NotRequired[List[TagTypeDef]]
    settings: NotRequired[List[ClusterSettingTypeDef]]
    capacityProviders: NotRequired[List[str]]
    defaultCapacityProviderStrategy: NotRequired[List[CapacityProviderStrategyItemTypeDef]]
    attachments: NotRequired[List[AttachmentTypeDef]]
    attachmentsStatus: NotRequired[str]
    serviceConnectDefaults: NotRequired[ClusterServiceConnectDefaultsTypeDef]

class CreateClusterRequestTypeDef(TypedDict):
    clusterName: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    settings: NotRequired[Sequence[ClusterSettingTypeDef]]
    configuration: NotRequired[ClusterConfigurationTypeDef]
    capacityProviders: NotRequired[Sequence[str]]
    defaultCapacityProviderStrategy: NotRequired[Sequence[CapacityProviderStrategyItemTypeDef]]
    serviceConnectDefaults: NotRequired[ClusterServiceConnectDefaultsRequestTypeDef]

class UpdateClusterRequestTypeDef(TypedDict):
    cluster: str
    settings: NotRequired[Sequence[ClusterSettingTypeDef]]
    configuration: NotRequired[ClusterConfigurationTypeDef]
    serviceConnectDefaults: NotRequired[ClusterServiceConnectDefaultsRequestTypeDef]

VolumeUnionTypeDef = Union[VolumeTypeDef, VolumeOutputTypeDef]

class TaskDefinitionTypeDef(TypedDict):
    taskDefinitionArn: NotRequired[str]
    containerDefinitions: NotRequired[List[ContainerDefinitionOutputTypeDef]]
    family: NotRequired[str]
    taskRoleArn: NotRequired[str]
    executionRoleArn: NotRequired[str]
    networkMode: NotRequired[NetworkModeType]
    revision: NotRequired[int]
    volumes: NotRequired[List[VolumeOutputTypeDef]]
    status: NotRequired[TaskDefinitionStatusType]
    requiresAttributes: NotRequired[List[AttributeTypeDef]]
    placementConstraints: NotRequired[List[TaskDefinitionPlacementConstraintTypeDef]]
    compatibilities: NotRequired[List[CompatibilityType]]
    runtimePlatform: NotRequired[RuntimePlatformTypeDef]
    requiresCompatibilities: NotRequired[List[CompatibilityType]]
    cpu: NotRequired[str]
    memory: NotRequired[str]
    inferenceAccelerators: NotRequired[List[InferenceAcceleratorTypeDef]]
    pidMode: NotRequired[PidModeType]
    ipcMode: NotRequired[IpcModeType]
    proxyConfiguration: NotRequired[ProxyConfigurationOutputTypeDef]
    registeredAt: NotRequired[datetime]
    deregisteredAt: NotRequired[datetime]
    registeredBy: NotRequired[str]
    ephemeralStorage: NotRequired[EphemeralStorageTypeDef]
    enableFaultInjection: NotRequired[bool]

class ServiceConnectConfigurationOutputTypeDef(TypedDict):
    enabled: bool
    namespace: NotRequired[str]
    services: NotRequired[List[ServiceConnectServiceOutputTypeDef]]
    logConfiguration: NotRequired[LogConfigurationOutputTypeDef]

class ServiceConnectConfigurationTypeDef(TypedDict):
    enabled: bool
    namespace: NotRequired[str]
    services: NotRequired[Sequence[ServiceConnectServiceTypeDef]]
    logConfiguration: NotRequired[LogConfigurationTypeDef]

LinuxParametersUnionTypeDef = Union[LinuxParametersTypeDef, LinuxParametersOutputTypeDef]
ServiceManagedEBSVolumeConfigurationUnionTypeDef = Union[
    ServiceManagedEBSVolumeConfigurationTypeDef, ServiceManagedEBSVolumeConfigurationOutputTypeDef
]

class TaskVolumeConfigurationTypeDef(TypedDict):
    name: str
    managedEBSVolume: NotRequired[TaskManagedEBSVolumeConfigurationTypeDef]

class DescribeTasksResponseTypeDef(TypedDict):
    tasks: List[TaskTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RunTaskResponseTypeDef(TypedDict):
    tasks: List[TaskTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartTaskResponseTypeDef(TypedDict):
    tasks: List[TaskTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StopTaskResponseTypeDef(TypedDict):
    task: TaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterResponseTypeDef(TypedDict):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterResponseTypeDef(TypedDict):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClustersResponseTypeDef(TypedDict):
    clusters: List[ClusterTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutClusterCapacityProvidersResponseTypeDef(TypedDict):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterResponseTypeDef(TypedDict):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterSettingsResponseTypeDef(TypedDict):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTaskDefinitionsResponseTypeDef(TypedDict):
    taskDefinitions: List[TaskDefinitionTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterTaskDefinitionResponseTypeDef(TypedDict):
    taskDefinition: TaskDefinitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTaskDefinitionResponseTypeDef(TypedDict):
    taskDefinition: TaskDefinitionTypeDef
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterTaskDefinitionResponseTypeDef(TypedDict):
    taskDefinition: TaskDefinitionTypeDef
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "id": NotRequired[str],
        "status": NotRequired[str],
        "taskDefinition": NotRequired[str],
        "desiredCount": NotRequired[int],
        "pendingCount": NotRequired[int],
        "runningCount": NotRequired[int],
        "failedTasks": NotRequired[int],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "capacityProviderStrategy": NotRequired[List[CapacityProviderStrategyItemTypeDef]],
        "launchType": NotRequired[LaunchTypeType],
        "platformVersion": NotRequired[str],
        "platformFamily": NotRequired[str],
        "networkConfiguration": NotRequired[NetworkConfigurationOutputTypeDef],
        "rolloutState": NotRequired[DeploymentRolloutStateType],
        "rolloutStateReason": NotRequired[str],
        "serviceConnectConfiguration": NotRequired[ServiceConnectConfigurationOutputTypeDef],
        "serviceConnectResources": NotRequired[List[ServiceConnectServiceResourceTypeDef]],
        "volumeConfigurations": NotRequired[List[ServiceVolumeConfigurationOutputTypeDef]],
        "fargateEphemeralStorage": NotRequired[DeploymentEphemeralStorageTypeDef],
        "vpcLatticeConfigurations": NotRequired[List[VpcLatticeConfigurationTypeDef]],
    },
)

class ServiceRevisionTypeDef(TypedDict):
    serviceRevisionArn: NotRequired[str]
    serviceArn: NotRequired[str]
    clusterArn: NotRequired[str]
    taskDefinition: NotRequired[str]
    capacityProviderStrategy: NotRequired[List[CapacityProviderStrategyItemTypeDef]]
    launchType: NotRequired[LaunchTypeType]
    platformVersion: NotRequired[str]
    platformFamily: NotRequired[str]
    loadBalancers: NotRequired[List[LoadBalancerTypeDef]]
    serviceRegistries: NotRequired[List[ServiceRegistryTypeDef]]
    networkConfiguration: NotRequired[NetworkConfigurationOutputTypeDef]
    containerImages: NotRequired[List[ContainerImageTypeDef]]
    guardDutyEnabled: NotRequired[bool]
    serviceConnectConfiguration: NotRequired[ServiceConnectConfigurationOutputTypeDef]
    volumeConfigurations: NotRequired[List[ServiceVolumeConfigurationOutputTypeDef]]
    fargateEphemeralStorage: NotRequired[DeploymentEphemeralStorageTypeDef]
    createdAt: NotRequired[datetime]
    vpcLatticeConfigurations: NotRequired[List[VpcLatticeConfigurationTypeDef]]

ServiceConnectConfigurationUnionTypeDef = Union[
    ServiceConnectConfigurationTypeDef, ServiceConnectConfigurationOutputTypeDef
]

class ContainerDefinitionTypeDef(TypedDict):
    name: NotRequired[str]
    image: NotRequired[str]
    repositoryCredentials: NotRequired[RepositoryCredentialsTypeDef]
    cpu: NotRequired[int]
    memory: NotRequired[int]
    memoryReservation: NotRequired[int]
    links: NotRequired[Sequence[str]]
    portMappings: NotRequired[Sequence[PortMappingTypeDef]]
    essential: NotRequired[bool]
    restartPolicy: NotRequired[ContainerRestartPolicyUnionTypeDef]
    entryPoint: NotRequired[Sequence[str]]
    command: NotRequired[Sequence[str]]
    environment: NotRequired[Sequence[KeyValuePairTypeDef]]
    environmentFiles: NotRequired[Sequence[EnvironmentFileTypeDef]]
    mountPoints: NotRequired[Sequence[MountPointTypeDef]]
    volumesFrom: NotRequired[Sequence[VolumeFromTypeDef]]
    linuxParameters: NotRequired[LinuxParametersUnionTypeDef]
    secrets: NotRequired[Sequence[SecretTypeDef]]
    dependsOn: NotRequired[Sequence[ContainerDependencyTypeDef]]
    startTimeout: NotRequired[int]
    stopTimeout: NotRequired[int]
    versionConsistency: NotRequired[VersionConsistencyType]
    hostname: NotRequired[str]
    user: NotRequired[str]
    workingDirectory: NotRequired[str]
    disableNetworking: NotRequired[bool]
    privileged: NotRequired[bool]
    readonlyRootFilesystem: NotRequired[bool]
    dnsServers: NotRequired[Sequence[str]]
    dnsSearchDomains: NotRequired[Sequence[str]]
    extraHosts: NotRequired[Sequence[HostEntryTypeDef]]
    dockerSecurityOptions: NotRequired[Sequence[str]]
    interactive: NotRequired[bool]
    pseudoTerminal: NotRequired[bool]
    dockerLabels: NotRequired[Mapping[str, str]]
    ulimits: NotRequired[Sequence[UlimitTypeDef]]
    logConfiguration: NotRequired[LogConfigurationUnionTypeDef]
    healthCheck: NotRequired[HealthCheckUnionTypeDef]
    systemControls: NotRequired[Sequence[SystemControlTypeDef]]
    resourceRequirements: NotRequired[Sequence[ResourceRequirementTypeDef]]
    firelensConfiguration: NotRequired[FirelensConfigurationUnionTypeDef]
    credentialSpecs: NotRequired[Sequence[str]]

class ServiceVolumeConfigurationTypeDef(TypedDict):
    name: str
    managedEBSVolume: NotRequired[ServiceManagedEBSVolumeConfigurationUnionTypeDef]

class RunTaskRequestTypeDef(TypedDict):
    taskDefinition: str
    capacityProviderStrategy: NotRequired[Sequence[CapacityProviderStrategyItemTypeDef]]
    cluster: NotRequired[str]
    count: NotRequired[int]
    enableECSManagedTags: NotRequired[bool]
    enableExecuteCommand: NotRequired[bool]
    group: NotRequired[str]
    launchType: NotRequired[LaunchTypeType]
    networkConfiguration: NotRequired[NetworkConfigurationUnionTypeDef]
    overrides: NotRequired[TaskOverrideUnionTypeDef]
    placementConstraints: NotRequired[Sequence[PlacementConstraintTypeDef]]
    placementStrategy: NotRequired[Sequence[PlacementStrategyTypeDef]]
    platformVersion: NotRequired[str]
    propagateTags: NotRequired[PropagateTagsType]
    referenceId: NotRequired[str]
    startedBy: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    clientToken: NotRequired[str]
    volumeConfigurations: NotRequired[Sequence[TaskVolumeConfigurationTypeDef]]

class StartTaskRequestTypeDef(TypedDict):
    containerInstances: Sequence[str]
    taskDefinition: str
    cluster: NotRequired[str]
    enableECSManagedTags: NotRequired[bool]
    enableExecuteCommand: NotRequired[bool]
    group: NotRequired[str]
    networkConfiguration: NotRequired[NetworkConfigurationUnionTypeDef]
    overrides: NotRequired[TaskOverrideUnionTypeDef]
    propagateTags: NotRequired[PropagateTagsType]
    referenceId: NotRequired[str]
    startedBy: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    volumeConfigurations: NotRequired[Sequence[TaskVolumeConfigurationTypeDef]]

class ServiceTypeDef(TypedDict):
    serviceArn: NotRequired[str]
    serviceName: NotRequired[str]
    clusterArn: NotRequired[str]
    loadBalancers: NotRequired[List[LoadBalancerTypeDef]]
    serviceRegistries: NotRequired[List[ServiceRegistryTypeDef]]
    status: NotRequired[str]
    desiredCount: NotRequired[int]
    runningCount: NotRequired[int]
    pendingCount: NotRequired[int]
    launchType: NotRequired[LaunchTypeType]
    capacityProviderStrategy: NotRequired[List[CapacityProviderStrategyItemTypeDef]]
    platformVersion: NotRequired[str]
    platformFamily: NotRequired[str]
    taskDefinition: NotRequired[str]
    deploymentConfiguration: NotRequired[DeploymentConfigurationOutputTypeDef]
    taskSets: NotRequired[List[TaskSetTypeDef]]
    deployments: NotRequired[List[DeploymentTypeDef]]
    roleArn: NotRequired[str]
    events: NotRequired[List[ServiceEventTypeDef]]
    createdAt: NotRequired[datetime]
    placementConstraints: NotRequired[List[PlacementConstraintTypeDef]]
    placementStrategy: NotRequired[List[PlacementStrategyTypeDef]]
    networkConfiguration: NotRequired[NetworkConfigurationOutputTypeDef]
    healthCheckGracePeriodSeconds: NotRequired[int]
    schedulingStrategy: NotRequired[SchedulingStrategyType]
    deploymentController: NotRequired[DeploymentControllerTypeDef]
    tags: NotRequired[List[TagTypeDef]]
    createdBy: NotRequired[str]
    enableECSManagedTags: NotRequired[bool]
    propagateTags: NotRequired[PropagateTagsType]
    enableExecuteCommand: NotRequired[bool]
    availabilityZoneRebalancing: NotRequired[AvailabilityZoneRebalancingType]

class DescribeServiceRevisionsResponseTypeDef(TypedDict):
    serviceRevisions: List[ServiceRevisionTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

ContainerDefinitionUnionTypeDef = Union[
    ContainerDefinitionTypeDef, ContainerDefinitionOutputTypeDef
]
ServiceVolumeConfigurationUnionTypeDef = Union[
    ServiceVolumeConfigurationTypeDef, ServiceVolumeConfigurationOutputTypeDef
]

class CreateServiceResponseTypeDef(TypedDict):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceResponseTypeDef(TypedDict):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServicesResponseTypeDef(TypedDict):
    services: List[ServiceTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceResponseTypeDef(TypedDict):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterTaskDefinitionRequestTypeDef(TypedDict):
    family: str
    containerDefinitions: Sequence[ContainerDefinitionUnionTypeDef]
    taskRoleArn: NotRequired[str]
    executionRoleArn: NotRequired[str]
    networkMode: NotRequired[NetworkModeType]
    volumes: NotRequired[Sequence[VolumeUnionTypeDef]]
    placementConstraints: NotRequired[Sequence[TaskDefinitionPlacementConstraintTypeDef]]
    requiresCompatibilities: NotRequired[Sequence[CompatibilityType]]
    cpu: NotRequired[str]
    memory: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    pidMode: NotRequired[PidModeType]
    ipcMode: NotRequired[IpcModeType]
    proxyConfiguration: NotRequired[ProxyConfigurationUnionTypeDef]
    inferenceAccelerators: NotRequired[Sequence[InferenceAcceleratorTypeDef]]
    ephemeralStorage: NotRequired[EphemeralStorageTypeDef]
    runtimePlatform: NotRequired[RuntimePlatformTypeDef]
    enableFaultInjection: NotRequired[bool]

class CreateServiceRequestTypeDef(TypedDict):
    serviceName: str
    cluster: NotRequired[str]
    taskDefinition: NotRequired[str]
    availabilityZoneRebalancing: NotRequired[AvailabilityZoneRebalancingType]
    loadBalancers: NotRequired[Sequence[LoadBalancerTypeDef]]
    serviceRegistries: NotRequired[Sequence[ServiceRegistryTypeDef]]
    desiredCount: NotRequired[int]
    clientToken: NotRequired[str]
    launchType: NotRequired[LaunchTypeType]
    capacityProviderStrategy: NotRequired[Sequence[CapacityProviderStrategyItemTypeDef]]
    platformVersion: NotRequired[str]
    role: NotRequired[str]
    deploymentConfiguration: NotRequired[DeploymentConfigurationUnionTypeDef]
    placementConstraints: NotRequired[Sequence[PlacementConstraintTypeDef]]
    placementStrategy: NotRequired[Sequence[PlacementStrategyTypeDef]]
    networkConfiguration: NotRequired[NetworkConfigurationUnionTypeDef]
    healthCheckGracePeriodSeconds: NotRequired[int]
    schedulingStrategy: NotRequired[SchedulingStrategyType]
    deploymentController: NotRequired[DeploymentControllerTypeDef]
    tags: NotRequired[Sequence[TagTypeDef]]
    enableECSManagedTags: NotRequired[bool]
    propagateTags: NotRequired[PropagateTagsType]
    enableExecuteCommand: NotRequired[bool]
    serviceConnectConfiguration: NotRequired[ServiceConnectConfigurationUnionTypeDef]
    volumeConfigurations: NotRequired[Sequence[ServiceVolumeConfigurationUnionTypeDef]]
    vpcLatticeConfigurations: NotRequired[Sequence[VpcLatticeConfigurationTypeDef]]

class UpdateServiceRequestTypeDef(TypedDict):
    service: str
    cluster: NotRequired[str]
    desiredCount: NotRequired[int]
    taskDefinition: NotRequired[str]
    capacityProviderStrategy: NotRequired[Sequence[CapacityProviderStrategyItemTypeDef]]
    deploymentConfiguration: NotRequired[DeploymentConfigurationUnionTypeDef]
    availabilityZoneRebalancing: NotRequired[AvailabilityZoneRebalancingType]
    networkConfiguration: NotRequired[NetworkConfigurationUnionTypeDef]
    placementConstraints: NotRequired[Sequence[PlacementConstraintTypeDef]]
    placementStrategy: NotRequired[Sequence[PlacementStrategyTypeDef]]
    platformVersion: NotRequired[str]
    forceNewDeployment: NotRequired[bool]
    healthCheckGracePeriodSeconds: NotRequired[int]
    enableExecuteCommand: NotRequired[bool]
    enableECSManagedTags: NotRequired[bool]
    loadBalancers: NotRequired[Sequence[LoadBalancerTypeDef]]
    propagateTags: NotRequired[PropagateTagsType]
    serviceRegistries: NotRequired[Sequence[ServiceRegistryTypeDef]]
    serviceConnectConfiguration: NotRequired[ServiceConnectConfigurationUnionTypeDef]
    volumeConfigurations: NotRequired[Sequence[ServiceVolumeConfigurationUnionTypeDef]]
    vpcLatticeConfigurations: NotRequired[Sequence[VpcLatticeConfigurationTypeDef]]
