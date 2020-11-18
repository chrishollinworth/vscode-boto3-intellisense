"""
Main interface for robomaker service type definitions.

Usage::

    ```python
    from mypy_boto3_robomaker.type_defs import BatchPolicyTypeDef

    data: BatchPolicyTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchPolicyTypeDef",
    "ComputeResponseTypeDef",
    "ComputeTypeDef",
    "DataSourceConfigTypeDef",
    "DataSourceTypeDef",
    "DeploymentApplicationConfigTypeDef",
    "DeploymentConfigTypeDef",
    "DeploymentJobTypeDef",
    "DeploymentLaunchConfigTypeDef",
    "FailedCreateSimulationJobRequestTypeDef",
    "FailureSummaryTypeDef",
    "FinishedWorldsSummaryTypeDef",
    "FleetTypeDef",
    "LaunchConfigTypeDef",
    "LoggingConfigTypeDef",
    "NetworkInterfaceTypeDef",
    "OutputLocationTypeDef",
    "PortForwardingConfigTypeDef",
    "PortMappingTypeDef",
    "ProgressDetailTypeDef",
    "RenderingEngineTypeDef",
    "ResponseMetadata",
    "RobotApplicationConfigTypeDef",
    "RobotApplicationSummaryTypeDef",
    "RobotDeploymentTypeDef",
    "RobotSoftwareSuiteTypeDef",
    "RobotTypeDef",
    "S3KeyOutputTypeDef",
    "S3ObjectTypeDef",
    "SimulationApplicationConfigTypeDef",
    "SimulationApplicationSummaryTypeDef",
    "SimulationJobBatchSummaryTypeDef",
    "SimulationJobRequestTypeDef",
    "SimulationJobSummaryTypeDef",
    "SimulationJobTypeDef",
    "SimulationSoftwareSuiteTypeDef",
    "SourceTypeDef",
    "TemplateSummaryTypeDef",
    "VPCConfigResponseTypeDef",
    "VPCConfigTypeDef",
    "WorldConfigTypeDef",
    "WorldCountTypeDef",
    "WorldExportJobSummaryTypeDef",
    "WorldFailureTypeDef",
    "WorldGenerationJobSummaryTypeDef",
    "WorldSummaryTypeDef",
    "BatchDeleteWorldsResponseTypeDef",
    "BatchDescribeSimulationJobResponseTypeDef",
    "CreateDeploymentJobResponseTypeDef",
    "CreateFleetResponseTypeDef",
    "CreateRobotApplicationResponseTypeDef",
    "CreateRobotApplicationVersionResponseTypeDef",
    "CreateRobotResponseTypeDef",
    "CreateSimulationApplicationResponseTypeDef",
    "CreateSimulationApplicationVersionResponseTypeDef",
    "CreateSimulationJobResponseTypeDef",
    "CreateWorldExportJobResponseTypeDef",
    "CreateWorldGenerationJobResponseTypeDef",
    "CreateWorldTemplateResponseTypeDef",
    "DeregisterRobotResponseTypeDef",
    "DescribeDeploymentJobResponseTypeDef",
    "DescribeFleetResponseTypeDef",
    "DescribeRobotApplicationResponseTypeDef",
    "DescribeRobotResponseTypeDef",
    "DescribeSimulationApplicationResponseTypeDef",
    "DescribeSimulationJobBatchResponseTypeDef",
    "DescribeSimulationJobResponseTypeDef",
    "DescribeWorldExportJobResponseTypeDef",
    "DescribeWorldGenerationJobResponseTypeDef",
    "DescribeWorldResponseTypeDef",
    "DescribeWorldTemplateResponseTypeDef",
    "FilterTypeDef",
    "GetWorldTemplateBodyResponseTypeDef",
    "ListDeploymentJobsResponseTypeDef",
    "ListFleetsResponseTypeDef",
    "ListRobotApplicationsResponseTypeDef",
    "ListRobotsResponseTypeDef",
    "ListSimulationApplicationsResponseTypeDef",
    "ListSimulationJobBatchesResponseTypeDef",
    "ListSimulationJobsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorldExportJobsResponseTypeDef",
    "ListWorldGenerationJobsResponseTypeDef",
    "ListWorldTemplatesResponseTypeDef",
    "ListWorldsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterRobotResponseTypeDef",
    "SourceConfigTypeDef",
    "StartSimulationJobBatchResponseTypeDef",
    "SyncDeploymentJobResponseTypeDef",
    "TemplateLocationTypeDef",
    "UpdateRobotApplicationResponseTypeDef",
    "UpdateSimulationApplicationResponseTypeDef",
    "UpdateWorldTemplateResponseTypeDef",
)

BatchPolicyTypeDef = TypedDict(
    "BatchPolicyTypeDef", {"timeoutInSeconds": int, "maxConcurrency": int}, total=False
)

ComputeResponseTypeDef = TypedDict(
    "ComputeResponseTypeDef", {"simulationUnitLimit": int}, total=False
)

ComputeTypeDef = TypedDict("ComputeTypeDef", {"simulationUnitLimit": int}, total=False)

DataSourceConfigTypeDef = TypedDict(
    "DataSourceConfigTypeDef", {"name": str, "s3Bucket": str, "s3Keys": List[str]}
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {"name": str, "s3Bucket": str, "s3Keys": List["S3KeyOutputTypeDef"]},
    total=False,
)

DeploymentApplicationConfigTypeDef = TypedDict(
    "DeploymentApplicationConfigTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": "DeploymentLaunchConfigTypeDef",
    },
)

DeploymentConfigTypeDef = TypedDict(
    "DeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": "S3ObjectTypeDef",
    },
    total=False,
)

DeploymentJobTypeDef = TypedDict(
    "DeploymentJobTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": Literal["Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"],
        "deploymentApplicationConfigs": List["DeploymentApplicationConfigTypeDef"],
        "deploymentConfig": "DeploymentConfigTypeDef",
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "InvalidGreengrassGroup",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "LambdaDeleted",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
        "createdAt": datetime,
    },
    total=False,
)

_RequiredDeploymentLaunchConfigTypeDef = TypedDict(
    "_RequiredDeploymentLaunchConfigTypeDef", {"packageName": str, "launchFile": str}
)
_OptionalDeploymentLaunchConfigTypeDef = TypedDict(
    "_OptionalDeploymentLaunchConfigTypeDef",
    {"preLaunchFile": str, "postLaunchFile": str, "environmentVariables": Dict[str, str]},
    total=False,
)


class DeploymentLaunchConfigTypeDef(
    _RequiredDeploymentLaunchConfigTypeDef, _OptionalDeploymentLaunchConfigTypeDef
):
    pass


FailedCreateSimulationJobRequestTypeDef = TypedDict(
    "FailedCreateSimulationJobRequestTypeDef",
    {
        "request": "SimulationJobRequestTypeDef",
        "failureReason": str,
        "failureCode": Literal[
            "InternalServiceError",
            "RobotApplicationCrash",
            "SimulationApplicationCrash",
            "BadPermissionsRobotApplication",
            "BadPermissionsSimulationApplication",
            "BadPermissionsS3Object",
            "BadPermissionsS3Output",
            "BadPermissionsCloudwatchLogs",
            "SubnetIpLimitExceeded",
            "ENILimitExceeded",
            "BadPermissionsUserCredentials",
            "InvalidBundleRobotApplication",
            "InvalidBundleSimulationApplication",
            "InvalidS3Resource",
            "LimitExceeded",
            "MismatchedEtag",
            "RobotApplicationVersionMismatchedEtag",
            "SimulationApplicationVersionMismatchedEtag",
            "ResourceNotFound",
            "RequestThrottled",
            "BatchTimedOut",
            "BatchCanceled",
            "InvalidInput",
            "WrongRegionS3Bucket",
            "WrongRegionS3Output",
            "WrongRegionRobotApplication",
            "WrongRegionSimulationApplication",
        ],
        "failedAt": datetime,
    },
    total=False,
)

FailureSummaryTypeDef = TypedDict(
    "FailureSummaryTypeDef",
    {"totalFailureCount": int, "failures": List["WorldFailureTypeDef"]},
    total=False,
)

FinishedWorldsSummaryTypeDef = TypedDict(
    "FinishedWorldsSummaryTypeDef",
    {"finishedCount": int, "succeededWorlds": List[str], "failureSummary": "FailureSummaryTypeDef"},
    total=False,
)

FleetTypeDef = TypedDict(
    "FleetTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "lastDeploymentStatus": Literal[
            "Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"
        ],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)

_RequiredLaunchConfigTypeDef = TypedDict(
    "_RequiredLaunchConfigTypeDef", {"packageName": str, "launchFile": str}
)
_OptionalLaunchConfigTypeDef = TypedDict(
    "_OptionalLaunchConfigTypeDef",
    {
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": "PortForwardingConfigTypeDef",
        "streamUI": bool,
    },
    total=False,
)


class LaunchConfigTypeDef(_RequiredLaunchConfigTypeDef, _OptionalLaunchConfigTypeDef):
    pass


LoggingConfigTypeDef = TypedDict("LoggingConfigTypeDef", {"recordAllRosTopics": bool})

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {"networkInterfaceId": str, "privateIpAddress": str, "publicIpAddress": str},
    total=False,
)

OutputLocationTypeDef = TypedDict(
    "OutputLocationTypeDef", {"s3Bucket": str, "s3Prefix": str}, total=False
)

PortForwardingConfigTypeDef = TypedDict(
    "PortForwardingConfigTypeDef", {"portMappings": List["PortMappingTypeDef"]}, total=False
)

_RequiredPortMappingTypeDef = TypedDict(
    "_RequiredPortMappingTypeDef", {"jobPort": int, "applicationPort": int}
)
_OptionalPortMappingTypeDef = TypedDict(
    "_OptionalPortMappingTypeDef", {"enableOnPublicIp": bool}, total=False
)


class PortMappingTypeDef(_RequiredPortMappingTypeDef, _OptionalPortMappingTypeDef):
    pass


ProgressDetailTypeDef = TypedDict(
    "ProgressDetailTypeDef",
    {
        "currentProgress": Literal[
            "Validating",
            "DownloadingExtracting",
            "ExecutingDownloadCondition",
            "ExecutingPreLaunch",
            "Launching",
            "ExecutingPostLaunch",
            "Finished",
        ],
        "percentDone": float,
        "estimatedTimeRemainingSeconds": int,
        "targetResource": str,
    },
    total=False,
)

RenderingEngineTypeDef = TypedDict(
    "RenderingEngineTypeDef", {"name": Literal["OGRE"], "version": str}, total=False
)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredRobotApplicationConfigTypeDef = TypedDict(
    "_RequiredRobotApplicationConfigTypeDef",
    {"application": str, "launchConfig": "LaunchConfigTypeDef"},
)
_OptionalRobotApplicationConfigTypeDef = TypedDict(
    "_OptionalRobotApplicationConfigTypeDef", {"applicationVersion": str}, total=False
)


class RobotApplicationConfigTypeDef(
    _RequiredRobotApplicationConfigTypeDef, _OptionalRobotApplicationConfigTypeDef
):
    pass


RobotApplicationSummaryTypeDef = TypedDict(
    "RobotApplicationSummaryTypeDef",
    {
        "name": str,
        "arn": str,
        "version": str,
        "lastUpdatedAt": datetime,
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
    },
    total=False,
)

RobotDeploymentTypeDef = TypedDict(
    "RobotDeploymentTypeDef",
    {
        "arn": str,
        "deploymentStartTime": datetime,
        "deploymentFinishTime": datetime,
        "status": Literal[
            "Available",
            "Registered",
            "PendingNewDeployment",
            "Deploying",
            "Failed",
            "InSync",
            "NoResponse",
        ],
        "progressDetail": "ProgressDetailTypeDef",
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "InvalidGreengrassGroup",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "LambdaDeleted",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
    },
    total=False,
)

RobotSoftwareSuiteTypeDef = TypedDict(
    "RobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)

RobotTypeDef = TypedDict(
    "RobotTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": Literal[
            "Available",
            "Registered",
            "PendingNewDeployment",
            "Deploying",
            "Failed",
            "InSync",
            "NoResponse",
        ],
        "greenGrassGroupId": str,
        "createdAt": datetime,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)

S3KeyOutputTypeDef = TypedDict(
    "S3KeyOutputTypeDef",
    {"s3Key": str, "etag": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredS3ObjectTypeDef = TypedDict("_RequiredS3ObjectTypeDef", {"bucket": str, "key": str})
_OptionalS3ObjectTypeDef = TypedDict("_OptionalS3ObjectTypeDef", {"etag": str}, total=False)


class S3ObjectTypeDef(_RequiredS3ObjectTypeDef, _OptionalS3ObjectTypeDef):
    pass


_RequiredSimulationApplicationConfigTypeDef = TypedDict(
    "_RequiredSimulationApplicationConfigTypeDef",
    {"application": str, "launchConfig": "LaunchConfigTypeDef"},
)
_OptionalSimulationApplicationConfigTypeDef = TypedDict(
    "_OptionalSimulationApplicationConfigTypeDef",
    {"applicationVersion": str, "worldConfigs": List["WorldConfigTypeDef"]},
    total=False,
)


class SimulationApplicationConfigTypeDef(
    _RequiredSimulationApplicationConfigTypeDef, _OptionalSimulationApplicationConfigTypeDef
):
    pass


SimulationApplicationSummaryTypeDef = TypedDict(
    "SimulationApplicationSummaryTypeDef",
    {
        "name": str,
        "arn": str,
        "version": str,
        "lastUpdatedAt": datetime,
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
    },
    total=False,
)

SimulationJobBatchSummaryTypeDef = TypedDict(
    "SimulationJobBatchSummaryTypeDef",
    {
        "arn": str,
        "lastUpdatedAt": datetime,
        "createdAt": datetime,
        "status": Literal[
            "Pending",
            "InProgress",
            "Failed",
            "Completed",
            "Canceled",
            "Canceling",
            "Completing",
            "TimingOut",
            "TimedOut",
        ],
        "failedRequestCount": int,
        "pendingRequestCount": int,
        "createdRequestCount": int,
    },
    total=False,
)

_RequiredSimulationJobRequestTypeDef = TypedDict(
    "_RequiredSimulationJobRequestTypeDef", {"maxJobDurationInSeconds": int}
)
_OptionalSimulationJobRequestTypeDef = TypedDict(
    "_OptionalSimulationJobRequestTypeDef",
    {
        "outputLocation": "OutputLocationTypeDef",
        "loggingConfig": "LoggingConfigTypeDef",
        "iamRole": str,
        "failureBehavior": Literal["Fail", "Continue"],
        "useDefaultApplications": bool,
        "robotApplications": List["RobotApplicationConfigTypeDef"],
        "simulationApplications": List["SimulationApplicationConfigTypeDef"],
        "dataSources": List["DataSourceConfigTypeDef"],
        "vpcConfig": "VPCConfigTypeDef",
        "compute": "ComputeTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class SimulationJobRequestTypeDef(
    _RequiredSimulationJobRequestTypeDef, _OptionalSimulationJobRequestTypeDef
):
    pass


SimulationJobSummaryTypeDef = TypedDict(
    "SimulationJobSummaryTypeDef",
    {
        "arn": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "simulationApplicationNames": List[str],
        "robotApplicationNames": List[str],
        "dataSourceNames": List[str],
    },
    total=False,
)

SimulationJobTypeDef = TypedDict(
    "SimulationJobTypeDef",
    {
        "arn": str,
        "name": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": Literal["Fail", "Continue"],
        "failureCode": Literal[
            "InternalServiceError",
            "RobotApplicationCrash",
            "SimulationApplicationCrash",
            "BadPermissionsRobotApplication",
            "BadPermissionsSimulationApplication",
            "BadPermissionsS3Object",
            "BadPermissionsS3Output",
            "BadPermissionsCloudwatchLogs",
            "SubnetIpLimitExceeded",
            "ENILimitExceeded",
            "BadPermissionsUserCredentials",
            "InvalidBundleRobotApplication",
            "InvalidBundleSimulationApplication",
            "InvalidS3Resource",
            "LimitExceeded",
            "MismatchedEtag",
            "RobotApplicationVersionMismatchedEtag",
            "SimulationApplicationVersionMismatchedEtag",
            "ResourceNotFound",
            "RequestThrottled",
            "BatchTimedOut",
            "BatchCanceled",
            "InvalidInput",
            "WrongRegionS3Bucket",
            "WrongRegionS3Output",
            "WrongRegionRobotApplication",
            "WrongRegionSimulationApplication",
        ],
        "failureReason": str,
        "clientRequestToken": str,
        "outputLocation": "OutputLocationTypeDef",
        "loggingConfig": "LoggingConfigTypeDef",
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List["RobotApplicationConfigTypeDef"],
        "simulationApplications": List["SimulationApplicationConfigTypeDef"],
        "dataSources": List["DataSourceTypeDef"],
        "tags": Dict[str, str],
        "vpcConfig": "VPCConfigResponseTypeDef",
        "networkInterface": "NetworkInterfaceTypeDef",
        "compute": "ComputeResponseTypeDef",
    },
    total=False,
)

SimulationSoftwareSuiteTypeDef = TypedDict(
    "SimulationSoftwareSuiteTypeDef",
    {"name": Literal["Gazebo", "RosbagPlay"], "version": str},
    total=False,
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
    },
    total=False,
)

TemplateSummaryTypeDef = TypedDict(
    "TemplateSummaryTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "name": str},
    total=False,
)

VPCConfigResponseTypeDef = TypedDict(
    "VPCConfigResponseTypeDef",
    {"subnets": List[str], "securityGroups": List[str], "vpcId": str, "assignPublicIp": bool},
    total=False,
)

_RequiredVPCConfigTypeDef = TypedDict("_RequiredVPCConfigTypeDef", {"subnets": List[str]})
_OptionalVPCConfigTypeDef = TypedDict(
    "_OptionalVPCConfigTypeDef", {"securityGroups": List[str], "assignPublicIp": bool}, total=False
)


class VPCConfigTypeDef(_RequiredVPCConfigTypeDef, _OptionalVPCConfigTypeDef):
    pass


WorldConfigTypeDef = TypedDict("WorldConfigTypeDef", {"world": str}, total=False)

WorldCountTypeDef = TypedDict(
    "WorldCountTypeDef", {"floorplanCount": int, "interiorCountPerFloorplan": int}, total=False
)

WorldExportJobSummaryTypeDef = TypedDict(
    "WorldExportJobSummaryTypeDef",
    {
        "arn": str,
        "status": Literal["Pending", "Running", "Completed", "Failed", "Canceling", "Canceled"],
        "createdAt": datetime,
        "worlds": List[str],
    },
    total=False,
)

WorldFailureTypeDef = TypedDict(
    "WorldFailureTypeDef",
    {
        "failureCode": Literal[
            "InternalServiceError",
            "LimitExceeded",
            "ResourceNotFound",
            "RequestThrottled",
            "InvalidInput",
            "AllWorldGenerationFailed",
        ],
        "sampleFailureReason": str,
        "failureCount": int,
    },
    total=False,
)

WorldGenerationJobSummaryTypeDef = TypedDict(
    "WorldGenerationJobSummaryTypeDef",
    {
        "arn": str,
        "template": str,
        "createdAt": datetime,
        "status": Literal[
            "Pending", "Running", "Completed", "Failed", "PartialFailed", "Canceling", "Canceled"
        ],
        "worldCount": "WorldCountTypeDef",
        "succeededWorldCount": int,
        "failedWorldCount": int,
    },
    total=False,
)

WorldSummaryTypeDef = TypedDict(
    "WorldSummaryTypeDef",
    {"arn": str, "createdAt": datetime, "generationJob": str, "template": str},
    total=False,
)

BatchDeleteWorldsResponseTypeDef = TypedDict(
    "BatchDeleteWorldsResponseTypeDef", {"unprocessedWorlds": List[str]}, total=False
)

BatchDescribeSimulationJobResponseTypeDef = TypedDict(
    "BatchDescribeSimulationJobResponseTypeDef",
    {"jobs": List["SimulationJobTypeDef"], "unprocessedJobs": List[str]},
    total=False,
)

CreateDeploymentJobResponseTypeDef = TypedDict(
    "CreateDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": Literal["Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"],
        "deploymentApplicationConfigs": List["DeploymentApplicationConfigTypeDef"],
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "InvalidGreengrassGroup",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "LambdaDeleted",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
        "createdAt": datetime,
        "deploymentConfig": "DeploymentConfigTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

CreateFleetResponseTypeDef = TypedDict(
    "CreateFleetResponseTypeDef",
    {"arn": str, "name": str, "createdAt": datetime, "tags": Dict[str, str]},
    total=False,
)

CreateRobotApplicationResponseTypeDef = TypedDict(
    "CreateRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateRobotApplicationVersionResponseTypeDef = TypedDict(
    "CreateRobotApplicationVersionResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)

CreateRobotResponseTypeDef = TypedDict(
    "CreateRobotResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "greengrassGroupId": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
        "tags": Dict[str, str],
    },
    total=False,
)

CreateSimulationApplicationResponseTypeDef = TypedDict(
    "CreateSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "renderingEngine": "RenderingEngineTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateSimulationApplicationVersionResponseTypeDef = TypedDict(
    "CreateSimulationApplicationVersionResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "renderingEngine": "RenderingEngineTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)

CreateSimulationJobResponseTypeDef = TypedDict(
    "CreateSimulationJobResponseTypeDef",
    {
        "arn": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": Literal["Fail", "Continue"],
        "failureCode": Literal[
            "InternalServiceError",
            "RobotApplicationCrash",
            "SimulationApplicationCrash",
            "BadPermissionsRobotApplication",
            "BadPermissionsSimulationApplication",
            "BadPermissionsS3Object",
            "BadPermissionsS3Output",
            "BadPermissionsCloudwatchLogs",
            "SubnetIpLimitExceeded",
            "ENILimitExceeded",
            "BadPermissionsUserCredentials",
            "InvalidBundleRobotApplication",
            "InvalidBundleSimulationApplication",
            "InvalidS3Resource",
            "LimitExceeded",
            "MismatchedEtag",
            "RobotApplicationVersionMismatchedEtag",
            "SimulationApplicationVersionMismatchedEtag",
            "ResourceNotFound",
            "RequestThrottled",
            "BatchTimedOut",
            "BatchCanceled",
            "InvalidInput",
            "WrongRegionS3Bucket",
            "WrongRegionS3Output",
            "WrongRegionRobotApplication",
            "WrongRegionSimulationApplication",
        ],
        "clientRequestToken": str,
        "outputLocation": "OutputLocationTypeDef",
        "loggingConfig": "LoggingConfigTypeDef",
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List["RobotApplicationConfigTypeDef"],
        "simulationApplications": List["SimulationApplicationConfigTypeDef"],
        "dataSources": List["DataSourceTypeDef"],
        "tags": Dict[str, str],
        "vpcConfig": "VPCConfigResponseTypeDef",
        "compute": "ComputeResponseTypeDef",
    },
    total=False,
)

CreateWorldExportJobResponseTypeDef = TypedDict(
    "CreateWorldExportJobResponseTypeDef",
    {
        "arn": str,
        "status": Literal["Pending", "Running", "Completed", "Failed", "Canceling", "Canceled"],
        "createdAt": datetime,
        "failureCode": Literal[
            "InternalServiceError",
            "LimitExceeded",
            "ResourceNotFound",
            "RequestThrottled",
            "InvalidInput",
            "AccessDenied",
        ],
        "clientRequestToken": str,
        "outputLocation": "OutputLocationTypeDef",
        "iamRole": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateWorldGenerationJobResponseTypeDef = TypedDict(
    "CreateWorldGenerationJobResponseTypeDef",
    {
        "arn": str,
        "status": Literal[
            "Pending", "Running", "Completed", "Failed", "PartialFailed", "Canceling", "Canceled"
        ],
        "createdAt": datetime,
        "failureCode": Literal[
            "InternalServiceError",
            "LimitExceeded",
            "ResourceNotFound",
            "RequestThrottled",
            "InvalidInput",
            "AllWorldGenerationFailed",
        ],
        "clientRequestToken": str,
        "template": str,
        "worldCount": "WorldCountTypeDef",
        "tags": Dict[str, str],
        "worldTags": Dict[str, str],
    },
    total=False,
)

CreateWorldTemplateResponseTypeDef = TypedDict(
    "CreateWorldTemplateResponseTypeDef",
    {
        "arn": str,
        "clientRequestToken": str,
        "createdAt": datetime,
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

DeregisterRobotResponseTypeDef = TypedDict(
    "DeregisterRobotResponseTypeDef", {"fleet": str, "robot": str}, total=False
)

DescribeDeploymentJobResponseTypeDef = TypedDict(
    "DescribeDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": Literal["Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"],
        "deploymentConfig": "DeploymentConfigTypeDef",
        "deploymentApplicationConfigs": List["DeploymentApplicationConfigTypeDef"],
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "InvalidGreengrassGroup",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "LambdaDeleted",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
        "createdAt": datetime,
        "robotDeploymentSummary": List["RobotDeploymentTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeFleetResponseTypeDef = TypedDict(
    "DescribeFleetResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "robots": List["RobotTypeDef"],
        "createdAt": datetime,
        "lastDeploymentStatus": Literal[
            "Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"
        ],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeRobotApplicationResponseTypeDef = TypedDict(
    "DescribeRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "revisionId": str,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeRobotResponseTypeDef = TypedDict(
    "DescribeRobotResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": Literal[
            "Available",
            "Registered",
            "PendingNewDeployment",
            "Deploying",
            "Failed",
            "InSync",
            "NoResponse",
        ],
        "greengrassGroupId": str,
        "createdAt": datetime,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeSimulationApplicationResponseTypeDef = TypedDict(
    "DescribeSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "renderingEngine": "RenderingEngineTypeDef",
        "revisionId": str,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeSimulationJobBatchResponseTypeDef = TypedDict(
    "DescribeSimulationJobBatchResponseTypeDef",
    {
        "arn": str,
        "status": Literal[
            "Pending",
            "InProgress",
            "Failed",
            "Completed",
            "Canceled",
            "Canceling",
            "Completing",
            "TimingOut",
            "TimedOut",
        ],
        "lastUpdatedAt": datetime,
        "createdAt": datetime,
        "clientRequestToken": str,
        "batchPolicy": "BatchPolicyTypeDef",
        "failureCode": Literal["InternalServiceError"],
        "failureReason": str,
        "failedRequests": List["FailedCreateSimulationJobRequestTypeDef"],
        "pendingRequests": List["SimulationJobRequestTypeDef"],
        "createdRequests": List["SimulationJobSummaryTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeSimulationJobResponseTypeDef = TypedDict(
    "DescribeSimulationJobResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": Literal["Fail", "Continue"],
        "failureCode": Literal[
            "InternalServiceError",
            "RobotApplicationCrash",
            "SimulationApplicationCrash",
            "BadPermissionsRobotApplication",
            "BadPermissionsSimulationApplication",
            "BadPermissionsS3Object",
            "BadPermissionsS3Output",
            "BadPermissionsCloudwatchLogs",
            "SubnetIpLimitExceeded",
            "ENILimitExceeded",
            "BadPermissionsUserCredentials",
            "InvalidBundleRobotApplication",
            "InvalidBundleSimulationApplication",
            "InvalidS3Resource",
            "LimitExceeded",
            "MismatchedEtag",
            "RobotApplicationVersionMismatchedEtag",
            "SimulationApplicationVersionMismatchedEtag",
            "ResourceNotFound",
            "RequestThrottled",
            "BatchTimedOut",
            "BatchCanceled",
            "InvalidInput",
            "WrongRegionS3Bucket",
            "WrongRegionS3Output",
            "WrongRegionRobotApplication",
            "WrongRegionSimulationApplication",
        ],
        "failureReason": str,
        "clientRequestToken": str,
        "outputLocation": "OutputLocationTypeDef",
        "loggingConfig": "LoggingConfigTypeDef",
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List["RobotApplicationConfigTypeDef"],
        "simulationApplications": List["SimulationApplicationConfigTypeDef"],
        "dataSources": List["DataSourceTypeDef"],
        "tags": Dict[str, str],
        "vpcConfig": "VPCConfigResponseTypeDef",
        "networkInterface": "NetworkInterfaceTypeDef",
        "compute": "ComputeResponseTypeDef",
    },
    total=False,
)

DescribeWorldExportJobResponseTypeDef = TypedDict(
    "DescribeWorldExportJobResponseTypeDef",
    {
        "arn": str,
        "status": Literal["Pending", "Running", "Completed", "Failed", "Canceling", "Canceled"],
        "createdAt": datetime,
        "failureCode": Literal[
            "InternalServiceError",
            "LimitExceeded",
            "ResourceNotFound",
            "RequestThrottled",
            "InvalidInput",
            "AccessDenied",
        ],
        "failureReason": str,
        "clientRequestToken": str,
        "worlds": List[str],
        "outputLocation": "OutputLocationTypeDef",
        "iamRole": str,
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeWorldGenerationJobResponseTypeDef = TypedDict(
    "DescribeWorldGenerationJobResponseTypeDef",
    {
        "arn": str,
        "status": Literal[
            "Pending", "Running", "Completed", "Failed", "PartialFailed", "Canceling", "Canceled"
        ],
        "createdAt": datetime,
        "failureCode": Literal[
            "InternalServiceError",
            "LimitExceeded",
            "ResourceNotFound",
            "RequestThrottled",
            "InvalidInput",
            "AllWorldGenerationFailed",
        ],
        "failureReason": str,
        "clientRequestToken": str,
        "template": str,
        "worldCount": "WorldCountTypeDef",
        "finishedWorldsSummary": "FinishedWorldsSummaryTypeDef",
        "tags": Dict[str, str],
        "worldTags": Dict[str, str],
    },
    total=False,
)

DescribeWorldResponseTypeDef = TypedDict(
    "DescribeWorldResponseTypeDef",
    {
        "arn": str,
        "generationJob": str,
        "template": str,
        "createdAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeWorldTemplateResponseTypeDef = TypedDict(
    "DescribeWorldTemplateResponseTypeDef",
    {
        "arn": str,
        "clientRequestToken": str,
        "name": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

FilterTypeDef = TypedDict("FilterTypeDef", {"name": str, "values": List[str]}, total=False)

GetWorldTemplateBodyResponseTypeDef = TypedDict(
    "GetWorldTemplateBodyResponseTypeDef", {"templateBody": str}, total=False
)

ListDeploymentJobsResponseTypeDef = TypedDict(
    "ListDeploymentJobsResponseTypeDef",
    {"deploymentJobs": List["DeploymentJobTypeDef"], "nextToken": str},
    total=False,
)

ListFleetsResponseTypeDef = TypedDict(
    "ListFleetsResponseTypeDef",
    {"fleetDetails": List["FleetTypeDef"], "nextToken": str},
    total=False,
)

ListRobotApplicationsResponseTypeDef = TypedDict(
    "ListRobotApplicationsResponseTypeDef",
    {"robotApplicationSummaries": List["RobotApplicationSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListRobotsResponseTypeDef = TypedDict(
    "ListRobotsResponseTypeDef", {"robots": List["RobotTypeDef"], "nextToken": str}, total=False
)

ListSimulationApplicationsResponseTypeDef = TypedDict(
    "ListSimulationApplicationsResponseTypeDef",
    {
        "simulationApplicationSummaries": List["SimulationApplicationSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListSimulationJobBatchesResponseTypeDef = TypedDict(
    "ListSimulationJobBatchesResponseTypeDef",
    {"simulationJobBatchSummaries": List["SimulationJobBatchSummaryTypeDef"], "nextToken": str},
    total=False,
)

_RequiredListSimulationJobsResponseTypeDef = TypedDict(
    "_RequiredListSimulationJobsResponseTypeDef",
    {"simulationJobSummaries": List["SimulationJobSummaryTypeDef"]},
)
_OptionalListSimulationJobsResponseTypeDef = TypedDict(
    "_OptionalListSimulationJobsResponseTypeDef", {"nextToken": str}, total=False
)


class ListSimulationJobsResponseTypeDef(
    _RequiredListSimulationJobsResponseTypeDef, _OptionalListSimulationJobsResponseTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

_RequiredListWorldExportJobsResponseTypeDef = TypedDict(
    "_RequiredListWorldExportJobsResponseTypeDef",
    {"worldExportJobSummaries": List["WorldExportJobSummaryTypeDef"]},
)
_OptionalListWorldExportJobsResponseTypeDef = TypedDict(
    "_OptionalListWorldExportJobsResponseTypeDef", {"nextToken": str}, total=False
)


class ListWorldExportJobsResponseTypeDef(
    _RequiredListWorldExportJobsResponseTypeDef, _OptionalListWorldExportJobsResponseTypeDef
):
    pass


_RequiredListWorldGenerationJobsResponseTypeDef = TypedDict(
    "_RequiredListWorldGenerationJobsResponseTypeDef",
    {"worldGenerationJobSummaries": List["WorldGenerationJobSummaryTypeDef"]},
)
_OptionalListWorldGenerationJobsResponseTypeDef = TypedDict(
    "_OptionalListWorldGenerationJobsResponseTypeDef", {"nextToken": str}, total=False
)


class ListWorldGenerationJobsResponseTypeDef(
    _RequiredListWorldGenerationJobsResponseTypeDef, _OptionalListWorldGenerationJobsResponseTypeDef
):
    pass


ListWorldTemplatesResponseTypeDef = TypedDict(
    "ListWorldTemplatesResponseTypeDef",
    {"templateSummaries": List["TemplateSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListWorldsResponseTypeDef = TypedDict(
    "ListWorldsResponseTypeDef",
    {"worldSummaries": List["WorldSummaryTypeDef"], "nextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RegisterRobotResponseTypeDef = TypedDict(
    "RegisterRobotResponseTypeDef", {"fleet": str, "robot": str}, total=False
)

SourceConfigTypeDef = TypedDict(
    "SourceConfigTypeDef",
    {"s3Bucket": str, "s3Key": str, "architecture": Literal["X86_64", "ARM64", "ARMHF"]},
    total=False,
)

StartSimulationJobBatchResponseTypeDef = TypedDict(
    "StartSimulationJobBatchResponseTypeDef",
    {
        "arn": str,
        "status": Literal[
            "Pending",
            "InProgress",
            "Failed",
            "Completed",
            "Canceled",
            "Canceling",
            "Completing",
            "TimingOut",
            "TimedOut",
        ],
        "createdAt": datetime,
        "clientRequestToken": str,
        "batchPolicy": "BatchPolicyTypeDef",
        "failureCode": Literal["InternalServiceError"],
        "failureReason": str,
        "failedRequests": List["FailedCreateSimulationJobRequestTypeDef"],
        "pendingRequests": List["SimulationJobRequestTypeDef"],
        "createdRequests": List["SimulationJobSummaryTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)

SyncDeploymentJobResponseTypeDef = TypedDict(
    "SyncDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": Literal["Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"],
        "deploymentConfig": "DeploymentConfigTypeDef",
        "deploymentApplicationConfigs": List["DeploymentApplicationConfigTypeDef"],
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "InvalidGreengrassGroup",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "LambdaDeleted",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
        "createdAt": datetime,
    },
    total=False,
)

TemplateLocationTypeDef = TypedDict("TemplateLocationTypeDef", {"s3Bucket": str, "s3Key": str})

UpdateRobotApplicationResponseTypeDef = TypedDict(
    "UpdateRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)

UpdateSimulationApplicationResponseTypeDef = TypedDict(
    "UpdateSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "renderingEngine": "RenderingEngineTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)

UpdateWorldTemplateResponseTypeDef = TypedDict(
    "UpdateWorldTemplateResponseTypeDef",
    {"arn": str, "name": str, "createdAt": datetime, "lastUpdatedAt": datetime},
    total=False,
)
