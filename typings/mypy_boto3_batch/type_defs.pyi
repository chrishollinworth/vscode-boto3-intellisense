"""
Type annotations for batch service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/type_defs.html)

Usage::

    ```python
    from mypy_boto3_batch.type_defs import ArrayPropertiesDetailTypeDef

    data: ArrayPropertiesDetailTypeDef = {...}
    ```
"""

import sys
from typing import Any, Dict, List

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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ArrayPropertiesDetailTypeDef",
    "ArrayPropertiesSummaryTypeDef",
    "ArrayPropertiesTypeDef",
    "AttemptContainerDetailTypeDef",
    "AttemptDetailTypeDef",
    "AttemptEcsTaskDetailsTypeDef",
    "AttemptTaskContainerDetailsTypeDef",
    "CancelJobRequestRequestTypeDef",
    "ComputeEnvironmentDetailTypeDef",
    "ComputeEnvironmentOrderTypeDef",
    "ComputeResourceTypeDef",
    "ComputeResourceUpdateTypeDef",
    "ContainerDetailTypeDef",
    "ContainerOverridesTypeDef",
    "ContainerPropertiesTypeDef",
    "ContainerSummaryTypeDef",
    "CreateComputeEnvironmentRequestRequestTypeDef",
    "CreateComputeEnvironmentResponseTypeDef",
    "CreateJobQueueRequestRequestTypeDef",
    "CreateJobQueueResponseTypeDef",
    "CreateSchedulingPolicyRequestRequestTypeDef",
    "CreateSchedulingPolicyResponseTypeDef",
    "DeleteComputeEnvironmentRequestRequestTypeDef",
    "DeleteJobQueueRequestRequestTypeDef",
    "DeleteSchedulingPolicyRequestRequestTypeDef",
    "DeregisterJobDefinitionRequestRequestTypeDef",
    "DescribeComputeEnvironmentsRequestRequestTypeDef",
    "DescribeComputeEnvironmentsResponseTypeDef",
    "DescribeJobDefinitionsRequestRequestTypeDef",
    "DescribeJobDefinitionsResponseTypeDef",
    "DescribeJobQueuesRequestRequestTypeDef",
    "DescribeJobQueuesResponseTypeDef",
    "DescribeJobsRequestRequestTypeDef",
    "DescribeJobsResponseTypeDef",
    "DescribeSchedulingPoliciesRequestRequestTypeDef",
    "DescribeSchedulingPoliciesResponseTypeDef",
    "DeviceTypeDef",
    "EFSAuthorizationConfigTypeDef",
    "EFSVolumeConfigurationTypeDef",
    "Ec2ConfigurationTypeDef",
    "EcsPropertiesDetailTypeDef",
    "EcsPropertiesOverrideTypeDef",
    "EcsPropertiesTypeDef",
    "EcsTaskDetailsTypeDef",
    "EcsTaskPropertiesTypeDef",
    "EksAttemptContainerDetailTypeDef",
    "EksAttemptDetailTypeDef",
    "EksConfigurationTypeDef",
    "EksContainerDetailTypeDef",
    "EksContainerEnvironmentVariableTypeDef",
    "EksContainerOverrideTypeDef",
    "EksContainerResourceRequirementsTypeDef",
    "EksContainerSecurityContextTypeDef",
    "EksContainerTypeDef",
    "EksContainerVolumeMountTypeDef",
    "EksEmptyDirTypeDef",
    "EksHostPathTypeDef",
    "EksMetadataTypeDef",
    "EksPodPropertiesDetailTypeDef",
    "EksPodPropertiesOverrideTypeDef",
    "EksPodPropertiesTypeDef",
    "EksPropertiesDetailTypeDef",
    "EksPropertiesOverrideTypeDef",
    "EksPropertiesTypeDef",
    "EksSecretTypeDef",
    "EksVolumeTypeDef",
    "EphemeralStorageTypeDef",
    "EvaluateOnExitTypeDef",
    "FairsharePolicyTypeDef",
    "FargatePlatformConfigurationTypeDef",
    "FrontOfQueueDetailTypeDef",
    "FrontOfQueueJobSummaryTypeDef",
    "GetJobQueueSnapshotRequestRequestTypeDef",
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
    "LaunchTemplateSpecificationTypeDef",
    "LinuxParametersTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListJobsResponseTypeDef",
    "ListSchedulingPoliciesRequestRequestTypeDef",
    "ListSchedulingPoliciesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogConfigurationTypeDef",
    "MountPointTypeDef",
    "NetworkConfigurationTypeDef",
    "NetworkInterfaceTypeDef",
    "NodeDetailsTypeDef",
    "NodeOverridesTypeDef",
    "NodePropertiesSummaryTypeDef",
    "NodePropertiesTypeDef",
    "NodePropertyOverrideTypeDef",
    "NodeRangePropertyTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterJobDefinitionRequestRequestTypeDef",
    "RegisterJobDefinitionResponseTypeDef",
    "RepositoryCredentialsTypeDef",
    "ResourceRequirementTypeDef",
    "ResponseMetadataTypeDef",
    "RetryStrategyTypeDef",
    "RuntimePlatformTypeDef",
    "SchedulingPolicyDetailTypeDef",
    "SchedulingPolicyListingDetailTypeDef",
    "SecretTypeDef",
    "ShareAttributesTypeDef",
    "SubmitJobRequestRequestTypeDef",
    "SubmitJobResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TaskContainerDependencyTypeDef",
    "TaskContainerDetailsTypeDef",
    "TaskContainerOverridesTypeDef",
    "TaskContainerPropertiesTypeDef",
    "TaskPropertiesOverrideTypeDef",
    "TerminateJobRequestRequestTypeDef",
    "TmpfsTypeDef",
    "UlimitTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateComputeEnvironmentRequestRequestTypeDef",
    "UpdateComputeEnvironmentResponseTypeDef",
    "UpdateJobQueueRequestRequestTypeDef",
    "UpdateJobQueueResponseTypeDef",
    "UpdatePolicyTypeDef",
    "UpdateSchedulingPolicyRequestRequestTypeDef",
    "VolumeTypeDef",
)

ArrayPropertiesDetailTypeDef = TypedDict(
    "ArrayPropertiesDetailTypeDef",
    {
        "statusSummary": Dict[str, int],
        "size": int,
        "index": int,
    },
    total=False,
)

