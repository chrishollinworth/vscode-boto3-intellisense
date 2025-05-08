"""
Type annotations for robomaker service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_robomaker.type_defs import BatchDeleteWorldsRequestTypeDef

    data: BatchDeleteWorldsRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ArchitectureType,
    ComputeTypeType,
    DataSourceTypeType,
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
    "BatchDeleteWorldsRequestTypeDef",
    "BatchDeleteWorldsResponseTypeDef",
    "BatchDescribeSimulationJobRequestTypeDef",
    "BatchDescribeSimulationJobResponseTypeDef",
    "BatchPolicyTypeDef",
    "CancelDeploymentJobRequestTypeDef",
    "CancelSimulationJobBatchRequestTypeDef",
    "CancelSimulationJobRequestTypeDef",
    "CancelWorldExportJobRequestTypeDef",
    "CancelWorldGenerationJobRequestTypeDef",
    "ComputeResponseTypeDef",
    "ComputeTypeDef",
    "CreateDeploymentJobRequestTypeDef",
    "CreateDeploymentJobResponseTypeDef",
    "CreateFleetRequestTypeDef",
    "CreateFleetResponseTypeDef",
    "CreateRobotApplicationRequestTypeDef",
    "CreateRobotApplicationResponseTypeDef",
    "CreateRobotApplicationVersionRequestTypeDef",
    "CreateRobotApplicationVersionResponseTypeDef",
    "CreateRobotRequestTypeDef",
    "CreateRobotResponseTypeDef",
    "CreateSimulationApplicationRequestTypeDef",
    "CreateSimulationApplicationResponseTypeDef",
    "CreateSimulationApplicationVersionRequestTypeDef",
    "CreateSimulationApplicationVersionResponseTypeDef",
    "CreateSimulationJobRequestTypeDef",
    "CreateSimulationJobResponseTypeDef",
    "CreateWorldExportJobRequestTypeDef",
    "CreateWorldExportJobResponseTypeDef",
    "CreateWorldGenerationJobRequestTypeDef",
    "CreateWorldGenerationJobResponseTypeDef",
    "CreateWorldTemplateRequestTypeDef",
    "CreateWorldTemplateResponseTypeDef",
    "DataSourceConfigOutputTypeDef",
    "DataSourceConfigTypeDef",
    "DataSourceConfigUnionTypeDef",
    "DataSourceTypeDef",
    "DeleteFleetRequestTypeDef",
    "DeleteRobotApplicationRequestTypeDef",
    "DeleteRobotRequestTypeDef",
    "DeleteSimulationApplicationRequestTypeDef",
    "DeleteWorldTemplateRequestTypeDef",
    "DeploymentApplicationConfigOutputTypeDef",
    "DeploymentApplicationConfigTypeDef",
    "DeploymentApplicationConfigUnionTypeDef",
    "DeploymentConfigTypeDef",
    "DeploymentJobTypeDef",
    "DeploymentLaunchConfigOutputTypeDef",
    "DeploymentLaunchConfigTypeDef",
    "DeploymentLaunchConfigUnionTypeDef",
    "DeregisterRobotRequestTypeDef",
    "DeregisterRobotResponseTypeDef",
    "DescribeDeploymentJobRequestTypeDef",
    "DescribeDeploymentJobResponseTypeDef",
    "DescribeFleetRequestTypeDef",
    "DescribeFleetResponseTypeDef",
    "DescribeRobotApplicationRequestTypeDef",
    "DescribeRobotApplicationResponseTypeDef",
    "DescribeRobotRequestTypeDef",
    "DescribeRobotResponseTypeDef",
    "DescribeSimulationApplicationRequestTypeDef",
    "DescribeSimulationApplicationResponseTypeDef",
    "DescribeSimulationJobBatchRequestTypeDef",
    "DescribeSimulationJobBatchResponseTypeDef",
    "DescribeSimulationJobRequestTypeDef",
    "DescribeSimulationJobResponseTypeDef",
    "DescribeWorldExportJobRequestTypeDef",
    "DescribeWorldExportJobResponseTypeDef",
    "DescribeWorldGenerationJobRequestTypeDef",
    "DescribeWorldGenerationJobResponseTypeDef",
    "DescribeWorldRequestTypeDef",
    "DescribeWorldResponseTypeDef",
    "DescribeWorldTemplateRequestTypeDef",
    "DescribeWorldTemplateResponseTypeDef",
    "EnvironmentTypeDef",
    "FailedCreateSimulationJobRequestTypeDef",
    "FailureSummaryTypeDef",
    "FilterTypeDef",
    "FinishedWorldsSummaryTypeDef",
    "FleetTypeDef",
    "GetWorldTemplateBodyRequestTypeDef",
    "GetWorldTemplateBodyResponseTypeDef",
    "LaunchConfigOutputTypeDef",
    "LaunchConfigTypeDef",
    "LaunchConfigUnionTypeDef",
    "ListDeploymentJobsRequestPaginateTypeDef",
    "ListDeploymentJobsRequestTypeDef",
    "ListDeploymentJobsResponseTypeDef",
    "ListFleetsRequestPaginateTypeDef",
    "ListFleetsRequestTypeDef",
    "ListFleetsResponseTypeDef",
    "ListRobotApplicationsRequestPaginateTypeDef",
    "ListRobotApplicationsRequestTypeDef",
    "ListRobotApplicationsResponseTypeDef",
    "ListRobotsRequestPaginateTypeDef",
    "ListRobotsRequestTypeDef",
    "ListRobotsResponseTypeDef",
    "ListSimulationApplicationsRequestPaginateTypeDef",
    "ListSimulationApplicationsRequestTypeDef",
    "ListSimulationApplicationsResponseTypeDef",
    "ListSimulationJobBatchesRequestPaginateTypeDef",
    "ListSimulationJobBatchesRequestTypeDef",
    "ListSimulationJobBatchesResponseTypeDef",
    "ListSimulationJobsRequestPaginateTypeDef",
    "ListSimulationJobsRequestTypeDef",
    "ListSimulationJobsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorldExportJobsRequestPaginateTypeDef",
    "ListWorldExportJobsRequestTypeDef",
    "ListWorldExportJobsResponseTypeDef",
    "ListWorldGenerationJobsRequestPaginateTypeDef",
    "ListWorldGenerationJobsRequestTypeDef",
    "ListWorldGenerationJobsResponseTypeDef",
    "ListWorldTemplatesRequestPaginateTypeDef",
    "ListWorldTemplatesRequestTypeDef",
    "ListWorldTemplatesResponseTypeDef",
    "ListWorldsRequestPaginateTypeDef",
    "ListWorldsRequestTypeDef",
    "ListWorldsResponseTypeDef",
    "LoggingConfigTypeDef",
    "NetworkInterfaceTypeDef",
    "OutputLocationTypeDef",
    "PaginatorConfigTypeDef",
    "PortForwardingConfigOutputTypeDef",
    "PortForwardingConfigTypeDef",
    "PortForwardingConfigUnionTypeDef",
    "PortMappingTypeDef",
    "ProgressDetailTypeDef",
    "RegisterRobotRequestTypeDef",
    "RegisterRobotResponseTypeDef",
    "RenderingEngineTypeDef",
    "ResponseMetadataTypeDef",
    "RestartSimulationJobRequestTypeDef",
    "RobotApplicationConfigOutputTypeDef",
    "RobotApplicationConfigTypeDef",
    "RobotApplicationConfigUnionTypeDef",
    "RobotApplicationSummaryTypeDef",
    "RobotDeploymentTypeDef",
    "RobotSoftwareSuiteTypeDef",
    "RobotTypeDef",
    "S3KeyOutputTypeDef",
    "S3ObjectTypeDef",
    "SimulationApplicationConfigOutputTypeDef",
    "SimulationApplicationConfigTypeDef",
    "SimulationApplicationConfigUnionTypeDef",
    "SimulationApplicationSummaryTypeDef",
    "SimulationJobBatchSummaryTypeDef",
    "SimulationJobRequestOutputTypeDef",
    "SimulationJobRequestTypeDef",
    "SimulationJobRequestUnionTypeDef",
    "SimulationJobSummaryTypeDef",
    "SimulationJobTypeDef",
    "SimulationSoftwareSuiteTypeDef",
    "SourceConfigTypeDef",
    "SourceTypeDef",
    "StartSimulationJobBatchRequestTypeDef",
    "StartSimulationJobBatchResponseTypeDef",
    "SyncDeploymentJobRequestTypeDef",
    "SyncDeploymentJobResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TemplateLocationTypeDef",
    "TemplateSummaryTypeDef",
    "ToolTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateRobotApplicationRequestTypeDef",
    "UpdateRobotApplicationResponseTypeDef",
    "UpdateSimulationApplicationRequestTypeDef",
    "UpdateSimulationApplicationResponseTypeDef",
    "UpdateWorldTemplateRequestTypeDef",
    "UpdateWorldTemplateResponseTypeDef",
    "UploadConfigurationTypeDef",
    "VPCConfigOutputTypeDef",
    "VPCConfigResponseTypeDef",
    "VPCConfigTypeDef",
    "VPCConfigUnionTypeDef",
    "WorldConfigTypeDef",
    "WorldCountTypeDef",
    "WorldExportJobSummaryTypeDef",
    "WorldFailureTypeDef",
    "WorldGenerationJobSummaryTypeDef",
    "WorldSummaryTypeDef",
)

class BatchDeleteWorldsRequestTypeDef(TypedDict):
    worlds: Sequence[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BatchDescribeSimulationJobRequestTypeDef(TypedDict):
    jobs: Sequence[str]

class BatchPolicyTypeDef(TypedDict):
    timeoutInSeconds: NotRequired[int]
    maxConcurrency: NotRequired[int]

class CancelDeploymentJobRequestTypeDef(TypedDict):
    job: str

class CancelSimulationJobBatchRequestTypeDef(TypedDict):
    batch: str

class CancelSimulationJobRequestTypeDef(TypedDict):
    job: str

class CancelWorldExportJobRequestTypeDef(TypedDict):
    job: str

class CancelWorldGenerationJobRequestTypeDef(TypedDict):
    job: str

class ComputeResponseTypeDef(TypedDict):
    simulationUnitLimit: NotRequired[int]
    computeType: NotRequired[ComputeTypeType]
    gpuUnitLimit: NotRequired[int]

class ComputeTypeDef(TypedDict):
    simulationUnitLimit: NotRequired[int]
    computeType: NotRequired[ComputeTypeType]
    gpuUnitLimit: NotRequired[int]

class CreateFleetRequestTypeDef(TypedDict):
    name: str
    tags: NotRequired[Mapping[str, str]]

class EnvironmentTypeDef(TypedDict):
    uri: NotRequired[str]

class RobotSoftwareSuiteTypeDef(TypedDict):
    name: NotRequired[RobotSoftwareSuiteTypeType]
    version: NotRequired[RobotSoftwareSuiteVersionTypeType]

class SourceConfigTypeDef(TypedDict):
    s3Bucket: NotRequired[str]
    s3Key: NotRequired[str]
    architecture: NotRequired[ArchitectureType]

class SourceTypeDef(TypedDict):
    s3Bucket: NotRequired[str]
    s3Key: NotRequired[str]
    etag: NotRequired[str]
    architecture: NotRequired[ArchitectureType]

class CreateRobotApplicationVersionRequestTypeDef(TypedDict):
    application: str
    currentRevisionId: NotRequired[str]
    s3Etags: NotRequired[Sequence[str]]
    imageDigest: NotRequired[str]

class CreateRobotRequestTypeDef(TypedDict):
    name: str
    architecture: ArchitectureType
    greengrassGroupId: str
    tags: NotRequired[Mapping[str, str]]

class RenderingEngineTypeDef(TypedDict):
    name: NotRequired[Literal["OGRE"]]
    version: NotRequired[str]

class SimulationSoftwareSuiteTypeDef(TypedDict):
    name: NotRequired[SimulationSoftwareSuiteTypeType]
    version: NotRequired[str]

class CreateSimulationApplicationVersionRequestTypeDef(TypedDict):
    application: str
    currentRevisionId: NotRequired[str]
    s3Etags: NotRequired[Sequence[str]]
    imageDigest: NotRequired[str]

class LoggingConfigTypeDef(TypedDict):
    recordAllRosTopics: NotRequired[bool]

class OutputLocationTypeDef(TypedDict):
    s3Bucket: NotRequired[str]
    s3Prefix: NotRequired[str]

class VPCConfigResponseTypeDef(TypedDict):
    subnets: NotRequired[List[str]]
    securityGroups: NotRequired[List[str]]
    vpcId: NotRequired[str]
    assignPublicIp: NotRequired[bool]

class WorldCountTypeDef(TypedDict):
    floorplanCount: NotRequired[int]
    interiorCountPerFloorplan: NotRequired[int]

class TemplateLocationTypeDef(TypedDict):
    s3Bucket: str
    s3Key: str

DataSourceConfigOutputTypeDef = TypedDict(
    "DataSourceConfigOutputTypeDef",
    {
        "name": str,
        "s3Bucket": str,
        "s3Keys": List[str],
        "type": NotRequired[DataSourceTypeType],
        "destination": NotRequired[str],
    },
)
DataSourceConfigTypeDef = TypedDict(
    "DataSourceConfigTypeDef",
    {
        "name": str,
        "s3Bucket": str,
        "s3Keys": Sequence[str],
        "type": NotRequired[DataSourceTypeType],
        "destination": NotRequired[str],
    },
)

class S3KeyOutputTypeDef(TypedDict):
    s3Key: NotRequired[str]
    etag: NotRequired[str]

class DeleteFleetRequestTypeDef(TypedDict):
    fleet: str

class DeleteRobotApplicationRequestTypeDef(TypedDict):
    application: str
    applicationVersion: NotRequired[str]

class DeleteRobotRequestTypeDef(TypedDict):
    robot: str

class DeleteSimulationApplicationRequestTypeDef(TypedDict):
    application: str
    applicationVersion: NotRequired[str]

class DeleteWorldTemplateRequestTypeDef(TypedDict):
    template: str

class DeploymentLaunchConfigOutputTypeDef(TypedDict):
    packageName: str
    launchFile: str
    preLaunchFile: NotRequired[str]
    postLaunchFile: NotRequired[str]
    environmentVariables: NotRequired[Dict[str, str]]

class S3ObjectTypeDef(TypedDict):
    bucket: str
    key: str
    etag: NotRequired[str]

class DeploymentLaunchConfigTypeDef(TypedDict):
    packageName: str
    launchFile: str
    preLaunchFile: NotRequired[str]
    postLaunchFile: NotRequired[str]
    environmentVariables: NotRequired[Mapping[str, str]]

class DeregisterRobotRequestTypeDef(TypedDict):
    fleet: str
    robot: str

class DescribeDeploymentJobRequestTypeDef(TypedDict):
    job: str

class DescribeFleetRequestTypeDef(TypedDict):
    fleet: str

class RobotTypeDef(TypedDict):
    arn: NotRequired[str]
    name: NotRequired[str]
    fleetArn: NotRequired[str]
    status: NotRequired[RobotStatusType]
    greenGrassGroupId: NotRequired[str]
    createdAt: NotRequired[datetime]
    architecture: NotRequired[ArchitectureType]
    lastDeploymentJob: NotRequired[str]
    lastDeploymentTime: NotRequired[datetime]

class DescribeRobotApplicationRequestTypeDef(TypedDict):
    application: str
    applicationVersion: NotRequired[str]

class DescribeRobotRequestTypeDef(TypedDict):
    robot: str

class DescribeSimulationApplicationRequestTypeDef(TypedDict):
    application: str
    applicationVersion: NotRequired[str]

class DescribeSimulationJobBatchRequestTypeDef(TypedDict):
    batch: str

class SimulationJobSummaryTypeDef(TypedDict):
    arn: NotRequired[str]
    lastUpdatedAt: NotRequired[datetime]
    name: NotRequired[str]
    status: NotRequired[SimulationJobStatusType]
    simulationApplicationNames: NotRequired[List[str]]
    robotApplicationNames: NotRequired[List[str]]
    dataSourceNames: NotRequired[List[str]]
    computeType: NotRequired[ComputeTypeType]

class DescribeSimulationJobRequestTypeDef(TypedDict):
    job: str

class NetworkInterfaceTypeDef(TypedDict):
    networkInterfaceId: NotRequired[str]
    privateIpAddress: NotRequired[str]
    publicIpAddress: NotRequired[str]

class DescribeWorldExportJobRequestTypeDef(TypedDict):
    job: str

class DescribeWorldGenerationJobRequestTypeDef(TypedDict):
    job: str

class DescribeWorldRequestTypeDef(TypedDict):
    world: str

class DescribeWorldTemplateRequestTypeDef(TypedDict):
    template: str

class WorldFailureTypeDef(TypedDict):
    failureCode: NotRequired[WorldGenerationJobErrorCodeType]
    sampleFailureReason: NotRequired[str]
    failureCount: NotRequired[int]

class FilterTypeDef(TypedDict):
    name: NotRequired[str]
    values: NotRequired[Sequence[str]]

class FleetTypeDef(TypedDict):
    name: NotRequired[str]
    arn: NotRequired[str]
    createdAt: NotRequired[datetime]
    lastDeploymentStatus: NotRequired[DeploymentStatusType]
    lastDeploymentJob: NotRequired[str]
    lastDeploymentTime: NotRequired[datetime]

class GetWorldTemplateBodyRequestTypeDef(TypedDict):
    template: NotRequired[str]
    generationJob: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class SimulationJobBatchSummaryTypeDef(TypedDict):
    arn: NotRequired[str]
    lastUpdatedAt: NotRequired[datetime]
    createdAt: NotRequired[datetime]
    status: NotRequired[SimulationJobBatchStatusType]
    failedRequestCount: NotRequired[int]
    pendingRequestCount: NotRequired[int]
    createdRequestCount: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListWorldTemplatesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class TemplateSummaryTypeDef(TypedDict):
    arn: NotRequired[str]
    createdAt: NotRequired[datetime]
    lastUpdatedAt: NotRequired[datetime]
    name: NotRequired[str]
    version: NotRequired[str]

class WorldSummaryTypeDef(TypedDict):
    arn: NotRequired[str]
    createdAt: NotRequired[datetime]
    generationJob: NotRequired[str]
    template: NotRequired[str]

class PortMappingTypeDef(TypedDict):
    jobPort: int
    applicationPort: int
    enableOnPublicIp: NotRequired[bool]

class ProgressDetailTypeDef(TypedDict):
    currentProgress: NotRequired[RobotDeploymentStepType]
    percentDone: NotRequired[float]
    estimatedTimeRemainingSeconds: NotRequired[int]
    targetResource: NotRequired[str]

class RegisterRobotRequestTypeDef(TypedDict):
    fleet: str
    robot: str

class RestartSimulationJobRequestTypeDef(TypedDict):
    job: str

class ToolTypeDef(TypedDict):
    name: str
    command: str
    streamUI: NotRequired[bool]
    streamOutputToCloudWatch: NotRequired[bool]
    exitBehavior: NotRequired[ExitBehaviorType]

class UploadConfigurationTypeDef(TypedDict):
    name: str
    path: str
    uploadBehavior: UploadBehaviorType

class WorldConfigTypeDef(TypedDict):
    world: NotRequired[str]

class VPCConfigOutputTypeDef(TypedDict):
    subnets: List[str]
    securityGroups: NotRequired[List[str]]
    assignPublicIp: NotRequired[bool]

class SyncDeploymentJobRequestTypeDef(TypedDict):
    clientRequestToken: str
    fleet: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class VPCConfigTypeDef(TypedDict):
    subnets: Sequence[str]
    securityGroups: NotRequired[Sequence[str]]
    assignPublicIp: NotRequired[bool]

class BatchDeleteWorldsResponseTypeDef(TypedDict):
    unprocessedWorlds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetResponseTypeDef(TypedDict):
    arn: str
    name: str
    createdAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRobotResponseTypeDef(TypedDict):
    arn: str
    name: str
    createdAt: datetime
    greengrassGroupId: str
    architecture: ArchitectureType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorldTemplateResponseTypeDef(TypedDict):
    arn: str
    clientRequestToken: str
    createdAt: datetime
    name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterRobotResponseTypeDef(TypedDict):
    fleet: str
    robot: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRobotResponseTypeDef(TypedDict):
    arn: str
    name: str
    fleetArn: str
    status: RobotStatusType
    greengrassGroupId: str
    createdAt: datetime
    architecture: ArchitectureType
    lastDeploymentJob: str
    lastDeploymentTime: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorldResponseTypeDef(TypedDict):
    arn: str
    generationJob: str
    template: str
    createdAt: datetime
    tags: Dict[str, str]
    worldDescriptionBody: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorldTemplateResponseTypeDef(TypedDict):
    arn: str
    clientRequestToken: str
    name: str
    createdAt: datetime
    lastUpdatedAt: datetime
    tags: Dict[str, str]
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorldTemplateBodyResponseTypeDef(TypedDict):
    templateBody: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterRobotResponseTypeDef(TypedDict):
    fleet: str
    robot: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorldTemplateResponseTypeDef(TypedDict):
    arn: str
    name: str
    createdAt: datetime
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class RobotApplicationSummaryTypeDef(TypedDict):
    name: NotRequired[str]
    arn: NotRequired[str]
    version: NotRequired[str]
    lastUpdatedAt: NotRequired[datetime]
    robotSoftwareSuite: NotRequired[RobotSoftwareSuiteTypeDef]

class CreateRobotApplicationRequestTypeDef(TypedDict):
    name: str
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    sources: NotRequired[Sequence[SourceConfigTypeDef]]
    tags: NotRequired[Mapping[str, str]]
    environment: NotRequired[EnvironmentTypeDef]

class UpdateRobotApplicationRequestTypeDef(TypedDict):
    application: str
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    sources: NotRequired[Sequence[SourceConfigTypeDef]]
    currentRevisionId: NotRequired[str]
    environment: NotRequired[EnvironmentTypeDef]

class CreateRobotApplicationResponseTypeDef(TypedDict):
    arn: str
    name: str
    version: str
    sources: List[SourceTypeDef]
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    lastUpdatedAt: datetime
    revisionId: str
    tags: Dict[str, str]
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRobotApplicationVersionResponseTypeDef(TypedDict):
    arn: str
    name: str
    version: str
    sources: List[SourceTypeDef]
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    lastUpdatedAt: datetime
    revisionId: str
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRobotApplicationResponseTypeDef(TypedDict):
    arn: str
    name: str
    version: str
    sources: List[SourceTypeDef]
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    revisionId: str
    lastUpdatedAt: datetime
    tags: Dict[str, str]
    environment: EnvironmentTypeDef
    imageDigest: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRobotApplicationResponseTypeDef(TypedDict):
    arn: str
    name: str
    version: str
    sources: List[SourceTypeDef]
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    lastUpdatedAt: datetime
    revisionId: str
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSimulationApplicationRequestTypeDef(TypedDict):
    name: str
    simulationSoftwareSuite: SimulationSoftwareSuiteTypeDef
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    sources: NotRequired[Sequence[SourceConfigTypeDef]]
    renderingEngine: NotRequired[RenderingEngineTypeDef]
    tags: NotRequired[Mapping[str, str]]
    environment: NotRequired[EnvironmentTypeDef]

class CreateSimulationApplicationResponseTypeDef(TypedDict):
    arn: str
    name: str
    version: str
    sources: List[SourceTypeDef]
    simulationSoftwareSuite: SimulationSoftwareSuiteTypeDef
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    renderingEngine: RenderingEngineTypeDef
    lastUpdatedAt: datetime
    revisionId: str
    tags: Dict[str, str]
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSimulationApplicationVersionResponseTypeDef(TypedDict):
    arn: str
    name: str
    version: str
    sources: List[SourceTypeDef]
    simulationSoftwareSuite: SimulationSoftwareSuiteTypeDef
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    renderingEngine: RenderingEngineTypeDef
    lastUpdatedAt: datetime
    revisionId: str
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSimulationApplicationResponseTypeDef(TypedDict):
    arn: str
    name: str
    version: str
    sources: List[SourceTypeDef]
    simulationSoftwareSuite: SimulationSoftwareSuiteTypeDef
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    renderingEngine: RenderingEngineTypeDef
    revisionId: str
    lastUpdatedAt: datetime
    tags: Dict[str, str]
    environment: EnvironmentTypeDef
    imageDigest: str
    ResponseMetadata: ResponseMetadataTypeDef

class SimulationApplicationSummaryTypeDef(TypedDict):
    name: NotRequired[str]
    arn: NotRequired[str]
    version: NotRequired[str]
    lastUpdatedAt: NotRequired[datetime]
    robotSoftwareSuite: NotRequired[RobotSoftwareSuiteTypeDef]
    simulationSoftwareSuite: NotRequired[SimulationSoftwareSuiteTypeDef]

class UpdateSimulationApplicationRequestTypeDef(TypedDict):
    application: str
    simulationSoftwareSuite: SimulationSoftwareSuiteTypeDef
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    sources: NotRequired[Sequence[SourceConfigTypeDef]]
    renderingEngine: NotRequired[RenderingEngineTypeDef]
    currentRevisionId: NotRequired[str]
    environment: NotRequired[EnvironmentTypeDef]

class UpdateSimulationApplicationResponseTypeDef(TypedDict):
    arn: str
    name: str
    version: str
    sources: List[SourceTypeDef]
    simulationSoftwareSuite: SimulationSoftwareSuiteTypeDef
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    renderingEngine: RenderingEngineTypeDef
    lastUpdatedAt: datetime
    revisionId: str
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorldExportJobRequestTypeDef(TypedDict):
    worlds: Sequence[str]
    outputLocation: OutputLocationTypeDef
    iamRole: str
    clientRequestToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateWorldExportJobResponseTypeDef(TypedDict):
    arn: str
    status: WorldExportJobStatusType
    createdAt: datetime
    failureCode: WorldExportJobErrorCodeType
    clientRequestToken: str
    outputLocation: OutputLocationTypeDef
    iamRole: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorldExportJobResponseTypeDef(TypedDict):
    arn: str
    status: WorldExportJobStatusType
    createdAt: datetime
    failureCode: WorldExportJobErrorCodeType
    failureReason: str
    clientRequestToken: str
    worlds: List[str]
    outputLocation: OutputLocationTypeDef
    iamRole: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class WorldExportJobSummaryTypeDef(TypedDict):
    arn: NotRequired[str]
    status: NotRequired[WorldExportJobStatusType]
    createdAt: NotRequired[datetime]
    worlds: NotRequired[List[str]]
    outputLocation: NotRequired[OutputLocationTypeDef]

class CreateWorldGenerationJobRequestTypeDef(TypedDict):
    template: str
    worldCount: WorldCountTypeDef
    clientRequestToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    worldTags: NotRequired[Mapping[str, str]]

class CreateWorldGenerationJobResponseTypeDef(TypedDict):
    arn: str
    status: WorldGenerationJobStatusType
    createdAt: datetime
    failureCode: WorldGenerationJobErrorCodeType
    clientRequestToken: str
    template: str
    worldCount: WorldCountTypeDef
    tags: Dict[str, str]
    worldTags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class WorldGenerationJobSummaryTypeDef(TypedDict):
    arn: NotRequired[str]
    template: NotRequired[str]
    createdAt: NotRequired[datetime]
    status: NotRequired[WorldGenerationJobStatusType]
    worldCount: NotRequired[WorldCountTypeDef]
    succeededWorldCount: NotRequired[int]
    failedWorldCount: NotRequired[int]

class CreateWorldTemplateRequestTypeDef(TypedDict):
    clientRequestToken: NotRequired[str]
    name: NotRequired[str]
    templateBody: NotRequired[str]
    templateLocation: NotRequired[TemplateLocationTypeDef]
    tags: NotRequired[Mapping[str, str]]

class UpdateWorldTemplateRequestTypeDef(TypedDict):
    template: str
    name: NotRequired[str]
    templateBody: NotRequired[str]
    templateLocation: NotRequired[TemplateLocationTypeDef]

DataSourceConfigUnionTypeDef = Union[DataSourceConfigTypeDef, DataSourceConfigOutputTypeDef]
DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "name": NotRequired[str],
        "s3Bucket": NotRequired[str],
        "s3Keys": NotRequired[List[S3KeyOutputTypeDef]],
        "type": NotRequired[DataSourceTypeType],
        "destination": NotRequired[str],
    },
)

class DeploymentApplicationConfigOutputTypeDef(TypedDict):
    application: str
    applicationVersion: str
    launchConfig: DeploymentLaunchConfigOutputTypeDef

class DeploymentConfigTypeDef(TypedDict):
    concurrentDeploymentPercentage: NotRequired[int]
    failureThresholdPercentage: NotRequired[int]
    robotDeploymentTimeoutInSeconds: NotRequired[int]
    downloadConditionFile: NotRequired[S3ObjectTypeDef]

DeploymentLaunchConfigUnionTypeDef = Union[
    DeploymentLaunchConfigTypeDef, DeploymentLaunchConfigOutputTypeDef
]

class DescribeFleetResponseTypeDef(TypedDict):
    name: str
    arn: str
    robots: List[RobotTypeDef]
    createdAt: datetime
    lastDeploymentStatus: DeploymentStatusType
    lastDeploymentJob: str
    lastDeploymentTime: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRobotsResponseTypeDef(TypedDict):
    robots: List[RobotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSimulationJobsResponseTypeDef(TypedDict):
    simulationJobSummaries: List[SimulationJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class FailureSummaryTypeDef(TypedDict):
    totalFailureCount: NotRequired[int]
    failures: NotRequired[List[WorldFailureTypeDef]]

class ListDeploymentJobsRequestTypeDef(TypedDict):
    filters: NotRequired[Sequence[FilterTypeDef]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListFleetsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    filters: NotRequired[Sequence[FilterTypeDef]]

class ListRobotApplicationsRequestTypeDef(TypedDict):
    versionQualifier: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    filters: NotRequired[Sequence[FilterTypeDef]]

class ListRobotsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    filters: NotRequired[Sequence[FilterTypeDef]]

class ListSimulationApplicationsRequestTypeDef(TypedDict):
    versionQualifier: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    filters: NotRequired[Sequence[FilterTypeDef]]

class ListSimulationJobBatchesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    filters: NotRequired[Sequence[FilterTypeDef]]

class ListSimulationJobsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    filters: NotRequired[Sequence[FilterTypeDef]]

class ListWorldExportJobsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    filters: NotRequired[Sequence[FilterTypeDef]]

class ListWorldGenerationJobsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    filters: NotRequired[Sequence[FilterTypeDef]]

class ListWorldsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    filters: NotRequired[Sequence[FilterTypeDef]]

class ListFleetsResponseTypeDef(TypedDict):
    fleetDetails: List[FleetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListDeploymentJobsRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFleetsRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRobotApplicationsRequestPaginateTypeDef(TypedDict):
    versionQualifier: NotRequired[str]
    filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRobotsRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSimulationApplicationsRequestPaginateTypeDef(TypedDict):
    versionQualifier: NotRequired[str]
    filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSimulationJobBatchesRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSimulationJobsRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorldExportJobsRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorldGenerationJobsRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorldTemplatesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorldsRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSimulationJobBatchesResponseTypeDef(TypedDict):
    simulationJobBatchSummaries: List[SimulationJobBatchSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListWorldTemplatesResponseTypeDef(TypedDict):
    templateSummaries: List[TemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListWorldsResponseTypeDef(TypedDict):
    worldSummaries: List[WorldSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PortForwardingConfigOutputTypeDef(TypedDict):
    portMappings: NotRequired[List[PortMappingTypeDef]]

class PortForwardingConfigTypeDef(TypedDict):
    portMappings: NotRequired[Sequence[PortMappingTypeDef]]

class RobotDeploymentTypeDef(TypedDict):
    arn: NotRequired[str]
    deploymentStartTime: NotRequired[datetime]
    deploymentFinishTime: NotRequired[datetime]
    status: NotRequired[RobotStatusType]
    progressDetail: NotRequired[ProgressDetailTypeDef]
    failureReason: NotRequired[str]
    failureCode: NotRequired[DeploymentJobErrorCodeType]

VPCConfigUnionTypeDef = Union[VPCConfigTypeDef, VPCConfigOutputTypeDef]

class ListRobotApplicationsResponseTypeDef(TypedDict):
    robotApplicationSummaries: List[RobotApplicationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSimulationApplicationsResponseTypeDef(TypedDict):
    simulationApplicationSummaries: List[SimulationApplicationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListWorldExportJobsResponseTypeDef(TypedDict):
    worldExportJobSummaries: List[WorldExportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListWorldGenerationJobsResponseTypeDef(TypedDict):
    worldGenerationJobSummaries: List[WorldGenerationJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateDeploymentJobResponseTypeDef(TypedDict):
    arn: str
    fleet: str
    status: DeploymentStatusType
    deploymentApplicationConfigs: List[DeploymentApplicationConfigOutputTypeDef]
    failureReason: str
    failureCode: DeploymentJobErrorCodeType
    createdAt: datetime
    deploymentConfig: DeploymentConfigTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentJobTypeDef(TypedDict):
    arn: NotRequired[str]
    fleet: NotRequired[str]
    status: NotRequired[DeploymentStatusType]
    deploymentApplicationConfigs: NotRequired[List[DeploymentApplicationConfigOutputTypeDef]]
    deploymentConfig: NotRequired[DeploymentConfigTypeDef]
    failureReason: NotRequired[str]
    failureCode: NotRequired[DeploymentJobErrorCodeType]
    createdAt: NotRequired[datetime]

class SyncDeploymentJobResponseTypeDef(TypedDict):
    arn: str
    fleet: str
    status: DeploymentStatusType
    deploymentConfig: DeploymentConfigTypeDef
    deploymentApplicationConfigs: List[DeploymentApplicationConfigOutputTypeDef]
    failureReason: str
    failureCode: DeploymentJobErrorCodeType
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentApplicationConfigTypeDef(TypedDict):
    application: str
    applicationVersion: str
    launchConfig: DeploymentLaunchConfigUnionTypeDef

class FinishedWorldsSummaryTypeDef(TypedDict):
    finishedCount: NotRequired[int]
    succeededWorlds: NotRequired[List[str]]
    failureSummary: NotRequired[FailureSummaryTypeDef]

class LaunchConfigOutputTypeDef(TypedDict):
    packageName: NotRequired[str]
    launchFile: NotRequired[str]
    environmentVariables: NotRequired[Dict[str, str]]
    portForwardingConfig: NotRequired[PortForwardingConfigOutputTypeDef]
    streamUI: NotRequired[bool]
    command: NotRequired[List[str]]

PortForwardingConfigUnionTypeDef = Union[
    PortForwardingConfigTypeDef, PortForwardingConfigOutputTypeDef
]

class DescribeDeploymentJobResponseTypeDef(TypedDict):
    arn: str
    fleet: str
    status: DeploymentStatusType
    deploymentConfig: DeploymentConfigTypeDef
    deploymentApplicationConfigs: List[DeploymentApplicationConfigOutputTypeDef]
    failureReason: str
    failureCode: DeploymentJobErrorCodeType
    createdAt: datetime
    robotDeploymentSummary: List[RobotDeploymentTypeDef]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentJobsResponseTypeDef(TypedDict):
    deploymentJobs: List[DeploymentJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

DeploymentApplicationConfigUnionTypeDef = Union[
    DeploymentApplicationConfigTypeDef, DeploymentApplicationConfigOutputTypeDef
]

class DescribeWorldGenerationJobResponseTypeDef(TypedDict):
    arn: str
    status: WorldGenerationJobStatusType
    createdAt: datetime
    failureCode: WorldGenerationJobErrorCodeType
    failureReason: str
    clientRequestToken: str
    template: str
    worldCount: WorldCountTypeDef
    finishedWorldsSummary: FinishedWorldsSummaryTypeDef
    tags: Dict[str, str]
    worldTags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RobotApplicationConfigOutputTypeDef(TypedDict):
    application: str
    launchConfig: LaunchConfigOutputTypeDef
    applicationVersion: NotRequired[str]
    uploadConfigurations: NotRequired[List[UploadConfigurationTypeDef]]
    useDefaultUploadConfigurations: NotRequired[bool]
    tools: NotRequired[List[ToolTypeDef]]
    useDefaultTools: NotRequired[bool]

class SimulationApplicationConfigOutputTypeDef(TypedDict):
    application: str
    launchConfig: LaunchConfigOutputTypeDef
    applicationVersion: NotRequired[str]
    uploadConfigurations: NotRequired[List[UploadConfigurationTypeDef]]
    worldConfigs: NotRequired[List[WorldConfigTypeDef]]
    useDefaultUploadConfigurations: NotRequired[bool]
    tools: NotRequired[List[ToolTypeDef]]
    useDefaultTools: NotRequired[bool]

class LaunchConfigTypeDef(TypedDict):
    packageName: NotRequired[str]
    launchFile: NotRequired[str]
    environmentVariables: NotRequired[Mapping[str, str]]
    portForwardingConfig: NotRequired[PortForwardingConfigUnionTypeDef]
    streamUI: NotRequired[bool]
    command: NotRequired[Sequence[str]]

class CreateDeploymentJobRequestTypeDef(TypedDict):
    clientRequestToken: str
    fleet: str
    deploymentApplicationConfigs: Sequence[DeploymentApplicationConfigUnionTypeDef]
    deploymentConfig: NotRequired[DeploymentConfigTypeDef]
    tags: NotRequired[Mapping[str, str]]

class CreateSimulationJobResponseTypeDef(TypedDict):
    arn: str
    status: SimulationJobStatusType
    lastStartedAt: datetime
    lastUpdatedAt: datetime
    failureBehavior: FailureBehaviorType
    failureCode: SimulationJobErrorCodeType
    clientRequestToken: str
    outputLocation: OutputLocationTypeDef
    loggingConfig: LoggingConfigTypeDef
    maxJobDurationInSeconds: int
    simulationTimeMillis: int
    iamRole: str
    robotApplications: List[RobotApplicationConfigOutputTypeDef]
    simulationApplications: List[SimulationApplicationConfigOutputTypeDef]
    dataSources: List[DataSourceTypeDef]
    tags: Dict[str, str]
    vpcConfig: VPCConfigResponseTypeDef
    compute: ComputeResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSimulationJobResponseTypeDef(TypedDict):
    arn: str
    name: str
    status: SimulationJobStatusType
    lastStartedAt: datetime
    lastUpdatedAt: datetime
    failureBehavior: FailureBehaviorType
    failureCode: SimulationJobErrorCodeType
    failureReason: str
    clientRequestToken: str
    outputLocation: OutputLocationTypeDef
    loggingConfig: LoggingConfigTypeDef
    maxJobDurationInSeconds: int
    simulationTimeMillis: int
    iamRole: str
    robotApplications: List[RobotApplicationConfigOutputTypeDef]
    simulationApplications: List[SimulationApplicationConfigOutputTypeDef]
    dataSources: List[DataSourceTypeDef]
    tags: Dict[str, str]
    vpcConfig: VPCConfigResponseTypeDef
    networkInterface: NetworkInterfaceTypeDef
    compute: ComputeResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SimulationJobRequestOutputTypeDef(TypedDict):
    maxJobDurationInSeconds: int
    outputLocation: NotRequired[OutputLocationTypeDef]
    loggingConfig: NotRequired[LoggingConfigTypeDef]
    iamRole: NotRequired[str]
    failureBehavior: NotRequired[FailureBehaviorType]
    useDefaultApplications: NotRequired[bool]
    robotApplications: NotRequired[List[RobotApplicationConfigOutputTypeDef]]
    simulationApplications: NotRequired[List[SimulationApplicationConfigOutputTypeDef]]
    dataSources: NotRequired[List[DataSourceConfigOutputTypeDef]]
    vpcConfig: NotRequired[VPCConfigOutputTypeDef]
    compute: NotRequired[ComputeTypeDef]
    tags: NotRequired[Dict[str, str]]

class SimulationJobTypeDef(TypedDict):
    arn: NotRequired[str]
    name: NotRequired[str]
    status: NotRequired[SimulationJobStatusType]
    lastStartedAt: NotRequired[datetime]
    lastUpdatedAt: NotRequired[datetime]
    failureBehavior: NotRequired[FailureBehaviorType]
    failureCode: NotRequired[SimulationJobErrorCodeType]
    failureReason: NotRequired[str]
    clientRequestToken: NotRequired[str]
    outputLocation: NotRequired[OutputLocationTypeDef]
    loggingConfig: NotRequired[LoggingConfigTypeDef]
    maxJobDurationInSeconds: NotRequired[int]
    simulationTimeMillis: NotRequired[int]
    iamRole: NotRequired[str]
    robotApplications: NotRequired[List[RobotApplicationConfigOutputTypeDef]]
    simulationApplications: NotRequired[List[SimulationApplicationConfigOutputTypeDef]]
    dataSources: NotRequired[List[DataSourceTypeDef]]
    tags: NotRequired[Dict[str, str]]
    vpcConfig: NotRequired[VPCConfigResponseTypeDef]
    networkInterface: NotRequired[NetworkInterfaceTypeDef]
    compute: NotRequired[ComputeResponseTypeDef]

LaunchConfigUnionTypeDef = Union[LaunchConfigTypeDef, LaunchConfigOutputTypeDef]

class FailedCreateSimulationJobRequestTypeDef(TypedDict):
    request: NotRequired[SimulationJobRequestOutputTypeDef]
    failureReason: NotRequired[str]
    failureCode: NotRequired[SimulationJobErrorCodeType]
    failedAt: NotRequired[datetime]

class BatchDescribeSimulationJobResponseTypeDef(TypedDict):
    jobs: List[SimulationJobTypeDef]
    unprocessedJobs: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class RobotApplicationConfigTypeDef(TypedDict):
    application: str
    launchConfig: LaunchConfigUnionTypeDef
    applicationVersion: NotRequired[str]
    uploadConfigurations: NotRequired[Sequence[UploadConfigurationTypeDef]]
    useDefaultUploadConfigurations: NotRequired[bool]
    tools: NotRequired[Sequence[ToolTypeDef]]
    useDefaultTools: NotRequired[bool]

class SimulationApplicationConfigTypeDef(TypedDict):
    application: str
    launchConfig: LaunchConfigUnionTypeDef
    applicationVersion: NotRequired[str]
    uploadConfigurations: NotRequired[Sequence[UploadConfigurationTypeDef]]
    worldConfigs: NotRequired[Sequence[WorldConfigTypeDef]]
    useDefaultUploadConfigurations: NotRequired[bool]
    tools: NotRequired[Sequence[ToolTypeDef]]
    useDefaultTools: NotRequired[bool]

class DescribeSimulationJobBatchResponseTypeDef(TypedDict):
    arn: str
    status: SimulationJobBatchStatusType
    lastUpdatedAt: datetime
    createdAt: datetime
    clientRequestToken: str
    batchPolicy: BatchPolicyTypeDef
    failureCode: Literal["InternalServiceError"]
    failureReason: str
    failedRequests: List[FailedCreateSimulationJobRequestTypeDef]
    pendingRequests: List[SimulationJobRequestOutputTypeDef]
    createdRequests: List[SimulationJobSummaryTypeDef]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartSimulationJobBatchResponseTypeDef(TypedDict):
    arn: str
    status: SimulationJobBatchStatusType
    createdAt: datetime
    clientRequestToken: str
    batchPolicy: BatchPolicyTypeDef
    failureCode: Literal["InternalServiceError"]
    failureReason: str
    failedRequests: List[FailedCreateSimulationJobRequestTypeDef]
    pendingRequests: List[SimulationJobRequestOutputTypeDef]
    createdRequests: List[SimulationJobSummaryTypeDef]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

RobotApplicationConfigUnionTypeDef = Union[
    RobotApplicationConfigTypeDef, RobotApplicationConfigOutputTypeDef
]
SimulationApplicationConfigUnionTypeDef = Union[
    SimulationApplicationConfigTypeDef, SimulationApplicationConfigOutputTypeDef
]

class CreateSimulationJobRequestTypeDef(TypedDict):
    maxJobDurationInSeconds: int
    iamRole: str
    clientRequestToken: NotRequired[str]
    outputLocation: NotRequired[OutputLocationTypeDef]
    loggingConfig: NotRequired[LoggingConfigTypeDef]
    failureBehavior: NotRequired[FailureBehaviorType]
    robotApplications: NotRequired[Sequence[RobotApplicationConfigUnionTypeDef]]
    simulationApplications: NotRequired[Sequence[SimulationApplicationConfigUnionTypeDef]]
    dataSources: NotRequired[Sequence[DataSourceConfigUnionTypeDef]]
    tags: NotRequired[Mapping[str, str]]
    vpcConfig: NotRequired[VPCConfigUnionTypeDef]
    compute: NotRequired[ComputeTypeDef]

class SimulationJobRequestTypeDef(TypedDict):
    maxJobDurationInSeconds: int
    outputLocation: NotRequired[OutputLocationTypeDef]
    loggingConfig: NotRequired[LoggingConfigTypeDef]
    iamRole: NotRequired[str]
    failureBehavior: NotRequired[FailureBehaviorType]
    useDefaultApplications: NotRequired[bool]
    robotApplications: NotRequired[Sequence[RobotApplicationConfigUnionTypeDef]]
    simulationApplications: NotRequired[Sequence[SimulationApplicationConfigUnionTypeDef]]
    dataSources: NotRequired[Sequence[DataSourceConfigUnionTypeDef]]
    vpcConfig: NotRequired[VPCConfigUnionTypeDef]
    compute: NotRequired[ComputeTypeDef]
    tags: NotRequired[Mapping[str, str]]

SimulationJobRequestUnionTypeDef = Union[
    SimulationJobRequestTypeDef, SimulationJobRequestOutputTypeDef
]

class StartSimulationJobBatchRequestTypeDef(TypedDict):
    createSimulationJobRequests: Sequence[SimulationJobRequestUnionTypeDef]
    clientRequestToken: NotRequired[str]
    batchPolicy: NotRequired[BatchPolicyTypeDef]
    tags: NotRequired[Mapping[str, str]]
