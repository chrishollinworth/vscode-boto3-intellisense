"""
Main interface for batch service type definitions.

Usage::

    ```python
    from mypy_boto3_batch.type_defs import ArrayPropertiesDetailTypeDef

    data: ArrayPropertiesDetailTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

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
    "AttemptContainerDetailTypeDef",
    "AttemptDetailTypeDef",
    "ComputeEnvironmentDetailTypeDef",
    "ComputeEnvironmentOrderTypeDef",
    "ComputeResourceTypeDef",
    "ContainerDetailTypeDef",
    "ContainerOverridesTypeDef",
    "ContainerPropertiesTypeDef",
    "ContainerSummaryTypeDef",
    "DeviceTypeDef",
    "Ec2ConfigurationTypeDef",
    "EvaluateOnExitTypeDef",
    "FargatePlatformConfigurationTypeDef",
    "HostTypeDef",
    "JobDefinitionTypeDef",
    "JobDependencyTypeDef",
    "JobDetailTypeDef",
    "JobQueueDetailTypeDef",
    "JobSummaryTypeDef",
    "JobTimeoutTypeDef",
    "KeyValuePairTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "LinuxParametersTypeDef",
    "LogConfigurationTypeDef",
    "MountPointTypeDef",
    "NetworkConfigurationTypeDef",
    "NetworkInterfaceTypeDef",
    "NodeDetailsTypeDef",
    "NodePropertiesSummaryTypeDef",
    "NodePropertiesTypeDef",
    "NodePropertyOverrideTypeDef",
    "NodeRangePropertyTypeDef",
    "ResourceRequirementTypeDef",
    "RetryStrategyTypeDef",
    "SecretTypeDef",
    "TmpfsTypeDef",
    "UlimitTypeDef",
    "VolumeTypeDef",
    "ArrayPropertiesTypeDef",
    "ComputeResourceUpdateTypeDef",
    "CreateComputeEnvironmentResponseTypeDef",
    "CreateJobQueueResponseTypeDef",
    "DescribeComputeEnvironmentsResponseTypeDef",
    "DescribeJobDefinitionsResponseTypeDef",
    "DescribeJobQueuesResponseTypeDef",
    "DescribeJobsResponseTypeDef",
    "ListJobsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NodeOverridesTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterJobDefinitionResponseTypeDef",
    "SubmitJobResponseTypeDef",
    "UpdateComputeEnvironmentResponseTypeDef",
    "UpdateJobQueueResponseTypeDef",
)

ArrayPropertiesDetailTypeDef = TypedDict(
    "ArrayPropertiesDetailTypeDef",
    {"statusSummary": Dict[str, int], "size": int, "index": int},
    total=False,
)

ArrayPropertiesSummaryTypeDef = TypedDict(
    "ArrayPropertiesSummaryTypeDef", {"size": int, "index": int}, total=False
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
    },
    total=False,
)

_RequiredComputeEnvironmentDetailTypeDef = TypedDict(
    "_RequiredComputeEnvironmentDetailTypeDef",
    {"computeEnvironmentName": str, "computeEnvironmentArn": str, "ecsClusterArn": str},
)
_OptionalComputeEnvironmentDetailTypeDef = TypedDict(
    "_OptionalComputeEnvironmentDetailTypeDef",
    {
        "tags": Dict[str, str],
        "type": Literal["MANAGED", "UNMANAGED"],
        "state": Literal["ENABLED", "DISABLED"],
        "status": Literal["CREATING", "UPDATING", "DELETING", "DELETED", "VALID", "INVALID"],
        "statusReason": str,
        "computeResources": "ComputeResourceTypeDef",
        "serviceRole": str,
    },
    total=False,
)


class ComputeEnvironmentDetailTypeDef(
    _RequiredComputeEnvironmentDetailTypeDef, _OptionalComputeEnvironmentDetailTypeDef
):
    pass


ComputeEnvironmentOrderTypeDef = TypedDict(
    "ComputeEnvironmentOrderTypeDef", {"order": int, "computeEnvironment": str}
)

_RequiredComputeResourceTypeDef = TypedDict(
    "_RequiredComputeResourceTypeDef",
    {
        "type": Literal["EC2", "SPOT", "FARGATE", "FARGATE_SPOT"],
        "maxvCpus": int,
        "subnets": List[str],
    },
)
_OptionalComputeResourceTypeDef = TypedDict(
    "_OptionalComputeResourceTypeDef",
    {
        "allocationStrategy": Literal[
            "BEST_FIT", "BEST_FIT_PROGRESSIVE", "SPOT_CAPACITY_OPTIMIZED"
        ],
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
    },
    total=False,
)

ContainerSummaryTypeDef = TypedDict(
    "ContainerSummaryTypeDef", {"exitCode": int, "reason": str}, total=False
)

_RequiredDeviceTypeDef = TypedDict("_RequiredDeviceTypeDef", {"hostPath": str})
_OptionalDeviceTypeDef = TypedDict(
    "_OptionalDeviceTypeDef",
    {"containerPath": str, "permissions": List[Literal["READ", "WRITE", "MKNOD"]]},
    total=False,
)


class DeviceTypeDef(_RequiredDeviceTypeDef, _OptionalDeviceTypeDef):
    pass


_RequiredEc2ConfigurationTypeDef = TypedDict("_RequiredEc2ConfigurationTypeDef", {"imageType": str})
_OptionalEc2ConfigurationTypeDef = TypedDict(
    "_OptionalEc2ConfigurationTypeDef", {"imageIdOverride": str}, total=False
)


class Ec2ConfigurationTypeDef(_RequiredEc2ConfigurationTypeDef, _OptionalEc2ConfigurationTypeDef):
    pass


_RequiredEvaluateOnExitTypeDef = TypedDict(
    "_RequiredEvaluateOnExitTypeDef", {"action": Literal["RETRY", "EXIT"]}
)
_OptionalEvaluateOnExitTypeDef = TypedDict(
    "_OptionalEvaluateOnExitTypeDef",
    {"onStatusReason": str, "onReason": str, "onExitCode": str},
    total=False,
)


class EvaluateOnExitTypeDef(_RequiredEvaluateOnExitTypeDef, _OptionalEvaluateOnExitTypeDef):
    pass


FargatePlatformConfigurationTypeDef = TypedDict(
    "FargatePlatformConfigurationTypeDef", {"platformVersion": str}, total=False
)

HostTypeDef = TypedDict("HostTypeDef", {"sourcePath": str}, total=False)

_RequiredJobDefinitionTypeDef = TypedDict(
    "_RequiredJobDefinitionTypeDef",
    {"jobDefinitionName": str, "jobDefinitionArn": str, "revision": int, "type": str},
)
_OptionalJobDefinitionTypeDef = TypedDict(
    "_OptionalJobDefinitionTypeDef",
    {
        "status": str,
        "parameters": Dict[str, str],
        "retryStrategy": "RetryStrategyTypeDef",
        "containerProperties": "ContainerPropertiesTypeDef",
        "timeout": "JobTimeoutTypeDef",
        "nodeProperties": "NodePropertiesTypeDef",
        "tags": Dict[str, str],
        "propagateTags": bool,
        "platformCapabilities": List[Literal["EC2", "FARGATE"]],
    },
    total=False,
)


class JobDefinitionTypeDef(_RequiredJobDefinitionTypeDef, _OptionalJobDefinitionTypeDef):
    pass


JobDependencyTypeDef = TypedDict(
    "JobDependencyTypeDef", {"jobId": str, "type": Literal["N_TO_N", "SEQUENTIAL"]}, total=False
)

_RequiredJobDetailTypeDef = TypedDict(
    "_RequiredJobDetailTypeDef",
    {
        "jobName": str,
        "jobId": str,
        "jobQueue": str,
        "status": Literal[
            "SUBMITTED", "PENDING", "RUNNABLE", "STARTING", "RUNNING", "SUCCEEDED", "FAILED"
        ],
        "startedAt": int,
        "jobDefinition": str,
    },
)
_OptionalJobDetailTypeDef = TypedDict(
    "_OptionalJobDetailTypeDef",
    {
        "jobArn": str,
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
        "platformCapabilities": List[Literal["EC2", "FARGATE"]],
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
        "state": Literal["ENABLED", "DISABLED"],
        "priority": int,
        "computeEnvironmentOrder": List["ComputeEnvironmentOrderTypeDef"],
    },
)
_OptionalJobQueueDetailTypeDef = TypedDict(
    "_OptionalJobQueueDetailTypeDef",
    {
        "status": Literal["CREATING", "UPDATING", "DELETING", "DELETED", "VALID", "INVALID"],
        "statusReason": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class JobQueueDetailTypeDef(_RequiredJobQueueDetailTypeDef, _OptionalJobQueueDetailTypeDef):
    pass


_RequiredJobSummaryTypeDef = TypedDict("_RequiredJobSummaryTypeDef", {"jobId": str, "jobName": str})
_OptionalJobSummaryTypeDef = TypedDict(
    "_OptionalJobSummaryTypeDef",
    {
        "jobArn": str,
        "createdAt": int,
        "status": Literal[
            "SUBMITTED", "PENDING", "RUNNABLE", "STARTING", "RUNNING", "SUCCEEDED", "FAILED"
        ],
        "statusReason": str,
        "startedAt": int,
        "stoppedAt": int,
        "container": "ContainerSummaryTypeDef",
        "arrayProperties": "ArrayPropertiesSummaryTypeDef",
        "nodeProperties": "NodePropertiesSummaryTypeDef",
    },
    total=False,
)


class JobSummaryTypeDef(_RequiredJobSummaryTypeDef, _OptionalJobSummaryTypeDef):
    pass


JobTimeoutTypeDef = TypedDict("JobTimeoutTypeDef", {"attemptDurationSeconds": int}, total=False)

KeyValuePairTypeDef = TypedDict("KeyValuePairTypeDef", {"name": str, "value": str}, total=False)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {"launchTemplateId": str, "launchTemplateName": str, "version": str},
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

_RequiredLogConfigurationTypeDef = TypedDict(
    "_RequiredLogConfigurationTypeDef",
    {
        "logDriver": Literal[
            "json-file", "syslog", "journald", "gelf", "fluentd", "awslogs", "splunk"
        ]
    },
)
_OptionalLogConfigurationTypeDef = TypedDict(
    "_OptionalLogConfigurationTypeDef",
    {"options": Dict[str, str], "secretOptions": List["SecretTypeDef"]},
    total=False,
)


class LogConfigurationTypeDef(_RequiredLogConfigurationTypeDef, _OptionalLogConfigurationTypeDef):
    pass


MountPointTypeDef = TypedDict(
    "MountPointTypeDef", {"containerPath": str, "readOnly": bool, "sourceVolume": str}, total=False
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef", {"assignPublicIp": Literal["ENABLED", "DISABLED"]}, total=False
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {"attachmentId": str, "ipv6Address": str, "privateIpv4Address": str},
    total=False,
)

NodeDetailsTypeDef = TypedDict(
    "NodeDetailsTypeDef", {"nodeIndex": int, "isMainNode": bool}, total=False
)

NodePropertiesSummaryTypeDef = TypedDict(
    "NodePropertiesSummaryTypeDef",
    {"isMainNode": bool, "numNodes": int, "nodeIndex": int},
    total=False,
)

NodePropertiesTypeDef = TypedDict(
    "NodePropertiesTypeDef",
    {"numNodes": int, "mainNode": int, "nodeRangeProperties": List["NodeRangePropertyTypeDef"]},
)

_RequiredNodePropertyOverrideTypeDef = TypedDict(
    "_RequiredNodePropertyOverrideTypeDef", {"targetNodes": str}
)
_OptionalNodePropertyOverrideTypeDef = TypedDict(
    "_OptionalNodePropertyOverrideTypeDef",
    {"containerOverrides": "ContainerOverridesTypeDef"},
    total=False,
)


class NodePropertyOverrideTypeDef(
    _RequiredNodePropertyOverrideTypeDef, _OptionalNodePropertyOverrideTypeDef
):
    pass


_RequiredNodeRangePropertyTypeDef = TypedDict(
    "_RequiredNodeRangePropertyTypeDef", {"targetNodes": str}
)
_OptionalNodeRangePropertyTypeDef = TypedDict(
    "_OptionalNodeRangePropertyTypeDef", {"container": "ContainerPropertiesTypeDef"}, total=False
)


class NodeRangePropertyTypeDef(
    _RequiredNodeRangePropertyTypeDef, _OptionalNodeRangePropertyTypeDef
):
    pass


ResourceRequirementTypeDef = TypedDict(
    "ResourceRequirementTypeDef", {"value": str, "type": Literal["GPU", "VCPU", "MEMORY"]}
)

RetryStrategyTypeDef = TypedDict(
    "RetryStrategyTypeDef",
    {"attempts": int, "evaluateOnExit": List["EvaluateOnExitTypeDef"]},
    total=False,
)

SecretTypeDef = TypedDict("SecretTypeDef", {"name": str, "valueFrom": str})

_RequiredTmpfsTypeDef = TypedDict("_RequiredTmpfsTypeDef", {"containerPath": str, "size": int})
_OptionalTmpfsTypeDef = TypedDict("_OptionalTmpfsTypeDef", {"mountOptions": List[str]}, total=False)


class TmpfsTypeDef(_RequiredTmpfsTypeDef, _OptionalTmpfsTypeDef):
    pass


UlimitTypeDef = TypedDict("UlimitTypeDef", {"hardLimit": int, "name": str, "softLimit": int})

VolumeTypeDef = TypedDict("VolumeTypeDef", {"host": "HostTypeDef", "name": str}, total=False)

ArrayPropertiesTypeDef = TypedDict("ArrayPropertiesTypeDef", {"size": int}, total=False)

ComputeResourceUpdateTypeDef = TypedDict(
    "ComputeResourceUpdateTypeDef",
    {
        "minvCpus": int,
        "maxvCpus": int,
        "desiredvCpus": int,
        "subnets": List[str],
        "securityGroupIds": List[str],
    },
    total=False,
)

CreateComputeEnvironmentResponseTypeDef = TypedDict(
    "CreateComputeEnvironmentResponseTypeDef",
    {"computeEnvironmentName": str, "computeEnvironmentArn": str},
    total=False,
)

CreateJobQueueResponseTypeDef = TypedDict(
    "CreateJobQueueResponseTypeDef", {"jobQueueName": str, "jobQueueArn": str}
)

DescribeComputeEnvironmentsResponseTypeDef = TypedDict(
    "DescribeComputeEnvironmentsResponseTypeDef",
    {"computeEnvironments": List["ComputeEnvironmentDetailTypeDef"], "nextToken": str},
    total=False,
)

DescribeJobDefinitionsResponseTypeDef = TypedDict(
    "DescribeJobDefinitionsResponseTypeDef",
    {"jobDefinitions": List["JobDefinitionTypeDef"], "nextToken": str},
    total=False,
)

DescribeJobQueuesResponseTypeDef = TypedDict(
    "DescribeJobQueuesResponseTypeDef",
    {"jobQueues": List["JobQueueDetailTypeDef"], "nextToken": str},
    total=False,
)

DescribeJobsResponseTypeDef = TypedDict(
    "DescribeJobsResponseTypeDef", {"jobs": List["JobDetailTypeDef"]}, total=False
)

_RequiredListJobsResponseTypeDef = TypedDict(
    "_RequiredListJobsResponseTypeDef", {"jobSummaryList": List["JobSummaryTypeDef"]}
)
_OptionalListJobsResponseTypeDef = TypedDict(
    "_OptionalListJobsResponseTypeDef", {"nextToken": str}, total=False
)


class ListJobsResponseTypeDef(_RequiredListJobsResponseTypeDef, _OptionalListJobsResponseTypeDef):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

NodeOverridesTypeDef = TypedDict(
    "NodeOverridesTypeDef",
    {"numNodes": int, "nodePropertyOverrides": List["NodePropertyOverrideTypeDef"]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RegisterJobDefinitionResponseTypeDef = TypedDict(
    "RegisterJobDefinitionResponseTypeDef",
    {"jobDefinitionName": str, "jobDefinitionArn": str, "revision": int},
)

_RequiredSubmitJobResponseTypeDef = TypedDict(
    "_RequiredSubmitJobResponseTypeDef", {"jobName": str, "jobId": str}
)
_OptionalSubmitJobResponseTypeDef = TypedDict(
    "_OptionalSubmitJobResponseTypeDef", {"jobArn": str}, total=False
)


class SubmitJobResponseTypeDef(
    _RequiredSubmitJobResponseTypeDef, _OptionalSubmitJobResponseTypeDef
):
    pass


UpdateComputeEnvironmentResponseTypeDef = TypedDict(
    "UpdateComputeEnvironmentResponseTypeDef",
    {"computeEnvironmentName": str, "computeEnvironmentArn": str},
    total=False,
)

UpdateJobQueueResponseTypeDef = TypedDict(
    "UpdateJobQueueResponseTypeDef", {"jobQueueName": str, "jobQueueArn": str}, total=False
)
