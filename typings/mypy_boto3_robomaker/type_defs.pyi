"""
Type annotations for robomaker service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/type_defs.html)

Usage::

    ```python
    from mypy_boto3_robomaker.type_defs import BatchDeleteWorldsRequestRequestTypeDef

    data: BatchDeleteWorldsRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ArchitectureType,
    DeploymentJobErrorCodeType,
    DeploymentStatusType,
    ExitBehaviorType,
    FailureBehaviorType,
    RobotDeploymentStepType,
    RobotSoftwareSuiteTypeType,
    RobotSoftwareSuiteVersionTypeType,
    RobotStatusType,
    SimulationJobBatchStatusType,
    SimulationJobErrorCodeType,
    SimulationJobStatusType,
    SimulationSoftwareSuiteTypeType,
    UploadBehaviorType,
    WorldExportJobErrorCodeType,
    WorldExportJobStatusType,
    WorldGenerationJobErrorCodeType,
    WorldGenerationJobStatusType,
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
    "BatchDeleteWorldsRequestRequestTypeDef",
    "BatchDeleteWorldsResponseTypeDef",
    "BatchDescribeSimulationJobRequestRequestTypeDef",
    "BatchDescribeSimulationJobResponseTypeDef",
    "BatchPolicyTypeDef",
    "CancelDeploymentJobRequestRequestTypeDef",
    "CancelSimulationJobBatchRequestRequestTypeDef",
    "CancelSimulationJobRequestRequestTypeDef",
    "CancelWorldExportJobRequestRequestTypeDef",
    "CancelWorldGenerationJobRequestRequestTypeDef",
    "ComputeResponseTypeDef",
    "ComputeTypeDef",
    "CreateDeploymentJobRequestRequestTypeDef",
    "CreateDeploymentJobResponseTypeDef",
    "CreateFleetRequestRequestTypeDef",
    "CreateFleetResponseTypeDef",
    "CreateRobotApplicationRequestRequestTypeDef",
    "CreateRobotApplicationResponseTypeDef",
    "CreateRobotApplicationVersionRequestRequestTypeDef",
    "CreateRobotApplicationVersionResponseTypeDef",
    "CreateRobotRequestRequestTypeDef",
    "CreateRobotResponseTypeDef",
    "CreateSimulationApplicationRequestRequestTypeDef",
    "CreateSimulationApplicationResponseTypeDef",
    "CreateSimulationApplicationVersionRequestRequestTypeDef",
    "CreateSimulationApplicationVersionResponseTypeDef",
    "CreateSimulationJobRequestRequestTypeDef",
    "CreateSimulationJobResponseTypeDef",
    "CreateWorldExportJobRequestRequestTypeDef",
    "CreateWorldExportJobResponseTypeDef",
    "CreateWorldGenerationJobRequestRequestTypeDef",
    "CreateWorldGenerationJobResponseTypeDef",
    "CreateWorldTemplateRequestRequestTypeDef",
    "CreateWorldTemplateResponseTypeDef",
    "DataSourceConfigTypeDef",
    "DataSourceTypeDef",
    "DeleteFleetRequestRequestTypeDef",
    "DeleteRobotApplicationRequestRequestTypeDef",
    "DeleteRobotRequestRequestTypeDef",
    "DeleteSimulationApplicationRequestRequestTypeDef",
    "DeleteWorldTemplateRequestRequestTypeDef",
    "DeploymentApplicationConfigTypeDef",
    "DeploymentConfigTypeDef",
    "DeploymentJobTypeDef",
    "DeploymentLaunchConfigTypeDef",
    "DeregisterRobotRequestRequestTypeDef",
    "DeregisterRobotResponseTypeDef",
    "DescribeDeploymentJobRequestRequestTypeDef",
    "DescribeDeploymentJobResponseTypeDef",
    "DescribeFleetRequestRequestTypeDef",
    "DescribeFleetResponseTypeDef",
    "DescribeRobotApplicationRequestRequestTypeDef",
    "DescribeRobotApplicationResponseTypeDef",
    "DescribeRobotRequestRequestTypeDef",
    "DescribeRobotResponseTypeDef",
    "DescribeSimulationApplicationRequestRequestTypeDef",
    "DescribeSimulationApplicationResponseTypeDef",
    "DescribeSimulationJobBatchRequestRequestTypeDef",
    "DescribeSimulationJobBatchResponseTypeDef",
    "DescribeSimulationJobRequestRequestTypeDef",
    "DescribeSimulationJobResponseTypeDef",
    "DescribeWorldExportJobRequestRequestTypeDef",
    "DescribeWorldExportJobResponseTypeDef",
    "DescribeWorldGenerationJobRequestRequestTypeDef",
    "DescribeWorldGenerationJobResponseTypeDef",
    "DescribeWorldRequestRequestTypeDef",
    "DescribeWorldResponseTypeDef",
    "DescribeWorldTemplateRequestRequestTypeDef",
    "DescribeWorldTemplateResponseTypeDef",
    "FailedCreateSimulationJobRequestTypeDef",
    "FailureSummaryTypeDef",
    "FilterTypeDef",
    "FinishedWorldsSummaryTypeDef",
    "FleetTypeDef",
    "GetWorldTemplateBodyRequestRequestTypeDef",
    "GetWorldTemplateBodyResponseTypeDef",
    "LaunchConfigTypeDef",
    "ListDeploymentJobsRequestRequestTypeDef",
    "ListDeploymentJobsResponseTypeDef",
    "ListFleetsRequestRequestTypeDef",
    "ListFleetsResponseTypeDef",
    "ListRobotApplicationsRequestRequestTypeDef",
    "ListRobotApplicationsResponseTypeDef",
    "ListRobotsRequestRequestTypeDef",
    "ListRobotsResponseTypeDef",
    "ListSimulationApplicationsRequestRequestTypeDef",
    "ListSimulationApplicationsResponseTypeDef",
    "ListSimulationJobBatchesRequestRequestTypeDef",
    "ListSimulationJobBatchesResponseTypeDef",
    "ListSimulationJobsRequestRequestTypeDef",
    "ListSimulationJobsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorldExportJobsRequestRequestTypeDef",
    "ListWorldExportJobsResponseTypeDef",
    "ListWorldGenerationJobsRequestRequestTypeDef",
    "ListWorldGenerationJobsResponseTypeDef",
    "ListWorldTemplatesRequestRequestTypeDef",
    "ListWorldTemplatesResponseTypeDef",
    "ListWorldsRequestRequestTypeDef",
    "ListWorldsResponseTypeDef",
    "LoggingConfigTypeDef",
    "NetworkInterfaceTypeDef",
    "OutputLocationTypeDef",
    "PaginatorConfigTypeDef",
    "PortForwardingConfigTypeDef",
    "PortMappingTypeDef",
    "ProgressDetailTypeDef",
    "RegisterRobotRequestRequestTypeDef",
    "RegisterRobotResponseTypeDef",
    "RenderingEngineTypeDef",
    "ResponseMetadataTypeDef",
    "RestartSimulationJobRequestRequestTypeDef",
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
    "SourceConfigTypeDef",
    "SourceTypeDef",
    "StartSimulationJobBatchRequestRequestTypeDef",
    "StartSimulationJobBatchResponseTypeDef",
    "SyncDeploymentJobRequestRequestTypeDef",
    "SyncDeploymentJobResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TemplateLocationTypeDef",
    "TemplateSummaryTypeDef",
    "ToolTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateRobotApplicationRequestRequestTypeDef",
    "UpdateRobotApplicationResponseTypeDef",
    "UpdateSimulationApplicationRequestRequestTypeDef",
    "UpdateSimulationApplicationResponseTypeDef",
    "UpdateWorldTemplateRequestRequestTypeDef",
    "UpdateWorldTemplateResponseTypeDef",
    "UploadConfigurationTypeDef",
    "VPCConfigResponseTypeDef",
    "VPCConfigTypeDef",
    "WorldConfigTypeDef",
    "WorldCountTypeDef",
    "WorldExportJobSummaryTypeDef",
    "WorldFailureTypeDef",
    "WorldGenerationJobSummaryTypeDef",
    "WorldSummaryTypeDef",
)

BatchDeleteWorldsRequestRequestTypeDef = TypedDict(
    "BatchDeleteWorldsRequestRequestTypeDef",
    {
        "worlds": List[str],
    },
)

BatchDeleteWorldsResponseTypeDef = TypedDict(
    "BatchDeleteWorldsResponseTypeDef",
    {
        "unprocessedWorlds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDescribeSimulationJobRequestRequestTypeDef = TypedDict(
    "BatchDescribeSimulationJobRequestRequestTypeDef",
    {
        "jobs": List[str],
    },
)

BatchDescribeSimulationJobResponseTypeDef = TypedDict(
    "BatchDescribeSimulationJobResponseTypeDef",
    {
        "jobs": List["SimulationJobTypeDef"],
        "unprocessedJobs": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPolicyTypeDef = TypedDict(
    "BatchPolicyTypeDef",
    {
        "timeoutInSeconds": int,
        "maxConcurrency": int,
    },
    total=False,
)

CancelDeploymentJobRequestRequestTypeDef = TypedDict(
    "CancelDeploymentJobRequestRequestTypeDef",
    {
        "job": str,
    },
)

CancelSimulationJobBatchRequestRequestTypeDef = TypedDict(
    "CancelSimulationJobBatchRequestRequestTypeDef",
    {
        "batch": str,
    },
)

CancelSimulationJobRequestRequestTypeDef = TypedDict(
    "CancelSimulationJobRequestRequestTypeDef",
    {
        "job": str,
    },
)

CancelWorldExportJobRequestRequestTypeDef = TypedDict(
    "CancelWorldExportJobRequestRequestTypeDef",
    {
        "job": str,
    },
)

CancelWorldGenerationJobRequestRequestTypeDef = TypedDict(
    "CancelWorldGenerationJobRequestRequestTypeDef",
    {
        "job": str,
    },
)

ComputeResponseTypeDef = TypedDict(
    "ComputeResponseTypeDef",
    {
        "simulationUnitLimit": int,
    },
    total=False,
)

ComputeTypeDef = TypedDict(
    "ComputeTypeDef",
    {
        "simulationUnitLimit": int,
    },
    total=False,
)

_RequiredCreateDeploymentJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDeploymentJobRequestRequestTypeDef",
    {
        "clientRequestToken": str,
        "fleet": str,
        "deploymentApplicationConfigs": List["DeploymentApplicationConfigTypeDef"],
    },
)
_OptionalCreateDeploymentJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDeploymentJobRequestRequestTypeDef",
    {
        "deploymentConfig": "DeploymentConfigTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateDeploymentJobRequestRequestTypeDef(
    _RequiredCreateDeploymentJobRequestRequestTypeDef,
    _OptionalCreateDeploymentJobRequestRequestTypeDef,
):
    pass

CreateDeploymentJobResponseTypeDef = TypedDict(
    "CreateDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": DeploymentStatusType,
        "deploymentApplicationConfigs": List["DeploymentApplicationConfigTypeDef"],
        "failureReason": str,
        "failureCode": DeploymentJobErrorCodeType,
        "createdAt": datetime,
        "deploymentConfig": "DeploymentConfigTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFleetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFleetRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateFleetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFleetRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateFleetRequestRequestTypeDef(
    _RequiredCreateFleetRequestRequestTypeDef, _OptionalCreateFleetRequestRequestTypeDef
):
    pass

CreateFleetResponseTypeDef = TypedDict(
    "CreateFleetResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRobotApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRobotApplicationRequestRequestTypeDef",
    {
        "name": str,
        "sources": List["SourceConfigTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
    },
)
_OptionalCreateRobotApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRobotApplicationRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateRobotApplicationRequestRequestTypeDef(
    _RequiredCreateRobotApplicationRequestRequestTypeDef,
    _OptionalCreateRobotApplicationRequestRequestTypeDef,
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRobotApplicationVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRobotApplicationVersionRequestRequestTypeDef",
    {
        "application": str,
    },
)
_OptionalCreateRobotApplicationVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRobotApplicationVersionRequestRequestTypeDef",
    {
        "currentRevisionId": str,
    },
    total=False,
)

class CreateRobotApplicationVersionRequestRequestTypeDef(
    _RequiredCreateRobotApplicationVersionRequestRequestTypeDef,
    _OptionalCreateRobotApplicationVersionRequestRequestTypeDef,
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRobotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRobotRequestRequestTypeDef",
    {
        "name": str,
        "architecture": ArchitectureType,
        "greengrassGroupId": str,
    },
)
_OptionalCreateRobotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRobotRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateRobotRequestRequestTypeDef(
    _RequiredCreateRobotRequestRequestTypeDef, _OptionalCreateRobotRequestRequestTypeDef
):
    pass

CreateRobotResponseTypeDef = TypedDict(
    "CreateRobotResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "greengrassGroupId": str,
        "architecture": ArchitectureType,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSimulationApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSimulationApplicationRequestRequestTypeDef",
    {
        "name": str,
        "sources": List["SourceConfigTypeDef"],
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
    },
)
_OptionalCreateSimulationApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSimulationApplicationRequestRequestTypeDef",
    {
        "renderingEngine": "RenderingEngineTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateSimulationApplicationRequestRequestTypeDef(
    _RequiredCreateSimulationApplicationRequestRequestTypeDef,
    _OptionalCreateSimulationApplicationRequestRequestTypeDef,
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSimulationApplicationVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSimulationApplicationVersionRequestRequestTypeDef",
    {
        "application": str,
    },
)
_OptionalCreateSimulationApplicationVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSimulationApplicationVersionRequestRequestTypeDef",
    {
        "currentRevisionId": str,
    },
    total=False,
)

class CreateSimulationApplicationVersionRequestRequestTypeDef(
    _RequiredCreateSimulationApplicationVersionRequestRequestTypeDef,
    _OptionalCreateSimulationApplicationVersionRequestRequestTypeDef,
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSimulationJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSimulationJobRequestRequestTypeDef",
    {
        "maxJobDurationInSeconds": int,
        "iamRole": str,
    },
)
_OptionalCreateSimulationJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSimulationJobRequestRequestTypeDef",
    {
        "clientRequestToken": str,
        "outputLocation": "OutputLocationTypeDef",
        "loggingConfig": "LoggingConfigTypeDef",
        "failureBehavior": FailureBehaviorType,
        "robotApplications": List["RobotApplicationConfigTypeDef"],
        "simulationApplications": List["SimulationApplicationConfigTypeDef"],
        "dataSources": List["DataSourceConfigTypeDef"],
        "tags": Dict[str, str],
        "vpcConfig": "VPCConfigTypeDef",
        "compute": "ComputeTypeDef",
    },
    total=False,
)

class CreateSimulationJobRequestRequestTypeDef(
    _RequiredCreateSimulationJobRequestRequestTypeDef,
    _OptionalCreateSimulationJobRequestRequestTypeDef,
):
    pass

CreateSimulationJobResponseTypeDef = TypedDict(
    "CreateSimulationJobResponseTypeDef",
    {
        "arn": str,
        "status": SimulationJobStatusType,
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": FailureBehaviorType,
        "failureCode": SimulationJobErrorCodeType,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorldExportJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorldExportJobRequestRequestTypeDef",
    {
        "worlds": List[str],
        "outputLocation": "OutputLocationTypeDef",
        "iamRole": str,
    },
)
_OptionalCreateWorldExportJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorldExportJobRequestRequestTypeDef",
    {
        "clientRequestToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateWorldExportJobRequestRequestTypeDef(
    _RequiredCreateWorldExportJobRequestRequestTypeDef,
    _OptionalCreateWorldExportJobRequestRequestTypeDef,
):
    pass

CreateWorldExportJobResponseTypeDef = TypedDict(
    "CreateWorldExportJobResponseTypeDef",
    {
        "arn": str,
        "status": WorldExportJobStatusType,
        "createdAt": datetime,
        "failureCode": WorldExportJobErrorCodeType,
        "clientRequestToken": str,
        "outputLocation": "OutputLocationTypeDef",
        "iamRole": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorldGenerationJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorldGenerationJobRequestRequestTypeDef",
    {
        "template": str,
        "worldCount": "WorldCountTypeDef",
    },
)
_OptionalCreateWorldGenerationJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorldGenerationJobRequestRequestTypeDef",
    {
        "clientRequestToken": str,
        "tags": Dict[str, str],
        "worldTags": Dict[str, str],
    },
    total=False,
)

class CreateWorldGenerationJobRequestRequestTypeDef(
    _RequiredCreateWorldGenerationJobRequestRequestTypeDef,
    _OptionalCreateWorldGenerationJobRequestRequestTypeDef,
):
    pass

CreateWorldGenerationJobResponseTypeDef = TypedDict(
    "CreateWorldGenerationJobResponseTypeDef",
    {
        "arn": str,
        "status": WorldGenerationJobStatusType,
        "createdAt": datetime,
        "failureCode": WorldGenerationJobErrorCodeType,
        "clientRequestToken": str,
        "template": str,
        "worldCount": "WorldCountTypeDef",
        "tags": Dict[str, str],
        "worldTags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorldTemplateRequestRequestTypeDef = TypedDict(
    "CreateWorldTemplateRequestRequestTypeDef",
    {
        "clientRequestToken": str,
        "name": str,
        "templateBody": str,
        "templateLocation": "TemplateLocationTypeDef",
        "tags": Dict[str, str],
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceConfigTypeDef = TypedDict(
    "DataSourceConfigTypeDef",
    {
        "name": str,
        "s3Bucket": str,
        "s3Keys": List[str],
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "name": str,
        "s3Bucket": str,
        "s3Keys": List["S3KeyOutputTypeDef"],
    },
    total=False,
)

DeleteFleetRequestRequestTypeDef = TypedDict(
    "DeleteFleetRequestRequestTypeDef",
    {
        "fleet": str,
    },
)

_RequiredDeleteRobotApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRobotApplicationRequestRequestTypeDef",
    {
        "application": str,
    },
)
_OptionalDeleteRobotApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRobotApplicationRequestRequestTypeDef",
    {
        "applicationVersion": str,
    },
    total=False,
)

class DeleteRobotApplicationRequestRequestTypeDef(
    _RequiredDeleteRobotApplicationRequestRequestTypeDef,
    _OptionalDeleteRobotApplicationRequestRequestTypeDef,
):
    pass

DeleteRobotRequestRequestTypeDef = TypedDict(
    "DeleteRobotRequestRequestTypeDef",
    {
        "robot": str,
    },
)

_RequiredDeleteSimulationApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteSimulationApplicationRequestRequestTypeDef",
    {
        "application": str,
    },
)
_OptionalDeleteSimulationApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteSimulationApplicationRequestRequestTypeDef",
    {
        "applicationVersion": str,
    },
    total=False,
)

class DeleteSimulationApplicationRequestRequestTypeDef(
    _RequiredDeleteSimulationApplicationRequestRequestTypeDef,
    _OptionalDeleteSimulationApplicationRequestRequestTypeDef,
):
    pass

DeleteWorldTemplateRequestRequestTypeDef = TypedDict(
    "DeleteWorldTemplateRequestRequestTypeDef",
    {
        "template": str,
    },
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
        "status": DeploymentStatusType,
        "deploymentApplicationConfigs": List["DeploymentApplicationConfigTypeDef"],
        "deploymentConfig": "DeploymentConfigTypeDef",
        "failureReason": str,
        "failureCode": DeploymentJobErrorCodeType,
        "createdAt": datetime,
    },
    total=False,
)

_RequiredDeploymentLaunchConfigTypeDef = TypedDict(
    "_RequiredDeploymentLaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
    },
)
_OptionalDeploymentLaunchConfigTypeDef = TypedDict(
    "_OptionalDeploymentLaunchConfigTypeDef",
    {
        "preLaunchFile": str,
        "postLaunchFile": str,
        "environmentVariables": Dict[str, str],
    },
    total=False,
)

class DeploymentLaunchConfigTypeDef(
    _RequiredDeploymentLaunchConfigTypeDef, _OptionalDeploymentLaunchConfigTypeDef
):
    pass

DeregisterRobotRequestRequestTypeDef = TypedDict(
    "DeregisterRobotRequestRequestTypeDef",
    {
        "fleet": str,
        "robot": str,
    },
)

DeregisterRobotResponseTypeDef = TypedDict(
    "DeregisterRobotResponseTypeDef",
    {
        "fleet": str,
        "robot": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeploymentJobRequestRequestTypeDef = TypedDict(
    "DescribeDeploymentJobRequestRequestTypeDef",
    {
        "job": str,
    },
)

DescribeDeploymentJobResponseTypeDef = TypedDict(
    "DescribeDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": DeploymentStatusType,
        "deploymentConfig": "DeploymentConfigTypeDef",
        "deploymentApplicationConfigs": List["DeploymentApplicationConfigTypeDef"],
        "failureReason": str,
        "failureCode": DeploymentJobErrorCodeType,
        "createdAt": datetime,
        "robotDeploymentSummary": List["RobotDeploymentTypeDef"],
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetRequestRequestTypeDef = TypedDict(
    "DescribeFleetRequestRequestTypeDef",
    {
        "fleet": str,
    },
)

DescribeFleetResponseTypeDef = TypedDict(
    "DescribeFleetResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "robots": List["RobotTypeDef"],
        "createdAt": datetime,
        "lastDeploymentStatus": DeploymentStatusType,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRobotApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRobotApplicationRequestRequestTypeDef",
    {
        "application": str,
    },
)
_OptionalDescribeRobotApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRobotApplicationRequestRequestTypeDef",
    {
        "applicationVersion": str,
    },
    total=False,
)

class DescribeRobotApplicationRequestRequestTypeDef(
    _RequiredDescribeRobotApplicationRequestRequestTypeDef,
    _OptionalDescribeRobotApplicationRequestRequestTypeDef,
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRobotRequestRequestTypeDef = TypedDict(
    "DescribeRobotRequestRequestTypeDef",
    {
        "robot": str,
    },
)

DescribeRobotResponseTypeDef = TypedDict(
    "DescribeRobotResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": RobotStatusType,
        "greengrassGroupId": str,
        "createdAt": datetime,
        "architecture": ArchitectureType,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSimulationApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeSimulationApplicationRequestRequestTypeDef",
    {
        "application": str,
    },
)
_OptionalDescribeSimulationApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeSimulationApplicationRequestRequestTypeDef",
    {
        "applicationVersion": str,
    },
    total=False,
)

class DescribeSimulationApplicationRequestRequestTypeDef(
    _RequiredDescribeSimulationApplicationRequestRequestTypeDef,
    _OptionalDescribeSimulationApplicationRequestRequestTypeDef,
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSimulationJobBatchRequestRequestTypeDef = TypedDict(
    "DescribeSimulationJobBatchRequestRequestTypeDef",
    {
        "batch": str,
    },
)

DescribeSimulationJobBatchResponseTypeDef = TypedDict(
    "DescribeSimulationJobBatchResponseTypeDef",
    {
        "arn": str,
        "status": SimulationJobBatchStatusType,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSimulationJobRequestRequestTypeDef = TypedDict(
    "DescribeSimulationJobRequestRequestTypeDef",
    {
        "job": str,
    },
)

DescribeSimulationJobResponseTypeDef = TypedDict(
    "DescribeSimulationJobResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "status": SimulationJobStatusType,
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": FailureBehaviorType,
        "failureCode": SimulationJobErrorCodeType,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorldExportJobRequestRequestTypeDef = TypedDict(
    "DescribeWorldExportJobRequestRequestTypeDef",
    {
        "job": str,
    },
)

DescribeWorldExportJobResponseTypeDef = TypedDict(
    "DescribeWorldExportJobResponseTypeDef",
    {
        "arn": str,
        "status": WorldExportJobStatusType,
        "createdAt": datetime,
        "failureCode": WorldExportJobErrorCodeType,
        "failureReason": str,
        "clientRequestToken": str,
        "worlds": List[str],
        "outputLocation": "OutputLocationTypeDef",
        "iamRole": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorldGenerationJobRequestRequestTypeDef = TypedDict(
    "DescribeWorldGenerationJobRequestRequestTypeDef",
    {
        "job": str,
    },
)

DescribeWorldGenerationJobResponseTypeDef = TypedDict(
    "DescribeWorldGenerationJobResponseTypeDef",
    {
        "arn": str,
        "status": WorldGenerationJobStatusType,
        "createdAt": datetime,
        "failureCode": WorldGenerationJobErrorCodeType,
        "failureReason": str,
        "clientRequestToken": str,
        "template": str,
        "worldCount": "WorldCountTypeDef",
        "finishedWorldsSummary": "FinishedWorldsSummaryTypeDef",
        "tags": Dict[str, str],
        "worldTags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorldRequestRequestTypeDef = TypedDict(
    "DescribeWorldRequestRequestTypeDef",
    {
        "world": str,
    },
)

DescribeWorldResponseTypeDef = TypedDict(
    "DescribeWorldResponseTypeDef",
    {
        "arn": str,
        "generationJob": str,
        "template": str,
        "createdAt": datetime,
        "tags": Dict[str, str],
        "worldDescriptionBody": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorldTemplateRequestRequestTypeDef = TypedDict(
    "DescribeWorldTemplateRequestRequestTypeDef",
    {
        "template": str,
    },
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
        "version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailedCreateSimulationJobRequestTypeDef = TypedDict(
    "FailedCreateSimulationJobRequestTypeDef",
    {
        "request": "SimulationJobRequestTypeDef",
        "failureReason": str,
        "failureCode": SimulationJobErrorCodeType,
        "failedAt": datetime,
    },
    total=False,
)

FailureSummaryTypeDef = TypedDict(
    "FailureSummaryTypeDef",
    {
        "totalFailureCount": int,
        "failures": List["WorldFailureTypeDef"],
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": str,
        "values": List[str],
    },
    total=False,
)

FinishedWorldsSummaryTypeDef = TypedDict(
    "FinishedWorldsSummaryTypeDef",
    {
        "finishedCount": int,
        "succeededWorlds": List[str],
        "failureSummary": "FailureSummaryTypeDef",
    },
    total=False,
)

FleetTypeDef = TypedDict(
    "FleetTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "lastDeploymentStatus": DeploymentStatusType,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)

GetWorldTemplateBodyRequestRequestTypeDef = TypedDict(
    "GetWorldTemplateBodyRequestRequestTypeDef",
    {
        "template": str,
        "generationJob": str,
    },
    total=False,
)

GetWorldTemplateBodyResponseTypeDef = TypedDict(
    "GetWorldTemplateBodyResponseTypeDef",
    {
        "templateBody": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLaunchConfigTypeDef = TypedDict(
    "_RequiredLaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
    },
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

ListDeploymentJobsRequestRequestTypeDef = TypedDict(
    "ListDeploymentJobsRequestRequestTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDeploymentJobsResponseTypeDef = TypedDict(
    "ListDeploymentJobsResponseTypeDef",
    {
        "deploymentJobs": List["DeploymentJobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFleetsRequestRequestTypeDef = TypedDict(
    "ListFleetsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
    },
    total=False,
)

ListFleetsResponseTypeDef = TypedDict(
    "ListFleetsResponseTypeDef",
    {
        "fleetDetails": List["FleetTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRobotApplicationsRequestRequestTypeDef = TypedDict(
    "ListRobotApplicationsRequestRequestTypeDef",
    {
        "versionQualifier": str,
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
    },
    total=False,
)

ListRobotApplicationsResponseTypeDef = TypedDict(
    "ListRobotApplicationsResponseTypeDef",
    {
        "robotApplicationSummaries": List["RobotApplicationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRobotsRequestRequestTypeDef = TypedDict(
    "ListRobotsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
    },
    total=False,
)

ListRobotsResponseTypeDef = TypedDict(
    "ListRobotsResponseTypeDef",
    {
        "robots": List["RobotTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSimulationApplicationsRequestRequestTypeDef = TypedDict(
    "ListSimulationApplicationsRequestRequestTypeDef",
    {
        "versionQualifier": str,
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
    },
    total=False,
)

ListSimulationApplicationsResponseTypeDef = TypedDict(
    "ListSimulationApplicationsResponseTypeDef",
    {
        "simulationApplicationSummaries": List["SimulationApplicationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSimulationJobBatchesRequestRequestTypeDef = TypedDict(
    "ListSimulationJobBatchesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
    },
    total=False,
)

ListSimulationJobBatchesResponseTypeDef = TypedDict(
    "ListSimulationJobBatchesResponseTypeDef",
    {
        "simulationJobBatchSummaries": List["SimulationJobBatchSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSimulationJobsRequestRequestTypeDef = TypedDict(
    "ListSimulationJobsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
    },
    total=False,
)

ListSimulationJobsResponseTypeDef = TypedDict(
    "ListSimulationJobsResponseTypeDef",
    {
        "simulationJobSummaries": List["SimulationJobSummaryTypeDef"],
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

ListWorldExportJobsRequestRequestTypeDef = TypedDict(
    "ListWorldExportJobsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
    },
    total=False,
)

ListWorldExportJobsResponseTypeDef = TypedDict(
    "ListWorldExportJobsResponseTypeDef",
    {
        "worldExportJobSummaries": List["WorldExportJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorldGenerationJobsRequestRequestTypeDef = TypedDict(
    "ListWorldGenerationJobsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
    },
    total=False,
)

ListWorldGenerationJobsResponseTypeDef = TypedDict(
    "ListWorldGenerationJobsResponseTypeDef",
    {
        "worldGenerationJobSummaries": List["WorldGenerationJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorldTemplatesRequestRequestTypeDef = TypedDict(
    "ListWorldTemplatesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListWorldTemplatesResponseTypeDef = TypedDict(
    "ListWorldTemplatesResponseTypeDef",
    {
        "templateSummaries": List["TemplateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorldsRequestRequestTypeDef = TypedDict(
    "ListWorldsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
    },
    total=False,
)

ListWorldsResponseTypeDef = TypedDict(
    "ListWorldsResponseTypeDef",
    {
        "worldSummaries": List["WorldSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingConfigTypeDef = TypedDict(
    "LoggingConfigTypeDef",
    {
        "recordAllRosTopics": bool,
    },
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "networkInterfaceId": str,
        "privateIpAddress": str,
        "publicIpAddress": str,
    },
    total=False,
)

OutputLocationTypeDef = TypedDict(
    "OutputLocationTypeDef",
    {
        "s3Bucket": str,
        "s3Prefix": str,
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

PortForwardingConfigTypeDef = TypedDict(
    "PortForwardingConfigTypeDef",
    {
        "portMappings": List["PortMappingTypeDef"],
    },
    total=False,
)

_RequiredPortMappingTypeDef = TypedDict(
    "_RequiredPortMappingTypeDef",
    {
        "jobPort": int,
        "applicationPort": int,
    },
)
_OptionalPortMappingTypeDef = TypedDict(
    "_OptionalPortMappingTypeDef",
    {
        "enableOnPublicIp": bool,
    },
    total=False,
)

class PortMappingTypeDef(_RequiredPortMappingTypeDef, _OptionalPortMappingTypeDef):
    pass

ProgressDetailTypeDef = TypedDict(
    "ProgressDetailTypeDef",
    {
        "currentProgress": RobotDeploymentStepType,
        "percentDone": float,
        "estimatedTimeRemainingSeconds": int,
        "targetResource": str,
    },
    total=False,
)

RegisterRobotRequestRequestTypeDef = TypedDict(
    "RegisterRobotRequestRequestTypeDef",
    {
        "fleet": str,
        "robot": str,
    },
)

RegisterRobotResponseTypeDef = TypedDict(
    "RegisterRobotResponseTypeDef",
    {
        "fleet": str,
        "robot": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RenderingEngineTypeDef = TypedDict(
    "RenderingEngineTypeDef",
    {
        "name": Literal["OGRE"],
        "version": str,
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

RestartSimulationJobRequestRequestTypeDef = TypedDict(
    "RestartSimulationJobRequestRequestTypeDef",
    {
        "job": str,
    },
)

_RequiredRobotApplicationConfigTypeDef = TypedDict(
    "_RequiredRobotApplicationConfigTypeDef",
    {
        "application": str,
        "launchConfig": "LaunchConfigTypeDef",
    },
)
_OptionalRobotApplicationConfigTypeDef = TypedDict(
    "_OptionalRobotApplicationConfigTypeDef",
    {
        "applicationVersion": str,
        "uploadConfigurations": List["UploadConfigurationTypeDef"],
        "useDefaultUploadConfigurations": bool,
        "tools": List["ToolTypeDef"],
        "useDefaultTools": bool,
    },
    total=False,
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
        "status": RobotStatusType,
        "progressDetail": "ProgressDetailTypeDef",
        "failureReason": str,
        "failureCode": DeploymentJobErrorCodeType,
    },
    total=False,
)

RobotSoftwareSuiteTypeDef = TypedDict(
    "RobotSoftwareSuiteTypeDef",
    {
        "name": RobotSoftwareSuiteTypeType,
        "version": RobotSoftwareSuiteVersionTypeType,
    },
    total=False,
)

RobotTypeDef = TypedDict(
    "RobotTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": RobotStatusType,
        "greenGrassGroupId": str,
        "createdAt": datetime,
        "architecture": ArchitectureType,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)

S3KeyOutputTypeDef = TypedDict(
    "S3KeyOutputTypeDef",
    {
        "s3Key": str,
        "etag": str,
    },
    total=False,
)

_RequiredS3ObjectTypeDef = TypedDict(
    "_RequiredS3ObjectTypeDef",
    {
        "bucket": str,
        "key": str,
    },
)
_OptionalS3ObjectTypeDef = TypedDict(
    "_OptionalS3ObjectTypeDef",
    {
        "etag": str,
    },
    total=False,
)

class S3ObjectTypeDef(_RequiredS3ObjectTypeDef, _OptionalS3ObjectTypeDef):
    pass

_RequiredSimulationApplicationConfigTypeDef = TypedDict(
    "_RequiredSimulationApplicationConfigTypeDef",
    {
        "application": str,
        "launchConfig": "LaunchConfigTypeDef",
    },
)
_OptionalSimulationApplicationConfigTypeDef = TypedDict(
    "_OptionalSimulationApplicationConfigTypeDef",
    {
        "applicationVersion": str,
        "uploadConfigurations": List["UploadConfigurationTypeDef"],
        "worldConfigs": List["WorldConfigTypeDef"],
        "useDefaultUploadConfigurations": bool,
        "tools": List["ToolTypeDef"],
        "useDefaultTools": bool,
    },
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
        "status": SimulationJobBatchStatusType,
        "failedRequestCount": int,
        "pendingRequestCount": int,
        "createdRequestCount": int,
    },
    total=False,
)

_RequiredSimulationJobRequestTypeDef = TypedDict(
    "_RequiredSimulationJobRequestTypeDef",
    {
        "maxJobDurationInSeconds": int,
    },
)
_OptionalSimulationJobRequestTypeDef = TypedDict(
    "_OptionalSimulationJobRequestTypeDef",
    {
        "outputLocation": "OutputLocationTypeDef",
        "loggingConfig": "LoggingConfigTypeDef",
        "iamRole": str,
        "failureBehavior": FailureBehaviorType,
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
        "status": SimulationJobStatusType,
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
        "status": SimulationJobStatusType,
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": FailureBehaviorType,
        "failureCode": SimulationJobErrorCodeType,
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
    {
        "name": SimulationSoftwareSuiteTypeType,
        "version": str,
    },
    total=False,
)

SourceConfigTypeDef = TypedDict(
    "SourceConfigTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "architecture": ArchitectureType,
    },
    total=False,
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": ArchitectureType,
    },
    total=False,
)

_RequiredStartSimulationJobBatchRequestRequestTypeDef = TypedDict(
    "_RequiredStartSimulationJobBatchRequestRequestTypeDef",
    {
        "createSimulationJobRequests": List["SimulationJobRequestTypeDef"],
    },
)
_OptionalStartSimulationJobBatchRequestRequestTypeDef = TypedDict(
    "_OptionalStartSimulationJobBatchRequestRequestTypeDef",
    {
        "clientRequestToken": str,
        "batchPolicy": "BatchPolicyTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class StartSimulationJobBatchRequestRequestTypeDef(
    _RequiredStartSimulationJobBatchRequestRequestTypeDef,
    _OptionalStartSimulationJobBatchRequestRequestTypeDef,
):
    pass

StartSimulationJobBatchResponseTypeDef = TypedDict(
    "StartSimulationJobBatchResponseTypeDef",
    {
        "arn": str,
        "status": SimulationJobBatchStatusType,
        "createdAt": datetime,
        "clientRequestToken": str,
        "batchPolicy": "BatchPolicyTypeDef",
        "failureCode": Literal["InternalServiceError"],
        "failureReason": str,
        "failedRequests": List["FailedCreateSimulationJobRequestTypeDef"],
        "pendingRequests": List["SimulationJobRequestTypeDef"],
        "createdRequests": List["SimulationJobSummaryTypeDef"],
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SyncDeploymentJobRequestRequestTypeDef = TypedDict(
    "SyncDeploymentJobRequestRequestTypeDef",
    {
        "clientRequestToken": str,
        "fleet": str,
    },
)

SyncDeploymentJobResponseTypeDef = TypedDict(
    "SyncDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": DeploymentStatusType,
        "deploymentConfig": "DeploymentConfigTypeDef",
        "deploymentApplicationConfigs": List["DeploymentApplicationConfigTypeDef"],
        "failureReason": str,
        "failureCode": DeploymentJobErrorCodeType,
        "createdAt": datetime,
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

TemplateLocationTypeDef = TypedDict(
    "TemplateLocationTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
    },
)

TemplateSummaryTypeDef = TypedDict(
    "TemplateSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "name": str,
        "version": str,
    },
    total=False,
)

_RequiredToolTypeDef = TypedDict(
    "_RequiredToolTypeDef",
    {
        "name": str,
        "command": str,
    },
)
_OptionalToolTypeDef = TypedDict(
    "_OptionalToolTypeDef",
    {
        "streamUI": bool,
        "streamOutputToCloudWatch": bool,
        "exitBehavior": ExitBehaviorType,
    },
    total=False,
)

class ToolTypeDef(_RequiredToolTypeDef, _OptionalToolTypeDef):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateRobotApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRobotApplicationRequestRequestTypeDef",
    {
        "application": str,
        "sources": List["SourceConfigTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
    },
)
_OptionalUpdateRobotApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRobotApplicationRequestRequestTypeDef",
    {
        "currentRevisionId": str,
    },
    total=False,
)

class UpdateRobotApplicationRequestRequestTypeDef(
    _RequiredUpdateRobotApplicationRequestRequestTypeDef,
    _OptionalUpdateRobotApplicationRequestRequestTypeDef,
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSimulationApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSimulationApplicationRequestRequestTypeDef",
    {
        "application": str,
        "sources": List["SourceConfigTypeDef"],
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
    },
)
_OptionalUpdateSimulationApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSimulationApplicationRequestRequestTypeDef",
    {
        "renderingEngine": "RenderingEngineTypeDef",
        "currentRevisionId": str,
    },
    total=False,
)

class UpdateSimulationApplicationRequestRequestTypeDef(
    _RequiredUpdateSimulationApplicationRequestRequestTypeDef,
    _OptionalUpdateSimulationApplicationRequestRequestTypeDef,
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWorldTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWorldTemplateRequestRequestTypeDef",
    {
        "template": str,
    },
)
_OptionalUpdateWorldTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWorldTemplateRequestRequestTypeDef",
    {
        "name": str,
        "templateBody": str,
        "templateLocation": "TemplateLocationTypeDef",
    },
    total=False,
)

class UpdateWorldTemplateRequestRequestTypeDef(
    _RequiredUpdateWorldTemplateRequestRequestTypeDef,
    _OptionalUpdateWorldTemplateRequestRequestTypeDef,
):
    pass

UpdateWorldTemplateResponseTypeDef = TypedDict(
    "UpdateWorldTemplateResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UploadConfigurationTypeDef = TypedDict(
    "UploadConfigurationTypeDef",
    {
        "name": str,
        "path": str,
        "uploadBehavior": UploadBehaviorType,
    },
)

VPCConfigResponseTypeDef = TypedDict(
    "VPCConfigResponseTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "vpcId": str,
        "assignPublicIp": bool,
    },
    total=False,
)

_RequiredVPCConfigTypeDef = TypedDict(
    "_RequiredVPCConfigTypeDef",
    {
        "subnets": List[str],
    },
)
_OptionalVPCConfigTypeDef = TypedDict(
    "_OptionalVPCConfigTypeDef",
    {
        "securityGroups": List[str],
        "assignPublicIp": bool,
    },
    total=False,
)

class VPCConfigTypeDef(_RequiredVPCConfigTypeDef, _OptionalVPCConfigTypeDef):
    pass

WorldConfigTypeDef = TypedDict(
    "WorldConfigTypeDef",
    {
        "world": str,
    },
    total=False,
)

WorldCountTypeDef = TypedDict(
    "WorldCountTypeDef",
    {
        "floorplanCount": int,
        "interiorCountPerFloorplan": int,
    },
    total=False,
)

WorldExportJobSummaryTypeDef = TypedDict(
    "WorldExportJobSummaryTypeDef",
    {
        "arn": str,
        "status": WorldExportJobStatusType,
        "createdAt": datetime,
        "worlds": List[str],
    },
    total=False,
)

WorldFailureTypeDef = TypedDict(
    "WorldFailureTypeDef",
    {
        "failureCode": WorldGenerationJobErrorCodeType,
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
        "status": WorldGenerationJobStatusType,
        "worldCount": "WorldCountTypeDef",
        "succeededWorldCount": int,
        "failedWorldCount": int,
    },
    total=False,
)

WorldSummaryTypeDef = TypedDict(
    "WorldSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "generationJob": str,
        "template": str,
    },
    total=False,
)
