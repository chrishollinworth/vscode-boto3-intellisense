"""
Type annotations for ecs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ecs.type_defs import AttachmentStateChangeTypeDef

    data: AttachmentStateChangeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AgentUpdateStatusType,
    AssignPublicIpType,
    CapacityProviderStatusType,
    CapacityProviderUpdateStatusType,
    ClusterFieldType,
    CompatibilityType,
    ConnectivityType,
    ContainerConditionType,
    ContainerInstanceStatusType,
    DeploymentControllerTypeType,
    DeploymentRolloutStateType,
    DesiredStatusType,
    DeviceCgroupPermissionType,
    EFSAuthorizationConfigIAMType,
    EFSTransitEncryptionType,
    ExecuteCommandLoggingType,
    FirelensConfigurationTypeType,
    HealthStatusType,
    IpcModeType,
    LaunchTypeType,
    LogDriverType,
    ManagedScalingStatusType,
    ManagedTerminationProtectionType,
    NetworkModeType,
    PidModeType,
    PlacementConstraintTypeType,
    PlacementStrategyTypeType,
    PropagateTagsType,
    ResourceTypeType,
    SchedulingStrategyType,
    ScopeType,
    SettingNameType,
    SortOrderType,
    StabilityStatusType,
    TaskDefinitionFamilyStatusType,
    TaskDefinitionStatusType,
    TaskStopCodeType,
    TransportProtocolType,
    UlimitNameType,
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
    "AttachmentStateChangeTypeDef",
    "AttachmentTypeDef",
    "AttributeTypeDef",
    "AutoScalingGroupProviderTypeDef",
    "AutoScalingGroupProviderUpdateTypeDef",
    "AwsVpcConfigurationTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "CapacityProviderTypeDef",
    "ClusterConfigurationTypeDef",
    "ClusterSettingTypeDef",
    "ClusterTypeDef",
    "ContainerDefinitionTypeDef",
    "ContainerDependencyTypeDef",
    "ContainerInstanceTypeDef",
    "ContainerOverrideTypeDef",
    "ContainerStateChangeTypeDef",
    "ContainerTypeDef",
    "CreateCapacityProviderRequestRequestTypeDef",
    "CreateCapacityProviderResponseTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateServiceRequestRequestTypeDef",
    "CreateServiceResponseTypeDef",
    "CreateTaskSetRequestRequestTypeDef",
    "CreateTaskSetResponseTypeDef",
    "DeleteAccountSettingRequestRequestTypeDef",
    "DeleteAccountSettingResponseTypeDef",
    "DeleteAttributesRequestRequestTypeDef",
    "DeleteAttributesResponseTypeDef",
    "DeleteCapacityProviderRequestRequestTypeDef",
    "DeleteCapacityProviderResponseTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteServiceRequestRequestTypeDef",
    "DeleteServiceResponseTypeDef",
    "DeleteTaskSetRequestRequestTypeDef",
    "DeleteTaskSetResponseTypeDef",
    "DeploymentCircuitBreakerTypeDef",
    "DeploymentConfigurationTypeDef",
    "DeploymentControllerTypeDef",
    "DeploymentTypeDef",
    "DeregisterContainerInstanceRequestRequestTypeDef",
    "DeregisterContainerInstanceResponseTypeDef",
    "DeregisterTaskDefinitionRequestRequestTypeDef",
    "DeregisterTaskDefinitionResponseTypeDef",
    "DescribeCapacityProvidersRequestRequestTypeDef",
    "DescribeCapacityProvidersResponseTypeDef",
    "DescribeClustersRequestRequestTypeDef",
    "DescribeClustersResponseTypeDef",
    "DescribeContainerInstancesRequestRequestTypeDef",
    "DescribeContainerInstancesResponseTypeDef",
    "DescribeServicesRequestRequestTypeDef",
    "DescribeServicesResponseTypeDef",
    "DescribeTaskDefinitionRequestRequestTypeDef",
    "DescribeTaskDefinitionResponseTypeDef",
    "DescribeTaskSetsRequestRequestTypeDef",
    "DescribeTaskSetsResponseTypeDef",
    "DescribeTasksRequestRequestTypeDef",
    "DescribeTasksResponseTypeDef",
    "DeviceTypeDef",
    "DiscoverPollEndpointRequestRequestTypeDef",
    "DiscoverPollEndpointResponseTypeDef",
    "DockerVolumeConfigurationTypeDef",
    "EFSAuthorizationConfigTypeDef",
    "EFSVolumeConfigurationTypeDef",
    "EnvironmentFileTypeDef",
    "EphemeralStorageTypeDef",
    "ExecuteCommandConfigurationTypeDef",
    "ExecuteCommandLogConfigurationTypeDef",
    "ExecuteCommandRequestRequestTypeDef",
    "ExecuteCommandResponseTypeDef",
    "FSxWindowsFileServerAuthorizationConfigTypeDef",
    "FSxWindowsFileServerVolumeConfigurationTypeDef",
    "FailureTypeDef",
    "FirelensConfigurationTypeDef",
    "HealthCheckTypeDef",
    "HostEntryTypeDef",
    "HostVolumePropertiesTypeDef",
    "InferenceAcceleratorOverrideTypeDef",
    "InferenceAcceleratorTypeDef",
    "KernelCapabilitiesTypeDef",
    "KeyValuePairTypeDef",
    "LinuxParametersTypeDef",
    "ListAccountSettingsRequestRequestTypeDef",
    "ListAccountSettingsResponseTypeDef",
    "ListAttributesRequestRequestTypeDef",
    "ListAttributesResponseTypeDef",
    "ListClustersRequestRequestTypeDef",
    "ListClustersResponseTypeDef",
    "ListContainerInstancesRequestRequestTypeDef",
    "ListContainerInstancesResponseTypeDef",
    "ListServicesRequestRequestTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTaskDefinitionFamiliesRequestRequestTypeDef",
    "ListTaskDefinitionFamiliesResponseTypeDef",
    "ListTaskDefinitionsRequestRequestTypeDef",
    "ListTaskDefinitionsResponseTypeDef",
    "ListTasksRequestRequestTypeDef",
    "ListTasksResponseTypeDef",
    "LoadBalancerTypeDef",
    "LogConfigurationTypeDef",
    "ManagedAgentStateChangeTypeDef",
    "ManagedAgentTypeDef",
    "ManagedScalingTypeDef",
    "MountPointTypeDef",
    "NetworkBindingTypeDef",
    "NetworkConfigurationTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "PlatformDeviceTypeDef",
    "PortMappingTypeDef",
    "ProxyConfigurationTypeDef",
    "PutAccountSettingDefaultRequestRequestTypeDef",
    "PutAccountSettingDefaultResponseTypeDef",
    "PutAccountSettingRequestRequestTypeDef",
    "PutAccountSettingResponseTypeDef",
    "PutAttributesRequestRequestTypeDef",
    "PutAttributesResponseTypeDef",
    "PutClusterCapacityProvidersRequestRequestTypeDef",
    "PutClusterCapacityProvidersResponseTypeDef",
    "RegisterContainerInstanceRequestRequestTypeDef",
    "RegisterContainerInstanceResponseTypeDef",
    "RegisterTaskDefinitionRequestRequestTypeDef",
    "RegisterTaskDefinitionResponseTypeDef",
    "RepositoryCredentialsTypeDef",
    "ResourceRequirementTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RunTaskRequestRequestTypeDef",
    "RunTaskResponseTypeDef",
    "ScaleTypeDef",
    "SecretTypeDef",
    "ServiceEventTypeDef",
    "ServiceRegistryTypeDef",
    "ServiceTypeDef",
    "SessionTypeDef",
    "SettingTypeDef",
    "StartTaskRequestRequestTypeDef",
    "StartTaskResponseTypeDef",
    "StopTaskRequestRequestTypeDef",
    "StopTaskResponseTypeDef",
    "SubmitAttachmentStateChangesRequestRequestTypeDef",
    "SubmitAttachmentStateChangesResponseTypeDef",
    "SubmitContainerStateChangeRequestRequestTypeDef",
    "SubmitContainerStateChangeResponseTypeDef",
    "SubmitTaskStateChangeRequestRequestTypeDef",
    "SubmitTaskStateChangeResponseTypeDef",
    "SystemControlTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TaskDefinitionPlacementConstraintTypeDef",
    "TaskDefinitionTypeDef",
    "TaskOverrideTypeDef",
    "TaskSetTypeDef",
    "TaskTypeDef",
    "TmpfsTypeDef",
    "UlimitTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCapacityProviderRequestRequestTypeDef",
    "UpdateCapacityProviderResponseTypeDef",
    "UpdateClusterRequestRequestTypeDef",
    "UpdateClusterResponseTypeDef",
    "UpdateClusterSettingsRequestRequestTypeDef",
    "UpdateClusterSettingsResponseTypeDef",
    "UpdateContainerAgentRequestRequestTypeDef",
    "UpdateContainerAgentResponseTypeDef",
    "UpdateContainerInstancesStateRequestRequestTypeDef",
    "UpdateContainerInstancesStateResponseTypeDef",
    "UpdateServicePrimaryTaskSetRequestRequestTypeDef",
    "UpdateServicePrimaryTaskSetResponseTypeDef",
    "UpdateServiceRequestRequestTypeDef",
    "UpdateServiceResponseTypeDef",
    "UpdateTaskSetRequestRequestTypeDef",
    "UpdateTaskSetResponseTypeDef",
    "VersionInfoTypeDef",
    "VolumeFromTypeDef",
    "VolumeTypeDef",
    "WaiterConfigTypeDef",
)

AttachmentStateChangeTypeDef = TypedDict(
    "AttachmentStateChangeTypeDef",
    {
        "attachmentArn": str,
        "status": str,
    },
)

AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List["KeyValuePairTypeDef"],
    },
    total=False,
)

_RequiredAttributeTypeDef = TypedDict(
    "_RequiredAttributeTypeDef",
    {
        "name": str,
    },
)
_OptionalAttributeTypeDef = TypedDict(
    "_OptionalAttributeTypeDef",
    {
        "value": str,
        "targetType": Literal["container-instance"],
        "targetId": str,
    },
    total=False,
)

class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass

_RequiredAutoScalingGroupProviderTypeDef = TypedDict(
    "_RequiredAutoScalingGroupProviderTypeDef",
    {
        "autoScalingGroupArn": str,
    },
)
_OptionalAutoScalingGroupProviderTypeDef = TypedDict(
    "_OptionalAutoScalingGroupProviderTypeDef",
    {
        "managedScaling": "ManagedScalingTypeDef",
        "managedTerminationProtection": ManagedTerminationProtectionType,
    },
    total=False,
)

class AutoScalingGroupProviderTypeDef(
    _RequiredAutoScalingGroupProviderTypeDef, _OptionalAutoScalingGroupProviderTypeDef
):
    pass

AutoScalingGroupProviderUpdateTypeDef = TypedDict(
    "AutoScalingGroupProviderUpdateTypeDef",
    {
        "managedScaling": "ManagedScalingTypeDef",
        "managedTerminationProtection": ManagedTerminationProtectionType,
    },
    total=False,
)

_RequiredAwsVpcConfigurationTypeDef = TypedDict(
    "_RequiredAwsVpcConfigurationTypeDef",
    {
        "subnets": List[str],
    },
)
_OptionalAwsVpcConfigurationTypeDef = TypedDict(
    "_OptionalAwsVpcConfigurationTypeDef",
    {
        "securityGroups": List[str],
        "assignPublicIp": AssignPublicIpType,
    },
    total=False,
)

class AwsVpcConfigurationTypeDef(
    _RequiredAwsVpcConfigurationTypeDef, _OptionalAwsVpcConfigurationTypeDef
):
    pass

_RequiredCapacityProviderStrategyItemTypeDef = TypedDict(
    "_RequiredCapacityProviderStrategyItemTypeDef",
    {
        "capacityProvider": str,
    },
)
_OptionalCapacityProviderStrategyItemTypeDef = TypedDict(
    "_OptionalCapacityProviderStrategyItemTypeDef",
    {
        "weight": int,
        "base": int,
    },
    total=False,
)

class CapacityProviderStrategyItemTypeDef(
    _RequiredCapacityProviderStrategyItemTypeDef, _OptionalCapacityProviderStrategyItemTypeDef
):
    pass

CapacityProviderTypeDef = TypedDict(
    "CapacityProviderTypeDef",
    {
        "capacityProviderArn": str,
        "name": str,
        "status": CapacityProviderStatusType,
        "autoScalingGroupProvider": "AutoScalingGroupProviderTypeDef",
        "updateStatus": CapacityProviderUpdateStatusType,
        "updateStatusReason": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

ClusterConfigurationTypeDef = TypedDict(
    "ClusterConfigurationTypeDef",
    {
        "executeCommandConfiguration": "ExecuteCommandConfigurationTypeDef",
    },
    total=False,
)

ClusterSettingTypeDef = TypedDict(
    "ClusterSettingTypeDef",
    {
        "name": Literal["containerInsights"],
        "value": str,
    },
    total=False,
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "clusterArn": str,
        "clusterName": str,
        "configuration": "ClusterConfigurationTypeDef",
        "status": str,
        "registeredContainerInstancesCount": int,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "activeServicesCount": int,
        "statistics": List["KeyValuePairTypeDef"],
        "tags": List["TagTypeDef"],
        "settings": List["ClusterSettingTypeDef"],
        "capacityProviders": List[str],
        "defaultCapacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "attachments": List["AttachmentTypeDef"],
        "attachmentsStatus": str,
    },
    total=False,
)

ContainerDefinitionTypeDef = TypedDict(
    "ContainerDefinitionTypeDef",
    {
        "name": str,
        "image": str,
        "repositoryCredentials": "RepositoryCredentialsTypeDef",
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "links": List[str],
        "portMappings": List["PortMappingTypeDef"],
        "essential": bool,
        "entryPoint": List[str],
        "command": List[str],
        "environment": List["KeyValuePairTypeDef"],
        "environmentFiles": List["EnvironmentFileTypeDef"],
        "mountPoints": List["MountPointTypeDef"],
        "volumesFrom": List["VolumeFromTypeDef"],
        "linuxParameters": "LinuxParametersTypeDef",
        "secrets": List["SecretTypeDef"],
        "dependsOn": List["ContainerDependencyTypeDef"],
        "startTimeout": int,
        "stopTimeout": int,
        "hostname": str,
        "user": str,
        "workingDirectory": str,
        "disableNetworking": bool,
        "privileged": bool,
        "readonlyRootFilesystem": bool,
        "dnsServers": List[str],
        "dnsSearchDomains": List[str],
        "extraHosts": List["HostEntryTypeDef"],
        "dockerSecurityOptions": List[str],
        "interactive": bool,
        "pseudoTerminal": bool,
        "dockerLabels": Dict[str, str],
        "ulimits": List["UlimitTypeDef"],
        "logConfiguration": "LogConfigurationTypeDef",
        "healthCheck": "HealthCheckTypeDef",
        "systemControls": List["SystemControlTypeDef"],
        "resourceRequirements": List["ResourceRequirementTypeDef"],
        "firelensConfiguration": "FirelensConfigurationTypeDef",
    },
    total=False,
)

ContainerDependencyTypeDef = TypedDict(
    "ContainerDependencyTypeDef",
    {
        "containerName": str,
        "condition": ContainerConditionType,
    },
)

ContainerInstanceTypeDef = TypedDict(
    "ContainerInstanceTypeDef",
    {
        "containerInstanceArn": str,
        "ec2InstanceId": str,
        "capacityProviderName": str,
        "version": int,
        "versionInfo": "VersionInfoTypeDef",
        "remainingResources": List["ResourceTypeDef"],
        "registeredResources": List["ResourceTypeDef"],
        "status": str,
        "statusReason": str,
        "agentConnected": bool,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "agentUpdateStatus": AgentUpdateStatusType,
        "attributes": List["AttributeTypeDef"],
        "registeredAt": datetime,
        "attachments": List["AttachmentTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

ContainerOverrideTypeDef = TypedDict(
    "ContainerOverrideTypeDef",
    {
        "name": str,
        "command": List[str],
        "environment": List["KeyValuePairTypeDef"],
        "environmentFiles": List["EnvironmentFileTypeDef"],
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "resourceRequirements": List["ResourceRequirementTypeDef"],
    },
    total=False,
)

ContainerStateChangeTypeDef = TypedDict(
    "ContainerStateChangeTypeDef",
    {
        "containerName": str,
        "imageDigest": str,
        "runtimeId": str,
        "exitCode": int,
        "networkBindings": List["NetworkBindingTypeDef"],
        "reason": str,
        "status": str,
    },
    total=False,
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "containerArn": str,
        "taskArn": str,
        "name": str,
        "image": str,
        "imageDigest": str,
        "runtimeId": str,
        "lastStatus": str,
        "exitCode": int,
        "reason": str,
        "networkBindings": List["NetworkBindingTypeDef"],
        "networkInterfaces": List["NetworkInterfaceTypeDef"],
        "healthStatus": HealthStatusType,
        "managedAgents": List["ManagedAgentTypeDef"],
        "cpu": str,
        "memory": str,
        "memoryReservation": str,
        "gpuIds": List[str],
    },
    total=False,
)

_RequiredCreateCapacityProviderRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCapacityProviderRequestRequestTypeDef",
    {
        "name": str,
        "autoScalingGroupProvider": "AutoScalingGroupProviderTypeDef",
    },
)
_OptionalCreateCapacityProviderRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCapacityProviderRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateCapacityProviderRequestRequestTypeDef(
    _RequiredCreateCapacityProviderRequestRequestTypeDef,
    _OptionalCreateCapacityProviderRequestRequestTypeDef,
):
    pass

CreateCapacityProviderResponseTypeDef = TypedDict(
    "CreateCapacityProviderResponseTypeDef",
    {
        "capacityProvider": "CapacityProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClusterRequestRequestTypeDef = TypedDict(
    "CreateClusterRequestRequestTypeDef",
    {
        "clusterName": str,
        "tags": List["TagTypeDef"],
        "settings": List["ClusterSettingTypeDef"],
        "configuration": "ClusterConfigurationTypeDef",
        "capacityProviders": List[str],
        "defaultCapacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
    },
    total=False,
)

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateServiceRequestRequestTypeDef",
    {
        "serviceName": str,
    },
)
_OptionalCreateServiceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateServiceRequestRequestTypeDef",
    {
        "cluster": str,
        "taskDefinition": str,
        "loadBalancers": List["LoadBalancerTypeDef"],
        "serviceRegistries": List["ServiceRegistryTypeDef"],
        "desiredCount": int,
        "clientToken": str,
        "launchType": LaunchTypeType,
        "capacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "platformVersion": str,
        "role": str,
        "deploymentConfiguration": "DeploymentConfigurationTypeDef",
        "placementConstraints": List["PlacementConstraintTypeDef"],
        "placementStrategy": List["PlacementStrategyTypeDef"],
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "healthCheckGracePeriodSeconds": int,
        "schedulingStrategy": SchedulingStrategyType,
        "deploymentController": "DeploymentControllerTypeDef",
        "tags": List["TagTypeDef"],
        "enableECSManagedTags": bool,
        "propagateTags": PropagateTagsType,
        "enableExecuteCommand": bool,
    },
    total=False,
)

class CreateServiceRequestRequestTypeDef(
    _RequiredCreateServiceRequestRequestTypeDef, _OptionalCreateServiceRequestRequestTypeDef
):
    pass

CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTaskSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTaskSetRequestRequestTypeDef",
    {
        "service": str,
        "cluster": str,
        "taskDefinition": str,
    },
)
_OptionalCreateTaskSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTaskSetRequestRequestTypeDef",
    {
        "externalId": str,
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "loadBalancers": List["LoadBalancerTypeDef"],
        "serviceRegistries": List["ServiceRegistryTypeDef"],
        "launchType": LaunchTypeType,
        "capacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "platformVersion": str,
        "scale": "ScaleTypeDef",
        "clientToken": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateTaskSetRequestRequestTypeDef(
    _RequiredCreateTaskSetRequestRequestTypeDef, _OptionalCreateTaskSetRequestRequestTypeDef
):
    pass

CreateTaskSetResponseTypeDef = TypedDict(
    "CreateTaskSetResponseTypeDef",
    {
        "taskSet": "TaskSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAccountSettingRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAccountSettingRequestRequestTypeDef",
    {
        "name": SettingNameType,
    },
)
_OptionalDeleteAccountSettingRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAccountSettingRequestRequestTypeDef",
    {
        "principalArn": str,
    },
    total=False,
)

class DeleteAccountSettingRequestRequestTypeDef(
    _RequiredDeleteAccountSettingRequestRequestTypeDef,
    _OptionalDeleteAccountSettingRequestRequestTypeDef,
):
    pass

DeleteAccountSettingResponseTypeDef = TypedDict(
    "DeleteAccountSettingResponseTypeDef",
    {
        "setting": "SettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAttributesRequestRequestTypeDef",
    {
        "attributes": List["AttributeTypeDef"],
    },
)
_OptionalDeleteAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAttributesRequestRequestTypeDef",
    {
        "cluster": str,
    },
    total=False,
)

class DeleteAttributesRequestRequestTypeDef(
    _RequiredDeleteAttributesRequestRequestTypeDef, _OptionalDeleteAttributesRequestRequestTypeDef
):
    pass

DeleteAttributesResponseTypeDef = TypedDict(
    "DeleteAttributesResponseTypeDef",
    {
        "attributes": List["AttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCapacityProviderRequestRequestTypeDef = TypedDict(
    "DeleteCapacityProviderRequestRequestTypeDef",
    {
        "capacityProvider": str,
    },
)

DeleteCapacityProviderResponseTypeDef = TypedDict(
    "DeleteCapacityProviderResponseTypeDef",
    {
        "capacityProvider": "CapacityProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterRequestRequestTypeDef = TypedDict(
    "DeleteClusterRequestRequestTypeDef",
    {
        "cluster": str,
    },
)

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteServiceRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteServiceRequestRequestTypeDef",
    {
        "service": str,
    },
)
_OptionalDeleteServiceRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteServiceRequestRequestTypeDef",
    {
        "cluster": str,
        "force": bool,
    },
    total=False,
)

class DeleteServiceRequestRequestTypeDef(
    _RequiredDeleteServiceRequestRequestTypeDef, _OptionalDeleteServiceRequestRequestTypeDef
):
    pass

DeleteServiceResponseTypeDef = TypedDict(
    "DeleteServiceResponseTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTaskSetRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTaskSetRequestRequestTypeDef",
    {
        "cluster": str,
        "service": str,
        "taskSet": str,
    },
)
_OptionalDeleteTaskSetRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTaskSetRequestRequestTypeDef",
    {
        "force": bool,
    },
    total=False,
)

class DeleteTaskSetRequestRequestTypeDef(
    _RequiredDeleteTaskSetRequestRequestTypeDef, _OptionalDeleteTaskSetRequestRequestTypeDef
):
    pass

DeleteTaskSetResponseTypeDef = TypedDict(
    "DeleteTaskSetResponseTypeDef",
    {
        "taskSet": "TaskSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeploymentCircuitBreakerTypeDef = TypedDict(
    "DeploymentCircuitBreakerTypeDef",
    {
        "enable": bool,
        "rollback": bool,
    },
)

DeploymentConfigurationTypeDef = TypedDict(
    "DeploymentConfigurationTypeDef",
    {
        "deploymentCircuitBreaker": "DeploymentCircuitBreakerTypeDef",
        "maximumPercent": int,
        "minimumHealthyPercent": int,
    },
    total=False,
)

DeploymentControllerTypeDef = TypedDict(
    "DeploymentControllerTypeDef",
    {
        "type": DeploymentControllerTypeType,
    },
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "id": str,
        "status": str,
        "taskDefinition": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "failedTasks": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "capacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "launchType": LaunchTypeType,
        "platformVersion": str,
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "rolloutState": DeploymentRolloutStateType,
        "rolloutStateReason": str,
    },
    total=False,
)

_RequiredDeregisterContainerInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredDeregisterContainerInstanceRequestRequestTypeDef",
    {
        "containerInstance": str,
    },
)
_OptionalDeregisterContainerInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalDeregisterContainerInstanceRequestRequestTypeDef",
    {
        "cluster": str,
        "force": bool,
    },
    total=False,
)

class DeregisterContainerInstanceRequestRequestTypeDef(
    _RequiredDeregisterContainerInstanceRequestRequestTypeDef,
    _OptionalDeregisterContainerInstanceRequestRequestTypeDef,
):
    pass

DeregisterContainerInstanceResponseTypeDef = TypedDict(
    "DeregisterContainerInstanceResponseTypeDef",
    {
        "containerInstance": "ContainerInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterTaskDefinitionRequestRequestTypeDef = TypedDict(
    "DeregisterTaskDefinitionRequestRequestTypeDef",
    {
        "taskDefinition": str,
    },
)

DeregisterTaskDefinitionResponseTypeDef = TypedDict(
    "DeregisterTaskDefinitionResponseTypeDef",
    {
        "taskDefinition": "TaskDefinitionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCapacityProvidersRequestRequestTypeDef = TypedDict(
    "DescribeCapacityProvidersRequestRequestTypeDef",
    {
        "capacityProviders": List[str],
        "include": List[Literal["TAGS"]],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeCapacityProvidersResponseTypeDef = TypedDict(
    "DescribeCapacityProvidersResponseTypeDef",
    {
        "capacityProviders": List["CapacityProviderTypeDef"],
        "failures": List["FailureTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClustersRequestRequestTypeDef = TypedDict(
    "DescribeClustersRequestRequestTypeDef",
    {
        "clusters": List[str],
        "include": List[ClusterFieldType],
    },
    total=False,
)

DescribeClustersResponseTypeDef = TypedDict(
    "DescribeClustersResponseTypeDef",
    {
        "clusters": List["ClusterTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeContainerInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeContainerInstancesRequestRequestTypeDef",
    {
        "containerInstances": List[str],
    },
)
_OptionalDescribeContainerInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeContainerInstancesRequestRequestTypeDef",
    {
        "cluster": str,
        "include": List[Literal["TAGS"]],
    },
    total=False,
)

class DescribeContainerInstancesRequestRequestTypeDef(
    _RequiredDescribeContainerInstancesRequestRequestTypeDef,
    _OptionalDescribeContainerInstancesRequestRequestTypeDef,
):
    pass

DescribeContainerInstancesResponseTypeDef = TypedDict(
    "DescribeContainerInstancesResponseTypeDef",
    {
        "containerInstances": List["ContainerInstanceTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeServicesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeServicesRequestRequestTypeDef",
    {
        "services": List[str],
    },
)
_OptionalDescribeServicesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeServicesRequestRequestTypeDef",
    {
        "cluster": str,
        "include": List[Literal["TAGS"]],
    },
    total=False,
)

class DescribeServicesRequestRequestTypeDef(
    _RequiredDescribeServicesRequestRequestTypeDef, _OptionalDescribeServicesRequestRequestTypeDef
):
    pass

DescribeServicesResponseTypeDef = TypedDict(
    "DescribeServicesResponseTypeDef",
    {
        "services": List["ServiceTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTaskDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeTaskDefinitionRequestRequestTypeDef",
    {
        "taskDefinition": str,
    },
)
_OptionalDescribeTaskDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeTaskDefinitionRequestRequestTypeDef",
    {
        "include": List[Literal["TAGS"]],
    },
    total=False,
)

class DescribeTaskDefinitionRequestRequestTypeDef(
    _RequiredDescribeTaskDefinitionRequestRequestTypeDef,
    _OptionalDescribeTaskDefinitionRequestRequestTypeDef,
):
    pass

DescribeTaskDefinitionResponseTypeDef = TypedDict(
    "DescribeTaskDefinitionResponseTypeDef",
    {
        "taskDefinition": "TaskDefinitionTypeDef",
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTaskSetsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeTaskSetsRequestRequestTypeDef",
    {
        "cluster": str,
        "service": str,
    },
)
_OptionalDescribeTaskSetsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeTaskSetsRequestRequestTypeDef",
    {
        "taskSets": List[str],
        "include": List[Literal["TAGS"]],
    },
    total=False,
)

class DescribeTaskSetsRequestRequestTypeDef(
    _RequiredDescribeTaskSetsRequestRequestTypeDef, _OptionalDescribeTaskSetsRequestRequestTypeDef
):
    pass

DescribeTaskSetsResponseTypeDef = TypedDict(
    "DescribeTaskSetsResponseTypeDef",
    {
        "taskSets": List["TaskSetTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTasksRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeTasksRequestRequestTypeDef",
    {
        "tasks": List[str],
    },
)
_OptionalDescribeTasksRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeTasksRequestRequestTypeDef",
    {
        "cluster": str,
        "include": List[Literal["TAGS"]],
    },
    total=False,
)

class DescribeTasksRequestRequestTypeDef(
    _RequiredDescribeTasksRequestRequestTypeDef, _OptionalDescribeTasksRequestRequestTypeDef
):
    pass

DescribeTasksResponseTypeDef = TypedDict(
    "DescribeTasksResponseTypeDef",
    {
        "tasks": List["TaskTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeviceTypeDef = TypedDict(
    "_RequiredDeviceTypeDef",
    {
        "hostPath": str,
    },
)
_OptionalDeviceTypeDef = TypedDict(
    "_OptionalDeviceTypeDef",
    {
        "containerPath": str,
        "permissions": List[DeviceCgroupPermissionType],
    },
    total=False,
)

class DeviceTypeDef(_RequiredDeviceTypeDef, _OptionalDeviceTypeDef):
    pass

DiscoverPollEndpointRequestRequestTypeDef = TypedDict(
    "DiscoverPollEndpointRequestRequestTypeDef",
    {
        "containerInstance": str,
        "cluster": str,
    },
    total=False,
)

DiscoverPollEndpointResponseTypeDef = TypedDict(
    "DiscoverPollEndpointResponseTypeDef",
    {
        "endpoint": str,
        "telemetryEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DockerVolumeConfigurationTypeDef = TypedDict(
    "DockerVolumeConfigurationTypeDef",
    {
        "scope": ScopeType,
        "autoprovision": bool,
        "driver": str,
        "driverOpts": Dict[str, str],
        "labels": Dict[str, str],
    },
    total=False,
)

EFSAuthorizationConfigTypeDef = TypedDict(
    "EFSAuthorizationConfigTypeDef",
    {
        "accessPointId": str,
        "iam": EFSAuthorizationConfigIAMType,
    },
    total=False,
)

_RequiredEFSVolumeConfigurationTypeDef = TypedDict(
    "_RequiredEFSVolumeConfigurationTypeDef",
    {
        "fileSystemId": str,
    },
)
_OptionalEFSVolumeConfigurationTypeDef = TypedDict(
    "_OptionalEFSVolumeConfigurationTypeDef",
    {
        "rootDirectory": str,
        "transitEncryption": EFSTransitEncryptionType,
        "transitEncryptionPort": int,
        "authorizationConfig": "EFSAuthorizationConfigTypeDef",
    },
    total=False,
)

class EFSVolumeConfigurationTypeDef(
    _RequiredEFSVolumeConfigurationTypeDef, _OptionalEFSVolumeConfigurationTypeDef
):
    pass

EnvironmentFileTypeDef = TypedDict(
    "EnvironmentFileTypeDef",
    {
        "value": str,
        "type": Literal["s3"],
    },
)

EphemeralStorageTypeDef = TypedDict(
    "EphemeralStorageTypeDef",
    {
        "sizeInGiB": int,
    },
)

ExecuteCommandConfigurationTypeDef = TypedDict(
    "ExecuteCommandConfigurationTypeDef",
    {
        "kmsKeyId": str,
        "logging": ExecuteCommandLoggingType,
        "logConfiguration": "ExecuteCommandLogConfigurationTypeDef",
    },
    total=False,
)

ExecuteCommandLogConfigurationTypeDef = TypedDict(
    "ExecuteCommandLogConfigurationTypeDef",
    {
        "cloudWatchLogGroupName": str,
        "cloudWatchEncryptionEnabled": bool,
        "s3BucketName": str,
        "s3EncryptionEnabled": bool,
        "s3KeyPrefix": str,
    },
    total=False,
)

_RequiredExecuteCommandRequestRequestTypeDef = TypedDict(
    "_RequiredExecuteCommandRequestRequestTypeDef",
    {
        "command": str,
        "interactive": bool,
        "task": str,
    },
)
_OptionalExecuteCommandRequestRequestTypeDef = TypedDict(
    "_OptionalExecuteCommandRequestRequestTypeDef",
    {
        "cluster": str,
        "container": str,
    },
    total=False,
)

class ExecuteCommandRequestRequestTypeDef(
    _RequiredExecuteCommandRequestRequestTypeDef, _OptionalExecuteCommandRequestRequestTypeDef
):
    pass

ExecuteCommandResponseTypeDef = TypedDict(
    "ExecuteCommandResponseTypeDef",
    {
        "clusterArn": str,
        "containerArn": str,
        "containerName": str,
        "interactive": bool,
        "session": "SessionTypeDef",
        "taskArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FSxWindowsFileServerAuthorizationConfigTypeDef = TypedDict(
    "FSxWindowsFileServerAuthorizationConfigTypeDef",
    {
        "credentialsParameter": str,
        "domain": str,
    },
)

FSxWindowsFileServerVolumeConfigurationTypeDef = TypedDict(
    "FSxWindowsFileServerVolumeConfigurationTypeDef",
    {
        "fileSystemId": str,
        "rootDirectory": str,
        "authorizationConfig": "FSxWindowsFileServerAuthorizationConfigTypeDef",
    },
)

FailureTypeDef = TypedDict(
    "FailureTypeDef",
    {
        "arn": str,
        "reason": str,
        "detail": str,
    },
    total=False,
)

_RequiredFirelensConfigurationTypeDef = TypedDict(
    "_RequiredFirelensConfigurationTypeDef",
    {
        "type": FirelensConfigurationTypeType,
    },
)
_OptionalFirelensConfigurationTypeDef = TypedDict(
    "_OptionalFirelensConfigurationTypeDef",
    {
        "options": Dict[str, str],
    },
    total=False,
)

class FirelensConfigurationTypeDef(
    _RequiredFirelensConfigurationTypeDef, _OptionalFirelensConfigurationTypeDef
):
    pass

_RequiredHealthCheckTypeDef = TypedDict(
    "_RequiredHealthCheckTypeDef",
    {
        "command": List[str],
    },
)
_OptionalHealthCheckTypeDef = TypedDict(
    "_OptionalHealthCheckTypeDef",
    {
        "interval": int,
        "timeout": int,
        "retries": int,
        "startPeriod": int,
    },
    total=False,
)

class HealthCheckTypeDef(_RequiredHealthCheckTypeDef, _OptionalHealthCheckTypeDef):
    pass

HostEntryTypeDef = TypedDict(
    "HostEntryTypeDef",
    {
        "hostname": str,
        "ipAddress": str,
    },
)

HostVolumePropertiesTypeDef = TypedDict(
    "HostVolumePropertiesTypeDef",
    {
        "sourcePath": str,
    },
    total=False,
)

InferenceAcceleratorOverrideTypeDef = TypedDict(
    "InferenceAcceleratorOverrideTypeDef",
    {
        "deviceName": str,
        "deviceType": str,
    },
    total=False,
)

InferenceAcceleratorTypeDef = TypedDict(
    "InferenceAcceleratorTypeDef",
    {
        "deviceName": str,
        "deviceType": str,
    },
)

KernelCapabilitiesTypeDef = TypedDict(
    "KernelCapabilitiesTypeDef",
    {
        "add": List[str],
        "drop": List[str],
    },
    total=False,
)

KeyValuePairTypeDef = TypedDict(
    "KeyValuePairTypeDef",
    {
        "name": str,
        "value": str,
    },
    total=False,
)

LinuxParametersTypeDef = TypedDict(
    "LinuxParametersTypeDef",
    {
        "capabilities": "KernelCapabilitiesTypeDef",
        "devices": List["DeviceTypeDef"],
        "initProcessEnabled": bool,
        "sharedMemorySize": int,
        "tmpfs": List["TmpfsTypeDef"],
        "maxSwap": int,
        "swappiness": int,
    },
    total=False,
)

ListAccountSettingsRequestRequestTypeDef = TypedDict(
    "ListAccountSettingsRequestRequestTypeDef",
    {
        "name": SettingNameType,
        "value": str,
        "principalArn": str,
        "effectiveSettings": bool,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAccountSettingsResponseTypeDef = TypedDict(
    "ListAccountSettingsResponseTypeDef",
    {
        "settings": List["SettingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredListAttributesRequestRequestTypeDef",
    {
        "targetType": Literal["container-instance"],
    },
)
_OptionalListAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalListAttributesRequestRequestTypeDef",
    {
        "cluster": str,
        "attributeName": str,
        "attributeValue": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListAttributesRequestRequestTypeDef(
    _RequiredListAttributesRequestRequestTypeDef, _OptionalListAttributesRequestRequestTypeDef
):
    pass

ListAttributesResponseTypeDef = TypedDict(
    "ListAttributesResponseTypeDef",
    {
        "attributes": List["AttributeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClustersRequestRequestTypeDef = TypedDict(
    "ListClustersRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef",
    {
        "clusterArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContainerInstancesRequestRequestTypeDef = TypedDict(
    "ListContainerInstancesRequestRequestTypeDef",
    {
        "cluster": str,
        "filter": str,
        "nextToken": str,
        "maxResults": int,
        "status": ContainerInstanceStatusType,
    },
    total=False,
)

ListContainerInstancesResponseTypeDef = TypedDict(
    "ListContainerInstancesResponseTypeDef",
    {
        "containerInstanceArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicesRequestRequestTypeDef = TypedDict(
    "ListServicesRequestRequestTypeDef",
    {
        "cluster": str,
        "nextToken": str,
        "maxResults": int,
        "launchType": LaunchTypeType,
        "schedulingStrategy": SchedulingStrategyType,
    },
    total=False,
)

ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {
        "serviceArns": List[str],
        "nextToken": str,
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
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTaskDefinitionFamiliesRequestRequestTypeDef = TypedDict(
    "ListTaskDefinitionFamiliesRequestRequestTypeDef",
    {
        "familyPrefix": str,
        "status": TaskDefinitionFamilyStatusType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListTaskDefinitionFamiliesResponseTypeDef = TypedDict(
    "ListTaskDefinitionFamiliesResponseTypeDef",
    {
        "families": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTaskDefinitionsRequestRequestTypeDef = TypedDict(
    "ListTaskDefinitionsRequestRequestTypeDef",
    {
        "familyPrefix": str,
        "status": TaskDefinitionStatusType,
        "sort": SortOrderType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListTaskDefinitionsResponseTypeDef = TypedDict(
    "ListTaskDefinitionsResponseTypeDef",
    {
        "taskDefinitionArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTasksRequestRequestTypeDef = TypedDict(
    "ListTasksRequestRequestTypeDef",
    {
        "cluster": str,
        "containerInstance": str,
        "family": str,
        "nextToken": str,
        "maxResults": int,
        "startedBy": str,
        "serviceName": str,
        "desiredStatus": DesiredStatusType,
        "launchType": LaunchTypeType,
    },
    total=False,
)

ListTasksResponseTypeDef = TypedDict(
    "ListTasksResponseTypeDef",
    {
        "taskArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "targetGroupArn": str,
        "loadBalancerName": str,
        "containerName": str,
        "containerPort": int,
    },
    total=False,
)

_RequiredLogConfigurationTypeDef = TypedDict(
    "_RequiredLogConfigurationTypeDef",
    {
        "logDriver": LogDriverType,
    },
)
_OptionalLogConfigurationTypeDef = TypedDict(
    "_OptionalLogConfigurationTypeDef",
    {
        "options": Dict[str, str],
        "secretOptions": List["SecretTypeDef"],
    },
    total=False,
)

class LogConfigurationTypeDef(_RequiredLogConfigurationTypeDef, _OptionalLogConfigurationTypeDef):
    pass

_RequiredManagedAgentStateChangeTypeDef = TypedDict(
    "_RequiredManagedAgentStateChangeTypeDef",
    {
        "containerName": str,
        "managedAgentName": Literal["ExecuteCommandAgent"],
        "status": str,
    },
)
_OptionalManagedAgentStateChangeTypeDef = TypedDict(
    "_OptionalManagedAgentStateChangeTypeDef",
    {
        "reason": str,
    },
    total=False,
)

class ManagedAgentStateChangeTypeDef(
    _RequiredManagedAgentStateChangeTypeDef, _OptionalManagedAgentStateChangeTypeDef
):
    pass

ManagedAgentTypeDef = TypedDict(
    "ManagedAgentTypeDef",
    {
        "lastStartedAt": datetime,
        "name": Literal["ExecuteCommandAgent"],
        "reason": str,
        "lastStatus": str,
    },
    total=False,
)

ManagedScalingTypeDef = TypedDict(
    "ManagedScalingTypeDef",
    {
        "status": ManagedScalingStatusType,
        "targetCapacity": int,
        "minimumScalingStepSize": int,
        "maximumScalingStepSize": int,
        "instanceWarmupPeriod": int,
    },
    total=False,
)

MountPointTypeDef = TypedDict(
    "MountPointTypeDef",
    {
        "sourceVolume": str,
        "containerPath": str,
        "readOnly": bool,
    },
    total=False,
)

NetworkBindingTypeDef = TypedDict(
    "NetworkBindingTypeDef",
    {
        "bindIP": str,
        "containerPort": int,
        "hostPort": int,
        "protocol": TransportProtocolType,
    },
    total=False,
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": "AwsVpcConfigurationTypeDef",
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "attachmentId": str,
        "privateIpv4Address": str,
        "ipv6Address": str,
    },
    total=False,
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

PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef",
    {
        "type": PlacementConstraintTypeType,
        "expression": str,
    },
    total=False,
)

PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef",
    {
        "type": PlacementStrategyTypeType,
        "field": str,
    },
    total=False,
)

PlatformDeviceTypeDef = TypedDict(
    "PlatformDeviceTypeDef",
    {
        "id": str,
        "type": Literal["GPU"],
    },
)

PortMappingTypeDef = TypedDict(
    "PortMappingTypeDef",
    {
        "containerPort": int,
        "hostPort": int,
        "protocol": TransportProtocolType,
    },
    total=False,
)

_RequiredProxyConfigurationTypeDef = TypedDict(
    "_RequiredProxyConfigurationTypeDef",
    {
        "containerName": str,
    },
)
_OptionalProxyConfigurationTypeDef = TypedDict(
    "_OptionalProxyConfigurationTypeDef",
    {
        "type": Literal["APPMESH"],
        "properties": List["KeyValuePairTypeDef"],
    },
    total=False,
)

class ProxyConfigurationTypeDef(
    _RequiredProxyConfigurationTypeDef, _OptionalProxyConfigurationTypeDef
):
    pass

PutAccountSettingDefaultRequestRequestTypeDef = TypedDict(
    "PutAccountSettingDefaultRequestRequestTypeDef",
    {
        "name": SettingNameType,
        "value": str,
    },
)

PutAccountSettingDefaultResponseTypeDef = TypedDict(
    "PutAccountSettingDefaultResponseTypeDef",
    {
        "setting": "SettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutAccountSettingRequestRequestTypeDef = TypedDict(
    "_RequiredPutAccountSettingRequestRequestTypeDef",
    {
        "name": SettingNameType,
        "value": str,
    },
)
_OptionalPutAccountSettingRequestRequestTypeDef = TypedDict(
    "_OptionalPutAccountSettingRequestRequestTypeDef",
    {
        "principalArn": str,
    },
    total=False,
)

class PutAccountSettingRequestRequestTypeDef(
    _RequiredPutAccountSettingRequestRequestTypeDef, _OptionalPutAccountSettingRequestRequestTypeDef
):
    pass

PutAccountSettingResponseTypeDef = TypedDict(
    "PutAccountSettingResponseTypeDef",
    {
        "setting": "SettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredPutAttributesRequestRequestTypeDef",
    {
        "attributes": List["AttributeTypeDef"],
    },
)
_OptionalPutAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalPutAttributesRequestRequestTypeDef",
    {
        "cluster": str,
    },
    total=False,
)

class PutAttributesRequestRequestTypeDef(
    _RequiredPutAttributesRequestRequestTypeDef, _OptionalPutAttributesRequestRequestTypeDef
):
    pass

PutAttributesResponseTypeDef = TypedDict(
    "PutAttributesResponseTypeDef",
    {
        "attributes": List["AttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutClusterCapacityProvidersRequestRequestTypeDef = TypedDict(
    "PutClusterCapacityProvidersRequestRequestTypeDef",
    {
        "cluster": str,
        "capacityProviders": List[str],
        "defaultCapacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
    },
)

PutClusterCapacityProvidersResponseTypeDef = TypedDict(
    "PutClusterCapacityProvidersResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterContainerInstanceRequestRequestTypeDef = TypedDict(
    "RegisterContainerInstanceRequestRequestTypeDef",
    {
        "cluster": str,
        "instanceIdentityDocument": str,
        "instanceIdentityDocumentSignature": str,
        "totalResources": List["ResourceTypeDef"],
        "versionInfo": "VersionInfoTypeDef",
        "containerInstanceArn": str,
        "attributes": List["AttributeTypeDef"],
        "platformDevices": List["PlatformDeviceTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

RegisterContainerInstanceResponseTypeDef = TypedDict(
    "RegisterContainerInstanceResponseTypeDef",
    {
        "containerInstance": "ContainerInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterTaskDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterTaskDefinitionRequestRequestTypeDef",
    {
        "family": str,
        "containerDefinitions": List["ContainerDefinitionTypeDef"],
    },
)
_OptionalRegisterTaskDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterTaskDefinitionRequestRequestTypeDef",
    {
        "taskRoleArn": str,
        "executionRoleArn": str,
        "networkMode": NetworkModeType,
        "volumes": List["VolumeTypeDef"],
        "placementConstraints": List["TaskDefinitionPlacementConstraintTypeDef"],
        "requiresCompatibilities": List[CompatibilityType],
        "cpu": str,
        "memory": str,
        "tags": List["TagTypeDef"],
        "pidMode": PidModeType,
        "ipcMode": IpcModeType,
        "proxyConfiguration": "ProxyConfigurationTypeDef",
        "inferenceAccelerators": List["InferenceAcceleratorTypeDef"],
        "ephemeralStorage": "EphemeralStorageTypeDef",
    },
    total=False,
)

class RegisterTaskDefinitionRequestRequestTypeDef(
    _RequiredRegisterTaskDefinitionRequestRequestTypeDef,
    _OptionalRegisterTaskDefinitionRequestRequestTypeDef,
):
    pass

RegisterTaskDefinitionResponseTypeDef = TypedDict(
    "RegisterTaskDefinitionResponseTypeDef",
    {
        "taskDefinition": "TaskDefinitionTypeDef",
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RepositoryCredentialsTypeDef = TypedDict(
    "RepositoryCredentialsTypeDef",
    {
        "credentialsParameter": str,
    },
)

ResourceRequirementTypeDef = TypedDict(
    "ResourceRequirementTypeDef",
    {
        "value": str,
        "type": ResourceTypeType,
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)

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

_RequiredRunTaskRequestRequestTypeDef = TypedDict(
    "_RequiredRunTaskRequestRequestTypeDef",
    {
        "taskDefinition": str,
    },
)
_OptionalRunTaskRequestRequestTypeDef = TypedDict(
    "_OptionalRunTaskRequestRequestTypeDef",
    {
        "capacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "cluster": str,
        "count": int,
        "enableECSManagedTags": bool,
        "enableExecuteCommand": bool,
        "group": str,
        "launchType": LaunchTypeType,
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "overrides": "TaskOverrideTypeDef",
        "placementConstraints": List["PlacementConstraintTypeDef"],
        "placementStrategy": List["PlacementStrategyTypeDef"],
        "platformVersion": str,
        "propagateTags": PropagateTagsType,
        "referenceId": str,
        "startedBy": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class RunTaskRequestRequestTypeDef(
    _RequiredRunTaskRequestRequestTypeDef, _OptionalRunTaskRequestRequestTypeDef
):
    pass

RunTaskResponseTypeDef = TypedDict(
    "RunTaskResponseTypeDef",
    {
        "tasks": List["TaskTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ScaleTypeDef = TypedDict(
    "ScaleTypeDef",
    {
        "value": float,
        "unit": Literal["PERCENT"],
    },
    total=False,
)

SecretTypeDef = TypedDict(
    "SecretTypeDef",
    {
        "name": str,
        "valueFrom": str,
    },
)

ServiceEventTypeDef = TypedDict(
    "ServiceEventTypeDef",
    {
        "id": str,
        "createdAt": datetime,
        "message": str,
    },
    total=False,
)

ServiceRegistryTypeDef = TypedDict(
    "ServiceRegistryTypeDef",
    {
        "registryArn": str,
        "port": int,
        "containerName": str,
        "containerPort": int,
    },
    total=False,
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "serviceArn": str,
        "serviceName": str,
        "clusterArn": str,
        "loadBalancers": List["LoadBalancerTypeDef"],
        "serviceRegistries": List["ServiceRegistryTypeDef"],
        "status": str,
        "desiredCount": int,
        "runningCount": int,
        "pendingCount": int,
        "launchType": LaunchTypeType,
        "capacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "platformVersion": str,
        "taskDefinition": str,
        "deploymentConfiguration": "DeploymentConfigurationTypeDef",
        "taskSets": List["TaskSetTypeDef"],
        "deployments": List["DeploymentTypeDef"],
        "roleArn": str,
        "events": List["ServiceEventTypeDef"],
        "createdAt": datetime,
        "placementConstraints": List["PlacementConstraintTypeDef"],
        "placementStrategy": List["PlacementStrategyTypeDef"],
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "healthCheckGracePeriodSeconds": int,
        "schedulingStrategy": SchedulingStrategyType,
        "deploymentController": "DeploymentControllerTypeDef",
        "tags": List["TagTypeDef"],
        "createdBy": str,
        "enableECSManagedTags": bool,
        "propagateTags": PropagateTagsType,
        "enableExecuteCommand": bool,
    },
    total=False,
)

SessionTypeDef = TypedDict(
    "SessionTypeDef",
    {
        "sessionId": str,
        "streamUrl": str,
        "tokenValue": str,
    },
    total=False,
)

SettingTypeDef = TypedDict(
    "SettingTypeDef",
    {
        "name": SettingNameType,
        "value": str,
        "principalArn": str,
    },
    total=False,
)

_RequiredStartTaskRequestRequestTypeDef = TypedDict(
    "_RequiredStartTaskRequestRequestTypeDef",
    {
        "containerInstances": List[str],
        "taskDefinition": str,
    },
)
_OptionalStartTaskRequestRequestTypeDef = TypedDict(
    "_OptionalStartTaskRequestRequestTypeDef",
    {
        "cluster": str,
        "enableECSManagedTags": bool,
        "enableExecuteCommand": bool,
        "group": str,
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "overrides": "TaskOverrideTypeDef",
        "propagateTags": PropagateTagsType,
        "referenceId": str,
        "startedBy": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class StartTaskRequestRequestTypeDef(
    _RequiredStartTaskRequestRequestTypeDef, _OptionalStartTaskRequestRequestTypeDef
):
    pass

StartTaskResponseTypeDef = TypedDict(
    "StartTaskResponseTypeDef",
    {
        "tasks": List["TaskTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStopTaskRequestRequestTypeDef = TypedDict(
    "_RequiredStopTaskRequestRequestTypeDef",
    {
        "task": str,
    },
)
_OptionalStopTaskRequestRequestTypeDef = TypedDict(
    "_OptionalStopTaskRequestRequestTypeDef",
    {
        "cluster": str,
        "reason": str,
    },
    total=False,
)

class StopTaskRequestRequestTypeDef(
    _RequiredStopTaskRequestRequestTypeDef, _OptionalStopTaskRequestRequestTypeDef
):
    pass

StopTaskResponseTypeDef = TypedDict(
    "StopTaskResponseTypeDef",
    {
        "task": "TaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSubmitAttachmentStateChangesRequestRequestTypeDef = TypedDict(
    "_RequiredSubmitAttachmentStateChangesRequestRequestTypeDef",
    {
        "attachments": List["AttachmentStateChangeTypeDef"],
    },
)
_OptionalSubmitAttachmentStateChangesRequestRequestTypeDef = TypedDict(
    "_OptionalSubmitAttachmentStateChangesRequestRequestTypeDef",
    {
        "cluster": str,
    },
    total=False,
)

class SubmitAttachmentStateChangesRequestRequestTypeDef(
    _RequiredSubmitAttachmentStateChangesRequestRequestTypeDef,
    _OptionalSubmitAttachmentStateChangesRequestRequestTypeDef,
):
    pass

SubmitAttachmentStateChangesResponseTypeDef = TypedDict(
    "SubmitAttachmentStateChangesResponseTypeDef",
    {
        "acknowledgment": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubmitContainerStateChangeRequestRequestTypeDef = TypedDict(
    "SubmitContainerStateChangeRequestRequestTypeDef",
    {
        "cluster": str,
        "task": str,
        "containerName": str,
        "runtimeId": str,
        "status": str,
        "exitCode": int,
        "reason": str,
        "networkBindings": List["NetworkBindingTypeDef"],
    },
    total=False,
)

SubmitContainerStateChangeResponseTypeDef = TypedDict(
    "SubmitContainerStateChangeResponseTypeDef",
    {
        "acknowledgment": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubmitTaskStateChangeRequestRequestTypeDef = TypedDict(
    "SubmitTaskStateChangeRequestRequestTypeDef",
    {
        "cluster": str,
        "task": str,
        "status": str,
        "reason": str,
        "containers": List["ContainerStateChangeTypeDef"],
        "attachments": List["AttachmentStateChangeTypeDef"],
        "managedAgents": List["ManagedAgentStateChangeTypeDef"],
        "pullStartedAt": Union[datetime, str],
        "pullStoppedAt": Union[datetime, str],
        "executionStoppedAt": Union[datetime, str],
    },
    total=False,
)

SubmitTaskStateChangeResponseTypeDef = TypedDict(
    "SubmitTaskStateChangeResponseTypeDef",
    {
        "acknowledgment": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SystemControlTypeDef = TypedDict(
    "SystemControlTypeDef",
    {
        "namespace": str,
        "value": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

TaskDefinitionPlacementConstraintTypeDef = TypedDict(
    "TaskDefinitionPlacementConstraintTypeDef",
    {
        "type": Literal["memberOf"],
        "expression": str,
    },
    total=False,
)

TaskDefinitionTypeDef = TypedDict(
    "TaskDefinitionTypeDef",
    {
        "taskDefinitionArn": str,
        "containerDefinitions": List["ContainerDefinitionTypeDef"],
        "family": str,
        "taskRoleArn": str,
        "executionRoleArn": str,
        "networkMode": NetworkModeType,
        "revision": int,
        "volumes": List["VolumeTypeDef"],
        "status": TaskDefinitionStatusType,
        "requiresAttributes": List["AttributeTypeDef"],
        "placementConstraints": List["TaskDefinitionPlacementConstraintTypeDef"],
        "compatibilities": List[CompatibilityType],
        "requiresCompatibilities": List[CompatibilityType],
        "cpu": str,
        "memory": str,
        "inferenceAccelerators": List["InferenceAcceleratorTypeDef"],
        "pidMode": PidModeType,
        "ipcMode": IpcModeType,
        "proxyConfiguration": "ProxyConfigurationTypeDef",
        "registeredAt": datetime,
        "deregisteredAt": datetime,
        "registeredBy": str,
        "ephemeralStorage": "EphemeralStorageTypeDef",
    },
    total=False,
)

TaskOverrideTypeDef = TypedDict(
    "TaskOverrideTypeDef",
    {
        "containerOverrides": List["ContainerOverrideTypeDef"],
        "cpu": str,
        "inferenceAcceleratorOverrides": List["InferenceAcceleratorOverrideTypeDef"],
        "executionRoleArn": str,
        "memory": str,
        "taskRoleArn": str,
        "ephemeralStorage": "EphemeralStorageTypeDef",
    },
    total=False,
)

TaskSetTypeDef = TypedDict(
    "TaskSetTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": LaunchTypeType,
        "capacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "platformVersion": str,
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "loadBalancers": List["LoadBalancerTypeDef"],
        "serviceRegistries": List["ServiceRegistryTypeDef"],
        "scale": "ScaleTypeDef",
        "stabilityStatus": StabilityStatusType,
        "stabilityStatusAt": datetime,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

TaskTypeDef = TypedDict(
    "TaskTypeDef",
    {
        "attachments": List["AttachmentTypeDef"],
        "attributes": List["AttributeTypeDef"],
        "availabilityZone": str,
        "capacityProviderName": str,
        "clusterArn": str,
        "connectivity": ConnectivityType,
        "connectivityAt": datetime,
        "containerInstanceArn": str,
        "containers": List["ContainerTypeDef"],
        "cpu": str,
        "createdAt": datetime,
        "desiredStatus": str,
        "enableExecuteCommand": bool,
        "executionStoppedAt": datetime,
        "group": str,
        "healthStatus": HealthStatusType,
        "inferenceAccelerators": List["InferenceAcceleratorTypeDef"],
        "lastStatus": str,
        "launchType": LaunchTypeType,
        "memory": str,
        "overrides": "TaskOverrideTypeDef",
        "platformVersion": str,
        "pullStartedAt": datetime,
        "pullStoppedAt": datetime,
        "startedAt": datetime,
        "startedBy": str,
        "stopCode": TaskStopCodeType,
        "stoppedAt": datetime,
        "stoppedReason": str,
        "stoppingAt": datetime,
        "tags": List["TagTypeDef"],
        "taskArn": str,
        "taskDefinitionArn": str,
        "version": int,
        "ephemeralStorage": "EphemeralStorageTypeDef",
    },
    total=False,
)

_RequiredTmpfsTypeDef = TypedDict(
    "_RequiredTmpfsTypeDef",
    {
        "containerPath": str,
        "size": int,
    },
)
_OptionalTmpfsTypeDef = TypedDict(
    "_OptionalTmpfsTypeDef",
    {
        "mountOptions": List[str],
    },
    total=False,
)

class TmpfsTypeDef(_RequiredTmpfsTypeDef, _OptionalTmpfsTypeDef):
    pass

UlimitTypeDef = TypedDict(
    "UlimitTypeDef",
    {
        "name": UlimitNameType,
        "softLimit": int,
        "hardLimit": int,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateCapacityProviderRequestRequestTypeDef = TypedDict(
    "UpdateCapacityProviderRequestRequestTypeDef",
    {
        "name": str,
        "autoScalingGroupProvider": "AutoScalingGroupProviderUpdateTypeDef",
    },
)

UpdateCapacityProviderResponseTypeDef = TypedDict(
    "UpdateCapacityProviderResponseTypeDef",
    {
        "capacityProvider": "CapacityProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateClusterRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateClusterRequestRequestTypeDef",
    {
        "cluster": str,
    },
)
_OptionalUpdateClusterRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateClusterRequestRequestTypeDef",
    {
        "settings": List["ClusterSettingTypeDef"],
        "configuration": "ClusterConfigurationTypeDef",
    },
    total=False,
)

class UpdateClusterRequestRequestTypeDef(
    _RequiredUpdateClusterRequestRequestTypeDef, _OptionalUpdateClusterRequestRequestTypeDef
):
    pass

UpdateClusterResponseTypeDef = TypedDict(
    "UpdateClusterResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateClusterSettingsRequestRequestTypeDef = TypedDict(
    "UpdateClusterSettingsRequestRequestTypeDef",
    {
        "cluster": str,
        "settings": List["ClusterSettingTypeDef"],
    },
)

UpdateClusterSettingsResponseTypeDef = TypedDict(
    "UpdateClusterSettingsResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateContainerAgentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContainerAgentRequestRequestTypeDef",
    {
        "containerInstance": str,
    },
)
_OptionalUpdateContainerAgentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContainerAgentRequestRequestTypeDef",
    {
        "cluster": str,
    },
    total=False,
)

class UpdateContainerAgentRequestRequestTypeDef(
    _RequiredUpdateContainerAgentRequestRequestTypeDef,
    _OptionalUpdateContainerAgentRequestRequestTypeDef,
):
    pass

UpdateContainerAgentResponseTypeDef = TypedDict(
    "UpdateContainerAgentResponseTypeDef",
    {
        "containerInstance": "ContainerInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateContainerInstancesStateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContainerInstancesStateRequestRequestTypeDef",
    {
        "containerInstances": List[str],
        "status": ContainerInstanceStatusType,
    },
)
_OptionalUpdateContainerInstancesStateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContainerInstancesStateRequestRequestTypeDef",
    {
        "cluster": str,
    },
    total=False,
)

class UpdateContainerInstancesStateRequestRequestTypeDef(
    _RequiredUpdateContainerInstancesStateRequestRequestTypeDef,
    _OptionalUpdateContainerInstancesStateRequestRequestTypeDef,
):
    pass

UpdateContainerInstancesStateResponseTypeDef = TypedDict(
    "UpdateContainerInstancesStateResponseTypeDef",
    {
        "containerInstances": List["ContainerInstanceTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServicePrimaryTaskSetRequestRequestTypeDef = TypedDict(
    "UpdateServicePrimaryTaskSetRequestRequestTypeDef",
    {
        "cluster": str,
        "service": str,
        "primaryTaskSet": str,
    },
)

UpdateServicePrimaryTaskSetResponseTypeDef = TypedDict(
    "UpdateServicePrimaryTaskSetResponseTypeDef",
    {
        "taskSet": "TaskSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateServiceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateServiceRequestRequestTypeDef",
    {
        "service": str,
    },
)
_OptionalUpdateServiceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateServiceRequestRequestTypeDef",
    {
        "cluster": str,
        "desiredCount": int,
        "taskDefinition": str,
        "capacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "deploymentConfiguration": "DeploymentConfigurationTypeDef",
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "placementConstraints": List["PlacementConstraintTypeDef"],
        "placementStrategy": List["PlacementStrategyTypeDef"],
        "platformVersion": str,
        "forceNewDeployment": bool,
        "healthCheckGracePeriodSeconds": int,
        "enableExecuteCommand": bool,
    },
    total=False,
)

class UpdateServiceRequestRequestTypeDef(
    _RequiredUpdateServiceRequestRequestTypeDef, _OptionalUpdateServiceRequestRequestTypeDef
):
    pass

UpdateServiceResponseTypeDef = TypedDict(
    "UpdateServiceResponseTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTaskSetRequestRequestTypeDef = TypedDict(
    "UpdateTaskSetRequestRequestTypeDef",
    {
        "cluster": str,
        "service": str,
        "taskSet": str,
        "scale": "ScaleTypeDef",
    },
)

UpdateTaskSetResponseTypeDef = TypedDict(
    "UpdateTaskSetResponseTypeDef",
    {
        "taskSet": "TaskSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VersionInfoTypeDef = TypedDict(
    "VersionInfoTypeDef",
    {
        "agentVersion": str,
        "agentHash": str,
        "dockerVersion": str,
    },
    total=False,
)

VolumeFromTypeDef = TypedDict(
    "VolumeFromTypeDef",
    {
        "sourceContainer": str,
        "readOnly": bool,
    },
    total=False,
)

VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "name": str,
        "host": "HostVolumePropertiesTypeDef",
        "dockerVolumeConfiguration": "DockerVolumeConfigurationTypeDef",
        "efsVolumeConfiguration": "EFSVolumeConfigurationTypeDef",
        "fsxWindowsFileServerVolumeConfiguration": "FSxWindowsFileServerVolumeConfigurationTypeDef",
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
