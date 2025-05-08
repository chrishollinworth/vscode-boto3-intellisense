"""
Type annotations for batch service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_batch.type_defs import ArrayPropertiesDetailTypeDef

    data: ArrayPropertiesDetailTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Union

from .literals import (
    ArrayJobDependencyType,
    AssignPublicIpType,
    CEStateType,
    CEStatusType,
    CETypeType,
    CRAllocationStrategyType,
    CRTypeType,
    CRUpdateAllocationStrategyType,
    DeviceCgroupPermissionType,
    EFSAuthorizationConfigIAMType,
    EFSTransitEncryptionType,
    FirelensConfigurationTypeType,
    JobDefinitionTypeType,
    JobStatusType,
    JQStateType,
    JQStatusType,
    LogDriverType,
    OrchestrationTypeType,
    PlatformCapabilityType,
    ResourceTypeType,
    RetryActionType,
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
    "ArrayPropertiesDetailTypeDef",
    "ArrayPropertiesSummaryTypeDef",
    "ArrayPropertiesTypeDef",
    "AttemptContainerDetailTypeDef",
    "AttemptDetailTypeDef",
    "AttemptEcsTaskDetailsTypeDef",
    "AttemptTaskContainerDetailsTypeDef",
    "CancelJobRequestTypeDef",
    "ComputeEnvironmentDetailTypeDef",
    "ComputeEnvironmentOrderTypeDef",
    "ComputeResourceOutputTypeDef",
    "ComputeResourceTypeDef",
    "ComputeResourceUnionTypeDef",
    "ComputeResourceUpdateTypeDef",
    "ConsumableResourcePropertiesOutputTypeDef",
    "ConsumableResourcePropertiesTypeDef",
    "ConsumableResourcePropertiesUnionTypeDef",
    "ConsumableResourceRequirementTypeDef",
    "ConsumableResourceSummaryTypeDef",
    "ContainerDetailTypeDef",
    "ContainerOverridesTypeDef",
    "ContainerPropertiesOutputTypeDef",
    "ContainerPropertiesTypeDef",
    "ContainerPropertiesUnionTypeDef",
    "ContainerSummaryTypeDef",
    "CreateComputeEnvironmentRequestTypeDef",
    "CreateComputeEnvironmentResponseTypeDef",
    "CreateConsumableResourceRequestTypeDef",
    "CreateConsumableResourceResponseTypeDef",
    "CreateJobQueueRequestTypeDef",
    "CreateJobQueueResponseTypeDef",
    "CreateSchedulingPolicyRequestTypeDef",
    "CreateSchedulingPolicyResponseTypeDef",
    "DeleteComputeEnvironmentRequestTypeDef",
    "DeleteConsumableResourceRequestTypeDef",
    "DeleteJobQueueRequestTypeDef",
    "DeleteSchedulingPolicyRequestTypeDef",
    "DeregisterJobDefinitionRequestTypeDef",
    "DescribeComputeEnvironmentsRequestPaginateTypeDef",
    "DescribeComputeEnvironmentsRequestTypeDef",
    "DescribeComputeEnvironmentsResponseTypeDef",
    "DescribeConsumableResourceRequestTypeDef",
    "DescribeConsumableResourceResponseTypeDef",
    "DescribeJobDefinitionsRequestPaginateTypeDef",
    "DescribeJobDefinitionsRequestTypeDef",
    "DescribeJobDefinitionsResponseTypeDef",
    "DescribeJobQueuesRequestPaginateTypeDef",
    "DescribeJobQueuesRequestTypeDef",
    "DescribeJobQueuesResponseTypeDef",
    "DescribeJobsRequestTypeDef",
    "DescribeJobsResponseTypeDef",
    "DescribeSchedulingPoliciesRequestTypeDef",
    "DescribeSchedulingPoliciesResponseTypeDef",
    "DeviceOutputTypeDef",
    "DeviceTypeDef",
    "EFSAuthorizationConfigTypeDef",
    "EFSVolumeConfigurationTypeDef",
    "Ec2ConfigurationTypeDef",
    "EcsPropertiesDetailTypeDef",
    "EcsPropertiesOutputTypeDef",
    "EcsPropertiesOverrideTypeDef",
    "EcsPropertiesTypeDef",
    "EcsPropertiesUnionTypeDef",
    "EcsTaskDetailsTypeDef",
    "EcsTaskPropertiesOutputTypeDef",
    "EcsTaskPropertiesTypeDef",
    "EksAttemptContainerDetailTypeDef",
    "EksAttemptDetailTypeDef",
    "EksConfigurationTypeDef",
    "EksContainerDetailTypeDef",
    "EksContainerEnvironmentVariableTypeDef",
    "EksContainerOutputTypeDef",
    "EksContainerOverrideTypeDef",
    "EksContainerResourceRequirementsOutputTypeDef",
    "EksContainerResourceRequirementsTypeDef",
    "EksContainerResourceRequirementsUnionTypeDef",
    "EksContainerSecurityContextTypeDef",
    "EksContainerTypeDef",
    "EksContainerVolumeMountTypeDef",
    "EksEmptyDirTypeDef",
    "EksHostPathTypeDef",
    "EksMetadataOutputTypeDef",
    "EksMetadataTypeDef",
    "EksMetadataUnionTypeDef",
    "EksPersistentVolumeClaimTypeDef",
    "EksPodPropertiesDetailTypeDef",
    "EksPodPropertiesOutputTypeDef",
    "EksPodPropertiesOverrideTypeDef",
    "EksPodPropertiesTypeDef",
    "EksPropertiesDetailTypeDef",
    "EksPropertiesOutputTypeDef",
    "EksPropertiesOverrideTypeDef",
    "EksPropertiesTypeDef",
    "EksPropertiesUnionTypeDef",
    "EksSecretTypeDef",
    "EksVolumeTypeDef",
    "EphemeralStorageTypeDef",
    "EvaluateOnExitTypeDef",
    "FairsharePolicyOutputTypeDef",
    "FairsharePolicyTypeDef",
    "FairsharePolicyUnionTypeDef",
    "FargatePlatformConfigurationTypeDef",
    "FirelensConfigurationOutputTypeDef",
    "FirelensConfigurationTypeDef",
    "FrontOfQueueDetailTypeDef",
    "FrontOfQueueJobSummaryTypeDef",
    "GetJobQueueSnapshotRequestTypeDef",
    "GetJobQueueSnapshotResponseTypeDef",
    "HostTypeDef",
    "ImagePullSecretTypeDef",
    "JobDefinitionTypeDef",
    "JobDependencyTypeDef",
    "JobDetailTypeDef",
    "JobQueueDetailTypeDef",
    "JobStateTimeLimitActionTypeDef",
    "JobSummaryTypeDef",
    "JobTimeoutTypeDef",
    "KeyValuePairTypeDef",
    "KeyValuesPairTypeDef",
    "LaunchTemplateSpecificationOutputTypeDef",
    "LaunchTemplateSpecificationOverrideOutputTypeDef",
    "LaunchTemplateSpecificationOverrideTypeDef",
    "LaunchTemplateSpecificationOverrideUnionTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "LaunchTemplateSpecificationUnionTypeDef",
    "LinuxParametersOutputTypeDef",
    "LinuxParametersTypeDef",
    "ListConsumableResourcesRequestPaginateTypeDef",
    "ListConsumableResourcesRequestTypeDef",
    "ListConsumableResourcesResponseTypeDef",
    "ListJobsByConsumableResourceRequestPaginateTypeDef",
    "ListJobsByConsumableResourceRequestTypeDef",
    "ListJobsByConsumableResourceResponseTypeDef",
    "ListJobsByConsumableResourceSummaryTypeDef",
    "ListJobsRequestPaginateTypeDef",
    "ListJobsRequestTypeDef",
    "ListJobsResponseTypeDef",
    "ListSchedulingPoliciesRequestPaginateTypeDef",
    "ListSchedulingPoliciesRequestTypeDef",
    "ListSchedulingPoliciesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogConfigurationOutputTypeDef",
    "LogConfigurationTypeDef",
    "MountPointTypeDef",
    "NetworkConfigurationTypeDef",
    "NetworkInterfaceTypeDef",
    "NodeDetailsTypeDef",
    "NodeOverridesTypeDef",
    "NodePropertiesOutputTypeDef",
    "NodePropertiesSummaryTypeDef",
    "NodePropertiesTypeDef",
    "NodePropertiesUnionTypeDef",
    "NodePropertyOverrideTypeDef",
    "NodeRangePropertyOutputTypeDef",
    "NodeRangePropertyTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterJobDefinitionRequestTypeDef",
    "RegisterJobDefinitionResponseTypeDef",
    "RepositoryCredentialsTypeDef",
    "ResourceRequirementTypeDef",
    "ResponseMetadataTypeDef",
    "RetryStrategyOutputTypeDef",
    "RetryStrategyTypeDef",
    "RetryStrategyUnionTypeDef",
    "RuntimePlatformTypeDef",
    "SchedulingPolicyDetailTypeDef",
    "SchedulingPolicyListingDetailTypeDef",
    "SecretTypeDef",
    "ShareAttributesTypeDef",
    "SubmitJobRequestTypeDef",
    "SubmitJobResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TaskContainerDependencyTypeDef",
    "TaskContainerDetailsTypeDef",
    "TaskContainerOverridesTypeDef",
    "TaskContainerPropertiesOutputTypeDef",
    "TaskContainerPropertiesTypeDef",
    "TaskPropertiesOverrideTypeDef",
    "TerminateJobRequestTypeDef",
    "TmpfsOutputTypeDef",
    "TmpfsTypeDef",
    "UlimitTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateComputeEnvironmentRequestTypeDef",
    "UpdateComputeEnvironmentResponseTypeDef",
    "UpdateConsumableResourceRequestTypeDef",
    "UpdateConsumableResourceResponseTypeDef",
    "UpdateJobQueueRequestTypeDef",
    "UpdateJobQueueResponseTypeDef",
    "UpdatePolicyTypeDef",
    "UpdateSchedulingPolicyRequestTypeDef",
    "VolumeTypeDef",
)

class ArrayPropertiesDetailTypeDef(TypedDict):
    statusSummary: NotRequired[Dict[str, int]]
    size: NotRequired[int]
    index: NotRequired[int]

class ArrayPropertiesSummaryTypeDef(TypedDict):
    size: NotRequired[int]
    index: NotRequired[int]

class ArrayPropertiesTypeDef(TypedDict):
    size: NotRequired[int]

class NetworkInterfaceTypeDef(TypedDict):
    attachmentId: NotRequired[str]
    ipv6Address: NotRequired[str]
    privateIpv4Address: NotRequired[str]

class CancelJobRequestTypeDef(TypedDict):
    jobId: str
    reason: str

class EksConfigurationTypeDef(TypedDict):
    eksClusterArn: str
    kubernetesNamespace: str

class UpdatePolicyTypeDef(TypedDict):
    terminateJobsOnUpdate: NotRequired[bool]
    jobExecutionTimeoutMinutes: NotRequired[int]

class ComputeEnvironmentOrderTypeDef(TypedDict):
    order: int
    computeEnvironment: str

class Ec2ConfigurationTypeDef(TypedDict):
    imageType: str
    imageIdOverride: NotRequired[str]
    imageKubernetesVersion: NotRequired[str]

class ConsumableResourceRequirementTypeDef(TypedDict):
    consumableResource: NotRequired[str]
    quantity: NotRequired[int]

class ConsumableResourceSummaryTypeDef(TypedDict):
    consumableResourceArn: str
    consumableResourceName: str
    totalQuantity: NotRequired[int]
    inUseQuantity: NotRequired[int]
    resourceType: NotRequired[str]

class EphemeralStorageTypeDef(TypedDict):
    sizeInGiB: int

class FargatePlatformConfigurationTypeDef(TypedDict):
    platformVersion: NotRequired[str]

class KeyValuePairTypeDef(TypedDict):
    name: NotRequired[str]
    value: NotRequired[str]

class MountPointTypeDef(TypedDict):
    containerPath: NotRequired[str]
    readOnly: NotRequired[bool]
    sourceVolume: NotRequired[str]

class NetworkConfigurationTypeDef(TypedDict):
    assignPublicIp: NotRequired[AssignPublicIpType]

class RepositoryCredentialsTypeDef(TypedDict):
    credentialsParameter: str

ResourceRequirementTypeDef = TypedDict(
    "ResourceRequirementTypeDef",
    {
        "value": str,
        "type": ResourceTypeType,
    },
)

class RuntimePlatformTypeDef(TypedDict):
    operatingSystemFamily: NotRequired[str]
    cpuArchitecture: NotRequired[str]

class SecretTypeDef(TypedDict):
    name: str
    valueFrom: str

class UlimitTypeDef(TypedDict):
    hardLimit: int
    name: str
    softLimit: int

class ContainerSummaryTypeDef(TypedDict):
    exitCode: NotRequired[int]
    reason: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateConsumableResourceRequestTypeDef(TypedDict):
    consumableResourceName: str
    totalQuantity: NotRequired[int]
    resourceType: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class JobStateTimeLimitActionTypeDef(TypedDict):
    reason: str
    state: Literal["RUNNABLE"]
    maxTimeSeconds: int
    action: Literal["CANCEL"]

class DeleteComputeEnvironmentRequestTypeDef(TypedDict):
    computeEnvironment: str

class DeleteConsumableResourceRequestTypeDef(TypedDict):
    consumableResource: str

class DeleteJobQueueRequestTypeDef(TypedDict):
    jobQueue: str

class DeleteSchedulingPolicyRequestTypeDef(TypedDict):
    arn: str

class DeregisterJobDefinitionRequestTypeDef(TypedDict):
    jobDefinition: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeComputeEnvironmentsRequestTypeDef(TypedDict):
    computeEnvironments: NotRequired[Sequence[str]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class DescribeConsumableResourceRequestTypeDef(TypedDict):
    consumableResource: str

class DescribeJobDefinitionsRequestTypeDef(TypedDict):
    jobDefinitions: NotRequired[Sequence[str]]
    maxResults: NotRequired[int]
    jobDefinitionName: NotRequired[str]
    status: NotRequired[str]
    nextToken: NotRequired[str]

class DescribeJobQueuesRequestTypeDef(TypedDict):
    jobQueues: NotRequired[Sequence[str]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class DescribeJobsRequestTypeDef(TypedDict):
    jobs: Sequence[str]

class DescribeSchedulingPoliciesRequestTypeDef(TypedDict):
    arns: Sequence[str]

class DeviceOutputTypeDef(TypedDict):
    hostPath: str
    containerPath: NotRequired[str]
    permissions: NotRequired[List[DeviceCgroupPermissionType]]

class DeviceTypeDef(TypedDict):
    hostPath: str
    containerPath: NotRequired[str]
    permissions: NotRequired[Sequence[DeviceCgroupPermissionType]]

class EFSAuthorizationConfigTypeDef(TypedDict):
    accessPointId: NotRequired[str]
    iam: NotRequired[EFSAuthorizationConfigIAMType]

class EksAttemptContainerDetailTypeDef(TypedDict):
    name: NotRequired[str]
    containerID: NotRequired[str]
    exitCode: NotRequired[int]
    reason: NotRequired[str]

class EksContainerEnvironmentVariableTypeDef(TypedDict):
    name: str
    value: NotRequired[str]

class EksContainerResourceRequirementsOutputTypeDef(TypedDict):
    limits: NotRequired[Dict[str, str]]
    requests: NotRequired[Dict[str, str]]

class EksContainerSecurityContextTypeDef(TypedDict):
    runAsUser: NotRequired[int]
    runAsGroup: NotRequired[int]
    privileged: NotRequired[bool]
    allowPrivilegeEscalation: NotRequired[bool]
    readOnlyRootFilesystem: NotRequired[bool]
    runAsNonRoot: NotRequired[bool]

class EksContainerVolumeMountTypeDef(TypedDict):
    name: NotRequired[str]
    mountPath: NotRequired[str]
    subPath: NotRequired[str]
    readOnly: NotRequired[bool]

class EksContainerResourceRequirementsTypeDef(TypedDict):
    limits: NotRequired[Mapping[str, str]]
    requests: NotRequired[Mapping[str, str]]

class EksEmptyDirTypeDef(TypedDict):
    medium: NotRequired[str]
    sizeLimit: NotRequired[str]

class EksHostPathTypeDef(TypedDict):
    path: NotRequired[str]

class EksMetadataOutputTypeDef(TypedDict):
    labels: NotRequired[Dict[str, str]]
    annotations: NotRequired[Dict[str, str]]
    namespace: NotRequired[str]

class EksMetadataTypeDef(TypedDict):
    labels: NotRequired[Mapping[str, str]]
    annotations: NotRequired[Mapping[str, str]]
    namespace: NotRequired[str]

class EksPersistentVolumeClaimTypeDef(TypedDict):
    claimName: str
    readOnly: NotRequired[bool]

class ImagePullSecretTypeDef(TypedDict):
    name: str

class EksSecretTypeDef(TypedDict):
    secretName: str
    optional: NotRequired[bool]

class EvaluateOnExitTypeDef(TypedDict):
    action: RetryActionType
    onStatusReason: NotRequired[str]
    onReason: NotRequired[str]
    onExitCode: NotRequired[str]

class ShareAttributesTypeDef(TypedDict):
    shareIdentifier: str
    weightFactor: NotRequired[float]

FirelensConfigurationOutputTypeDef = TypedDict(
    "FirelensConfigurationOutputTypeDef",
    {
        "type": FirelensConfigurationTypeType,
        "options": NotRequired[Dict[str, str]],
    },
)
FirelensConfigurationTypeDef = TypedDict(
    "FirelensConfigurationTypeDef",
    {
        "type": FirelensConfigurationTypeType,
        "options": NotRequired[Mapping[str, str]],
    },
)

class FrontOfQueueJobSummaryTypeDef(TypedDict):
    jobArn: NotRequired[str]
    earliestTimeAtPosition: NotRequired[int]

class GetJobQueueSnapshotRequestTypeDef(TypedDict):
    jobQueue: str

class HostTypeDef(TypedDict):
    sourcePath: NotRequired[str]

class JobTimeoutTypeDef(TypedDict):
    attemptDurationSeconds: NotRequired[int]

JobDependencyTypeDef = TypedDict(
    "JobDependencyTypeDef",
    {
        "jobId": NotRequired[str],
        "type": NotRequired[ArrayJobDependencyType],
    },
)

class NodeDetailsTypeDef(TypedDict):
    nodeIndex: NotRequired[int]
    isMainNode: NotRequired[bool]

class NodePropertiesSummaryTypeDef(TypedDict):
    isMainNode: NotRequired[bool]
    numNodes: NotRequired[int]
    nodeIndex: NotRequired[int]

class KeyValuesPairTypeDef(TypedDict):
    name: NotRequired[str]
    values: NotRequired[Sequence[str]]

class LaunchTemplateSpecificationOverrideOutputTypeDef(TypedDict):
    launchTemplateId: NotRequired[str]
    launchTemplateName: NotRequired[str]
    version: NotRequired[str]
    targetInstanceTypes: NotRequired[List[str]]

class LaunchTemplateSpecificationOverrideTypeDef(TypedDict):
    launchTemplateId: NotRequired[str]
    launchTemplateName: NotRequired[str]
    version: NotRequired[str]
    targetInstanceTypes: NotRequired[Sequence[str]]

class TmpfsOutputTypeDef(TypedDict):
    containerPath: str
    size: int
    mountOptions: NotRequired[List[str]]

class TmpfsTypeDef(TypedDict):
    containerPath: str
    size: int
    mountOptions: NotRequired[Sequence[str]]

class ListSchedulingPoliciesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class SchedulingPolicyListingDetailTypeDef(TypedDict):
    arn: str

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class TaskContainerDependencyTypeDef(TypedDict):
    containerName: NotRequired[str]
    condition: NotRequired[str]

class TerminateJobRequestTypeDef(TypedDict):
    jobId: str
    reason: str

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateConsumableResourceRequestTypeDef(TypedDict):
    consumableResource: str
    operation: NotRequired[str]
    quantity: NotRequired[int]
    clientToken: NotRequired[str]

class AttemptContainerDetailTypeDef(TypedDict):
    containerInstanceArn: NotRequired[str]
    taskArn: NotRequired[str]
    exitCode: NotRequired[int]
    reason: NotRequired[str]
    logStreamName: NotRequired[str]
    networkInterfaces: NotRequired[List[NetworkInterfaceTypeDef]]

class AttemptTaskContainerDetailsTypeDef(TypedDict):
    exitCode: NotRequired[int]
    name: NotRequired[str]
    reason: NotRequired[str]
    logStreamName: NotRequired[str]
    networkInterfaces: NotRequired[List[NetworkInterfaceTypeDef]]

class ConsumableResourcePropertiesOutputTypeDef(TypedDict):
    consumableResourceList: NotRequired[List[ConsumableResourceRequirementTypeDef]]

class ConsumableResourcePropertiesTypeDef(TypedDict):
    consumableResourceList: NotRequired[Sequence[ConsumableResourceRequirementTypeDef]]

class ContainerOverridesTypeDef(TypedDict):
    vcpus: NotRequired[int]
    memory: NotRequired[int]
    command: NotRequired[Sequence[str]]
    instanceType: NotRequired[str]
    environment: NotRequired[Sequence[KeyValuePairTypeDef]]
    resourceRequirements: NotRequired[Sequence[ResourceRequirementTypeDef]]

class TaskContainerOverridesTypeDef(TypedDict):
    command: NotRequired[Sequence[str]]
    environment: NotRequired[Sequence[KeyValuePairTypeDef]]
    name: NotRequired[str]
    resourceRequirements: NotRequired[Sequence[ResourceRequirementTypeDef]]

class LogConfigurationOutputTypeDef(TypedDict):
    logDriver: LogDriverType
    options: NotRequired[Dict[str, str]]
    secretOptions: NotRequired[List[SecretTypeDef]]

class LogConfigurationTypeDef(TypedDict):
    logDriver: LogDriverType
    options: NotRequired[Mapping[str, str]]
    secretOptions: NotRequired[Sequence[SecretTypeDef]]

class CreateComputeEnvironmentResponseTypeDef(TypedDict):
    computeEnvironmentName: str
    computeEnvironmentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConsumableResourceResponseTypeDef(TypedDict):
    consumableResourceName: str
    consumableResourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobQueueResponseTypeDef(TypedDict):
    jobQueueName: str
    jobQueueArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSchedulingPolicyResponseTypeDef(TypedDict):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConsumableResourceResponseTypeDef(TypedDict):
    consumableResourceName: str
    consumableResourceArn: str
    totalQuantity: int
    inUseQuantity: int
    availableQuantity: int
    resourceType: str
    createdAt: int
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListConsumableResourcesResponseTypeDef(TypedDict):
    consumableResources: List[ConsumableResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterJobDefinitionResponseTypeDef(TypedDict):
    jobDefinitionName: str
    jobDefinitionArn: str
    revision: int
    ResponseMetadata: ResponseMetadataTypeDef

class SubmitJobResponseTypeDef(TypedDict):
    jobArn: str
    jobName: str
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateComputeEnvironmentResponseTypeDef(TypedDict):
    computeEnvironmentName: str
    computeEnvironmentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConsumableResourceResponseTypeDef(TypedDict):
    consumableResourceName: str
    consumableResourceArn: str
    totalQuantity: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateJobQueueResponseTypeDef(TypedDict):
    jobQueueName: str
    jobQueueArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobQueueRequestTypeDef(TypedDict):
    jobQueueName: str
    priority: int
    computeEnvironmentOrder: Sequence[ComputeEnvironmentOrderTypeDef]
    state: NotRequired[JQStateType]
    schedulingPolicyArn: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    jobStateTimeLimitActions: NotRequired[Sequence[JobStateTimeLimitActionTypeDef]]

class JobQueueDetailTypeDef(TypedDict):
    jobQueueName: str
    jobQueueArn: str
    state: JQStateType
    priority: int
    computeEnvironmentOrder: List[ComputeEnvironmentOrderTypeDef]
    schedulingPolicyArn: NotRequired[str]
    status: NotRequired[JQStatusType]
    statusReason: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    jobStateTimeLimitActions: NotRequired[List[JobStateTimeLimitActionTypeDef]]

class UpdateJobQueueRequestTypeDef(TypedDict):
    jobQueue: str
    state: NotRequired[JQStateType]
    schedulingPolicyArn: NotRequired[str]
    priority: NotRequired[int]
    computeEnvironmentOrder: NotRequired[Sequence[ComputeEnvironmentOrderTypeDef]]
    jobStateTimeLimitActions: NotRequired[Sequence[JobStateTimeLimitActionTypeDef]]

class DescribeComputeEnvironmentsRequestPaginateTypeDef(TypedDict):
    computeEnvironments: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeJobDefinitionsRequestPaginateTypeDef(TypedDict):
    jobDefinitions: NotRequired[Sequence[str]]
    jobDefinitionName: NotRequired[str]
    status: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeJobQueuesRequestPaginateTypeDef(TypedDict):
    jobQueues: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSchedulingPoliciesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class EFSVolumeConfigurationTypeDef(TypedDict):
    fileSystemId: str
    rootDirectory: NotRequired[str]
    transitEncryption: NotRequired[EFSTransitEncryptionType]
    transitEncryptionPort: NotRequired[int]
    authorizationConfig: NotRequired[EFSAuthorizationConfigTypeDef]

class EksAttemptDetailTypeDef(TypedDict):
    containers: NotRequired[List[EksAttemptContainerDetailTypeDef]]
    initContainers: NotRequired[List[EksAttemptContainerDetailTypeDef]]
    eksClusterArn: NotRequired[str]
    podName: NotRequired[str]
    podNamespace: NotRequired[str]
    nodeName: NotRequired[str]
    startedAt: NotRequired[int]
    stoppedAt: NotRequired[int]
    statusReason: NotRequired[str]

class EksContainerDetailTypeDef(TypedDict):
    name: NotRequired[str]
    image: NotRequired[str]
    imagePullPolicy: NotRequired[str]
    command: NotRequired[List[str]]
    args: NotRequired[List[str]]
    env: NotRequired[List[EksContainerEnvironmentVariableTypeDef]]
    resources: NotRequired[EksContainerResourceRequirementsOutputTypeDef]
    exitCode: NotRequired[int]
    reason: NotRequired[str]
    volumeMounts: NotRequired[List[EksContainerVolumeMountTypeDef]]
    securityContext: NotRequired[EksContainerSecurityContextTypeDef]

class EksContainerOutputTypeDef(TypedDict):
    image: str
    name: NotRequired[str]
    imagePullPolicy: NotRequired[str]
    command: NotRequired[List[str]]
    args: NotRequired[List[str]]
    env: NotRequired[List[EksContainerEnvironmentVariableTypeDef]]
    resources: NotRequired[EksContainerResourceRequirementsOutputTypeDef]
    volumeMounts: NotRequired[List[EksContainerVolumeMountTypeDef]]
    securityContext: NotRequired[EksContainerSecurityContextTypeDef]

EksContainerResourceRequirementsUnionTypeDef = Union[
    EksContainerResourceRequirementsTypeDef, EksContainerResourceRequirementsOutputTypeDef
]

class EksContainerTypeDef(TypedDict):
    image: str
    name: NotRequired[str]
    imagePullPolicy: NotRequired[str]
    command: NotRequired[Sequence[str]]
    args: NotRequired[Sequence[str]]
    env: NotRequired[Sequence[EksContainerEnvironmentVariableTypeDef]]
    resources: NotRequired[EksContainerResourceRequirementsTypeDef]
    volumeMounts: NotRequired[Sequence[EksContainerVolumeMountTypeDef]]
    securityContext: NotRequired[EksContainerSecurityContextTypeDef]

EksMetadataUnionTypeDef = Union[EksMetadataTypeDef, EksMetadataOutputTypeDef]

class EksVolumeTypeDef(TypedDict):
    name: str
    hostPath: NotRequired[EksHostPathTypeDef]
    emptyDir: NotRequired[EksEmptyDirTypeDef]
    secret: NotRequired[EksSecretTypeDef]
    persistentVolumeClaim: NotRequired[EksPersistentVolumeClaimTypeDef]

class RetryStrategyOutputTypeDef(TypedDict):
    attempts: NotRequired[int]
    evaluateOnExit: NotRequired[List[EvaluateOnExitTypeDef]]

class RetryStrategyTypeDef(TypedDict):
    attempts: NotRequired[int]
    evaluateOnExit: NotRequired[Sequence[EvaluateOnExitTypeDef]]

class FairsharePolicyOutputTypeDef(TypedDict):
    shareDecaySeconds: NotRequired[int]
    computeReservation: NotRequired[int]
    shareDistribution: NotRequired[List[ShareAttributesTypeDef]]

class FairsharePolicyTypeDef(TypedDict):
    shareDecaySeconds: NotRequired[int]
    computeReservation: NotRequired[int]
    shareDistribution: NotRequired[Sequence[ShareAttributesTypeDef]]

class FrontOfQueueDetailTypeDef(TypedDict):
    jobs: NotRequired[List[FrontOfQueueJobSummaryTypeDef]]
    lastUpdatedAt: NotRequired[int]

class JobSummaryTypeDef(TypedDict):
    jobId: str
    jobName: str
    jobArn: NotRequired[str]
    createdAt: NotRequired[int]
    status: NotRequired[JobStatusType]
    statusReason: NotRequired[str]
    startedAt: NotRequired[int]
    stoppedAt: NotRequired[int]
    container: NotRequired[ContainerSummaryTypeDef]
    arrayProperties: NotRequired[ArrayPropertiesSummaryTypeDef]
    nodeProperties: NotRequired[NodePropertiesSummaryTypeDef]
    jobDefinition: NotRequired[str]

class ListConsumableResourcesRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[KeyValuesPairTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConsumableResourcesRequestTypeDef(TypedDict):
    filters: NotRequired[Sequence[KeyValuesPairTypeDef]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListJobsByConsumableResourceRequestPaginateTypeDef(TypedDict):
    consumableResource: str
    filters: NotRequired[Sequence[KeyValuesPairTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListJobsByConsumableResourceRequestTypeDef(TypedDict):
    consumableResource: str
    filters: NotRequired[Sequence[KeyValuesPairTypeDef]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListJobsRequestPaginateTypeDef(TypedDict):
    jobQueue: NotRequired[str]
    arrayJobId: NotRequired[str]
    multiNodeJobId: NotRequired[str]
    jobStatus: NotRequired[JobStatusType]
    filters: NotRequired[Sequence[KeyValuesPairTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListJobsRequestTypeDef(TypedDict):
    jobQueue: NotRequired[str]
    arrayJobId: NotRequired[str]
    multiNodeJobId: NotRequired[str]
    jobStatus: NotRequired[JobStatusType]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    filters: NotRequired[Sequence[KeyValuesPairTypeDef]]

class LaunchTemplateSpecificationOutputTypeDef(TypedDict):
    launchTemplateId: NotRequired[str]
    launchTemplateName: NotRequired[str]
    version: NotRequired[str]
    overrides: NotRequired[List[LaunchTemplateSpecificationOverrideOutputTypeDef]]

LaunchTemplateSpecificationOverrideUnionTypeDef = Union[
    LaunchTemplateSpecificationOverrideTypeDef, LaunchTemplateSpecificationOverrideOutputTypeDef
]

class LinuxParametersOutputTypeDef(TypedDict):
    devices: NotRequired[List[DeviceOutputTypeDef]]
    initProcessEnabled: NotRequired[bool]
    sharedMemorySize: NotRequired[int]
    tmpfs: NotRequired[List[TmpfsOutputTypeDef]]
    maxSwap: NotRequired[int]
    swappiness: NotRequired[int]

class LinuxParametersTypeDef(TypedDict):
    devices: NotRequired[Sequence[DeviceTypeDef]]
    initProcessEnabled: NotRequired[bool]
    sharedMemorySize: NotRequired[int]
    tmpfs: NotRequired[Sequence[TmpfsTypeDef]]
    maxSwap: NotRequired[int]
    swappiness: NotRequired[int]

class ListSchedulingPoliciesResponseTypeDef(TypedDict):
    schedulingPolicies: List[SchedulingPolicyListingDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AttemptEcsTaskDetailsTypeDef(TypedDict):
    containerInstanceArn: NotRequired[str]
    taskArn: NotRequired[str]
    containers: NotRequired[List[AttemptTaskContainerDetailsTypeDef]]

class ListJobsByConsumableResourceSummaryTypeDef(TypedDict):
    jobArn: str
    jobQueueArn: str
    jobName: str
    jobStatus: str
    quantity: int
    createdAt: int
    consumableResourceProperties: ConsumableResourcePropertiesOutputTypeDef
    jobDefinitionArn: NotRequired[str]
    shareIdentifier: NotRequired[str]
    statusReason: NotRequired[str]
    startedAt: NotRequired[int]

ConsumableResourcePropertiesUnionTypeDef = Union[
    ConsumableResourcePropertiesTypeDef, ConsumableResourcePropertiesOutputTypeDef
]

class TaskPropertiesOverrideTypeDef(TypedDict):
    containers: NotRequired[Sequence[TaskContainerOverridesTypeDef]]

class DescribeJobQueuesResponseTypeDef(TypedDict):
    jobQueues: List[JobQueueDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class VolumeTypeDef(TypedDict):
    host: NotRequired[HostTypeDef]
    name: NotRequired[str]
    efsVolumeConfiguration: NotRequired[EFSVolumeConfigurationTypeDef]

class EksContainerOverrideTypeDef(TypedDict):
    name: NotRequired[str]
    image: NotRequired[str]
    command: NotRequired[Sequence[str]]
    args: NotRequired[Sequence[str]]
    env: NotRequired[Sequence[EksContainerEnvironmentVariableTypeDef]]
    resources: NotRequired[EksContainerResourceRequirementsUnionTypeDef]

class EksPodPropertiesDetailTypeDef(TypedDict):
    serviceAccountName: NotRequired[str]
    hostNetwork: NotRequired[bool]
    dnsPolicy: NotRequired[str]
    imagePullSecrets: NotRequired[List[ImagePullSecretTypeDef]]
    containers: NotRequired[List[EksContainerDetailTypeDef]]
    initContainers: NotRequired[List[EksContainerDetailTypeDef]]
    volumes: NotRequired[List[EksVolumeTypeDef]]
    podName: NotRequired[str]
    nodeName: NotRequired[str]
    metadata: NotRequired[EksMetadataOutputTypeDef]
    shareProcessNamespace: NotRequired[bool]

class EksPodPropertiesOutputTypeDef(TypedDict):
    serviceAccountName: NotRequired[str]
    hostNetwork: NotRequired[bool]
    dnsPolicy: NotRequired[str]
    imagePullSecrets: NotRequired[List[ImagePullSecretTypeDef]]
    containers: NotRequired[List[EksContainerOutputTypeDef]]
    initContainers: NotRequired[List[EksContainerOutputTypeDef]]
    volumes: NotRequired[List[EksVolumeTypeDef]]
    metadata: NotRequired[EksMetadataOutputTypeDef]
    shareProcessNamespace: NotRequired[bool]

class EksPodPropertiesTypeDef(TypedDict):
    serviceAccountName: NotRequired[str]
    hostNetwork: NotRequired[bool]
    dnsPolicy: NotRequired[str]
    imagePullSecrets: NotRequired[Sequence[ImagePullSecretTypeDef]]
    containers: NotRequired[Sequence[EksContainerTypeDef]]
    initContainers: NotRequired[Sequence[EksContainerTypeDef]]
    volumes: NotRequired[Sequence[EksVolumeTypeDef]]
    metadata: NotRequired[EksMetadataTypeDef]
    shareProcessNamespace: NotRequired[bool]

RetryStrategyUnionTypeDef = Union[RetryStrategyTypeDef, RetryStrategyOutputTypeDef]

class SchedulingPolicyDetailTypeDef(TypedDict):
    name: str
    arn: str
    fairsharePolicy: NotRequired[FairsharePolicyOutputTypeDef]
    tags: NotRequired[Dict[str, str]]

FairsharePolicyUnionTypeDef = Union[FairsharePolicyTypeDef, FairsharePolicyOutputTypeDef]

class GetJobQueueSnapshotResponseTypeDef(TypedDict):
    frontOfQueue: FrontOfQueueDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobsResponseTypeDef(TypedDict):
    jobSummaryList: List[JobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ComputeResourceOutputTypeDef = TypedDict(
    "ComputeResourceOutputTypeDef",
    {
        "type": CRTypeType,
        "maxvCpus": int,
        "subnets": List[str],
        "allocationStrategy": NotRequired[CRAllocationStrategyType],
        "minvCpus": NotRequired[int],
        "desiredvCpus": NotRequired[int],
        "instanceTypes": NotRequired[List[str]],
        "imageId": NotRequired[str],
        "securityGroupIds": NotRequired[List[str]],
        "ec2KeyPair": NotRequired[str],
        "instanceRole": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "placementGroup": NotRequired[str],
        "bidPercentage": NotRequired[int],
        "spotIamFleetRole": NotRequired[str],
        "launchTemplate": NotRequired[LaunchTemplateSpecificationOutputTypeDef],
        "ec2Configuration": NotRequired[List[Ec2ConfigurationTypeDef]],
    },
)

class LaunchTemplateSpecificationTypeDef(TypedDict):
    launchTemplateId: NotRequired[str]
    launchTemplateName: NotRequired[str]
    version: NotRequired[str]
    overrides: NotRequired[Sequence[LaunchTemplateSpecificationOverrideUnionTypeDef]]

class TaskContainerDetailsTypeDef(TypedDict):
    command: NotRequired[List[str]]
    dependsOn: NotRequired[List[TaskContainerDependencyTypeDef]]
    environment: NotRequired[List[KeyValuePairTypeDef]]
    essential: NotRequired[bool]
    firelensConfiguration: NotRequired[FirelensConfigurationOutputTypeDef]
    image: NotRequired[str]
    linuxParameters: NotRequired[LinuxParametersOutputTypeDef]
    logConfiguration: NotRequired[LogConfigurationOutputTypeDef]
    mountPoints: NotRequired[List[MountPointTypeDef]]
    name: NotRequired[str]
    privileged: NotRequired[bool]
    readonlyRootFilesystem: NotRequired[bool]
    repositoryCredentials: NotRequired[RepositoryCredentialsTypeDef]
    resourceRequirements: NotRequired[List[ResourceRequirementTypeDef]]
    secrets: NotRequired[List[SecretTypeDef]]
    ulimits: NotRequired[List[UlimitTypeDef]]
    user: NotRequired[str]
    exitCode: NotRequired[int]
    reason: NotRequired[str]
    logStreamName: NotRequired[str]
    networkInterfaces: NotRequired[List[NetworkInterfaceTypeDef]]

class TaskContainerPropertiesOutputTypeDef(TypedDict):
    image: str
    command: NotRequired[List[str]]
    dependsOn: NotRequired[List[TaskContainerDependencyTypeDef]]
    environment: NotRequired[List[KeyValuePairTypeDef]]
    essential: NotRequired[bool]
    firelensConfiguration: NotRequired[FirelensConfigurationOutputTypeDef]
    linuxParameters: NotRequired[LinuxParametersOutputTypeDef]
    logConfiguration: NotRequired[LogConfigurationOutputTypeDef]
    mountPoints: NotRequired[List[MountPointTypeDef]]
    name: NotRequired[str]
    privileged: NotRequired[bool]
    readonlyRootFilesystem: NotRequired[bool]
    repositoryCredentials: NotRequired[RepositoryCredentialsTypeDef]
    resourceRequirements: NotRequired[List[ResourceRequirementTypeDef]]
    secrets: NotRequired[List[SecretTypeDef]]
    ulimits: NotRequired[List[UlimitTypeDef]]
    user: NotRequired[str]

class TaskContainerPropertiesTypeDef(TypedDict):
    image: str
    command: NotRequired[Sequence[str]]
    dependsOn: NotRequired[Sequence[TaskContainerDependencyTypeDef]]
    environment: NotRequired[Sequence[KeyValuePairTypeDef]]
    essential: NotRequired[bool]
    firelensConfiguration: NotRequired[FirelensConfigurationTypeDef]
    linuxParameters: NotRequired[LinuxParametersTypeDef]
    logConfiguration: NotRequired[LogConfigurationTypeDef]
    mountPoints: NotRequired[Sequence[MountPointTypeDef]]
    name: NotRequired[str]
    privileged: NotRequired[bool]
    readonlyRootFilesystem: NotRequired[bool]
    repositoryCredentials: NotRequired[RepositoryCredentialsTypeDef]
    resourceRequirements: NotRequired[Sequence[ResourceRequirementTypeDef]]
    secrets: NotRequired[Sequence[SecretTypeDef]]
    ulimits: NotRequired[Sequence[UlimitTypeDef]]
    user: NotRequired[str]

class AttemptDetailTypeDef(TypedDict):
    container: NotRequired[AttemptContainerDetailTypeDef]
    startedAt: NotRequired[int]
    stoppedAt: NotRequired[int]
    statusReason: NotRequired[str]
    taskProperties: NotRequired[List[AttemptEcsTaskDetailsTypeDef]]

class ListJobsByConsumableResourceResponseTypeDef(TypedDict):
    jobs: List[ListJobsByConsumableResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class EcsPropertiesOverrideTypeDef(TypedDict):
    taskProperties: NotRequired[Sequence[TaskPropertiesOverrideTypeDef]]

class ContainerDetailTypeDef(TypedDict):
    image: NotRequired[str]
    vcpus: NotRequired[int]
    memory: NotRequired[int]
    command: NotRequired[List[str]]
    jobRoleArn: NotRequired[str]
    executionRoleArn: NotRequired[str]
    volumes: NotRequired[List[VolumeTypeDef]]
    environment: NotRequired[List[KeyValuePairTypeDef]]
    mountPoints: NotRequired[List[MountPointTypeDef]]
    readonlyRootFilesystem: NotRequired[bool]
    ulimits: NotRequired[List[UlimitTypeDef]]
    privileged: NotRequired[bool]
    user: NotRequired[str]
    exitCode: NotRequired[int]
    reason: NotRequired[str]
    containerInstanceArn: NotRequired[str]
    taskArn: NotRequired[str]
    logStreamName: NotRequired[str]
    instanceType: NotRequired[str]
    networkInterfaces: NotRequired[List[NetworkInterfaceTypeDef]]
    resourceRequirements: NotRequired[List[ResourceRequirementTypeDef]]
    linuxParameters: NotRequired[LinuxParametersOutputTypeDef]
    logConfiguration: NotRequired[LogConfigurationOutputTypeDef]
    secrets: NotRequired[List[SecretTypeDef]]
    networkConfiguration: NotRequired[NetworkConfigurationTypeDef]
    fargatePlatformConfiguration: NotRequired[FargatePlatformConfigurationTypeDef]
    ephemeralStorage: NotRequired[EphemeralStorageTypeDef]
    runtimePlatform: NotRequired[RuntimePlatformTypeDef]
    repositoryCredentials: NotRequired[RepositoryCredentialsTypeDef]
    enableExecuteCommand: NotRequired[bool]

class ContainerPropertiesOutputTypeDef(TypedDict):
    image: NotRequired[str]
    vcpus: NotRequired[int]
    memory: NotRequired[int]
    command: NotRequired[List[str]]
    jobRoleArn: NotRequired[str]
    executionRoleArn: NotRequired[str]
    volumes: NotRequired[List[VolumeTypeDef]]
    environment: NotRequired[List[KeyValuePairTypeDef]]
    mountPoints: NotRequired[List[MountPointTypeDef]]
    readonlyRootFilesystem: NotRequired[bool]
    privileged: NotRequired[bool]
    ulimits: NotRequired[List[UlimitTypeDef]]
    user: NotRequired[str]
    instanceType: NotRequired[str]
    resourceRequirements: NotRequired[List[ResourceRequirementTypeDef]]
    linuxParameters: NotRequired[LinuxParametersOutputTypeDef]
    logConfiguration: NotRequired[LogConfigurationOutputTypeDef]
    secrets: NotRequired[List[SecretTypeDef]]
    networkConfiguration: NotRequired[NetworkConfigurationTypeDef]
    fargatePlatformConfiguration: NotRequired[FargatePlatformConfigurationTypeDef]
    enableExecuteCommand: NotRequired[bool]
    ephemeralStorage: NotRequired[EphemeralStorageTypeDef]
    runtimePlatform: NotRequired[RuntimePlatformTypeDef]
    repositoryCredentials: NotRequired[RepositoryCredentialsTypeDef]

class ContainerPropertiesTypeDef(TypedDict):
    image: NotRequired[str]
    vcpus: NotRequired[int]
    memory: NotRequired[int]
    command: NotRequired[Sequence[str]]
    jobRoleArn: NotRequired[str]
    executionRoleArn: NotRequired[str]
    volumes: NotRequired[Sequence[VolumeTypeDef]]
    environment: NotRequired[Sequence[KeyValuePairTypeDef]]
    mountPoints: NotRequired[Sequence[MountPointTypeDef]]
    readonlyRootFilesystem: NotRequired[bool]
    privileged: NotRequired[bool]
    ulimits: NotRequired[Sequence[UlimitTypeDef]]
    user: NotRequired[str]
    instanceType: NotRequired[str]
    resourceRequirements: NotRequired[Sequence[ResourceRequirementTypeDef]]
    linuxParameters: NotRequired[LinuxParametersTypeDef]
    logConfiguration: NotRequired[LogConfigurationTypeDef]
    secrets: NotRequired[Sequence[SecretTypeDef]]
    networkConfiguration: NotRequired[NetworkConfigurationTypeDef]
    fargatePlatformConfiguration: NotRequired[FargatePlatformConfigurationTypeDef]
    enableExecuteCommand: NotRequired[bool]
    ephemeralStorage: NotRequired[EphemeralStorageTypeDef]
    runtimePlatform: NotRequired[RuntimePlatformTypeDef]
    repositoryCredentials: NotRequired[RepositoryCredentialsTypeDef]

class EksPodPropertiesOverrideTypeDef(TypedDict):
    containers: NotRequired[Sequence[EksContainerOverrideTypeDef]]
    initContainers: NotRequired[Sequence[EksContainerOverrideTypeDef]]
    metadata: NotRequired[EksMetadataUnionTypeDef]

class EksPropertiesDetailTypeDef(TypedDict):
    podProperties: NotRequired[EksPodPropertiesDetailTypeDef]

class EksPropertiesOutputTypeDef(TypedDict):
    podProperties: NotRequired[EksPodPropertiesOutputTypeDef]

class EksPropertiesTypeDef(TypedDict):
    podProperties: NotRequired[EksPodPropertiesTypeDef]

class DescribeSchedulingPoliciesResponseTypeDef(TypedDict):
    schedulingPolicies: List[SchedulingPolicyDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSchedulingPolicyRequestTypeDef(TypedDict):
    name: str
    fairsharePolicy: NotRequired[FairsharePolicyUnionTypeDef]
    tags: NotRequired[Mapping[str, str]]

class UpdateSchedulingPolicyRequestTypeDef(TypedDict):
    arn: str
    fairsharePolicy: NotRequired[FairsharePolicyUnionTypeDef]

ComputeEnvironmentDetailTypeDef = TypedDict(
    "ComputeEnvironmentDetailTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
        "unmanagedvCpus": NotRequired[int],
        "ecsClusterArn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "type": NotRequired[CETypeType],
        "state": NotRequired[CEStateType],
        "status": NotRequired[CEStatusType],
        "statusReason": NotRequired[str],
        "computeResources": NotRequired[ComputeResourceOutputTypeDef],
        "serviceRole": NotRequired[str],
        "updatePolicy": NotRequired[UpdatePolicyTypeDef],
        "eksConfiguration": NotRequired[EksConfigurationTypeDef],
        "containerOrchestrationType": NotRequired[OrchestrationTypeType],
        "uuid": NotRequired[str],
        "context": NotRequired[str],
    },
)
ComputeResourceTypeDef = TypedDict(
    "ComputeResourceTypeDef",
    {
        "type": CRTypeType,
        "maxvCpus": int,
        "subnets": Sequence[str],
        "allocationStrategy": NotRequired[CRAllocationStrategyType],
        "minvCpus": NotRequired[int],
        "desiredvCpus": NotRequired[int],
        "instanceTypes": NotRequired[Sequence[str]],
        "imageId": NotRequired[str],
        "securityGroupIds": NotRequired[Sequence[str]],
        "ec2KeyPair": NotRequired[str],
        "instanceRole": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "placementGroup": NotRequired[str],
        "bidPercentage": NotRequired[int],
        "spotIamFleetRole": NotRequired[str],
        "launchTemplate": NotRequired[LaunchTemplateSpecificationTypeDef],
        "ec2Configuration": NotRequired[Sequence[Ec2ConfigurationTypeDef]],
    },
)
LaunchTemplateSpecificationUnionTypeDef = Union[
    LaunchTemplateSpecificationTypeDef, LaunchTemplateSpecificationOutputTypeDef
]

class EcsTaskDetailsTypeDef(TypedDict):
    containers: NotRequired[List[TaskContainerDetailsTypeDef]]
    containerInstanceArn: NotRequired[str]
    taskArn: NotRequired[str]
    ephemeralStorage: NotRequired[EphemeralStorageTypeDef]
    executionRoleArn: NotRequired[str]
    platformVersion: NotRequired[str]
    ipcMode: NotRequired[str]
    taskRoleArn: NotRequired[str]
    pidMode: NotRequired[str]
    networkConfiguration: NotRequired[NetworkConfigurationTypeDef]
    runtimePlatform: NotRequired[RuntimePlatformTypeDef]
    volumes: NotRequired[List[VolumeTypeDef]]
    enableExecuteCommand: NotRequired[bool]

class EcsTaskPropertiesOutputTypeDef(TypedDict):
    containers: List[TaskContainerPropertiesOutputTypeDef]
    ephemeralStorage: NotRequired[EphemeralStorageTypeDef]
    executionRoleArn: NotRequired[str]
    platformVersion: NotRequired[str]
    ipcMode: NotRequired[str]
    taskRoleArn: NotRequired[str]
    pidMode: NotRequired[str]
    networkConfiguration: NotRequired[NetworkConfigurationTypeDef]
    runtimePlatform: NotRequired[RuntimePlatformTypeDef]
    volumes: NotRequired[List[VolumeTypeDef]]
    enableExecuteCommand: NotRequired[bool]

class EcsTaskPropertiesTypeDef(TypedDict):
    containers: Sequence[TaskContainerPropertiesTypeDef]
    ephemeralStorage: NotRequired[EphemeralStorageTypeDef]
    executionRoleArn: NotRequired[str]
    platformVersion: NotRequired[str]
    ipcMode: NotRequired[str]
    taskRoleArn: NotRequired[str]
    pidMode: NotRequired[str]
    networkConfiguration: NotRequired[NetworkConfigurationTypeDef]
    runtimePlatform: NotRequired[RuntimePlatformTypeDef]
    volumes: NotRequired[Sequence[VolumeTypeDef]]
    enableExecuteCommand: NotRequired[bool]

ContainerPropertiesUnionTypeDef = Union[
    ContainerPropertiesTypeDef, ContainerPropertiesOutputTypeDef
]

class EksPropertiesOverrideTypeDef(TypedDict):
    podProperties: NotRequired[EksPodPropertiesOverrideTypeDef]

EksPropertiesUnionTypeDef = Union[EksPropertiesTypeDef, EksPropertiesOutputTypeDef]

class DescribeComputeEnvironmentsResponseTypeDef(TypedDict):
    computeEnvironments: List[ComputeEnvironmentDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ComputeResourceUnionTypeDef = Union[ComputeResourceTypeDef, ComputeResourceOutputTypeDef]
ComputeResourceUpdateTypeDef = TypedDict(
    "ComputeResourceUpdateTypeDef",
    {
        "minvCpus": NotRequired[int],
        "maxvCpus": NotRequired[int],
        "desiredvCpus": NotRequired[int],
        "subnets": NotRequired[Sequence[str]],
        "securityGroupIds": NotRequired[Sequence[str]],
        "allocationStrategy": NotRequired[CRUpdateAllocationStrategyType],
        "instanceTypes": NotRequired[Sequence[str]],
        "ec2KeyPair": NotRequired[str],
        "instanceRole": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "placementGroup": NotRequired[str],
        "bidPercentage": NotRequired[int],
        "launchTemplate": NotRequired[LaunchTemplateSpecificationUnionTypeDef],
        "ec2Configuration": NotRequired[Sequence[Ec2ConfigurationTypeDef]],
        "updateToLatestImageVersion": NotRequired[bool],
        "type": NotRequired[CRTypeType],
        "imageId": NotRequired[str],
    },
)

class EcsPropertiesDetailTypeDef(TypedDict):
    taskProperties: NotRequired[List[EcsTaskDetailsTypeDef]]

class EcsPropertiesOutputTypeDef(TypedDict):
    taskProperties: List[EcsTaskPropertiesOutputTypeDef]

class EcsPropertiesTypeDef(TypedDict):
    taskProperties: Sequence[EcsTaskPropertiesTypeDef]

class NodePropertyOverrideTypeDef(TypedDict):
    targetNodes: str
    containerOverrides: NotRequired[ContainerOverridesTypeDef]
    ecsPropertiesOverride: NotRequired[EcsPropertiesOverrideTypeDef]
    instanceTypes: NotRequired[Sequence[str]]
    eksPropertiesOverride: NotRequired[EksPropertiesOverrideTypeDef]
    consumableResourcePropertiesOverride: NotRequired[ConsumableResourcePropertiesUnionTypeDef]

CreateComputeEnvironmentRequestTypeDef = TypedDict(
    "CreateComputeEnvironmentRequestTypeDef",
    {
        "computeEnvironmentName": str,
        "type": CETypeType,
        "state": NotRequired[CEStateType],
        "unmanagedvCpus": NotRequired[int],
        "computeResources": NotRequired[ComputeResourceUnionTypeDef],
        "serviceRole": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "eksConfiguration": NotRequired[EksConfigurationTypeDef],
        "context": NotRequired[str],
    },
)

class UpdateComputeEnvironmentRequestTypeDef(TypedDict):
    computeEnvironment: str
    state: NotRequired[CEStateType]
    unmanagedvCpus: NotRequired[int]
    computeResources: NotRequired[ComputeResourceUpdateTypeDef]
    serviceRole: NotRequired[str]
    updatePolicy: NotRequired[UpdatePolicyTypeDef]
    context: NotRequired[str]

class NodeRangePropertyOutputTypeDef(TypedDict):
    targetNodes: str
    container: NotRequired[ContainerPropertiesOutputTypeDef]
    instanceTypes: NotRequired[List[str]]
    ecsProperties: NotRequired[EcsPropertiesOutputTypeDef]
    eksProperties: NotRequired[EksPropertiesOutputTypeDef]
    consumableResourceProperties: NotRequired[ConsumableResourcePropertiesOutputTypeDef]

EcsPropertiesUnionTypeDef = Union[EcsPropertiesTypeDef, EcsPropertiesOutputTypeDef]

class NodeRangePropertyTypeDef(TypedDict):
    targetNodes: str
    container: NotRequired[ContainerPropertiesTypeDef]
    instanceTypes: NotRequired[Sequence[str]]
    ecsProperties: NotRequired[EcsPropertiesTypeDef]
    eksProperties: NotRequired[EksPropertiesTypeDef]
    consumableResourceProperties: NotRequired[ConsumableResourcePropertiesTypeDef]

class NodeOverridesTypeDef(TypedDict):
    numNodes: NotRequired[int]
    nodePropertyOverrides: NotRequired[Sequence[NodePropertyOverrideTypeDef]]

class NodePropertiesOutputTypeDef(TypedDict):
    numNodes: int
    mainNode: int
    nodeRangeProperties: List[NodeRangePropertyOutputTypeDef]

class NodePropertiesTypeDef(TypedDict):
    numNodes: int
    mainNode: int
    nodeRangeProperties: Sequence[NodeRangePropertyTypeDef]

class SubmitJobRequestTypeDef(TypedDict):
    jobName: str
    jobQueue: str
    jobDefinition: str
    shareIdentifier: NotRequired[str]
    schedulingPriorityOverride: NotRequired[int]
    arrayProperties: NotRequired[ArrayPropertiesTypeDef]
    dependsOn: NotRequired[Sequence[JobDependencyTypeDef]]
    parameters: NotRequired[Mapping[str, str]]
    containerOverrides: NotRequired[ContainerOverridesTypeDef]
    nodeOverrides: NotRequired[NodeOverridesTypeDef]
    retryStrategy: NotRequired[RetryStrategyUnionTypeDef]
    propagateTags: NotRequired[bool]
    timeout: NotRequired[JobTimeoutTypeDef]
    tags: NotRequired[Mapping[str, str]]
    eksPropertiesOverride: NotRequired[EksPropertiesOverrideTypeDef]
    ecsPropertiesOverride: NotRequired[EcsPropertiesOverrideTypeDef]
    consumableResourcePropertiesOverride: NotRequired[ConsumableResourcePropertiesUnionTypeDef]

JobDefinitionTypeDef = TypedDict(
    "JobDefinitionTypeDef",
    {
        "jobDefinitionName": str,
        "jobDefinitionArn": str,
        "revision": int,
        "type": str,
        "status": NotRequired[str],
        "schedulingPriority": NotRequired[int],
        "parameters": NotRequired[Dict[str, str]],
        "retryStrategy": NotRequired[RetryStrategyOutputTypeDef],
        "containerProperties": NotRequired[ContainerPropertiesOutputTypeDef],
        "timeout": NotRequired[JobTimeoutTypeDef],
        "nodeProperties": NotRequired[NodePropertiesOutputTypeDef],
        "tags": NotRequired[Dict[str, str]],
        "propagateTags": NotRequired[bool],
        "platformCapabilities": NotRequired[List[PlatformCapabilityType]],
        "ecsProperties": NotRequired[EcsPropertiesOutputTypeDef],
        "eksProperties": NotRequired[EksPropertiesOutputTypeDef],
        "containerOrchestrationType": NotRequired[OrchestrationTypeType],
        "consumableResourceProperties": NotRequired[ConsumableResourcePropertiesOutputTypeDef],
    },
)

class JobDetailTypeDef(TypedDict):
    jobName: str
    jobId: str
    jobQueue: str
    status: JobStatusType
    startedAt: int
    jobDefinition: str
    jobArn: NotRequired[str]
    shareIdentifier: NotRequired[str]
    schedulingPriority: NotRequired[int]
    attempts: NotRequired[List[AttemptDetailTypeDef]]
    statusReason: NotRequired[str]
    createdAt: NotRequired[int]
    retryStrategy: NotRequired[RetryStrategyOutputTypeDef]
    stoppedAt: NotRequired[int]
    dependsOn: NotRequired[List[JobDependencyTypeDef]]
    parameters: NotRequired[Dict[str, str]]
    container: NotRequired[ContainerDetailTypeDef]
    nodeDetails: NotRequired[NodeDetailsTypeDef]
    nodeProperties: NotRequired[NodePropertiesOutputTypeDef]
    arrayProperties: NotRequired[ArrayPropertiesDetailTypeDef]
    timeout: NotRequired[JobTimeoutTypeDef]
    tags: NotRequired[Dict[str, str]]
    propagateTags: NotRequired[bool]
    platformCapabilities: NotRequired[List[PlatformCapabilityType]]
    eksProperties: NotRequired[EksPropertiesDetailTypeDef]
    eksAttempts: NotRequired[List[EksAttemptDetailTypeDef]]
    ecsProperties: NotRequired[EcsPropertiesDetailTypeDef]
    isCancelled: NotRequired[bool]
    isTerminated: NotRequired[bool]
    consumableResourceProperties: NotRequired[ConsumableResourcePropertiesOutputTypeDef]

NodePropertiesUnionTypeDef = Union[NodePropertiesTypeDef, NodePropertiesOutputTypeDef]

class DescribeJobDefinitionsResponseTypeDef(TypedDict):
    jobDefinitions: List[JobDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeJobsResponseTypeDef(TypedDict):
    jobs: List[JobDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

RegisterJobDefinitionRequestTypeDef = TypedDict(
    "RegisterJobDefinitionRequestTypeDef",
    {
        "jobDefinitionName": str,
        "type": JobDefinitionTypeType,
        "parameters": NotRequired[Mapping[str, str]],
        "schedulingPriority": NotRequired[int],
        "containerProperties": NotRequired[ContainerPropertiesUnionTypeDef],
        "nodeProperties": NotRequired[NodePropertiesUnionTypeDef],
        "retryStrategy": NotRequired[RetryStrategyUnionTypeDef],
        "propagateTags": NotRequired[bool],
        "timeout": NotRequired[JobTimeoutTypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "platformCapabilities": NotRequired[Sequence[PlatformCapabilityType]],
        "eksProperties": NotRequired[EksPropertiesUnionTypeDef],
        "ecsProperties": NotRequired[EcsPropertiesUnionTypeDef],
        "consumableResourceProperties": NotRequired[ConsumableResourcePropertiesUnionTypeDef],
    },
)
