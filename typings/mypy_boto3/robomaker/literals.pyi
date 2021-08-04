"""
Type annotations for robomaker service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/literals.html)

Usage::

    ```python
    from mypy_boto3_robomaker.literals import ArchitectureType

    data: ArchitectureType = "ARM64"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ArchitectureType",
    "DeploymentJobErrorCodeType",
    "DeploymentStatusType",
    "ExitBehaviorType",
    "FailureBehaviorType",
    "ListDeploymentJobsPaginatorName",
    "ListFleetsPaginatorName",
    "ListRobotApplicationsPaginatorName",
    "ListRobotsPaginatorName",
    "ListSimulationApplicationsPaginatorName",
    "ListSimulationJobBatchesPaginatorName",
    "ListSimulationJobsPaginatorName",
    "ListWorldExportJobsPaginatorName",
    "ListWorldGenerationJobsPaginatorName",
    "ListWorldTemplatesPaginatorName",
    "ListWorldsPaginatorName",
    "RenderingEngineTypeType",
    "RobotDeploymentStepType",
    "RobotSoftwareSuiteTypeType",
    "RobotSoftwareSuiteVersionTypeType",
    "RobotStatusType",
    "SimulationJobBatchErrorCodeType",
    "SimulationJobBatchStatusType",
    "SimulationJobErrorCodeType",
    "SimulationJobStatusType",
    "SimulationSoftwareSuiteTypeType",
    "UploadBehaviorType",
    "WorldExportJobErrorCodeType",
    "WorldExportJobStatusType",
    "WorldGenerationJobErrorCodeType",
    "WorldGenerationJobStatusType",
)

ArchitectureType = Literal["ARM64", "ARMHF", "X86_64"]
DeploymentJobErrorCodeType = Literal[
    "BadLambdaAssociated",
    "BadPermissionError",
    "DeploymentFleetDoesNotExist",
    "DownloadConditionFailed",
    "EnvironmentSetupError",
    "EtagMismatch",
    "ExtractingBundleFailure",
    "FailureThresholdBreached",
    "FleetDeploymentTimeout",
    "GreengrassDeploymentFailed",
    "GreengrassGroupVersionDoesNotExist",
    "InternalServerError",
    "InvalidGreengrassGroup",
    "LambdaDeleted",
    "MissingRobotApplicationArchitecture",
    "MissingRobotArchitecture",
    "MissingRobotDeploymentResource",
    "PostLaunchFileFailure",
    "PreLaunchFileFailure",
    "ResourceNotFound",
    "RobotAgentConnectionTimeout",
    "RobotApplicationDoesNotExist",
    "RobotDeploymentAborted",
    "RobotDeploymentNoResponse",
]
DeploymentStatusType = Literal[
    "Canceled", "Failed", "InProgress", "Pending", "Preparing", "Succeeded"
]
ExitBehaviorType = Literal["FAIL", "RESTART"]
FailureBehaviorType = Literal["Continue", "Fail"]
ListDeploymentJobsPaginatorName = Literal["list_deployment_jobs"]
ListFleetsPaginatorName = Literal["list_fleets"]
ListRobotApplicationsPaginatorName = Literal["list_robot_applications"]
ListRobotsPaginatorName = Literal["list_robots"]
ListSimulationApplicationsPaginatorName = Literal["list_simulation_applications"]
ListSimulationJobBatchesPaginatorName = Literal["list_simulation_job_batches"]
ListSimulationJobsPaginatorName = Literal["list_simulation_jobs"]
ListWorldExportJobsPaginatorName = Literal["list_world_export_jobs"]
ListWorldGenerationJobsPaginatorName = Literal["list_world_generation_jobs"]
ListWorldTemplatesPaginatorName = Literal["list_world_templates"]
ListWorldsPaginatorName = Literal["list_worlds"]
RenderingEngineTypeType = Literal["OGRE"]
RobotDeploymentStepType = Literal[
    "DownloadingExtracting",
    "ExecutingDownloadCondition",
    "ExecutingPostLaunch",
    "ExecutingPreLaunch",
    "Finished",
    "Launching",
    "Validating",
]
RobotSoftwareSuiteTypeType = Literal["ROS", "ROS2"]
RobotSoftwareSuiteVersionTypeType = Literal["Dashing", "Foxy", "Kinetic", "Melodic"]
RobotStatusType = Literal[
    "Available", "Deploying", "Failed", "InSync", "NoResponse", "PendingNewDeployment", "Registered"
]
SimulationJobBatchErrorCodeType = Literal["InternalServiceError"]
SimulationJobBatchStatusType = Literal[
    "Canceled",
    "Canceling",
    "Completed",
    "Completing",
    "Failed",
    "InProgress",
    "Pending",
    "TimedOut",
    "TimingOut",
]
SimulationJobErrorCodeType = Literal[
    "BadPermissionsCloudwatchLogs",
    "BadPermissionsRobotApplication",
    "BadPermissionsS3Object",
    "BadPermissionsS3Output",
    "BadPermissionsSimulationApplication",
    "BadPermissionsUserCredentials",
    "BatchCanceled",
    "BatchTimedOut",
    "ENILimitExceeded",
    "InternalServiceError",
    "InvalidBundleRobotApplication",
    "InvalidBundleSimulationApplication",
    "InvalidInput",
    "InvalidS3Resource",
    "LimitExceeded",
    "MismatchedEtag",
    "RequestThrottled",
    "ResourceNotFound",
    "RobotApplicationCrash",
    "RobotApplicationHealthCheckFailure",
    "RobotApplicationVersionMismatchedEtag",
    "SimulationApplicationCrash",
    "SimulationApplicationHealthCheckFailure",
    "SimulationApplicationVersionMismatchedEtag",
    "SubnetIpLimitExceeded",
    "ThrottlingError",
    "UploadContentMismatchError",
    "WrongRegionRobotApplication",
    "WrongRegionS3Bucket",
    "WrongRegionS3Output",
    "WrongRegionSimulationApplication",
]
SimulationJobStatusType = Literal[
    "Canceled",
    "Completed",
    "Failed",
    "Pending",
    "Preparing",
    "Restarting",
    "Running",
    "RunningFailed",
    "Terminated",
    "Terminating",
]
SimulationSoftwareSuiteTypeType = Literal["Gazebo", "RosbagPlay"]
UploadBehaviorType = Literal["UPLOAD_ON_TERMINATE", "UPLOAD_ROLLING_AUTO_REMOVE"]
WorldExportJobErrorCodeType = Literal[
    "AccessDenied",
    "InternalServiceError",
    "InvalidInput",
    "LimitExceeded",
    "RequestThrottled",
    "ResourceNotFound",
]
WorldExportJobStatusType = Literal[
    "Canceled", "Canceling", "Completed", "Failed", "Pending", "Running"
]
WorldGenerationJobErrorCodeType = Literal[
    "AllWorldGenerationFailed",
    "InternalServiceError",
    "InvalidInput",
    "LimitExceeded",
    "RequestThrottled",
    "ResourceNotFound",
]
WorldGenerationJobStatusType = Literal[
    "Canceled", "Canceling", "Completed", "Failed", "PartialFailed", "Pending", "Running"
]
