"""
Type annotations for migrationhubstrategy service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/literals.html)

Usage::

    ```python
    from mypy_boto3_migrationhubstrategy.literals import AntipatternReportStatusType

    data: AntipatternReportStatusType = "FAILED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AntipatternReportStatusType",
    "AppTypeType",
    "ApplicationComponentCriteriaType",
    "AssessmentStatusType",
    "AwsManagedTargetDestinationType",
    "CollectorHealthType",
    "DataSourceTypeType",
    "DatabaseManagementPreferenceType",
    "GetServerDetailsPaginatorName",
    "GroupNameType",
    "HeterogeneousTargetDatabaseEngineType",
    "HomogeneousTargetDatabaseEngineType",
    "ImportFileTaskStatusType",
    "InclusionStatusType",
    "ListApplicationComponentsPaginatorName",
    "ListCollectorsPaginatorName",
    "ListImportFileTaskPaginatorName",
    "ListServersPaginatorName",
    "NoPreferenceTargetDestinationType",
    "OSTypeType",
    "OutputFormatType",
    "RecommendationReportStatusType",
    "ResourceSubTypeType",
    "RunTimeAssessmentStatusType",
    "SelfManageTargetDestinationType",
    "ServerCriteriaType",
    "ServerOsTypeType",
    "SeverityType",
    "SortOrderType",
    "SrcCodeOrDbAnalysisStatusType",
    "StrategyRecommendationType",
    "StrategyType",
    "TargetDatabaseEngineType",
    "TargetDestinationType",
    "TransformationToolNameType",
    "VersionControlType",
)

AntipatternReportStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCESS"]
AppTypeType = Literal["DotNetFramework", "IIS", "Java", "Oracle", "Other", "SQLServer"]
ApplicationComponentCriteriaType = Literal[
    "APP_NAME", "APP_TYPE", "DESTINATION", "NOT_DEFINED", "SERVER_ID", "STRATEGY"
]
AssessmentStatusType = Literal["COMPLETE", "FAILED", "IN_PROGRESS", "STOPPED"]
AwsManagedTargetDestinationType = Literal["AWS Elastic BeanStalk", "AWS Fargate", "None specified"]
CollectorHealthType = Literal["COLLECTOR_HEALTHY", "COLLECTOR_UNHEALTHY"]
DataSourceTypeType = Literal["ApplicationDiscoveryService", "MPA"]
DatabaseManagementPreferenceType = Literal["AWS-managed", "No preference", "Self-manage"]
GetServerDetailsPaginatorName = Literal["get_server_details"]
GroupNameType = Literal["ExternalId"]
HeterogeneousTargetDatabaseEngineType = Literal[
    "AWS PostgreSQL",
    "Amazon Aurora",
    "Db2 LUW",
    "MariaDB",
    "Microsoft SQL Server",
    "MongoDB",
    "MySQL",
    "None specified",
    "Oracle Database",
    "SAP",
]
HomogeneousTargetDatabaseEngineType = Literal["None specified"]
ImportFileTaskStatusType = Literal[
    "DeleteFailed",
    "DeleteInProgress",
    "DeletePartialSuccess",
    "DeleteSuccess",
    "ImportFailed",
    "ImportInProgress",
    "ImportPartialSuccess",
    "ImportSuccess",
]
InclusionStatusType = Literal["excludeFromAssessment", "includeInAssessment"]
ListApplicationComponentsPaginatorName = Literal["list_application_components"]
ListCollectorsPaginatorName = Literal["list_collectors"]
ListImportFileTaskPaginatorName = Literal["list_import_file_task"]
ListServersPaginatorName = Literal["list_servers"]
NoPreferenceTargetDestinationType = Literal[
    "AWS Elastic BeanStalk",
    "AWS Fargate",
    "Amazon Elastic Cloud Compute (EC2)",
    "Amazon Elastic Container Service (ECS)",
    "Amazon Elastic Kubernetes Service (EKS)",
    "None specified",
]
OSTypeType = Literal["LINUX", "WINDOWS"]
OutputFormatType = Literal["Excel", "Json"]
RecommendationReportStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCESS"]
ResourceSubTypeType = Literal["Database", "DatabaseProcess", "Process"]
RunTimeAssessmentStatusType = Literal[
    "dataCollectionTaskFailed",
    "dataCollectionTaskPartialSuccess",
    "dataCollectionTaskScheduled",
    "dataCollectionTaskStarted",
    "dataCollectionTaskStopped",
    "dataCollectionTaskSuccess",
    "dataCollectionTaskToBeScheduled",
]
SelfManageTargetDestinationType = Literal[
    "Amazon Elastic Cloud Compute (EC2)",
    "Amazon Elastic Container Service (ECS)",
    "Amazon Elastic Kubernetes Service (EKS)",
    "None specified",
]
ServerCriteriaType = Literal["DESTINATION", "NOT_DEFINED", "OS_NAME", "SERVER_ID", "STRATEGY"]
ServerOsTypeType = Literal[
    "AmazonLinux", "EndOfSupportWindowsServer", "Other", "Redhat", "WindowsServer"
]
SeverityType = Literal["HIGH", "LOW", "MEDIUM"]
SortOrderType = Literal["ASC", "DESC"]
SrcCodeOrDbAnalysisStatusType = Literal[
    "ANALYSIS_FAILED", "ANALYSIS_STARTED", "ANALYSIS_SUCCESS", "ANALYSIS_TO_BE_SCHEDULED"
]
StrategyRecommendationType = Literal["notRecommended", "recommended", "viableOption"]
StrategyType = Literal[
    "Refactor", "Rehost", "Relocate", "Replatform", "Repurchase", "Retain", "Retirement"
]
TargetDatabaseEngineType = Literal[
    "AWS PostgreSQL",
    "Amazon Aurora",
    "Db2 LUW",
    "MariaDB",
    "Microsoft SQL Server",
    "MongoDB",
    "MySQL",
    "None specified",
    "Oracle Database",
    "SAP",
]
TargetDestinationType = Literal[
    "AWS Elastic BeanStalk",
    "AWS Fargate",
    "Amazon DocumentDB",
    "Amazon DynamoDB",
    "Amazon Elastic Cloud Compute (EC2)",
    "Amazon Elastic Container Service (ECS)",
    "Amazon Elastic Kubernetes Service (EKS)",
    "Amazon Relational Database Service",
    "Amazon Relational Database Service on MySQL",
    "Amazon Relational Database Service on PostgreSQL",
    "Aurora MySQL",
    "Aurora PostgreSQL",
    "None specified",
]
TransformationToolNameType = Literal[
    "App2Container",
    "Application Migration Service",
    "Database Migration Service",
    "End of Support Migration",
    "In Place Operating System Upgrade",
    "Native SQL Server Backup/Restore",
    "Porting Assistant For .NET",
    "Schema Conversion Tool",
    "Strategy Recommendation Support",
    "Windows Web Application Migration Assistant",
]
VersionControlType = Literal["GITHUB", "GITHUB_ENTERPRISE"]
