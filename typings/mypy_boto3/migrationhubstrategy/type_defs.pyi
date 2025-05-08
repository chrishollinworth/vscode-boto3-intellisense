"""
Type annotations for migrationhubstrategy service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_migrationhubstrategy.type_defs import AnalysisStatusUnionTypeDef

    data: AnalysisStatusUnionTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AnalysisTypeType,
    AntipatternReportStatusType,
    ApplicationComponentCriteriaType,
    ApplicationModeType,
    AppTypeType,
    AppUnitErrorCategoryType,
    AssessmentDataSourceTypeType,
    AssessmentStatusType,
    AuthTypeType,
    AwsManagedTargetDestinationType,
    BinaryAnalyzerNameType,
    CollectorHealthType,
    ConditionType,
    DatabaseManagementPreferenceType,
    DataSourceTypeType,
    GroupNameType,
    HeterogeneousTargetDatabaseEngineType,
    ImportFileTaskStatusType,
    InclusionStatusType,
    NoPreferenceTargetDestinationType,
    OSTypeType,
    OutputFormatType,
    RecommendationReportStatusType,
    ResourceSubTypeType,
    RuntimeAnalysisStatusType,
    RunTimeAnalyzerNameType,
    RunTimeAssessmentStatusType,
    SelfManageTargetDestinationType,
    ServerCriteriaType,
    ServerErrorCategoryType,
    ServerOsTypeType,
    SeverityType,
    SortOrderType,
    SourceCodeAnalyzerNameType,
    SrcCodeOrDbAnalysisStatusType,
    StrategyRecommendationType,
    StrategyType,
    TargetDatabaseEngineType,
    TargetDestinationType,
    TransformationToolNameType,
    VersionControlType,
    VersionControlTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AnalysisStatusUnionTypeDef",
    "AnalyzableServerSummaryTypeDef",
    "AnalyzerNameUnionTypeDef",
    "AntipatternReportResultTypeDef",
    "AntipatternSeveritySummaryTypeDef",
    "AppUnitErrorTypeDef",
    "ApplicationComponentDetailTypeDef",
    "ApplicationComponentStatusSummaryTypeDef",
    "ApplicationComponentStrategyTypeDef",
    "ApplicationComponentSummaryTypeDef",
    "ApplicationPreferencesOutputTypeDef",
    "ApplicationPreferencesTypeDef",
    "ApplicationPreferencesUnionTypeDef",
    "AssessmentSummaryTypeDef",
    "AssessmentTargetOutputTypeDef",
    "AssessmentTargetTypeDef",
    "AssessmentTargetUnionTypeDef",
    "AssociatedApplicationTypeDef",
    "AwsManagedResourcesOutputTypeDef",
    "AwsManagedResourcesTypeDef",
    "BusinessGoalsTypeDef",
    "CollectorTypeDef",
    "ConfigurationSummaryTypeDef",
    "DataCollectionDetailsTypeDef",
    "DatabaseConfigDetailTypeDef",
    "DatabaseMigrationPreferenceOutputTypeDef",
    "DatabaseMigrationPreferenceTypeDef",
    "DatabasePreferencesOutputTypeDef",
    "DatabasePreferencesTypeDef",
    "DatabasePreferencesUnionTypeDef",
    "GetApplicationComponentDetailsRequestTypeDef",
    "GetApplicationComponentDetailsResponseTypeDef",
    "GetApplicationComponentStrategiesRequestTypeDef",
    "GetApplicationComponentStrategiesResponseTypeDef",
    "GetAssessmentRequestTypeDef",
    "GetAssessmentResponseTypeDef",
    "GetImportFileTaskRequestTypeDef",
    "GetImportFileTaskResponseTypeDef",
    "GetLatestAssessmentIdResponseTypeDef",
    "GetPortfolioPreferencesResponseTypeDef",
    "GetPortfolioSummaryResponseTypeDef",
    "GetRecommendationReportDetailsRequestTypeDef",
    "GetRecommendationReportDetailsResponseTypeDef",
    "GetServerDetailsRequestPaginateTypeDef",
    "GetServerDetailsRequestTypeDef",
    "GetServerDetailsResponseTypeDef",
    "GetServerStrategiesRequestTypeDef",
    "GetServerStrategiesResponseTypeDef",
    "GroupTypeDef",
    "HeterogeneousOutputTypeDef",
    "HeterogeneousTypeDef",
    "HomogeneousOutputTypeDef",
    "HomogeneousTypeDef",
    "IPAddressBasedRemoteInfoTypeDef",
    "ImportFileTaskInformationTypeDef",
    "ListAnalyzableServersRequestPaginateTypeDef",
    "ListAnalyzableServersRequestTypeDef",
    "ListAnalyzableServersResponseTypeDef",
    "ListApplicationComponentsRequestPaginateTypeDef",
    "ListApplicationComponentsRequestTypeDef",
    "ListApplicationComponentsResponseTypeDef",
    "ListCollectorsRequestPaginateTypeDef",
    "ListCollectorsRequestTypeDef",
    "ListCollectorsResponseTypeDef",
    "ListImportFileTaskRequestPaginateTypeDef",
    "ListImportFileTaskRequestTypeDef",
    "ListImportFileTaskResponseTypeDef",
    "ListServersRequestPaginateTypeDef",
    "ListServersRequestTypeDef",
    "ListServersResponseTypeDef",
    "ManagementPreferenceOutputTypeDef",
    "ManagementPreferenceTypeDef",
    "NetworkInfoTypeDef",
    "NoDatabaseMigrationPreferenceOutputTypeDef",
    "NoDatabaseMigrationPreferenceTypeDef",
    "NoManagementPreferenceOutputTypeDef",
    "NoManagementPreferenceTypeDef",
    "OSInfoTypeDef",
    "PaginatorConfigTypeDef",
    "PipelineInfoTypeDef",
    "PrioritizeBusinessGoalsTypeDef",
    "PutPortfolioPreferencesRequestTypeDef",
    "RecommendationReportDetailsTypeDef",
    "RecommendationSetTypeDef",
    "RemoteSourceCodeAnalysisServerInfoTypeDef",
    "ResponseMetadataTypeDef",
    "ResultTypeDef",
    "S3ObjectTypeDef",
    "SelfManageResourcesOutputTypeDef",
    "SelfManageResourcesTypeDef",
    "ServerDetailTypeDef",
    "ServerErrorTypeDef",
    "ServerStatusSummaryTypeDef",
    "ServerStrategyTypeDef",
    "ServerSummaryTypeDef",
    "SourceCodeRepositoryTypeDef",
    "SourceCodeTypeDef",
    "StartAssessmentRequestTypeDef",
    "StartAssessmentResponseTypeDef",
    "StartImportFileTaskRequestTypeDef",
    "StartImportFileTaskResponseTypeDef",
    "StartRecommendationReportGenerationRequestTypeDef",
    "StartRecommendationReportGenerationResponseTypeDef",
    "StopAssessmentRequestTypeDef",
    "StrategyOptionTypeDef",
    "StrategySummaryTypeDef",
    "SystemInfoTypeDef",
    "TransformationToolTypeDef",
    "UpdateApplicationComponentConfigRequestTypeDef",
    "UpdateServerConfigRequestTypeDef",
    "VcenterBasedRemoteInfoTypeDef",
    "VersionControlInfoTypeDef",
)

class AnalysisStatusUnionTypeDef(TypedDict):
    runtimeAnalysisStatus: NotRequired[RuntimeAnalysisStatusType]
    srcCodeOrDbAnalysisStatus: NotRequired[SrcCodeOrDbAnalysisStatusType]

class AnalyzableServerSummaryTypeDef(TypedDict):
    hostname: NotRequired[str]
    ipAddress: NotRequired[str]
    source: NotRequired[str]
    vmId: NotRequired[str]

class AnalyzerNameUnionTypeDef(TypedDict):
    binaryAnalyzerName: NotRequired[BinaryAnalyzerNameType]
    runTimeAnalyzerName: NotRequired[RunTimeAnalyzerNameType]
    sourceCodeAnalyzerName: NotRequired[SourceCodeAnalyzerNameType]

class S3ObjectTypeDef(TypedDict):
    s3Bucket: NotRequired[str]
    s3key: NotRequired[str]

class AntipatternSeveritySummaryTypeDef(TypedDict):
    count: NotRequired[int]
    severity: NotRequired[SeverityType]

class AppUnitErrorTypeDef(TypedDict):
    appUnitErrorCategory: NotRequired[AppUnitErrorCategoryType]

class DatabaseConfigDetailTypeDef(TypedDict):
    secretName: NotRequired[str]

class SourceCodeRepositoryTypeDef(TypedDict):
    branch: NotRequired[str]
    projectName: NotRequired[str]
    repository: NotRequired[str]
    versionControlType: NotRequired[str]

class ApplicationComponentStatusSummaryTypeDef(TypedDict):
    count: NotRequired[int]
    srcCodeOrDbAnalysisStatus: NotRequired[SrcCodeOrDbAnalysisStatusType]

class ApplicationComponentSummaryTypeDef(TypedDict):
    appType: NotRequired[AppTypeType]
    count: NotRequired[int]

class ServerStatusSummaryTypeDef(TypedDict):
    count: NotRequired[int]
    runTimeAssessmentStatus: NotRequired[RunTimeAssessmentStatusType]

class ServerSummaryTypeDef(TypedDict):
    ServerOsType: NotRequired[ServerOsTypeType]
    count: NotRequired[int]

class StrategySummaryTypeDef(TypedDict):
    count: NotRequired[int]
    strategy: NotRequired[StrategyType]

class AssessmentTargetOutputTypeDef(TypedDict):
    condition: ConditionType
    name: str
    values: List[str]

class AssessmentTargetTypeDef(TypedDict):
    condition: ConditionType
    name: str
    values: Sequence[str]

AssociatedApplicationTypeDef = TypedDict(
    "AssociatedApplicationTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
    },
)

class AwsManagedResourcesOutputTypeDef(TypedDict):
    targetDestination: List[AwsManagedTargetDestinationType]

class AwsManagedResourcesTypeDef(TypedDict):
    targetDestination: Sequence[AwsManagedTargetDestinationType]

class BusinessGoalsTypeDef(TypedDict):
    licenseCostReduction: NotRequired[int]
    modernizeInfrastructureWithCloudNativeTechnologies: NotRequired[int]
    reduceOperationalOverheadWithManagedServices: NotRequired[int]
    speedOfMigration: NotRequired[int]

class IPAddressBasedRemoteInfoTypeDef(TypedDict):
    authType: NotRequired[AuthTypeType]
    ipAddressConfigurationTimeStamp: NotRequired[str]
    osType: NotRequired[OSTypeType]

class PipelineInfoTypeDef(TypedDict):
    pipelineConfigurationTimeStamp: NotRequired[str]
    pipelineType: NotRequired[Literal["AZURE_DEVOPS"]]

class RemoteSourceCodeAnalysisServerInfoTypeDef(TypedDict):
    remoteSourceCodeAnalysisServerConfigurationTimestamp: NotRequired[str]

class VcenterBasedRemoteInfoTypeDef(TypedDict):
    osType: NotRequired[OSTypeType]
    vcenterConfigurationTimeStamp: NotRequired[str]

class VersionControlInfoTypeDef(TypedDict):
    versionControlConfigurationTimeStamp: NotRequired[str]
    versionControlType: NotRequired[VersionControlTypeType]

class DataCollectionDetailsTypeDef(TypedDict):
    completionTime: NotRequired[datetime]
    failed: NotRequired[int]
    inProgress: NotRequired[int]
    servers: NotRequired[int]
    startTime: NotRequired[datetime]
    status: NotRequired[AssessmentStatusType]
    statusMessage: NotRequired[str]
    success: NotRequired[int]

class HeterogeneousOutputTypeDef(TypedDict):
    targetDatabaseEngine: List[HeterogeneousTargetDatabaseEngineType]

class HomogeneousOutputTypeDef(TypedDict):
    targetDatabaseEngine: NotRequired[List[Literal["None specified"]]]

class NoDatabaseMigrationPreferenceOutputTypeDef(TypedDict):
    targetDatabaseEngine: List[TargetDatabaseEngineType]

class HeterogeneousTypeDef(TypedDict):
    targetDatabaseEngine: Sequence[HeterogeneousTargetDatabaseEngineType]

class HomogeneousTypeDef(TypedDict):
    targetDatabaseEngine: NotRequired[Sequence[Literal["None specified"]]]

class NoDatabaseMigrationPreferenceTypeDef(TypedDict):
    targetDatabaseEngine: Sequence[TargetDatabaseEngineType]

class GetApplicationComponentDetailsRequestTypeDef(TypedDict):
    applicationComponentId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetApplicationComponentStrategiesRequestTypeDef(TypedDict):
    applicationComponentId: str

GetAssessmentRequestTypeDef = TypedDict(
    "GetAssessmentRequestTypeDef",
    {
        "id": str,
    },
)
GetImportFileTaskRequestTypeDef = TypedDict(
    "GetImportFileTaskRequestTypeDef",
    {
        "id": str,
    },
)
GetRecommendationReportDetailsRequestTypeDef = TypedDict(
    "GetRecommendationReportDetailsRequestTypeDef",
    {
        "id": str,
    },
)

class RecommendationReportDetailsTypeDef(TypedDict):
    completionTime: NotRequired[datetime]
    s3Bucket: NotRequired[str]
    s3Keys: NotRequired[List[str]]
    startTime: NotRequired[datetime]
    status: NotRequired[RecommendationReportStatusType]
    statusMessage: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetServerDetailsRequestTypeDef(TypedDict):
    serverId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class GetServerStrategiesRequestTypeDef(TypedDict):
    serverId: str

class GroupTypeDef(TypedDict):
    name: NotRequired[GroupNameType]
    value: NotRequired[str]

ImportFileTaskInformationTypeDef = TypedDict(
    "ImportFileTaskInformationTypeDef",
    {
        "completionTime": NotRequired[datetime],
        "id": NotRequired[str],
        "importName": NotRequired[str],
        "inputS3Bucket": NotRequired[str],
        "inputS3Key": NotRequired[str],
        "numberOfRecordsFailed": NotRequired[int],
        "numberOfRecordsSuccess": NotRequired[int],
        "startTime": NotRequired[datetime],
        "status": NotRequired[ImportFileTaskStatusType],
        "statusReportS3Bucket": NotRequired[str],
        "statusReportS3Key": NotRequired[str],
    },
)

class ListAnalyzableServersRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sort: NotRequired[SortOrderType]

class ListCollectorsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListImportFileTaskRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class NoManagementPreferenceOutputTypeDef(TypedDict):
    targetDestination: List[NoPreferenceTargetDestinationType]

class SelfManageResourcesOutputTypeDef(TypedDict):
    targetDestination: List[SelfManageTargetDestinationType]

class NoManagementPreferenceTypeDef(TypedDict):
    targetDestination: Sequence[NoPreferenceTargetDestinationType]

class SelfManageResourcesTypeDef(TypedDict):
    targetDestination: Sequence[SelfManageTargetDestinationType]

class NetworkInfoTypeDef(TypedDict):
    interfaceName: str
    ipAddress: str
    macAddress: str
    netMask: str

OSInfoTypeDef = TypedDict(
    "OSInfoTypeDef",
    {
        "type": NotRequired[OSTypeType],
        "version": NotRequired[str],
    },
)

class TransformationToolTypeDef(TypedDict):
    description: NotRequired[str]
    name: NotRequired[TransformationToolNameType]
    tranformationToolInstallationLink: NotRequired[str]

class ServerErrorTypeDef(TypedDict):
    serverErrorCategory: NotRequired[ServerErrorCategoryType]

class SourceCodeTypeDef(TypedDict):
    location: NotRequired[str]
    projectName: NotRequired[str]
    sourceVersion: NotRequired[str]
    versionControl: NotRequired[VersionControlType]

class StopAssessmentRequestTypeDef(TypedDict):
    assessmentId: str

class StrategyOptionTypeDef(TypedDict):
    isPreferred: NotRequired[bool]
    strategy: NotRequired[StrategyType]
    targetDestination: NotRequired[TargetDestinationType]
    toolName: NotRequired[TransformationToolNameType]

class AntipatternReportResultTypeDef(TypedDict):
    analyzerName: NotRequired[AnalyzerNameUnionTypeDef]
    antiPatternReportS3Object: NotRequired[S3ObjectTypeDef]
    antipatternReportStatus: NotRequired[AntipatternReportStatusType]
    antipatternReportStatusMessage: NotRequired[str]

class AssessmentSummaryTypeDef(TypedDict):
    antipatternReportS3Object: NotRequired[S3ObjectTypeDef]
    antipatternReportStatus: NotRequired[AntipatternReportStatusType]
    antipatternReportStatusMessage: NotRequired[str]
    lastAnalyzedTimestamp: NotRequired[datetime]
    listAntipatternSeveritySummary: NotRequired[List[AntipatternSeveritySummaryTypeDef]]
    listApplicationComponentStatusSummary: NotRequired[
        List[ApplicationComponentStatusSummaryTypeDef]
    ]
    listApplicationComponentStrategySummary: NotRequired[List[StrategySummaryTypeDef]]
    listApplicationComponentSummary: NotRequired[List[ApplicationComponentSummaryTypeDef]]
    listServerStatusSummary: NotRequired[List[ServerStatusSummaryTypeDef]]
    listServerStrategySummary: NotRequired[List[StrategySummaryTypeDef]]
    listServerSummary: NotRequired[List[ServerSummaryTypeDef]]

AssessmentTargetUnionTypeDef = Union[AssessmentTargetTypeDef, AssessmentTargetOutputTypeDef]

class PrioritizeBusinessGoalsTypeDef(TypedDict):
    businessGoals: NotRequired[BusinessGoalsTypeDef]

class ConfigurationSummaryTypeDef(TypedDict):
    ipAddressBasedRemoteInfoList: NotRequired[List[IPAddressBasedRemoteInfoTypeDef]]
    pipelineInfoList: NotRequired[List[PipelineInfoTypeDef]]
    remoteSourceCodeAnalysisServerInfo: NotRequired[RemoteSourceCodeAnalysisServerInfoTypeDef]
    vcenterBasedRemoteInfoList: NotRequired[List[VcenterBasedRemoteInfoTypeDef]]
    versionControlInfoList: NotRequired[List[VersionControlInfoTypeDef]]

class DatabaseMigrationPreferenceOutputTypeDef(TypedDict):
    heterogeneous: NotRequired[HeterogeneousOutputTypeDef]
    homogeneous: NotRequired[HomogeneousOutputTypeDef]
    noPreference: NotRequired[NoDatabaseMigrationPreferenceOutputTypeDef]

class DatabaseMigrationPreferenceTypeDef(TypedDict):
    heterogeneous: NotRequired[HeterogeneousTypeDef]
    homogeneous: NotRequired[HomogeneousTypeDef]
    noPreference: NotRequired[NoDatabaseMigrationPreferenceTypeDef]

GetAssessmentResponseTypeDef = TypedDict(
    "GetAssessmentResponseTypeDef",
    {
        "assessmentTargets": List[AssessmentTargetOutputTypeDef],
        "dataCollectionDetails": DataCollectionDetailsTypeDef,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImportFileTaskResponseTypeDef = TypedDict(
    "GetImportFileTaskResponseTypeDef",
    {
        "completionTime": datetime,
        "id": str,
        "importName": str,
        "inputS3Bucket": str,
        "inputS3Key": str,
        "numberOfRecordsFailed": int,
        "numberOfRecordsSuccess": int,
        "startTime": datetime,
        "status": ImportFileTaskStatusType,
        "statusReportS3Bucket": str,
        "statusReportS3Key": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLatestAssessmentIdResponseTypeDef = TypedDict(
    "GetLatestAssessmentIdResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListAnalyzableServersResponseTypeDef(TypedDict):
    analyzableServers: List[AnalyzableServerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartAssessmentResponseTypeDef(TypedDict):
    assessmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

StartImportFileTaskResponseTypeDef = TypedDict(
    "StartImportFileTaskResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartRecommendationReportGenerationResponseTypeDef = TypedDict(
    "StartRecommendationReportGenerationResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRecommendationReportDetailsResponseTypeDef = TypedDict(
    "GetRecommendationReportDetailsResponseTypeDef",
    {
        "id": str,
        "recommendationReportDetails": RecommendationReportDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetServerDetailsRequestPaginateTypeDef(TypedDict):
    serverId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAnalyzableServersRequestPaginateTypeDef(TypedDict):
    sort: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCollectorsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListImportFileTaskRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListApplicationComponentsRequestPaginateTypeDef(TypedDict):
    applicationComponentCriteria: NotRequired[ApplicationComponentCriteriaType]
    filterValue: NotRequired[str]
    groupIdFilter: NotRequired[Sequence[GroupTypeDef]]
    sort: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListApplicationComponentsRequestTypeDef(TypedDict):
    applicationComponentCriteria: NotRequired[ApplicationComponentCriteriaType]
    filterValue: NotRequired[str]
    groupIdFilter: NotRequired[Sequence[GroupTypeDef]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sort: NotRequired[SortOrderType]

class ListServersRequestPaginateTypeDef(TypedDict):
    filterValue: NotRequired[str]
    groupIdFilter: NotRequired[Sequence[GroupTypeDef]]
    serverCriteria: NotRequired[ServerCriteriaType]
    sort: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServersRequestTypeDef(TypedDict):
    filterValue: NotRequired[str]
    groupIdFilter: NotRequired[Sequence[GroupTypeDef]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    serverCriteria: NotRequired[ServerCriteriaType]
    sort: NotRequired[SortOrderType]

class StartImportFileTaskRequestTypeDef(TypedDict):
    S3Bucket: str
    name: str
    s3key: str
    dataSourceType: NotRequired[DataSourceTypeType]
    groupId: NotRequired[Sequence[GroupTypeDef]]
    s3bucketForReportData: NotRequired[str]

class StartRecommendationReportGenerationRequestTypeDef(TypedDict):
    groupIdFilter: NotRequired[Sequence[GroupTypeDef]]
    outputFormat: NotRequired[OutputFormatType]

class ListImportFileTaskResponseTypeDef(TypedDict):
    taskInfos: List[ImportFileTaskInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ManagementPreferenceOutputTypeDef(TypedDict):
    awsManagedResources: NotRequired[AwsManagedResourcesOutputTypeDef]
    noPreference: NotRequired[NoManagementPreferenceOutputTypeDef]
    selfManageResources: NotRequired[SelfManageResourcesOutputTypeDef]

class ManagementPreferenceTypeDef(TypedDict):
    awsManagedResources: NotRequired[AwsManagedResourcesTypeDef]
    noPreference: NotRequired[NoManagementPreferenceTypeDef]
    selfManageResources: NotRequired[SelfManageResourcesTypeDef]

class SystemInfoTypeDef(TypedDict):
    cpuArchitecture: NotRequired[str]
    fileSystemType: NotRequired[str]
    networkInfoList: NotRequired[List[NetworkInfoTypeDef]]
    osInfo: NotRequired[OSInfoTypeDef]

class RecommendationSetTypeDef(TypedDict):
    strategy: NotRequired[StrategyType]
    targetDestination: NotRequired[TargetDestinationType]
    transformationTool: NotRequired[TransformationToolTypeDef]

class UpdateApplicationComponentConfigRequestTypeDef(TypedDict):
    applicationComponentId: str
    appType: NotRequired[AppTypeType]
    configureOnly: NotRequired[bool]
    inclusionStatus: NotRequired[InclusionStatusType]
    secretsManagerKey: NotRequired[str]
    sourceCodeList: NotRequired[Sequence[SourceCodeTypeDef]]
    strategyOption: NotRequired[StrategyOptionTypeDef]

class UpdateServerConfigRequestTypeDef(TypedDict):
    serverId: str
    strategyOption: NotRequired[StrategyOptionTypeDef]

class ResultTypeDef(TypedDict):
    analysisStatus: NotRequired[AnalysisStatusUnionTypeDef]
    analysisType: NotRequired[AnalysisTypeType]
    antipatternReportResultList: NotRequired[List[AntipatternReportResultTypeDef]]
    statusMessage: NotRequired[str]

class GetPortfolioSummaryResponseTypeDef(TypedDict):
    assessmentSummary: AssessmentSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartAssessmentRequestTypeDef(TypedDict):
    assessmentDataSourceType: NotRequired[AssessmentDataSourceTypeType]
    assessmentTargets: NotRequired[Sequence[AssessmentTargetUnionTypeDef]]
    s3bucketForAnalysisData: NotRequired[str]
    s3bucketForReportData: NotRequired[str]

class CollectorTypeDef(TypedDict):
    collectorHealth: NotRequired[CollectorHealthType]
    collectorId: NotRequired[str]
    collectorVersion: NotRequired[str]
    configurationSummary: NotRequired[ConfigurationSummaryTypeDef]
    hostName: NotRequired[str]
    ipAddress: NotRequired[str]
    lastActivityTimeStamp: NotRequired[str]
    registeredTimeStamp: NotRequired[str]

class DatabasePreferencesOutputTypeDef(TypedDict):
    databaseManagementPreference: NotRequired[DatabaseManagementPreferenceType]
    databaseMigrationPreference: NotRequired[DatabaseMigrationPreferenceOutputTypeDef]

class DatabasePreferencesTypeDef(TypedDict):
    databaseManagementPreference: NotRequired[DatabaseManagementPreferenceType]
    databaseMigrationPreference: NotRequired[DatabaseMigrationPreferenceTypeDef]

class ApplicationPreferencesOutputTypeDef(TypedDict):
    managementPreference: NotRequired[ManagementPreferenceOutputTypeDef]

class ApplicationPreferencesTypeDef(TypedDict):
    managementPreference: NotRequired[ManagementPreferenceTypeDef]

class ApplicationComponentStrategyTypeDef(TypedDict):
    isPreferred: NotRequired[bool]
    recommendation: NotRequired[RecommendationSetTypeDef]
    status: NotRequired[StrategyRecommendationType]

ServerDetailTypeDef = TypedDict(
    "ServerDetailTypeDef",
    {
        "antipatternReportS3Object": NotRequired[S3ObjectTypeDef],
        "antipatternReportStatus": NotRequired[AntipatternReportStatusType],
        "antipatternReportStatusMessage": NotRequired[str],
        "applicationComponentStrategySummary": NotRequired[List[StrategySummaryTypeDef]],
        "dataCollectionStatus": NotRequired[RunTimeAssessmentStatusType],
        "id": NotRequired[str],
        "lastAnalyzedTimestamp": NotRequired[datetime],
        "listAntipatternSeveritySummary": NotRequired[List[AntipatternSeveritySummaryTypeDef]],
        "name": NotRequired[str],
        "recommendationSet": NotRequired[RecommendationSetTypeDef],
        "serverError": NotRequired[ServerErrorTypeDef],
        "serverType": NotRequired[str],
        "statusMessage": NotRequired[str],
        "systemInfo": NotRequired[SystemInfoTypeDef],
    },
)

class ServerStrategyTypeDef(TypedDict):
    isPreferred: NotRequired[bool]
    numberOfApplicationComponents: NotRequired[int]
    recommendation: NotRequired[RecommendationSetTypeDef]
    status: NotRequired[StrategyRecommendationType]

ApplicationComponentDetailTypeDef = TypedDict(
    "ApplicationComponentDetailTypeDef",
    {
        "analysisStatus": NotRequired[SrcCodeOrDbAnalysisStatusType],
        "antipatternReportS3Object": NotRequired[S3ObjectTypeDef],
        "antipatternReportStatus": NotRequired[AntipatternReportStatusType],
        "antipatternReportStatusMessage": NotRequired[str],
        "appType": NotRequired[AppTypeType],
        "appUnitError": NotRequired[AppUnitErrorTypeDef],
        "associatedServerId": NotRequired[str],
        "databaseConfigDetail": NotRequired[DatabaseConfigDetailTypeDef],
        "id": NotRequired[str],
        "inclusionStatus": NotRequired[InclusionStatusType],
        "lastAnalyzedTimestamp": NotRequired[datetime],
        "listAntipatternSeveritySummary": NotRequired[List[AntipatternSeveritySummaryTypeDef]],
        "moreServerAssociationExists": NotRequired[bool],
        "name": NotRequired[str],
        "osDriver": NotRequired[str],
        "osVersion": NotRequired[str],
        "recommendationSet": NotRequired[RecommendationSetTypeDef],
        "resourceSubType": NotRequired[ResourceSubTypeType],
        "resultList": NotRequired[List[ResultTypeDef]],
        "runtimeStatus": NotRequired[RuntimeAnalysisStatusType],
        "runtimeStatusMessage": NotRequired[str],
        "sourceCodeRepositories": NotRequired[List[SourceCodeRepositoryTypeDef]],
        "statusMessage": NotRequired[str],
    },
)

class ListCollectorsResponseTypeDef(TypedDict):
    Collectors: List[CollectorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

DatabasePreferencesUnionTypeDef = Union[
    DatabasePreferencesTypeDef, DatabasePreferencesOutputTypeDef
]

class GetPortfolioPreferencesResponseTypeDef(TypedDict):
    applicationMode: ApplicationModeType
    applicationPreferences: ApplicationPreferencesOutputTypeDef
    databasePreferences: DatabasePreferencesOutputTypeDef
    prioritizeBusinessGoals: PrioritizeBusinessGoalsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

ApplicationPreferencesUnionTypeDef = Union[
    ApplicationPreferencesTypeDef, ApplicationPreferencesOutputTypeDef
]

class GetApplicationComponentStrategiesResponseTypeDef(TypedDict):
    applicationComponentStrategies: List[ApplicationComponentStrategyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetServerDetailsResponseTypeDef(TypedDict):
    associatedApplications: List[AssociatedApplicationTypeDef]
    serverDetail: ServerDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListServersResponseTypeDef(TypedDict):
    serverInfos: List[ServerDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetServerStrategiesResponseTypeDef(TypedDict):
    serverStrategies: List[ServerStrategyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationComponentDetailsResponseTypeDef(TypedDict):
    applicationComponentDetail: ApplicationComponentDetailTypeDef
    associatedApplications: List[AssociatedApplicationTypeDef]
    associatedServerIds: List[str]
    moreApplicationResource: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationComponentsResponseTypeDef(TypedDict):
    applicationComponentInfos: List[ApplicationComponentDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PutPortfolioPreferencesRequestTypeDef(TypedDict):
    applicationMode: NotRequired[ApplicationModeType]
    applicationPreferences: NotRequired[ApplicationPreferencesUnionTypeDef]
    databasePreferences: NotRequired[DatabasePreferencesUnionTypeDef]
    prioritizeBusinessGoals: NotRequired[PrioritizeBusinessGoalsTypeDef]
