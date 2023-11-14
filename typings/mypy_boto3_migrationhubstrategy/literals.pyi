"""
Type annotations for migrationhubstrategy service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/literals.html)

Usage::

    ```python
    from mypy_boto3_migrationhubstrategy.literals import AnalysisTypeType

    data: AnalysisTypeType = "BINARY_ANALYSIS"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AnalysisTypeType",
    "AntipatternReportStatusType",
    "AppTypeType",
    "AppUnitErrorCategoryType",
    "ApplicationComponentCriteriaType",
    "ApplicationModeType",
    "AssessmentDataSourceTypeType",
    "AssessmentStatusType",
    "AuthTypeType",
    "AwsManagedTargetDestinationType",
    "BinaryAnalyzerNameType",
    "CollectorHealthType",
    "ConditionType",
    "DataSourceTypeType",
    "DatabaseManagementPreferenceType",
    "GetServerDetailsPaginatorName",
    "GroupNameType",
    "HeterogeneousTargetDatabaseEngineType",
    "HomogeneousTargetDatabaseEngineType",
    "ImportFileTaskStatusType",
    "InclusionStatusType",
    "ListAnalyzableServersPaginatorName",
    "ListApplicationComponentsPaginatorName",
    "ListCollectorsPaginatorName",
    "ListImportFileTaskPaginatorName",
    "ListServersPaginatorName",
    "NoPreferenceTargetDestinationType",
    "OSTypeType",
    "OutputFormatType",
    "PipelineTypeType",
    "RecommendationReportStatusType",
    "ResourceSubTypeType",
    "RunTimeAnalyzerNameType",
    "RunTimeAssessmentStatusType",
    "RuntimeAnalysisStatusType",
    "SelfManageTargetDestinationType",
    "ServerCriteriaType",
    "ServerErrorCategoryType",
    "ServerOsTypeType",
    "SeverityType",
    "SortOrderType",
    "SourceCodeAnalyzerNameType",
    "SrcCodeOrDbAnalysisStatusType",
    "StrategyRecommendationType",
    "StrategyType",
    "TargetDatabaseEngineType",
    "TargetDestinationType",
    "TransformationToolNameType",
    "VersionControlType",
    "VersionControlTypeType",
)

AnalysisTypeType = Literal[
    "BINARY_ANALYSIS", "DATABASE_ANALYSIS", "RUNTIME_ANALYSIS", "SOURCE_CODE_ANALYSIS"
]
AntipatternReportStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCESS"]
AppTypeType = Literal[
    "Cassandra",
    "DB2",
    "DotNetFramework",
    "Dotnet",
    "DotnetCore",
    "IBM WebSphere",
    "IIS",
    "JBoss",
    "Java",
    "Maria DB",
    "Mongo DB",
    "MySQL",
    "Oracle",
    "Oracle WebLogic",
    "Other",
    "PostgreSQLServer",
    "SQLServer",
    "Spring",
    "Sybase",
    "Tomcat",
    "Unknown",
    "Visual Basic",
]
AppUnitErrorCategoryType = Literal[
    "CONNECTIVITY_ERROR", "CREDENTIAL_ERROR", "OTHER_ERROR", "PERMISSION_ERROR", "UNSUPPORTED_ERROR"
]
ApplicationComponentCriteriaType = Literal[
    "ANALYSIS_STATUS",
    "APP_NAME",
    "APP_TYPE",
    "DESTINATION",
    "ERROR_CATEGORY",
    "NOT_DEFINED",
    "SERVER_ID",
    "STRATEGY",
]
ApplicationModeType = Literal["ALL", "KNOWN", "UNKNOWN"]
AssessmentDataSourceTypeType = Literal[
    "ApplicationDiscoveryService", "ManualImport", "StrategyRecommendationsApplicationDataCollector"
]
AssessmentStatusType = Literal["COMPLETE", "FAILED", "IN_PROGRESS", "STOPPED"]
AuthTypeType = Literal["CERT", "NTLM", "SSH"]
AwsManagedTargetDestinationType = Literal["AWS Elastic BeanStalk", "AWS Fargate", "None specified"]
BinaryAnalyzerNameType = Literal["BYTECODE_ANALYZER", "DLL_ANALYZER"]
CollectorHealthType = Literal["COLLECTOR_HEALTHY", "COLLECTOR_UNHEALTHY"]
ConditionType = Literal["CONTAINS", "EQUALS", "NOT_CONTAINS", "NOT_EQUALS"]
DataSourceTypeType = Literal[
    "ApplicationDiscoveryService",
    "Import",
    "MPA",
    "StrategyRecommendationsApplicationDataCollector",
]
DatabaseManagementPreferenceType = Literal["AWS-managed", "No preference", "Self-manage"]
GetServerDetailsPaginatorName = Literal["get_server_details"]
GroupNameType = Literal["ExternalId", "ExternalSourceType"]
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
ListAnalyzableServersPaginatorName = Literal["list_analyzable_servers"]
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
PipelineTypeType = Literal["AZURE_DEVOPS"]
RecommendationReportStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCESS"]
ResourceSubTypeType = Literal["Database", "DatabaseProcess", "Process"]
RunTimeAnalyzerNameType = Literal[
    "A2C_ANALYZER", "DATABASE_ANALYZER", "EMP_PA_ANALYZER", "REHOST_ANALYZER", "SCT_ANALYZER"
]
RunTimeAssessmentStatusType = Literal[
    "dataCollectionTaskFailed",
    "dataCollectionTaskPartialSuccess",
    "dataCollectionTaskScheduled",
    "dataCollectionTaskStarted",
    "dataCollectionTaskStopped",
    "dataCollectionTaskSuccess",
    "dataCollectionTaskToBeScheduled",
]
RuntimeAnalysisStatusType = Literal[
    "ANALYSIS_FAILED", "ANALYSIS_STARTED", "ANALYSIS_SUCCESS", "ANALYSIS_TO_BE_SCHEDULED"
]
SelfManageTargetDestinationType = Literal[
    "Amazon Elastic Cloud Compute (EC2)",
    "Amazon Elastic Container Service (ECS)",
    "Amazon Elastic Kubernetes Service (EKS)",
    "None specified",
]
ServerCriteriaType = Literal[
    "ANALYSIS_STATUS",
    "DESTINATION",
    "ERROR_CATEGORY",
    "NOT_DEFINED",
    "OS_NAME",
    "SERVER_ID",
    "STRATEGY",
]
ServerErrorCategoryType = Literal[
    "ARCHITECTURE_ERROR",
    "CONNECTIVITY_ERROR",
    "CREDENTIAL_ERROR",
    "OTHER_ERROR",
    "PERMISSION_ERROR",
]
ServerOsTypeType = Literal[
    "AmazonLinux", "EndOfSupportWindowsServer", "Other", "Redhat", "WindowsServer"
]
SeverityType = Literal["HIGH", "LOW", "MEDIUM"]
SortOrderType = Literal["ASC", "DESC"]
SourceCodeAnalyzerNameType = Literal[
    "BYTECODE_ANALYZER", "CSHARP_ANALYZER", "JAVA_ANALYZER", "PORTING_ASSISTANT"
]
SrcCodeOrDbAnalysisStatusType = Literal[
    "ANALYSIS_FAILED",
    "ANALYSIS_PARTIAL_SUCCESS",
    "ANALYSIS_STARTED",
    "ANALYSIS_SUCCESS",
    "ANALYSIS_TO_BE_SCHEDULED",
    "CONFIGURED",
    "UNCONFIGURED",
]
StrategyRecommendationType = Literal["notRecommended", "potential", "recommended", "viableOption"]
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
    "Babelfish for Aurora PostgreSQL",
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
VersionControlType = Literal["AZURE_DEVOPS_GIT", "GITHUB", "GITHUB_ENTERPRISE"]
VersionControlTypeType = Literal["AZURE_DEVOPS_GIT", "GITHUB", "GITHUB_ENTERPRISE"]
