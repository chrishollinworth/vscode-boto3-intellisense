# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for glue service client

Usage::

    ```python
    import boto3
    from mypy_boto3_glue import GlueClient

    client: GlueClient = boto3.client("glue")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_glue.paginator import (
    GetClassifiersPaginator,
    GetConnectionsPaginator,
    GetCrawlerMetricsPaginator,
    GetCrawlersPaginator,
    GetDatabasesPaginator,
    GetDevEndpointsPaginator,
    GetJobRunsPaginator,
    GetJobsPaginator,
    GetPartitionsPaginator,
    GetSecurityConfigurationsPaginator,
    GetTablesPaginator,
    GetTableVersionsPaginator,
    GetTriggersPaginator,
    GetUserDefinedFunctionsPaginator,
)
from mypy_boto3_glue.type_defs import (
    ActionTypeDef,
    BatchCreatePartitionResponseTypeDef,
    BatchDeleteConnectionResponseTypeDef,
    BatchDeletePartitionResponseTypeDef,
    BatchDeleteTableResponseTypeDef,
    BatchDeleteTableVersionResponseTypeDef,
    BatchGetCrawlersResponseTypeDef,
    BatchGetDevEndpointsResponseTypeDef,
    BatchGetJobsResponseTypeDef,
    BatchGetPartitionResponseTypeDef,
    BatchGetTriggersResponseTypeDef,
    BatchGetWorkflowsResponseTypeDef,
    BatchStopJobRunResponseTypeDef,
    CancelMLTaskRunResponseTypeDef,
    CatalogEntryTypeDef,
    CodeGenEdgeTypeDef,
    CodeGenNodeTypeDef,
    ColumnStatisticsTypeDef,
    ConnectionInputTypeDef,
    ConnectionsListTypeDef,
    CrawlerTargetsTypeDef,
    CreateCsvClassifierRequestTypeDef,
    CreateDevEndpointResponseTypeDef,
    CreateGrokClassifierRequestTypeDef,
    CreateJobResponseTypeDef,
    CreateJsonClassifierRequestTypeDef,
    CreateMLTransformResponseTypeDef,
    CreateScriptResponseTypeDef,
    CreateSecurityConfigurationResponseTypeDef,
    CreateTriggerResponseTypeDef,
    CreateWorkflowResponseTypeDef,
    CreateXMLClassifierRequestTypeDef,
    DatabaseInputTypeDef,
    DataCatalogEncryptionSettingsTypeDef,
    DeleteJobResponseTypeDef,
    DeleteMLTransformResponseTypeDef,
    DeleteTriggerResponseTypeDef,
    DeleteWorkflowResponseTypeDef,
    DevEndpointCustomLibrariesTypeDef,
    EncryptionConfigurationTypeDef,
    ExecutionPropertyTypeDef,
    GetCatalogImportStatusResponseTypeDef,
    GetClassifierResponseTypeDef,
    GetClassifiersResponseTypeDef,
    GetColumnStatisticsForPartitionResponseTypeDef,
    GetColumnStatisticsForTableResponseTypeDef,
    GetConnectionResponseTypeDef,
    GetConnectionsFilterTypeDef,
    GetConnectionsResponseTypeDef,
    GetCrawlerMetricsResponseTypeDef,
    GetCrawlerResponseTypeDef,
    GetCrawlersResponseTypeDef,
    GetDatabaseResponseTypeDef,
    GetDatabasesResponseTypeDef,
    GetDataCatalogEncryptionSettingsResponseTypeDef,
    GetDataflowGraphResponseTypeDef,
    GetDevEndpointResponseTypeDef,
    GetDevEndpointsResponseTypeDef,
    GetJobBookmarkResponseTypeDef,
    GetJobResponseTypeDef,
    GetJobRunResponseTypeDef,
    GetJobRunsResponseTypeDef,
    GetJobsResponseTypeDef,
    GetMappingResponseTypeDef,
    GetMLTaskRunResponseTypeDef,
    GetMLTaskRunsResponseTypeDef,
    GetMLTransformResponseTypeDef,
    GetMLTransformsResponseTypeDef,
    GetPartitionResponseTypeDef,
    GetPartitionsResponseTypeDef,
    GetPlanResponseTypeDef,
    GetResourcePoliciesResponseTypeDef,
    GetResourcePolicyResponseTypeDef,
    GetSecurityConfigurationResponseTypeDef,
    GetSecurityConfigurationsResponseTypeDef,
    GetTableResponseTypeDef,
    GetTablesResponseTypeDef,
    GetTableVersionResponseTypeDef,
    GetTableVersionsResponseTypeDef,
    GetTagsResponseTypeDef,
    GetTriggerResponseTypeDef,
    GetTriggersResponseTypeDef,
    GetUserDefinedFunctionResponseTypeDef,
    GetUserDefinedFunctionsResponseTypeDef,
    GetWorkflowResponseTypeDef,
    GetWorkflowRunPropertiesResponseTypeDef,
    GetWorkflowRunResponseTypeDef,
    GetWorkflowRunsResponseTypeDef,
    GlueTableTypeDef,
    JobCommandTypeDef,
    JobUpdateTypeDef,
    ListCrawlersResponseTypeDef,
    ListDevEndpointsResponseTypeDef,
    ListJobsResponseTypeDef,
    ListMLTransformsResponseTypeDef,
    ListTriggersResponseTypeDef,
    ListWorkflowsResponseTypeDef,
    LocationTypeDef,
    MappingEntryTypeDef,
    NotificationPropertyTypeDef,
    PartitionInputTypeDef,
    PartitionValueListTypeDef,
    PredicateTypeDef,
    PropertyPredicateTypeDef,
    PutResourcePolicyResponseTypeDef,
    ResetJobBookmarkResponseTypeDef,
    ResumeWorkflowRunResponseTypeDef,
    SchemaChangePolicyTypeDef,
    SearchTablesResponseTypeDef,
    SegmentTypeDef,
    SortCriterionTypeDef,
    StartExportLabelsTaskRunResponseTypeDef,
    StartImportLabelsTaskRunResponseTypeDef,
    StartJobRunResponseTypeDef,
    StartMLEvaluationTaskRunResponseTypeDef,
    StartMLLabelingSetGenerationTaskRunResponseTypeDef,
    StartTriggerResponseTypeDef,
    StartWorkflowRunResponseTypeDef,
    StopTriggerResponseTypeDef,
    TableInputTypeDef,
    TaskRunFilterCriteriaTypeDef,
    TaskRunSortCriteriaTypeDef,
    TransformFilterCriteriaTypeDef,
    TransformParametersTypeDef,
    TransformSortCriteriaTypeDef,
    TriggerUpdateTypeDef,
    UpdateColumnStatisticsForPartitionResponseTypeDef,
    UpdateColumnStatisticsForTableResponseTypeDef,
    UpdateCsvClassifierRequestTypeDef,
    UpdateGrokClassifierRequestTypeDef,
    UpdateJobResponseTypeDef,
    UpdateJsonClassifierRequestTypeDef,
    UpdateMLTransformResponseTypeDef,
    UpdateTriggerResponseTypeDef,
    UpdateWorkflowResponseTypeDef,
    UpdateXMLClassifierRequestTypeDef,
    UserDefinedFunctionInputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GlueClient",)


class Exceptions:
    AccessDeniedException: Type[Boto3ClientError]
    AlreadyExistsException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    ConcurrentModificationException: Type[Boto3ClientError]
    ConcurrentRunsExceededException: Type[Boto3ClientError]
    ConditionCheckFailureException: Type[Boto3ClientError]
    CrawlerNotRunningException: Type[Boto3ClientError]
    CrawlerRunningException: Type[Boto3ClientError]
    CrawlerStoppingException: Type[Boto3ClientError]
    EntityNotFoundException: Type[Boto3ClientError]
    GlueEncryptionException: Type[Boto3ClientError]
    IdempotentParameterMismatchException: Type[Boto3ClientError]
    IllegalWorkflowStateException: Type[Boto3ClientError]
    InternalServiceException: Type[Boto3ClientError]
    InvalidInputException: Type[Boto3ClientError]
    MLTransformNotReadyException: Type[Boto3ClientError]
    NoScheduleException: Type[Boto3ClientError]
    OperationTimeoutException: Type[Boto3ClientError]
    ResourceNumberLimitExceededException: Type[Boto3ClientError]
    SchedulerNotRunningException: Type[Boto3ClientError]
    SchedulerRunningException: Type[Boto3ClientError]
    SchedulerTransitioningException: Type[Boto3ClientError]
    ValidationException: Type[Boto3ClientError]
    VersionMismatchException: Type[Boto3ClientError]


class GlueClient:
    """
    [Glue.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client)
    """

    exceptions: Exceptions

    def batch_create_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionInputList: List[PartitionInputTypeDef],
        CatalogId: str = None,
    ) -> BatchCreatePartitionResponseTypeDef:
        """
        [Client.batch_create_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.batch_create_partition)
        """

    def batch_delete_connection(
        self, ConnectionNameList: List[str], CatalogId: str = None
    ) -> BatchDeleteConnectionResponseTypeDef:
        """
        [Client.batch_delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.batch_delete_connection)
        """

    def batch_delete_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionsToDelete: List["PartitionValueListTypeDef"],
        CatalogId: str = None,
    ) -> BatchDeletePartitionResponseTypeDef:
        """
        [Client.batch_delete_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.batch_delete_partition)
        """

    def batch_delete_table(
        self, DatabaseName: str, TablesToDelete: List[str], CatalogId: str = None
    ) -> BatchDeleteTableResponseTypeDef:
        """
        [Client.batch_delete_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.batch_delete_table)
        """

    def batch_delete_table_version(
        self, DatabaseName: str, TableName: str, VersionIds: List[str], CatalogId: str = None
    ) -> BatchDeleteTableVersionResponseTypeDef:
        """
        [Client.batch_delete_table_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.batch_delete_table_version)
        """

    def batch_get_crawlers(self, CrawlerNames: List[str]) -> BatchGetCrawlersResponseTypeDef:
        """
        [Client.batch_get_crawlers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.batch_get_crawlers)
        """

    def batch_get_dev_endpoints(
        self, DevEndpointNames: List[str]
    ) -> BatchGetDevEndpointsResponseTypeDef:
        """
        [Client.batch_get_dev_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.batch_get_dev_endpoints)
        """

    def batch_get_jobs(self, JobNames: List[str]) -> BatchGetJobsResponseTypeDef:
        """
        [Client.batch_get_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.batch_get_jobs)
        """

    def batch_get_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionsToGet: List["PartitionValueListTypeDef"],
        CatalogId: str = None,
    ) -> BatchGetPartitionResponseTypeDef:
        """
        [Client.batch_get_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.batch_get_partition)
        """

    def batch_get_triggers(self, TriggerNames: List[str]) -> BatchGetTriggersResponseTypeDef:
        """
        [Client.batch_get_triggers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.batch_get_triggers)
        """

    def batch_get_workflows(
        self, Names: List[str], IncludeGraph: bool = None
    ) -> BatchGetWorkflowsResponseTypeDef:
        """
        [Client.batch_get_workflows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.batch_get_workflows)
        """

    def batch_stop_job_run(
        self, JobName: str, JobRunIds: List[str]
    ) -> BatchStopJobRunResponseTypeDef:
        """
        [Client.batch_stop_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.batch_stop_job_run)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.can_paginate)
        """

    def cancel_ml_task_run(
        self, TransformId: str, TaskRunId: str
    ) -> CancelMLTaskRunResponseTypeDef:
        """
        [Client.cancel_ml_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.cancel_ml_task_run)
        """

    def create_classifier(
        self,
        GrokClassifier: CreateGrokClassifierRequestTypeDef = None,
        XMLClassifier: CreateXMLClassifierRequestTypeDef = None,
        JsonClassifier: CreateJsonClassifierRequestTypeDef = None,
        CsvClassifier: CreateCsvClassifierRequestTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.create_classifier)
        """

    def create_connection(
        self, ConnectionInput: ConnectionInputTypeDef, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.create_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.create_connection)
        """

    def create_crawler(
        self,
        Name: str,
        Role: str,
        Targets: "CrawlerTargetsTypeDef",
        DatabaseName: str = None,
        Description: str = None,
        Schedule: str = None,
        Classifiers: List[str] = None,
        TablePrefix: str = None,
        SchemaChangePolicy: "SchemaChangePolicyTypeDef" = None,
        Configuration: str = None,
        CrawlerSecurityConfiguration: str = None,
        Tags: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.create_crawler)
        """

    def create_database(
        self, DatabaseInput: DatabaseInputTypeDef, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.create_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.create_database)
        """

    def create_dev_endpoint(
        self,
        EndpointName: str,
        RoleArn: str,
        SecurityGroupIds: List[str] = None,
        SubnetId: str = None,
        PublicKey: str = None,
        PublicKeys: List[str] = None,
        NumberOfNodes: int = None,
        WorkerType: Literal["Standard", "G.1X", "G.2X"] = None,
        GlueVersion: str = None,
        NumberOfWorkers: int = None,
        ExtraPythonLibsS3Path: str = None,
        ExtraJarsS3Path: str = None,
        SecurityConfiguration: str = None,
        Tags: Dict[str, str] = None,
        Arguments: Dict[str, str] = None,
    ) -> CreateDevEndpointResponseTypeDef:
        """
        [Client.create_dev_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.create_dev_endpoint)
        """

    def create_job(
        self,
        Name: str,
        Role: str,
        Command: "JobCommandTypeDef",
        Description: str = None,
        LogUri: str = None,
        ExecutionProperty: "ExecutionPropertyTypeDef" = None,
        DefaultArguments: Dict[str, str] = None,
        NonOverridableArguments: Dict[str, str] = None,
        Connections: "ConnectionsListTypeDef" = None,
        MaxRetries: int = None,
        AllocatedCapacity: int = None,
        Timeout: int = None,
        MaxCapacity: float = None,
        SecurityConfiguration: str = None,
        Tags: Dict[str, str] = None,
        NotificationProperty: "NotificationPropertyTypeDef" = None,
        GlueVersion: str = None,
        NumberOfWorkers: int = None,
        WorkerType: Literal["Standard", "G.1X", "G.2X"] = None,
    ) -> CreateJobResponseTypeDef:
        """
        [Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.create_job)
        """

    def create_ml_transform(
        self,
        Name: str,
        InputRecordTables: List["GlueTableTypeDef"],
        Parameters: "TransformParametersTypeDef",
        Role: str,
        Description: str = None,
        GlueVersion: str = None,
        MaxCapacity: float = None,
        WorkerType: Literal["Standard", "G.1X", "G.2X"] = None,
        NumberOfWorkers: int = None,
        Timeout: int = None,
        MaxRetries: int = None,
        Tags: Dict[str, str] = None,
    ) -> CreateMLTransformResponseTypeDef:
        """
        [Client.create_ml_transform documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.create_ml_transform)
        """

    def create_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionInput: PartitionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.create_partition)
        """

    def create_script(
        self,
        DagNodes: List["CodeGenNodeTypeDef"] = None,
        DagEdges: List["CodeGenEdgeTypeDef"] = None,
        Language: Literal["PYTHON", "SCALA"] = None,
    ) -> CreateScriptResponseTypeDef:
        """
        [Client.create_script documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.create_script)
        """

    def create_security_configuration(
        self, Name: str, EncryptionConfiguration: "EncryptionConfigurationTypeDef"
    ) -> CreateSecurityConfigurationResponseTypeDef:
        """
        [Client.create_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.create_security_configuration)
        """

    def create_table(
        self, DatabaseName: str, TableInput: TableInputTypeDef, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.create_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.create_table)
        """

    def create_trigger(
        self,
        Name: str,
        Type: Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        Actions: List["ActionTypeDef"],
        WorkflowName: str = None,
        Schedule: str = None,
        Predicate: "PredicateTypeDef" = None,
        Description: str = None,
        StartOnCreation: bool = None,
        Tags: Dict[str, str] = None,
    ) -> CreateTriggerResponseTypeDef:
        """
        [Client.create_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.create_trigger)
        """

    def create_user_defined_function(
        self,
        DatabaseName: str,
        FunctionInput: UserDefinedFunctionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_user_defined_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.create_user_defined_function)
        """

    def create_workflow(
        self,
        Name: str,
        Description: str = None,
        DefaultRunProperties: Dict[str, str] = None,
        Tags: Dict[str, str] = None,
        MaxConcurrentRuns: int = None,
    ) -> CreateWorkflowResponseTypeDef:
        """
        [Client.create_workflow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.create_workflow)
        """

    def delete_classifier(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.delete_classifier)
        """

    def delete_column_statistics_for_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionValues: List[str],
        ColumnName: str,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.delete_column_statistics_for_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.delete_column_statistics_for_partition)
        """

    def delete_column_statistics_for_table(
        self, DatabaseName: str, TableName: str, ColumnName: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_column_statistics_for_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.delete_column_statistics_for_table)
        """

    def delete_connection(self, ConnectionName: str, CatalogId: str = None) -> Dict[str, Any]:
        """
        [Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.delete_connection)
        """

    def delete_crawler(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.delete_crawler)
        """

    def delete_database(self, Name: str, CatalogId: str = None) -> Dict[str, Any]:
        """
        [Client.delete_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.delete_database)
        """

    def delete_dev_endpoint(self, EndpointName: str) -> Dict[str, Any]:
        """
        [Client.delete_dev_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.delete_dev_endpoint)
        """

    def delete_job(self, JobName: str) -> DeleteJobResponseTypeDef:
        """
        [Client.delete_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.delete_job)
        """

    def delete_ml_transform(self, TransformId: str) -> DeleteMLTransformResponseTypeDef:
        """
        [Client.delete_ml_transform documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.delete_ml_transform)
        """

    def delete_partition(
        self, DatabaseName: str, TableName: str, PartitionValues: List[str], CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.delete_partition)
        """

    def delete_resource_policy(
        self, PolicyHashCondition: str = None, ResourceArn: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.delete_resource_policy)
        """

    def delete_security_configuration(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.delete_security_configuration)
        """

    def delete_table(self, DatabaseName: str, Name: str, CatalogId: str = None) -> Dict[str, Any]:
        """
        [Client.delete_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.delete_table)
        """

    def delete_table_version(
        self, DatabaseName: str, TableName: str, VersionId: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_table_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.delete_table_version)
        """

    def delete_trigger(self, Name: str) -> DeleteTriggerResponseTypeDef:
        """
        [Client.delete_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.delete_trigger)
        """

    def delete_user_defined_function(
        self, DatabaseName: str, FunctionName: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_user_defined_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.delete_user_defined_function)
        """

    def delete_workflow(self, Name: str) -> DeleteWorkflowResponseTypeDef:
        """
        [Client.delete_workflow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.delete_workflow)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.generate_presigned_url)
        """

    def get_catalog_import_status(
        self, CatalogId: str = None
    ) -> GetCatalogImportStatusResponseTypeDef:
        """
        [Client.get_catalog_import_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_catalog_import_status)
        """

    def get_classifier(self, Name: str) -> GetClassifierResponseTypeDef:
        """
        [Client.get_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_classifier)
        """

    def get_classifiers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> GetClassifiersResponseTypeDef:
        """
        [Client.get_classifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_classifiers)
        """

    def get_column_statistics_for_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionValues: List[str],
        ColumnNames: List[str],
        CatalogId: str = None,
    ) -> GetColumnStatisticsForPartitionResponseTypeDef:
        """
        [Client.get_column_statistics_for_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_column_statistics_for_partition)
        """

    def get_column_statistics_for_table(
        self, DatabaseName: str, TableName: str, ColumnNames: List[str], CatalogId: str = None
    ) -> GetColumnStatisticsForTableResponseTypeDef:
        """
        [Client.get_column_statistics_for_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_column_statistics_for_table)
        """

    def get_connection(
        self, Name: str, CatalogId: str = None, HidePassword: bool = None
    ) -> GetConnectionResponseTypeDef:
        """
        [Client.get_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_connection)
        """

    def get_connections(
        self,
        CatalogId: str = None,
        Filter: GetConnectionsFilterTypeDef = None,
        HidePassword: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetConnectionsResponseTypeDef:
        """
        [Client.get_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_connections)
        """

    def get_crawler(self, Name: str) -> GetCrawlerResponseTypeDef:
        """
        [Client.get_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_crawler)
        """

    def get_crawler_metrics(
        self, CrawlerNameList: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> GetCrawlerMetricsResponseTypeDef:
        """
        [Client.get_crawler_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_crawler_metrics)
        """

    def get_crawlers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> GetCrawlersResponseTypeDef:
        """
        [Client.get_crawlers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_crawlers)
        """

    def get_data_catalog_encryption_settings(
        self, CatalogId: str = None
    ) -> GetDataCatalogEncryptionSettingsResponseTypeDef:
        """
        [Client.get_data_catalog_encryption_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_data_catalog_encryption_settings)
        """

    def get_database(self, Name: str, CatalogId: str = None) -> GetDatabaseResponseTypeDef:
        """
        [Client.get_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_database)
        """

    def get_databases(
        self,
        CatalogId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        ResourceShareType: Literal["FOREIGN", "ALL"] = None,
    ) -> GetDatabasesResponseTypeDef:
        """
        [Client.get_databases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_databases)
        """

    def get_dataflow_graph(self, PythonScript: str = None) -> GetDataflowGraphResponseTypeDef:
        """
        [Client.get_dataflow_graph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_dataflow_graph)
        """

    def get_dev_endpoint(self, EndpointName: str) -> GetDevEndpointResponseTypeDef:
        """
        [Client.get_dev_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_dev_endpoint)
        """

    def get_dev_endpoints(
        self, MaxResults: int = None, NextToken: str = None
    ) -> GetDevEndpointsResponseTypeDef:
        """
        [Client.get_dev_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_dev_endpoints)
        """

    def get_job(self, JobName: str) -> GetJobResponseTypeDef:
        """
        [Client.get_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_job)
        """

    def get_job_bookmark(self, JobName: str, RunId: str = None) -> GetJobBookmarkResponseTypeDef:
        """
        [Client.get_job_bookmark documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_job_bookmark)
        """

    def get_job_run(
        self, JobName: str, RunId: str, PredecessorsIncluded: bool = None
    ) -> GetJobRunResponseTypeDef:
        """
        [Client.get_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_job_run)
        """

    def get_job_runs(
        self, JobName: str, NextToken: str = None, MaxResults: int = None
    ) -> GetJobRunsResponseTypeDef:
        """
        [Client.get_job_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_job_runs)
        """

    def get_jobs(self, NextToken: str = None, MaxResults: int = None) -> GetJobsResponseTypeDef:
        """
        [Client.get_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_jobs)
        """

    def get_mapping(
        self,
        Source: CatalogEntryTypeDef,
        Sinks: List[CatalogEntryTypeDef] = None,
        Location: LocationTypeDef = None,
    ) -> GetMappingResponseTypeDef:
        """
        [Client.get_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_mapping)
        """

    def get_ml_task_run(self, TransformId: str, TaskRunId: str) -> GetMLTaskRunResponseTypeDef:
        """
        [Client.get_ml_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_ml_task_run)
        """

    def get_ml_task_runs(
        self,
        TransformId: str,
        NextToken: str = None,
        MaxResults: int = None,
        Filter: TaskRunFilterCriteriaTypeDef = None,
        Sort: TaskRunSortCriteriaTypeDef = None,
    ) -> GetMLTaskRunsResponseTypeDef:
        """
        [Client.get_ml_task_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_ml_task_runs)
        """

    def get_ml_transform(self, TransformId: str) -> GetMLTransformResponseTypeDef:
        """
        [Client.get_ml_transform documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_ml_transform)
        """

    def get_ml_transforms(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Filter: TransformFilterCriteriaTypeDef = None,
        Sort: TransformSortCriteriaTypeDef = None,
    ) -> GetMLTransformsResponseTypeDef:
        """
        [Client.get_ml_transforms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_ml_transforms)
        """

    def get_partition(
        self, DatabaseName: str, TableName: str, PartitionValues: List[str], CatalogId: str = None
    ) -> GetPartitionResponseTypeDef:
        """
        [Client.get_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_partition)
        """

    def get_partitions(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        Expression: str = None,
        NextToken: str = None,
        Segment: SegmentTypeDef = None,
        MaxResults: int = None,
    ) -> GetPartitionsResponseTypeDef:
        """
        [Client.get_partitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_partitions)
        """

    def get_plan(
        self,
        Mapping: List["MappingEntryTypeDef"],
        Source: CatalogEntryTypeDef,
        Sinks: List[CatalogEntryTypeDef] = None,
        Location: LocationTypeDef = None,
        Language: Literal["PYTHON", "SCALA"] = None,
    ) -> GetPlanResponseTypeDef:
        """
        [Client.get_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_plan)
        """

    def get_resource_policies(
        self, NextToken: str = None, MaxResults: int = None
    ) -> GetResourcePoliciesResponseTypeDef:
        """
        [Client.get_resource_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_resource_policies)
        """

    def get_resource_policy(self, ResourceArn: str = None) -> GetResourcePolicyResponseTypeDef:
        """
        [Client.get_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_resource_policy)
        """

    def get_security_configuration(self, Name: str) -> GetSecurityConfigurationResponseTypeDef:
        """
        [Client.get_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_security_configuration)
        """

    def get_security_configurations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> GetSecurityConfigurationsResponseTypeDef:
        """
        [Client.get_security_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_security_configurations)
        """

    def get_table(
        self, DatabaseName: str, Name: str, CatalogId: str = None
    ) -> GetTableResponseTypeDef:
        """
        [Client.get_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_table)
        """

    def get_table_version(
        self, DatabaseName: str, TableName: str, CatalogId: str = None, VersionId: str = None
    ) -> GetTableVersionResponseTypeDef:
        """
        [Client.get_table_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_table_version)
        """

    def get_table_versions(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetTableVersionsResponseTypeDef:
        """
        [Client.get_table_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_table_versions)
        """

    def get_tables(
        self,
        DatabaseName: str,
        CatalogId: str = None,
        Expression: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetTablesResponseTypeDef:
        """
        [Client.get_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_tables)
        """

    def get_tags(self, ResourceArn: str) -> GetTagsResponseTypeDef:
        """
        [Client.get_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_tags)
        """

    def get_trigger(self, Name: str) -> GetTriggerResponseTypeDef:
        """
        [Client.get_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_trigger)
        """

    def get_triggers(
        self, NextToken: str = None, DependentJobName: str = None, MaxResults: int = None
    ) -> GetTriggersResponseTypeDef:
        """
        [Client.get_triggers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_triggers)
        """

    def get_user_defined_function(
        self, DatabaseName: str, FunctionName: str, CatalogId: str = None
    ) -> GetUserDefinedFunctionResponseTypeDef:
        """
        [Client.get_user_defined_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_user_defined_function)
        """

    def get_user_defined_functions(
        self,
        Pattern: str,
        CatalogId: str = None,
        DatabaseName: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetUserDefinedFunctionsResponseTypeDef:
        """
        [Client.get_user_defined_functions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_user_defined_functions)
        """

    def get_workflow(self, Name: str, IncludeGraph: bool = None) -> GetWorkflowResponseTypeDef:
        """
        [Client.get_workflow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_workflow)
        """

    def get_workflow_run(
        self, Name: str, RunId: str, IncludeGraph: bool = None
    ) -> GetWorkflowRunResponseTypeDef:
        """
        [Client.get_workflow_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_workflow_run)
        """

    def get_workflow_run_properties(
        self, Name: str, RunId: str
    ) -> GetWorkflowRunPropertiesResponseTypeDef:
        """
        [Client.get_workflow_run_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_workflow_run_properties)
        """

    def get_workflow_runs(
        self, Name: str, IncludeGraph: bool = None, NextToken: str = None, MaxResults: int = None
    ) -> GetWorkflowRunsResponseTypeDef:
        """
        [Client.get_workflow_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.get_workflow_runs)
        """

    def import_catalog_to_glue(self, CatalogId: str = None) -> Dict[str, Any]:
        """
        [Client.import_catalog_to_glue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.import_catalog_to_glue)
        """

    def list_crawlers(
        self, MaxResults: int = None, NextToken: str = None, Tags: Dict[str, str] = None
    ) -> ListCrawlersResponseTypeDef:
        """
        [Client.list_crawlers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.list_crawlers)
        """

    def list_dev_endpoints(
        self, NextToken: str = None, MaxResults: int = None, Tags: Dict[str, str] = None
    ) -> ListDevEndpointsResponseTypeDef:
        """
        [Client.list_dev_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.list_dev_endpoints)
        """

    def list_jobs(
        self, NextToken: str = None, MaxResults: int = None, Tags: Dict[str, str] = None
    ) -> ListJobsResponseTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.list_jobs)
        """

    def list_ml_transforms(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Filter: TransformFilterCriteriaTypeDef = None,
        Sort: TransformSortCriteriaTypeDef = None,
        Tags: Dict[str, str] = None,
    ) -> ListMLTransformsResponseTypeDef:
        """
        [Client.list_ml_transforms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.list_ml_transforms)
        """

    def list_triggers(
        self,
        NextToken: str = None,
        DependentJobName: str = None,
        MaxResults: int = None,
        Tags: Dict[str, str] = None,
    ) -> ListTriggersResponseTypeDef:
        """
        [Client.list_triggers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.list_triggers)
        """

    def list_workflows(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListWorkflowsResponseTypeDef:
        """
        [Client.list_workflows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.list_workflows)
        """

    def put_data_catalog_encryption_settings(
        self,
        DataCatalogEncryptionSettings: "DataCatalogEncryptionSettingsTypeDef",
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_data_catalog_encryption_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.put_data_catalog_encryption_settings)
        """

    def put_resource_policy(
        self,
        PolicyInJson: str,
        ResourceArn: str = None,
        PolicyHashCondition: str = None,
        PolicyExistsCondition: Literal["MUST_EXIST", "NOT_EXIST", "NONE"] = None,
        EnableHybrid: Literal["TRUE", "FALSE"] = None,
    ) -> PutResourcePolicyResponseTypeDef:
        """
        [Client.put_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.put_resource_policy)
        """

    def put_workflow_run_properties(
        self, Name: str, RunId: str, RunProperties: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        [Client.put_workflow_run_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.put_workflow_run_properties)
        """

    def reset_job_bookmark(
        self, JobName: str, RunId: str = None
    ) -> ResetJobBookmarkResponseTypeDef:
        """
        [Client.reset_job_bookmark documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.reset_job_bookmark)
        """

    def resume_workflow_run(
        self, Name: str, RunId: str, NodeIds: List[str]
    ) -> ResumeWorkflowRunResponseTypeDef:
        """
        [Client.resume_workflow_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.resume_workflow_run)
        """

    def search_tables(
        self,
        CatalogId: str = None,
        NextToken: str = None,
        Filters: List[PropertyPredicateTypeDef] = None,
        SearchText: str = None,
        SortCriteria: List[SortCriterionTypeDef] = None,
        MaxResults: int = None,
        ResourceShareType: Literal["FOREIGN", "ALL"] = None,
    ) -> SearchTablesResponseTypeDef:
        """
        [Client.search_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.search_tables)
        """

    def start_crawler(self, Name: str) -> Dict[str, Any]:
        """
        [Client.start_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.start_crawler)
        """

    def start_crawler_schedule(self, CrawlerName: str) -> Dict[str, Any]:
        """
        [Client.start_crawler_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.start_crawler_schedule)
        """

    def start_export_labels_task_run(
        self, TransformId: str, OutputS3Path: str
    ) -> StartExportLabelsTaskRunResponseTypeDef:
        """
        [Client.start_export_labels_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.start_export_labels_task_run)
        """

    def start_import_labels_task_run(
        self, TransformId: str, InputS3Path: str, ReplaceAllLabels: bool = None
    ) -> StartImportLabelsTaskRunResponseTypeDef:
        """
        [Client.start_import_labels_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.start_import_labels_task_run)
        """

    def start_job_run(
        self,
        JobName: str,
        JobRunId: str = None,
        Arguments: Dict[str, str] = None,
        AllocatedCapacity: int = None,
        Timeout: int = None,
        MaxCapacity: float = None,
        SecurityConfiguration: str = None,
        NotificationProperty: "NotificationPropertyTypeDef" = None,
        WorkerType: Literal["Standard", "G.1X", "G.2X"] = None,
        NumberOfWorkers: int = None,
    ) -> StartJobRunResponseTypeDef:
        """
        [Client.start_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.start_job_run)
        """

    def start_ml_evaluation_task_run(
        self, TransformId: str
    ) -> StartMLEvaluationTaskRunResponseTypeDef:
        """
        [Client.start_ml_evaluation_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.start_ml_evaluation_task_run)
        """

    def start_ml_labeling_set_generation_task_run(
        self, TransformId: str, OutputS3Path: str
    ) -> StartMLLabelingSetGenerationTaskRunResponseTypeDef:
        """
        [Client.start_ml_labeling_set_generation_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.start_ml_labeling_set_generation_task_run)
        """

    def start_trigger(self, Name: str) -> StartTriggerResponseTypeDef:
        """
        [Client.start_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.start_trigger)
        """

    def start_workflow_run(self, Name: str) -> StartWorkflowRunResponseTypeDef:
        """
        [Client.start_workflow_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.start_workflow_run)
        """

    def stop_crawler(self, Name: str) -> Dict[str, Any]:
        """
        [Client.stop_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.stop_crawler)
        """

    def stop_crawler_schedule(self, CrawlerName: str) -> Dict[str, Any]:
        """
        [Client.stop_crawler_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.stop_crawler_schedule)
        """

    def stop_trigger(self, Name: str) -> StopTriggerResponseTypeDef:
        """
        [Client.stop_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.stop_trigger)
        """

    def stop_workflow_run(self, Name: str, RunId: str) -> Dict[str, Any]:
        """
        [Client.stop_workflow_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.stop_workflow_run)
        """

    def tag_resource(self, ResourceArn: str, TagsToAdd: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagsToRemove: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.untag_resource)
        """

    def update_classifier(
        self,
        GrokClassifier: UpdateGrokClassifierRequestTypeDef = None,
        XMLClassifier: UpdateXMLClassifierRequestTypeDef = None,
        JsonClassifier: UpdateJsonClassifierRequestTypeDef = None,
        CsvClassifier: UpdateCsvClassifierRequestTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.update_classifier)
        """

    def update_column_statistics_for_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionValues: List[str],
        ColumnStatisticsList: List["ColumnStatisticsTypeDef"],
        CatalogId: str = None,
    ) -> UpdateColumnStatisticsForPartitionResponseTypeDef:
        """
        [Client.update_column_statistics_for_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.update_column_statistics_for_partition)
        """

    def update_column_statistics_for_table(
        self,
        DatabaseName: str,
        TableName: str,
        ColumnStatisticsList: List["ColumnStatisticsTypeDef"],
        CatalogId: str = None,
    ) -> UpdateColumnStatisticsForTableResponseTypeDef:
        """
        [Client.update_column_statistics_for_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.update_column_statistics_for_table)
        """

    def update_connection(
        self, Name: str, ConnectionInput: ConnectionInputTypeDef, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.update_connection)
        """

    def update_crawler(
        self,
        Name: str,
        Role: str = None,
        DatabaseName: str = None,
        Description: str = None,
        Targets: "CrawlerTargetsTypeDef" = None,
        Schedule: str = None,
        Classifiers: List[str] = None,
        TablePrefix: str = None,
        SchemaChangePolicy: "SchemaChangePolicyTypeDef" = None,
        Configuration: str = None,
        CrawlerSecurityConfiguration: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.update_crawler)
        """

    def update_crawler_schedule(self, CrawlerName: str, Schedule: str = None) -> Dict[str, Any]:
        """
        [Client.update_crawler_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.update_crawler_schedule)
        """

    def update_database(
        self, Name: str, DatabaseInput: DatabaseInputTypeDef, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.update_database)
        """

    def update_dev_endpoint(
        self,
        EndpointName: str,
        PublicKey: str = None,
        AddPublicKeys: List[str] = None,
        DeletePublicKeys: List[str] = None,
        CustomLibraries: DevEndpointCustomLibrariesTypeDef = None,
        UpdateEtlLibraries: bool = None,
        DeleteArguments: List[str] = None,
        AddArguments: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_dev_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.update_dev_endpoint)
        """

    def update_job(self, JobName: str, JobUpdate: JobUpdateTypeDef) -> UpdateJobResponseTypeDef:
        """
        [Client.update_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.update_job)
        """

    def update_ml_transform(
        self,
        TransformId: str,
        Name: str = None,
        Description: str = None,
        Parameters: "TransformParametersTypeDef" = None,
        Role: str = None,
        GlueVersion: str = None,
        MaxCapacity: float = None,
        WorkerType: Literal["Standard", "G.1X", "G.2X"] = None,
        NumberOfWorkers: int = None,
        Timeout: int = None,
        MaxRetries: int = None,
    ) -> UpdateMLTransformResponseTypeDef:
        """
        [Client.update_ml_transform documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.update_ml_transform)
        """

    def update_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionValueList: List[str],
        PartitionInput: PartitionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.update_partition)
        """

    def update_table(
        self,
        DatabaseName: str,
        TableInput: TableInputTypeDef,
        CatalogId: str = None,
        SkipArchive: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.update_table)
        """

    def update_trigger(
        self, Name: str, TriggerUpdate: TriggerUpdateTypeDef
    ) -> UpdateTriggerResponseTypeDef:
        """
        [Client.update_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.update_trigger)
        """

    def update_user_defined_function(
        self,
        DatabaseName: str,
        FunctionName: str,
        FunctionInput: UserDefinedFunctionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_user_defined_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.update_user_defined_function)
        """

    def update_workflow(
        self,
        Name: str,
        Description: str = None,
        DefaultRunProperties: Dict[str, str] = None,
        MaxConcurrentRuns: int = None,
    ) -> UpdateWorkflowResponseTypeDef:
        """
        [Client.update_workflow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Client.update_workflow)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_classifiers"]) -> GetClassifiersPaginator:
        """
        [Paginator.GetClassifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Paginator.GetClassifiers)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_connections"]) -> GetConnectionsPaginator:
        """
        [Paginator.GetConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Paginator.GetConnections)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_crawler_metrics"]
    ) -> GetCrawlerMetricsPaginator:
        """
        [Paginator.GetCrawlerMetrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Paginator.GetCrawlerMetrics)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_crawlers"]) -> GetCrawlersPaginator:
        """
        [Paginator.GetCrawlers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Paginator.GetCrawlers)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_databases"]) -> GetDatabasesPaginator:
        """
        [Paginator.GetDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Paginator.GetDatabases)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_dev_endpoints"]
    ) -> GetDevEndpointsPaginator:
        """
        [Paginator.GetDevEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Paginator.GetDevEndpoints)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_job_runs"]) -> GetJobRunsPaginator:
        """
        [Paginator.GetJobRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Paginator.GetJobRuns)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_jobs"]) -> GetJobsPaginator:
        """
        [Paginator.GetJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Paginator.GetJobs)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_partitions"]) -> GetPartitionsPaginator:
        """
        [Paginator.GetPartitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Paginator.GetPartitions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_security_configurations"]
    ) -> GetSecurityConfigurationsPaginator:
        """
        [Paginator.GetSecurityConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Paginator.GetSecurityConfigurations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_table_versions"]
    ) -> GetTableVersionsPaginator:
        """
        [Paginator.GetTableVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Paginator.GetTableVersions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_tables"]) -> GetTablesPaginator:
        """
        [Paginator.GetTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Paginator.GetTables)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_triggers"]) -> GetTriggersPaginator:
        """
        [Paginator.GetTriggers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Paginator.GetTriggers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_user_defined_functions"]
    ) -> GetUserDefinedFunctionsPaginator:
        """
        [Paginator.GetUserDefinedFunctions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glue.html#Glue.Paginator.GetUserDefinedFunctions)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