ArrayPropertiesSummaryTypeDef = TypedDict(
    "ArrayPropertiesSummaryTypeDef",
    {
        "size": int,
        "index": int,
    },
    total=False,
)

ArrayPropertiesTypeDef = TypedDict(
    "ArrayPropertiesTypeDef",
    {
        "size": int,
    },
    total=False,
)

AttemptContainerDetailTypeDef = TypedDict(
    "AttemptContainerDetailTypeDef",
    {
        "containerInstanceArn": str,
        "taskArn": str,
        "exitCode": int,
        "reason": str,
        "logStreamName": str,
        "networkInterfaces": List["NetworkInterfaceTypeDef"],
    },
    total=False,
)

AttemptDetailTypeDef = TypedDict(
    "AttemptDetailTypeDef",
    {
        "container": "AttemptContainerDetailTypeDef",
        "startedAt": int,
        "stoppedAt": int,
        "statusReason": str,
        "taskProperties": List["AttemptEcsTaskDetailsTypeDef"],
    },
    total=False,
)

AttemptEcsTaskDetailsTypeDef = TypedDict(
    "AttemptEcsTaskDetailsTypeDef",
    {
        "containerInstanceArn": str,
        "taskArn": str,
        "containers": List["AttemptTaskContainerDetailsTypeDef"],
    },
    total=False,
)

AttemptTaskContainerDetailsTypeDef = TypedDict(
    "AttemptTaskContainerDetailsTypeDef",
    {
        "exitCode": int,
        "name": str,
        "reason": str,
        "logStreamName": str,
        "networkInterfaces": List["NetworkInterfaceTypeDef"],
    },
    total=False,
)

CancelJobRequestRequestTypeDef = TypedDict(
    "CancelJobRequestRequestTypeDef",
    {
        "jobId": str,
        "reason": str,
    },
)

_RequiredComputeEnvironmentDetailTypeDef = TypedDict(
    "_RequiredComputeEnvironmentDetailTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
    },
)
_OptionalComputeEnvironmentDetailTypeDef = TypedDict(
    "_OptionalComputeEnvironmentDetailTypeDef",
    {
        "unmanagedvCpus": int,
        "ecsClusterArn": str,
        "tags": Dict[str, str],
        "type": CETypeType,
        "state": CEStateType,
        "status": CEStatusType,
        "statusReason": str,
        "computeResources": "ComputeResourceTypeDef",
        "serviceRole": str,
        "updatePolicy": "UpdatePolicyTypeDef",
        "eksConfiguration": "EksConfigurationTypeDef",
        "containerOrchestrationType": OrchestrationTypeType,
        "uuid": str,
    },
    total=False,
)

class ComputeEnvironmentDetailTypeDef(
    _RequiredComputeEnvironmentDetailTypeDef, _OptionalComputeEnvironmentDetailTypeDef
):
    pass

ComputeEnvironmentOrderTypeDef = TypedDict(
    "ComputeEnvironmentOrderTypeDef",
    {
        "order": int,
        "computeEnvironment": str,
    },
)

_RequiredComputeResourceTypeDef = TypedDict(
    "_RequiredComputeResourceTypeDef",
    {
        "type": CRTypeType,
        "maxvCpus": int,
        "subnets": List[str],
    },
)
_OptionalComputeResourceTypeDef = TypedDict(
    "_OptionalComputeResourceTypeDef",
    {
        "allocationStrategy": CRAllocationStrategyType,
        "minvCpus": int,
        "desiredvCpus": int,
        "instanceTypes": List[str],
        "imageId": str,
        "securityGroupIds": List[str],
        "ec2KeyPair": str,
        "instanceRole": str,
        "tags": Dict[str, str],
        "placementGroup": str,
        "bidPercentage": int,
        "spotIamFleetRole": str,
        "launchTemplate": "LaunchTemplateSpecificationTypeDef",
        "ec2Configuration": List["Ec2ConfigurationTypeDef"],
    },
    total=False,
)

class ComputeResourceTypeDef(_RequiredComputeResourceTypeDef, _OptionalComputeResourceTypeDef):
    pass

ComputeResourceUpdateTypeDef = TypedDict(
    "ComputeResourceUpdateTypeDef",
    {
        "minvCpus": int,
        "maxvCpus": int,
        "desiredvCpus": int,
        "subnets": List[str],
        "securityGroupIds": List[str],
        "allocationStrategy": CRUpdateAllocationStrategyType,
        "instanceTypes": List[str],
        "ec2KeyPair": str,
        "instanceRole": str,
        "tags": Dict[str, str],
        "placementGroup": str,
        "bidPercentage": int,
        "launchTemplate": "LaunchTemplateSpecificationTypeDef",
        "ec2Configuration": List["Ec2ConfigurationTypeDef"],
        "updateToLatestImageVersion": bool,
        "type": CRTypeType,
        "imageId": str,
    },
    total=False,
)

ContainerDetailTypeDef = TypedDict(
    "ContainerDetailTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "executionRoleArn": str,
        "volumes": List["VolumeTypeDef"],
        "environment": List["KeyValuePairTypeDef"],
        "mountPoints": List["MountPointTypeDef"],
        "readonlyRootFilesystem": bool,
        "ulimits": List["UlimitTypeDef"],
        "privileged": bool,
        "user": str,
        "exitCode": int,
        "reason": str,
        "containerInstanceArn": str,
        "taskArn": str,
        "logStreamName": str,
        "instanceType": str,
        "networkInterfaces": List["NetworkInterfaceTypeDef"],
        "resourceRequirements": List["ResourceRequirementTypeDef"],
        "linuxParameters": "LinuxParametersTypeDef",
        "logConfiguration": "LogConfigurationTypeDef",
        "secrets": List["SecretTypeDef"],
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "fargatePlatformConfiguration": "FargatePlatformConfigurationTypeDef",
        "ephemeralStorage": "EphemeralStorageTypeDef",
        "runtimePlatform": "RuntimePlatformTypeDef",
        "repositoryCredentials": "RepositoryCredentialsTypeDef",
    },
    total=False,
)

