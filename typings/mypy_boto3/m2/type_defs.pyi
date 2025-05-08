"""
Type annotations for m2 service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_m2.type_defs import AlternateKeyTypeDef

    data: AlternateKeyTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ApplicationDeploymentLifecycleType,
    ApplicationLifecycleType,
    ApplicationVersionLifecycleType,
    BatchJobExecutionStatusType,
    BatchJobTypeType,
    DataSetTaskLifecycleType,
    DeploymentLifecycleType,
    EngineTypeType,
    EnvironmentLifecycleType,
    NetworkTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AlternateKeyTypeDef",
    "ApplicationSummaryTypeDef",
    "ApplicationVersionSummaryTypeDef",
    "BatchJobDefinitionTypeDef",
    "BatchJobExecutionSummaryTypeDef",
    "BatchJobIdentifierTypeDef",
    "CancelBatchJobExecutionRequestTypeDef",
    "CreateApplicationRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateDataSetExportTaskRequestTypeDef",
    "CreateDataSetExportTaskResponseTypeDef",
    "CreateDataSetImportTaskRequestTypeDef",
    "CreateDataSetImportTaskResponseTypeDef",
    "CreateDeploymentRequestTypeDef",
    "CreateDeploymentResponseTypeDef",
    "CreateEnvironmentRequestTypeDef",
    "CreateEnvironmentResponseTypeDef",
    "DataSetExportConfigTypeDef",
    "DataSetExportItemTypeDef",
    "DataSetExportSummaryTypeDef",
    "DataSetExportTaskTypeDef",
    "DataSetImportConfigTypeDef",
    "DataSetImportItemTypeDef",
    "DataSetImportSummaryTypeDef",
    "DataSetImportTaskTypeDef",
    "DataSetSummaryTypeDef",
    "DataSetTypeDef",
    "DatasetDetailOrgAttributesTypeDef",
    "DatasetOrgAttributesTypeDef",
    "DefinitionTypeDef",
    "DeleteApplicationFromEnvironmentRequestTypeDef",
    "DeleteApplicationRequestTypeDef",
    "DeleteEnvironmentRequestTypeDef",
    "DeployedVersionSummaryTypeDef",
    "DeploymentSummaryTypeDef",
    "EfsStorageConfigurationTypeDef",
    "EngineVersionsSummaryTypeDef",
    "EnvironmentSummaryTypeDef",
    "ExternalLocationTypeDef",
    "FileBatchJobDefinitionTypeDef",
    "FileBatchJobIdentifierTypeDef",
    "FsxStorageConfigurationTypeDef",
    "GdgAttributesTypeDef",
    "GdgDetailAttributesTypeDef",
    "GetApplicationRequestTypeDef",
    "GetApplicationResponseTypeDef",
    "GetApplicationVersionRequestTypeDef",
    "GetApplicationVersionResponseTypeDef",
    "GetBatchJobExecutionRequestTypeDef",
    "GetBatchJobExecutionResponseTypeDef",
    "GetDataSetDetailsRequestTypeDef",
    "GetDataSetDetailsResponseTypeDef",
    "GetDataSetExportTaskRequestTypeDef",
    "GetDataSetExportTaskResponseTypeDef",
    "GetDataSetImportTaskRequestTypeDef",
    "GetDataSetImportTaskResponseTypeDef",
    "GetDeploymentRequestTypeDef",
    "GetDeploymentResponseTypeDef",
    "GetEnvironmentRequestTypeDef",
    "GetEnvironmentResponseTypeDef",
    "GetSignedBluinsightsUrlResponseTypeDef",
    "HighAvailabilityConfigTypeDef",
    "JobIdentifierTypeDef",
    "JobStepRestartMarkerTypeDef",
    "JobStepTypeDef",
    "ListApplicationVersionsRequestPaginateTypeDef",
    "ListApplicationVersionsRequestTypeDef",
    "ListApplicationVersionsResponseTypeDef",
    "ListApplicationsRequestPaginateTypeDef",
    "ListApplicationsRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListBatchJobDefinitionsRequestPaginateTypeDef",
    "ListBatchJobDefinitionsRequestTypeDef",
    "ListBatchJobDefinitionsResponseTypeDef",
    "ListBatchJobExecutionsRequestPaginateTypeDef",
    "ListBatchJobExecutionsRequestTypeDef",
    "ListBatchJobExecutionsResponseTypeDef",
    "ListBatchJobRestartPointsRequestTypeDef",
    "ListBatchJobRestartPointsResponseTypeDef",
    "ListDataSetExportHistoryRequestPaginateTypeDef",
    "ListDataSetExportHistoryRequestTypeDef",
    "ListDataSetExportHistoryResponseTypeDef",
    "ListDataSetImportHistoryRequestPaginateTypeDef",
    "ListDataSetImportHistoryRequestTypeDef",
    "ListDataSetImportHistoryResponseTypeDef",
    "ListDataSetsRequestPaginateTypeDef",
    "ListDataSetsRequestTypeDef",
    "ListDataSetsResponseTypeDef",
    "ListDeploymentsRequestPaginateTypeDef",
    "ListDeploymentsRequestTypeDef",
    "ListDeploymentsResponseTypeDef",
    "ListEngineVersionsRequestPaginateTypeDef",
    "ListEngineVersionsRequestTypeDef",
    "ListEngineVersionsResponseTypeDef",
    "ListEnvironmentsRequestPaginateTypeDef",
    "ListEnvironmentsRequestTypeDef",
    "ListEnvironmentsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogGroupSummaryTypeDef",
    "MaintenanceScheduleTypeDef",
    "PaginatorConfigTypeDef",
    "PendingMaintenanceTypeDef",
    "PoAttributesTypeDef",
    "PoDetailAttributesTypeDef",
    "PrimaryKeyTypeDef",
    "PsAttributesTypeDef",
    "PsDetailAttributesTypeDef",
    "RecordLengthTypeDef",
    "ResponseMetadataTypeDef",
    "RestartBatchJobIdentifierTypeDef",
    "S3BatchJobIdentifierTypeDef",
    "ScriptBatchJobDefinitionTypeDef",
    "ScriptBatchJobIdentifierTypeDef",
    "StartApplicationRequestTypeDef",
    "StartBatchJobRequestTypeDef",
    "StartBatchJobResponseTypeDef",
    "StopApplicationRequestTypeDef",
    "StorageConfigurationTypeDef",
    "TagResourceRequestTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateApplicationRequestTypeDef",
    "UpdateApplicationResponseTypeDef",
    "UpdateEnvironmentRequestTypeDef",
    "UpdateEnvironmentResponseTypeDef",
    "VsamAttributesTypeDef",
    "VsamDetailAttributesTypeDef",
)

class AlternateKeyTypeDef(TypedDict):
    length: int
    offset: int
    allowDuplicates: NotRequired[bool]
    name: NotRequired[str]

class ApplicationSummaryTypeDef(TypedDict):
    applicationArn: str
    applicationId: str
    applicationVersion: int
    creationTime: datetime
    engineType: EngineTypeType
    name: str
    status: ApplicationLifecycleType
    deploymentStatus: NotRequired[ApplicationDeploymentLifecycleType]
    description: NotRequired[str]
    environmentId: NotRequired[str]
    lastStartTime: NotRequired[datetime]
    roleArn: NotRequired[str]
    versionStatus: NotRequired[ApplicationVersionLifecycleType]

class ApplicationVersionSummaryTypeDef(TypedDict):
    applicationVersion: int
    creationTime: datetime
    status: ApplicationVersionLifecycleType
    statusReason: NotRequired[str]

class FileBatchJobDefinitionTypeDef(TypedDict):
    fileName: str
    folderPath: NotRequired[str]

class ScriptBatchJobDefinitionTypeDef(TypedDict):
    scriptName: str

class FileBatchJobIdentifierTypeDef(TypedDict):
    fileName: str
    folderPath: NotRequired[str]

class ScriptBatchJobIdentifierTypeDef(TypedDict):
    scriptName: str

class CancelBatchJobExecutionRequestTypeDef(TypedDict):
    applicationId: str
    executionId: str
    authSecretsManagerArn: NotRequired[str]

class DefinitionTypeDef(TypedDict):
    content: NotRequired[str]
    s3Location: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateDeploymentRequestTypeDef(TypedDict):
    applicationId: str
    applicationVersion: int
    environmentId: str
    clientToken: NotRequired[str]

class HighAvailabilityConfigTypeDef(TypedDict):
    desiredCapacity: int

class ExternalLocationTypeDef(TypedDict):
    s3Location: NotRequired[str]

class DataSetExportSummaryTypeDef(TypedDict):
    failed: int
    inProgress: int
    pending: int
    succeeded: int
    total: int

class DataSetImportSummaryTypeDef(TypedDict):
    failed: int
    inProgress: int
    pending: int
    succeeded: int
    total: int

DataSetSummaryTypeDef = TypedDict(
    "DataSetSummaryTypeDef",
    {
        "dataSetName": str,
        "creationTime": NotRequired[datetime],
        "dataSetOrg": NotRequired[str],
        "format": NotRequired[str],
        "lastReferencedTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
    },
)
RecordLengthTypeDef = TypedDict(
    "RecordLengthTypeDef",
    {
        "max": int,
        "min": int,
    },
)

class GdgDetailAttributesTypeDef(TypedDict):
    limit: NotRequired[int]
    rollDisposition: NotRequired[str]

PoDetailAttributesTypeDef = TypedDict(
    "PoDetailAttributesTypeDef",
    {
        "encoding": str,
        "format": str,
    },
)
PsDetailAttributesTypeDef = TypedDict(
    "PsDetailAttributesTypeDef",
    {
        "encoding": str,
        "format": str,
    },
)

class GdgAttributesTypeDef(TypedDict):
    limit: NotRequired[int]
    rollDisposition: NotRequired[str]

PoAttributesTypeDef = TypedDict(
    "PoAttributesTypeDef",
    {
        "format": str,
        "memberFileExtensions": Sequence[str],
        "encoding": NotRequired[str],
    },
)
PsAttributesTypeDef = TypedDict(
    "PsAttributesTypeDef",
    {
        "format": str,
        "encoding": NotRequired[str],
    },
)

class DeleteApplicationFromEnvironmentRequestTypeDef(TypedDict):
    applicationId: str
    environmentId: str

class DeleteApplicationRequestTypeDef(TypedDict):
    applicationId: str

class DeleteEnvironmentRequestTypeDef(TypedDict):
    environmentId: str

class DeployedVersionSummaryTypeDef(TypedDict):
    applicationVersion: int
    status: DeploymentLifecycleType
    statusReason: NotRequired[str]

class DeploymentSummaryTypeDef(TypedDict):
    applicationId: str
    applicationVersion: int
    creationTime: datetime
    deploymentId: str
    environmentId: str
    status: DeploymentLifecycleType
    statusReason: NotRequired[str]

class EfsStorageConfigurationTypeDef(TypedDict):
    fileSystemId: str
    mountPoint: str

class EngineVersionsSummaryTypeDef(TypedDict):
    engineType: str
    engineVersion: str

class EnvironmentSummaryTypeDef(TypedDict):
    creationTime: datetime
    engineType: EngineTypeType
    engineVersion: str
    environmentArn: str
    environmentId: str
    instanceType: str
    name: str
    status: EnvironmentLifecycleType
    networkType: NotRequired[NetworkTypeType]

class FsxStorageConfigurationTypeDef(TypedDict):
    fileSystemId: str
    mountPoint: str

class GetApplicationRequestTypeDef(TypedDict):
    applicationId: str

class LogGroupSummaryTypeDef(TypedDict):
    logGroupName: str
    logType: str

class GetApplicationVersionRequestTypeDef(TypedDict):
    applicationId: str
    applicationVersion: int

class GetBatchJobExecutionRequestTypeDef(TypedDict):
    applicationId: str
    executionId: str

class JobStepRestartMarkerTypeDef(TypedDict):
    fromStep: str
    fromProcStep: NotRequired[str]
    skip: NotRequired[bool]
    stepCheckpoint: NotRequired[int]
    toProcStep: NotRequired[str]
    toStep: NotRequired[str]

class GetDataSetDetailsRequestTypeDef(TypedDict):
    applicationId: str
    dataSetName: str

class GetDataSetExportTaskRequestTypeDef(TypedDict):
    applicationId: str
    taskId: str

class GetDataSetImportTaskRequestTypeDef(TypedDict):
    applicationId: str
    taskId: str

class GetDeploymentRequestTypeDef(TypedDict):
    applicationId: str
    deploymentId: str

class GetEnvironmentRequestTypeDef(TypedDict):
    environmentId: str

class JobIdentifierTypeDef(TypedDict):
    fileName: NotRequired[str]
    scriptName: NotRequired[str]

class JobStepTypeDef(TypedDict):
    procStepName: NotRequired[str]
    procStepNumber: NotRequired[int]
    stepCheckpoint: NotRequired[int]
    stepCheckpointStatus: NotRequired[str]
    stepCheckpointTime: NotRequired[datetime]
    stepCondCode: NotRequired[str]
    stepName: NotRequired[str]
    stepNumber: NotRequired[int]
    stepRestartable: NotRequired[bool]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListApplicationVersionsRequestTypeDef(TypedDict):
    applicationId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListApplicationsRequestTypeDef(TypedDict):
    environmentId: NotRequired[str]
    maxResults: NotRequired[int]
    names: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]

class ListBatchJobDefinitionsRequestTypeDef(TypedDict):
    applicationId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    prefix: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class ListBatchJobRestartPointsRequestTypeDef(TypedDict):
    applicationId: str
    executionId: str
    authSecretsManagerArn: NotRequired[str]

class ListDataSetExportHistoryRequestTypeDef(TypedDict):
    applicationId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListDataSetImportHistoryRequestTypeDef(TypedDict):
    applicationId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListDataSetsRequestTypeDef(TypedDict):
    applicationId: str
    maxResults: NotRequired[int]
    nameFilter: NotRequired[str]
    nextToken: NotRequired[str]
    prefix: NotRequired[str]

class ListDeploymentsRequestTypeDef(TypedDict):
    applicationId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListEngineVersionsRequestTypeDef(TypedDict):
    engineType: NotRequired[EngineTypeType]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListEnvironmentsRequestTypeDef(TypedDict):
    engineType: NotRequired[EngineTypeType]
    maxResults: NotRequired[int]
    names: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class MaintenanceScheduleTypeDef(TypedDict):
    endTime: NotRequired[datetime]
    startTime: NotRequired[datetime]

class PrimaryKeyTypeDef(TypedDict):
    length: int
    offset: int
    name: NotRequired[str]

class StartApplicationRequestTypeDef(TypedDict):
    applicationId: str

class StopApplicationRequestTypeDef(TypedDict):
    applicationId: str
    forceStop: NotRequired[bool]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateEnvironmentRequestTypeDef(TypedDict):
    environmentId: str
    applyDuringMaintenanceWindow: NotRequired[bool]
    desiredCapacity: NotRequired[int]
    engineVersion: NotRequired[str]
    forceUpdate: NotRequired[bool]
    instanceType: NotRequired[str]
    preferredMaintenanceWindow: NotRequired[str]

class BatchJobDefinitionTypeDef(TypedDict):
    fileBatchJobDefinition: NotRequired[FileBatchJobDefinitionTypeDef]
    scriptBatchJobDefinition: NotRequired[ScriptBatchJobDefinitionTypeDef]

class CreateApplicationRequestTypeDef(TypedDict):
    definition: DefinitionTypeDef
    engineType: EngineTypeType
    name: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    kmsKeyId: NotRequired[str]
    roleArn: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateApplicationRequestTypeDef(TypedDict):
    applicationId: str
    currentApplicationVersion: int
    definition: NotRequired[DefinitionTypeDef]
    description: NotRequired[str]

class CreateApplicationResponseTypeDef(TypedDict):
    applicationArn: str
    applicationId: str
    applicationVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSetExportTaskResponseTypeDef(TypedDict):
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSetImportTaskResponseTypeDef(TypedDict):
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentResponseTypeDef(TypedDict):
    deploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentResponseTypeDef(TypedDict):
    environmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationVersionResponseTypeDef(TypedDict):
    applicationVersion: int
    creationTime: datetime
    definitionContent: str
    description: str
    name: str
    status: ApplicationVersionLifecycleType
    statusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentResponseTypeDef(TypedDict):
    applicationId: str
    applicationVersion: int
    creationTime: datetime
    deploymentId: str
    environmentId: str
    status: DeploymentLifecycleType
    statusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSignedBluinsightsUrlResponseTypeDef(TypedDict):
    signedBiUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationVersionsResponseTypeDef(TypedDict):
    applicationVersions: List[ApplicationVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListApplicationsResponseTypeDef(TypedDict):
    applications: List[ApplicationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartBatchJobResponseTypeDef(TypedDict):
    executionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationResponseTypeDef(TypedDict):
    applicationVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentResponseTypeDef(TypedDict):
    environmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataSetExportItemTypeDef(TypedDict):
    datasetName: str
    externalLocation: ExternalLocationTypeDef

class DataSetExportTaskTypeDef(TypedDict):
    status: DataSetTaskLifecycleType
    summary: DataSetExportSummaryTypeDef
    taskId: str
    statusReason: NotRequired[str]

class GetDataSetExportTaskResponseTypeDef(TypedDict):
    kmsKeyArn: str
    status: DataSetTaskLifecycleType
    statusReason: str
    summary: DataSetExportSummaryTypeDef
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataSetImportTaskTypeDef(TypedDict):
    status: DataSetTaskLifecycleType
    summary: DataSetImportSummaryTypeDef
    taskId: str
    statusReason: NotRequired[str]

class GetDataSetImportTaskResponseTypeDef(TypedDict):
    status: DataSetTaskLifecycleType
    summary: DataSetImportSummaryTypeDef
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataSetsResponseTypeDef(TypedDict):
    dataSets: List[DataSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListDeploymentsResponseTypeDef(TypedDict):
    deployments: List[DeploymentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListEngineVersionsResponseTypeDef(TypedDict):
    engineVersions: List[EngineVersionsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListEnvironmentsResponseTypeDef(TypedDict):
    environments: List[EnvironmentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StorageConfigurationTypeDef(TypedDict):
    efs: NotRequired[EfsStorageConfigurationTypeDef]
    fsx: NotRequired[FsxStorageConfigurationTypeDef]

class GetApplicationResponseTypeDef(TypedDict):
    applicationArn: str
    applicationId: str
    creationTime: datetime
    deployedVersion: DeployedVersionSummaryTypeDef
    description: str
    engineType: EngineTypeType
    environmentId: str
    kmsKeyId: str
    lastStartTime: datetime
    latestVersion: ApplicationVersionSummaryTypeDef
    listenerArns: List[str]
    listenerPorts: List[int]
    loadBalancerDnsName: str
    logGroups: List[LogGroupSummaryTypeDef]
    name: str
    roleArn: str
    status: ApplicationLifecycleType
    statusReason: str
    tags: Dict[str, str]
    targetGroupArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class RestartBatchJobIdentifierTypeDef(TypedDict):
    executionId: str
    jobStepRestartMarker: JobStepRestartMarkerTypeDef

class S3BatchJobIdentifierTypeDef(TypedDict):
    bucket: str
    identifier: JobIdentifierTypeDef
    keyPrefix: NotRequired[str]

class ListBatchJobRestartPointsResponseTypeDef(TypedDict):
    batchJobSteps: List[JobStepTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationVersionsRequestPaginateTypeDef(TypedDict):
    applicationId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListApplicationsRequestPaginateTypeDef(TypedDict):
    environmentId: NotRequired[str]
    names: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBatchJobDefinitionsRequestPaginateTypeDef(TypedDict):
    applicationId: str
    prefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataSetExportHistoryRequestPaginateTypeDef(TypedDict):
    applicationId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataSetImportHistoryRequestPaginateTypeDef(TypedDict):
    applicationId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataSetsRequestPaginateTypeDef(TypedDict):
    applicationId: str
    nameFilter: NotRequired[str]
    prefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDeploymentsRequestPaginateTypeDef(TypedDict):
    applicationId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEngineVersionsRequestPaginateTypeDef(TypedDict):
    engineType: NotRequired[EngineTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEnvironmentsRequestPaginateTypeDef(TypedDict):
    engineType: NotRequired[EngineTypeType]
    names: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBatchJobExecutionsRequestPaginateTypeDef(TypedDict):
    applicationId: str
    executionIds: NotRequired[Sequence[str]]
    jobName: NotRequired[str]
    startedAfter: NotRequired[TimestampTypeDef]
    startedBefore: NotRequired[TimestampTypeDef]
    status: NotRequired[BatchJobExecutionStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBatchJobExecutionsRequestTypeDef(TypedDict):
    applicationId: str
    executionIds: NotRequired[Sequence[str]]
    jobName: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    startedAfter: NotRequired[TimestampTypeDef]
    startedBefore: NotRequired[TimestampTypeDef]
    status: NotRequired[BatchJobExecutionStatusType]

class PendingMaintenanceTypeDef(TypedDict):
    engineVersion: NotRequired[str]
    schedule: NotRequired[MaintenanceScheduleTypeDef]

VsamAttributesTypeDef = TypedDict(
    "VsamAttributesTypeDef",
    {
        "format": str,
        "alternateKeys": NotRequired[Sequence[AlternateKeyTypeDef]],
        "compressed": NotRequired[bool],
        "encoding": NotRequired[str],
        "primaryKey": NotRequired[PrimaryKeyTypeDef],
    },
)

class VsamDetailAttributesTypeDef(TypedDict):
    alternateKeys: NotRequired[List[AlternateKeyTypeDef]]
    cacheAtStartup: NotRequired[bool]
    compressed: NotRequired[bool]
    encoding: NotRequired[str]
    primaryKey: NotRequired[PrimaryKeyTypeDef]
    recordFormat: NotRequired[str]

class ListBatchJobDefinitionsResponseTypeDef(TypedDict):
    batchJobDefinitions: List[BatchJobDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DataSetExportConfigTypeDef(TypedDict):
    dataSets: NotRequired[Sequence[DataSetExportItemTypeDef]]
    s3Location: NotRequired[str]

class ListDataSetExportHistoryResponseTypeDef(TypedDict):
    dataSetExportTasks: List[DataSetExportTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListDataSetImportHistoryResponseTypeDef(TypedDict):
    dataSetImportTasks: List[DataSetImportTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateEnvironmentRequestTypeDef(TypedDict):
    engineType: EngineTypeType
    instanceType: str
    name: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    engineVersion: NotRequired[str]
    highAvailabilityConfig: NotRequired[HighAvailabilityConfigTypeDef]
    kmsKeyId: NotRequired[str]
    networkType: NotRequired[NetworkTypeType]
    preferredMaintenanceWindow: NotRequired[str]
    publiclyAccessible: NotRequired[bool]
    securityGroupIds: NotRequired[Sequence[str]]
    storageConfigurations: NotRequired[Sequence[StorageConfigurationTypeDef]]
    subnetIds: NotRequired[Sequence[str]]
    tags: NotRequired[Mapping[str, str]]

class BatchJobIdentifierTypeDef(TypedDict):
    fileBatchJobIdentifier: NotRequired[FileBatchJobIdentifierTypeDef]
    restartBatchJobIdentifier: NotRequired[RestartBatchJobIdentifierTypeDef]
    s3BatchJobIdentifier: NotRequired[S3BatchJobIdentifierTypeDef]
    scriptBatchJobIdentifier: NotRequired[ScriptBatchJobIdentifierTypeDef]

class GetEnvironmentResponseTypeDef(TypedDict):
    actualCapacity: int
    creationTime: datetime
    description: str
    engineType: EngineTypeType
    engineVersion: str
    environmentArn: str
    environmentId: str
    highAvailabilityConfig: HighAvailabilityConfigTypeDef
    instanceType: str
    kmsKeyId: str
    loadBalancerArn: str
    name: str
    networkType: NetworkTypeType
    pendingMaintenance: PendingMaintenanceTypeDef
    preferredMaintenanceWindow: str
    publiclyAccessible: bool
    securityGroupIds: List[str]
    status: EnvironmentLifecycleType
    statusReason: str
    storageConfigurations: List[StorageConfigurationTypeDef]
    subnetIds: List[str]
    tags: Dict[str, str]
    vpcId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DatasetOrgAttributesTypeDef(TypedDict):
    gdg: NotRequired[GdgAttributesTypeDef]
    po: NotRequired[PoAttributesTypeDef]
    ps: NotRequired[PsAttributesTypeDef]
    vsam: NotRequired[VsamAttributesTypeDef]

class DatasetDetailOrgAttributesTypeDef(TypedDict):
    gdg: NotRequired[GdgDetailAttributesTypeDef]
    po: NotRequired[PoDetailAttributesTypeDef]
    ps: NotRequired[PsDetailAttributesTypeDef]
    vsam: NotRequired[VsamDetailAttributesTypeDef]

class CreateDataSetExportTaskRequestTypeDef(TypedDict):
    applicationId: str
    exportConfig: DataSetExportConfigTypeDef
    clientToken: NotRequired[str]
    kmsKeyId: NotRequired[str]

class BatchJobExecutionSummaryTypeDef(TypedDict):
    applicationId: str
    executionId: str
    startTime: datetime
    status: BatchJobExecutionStatusType
    batchJobIdentifier: NotRequired[BatchJobIdentifierTypeDef]
    endTime: NotRequired[datetime]
    jobId: NotRequired[str]
    jobName: NotRequired[str]
    jobType: NotRequired[BatchJobTypeType]
    returnCode: NotRequired[str]

class GetBatchJobExecutionResponseTypeDef(TypedDict):
    applicationId: str
    batchJobIdentifier: BatchJobIdentifierTypeDef
    endTime: datetime
    executionId: str
    jobId: str
    jobName: str
    jobStepRestartMarker: JobStepRestartMarkerTypeDef
    jobType: BatchJobTypeType
    jobUser: str
    returnCode: str
    startTime: datetime
    status: BatchJobExecutionStatusType
    statusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartBatchJobRequestTypeDef(TypedDict):
    applicationId: str
    batchJobIdentifier: BatchJobIdentifierTypeDef
    authSecretsManagerArn: NotRequired[str]
    jobParams: NotRequired[Mapping[str, str]]

class DataSetTypeDef(TypedDict):
    datasetName: str
    datasetOrg: DatasetOrgAttributesTypeDef
    recordLength: RecordLengthTypeDef
    relativePath: NotRequired[str]
    storageType: NotRequired[str]

class GetDataSetDetailsResponseTypeDef(TypedDict):
    blocksize: int
    creationTime: datetime
    dataSetName: str
    dataSetOrg: DatasetDetailOrgAttributesTypeDef
    fileSize: int
    lastReferencedTime: datetime
    lastUpdatedTime: datetime
    location: str
    recordLength: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListBatchJobExecutionsResponseTypeDef(TypedDict):
    batchJobExecutions: List[BatchJobExecutionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DataSetImportItemTypeDef(TypedDict):
    dataSet: DataSetTypeDef
    externalLocation: ExternalLocationTypeDef

class DataSetImportConfigTypeDef(TypedDict):
    dataSets: NotRequired[Sequence[DataSetImportItemTypeDef]]
    s3Location: NotRequired[str]

class CreateDataSetImportTaskRequestTypeDef(TypedDict):
    applicationId: str
    importConfig: DataSetImportConfigTypeDef
    clientToken: NotRequired[str]
