"""
Type annotations for migrationhubstrategy service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/type_defs.html)

Usage::

    ```python
    from mypy_boto3_migrationhubstrategy.type_defs import AntipatternSeveritySummaryTypeDef

    data: AntipatternSeveritySummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AntipatternReportStatusType,
    ApplicationComponentCriteriaType,
    AppTypeType,
    AssessmentStatusType,
    AwsManagedTargetDestinationType,
    CollectorHealthType,
    DatabaseManagementPreferenceType,
    DataSourceTypeType,
    HeterogeneousTargetDatabaseEngineType,
    ImportFileTaskStatusType,
    InclusionStatusType,
    NoPreferenceTargetDestinationType,
    OSTypeType,
    OutputFormatType,
    RecommendationReportStatusType,
    ResourceSubTypeType,
    RunTimeAssessmentStatusType,
    SelfManageTargetDestinationType,
    ServerCriteriaType,
    ServerOsTypeType,
    SeverityType,
    SortOrderType,
    SrcCodeOrDbAnalysisStatusType,
    StrategyRecommendationType,
    StrategyType,
    TargetDatabaseEngineType,
    TargetDestinationType,
    TransformationToolNameType,
    VersionControlType,
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
    "AntipatternSeveritySummaryTypeDef",
    "ApplicationComponentDetailTypeDef",
    "ApplicationComponentStrategyTypeDef",
    "ApplicationComponentSummaryTypeDef",
    "ApplicationPreferencesTypeDef",
    "AssessmentSummaryTypeDef",
    "AssociatedApplicationTypeDef",
    "AwsManagedResourcesTypeDef",
    "BusinessGoalsTypeDef",
    "CollectorTypeDef",
    "DataCollectionDetailsTypeDef",
    "DatabaseConfigDetailTypeDef",
    "DatabaseMigrationPreferenceTypeDef",
    "DatabasePreferencesTypeDef",
    "GetApplicationComponentDetailsRequestRequestTypeDef",
    "GetApplicationComponentDetailsResponseTypeDef",
    "GetApplicationComponentStrategiesRequestRequestTypeDef",
    "GetApplicationComponentStrategiesResponseTypeDef",
    "GetAssessmentRequestRequestTypeDef",
    "GetAssessmentResponseTypeDef",
    "GetImportFileTaskRequestRequestTypeDef",
    "GetImportFileTaskResponseTypeDef",
    "GetPortfolioPreferencesResponseTypeDef",
    "GetPortfolioSummaryResponseTypeDef",
    "GetRecommendationReportDetailsRequestRequestTypeDef",
    "GetRecommendationReportDetailsResponseTypeDef",
    "GetServerDetailsRequestRequestTypeDef",
    "GetServerDetailsResponseTypeDef",
    "GetServerStrategiesRequestRequestTypeDef",
    "GetServerStrategiesResponseTypeDef",
    "GroupTypeDef",
    "HeterogeneousTypeDef",
    "HomogeneousTypeDef",
    "ImportFileTaskInformationTypeDef",
    "ListApplicationComponentsRequestRequestTypeDef",
    "ListApplicationComponentsResponseTypeDef",
    "ListCollectorsRequestRequestTypeDef",
    "ListCollectorsResponseTypeDef",
    "ListImportFileTaskRequestRequestTypeDef",
    "ListImportFileTaskResponseTypeDef",
    "ListServersRequestRequestTypeDef",
    "ListServersResponseTypeDef",
    "ManagementPreferenceTypeDef",
    "NetworkInfoTypeDef",
    "NoDatabaseMigrationPreferenceTypeDef",
    "NoManagementPreferenceTypeDef",
    "OSInfoTypeDef",
    "PaginatorConfigTypeDef",
    "PrioritizeBusinessGoalsTypeDef",
    "PutPortfolioPreferencesRequestRequestTypeDef",
    "RecommendationReportDetailsTypeDef",
    "RecommendationSetTypeDef",
    "ResponseMetadataTypeDef",
    "S3ObjectTypeDef",
    "SelfManageResourcesTypeDef",
    "ServerDetailTypeDef",
    "ServerStrategyTypeDef",
    "ServerSummaryTypeDef",
    "SourceCodeRepositoryTypeDef",
    "SourceCodeTypeDef",
    "StartAssessmentRequestRequestTypeDef",
    "StartAssessmentResponseTypeDef",
    "StartImportFileTaskRequestRequestTypeDef",
    "StartImportFileTaskResponseTypeDef",
    "StartRecommendationReportGenerationRequestRequestTypeDef",
    "StartRecommendationReportGenerationResponseTypeDef",
    "StopAssessmentRequestRequestTypeDef",
    "StrategyOptionTypeDef",
    "StrategySummaryTypeDef",
    "SystemInfoTypeDef",
    "TransformationToolTypeDef",
    "UpdateApplicationComponentConfigRequestRequestTypeDef",
    "UpdateServerConfigRequestRequestTypeDef",
)

AntipatternSeveritySummaryTypeDef = TypedDict(
    "AntipatternSeveritySummaryTypeDef",
    {
        "count": int,
        "severity": SeverityType,
    },
    total=False,
)

ApplicationComponentDetailTypeDef = TypedDict(
    "ApplicationComponentDetailTypeDef",
    {
        "analysisStatus": SrcCodeOrDbAnalysisStatusType,
        "antipatternReportS3Object": "S3ObjectTypeDef",
        "antipatternReportStatus": AntipatternReportStatusType,
        "antipatternReportStatusMessage": str,
        "appType": AppTypeType,
        "associatedServerId": str,
        "databaseConfigDetail": "DatabaseConfigDetailTypeDef",
        "id": str,
        "inclusionStatus": InclusionStatusType,
        "lastAnalyzedTimestamp": datetime,
        "listAntipatternSeveritySummary": List["AntipatternSeveritySummaryTypeDef"],
        "moreServerAssociationExists": bool,
        "name": str,
        "osDriver": str,
        "osVersion": str,
        "recommendationSet": "RecommendationSetTypeDef",
        "resourceSubType": ResourceSubTypeType,
        "sourceCodeRepositories": List["SourceCodeRepositoryTypeDef"],
        "statusMessage": str,
    },
    total=False,
)

ApplicationComponentStrategyTypeDef = TypedDict(
    "ApplicationComponentStrategyTypeDef",
    {
        "isPreferred": bool,
        "recommendation": "RecommendationSetTypeDef",
        "status": StrategyRecommendationType,
    },
    total=False,
)

ApplicationComponentSummaryTypeDef = TypedDict(
    "ApplicationComponentSummaryTypeDef",
    {
        "appType": AppTypeType,
        "count": int,
    },
    total=False,
)

ApplicationPreferencesTypeDef = TypedDict(
    "ApplicationPreferencesTypeDef",
    {
        "managementPreference": "ManagementPreferenceTypeDef",
    },
    total=False,
)

AssessmentSummaryTypeDef = TypedDict(
    "AssessmentSummaryTypeDef",
    {
        "antipatternReportS3Object": "S3ObjectTypeDef",
        "antipatternReportStatus": AntipatternReportStatusType,
        "antipatternReportStatusMessage": str,
        "lastAnalyzedTimestamp": datetime,
        "listAntipatternSeveritySummary": List["AntipatternSeveritySummaryTypeDef"],
        "listApplicationComponentStrategySummary": List["StrategySummaryTypeDef"],
        "listApplicationComponentSummary": List["ApplicationComponentSummaryTypeDef"],
        "listServerStrategySummary": List["StrategySummaryTypeDef"],
        "listServerSummary": List["ServerSummaryTypeDef"],
    },
    total=False,
)

AssociatedApplicationTypeDef = TypedDict(
    "AssociatedApplicationTypeDef",
    {
        "id": str,
        "name": str,
    },
    total=False,
)

AwsManagedResourcesTypeDef = TypedDict(
    "AwsManagedResourcesTypeDef",
    {
        "targetDestination": List[AwsManagedTargetDestinationType],
    },
)

BusinessGoalsTypeDef = TypedDict(
    "BusinessGoalsTypeDef",
    {
        "licenseCostReduction": int,
        "modernizeInfrastructureWithCloudNativeTechnologies": int,
        "reduceOperationalOverheadWithManagedServices": int,
        "speedOfMigration": int,
    },
    total=False,
)

CollectorTypeDef = TypedDict(
    "CollectorTypeDef",
    {
        "collectorHealth": CollectorHealthType,
        "collectorId": str,
        "collectorVersion": str,
        "hostName": str,
        "ipAddress": str,
        "lastActivityTimeStamp": str,
        "registeredTimeStamp": str,
    },
    total=False,
)

DataCollectionDetailsTypeDef = TypedDict(
    "DataCollectionDetailsTypeDef",
    {
        "completionTime": datetime,
        "failed": int,
        "inProgress": int,
        "servers": int,
        "startTime": datetime,
        "status": AssessmentStatusType,
        "success": int,
    },
    total=False,
)

DatabaseConfigDetailTypeDef = TypedDict(
    "DatabaseConfigDetailTypeDef",
    {
        "secretName": str,
    },
    total=False,
)

DatabaseMigrationPreferenceTypeDef = TypedDict(
    "DatabaseMigrationPreferenceTypeDef",
    {
        "heterogeneous": "HeterogeneousTypeDef",
        "homogeneous": "HomogeneousTypeDef",
        "noPreference": "NoDatabaseMigrationPreferenceTypeDef",
    },
    total=False,
)

DatabasePreferencesTypeDef = TypedDict(
    "DatabasePreferencesTypeDef",
    {
        "databaseManagementPreference": DatabaseManagementPreferenceType,
        "databaseMigrationPreference": "DatabaseMigrationPreferenceTypeDef",
    },
    total=False,
)

GetApplicationComponentDetailsRequestRequestTypeDef = TypedDict(
    "GetApplicationComponentDetailsRequestRequestTypeDef",
    {
        "applicationComponentId": str,
    },
)

GetApplicationComponentDetailsResponseTypeDef = TypedDict(
    "GetApplicationComponentDetailsResponseTypeDef",
    {
        "applicationComponentDetail": "ApplicationComponentDetailTypeDef",
        "associatedApplications": List["AssociatedApplicationTypeDef"],
        "associatedServerIds": List[str],
        "moreApplicationResource": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationComponentStrategiesRequestRequestTypeDef = TypedDict(
    "GetApplicationComponentStrategiesRequestRequestTypeDef",
    {
        "applicationComponentId": str,
    },
)

GetApplicationComponentStrategiesResponseTypeDef = TypedDict(
    "GetApplicationComponentStrategiesResponseTypeDef",
    {
        "applicationComponentStrategies": List["ApplicationComponentStrategyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssessmentRequestRequestTypeDef = TypedDict(
    "GetAssessmentRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetAssessmentResponseTypeDef = TypedDict(
    "GetAssessmentResponseTypeDef",
    {
        "dataCollectionDetails": "DataCollectionDetailsTypeDef",
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImportFileTaskRequestRequestTypeDef = TypedDict(
    "GetImportFileTaskRequestRequestTypeDef",
    {
        "id": str,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPortfolioPreferencesResponseTypeDef = TypedDict(
    "GetPortfolioPreferencesResponseTypeDef",
    {
        "applicationPreferences": "ApplicationPreferencesTypeDef",
        "databasePreferences": "DatabasePreferencesTypeDef",
        "prioritizeBusinessGoals": "PrioritizeBusinessGoalsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPortfolioSummaryResponseTypeDef = TypedDict(
    "GetPortfolioSummaryResponseTypeDef",
    {
        "assessmentSummary": "AssessmentSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommendationReportDetailsRequestRequestTypeDef = TypedDict(
    "GetRecommendationReportDetailsRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetRecommendationReportDetailsResponseTypeDef = TypedDict(
    "GetRecommendationReportDetailsResponseTypeDef",
    {
        "id": str,
        "recommendationReportDetails": "RecommendationReportDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetServerDetailsRequestRequestTypeDef = TypedDict(
    "_RequiredGetServerDetailsRequestRequestTypeDef",
    {
        "serverId": str,
    },
)
_OptionalGetServerDetailsRequestRequestTypeDef = TypedDict(
    "_OptionalGetServerDetailsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class GetServerDetailsRequestRequestTypeDef(
    _RequiredGetServerDetailsRequestRequestTypeDef, _OptionalGetServerDetailsRequestRequestTypeDef
):
    pass

GetServerDetailsResponseTypeDef = TypedDict(
    "GetServerDetailsResponseTypeDef",
    {
        "associatedApplications": List["AssociatedApplicationTypeDef"],
        "nextToken": str,
        "serverDetail": "ServerDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServerStrategiesRequestRequestTypeDef = TypedDict(
    "GetServerStrategiesRequestRequestTypeDef",
    {
        "serverId": str,
    },
)

GetServerStrategiesResponseTypeDef = TypedDict(
    "GetServerStrategiesResponseTypeDef",
    {
        "serverStrategies": List["ServerStrategyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "name": Literal["ExternalId"],
        "value": str,
    },
    total=False,
)

HeterogeneousTypeDef = TypedDict(
    "HeterogeneousTypeDef",
    {
        "targetDatabaseEngine": List[HeterogeneousTargetDatabaseEngineType],
    },
)

HomogeneousTypeDef = TypedDict(
    "HomogeneousTypeDef",
    {
        "targetDatabaseEngine": List[Literal["None specified"]],
    },
    total=False,
)

ImportFileTaskInformationTypeDef = TypedDict(
    "ImportFileTaskInformationTypeDef",
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
    },
    total=False,
)

ListApplicationComponentsRequestRequestTypeDef = TypedDict(
    "ListApplicationComponentsRequestRequestTypeDef",
    {
        "applicationComponentCriteria": ApplicationComponentCriteriaType,
        "filterValue": str,
        "groupIdFilter": List["GroupTypeDef"],
        "maxResults": int,
        "nextToken": str,
        "sort": SortOrderType,
    },
    total=False,
)

ListApplicationComponentsResponseTypeDef = TypedDict(
    "ListApplicationComponentsResponseTypeDef",
    {
        "applicationComponentInfos": List["ApplicationComponentDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCollectorsRequestRequestTypeDef = TypedDict(
    "ListCollectorsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListCollectorsResponseTypeDef = TypedDict(
    "ListCollectorsResponseTypeDef",
    {
        "Collectors": List["CollectorTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImportFileTaskRequestRequestTypeDef = TypedDict(
    "ListImportFileTaskRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListImportFileTaskResponseTypeDef = TypedDict(
    "ListImportFileTaskResponseTypeDef",
    {
        "nextToken": str,
        "taskInfos": List["ImportFileTaskInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServersRequestRequestTypeDef = TypedDict(
    "ListServersRequestRequestTypeDef",
    {
        "filterValue": str,
        "groupIdFilter": List["GroupTypeDef"],
        "maxResults": int,
        "nextToken": str,
        "serverCriteria": ServerCriteriaType,
        "sort": SortOrderType,
    },
    total=False,
)

ListServersResponseTypeDef = TypedDict(
    "ListServersResponseTypeDef",
    {
        "nextToken": str,
        "serverInfos": List["ServerDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ManagementPreferenceTypeDef = TypedDict(
    "ManagementPreferenceTypeDef",
    {
        "awsManagedResources": "AwsManagedResourcesTypeDef",
        "noPreference": "NoManagementPreferenceTypeDef",
        "selfManageResources": "SelfManageResourcesTypeDef",
    },
    total=False,
)

NetworkInfoTypeDef = TypedDict(
    "NetworkInfoTypeDef",
    {
        "interfaceName": str,
        "ipAddress": str,
        "macAddress": str,
        "netMask": str,
    },
)

NoDatabaseMigrationPreferenceTypeDef = TypedDict(
    "NoDatabaseMigrationPreferenceTypeDef",
    {
        "targetDatabaseEngine": List[TargetDatabaseEngineType],
    },
)

NoManagementPreferenceTypeDef = TypedDict(
    "NoManagementPreferenceTypeDef",
    {
        "targetDestination": List[NoPreferenceTargetDestinationType],
    },
)

OSInfoTypeDef = TypedDict(
    "OSInfoTypeDef",
    {
        "type": OSTypeType,
        "version": str,
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

PrioritizeBusinessGoalsTypeDef = TypedDict(
    "PrioritizeBusinessGoalsTypeDef",
    {
        "businessGoals": "BusinessGoalsTypeDef",
    },
    total=False,
)

PutPortfolioPreferencesRequestRequestTypeDef = TypedDict(
    "PutPortfolioPreferencesRequestRequestTypeDef",
    {
        "applicationPreferences": "ApplicationPreferencesTypeDef",
        "databasePreferences": "DatabasePreferencesTypeDef",
        "prioritizeBusinessGoals": "PrioritizeBusinessGoalsTypeDef",
    },
    total=False,
)

RecommendationReportDetailsTypeDef = TypedDict(
    "RecommendationReportDetailsTypeDef",
    {
        "completionTime": datetime,
        "s3Bucket": str,
        "s3Keys": List[str],
        "startTime": datetime,
        "status": RecommendationReportStatusType,
        "statusMessage": str,
    },
    total=False,
)

RecommendationSetTypeDef = TypedDict(
    "RecommendationSetTypeDef",
    {
        "strategy": StrategyType,
        "targetDestination": TargetDestinationType,
        "transformationTool": "TransformationToolTypeDef",
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

S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "s3Bucket": str,
        "s3key": str,
    },
    total=False,
)

SelfManageResourcesTypeDef = TypedDict(
    "SelfManageResourcesTypeDef",
    {
        "targetDestination": List[SelfManageTargetDestinationType],
    },
)

ServerDetailTypeDef = TypedDict(
    "ServerDetailTypeDef",
    {
        "antipatternReportS3Object": "S3ObjectTypeDef",
        "antipatternReportStatus": AntipatternReportStatusType,
        "antipatternReportStatusMessage": str,
        "applicationComponentStrategySummary": List["StrategySummaryTypeDef"],
        "dataCollectionStatus": RunTimeAssessmentStatusType,
        "id": str,
        "lastAnalyzedTimestamp": datetime,
        "listAntipatternSeveritySummary": List["AntipatternSeveritySummaryTypeDef"],
        "name": str,
        "recommendationSet": "RecommendationSetTypeDef",
        "serverType": str,
        "statusMessage": str,
        "systemInfo": "SystemInfoTypeDef",
    },
    total=False,
)

ServerStrategyTypeDef = TypedDict(
    "ServerStrategyTypeDef",
    {
        "isPreferred": bool,
        "numberOfApplicationComponents": int,
        "recommendation": "RecommendationSetTypeDef",
        "status": StrategyRecommendationType,
    },
    total=False,
)

ServerSummaryTypeDef = TypedDict(
    "ServerSummaryTypeDef",
    {
        "ServerOsType": ServerOsTypeType,
        "count": int,
    },
    total=False,
)

SourceCodeRepositoryTypeDef = TypedDict(
    "SourceCodeRepositoryTypeDef",
    {
        "branch": str,
        "repository": str,
        "versionControlType": str,
    },
    total=False,
)

SourceCodeTypeDef = TypedDict(
    "SourceCodeTypeDef",
    {
        "location": str,
        "sourceVersion": str,
        "versionControl": VersionControlType,
    },
    total=False,
)

StartAssessmentRequestRequestTypeDef = TypedDict(
    "StartAssessmentRequestRequestTypeDef",
    {
        "s3bucketForAnalysisData": str,
        "s3bucketForReportData": str,
    },
    total=False,
)

StartAssessmentResponseTypeDef = TypedDict(
    "StartAssessmentResponseTypeDef",
    {
        "assessmentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartImportFileTaskRequestRequestTypeDef = TypedDict(
    "_RequiredStartImportFileTaskRequestRequestTypeDef",
    {
        "S3Bucket": str,
        "name": str,
        "s3key": str,
    },
)
_OptionalStartImportFileTaskRequestRequestTypeDef = TypedDict(
    "_OptionalStartImportFileTaskRequestRequestTypeDef",
    {
        "dataSourceType": DataSourceTypeType,
        "groupId": List["GroupTypeDef"],
        "s3bucketForReportData": str,
    },
    total=False,
)

class StartImportFileTaskRequestRequestTypeDef(
    _RequiredStartImportFileTaskRequestRequestTypeDef,
    _OptionalStartImportFileTaskRequestRequestTypeDef,
):
    pass

StartImportFileTaskResponseTypeDef = TypedDict(
    "StartImportFileTaskResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartRecommendationReportGenerationRequestRequestTypeDef = TypedDict(
    "StartRecommendationReportGenerationRequestRequestTypeDef",
    {
        "groupIdFilter": List["GroupTypeDef"],
        "outputFormat": OutputFormatType,
    },
    total=False,
)

StartRecommendationReportGenerationResponseTypeDef = TypedDict(
    "StartRecommendationReportGenerationResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopAssessmentRequestRequestTypeDef = TypedDict(
    "StopAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
    },
)

StrategyOptionTypeDef = TypedDict(
    "StrategyOptionTypeDef",
    {
        "isPreferred": bool,
        "strategy": StrategyType,
        "targetDestination": TargetDestinationType,
        "toolName": TransformationToolNameType,
    },
    total=False,
)

StrategySummaryTypeDef = TypedDict(
    "StrategySummaryTypeDef",
    {
        "count": int,
        "strategy": StrategyType,
    },
    total=False,
)

SystemInfoTypeDef = TypedDict(
    "SystemInfoTypeDef",
    {
        "cpuArchitecture": str,
        "fileSystemType": str,
        "networkInfoList": List["NetworkInfoTypeDef"],
        "osInfo": "OSInfoTypeDef",
    },
    total=False,
)

TransformationToolTypeDef = TypedDict(
    "TransformationToolTypeDef",
    {
        "description": str,
        "name": TransformationToolNameType,
        "tranformationToolInstallationLink": str,
    },
    total=False,
)

_RequiredUpdateApplicationComponentConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationComponentConfigRequestRequestTypeDef",
    {
        "applicationComponentId": str,
    },
)
_OptionalUpdateApplicationComponentConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationComponentConfigRequestRequestTypeDef",
    {
        "inclusionStatus": InclusionStatusType,
        "secretsManagerKey": str,
        "sourceCodeList": List["SourceCodeTypeDef"],
        "strategyOption": "StrategyOptionTypeDef",
    },
    total=False,
)

class UpdateApplicationComponentConfigRequestRequestTypeDef(
    _RequiredUpdateApplicationComponentConfigRequestRequestTypeDef,
    _OptionalUpdateApplicationComponentConfigRequestRequestTypeDef,
):
    pass

_RequiredUpdateServerConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateServerConfigRequestRequestTypeDef",
    {
        "serverId": str,
    },
)
_OptionalUpdateServerConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateServerConfigRequestRequestTypeDef",
    {
        "strategyOption": "StrategyOptionTypeDef",
    },
    total=False,
)

class UpdateServerConfigRequestRequestTypeDef(
    _RequiredUpdateServerConfigRequestRequestTypeDef,
    _OptionalUpdateServerConfigRequestRequestTypeDef,
):
    pass