ContainerOverridesTypeDef = TypedDict(
    "ContainerOverridesTypeDef",
    {
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "instanceType": str,
        "environment": List["KeyValuePairTypeDef"],
        "resourceRequirements": List["ResourceRequirementTypeDef"],
    },
    total=False,
)

ContainerPropertiesTypeDef = TypedDict(
    "ContainerPropertiesTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "executionRoleArn": str,
        "volumes": List["VolumeTypeDef"],
        "environment": List["KeyValuePairTypeDef"],
        "mountPoints": List["MountPointTypeDef"],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List["UlimitTypeDef"],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List["ResourceRequirementTypeDef"],
        "linuxParameters": "LinuxParametersTypeDef",
        "logConfiguration": "LogConfigurationTypeDef",
        "secrets": List["SecretTypeDef"],
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "fargatePlatformConfiguration": "FargatePlatformConfigurationTypeDef",
        "ephemeralStorage": "EphemeralStorageTypeDef",
        "runtimePlatform": "RuntimePlatformTypeDef",
        "repositoryCredentials": "RepositoryCredentialsTypeDef",
    },
    total=False,
)

ContainerSummaryTypeDef = TypedDict(
    "ContainerSummaryTypeDef",
    {
        "exitCode": int,
        "reason": str,
    },
    total=False,
)

_RequiredCreateComputeEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateComputeEnvironmentRequestRequestTypeDef",
    {
        "computeEnvironmentName": str,
        "type": CETypeType,
    },
)
_OptionalCreateComputeEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateComputeEnvironmentRequestRequestTypeDef",
    {
        "state": CEStateType,
        "unmanagedvCpus": int,
        "computeResources": "ComputeResourceTypeDef",
        "serviceRole": str,
        "tags": Dict[str, str],
        "eksConfiguration": "EksConfigurationTypeDef",
    },
    total=False,
)

class CreateComputeEnvironmentRequestRequestTypeDef(
    _RequiredCreateComputeEnvironmentRequestRequestTypeDef,
    _OptionalCreateComputeEnvironmentRequestRequestTypeDef,
):
    pass

CreateComputeEnvironmentResponseTypeDef = TypedDict(
    "CreateComputeEnvironmentResponseTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateJobQueueRequestRequestTypeDef = TypedDict(
    "_RequiredCreateJobQueueRequestRequestTypeDef",
    {
        "jobQueueName": str,
        "priority": int,
        "computeEnvironmentOrder": List["ComputeEnvironmentOrderTypeDef"],
    },
)
_OptionalCreateJobQueueRequestRequestTypeDef = TypedDict(
    "_OptionalCreateJobQueueRequestRequestTypeDef",
    {
        "state": JQStateType,
        "schedulingPolicyArn": str,
        "tags": Dict[str, str],
        "jobStateTimeLimitActions": List["JobStateTimeLimitActionTypeDef"],
    },
    total=False,
)

class CreateJobQueueRequestRequestTypeDef(
    _RequiredCreateJobQueueRequestRequestTypeDef, _OptionalCreateJobQueueRequestRequestTypeDef
):
    pass

