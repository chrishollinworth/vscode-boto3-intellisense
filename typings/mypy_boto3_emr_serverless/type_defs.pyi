"""
Type annotations for emr-serverless service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_emr_serverless.type_defs import ApplicationSummaryTypeDef

    data: ApplicationSummaryTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import ApplicationStateType, ArchitectureType, JobRunModeType, JobRunStateType

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
    "ApplicationSummaryTypeDef",
    "ApplicationTypeDef",
    "AutoStartConfigTypeDef",
    "AutoStopConfigTypeDef",
    "CancelJobRunRequestTypeDef",
    "CancelJobRunResponseTypeDef",
    "CloudWatchLoggingConfigurationOutputTypeDef",
    "CloudWatchLoggingConfigurationTypeDef",
    "ConfigurationOutputTypeDef",
    "ConfigurationOverridesOutputTypeDef",
    "ConfigurationOverridesTypeDef",
    "ConfigurationOverridesUnionTypeDef",
    "ConfigurationTypeDef",
    "ConfigurationUnionTypeDef",
    "CreateApplicationRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "DeleteApplicationRequestTypeDef",
    "GetApplicationRequestTypeDef",
    "GetApplicationResponseTypeDef",
    "GetDashboardForJobRunRequestTypeDef",
    "GetDashboardForJobRunResponseTypeDef",
    "GetJobRunRequestTypeDef",
    "GetJobRunResponseTypeDef",
    "HiveTypeDef",
    "ImageConfigurationInputTypeDef",
    "ImageConfigurationTypeDef",
    "InitialCapacityConfigTypeDef",
    "InteractiveConfigurationTypeDef",
    "JobDriverOutputTypeDef",
    "JobDriverTypeDef",
    "JobDriverUnionTypeDef",
    "JobRunAttemptSummaryTypeDef",
    "JobRunSummaryTypeDef",
    "JobRunTypeDef",
    "ListApplicationsRequestPaginateTypeDef",
    "ListApplicationsRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListJobRunAttemptsRequestPaginateTypeDef",
    "ListJobRunAttemptsRequestTypeDef",
    "ListJobRunAttemptsResponseTypeDef",
    "ListJobRunsRequestPaginateTypeDef",
    "ListJobRunsRequestTypeDef",
    "ListJobRunsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ManagedPersistenceMonitoringConfigurationTypeDef",
    "MaximumAllowedResourcesTypeDef",
    "MonitoringConfigurationOutputTypeDef",
    "MonitoringConfigurationTypeDef",
    "MonitoringConfigurationUnionTypeDef",
    "NetworkConfigurationOutputTypeDef",
    "NetworkConfigurationTypeDef",
    "NetworkConfigurationUnionTypeDef",
    "PaginatorConfigTypeDef",
    "PrometheusMonitoringConfigurationTypeDef",
    "ResourceUtilizationTypeDef",
    "ResponseMetadataTypeDef",
    "RetryPolicyTypeDef",
    "S3MonitoringConfigurationTypeDef",
    "SchedulerConfigurationTypeDef",
    "SparkSubmitOutputTypeDef",
    "SparkSubmitTypeDef",
    "StartApplicationRequestTypeDef",
    "StartJobRunRequestTypeDef",
    "StartJobRunResponseTypeDef",
    "StopApplicationRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TimestampTypeDef",
    "TotalResourceUtilizationTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateApplicationRequestTypeDef",
    "UpdateApplicationResponseTypeDef",
    "WorkerResourceConfigTypeDef",
    "WorkerTypeSpecificationInputTypeDef",
    "WorkerTypeSpecificationTypeDef",
)

ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "releaseLabel": str,
        "type": str,
        "state": ApplicationStateType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "name": NotRequired[str],
        "stateDetails": NotRequired[str],
        "architecture": NotRequired[ArchitectureType],
    },
)

class AutoStartConfigTypeDef(TypedDict):
    enabled: NotRequired[bool]

class AutoStopConfigTypeDef(TypedDict):
    enabled: NotRequired[bool]
    idleTimeoutMinutes: NotRequired[int]

class ConfigurationOutputTypeDef(TypedDict):
    classification: str
    properties: NotRequired[Dict[str, str]]
    configurations: NotRequired[List[Dict[str, Any]]]

class ImageConfigurationTypeDef(TypedDict):
    imageUri: str
    resolvedImageDigest: NotRequired[str]

class InteractiveConfigurationTypeDef(TypedDict):
    studioEnabled: NotRequired[bool]
    livyEndpointEnabled: NotRequired[bool]

class MaximumAllowedResourcesTypeDef(TypedDict):
    cpu: str
    memory: str
    disk: NotRequired[str]

class NetworkConfigurationOutputTypeDef(TypedDict):
    subnetIds: NotRequired[List[str]]
    securityGroupIds: NotRequired[List[str]]

class SchedulerConfigurationTypeDef(TypedDict):
    queueTimeoutMinutes: NotRequired[int]
    maxConcurrentRuns: NotRequired[int]

class CancelJobRunRequestTypeDef(TypedDict):
    applicationId: str
    jobRunId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CloudWatchLoggingConfigurationOutputTypeDef(TypedDict):
    enabled: bool
    logGroupName: NotRequired[str]
    logStreamNamePrefix: NotRequired[str]
    encryptionKeyArn: NotRequired[str]
    logTypes: NotRequired[Dict[str, List[str]]]

class CloudWatchLoggingConfigurationTypeDef(TypedDict):
    enabled: bool
    logGroupName: NotRequired[str]
    logStreamNamePrefix: NotRequired[str]
    encryptionKeyArn: NotRequired[str]
    logTypes: NotRequired[Mapping[str, Sequence[str]]]

class ConfigurationTypeDef(TypedDict):
    classification: str
    properties: NotRequired[Mapping[str, str]]
    configurations: NotRequired[Sequence[Mapping[str, Any]]]

class ImageConfigurationInputTypeDef(TypedDict):
    imageUri: NotRequired[str]

class DeleteApplicationRequestTypeDef(TypedDict):
    applicationId: str

class GetApplicationRequestTypeDef(TypedDict):
    applicationId: str

class GetDashboardForJobRunRequestTypeDef(TypedDict):
    applicationId: str
    jobRunId: str
    attempt: NotRequired[int]
    accessSystemProfileLogs: NotRequired[bool]

class GetJobRunRequestTypeDef(TypedDict):
    applicationId: str
    jobRunId: str
    attempt: NotRequired[int]

class HiveTypeDef(TypedDict):
    query: str
    initQueryFile: NotRequired[str]
    parameters: NotRequired[str]

class WorkerResourceConfigTypeDef(TypedDict):
    cpu: str
    memory: str
    disk: NotRequired[str]
    diskType: NotRequired[str]

class SparkSubmitOutputTypeDef(TypedDict):
    entryPoint: str
    entryPointArguments: NotRequired[List[str]]
    sparkSubmitParameters: NotRequired[str]

class SparkSubmitTypeDef(TypedDict):
    entryPoint: str
    entryPointArguments: NotRequired[Sequence[str]]
    sparkSubmitParameters: NotRequired[str]

JobRunAttemptSummaryTypeDef = TypedDict(
    "JobRunAttemptSummaryTypeDef",
    {
        "applicationId": str,
        "id": str,
        "arn": str,
        "createdBy": str,
        "jobCreatedAt": datetime,
        "createdAt": datetime,
        "updatedAt": datetime,
        "executionRole": str,
        "state": JobRunStateType,
        "stateDetails": str,
        "releaseLabel": str,
        "name": NotRequired[str],
        "mode": NotRequired[JobRunModeType],
        "type": NotRequired[str],
        "attempt": NotRequired[int],
    },
)
JobRunSummaryTypeDef = TypedDict(
    "JobRunSummaryTypeDef",
    {
        "applicationId": str,
        "id": str,
        "arn": str,
        "createdBy": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "executionRole": str,
        "state": JobRunStateType,
        "stateDetails": str,
        "releaseLabel": str,
        "name": NotRequired[str],
        "mode": NotRequired[JobRunModeType],
        "type": NotRequired[str],
        "attempt": NotRequired[int],
        "attemptCreatedAt": NotRequired[datetime],
        "attemptUpdatedAt": NotRequired[datetime],
    },
)

class ResourceUtilizationTypeDef(TypedDict):
    vCPUHour: NotRequired[float]
    memoryGBHour: NotRequired[float]
    storageGBHour: NotRequired[float]

class RetryPolicyTypeDef(TypedDict):
    maxAttempts: NotRequired[int]
    maxFailedAttemptsPerHour: NotRequired[int]

class TotalResourceUtilizationTypeDef(TypedDict):
    vCPUHour: NotRequired[float]
    memoryGBHour: NotRequired[float]
    storageGBHour: NotRequired[float]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListApplicationsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    states: NotRequired[Sequence[ApplicationStateType]]

class ListJobRunAttemptsRequestTypeDef(TypedDict):
    applicationId: str
    jobRunId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

TimestampTypeDef = Union[datetime, str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ManagedPersistenceMonitoringConfigurationTypeDef(TypedDict):
    enabled: NotRequired[bool]
    encryptionKeyArn: NotRequired[str]

class PrometheusMonitoringConfigurationTypeDef(TypedDict):
    remoteWriteUrl: NotRequired[str]

class S3MonitoringConfigurationTypeDef(TypedDict):
    logUri: NotRequired[str]
    encryptionKeyArn: NotRequired[str]

class NetworkConfigurationTypeDef(TypedDict):
    subnetIds: NotRequired[Sequence[str]]
    securityGroupIds: NotRequired[Sequence[str]]

class StartApplicationRequestTypeDef(TypedDict):
    applicationId: str

class StopApplicationRequestTypeDef(TypedDict):
    applicationId: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class WorkerTypeSpecificationTypeDef(TypedDict):
    imageConfiguration: NotRequired[ImageConfigurationTypeDef]

class CancelJobRunResponseTypeDef(TypedDict):
    applicationId: str
    jobRunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationResponseTypeDef(TypedDict):
    applicationId: str
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDashboardForJobRunResponseTypeDef(TypedDict):
    url: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsResponseTypeDef(TypedDict):
    applications: List[ApplicationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartJobRunResponseTypeDef(TypedDict):
    applicationId: str
    jobRunId: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

ConfigurationUnionTypeDef = Union[ConfigurationTypeDef, ConfigurationOutputTypeDef]

class WorkerTypeSpecificationInputTypeDef(TypedDict):
    imageConfiguration: NotRequired[ImageConfigurationInputTypeDef]

class InitialCapacityConfigTypeDef(TypedDict):
    workerCount: int
    workerConfiguration: NotRequired[WorkerResourceConfigTypeDef]

class JobDriverOutputTypeDef(TypedDict):
    sparkSubmit: NotRequired[SparkSubmitOutputTypeDef]
    hive: NotRequired[HiveTypeDef]

class JobDriverTypeDef(TypedDict):
    sparkSubmit: NotRequired[SparkSubmitTypeDef]
    hive: NotRequired[HiveTypeDef]

class ListJobRunAttemptsResponseTypeDef(TypedDict):
    jobRunAttempts: List[JobRunAttemptSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListJobRunsResponseTypeDef(TypedDict):
    jobRuns: List[JobRunSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListApplicationsRequestPaginateTypeDef(TypedDict):
    states: NotRequired[Sequence[ApplicationStateType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListJobRunAttemptsRequestPaginateTypeDef(TypedDict):
    applicationId: str
    jobRunId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListJobRunsRequestPaginateTypeDef(TypedDict):
    applicationId: str
    createdAtAfter: NotRequired[TimestampTypeDef]
    createdAtBefore: NotRequired[TimestampTypeDef]
    states: NotRequired[Sequence[JobRunStateType]]
    mode: NotRequired[JobRunModeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListJobRunsRequestTypeDef(TypedDict):
    applicationId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    createdAtAfter: NotRequired[TimestampTypeDef]
    createdAtBefore: NotRequired[TimestampTypeDef]
    states: NotRequired[Sequence[JobRunStateType]]
    mode: NotRequired[JobRunModeType]

class MonitoringConfigurationOutputTypeDef(TypedDict):
    s3MonitoringConfiguration: NotRequired[S3MonitoringConfigurationTypeDef]
    managedPersistenceMonitoringConfiguration: NotRequired[
        ManagedPersistenceMonitoringConfigurationTypeDef
    ]
    cloudWatchLoggingConfiguration: NotRequired[CloudWatchLoggingConfigurationOutputTypeDef]
    prometheusMonitoringConfiguration: NotRequired[PrometheusMonitoringConfigurationTypeDef]

class MonitoringConfigurationTypeDef(TypedDict):
    s3MonitoringConfiguration: NotRequired[S3MonitoringConfigurationTypeDef]
    managedPersistenceMonitoringConfiguration: NotRequired[
        ManagedPersistenceMonitoringConfigurationTypeDef
    ]
    cloudWatchLoggingConfiguration: NotRequired[CloudWatchLoggingConfigurationTypeDef]
    prometheusMonitoringConfiguration: NotRequired[PrometheusMonitoringConfigurationTypeDef]

NetworkConfigurationUnionTypeDef = Union[
    NetworkConfigurationTypeDef, NetworkConfigurationOutputTypeDef
]
JobDriverUnionTypeDef = Union[JobDriverTypeDef, JobDriverOutputTypeDef]
ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "applicationId": str,
        "arn": str,
        "releaseLabel": str,
        "type": str,
        "state": ApplicationStateType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "name": NotRequired[str],
        "stateDetails": NotRequired[str],
        "initialCapacity": NotRequired[Dict[str, InitialCapacityConfigTypeDef]],
        "maximumCapacity": NotRequired[MaximumAllowedResourcesTypeDef],
        "tags": NotRequired[Dict[str, str]],
        "autoStartConfiguration": NotRequired[AutoStartConfigTypeDef],
        "autoStopConfiguration": NotRequired[AutoStopConfigTypeDef],
        "networkConfiguration": NotRequired[NetworkConfigurationOutputTypeDef],
        "architecture": NotRequired[ArchitectureType],
        "imageConfiguration": NotRequired[ImageConfigurationTypeDef],
        "workerTypeSpecifications": NotRequired[Dict[str, WorkerTypeSpecificationTypeDef]],
        "runtimeConfiguration": NotRequired[List[ConfigurationOutputTypeDef]],
        "monitoringConfiguration": NotRequired[MonitoringConfigurationOutputTypeDef],
        "interactiveConfiguration": NotRequired[InteractiveConfigurationTypeDef],
        "schedulerConfiguration": NotRequired[SchedulerConfigurationTypeDef],
    },
)

class ConfigurationOverridesOutputTypeDef(TypedDict):
    applicationConfiguration: NotRequired[List[ConfigurationOutputTypeDef]]
    monitoringConfiguration: NotRequired[MonitoringConfigurationOutputTypeDef]

class ConfigurationOverridesTypeDef(TypedDict):
    applicationConfiguration: NotRequired[Sequence[ConfigurationTypeDef]]
    monitoringConfiguration: NotRequired[MonitoringConfigurationTypeDef]

MonitoringConfigurationUnionTypeDef = Union[
    MonitoringConfigurationTypeDef, MonitoringConfigurationOutputTypeDef
]

class GetApplicationResponseTypeDef(TypedDict):
    application: ApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationResponseTypeDef(TypedDict):
    application: ApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JobRunTypeDef(TypedDict):
    applicationId: str
    jobRunId: str
    arn: str
    createdBy: str
    createdAt: datetime
    updatedAt: datetime
    executionRole: str
    state: JobRunStateType
    stateDetails: str
    releaseLabel: str
    jobDriver: JobDriverOutputTypeDef
    name: NotRequired[str]
    configurationOverrides: NotRequired[ConfigurationOverridesOutputTypeDef]
    tags: NotRequired[Dict[str, str]]
    totalResourceUtilization: NotRequired[TotalResourceUtilizationTypeDef]
    networkConfiguration: NotRequired[NetworkConfigurationOutputTypeDef]
    totalExecutionDurationSeconds: NotRequired[int]
    executionTimeoutMinutes: NotRequired[int]
    billedResourceUtilization: NotRequired[ResourceUtilizationTypeDef]
    mode: NotRequired[JobRunModeType]
    retryPolicy: NotRequired[RetryPolicyTypeDef]
    attempt: NotRequired[int]
    attemptCreatedAt: NotRequired[datetime]
    attemptUpdatedAt: NotRequired[datetime]
    startedAt: NotRequired[datetime]
    endedAt: NotRequired[datetime]
    queuedDurationMilliseconds: NotRequired[int]

ConfigurationOverridesUnionTypeDef = Union[
    ConfigurationOverridesTypeDef, ConfigurationOverridesOutputTypeDef
]
CreateApplicationRequestTypeDef = TypedDict(
    "CreateApplicationRequestTypeDef",
    {
        "releaseLabel": str,
        "type": str,
        "clientToken": str,
        "name": NotRequired[str],
        "initialCapacity": NotRequired[Mapping[str, InitialCapacityConfigTypeDef]],
        "maximumCapacity": NotRequired[MaximumAllowedResourcesTypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "autoStartConfiguration": NotRequired[AutoStartConfigTypeDef],
        "autoStopConfiguration": NotRequired[AutoStopConfigTypeDef],
        "networkConfiguration": NotRequired[NetworkConfigurationUnionTypeDef],
        "architecture": NotRequired[ArchitectureType],
        "imageConfiguration": NotRequired[ImageConfigurationInputTypeDef],
        "workerTypeSpecifications": NotRequired[Mapping[str, WorkerTypeSpecificationInputTypeDef]],
        "runtimeConfiguration": NotRequired[Sequence[ConfigurationUnionTypeDef]],
        "monitoringConfiguration": NotRequired[MonitoringConfigurationUnionTypeDef],
        "interactiveConfiguration": NotRequired[InteractiveConfigurationTypeDef],
        "schedulerConfiguration": NotRequired[SchedulerConfigurationTypeDef],
    },
)

class UpdateApplicationRequestTypeDef(TypedDict):
    applicationId: str
    clientToken: str
    initialCapacity: NotRequired[Mapping[str, InitialCapacityConfigTypeDef]]
    maximumCapacity: NotRequired[MaximumAllowedResourcesTypeDef]
    autoStartConfiguration: NotRequired[AutoStartConfigTypeDef]
    autoStopConfiguration: NotRequired[AutoStopConfigTypeDef]
    networkConfiguration: NotRequired[NetworkConfigurationUnionTypeDef]
    architecture: NotRequired[ArchitectureType]
    imageConfiguration: NotRequired[ImageConfigurationInputTypeDef]
    workerTypeSpecifications: NotRequired[Mapping[str, WorkerTypeSpecificationInputTypeDef]]
    interactiveConfiguration: NotRequired[InteractiveConfigurationTypeDef]
    releaseLabel: NotRequired[str]
    runtimeConfiguration: NotRequired[Sequence[ConfigurationUnionTypeDef]]
    monitoringConfiguration: NotRequired[MonitoringConfigurationUnionTypeDef]
    schedulerConfiguration: NotRequired[SchedulerConfigurationTypeDef]

class GetJobRunResponseTypeDef(TypedDict):
    jobRun: JobRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartJobRunRequestTypeDef(TypedDict):
    applicationId: str
    clientToken: str
    executionRoleArn: str
    jobDriver: NotRequired[JobDriverUnionTypeDef]
    configurationOverrides: NotRequired[ConfigurationOverridesUnionTypeDef]
    tags: NotRequired[Mapping[str, str]]
    executionTimeoutMinutes: NotRequired[int]
    name: NotRequired[str]
    mode: NotRequired[JobRunModeType]
    retryPolicy: NotRequired[RetryPolicyTypeDef]