CreateJobQueueResponseTypeDef = TypedDict(
    "CreateJobQueueResponseTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSchedulingPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSchedulingPolicyRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateSchedulingPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSchedulingPolicyRequestRequestTypeDef",
    {
        "fairsharePolicy": "FairsharePolicyTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateSchedulingPolicyRequestRequestTypeDef(
    _RequiredCreateSchedulingPolicyRequestRequestTypeDef,
    _OptionalCreateSchedulingPolicyRequestRequestTypeDef,
):
    pass

CreateSchedulingPolicyResponseTypeDef = TypedDict(
    "CreateSchedulingPolicyResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteComputeEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteComputeEnvironmentRequestRequestTypeDef",
    {
        "computeEnvironment": str,
    },
)

DeleteJobQueueRequestRequestTypeDef = TypedDict(
    "DeleteJobQueueRequestRequestTypeDef",
    {
        "jobQueue": str,
    },
)

DeleteSchedulingPolicyRequestRequestTypeDef = TypedDict(
    "DeleteSchedulingPolicyRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeregisterJobDefinitionRequestRequestTypeDef = TypedDict(
    "DeregisterJobDefinitionRequestRequestTypeDef",
    {
        "jobDefinition": str,
    },
)

DescribeComputeEnvironmentsRequestRequestTypeDef = TypedDict(
    "DescribeComputeEnvironmentsRequestRequestTypeDef",
    {
        "computeEnvironments": List[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeComputeEnvironmentsResponseTypeDef = TypedDict(
    "DescribeComputeEnvironmentsResponseTypeDef",
    {
        "computeEnvironments": List["ComputeEnvironmentDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobDefinitionsRequestRequestTypeDef = TypedDict(
    "DescribeJobDefinitionsRequestRequestTypeDef",
    {
        "jobDefinitions": List[str],
        "maxResults": int,
        "jobDefinitionName": str,
        "status": str,
        "nextToken": str,
    },
    total=False,
)

DescribeJobDefinitionsResponseTypeDef = TypedDict(
    "DescribeJobDefinitionsResponseTypeDef",
    {
        "jobDefinitions": List["JobDefinitionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobQueuesRequestRequestTypeDef = TypedDict(
    "DescribeJobQueuesRequestRequestTypeDef",
    {
        "jobQueues": List[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeJobQueuesResponseTypeDef = TypedDict(
    "DescribeJobQueuesResponseTypeDef",
    {
        "jobQueues": List["JobQueueDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobsRequestRequestTypeDef = TypedDict(
    "DescribeJobsRequestRequestTypeDef",
    {
        "jobs": List[str],
    },
)

DescribeJobsResponseTypeDef = TypedDict(
    "DescribeJobsResponseTypeDef",
    {
        "jobs": List["JobDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSchedulingPoliciesRequestRequestTypeDef = TypedDict(
    "DescribeSchedulingPoliciesRequestRequestTypeDef",
    {
        "arns": List[str],
    },
)

DescribeSchedulingPoliciesResponseTypeDef = TypedDict(
    "DescribeSchedulingPoliciesResponseTypeDef",
    {
        "schedulingPolicies": List["SchedulingPolicyDetailTypeDef"],
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

_RequiredEc2ConfigurationTypeDef = TypedDict(
    "_RequiredEc2ConfigurationTypeDef",
    {
        "imageType": str,
    },
)
_OptionalEc2ConfigurationTypeDef = TypedDict(
    "_OptionalEc2ConfigurationTypeDef",
    {
        "imageIdOverride": str,
        "imageKubernetesVersion": str,
    },
    total=False,
)

class Ec2ConfigurationTypeDef(_RequiredEc2ConfigurationTypeDef, _OptionalEc2ConfigurationTypeDef):
    pass

EcsPropertiesDetailTypeDef = TypedDict(
    "EcsPropertiesDetailTypeDef",
    {
        "taskProperties": List["EcsTaskDetailsTypeDef"],
    },
    total=False,
)

EcsPropertiesOverrideTypeDef = TypedDict(
    "EcsPropertiesOverrideTypeDef",
    {
        "taskProperties": List["TaskPropertiesOverrideTypeDef"],
    },
    total=False,
)

EcsPropertiesTypeDef = TypedDict(
    "EcsPropertiesTypeDef",
    {
        "taskProperties": List["EcsTaskPropertiesTypeDef"],
    },
)

EcsTaskDetailsTypeDef = TypedDict(
    "EcsTaskDetailsTypeDef",
    {
        "containers": List["TaskContainerDetailsTypeDef"],
        "containerInstanceArn": str,
        "taskArn": str,
        "ephemeralStorage": "EphemeralStorageTypeDef",
        "executionRoleArn": str,
        "platformVersion": str,
        "ipcMode": str,
        "taskRoleArn": str,
        "pidMode": str,
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "runtimePlatform": "RuntimePlatformTypeDef",
        "volumes": List["VolumeTypeDef"],
    },
    total=False,
)

_RequiredEcsTaskPropertiesTypeDef = TypedDict(
    "_RequiredEcsTaskPropertiesTypeDef",
    {
        "containers": List["TaskContainerPropertiesTypeDef"],
    },
)
_OptionalEcsTaskPropertiesTypeDef = TypedDict(
    "_OptionalEcsTaskPropertiesTypeDef",
    {
        "ephemeralStorage": "EphemeralStorageTypeDef",
        "executionRoleArn": str,
        "platformVersion": str,
        "ipcMode": str,
        "taskRoleArn": str,
        "pidMode": str,
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "runtimePlatform": "RuntimePlatformTypeDef",
        "volumes": List["VolumeTypeDef"],
    },
    total=False,
)

class EcsTaskPropertiesTypeDef(
    _RequiredEcsTaskPropertiesTypeDef, _OptionalEcsTaskPropertiesTypeDef
):
    pass

EksAttemptContainerDetailTypeDef = TypedDict(
    "EksAttemptContainerDetailTypeDef",
    {
        "name": str,
        "exitCode": int,
        "reason": str,
    },
    total=False,
)

EksAttemptDetailTypeDef = TypedDict(
    "EksAttemptDetailTypeDef",
    {
        "containers": List["EksAttemptContainerDetailTypeDef"],
        "initContainers": List["EksAttemptContainerDetailTypeDef"],
        "podName": str,
        "nodeName": str,
        "startedAt": int,
        "stoppedAt": int,
        "statusReason": str,
    },
    total=False,
)

EksConfigurationTypeDef = TypedDict(
    "EksConfigurationTypeDef",
    {
        "eksClusterArn": str,
        "kubernetesNamespace": str,
    },
)

EksContainerDetailTypeDef = TypedDict(
    "EksContainerDetailTypeDef",
    {
        "name": str,
        "image": str,
        "imagePullPolicy": str,
        "command": List[str],
        "args": List[str],
        "env": List["EksContainerEnvironmentVariableTypeDef"],
        "resources": "EksContainerResourceRequirementsTypeDef",
        "exitCode": int,
        "reason": str,
        "volumeMounts": List["EksContainerVolumeMountTypeDef"],
        "securityContext": "EksContainerSecurityContextTypeDef",
    },
    total=False,
)

_RequiredEksContainerEnvironmentVariableTypeDef = TypedDict(
    "_RequiredEksContainerEnvironmentVariableTypeDef",
    {
        "name": str,
    },
)
_OptionalEksContainerEnvironmentVariableTypeDef = TypedDict(
    "_OptionalEksContainerEnvironmentVariableTypeDef",
    {
        "value": str,
    },
    total=False,
)

class EksContainerEnvironmentVariableTypeDef(
    _RequiredEksContainerEnvironmentVariableTypeDef, _OptionalEksContainerEnvironmentVariableTypeDef
):
    pass

EksContainerOverrideTypeDef = TypedDict(
    "EksContainerOverrideTypeDef",
    {
        "name": str,
        "image": str,
        "command": List[str],
        "args": List[str],
        "env": List["EksContainerEnvironmentVariableTypeDef"],
        "resources": "EksContainerResourceRequirementsTypeDef",
    },
    total=False,
)

EksContainerResourceRequirementsTypeDef = TypedDict(
    "EksContainerResourceRequirementsTypeDef",
    {
        "limits": Dict[str, str],
        "requests": Dict[str, str],
    },
    total=False,
)

EksContainerSecurityContextTypeDef = TypedDict(
    "EksContainerSecurityContextTypeDef",
    {
        "runAsUser": int,
        "runAsGroup": int,
        "privileged": bool,
        "allowPrivilegeEscalation": bool,
        "readOnlyRootFilesystem": bool,
        "runAsNonRoot": bool,
    },
    total=False,
)

_RequiredEksContainerTypeDef = TypedDict(
    "_RequiredEksContainerTypeDef",
    {
        "image": str,
    },
)
_OptionalEksContainerTypeDef = TypedDict(
    "_OptionalEksContainerTypeDef",
    {
        "name": str,
        "imagePullPolicy": str,
        "command": List[str],
        "args": List[str],
        "env": List["EksContainerEnvironmentVariableTypeDef"],
        "resources": "EksContainerResourceRequirementsTypeDef",
        "volumeMounts": List["EksContainerVolumeMountTypeDef"],
        "securityContext": "EksContainerSecurityContextTypeDef",
    },
    total=False,
)

class EksContainerTypeDef(_RequiredEksContainerTypeDef, _OptionalEksContainerTypeDef):
    pass

EksContainerVolumeMountTypeDef = TypedDict(
    "EksContainerVolumeMountTypeDef",
    {
        "name": str,
        "mountPath": str,
        "readOnly": bool,
    },
    total=False,
)

EksEmptyDirTypeDef = TypedDict(
    "EksEmptyDirTypeDef",
    {
        "medium": str,
        "sizeLimit": str,
    },
    total=False,
)

EksHostPathTypeDef = TypedDict(
    "EksHostPathTypeDef",
    {
        "path": str,
    },
    total=False,
)

EksMetadataTypeDef = TypedDict(
    "EksMetadataTypeDef",
    {
        "labels": Dict[str, str],
    },
    total=False,
)

EksPodPropertiesDetailTypeDef = TypedDict(
    "EksPodPropertiesDetailTypeDef",
    {
        "serviceAccountName": str,
        "hostNetwork": bool,
        "dnsPolicy": str,
        "imagePullSecrets": List["ImagePullSecretTypeDef"],
        "containers": List["EksContainerDetailTypeDef"],
        "initContainers": List["EksContainerDetailTypeDef"],
        "volumes": List["EksVolumeTypeDef"],
        "podName": str,
        "nodeName": str,
        "metadata": "EksMetadataTypeDef",
        "shareProcessNamespace": bool,
    },
    total=False,
)

EksPodPropertiesOverrideTypeDef = TypedDict(
    "EksPodPropertiesOverrideTypeDef",
    {
        "containers": List["EksContainerOverrideTypeDef"],
        "initContainers": List["EksContainerOverrideTypeDef"],
        "metadata": "EksMetadataTypeDef",
    },
    total=False,
)

EksPodPropertiesTypeDef = TypedDict(
    "EksPodPropertiesTypeDef",
    {
        "serviceAccountName": str,
        "hostNetwork": bool,
        "dnsPolicy": str,
        "imagePullSecrets": List["ImagePullSecretTypeDef"],
        "containers": List["EksContainerTypeDef"],
        "initContainers": List["EksContainerTypeDef"],
        "volumes": List["EksVolumeTypeDef"],
        "metadata": "EksMetadataTypeDef",
        "shareProcessNamespace": bool,
    },
    total=False,
)

EksPropertiesDetailTypeDef = TypedDict(
    "EksPropertiesDetailTypeDef",
    {
        "podProperties": "EksPodPropertiesDetailTypeDef",
    },
    total=False,
)

EksPropertiesOverrideTypeDef = TypedDict(
    "EksPropertiesOverrideTypeDef",
    {
        "podProperties": "EksPodPropertiesOverrideTypeDef",
    },
    total=False,
)

EksPropertiesTypeDef = TypedDict(
    "EksPropertiesTypeDef",
    {
        "podProperties": "EksPodPropertiesTypeDef",
    },
    total=False,
)

_RequiredEksSecretTypeDef = TypedDict(
    "_RequiredEksSecretTypeDef",
    {
        "secretName": str,
    },
)
_OptionalEksSecretTypeDef = TypedDict(
    "_OptionalEksSecretTypeDef",
    {
        "optional": bool,
    },
    total=False,
)

class EksSecretTypeDef(_RequiredEksSecretTypeDef, _OptionalEksSecretTypeDef):
    pass

_RequiredEksVolumeTypeDef = TypedDict(
    "_RequiredEksVolumeTypeDef",
    {
        "name": str,
    },
)
_OptionalEksVolumeTypeDef = TypedDict(
    "_OptionalEksVolumeTypeDef",
    {
        "hostPath": "EksHostPathTypeDef",
        "emptyDir": "EksEmptyDirTypeDef",
        "secret": "EksSecretTypeDef",
    },
    total=False,
)

class EksVolumeTypeDef(_RequiredEksVolumeTypeDef, _OptionalEksVolumeTypeDef):
    pass

EphemeralStorageTypeDef = TypedDict(
    "EphemeralStorageTypeDef",
    {
        "sizeInGiB": int,
    },
)

_RequiredEvaluateOnExitTypeDef = TypedDict(
    "_RequiredEvaluateOnExitTypeDef",
    {
        "action": RetryActionType,
    },
)
_OptionalEvaluateOnExitTypeDef = TypedDict(
    "_OptionalEvaluateOnExitTypeDef",
    {
        "onStatusReason": str,
        "onReason": str,
        "onExitCode": str,
    },
    total=False,
)

class EvaluateOnExitTypeDef(_RequiredEvaluateOnExitTypeDef, _OptionalEvaluateOnExitTypeDef):
    pass

FairsharePolicyTypeDef = TypedDict(
    "FairsharePolicyTypeDef",
    {
        "shareDecaySeconds": int,
        "computeReservation": int,
        "shareDistribution": List["ShareAttributesTypeDef"],
    },
    total=False,
)

FargatePlatformConfigurationTypeDef = TypedDict(
    "FargatePlatformConfigurationTypeDef",
    {
        "platformVersion": str,
    },
    total=False,
)

FrontOfQueueDetailTypeDef = TypedDict(
    "FrontOfQueueDetailTypeDef",
    {
        "jobs": List["FrontOfQueueJobSummaryTypeDef"],
        "lastUpdatedAt": int,
    },
    total=False,
)

FrontOfQueueJobSummaryTypeDef = TypedDict(
    "FrontOfQueueJobSummaryTypeDef",
    {
        "jobArn": str,
        "earliestTimeAtPosition": int,
    },
    total=False,
)

GetJobQueueSnapshotRequestRequestTypeDef = TypedDict(
    "GetJobQueueSnapshotRequestRequestTypeDef",
    {
        "jobQueue": str,
    },
)

GetJobQueueSnapshotResponseTypeDef = TypedDict(
    "GetJobQueueSnapshotResponseTypeDef",
    {
        "frontOfQueue": "FrontOfQueueDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HostTypeDef = TypedDict(
    "HostTypeDef",
    {
        "sourcePath": str,
    },
    total=False,
)

ImagePullSecretTypeDef = TypedDict(
    "ImagePullSecretTypeDef",
    {
        "name": str,
    },
)

_RequiredJobDefinitionTypeDef = TypedDict(
    "_RequiredJobDefinitionTypeDef",
    {
        "jobDefinitionName": str,
        "jobDefinitionArn": str,
        "revision": int,
        "type": str,
    },
)
_OptionalJobDefinitionTypeDef = TypedDict(
    "_OptionalJobDefinitionTypeDef",
    {
        "status": str,
        "schedulingPriority": int,
        "parameters": Dict[str, str],
        "retryStrategy": "RetryStrategyTypeDef",
        "containerProperties": "ContainerPropertiesTypeDef",
        "timeout": "JobTimeoutTypeDef",
        "nodeProperties": "NodePropertiesTypeDef",
        "tags": Dict[str, str],
        "propagateTags": bool,
        "platformCapabilities": List[PlatformCapabilityType],
        "ecsProperties": "EcsPropertiesTypeDef",
        "eksProperties": "EksPropertiesTypeDef",
        "containerOrchestrationType": OrchestrationTypeType,
    },
    total=False,
)

class JobDefinitionTypeDef(_RequiredJobDefinitionTypeDef, _OptionalJobDefinitionTypeDef):
    pass

JobDependencyTypeDef = TypedDict(
    "JobDependencyTypeDef",
    {
        "jobId": str,
        "type": ArrayJobDependencyType,
    },
    total=False,
)

_RequiredJobDetailTypeDef = TypedDict(
    "_RequiredJobDetailTypeDef",
    {
        "jobName": str,
        "jobId": str,
        "jobQueue": str,
        "status": JobStatusType,
        "startedAt": int,
        "jobDefinition": str,
    },
)
_OptionalJobDetailTypeDef = TypedDict(
    "_OptionalJobDetailTypeDef",
    {
        "jobArn": str,
        "shareIdentifier": str,
        "schedulingPriority": int,
        "attempts": List["AttemptDetailTypeDef"],
        "statusReason": str,
        "createdAt": int,
        "retryStrategy": "RetryStrategyTypeDef",
        "stoppedAt": int,
        "dependsOn": List["JobDependencyTypeDef"],
        "parameters": Dict[str, str],
        "container": "ContainerDetailTypeDef",
        "nodeDetails": "NodeDetailsTypeDef",
        "nodeProperties": "NodePropertiesTypeDef",
        "arrayProperties": "ArrayPropertiesDetailTypeDef",
        "timeout": "JobTimeoutTypeDef",
        "tags": Dict[str, str],
        "propagateTags": bool,
        "platformCapabilities": List[PlatformCapabilityType],
        "eksProperties": "EksPropertiesDetailTypeDef",
        "eksAttempts": List["EksAttemptDetailTypeDef"],
        "ecsProperties": "EcsPropertiesDetailTypeDef",
        "isCancelled": bool,
        "isTerminated": bool,
    },
    total=False,
)

class JobDetailTypeDef(_RequiredJobDetailTypeDef, _OptionalJobDetailTypeDef):
    pass

_RequiredJobQueueDetailTypeDef = TypedDict(
    "_RequiredJobQueueDetailTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "state": JQStateType,
        "priority": int,
        "computeEnvironmentOrder": List["ComputeEnvironmentOrderTypeDef"],
    },
)
_OptionalJobQueueDetailTypeDef = TypedDict(
    "_OptionalJobQueueDetailTypeDef",
    {
        "schedulingPolicyArn": str,
        "status": JQStatusType,
        "statusReason": str,
        "tags": Dict[str, str],
        "jobStateTimeLimitActions": List["JobStateTimeLimitActionTypeDef"],
    },
    total=False,
)

class JobQueueDetailTypeDef(_RequiredJobQueueDetailTypeDef, _OptionalJobQueueDetailTypeDef):
    pass

JobStateTimeLimitActionTypeDef = TypedDict(
    "JobStateTimeLimitActionTypeDef",
    {
        "reason": str,
        "state": Literal["RUNNABLE"],
        "maxTimeSeconds": int,
        "action": Literal["CANCEL"],
    },
)

_RequiredJobSummaryTypeDef = TypedDict(
    "_RequiredJobSummaryTypeDef",
    {
        "jobId": str,
        "jobName": str,
    },
)
_OptionalJobSummaryTypeDef = TypedDict(
    "_OptionalJobSummaryTypeDef",
    {
        "jobArn": str,
        "createdAt": int,
        "status": JobStatusType,
        "statusReason": str,
        "startedAt": int,
        "stoppedAt": int,
        "container": "ContainerSummaryTypeDef",
        "arrayProperties": "ArrayPropertiesSummaryTypeDef",
        "nodeProperties": "NodePropertiesSummaryTypeDef",
        "jobDefinition": str,
    },
    total=False,
)

class JobSummaryTypeDef(_RequiredJobSummaryTypeDef, _OptionalJobSummaryTypeDef):
    pass

JobTimeoutTypeDef = TypedDict(
    "JobTimeoutTypeDef",
    {
        "attemptDurationSeconds": int,
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

KeyValuesPairTypeDef = TypedDict(
    "KeyValuesPairTypeDef",
    {
        "name": str,
        "values": List[str],
    },
    total=False,
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "launchTemplateId": str,
        "launchTemplateName": str,
        "version": str,
    },
    total=False,
)

LinuxParametersTypeDef = TypedDict(
    "LinuxParametersTypeDef",
    {
        "devices": List["DeviceTypeDef"],
        "initProcessEnabled": bool,
        "sharedMemorySize": int,
        "tmpfs": List["TmpfsTypeDef"],
        "maxSwap": int,
        "swappiness": int,
    },
    total=False,
)

ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "jobQueue": str,
        "arrayJobId": str,
        "multiNodeJobId": str,
        "jobStatus": JobStatusType,
        "maxResults": int,
        "nextToken": str,
        "filters": List["KeyValuesPairTypeDef"],
    },
    total=False,
)

ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef",
    {
        "jobSummaryList": List["JobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSchedulingPoliciesRequestRequestTypeDef = TypedDict(
    "ListSchedulingPoliciesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSchedulingPoliciesResponseTypeDef = TypedDict(
    "ListSchedulingPoliciesResponseTypeDef",
    {
        "schedulingPolicies": List["SchedulingPolicyListingDetailTypeDef"],
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
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

MountPointTypeDef = TypedDict(
    "MountPointTypeDef",
    {
        "containerPath": str,
        "readOnly": bool,
        "sourceVolume": str,
    },
    total=False,
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "assignPublicIp": AssignPublicIpType,
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "attachmentId": str,
        "ipv6Address": str,
        "privateIpv4Address": str,
    },
    total=False,
)

NodeDetailsTypeDef = TypedDict(
    "NodeDetailsTypeDef",
    {
        "nodeIndex": int,
        "isMainNode": bool,
    },
    total=False,
)

NodeOverridesTypeDef = TypedDict(
    "NodeOverridesTypeDef",
    {
        "numNodes": int,
        "nodePropertyOverrides": List["NodePropertyOverrideTypeDef"],
    },
    total=False,
)

NodePropertiesSummaryTypeDef = TypedDict(
    "NodePropertiesSummaryTypeDef",
    {
        "isMainNode": bool,
        "numNodes": int,
        "nodeIndex": int,
    },
    total=False,
)

NodePropertiesTypeDef = TypedDict(
    "NodePropertiesTypeDef",
    {
        "numNodes": int,
        "mainNode": int,
        "nodeRangeProperties": List["NodeRangePropertyTypeDef"],
    },
)

_RequiredNodePropertyOverrideTypeDef = TypedDict(
    "_RequiredNodePropertyOverrideTypeDef",
    {
        "targetNodes": str,
    },
)
_OptionalNodePropertyOverrideTypeDef = TypedDict(
    "_OptionalNodePropertyOverrideTypeDef",
    {
        "containerOverrides": "ContainerOverridesTypeDef",
        "ecsPropertiesOverride": "EcsPropertiesOverrideTypeDef",
        "instanceTypes": List[str],
    },
    total=False,
)

class NodePropertyOverrideTypeDef(
    _RequiredNodePropertyOverrideTypeDef, _OptionalNodePropertyOverrideTypeDef
):
    pass

_RequiredNodeRangePropertyTypeDef = TypedDict(
    "_RequiredNodeRangePropertyTypeDef",
    {
        "targetNodes": str,
    },
)
_OptionalNodeRangePropertyTypeDef = TypedDict(
    "_OptionalNodeRangePropertyTypeDef",
    {
        "container": "ContainerPropertiesTypeDef",
        "instanceTypes": List[str],
        "ecsProperties": "EcsPropertiesTypeDef",
    },
    total=False,
)

class NodeRangePropertyTypeDef(
    _RequiredNodeRangePropertyTypeDef, _OptionalNodeRangePropertyTypeDef
):
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

_RequiredRegisterJobDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterJobDefinitionRequestRequestTypeDef",
    {
        "jobDefinitionName": str,
        "type": JobDefinitionTypeType,
    },
)
_OptionalRegisterJobDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterJobDefinitionRequestRequestTypeDef",
    {
        "parameters": Dict[str, str],
        "schedulingPriority": int,
        "containerProperties": "ContainerPropertiesTypeDef",
        "nodeProperties": "NodePropertiesTypeDef",
        "retryStrategy": "RetryStrategyTypeDef",
        "propagateTags": bool,
        "timeout": "JobTimeoutTypeDef",
        "tags": Dict[str, str],
        "platformCapabilities": List[PlatformCapabilityType],
        "eksProperties": "EksPropertiesTypeDef",
        "ecsProperties": "EcsPropertiesTypeDef",
    },
    total=False,
)

class RegisterJobDefinitionRequestRequestTypeDef(
    _RequiredRegisterJobDefinitionRequestRequestTypeDef,
    _OptionalRegisterJobDefinitionRequestRequestTypeDef,
):
    pass

RegisterJobDefinitionResponseTypeDef = TypedDict(
    "RegisterJobDefinitionResponseTypeDef",
    {
        "jobDefinitionName": str,
        "jobDefinitionArn": str,
        "revision": int,
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

RetryStrategyTypeDef = TypedDict(
    "RetryStrategyTypeDef",
    {
        "attempts": int,
        "evaluateOnExit": List["EvaluateOnExitTypeDef"],
    },
    total=False,
)

RuntimePlatformTypeDef = TypedDict(
    "RuntimePlatformTypeDef",
    {
        "operatingSystemFamily": str,
        "cpuArchitecture": str,
    },
    total=False,
)

_RequiredSchedulingPolicyDetailTypeDef = TypedDict(
    "_RequiredSchedulingPolicyDetailTypeDef",
    {
        "name": str,
        "arn": str,
    },
)
_OptionalSchedulingPolicyDetailTypeDef = TypedDict(
    "_OptionalSchedulingPolicyDetailTypeDef",
    {
        "fairsharePolicy": "FairsharePolicyTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class SchedulingPolicyDetailTypeDef(
    _RequiredSchedulingPolicyDetailTypeDef, _OptionalSchedulingPolicyDetailTypeDef
):
    pass

SchedulingPolicyListingDetailTypeDef = TypedDict(
    "SchedulingPolicyListingDetailTypeDef",
    {
        "arn": str,
    },
)

SecretTypeDef = TypedDict(
    "SecretTypeDef",
    {
        "name": str,
        "valueFrom": str,
    },
)

_RequiredShareAttributesTypeDef = TypedDict(
    "_RequiredShareAttributesTypeDef",
    {
        "shareIdentifier": str,
    },
)
_OptionalShareAttributesTypeDef = TypedDict(
    "_OptionalShareAttributesTypeDef",
    {
        "weightFactor": float,
    },
    total=False,
)

class ShareAttributesTypeDef(_RequiredShareAttributesTypeDef, _OptionalShareAttributesTypeDef):
    pass

_RequiredSubmitJobRequestRequestTypeDef = TypedDict(
    "_RequiredSubmitJobRequestRequestTypeDef",
    {
        "jobName": str,
        "jobQueue": str,
        "jobDefinition": str,
    },
)
_OptionalSubmitJobRequestRequestTypeDef = TypedDict(
    "_OptionalSubmitJobRequestRequestTypeDef",
    {
        "shareIdentifier": str,
        "schedulingPriorityOverride": int,
        "arrayProperties": "ArrayPropertiesTypeDef",
        "dependsOn": List["JobDependencyTypeDef"],
        "parameters": Dict[str, str],
        "containerOverrides": "ContainerOverridesTypeDef",
        "nodeOverrides": "NodeOverridesTypeDef",
        "retryStrategy": "RetryStrategyTypeDef",
        "propagateTags": bool,
        "timeout": "JobTimeoutTypeDef",
        "tags": Dict[str, str],
        "eksPropertiesOverride": "EksPropertiesOverrideTypeDef",
        "ecsPropertiesOverride": "EcsPropertiesOverrideTypeDef",
    },
    total=False,
)

class SubmitJobRequestRequestTypeDef(
    _RequiredSubmitJobRequestRequestTypeDef, _OptionalSubmitJobRequestRequestTypeDef
):
    pass

SubmitJobResponseTypeDef = TypedDict(
    "SubmitJobResponseTypeDef",
    {
        "jobArn": str,
        "jobName": str,
        "jobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TaskContainerDependencyTypeDef = TypedDict(
    "TaskContainerDependencyTypeDef",
    {
        "containerName": str,
        "condition": str,
    },
    total=False,
)

TaskContainerDetailsTypeDef = TypedDict(
    "TaskContainerDetailsTypeDef",
    {
        "command": List[str],
        "dependsOn": List["TaskContainerDependencyTypeDef"],
        "environment": List["KeyValuePairTypeDef"],
        "essential": bool,
        "image": str,
        "linuxParameters": "LinuxParametersTypeDef",
        "logConfiguration": "LogConfigurationTypeDef",
        "mountPoints": List["MountPointTypeDef"],
        "name": str,
        "privileged": bool,
        "readonlyRootFilesystem": bool,
        "repositoryCredentials": "RepositoryCredentialsTypeDef",
        "resourceRequirements": List["ResourceRequirementTypeDef"],
        "secrets": List["SecretTypeDef"],
        "ulimits": List["UlimitTypeDef"],
        "user": str,
        "exitCode": int,
        "reason": str,
        "logStreamName": str,
        "networkInterfaces": List["NetworkInterfaceTypeDef"],
    },
    total=False,
)

TaskContainerOverridesTypeDef = TypedDict(
    "TaskContainerOverridesTypeDef",
    {
        "command": List[str],
        "environment": List["KeyValuePairTypeDef"],
        "name": str,
        "resourceRequirements": List["ResourceRequirementTypeDef"],
    },
    total=False,
)

_RequiredTaskContainerPropertiesTypeDef = TypedDict(
    "_RequiredTaskContainerPropertiesTypeDef",
    {
        "image": str,
    },
)
_OptionalTaskContainerPropertiesTypeDef = TypedDict(
    "_OptionalTaskContainerPropertiesTypeDef",
    {
        "command": List[str],
        "dependsOn": List["TaskContainerDependencyTypeDef"],
        "environment": List["KeyValuePairTypeDef"],
        "essential": bool,
        "linuxParameters": "LinuxParametersTypeDef",
        "logConfiguration": "LogConfigurationTypeDef",
        "mountPoints": List["MountPointTypeDef"],
        "name": str,
        "privileged": bool,
        "readonlyRootFilesystem": bool,
        "repositoryCredentials": "RepositoryCredentialsTypeDef",
        "resourceRequirements": List["ResourceRequirementTypeDef"],
        "secrets": List["SecretTypeDef"],
        "ulimits": List["UlimitTypeDef"],
        "user": str,
    },
    total=False,
)

class TaskContainerPropertiesTypeDef(
    _RequiredTaskContainerPropertiesTypeDef, _OptionalTaskContainerPropertiesTypeDef
):
    pass

TaskPropertiesOverrideTypeDef = TypedDict(
    "TaskPropertiesOverrideTypeDef",
    {
        "containers": List["TaskContainerOverridesTypeDef"],
    },
    total=False,
)

TerminateJobRequestRequestTypeDef = TypedDict(
    "TerminateJobRequestRequestTypeDef",
    {
        "jobId": str,
        "reason": str,
    },
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
        "hardLimit": int,
        "name": str,
        "softLimit": int,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateComputeEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateComputeEnvironmentRequestRequestTypeDef",
    {
        "computeEnvironment": str,
    },
)
_OptionalUpdateComputeEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateComputeEnvironmentRequestRequestTypeDef",
    {
        "state": CEStateType,
        "unmanagedvCpus": int,
        "computeResources": "ComputeResourceUpdateTypeDef",
        "serviceRole": str,
        "updatePolicy": "UpdatePolicyTypeDef",
    },
    total=False,
)

class UpdateComputeEnvironmentRequestRequestTypeDef(
    _RequiredUpdateComputeEnvironmentRequestRequestTypeDef,
    _OptionalUpdateComputeEnvironmentRequestRequestTypeDef,
):
    pass

UpdateComputeEnvironmentResponseTypeDef = TypedDict(
    "UpdateComputeEnvironmentResponseTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateJobQueueRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateJobQueueRequestRequestTypeDef",
    {
        "jobQueue": str,
    },
)
_OptionalUpdateJobQueueRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateJobQueueRequestRequestTypeDef",
    {
        "state": JQStateType,
        "schedulingPolicyArn": str,
        "priority": int,
        "computeEnvironmentOrder": List["ComputeEnvironmentOrderTypeDef"],
        "jobStateTimeLimitActions": List["JobStateTimeLimitActionTypeDef"],
    },
    total=False,
)

class UpdateJobQueueRequestRequestTypeDef(
    _RequiredUpdateJobQueueRequestRequestTypeDef, _OptionalUpdateJobQueueRequestRequestTypeDef
):
    pass

UpdateJobQueueResponseTypeDef = TypedDict(
    "UpdateJobQueueResponseTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePolicyTypeDef = TypedDict(
    "UpdatePolicyTypeDef",
    {
        "terminateJobsOnUpdate": bool,
        "jobExecutionTimeoutMinutes": int,
    },
    total=False,
)

_RequiredUpdateSchedulingPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSchedulingPolicyRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateSchedulingPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSchedulingPolicyRequestRequestTypeDef",
    {
        "fairsharePolicy": "FairsharePolicyTypeDef",
    },
    total=False,
)

class UpdateSchedulingPolicyRequestRequestTypeDef(
    _RequiredUpdateSchedulingPolicyRequestRequestTypeDef,
    _OptionalUpdateSchedulingPolicyRequestRequestTypeDef,
):
    pass

VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "host": "HostTypeDef",
        "name": str,
        "efsVolumeConfiguration": "EFSVolumeConfigurationTypeDef",
    },
    total=False,
)
