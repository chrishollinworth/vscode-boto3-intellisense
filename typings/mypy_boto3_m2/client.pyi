"""
Type annotations for m2 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_m2 import MainframeModernizationClient

    client: MainframeModernizationClient = boto3.client("m2")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import BatchJobExecutionStatusType, EngineTypeType
from .paginator import (
    ListApplicationsPaginator,
    ListApplicationVersionsPaginator,
    ListBatchJobDefinitionsPaginator,
    ListBatchJobExecutionsPaginator,
    ListDataSetImportHistoryPaginator,
    ListDataSetsPaginator,
    ListDeploymentsPaginator,
    ListEngineVersionsPaginator,
    ListEnvironmentsPaginator,
)
from .type_defs import (
    BatchJobIdentifierTypeDef,
    CreateApplicationResponseTypeDef,
    CreateDataSetImportTaskResponseTypeDef,
    CreateDeploymentResponseTypeDef,
    CreateEnvironmentResponseTypeDef,
    DataSetImportConfigTypeDef,
    DefinitionTypeDef,
    GetApplicationResponseTypeDef,
    GetApplicationVersionResponseTypeDef,
    GetBatchJobExecutionResponseTypeDef,
    GetDataSetDetailsResponseTypeDef,
    GetDataSetImportTaskResponseTypeDef,
    GetDeploymentResponseTypeDef,
    GetEnvironmentResponseTypeDef,
    HighAvailabilityConfigTypeDef,
    ListApplicationsResponseTypeDef,
    ListApplicationVersionsResponseTypeDef,
    ListBatchJobDefinitionsResponseTypeDef,
    ListBatchJobExecutionsResponseTypeDef,
    ListDataSetImportHistoryResponseTypeDef,
    ListDataSetsResponseTypeDef,
    ListDeploymentsResponseTypeDef,
    ListEngineVersionsResponseTypeDef,
    ListEnvironmentsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartBatchJobResponseTypeDef,
    StorageConfigurationTypeDef,
    UpdateApplicationResponseTypeDef,
    UpdateEnvironmentResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("MainframeModernizationClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class MainframeModernizationClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MainframeModernizationClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#can_paginate)
        """
    def cancel_batch_job_execution(self, *, applicationId: str, executionId: str) -> Dict[str, Any]:
        """
        Cancels the running of a specific batch job execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.cancel_batch_job_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#cancel_batch_job_execution)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#close)
        """
    def create_application(
        self,
        *,
        definition: "DefinitionTypeDef",
        engineType: EngineTypeType,
        name: str,
        clientToken: str = None,
        description: str = None,
        kmsKeyId: str = None,
        tags: Dict[str, str] = None
    ) -> CreateApplicationResponseTypeDef:
        """
        Creates a new application with given parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.create_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#create_application)
        """
    def create_data_set_import_task(
        self,
        *,
        applicationId: str,
        importConfig: "DataSetImportConfigTypeDef",
        clientToken: str = None
    ) -> CreateDataSetImportTaskResponseTypeDef:
        """
        Starts a data set import task for a specific application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.create_data_set_import_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#create_data_set_import_task)
        """
    def create_deployment(
        self,
        *,
        applicationId: str,
        applicationVersion: int,
        environmentId: str,
        clientToken: str = None
    ) -> CreateDeploymentResponseTypeDef:
        """
        Creates and starts a deployment to deploy an application into a runtime
        environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.create_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#create_deployment)
        """
    def create_environment(
        self,
        *,
        engineType: EngineTypeType,
        instanceType: str,
        name: str,
        clientToken: str = None,
        description: str = None,
        engineVersion: str = None,
        highAvailabilityConfig: "HighAvailabilityConfigTypeDef" = None,
        kmsKeyId: str = None,
        preferredMaintenanceWindow: str = None,
        publiclyAccessible: bool = None,
        securityGroupIds: List[str] = None,
        storageConfigurations: List["StorageConfigurationTypeDef"] = None,
        subnetIds: List[str] = None,
        tags: Dict[str, str] = None
    ) -> CreateEnvironmentResponseTypeDef:
        """
        Creates a runtime environment for a given runtime engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.create_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#create_environment)
        """
    def delete_application(self, *, applicationId: str) -> Dict[str, Any]:
        """
        Deletes a specific application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.delete_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#delete_application)
        """
    def delete_application_from_environment(
        self, *, applicationId: str, environmentId: str
    ) -> Dict[str, Any]:
        """
        Deletes a specific application from the specific runtime environment where it
        was previously deployed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.delete_application_from_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#delete_application_from_environment)
        """
    def delete_environment(self, *, environmentId: str) -> Dict[str, Any]:
        """
        Deletes a specific runtime environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.delete_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#delete_environment)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#generate_presigned_url)
        """
    def get_application(self, *, applicationId: str) -> GetApplicationResponseTypeDef:
        """
        Describes the details of a specific application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.get_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#get_application)
        """
    def get_application_version(
        self, *, applicationId: str, applicationVersion: int
    ) -> GetApplicationVersionResponseTypeDef:
        """
        Returns details about a specific version of a specific application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.get_application_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#get_application_version)
        """
    def get_batch_job_execution(
        self, *, applicationId: str, executionId: str
    ) -> GetBatchJobExecutionResponseTypeDef:
        """
        Gets the details of a specific batch job execution for a specific application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.get_batch_job_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#get_batch_job_execution)
        """
    def get_data_set_details(
        self, *, applicationId: str, dataSetName: str
    ) -> GetDataSetDetailsResponseTypeDef:
        """
        Gets the details of a specific data set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.get_data_set_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#get_data_set_details)
        """
    def get_data_set_import_task(
        self, *, applicationId: str, taskId: str
    ) -> GetDataSetImportTaskResponseTypeDef:
        """
        Gets the status of a data set import task initiated with the
        CreateDataSetImportTask operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.get_data_set_import_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#get_data_set_import_task)
        """
    def get_deployment(
        self, *, applicationId: str, deploymentId: str
    ) -> GetDeploymentResponseTypeDef:
        """
        Gets details of a specific deployment with a given deployment identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.get_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#get_deployment)
        """
    def get_environment(self, *, environmentId: str) -> GetEnvironmentResponseTypeDef:
        """
        Describes a specific runtime environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.get_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#get_environment)
        """
    def list_application_versions(
        self, *, applicationId: str, maxResults: int = None, nextToken: str = None
    ) -> ListApplicationVersionsResponseTypeDef:
        """
        Returns a list of the application versions for a specific application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.list_application_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#list_application_versions)
        """
    def list_applications(
        self,
        *,
        environmentId: str = None,
        maxResults: int = None,
        names: List[str] = None,
        nextToken: str = None
    ) -> ListApplicationsResponseTypeDef:
        """
        Lists the applications associated with a specific Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.list_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#list_applications)
        """
    def list_batch_job_definitions(
        self,
        *,
        applicationId: str,
        maxResults: int = None,
        nextToken: str = None,
        prefix: str = None
    ) -> ListBatchJobDefinitionsResponseTypeDef:
        """
        Lists all the available batch job definitions based on the batch job resources
        uploaded during the application creation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.list_batch_job_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#list_batch_job_definitions)
        """
    def list_batch_job_executions(
        self,
        *,
        applicationId: str,
        executionIds: List[str] = None,
        jobName: str = None,
        maxResults: int = None,
        nextToken: str = None,
        startedAfter: Union[datetime, str] = None,
        startedBefore: Union[datetime, str] = None,
        status: BatchJobExecutionStatusType = None
    ) -> ListBatchJobExecutionsResponseTypeDef:
        """
        Lists historical, current, and scheduled batch job executions for a specific
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.list_batch_job_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#list_batch_job_executions)
        """
    def list_data_set_import_history(
        self, *, applicationId: str, maxResults: int = None, nextToken: str = None
    ) -> ListDataSetImportHistoryResponseTypeDef:
        """
        Lists the data set imports for the specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.list_data_set_import_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#list_data_set_import_history)
        """
    def list_data_sets(
        self,
        *,
        applicationId: str,
        maxResults: int = None,
        nextToken: str = None,
        prefix: str = None
    ) -> ListDataSetsResponseTypeDef:
        """
        Lists the data sets imported for a specific application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.list_data_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#list_data_sets)
        """
    def list_deployments(
        self, *, applicationId: str, maxResults: int = None, nextToken: str = None
    ) -> ListDeploymentsResponseTypeDef:
        """
        Returns a list of all deployments of a specific application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.list_deployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#list_deployments)
        """
    def list_engine_versions(
        self, *, engineType: EngineTypeType = None, maxResults: int = None, nextToken: str = None
    ) -> ListEngineVersionsResponseTypeDef:
        """
        Lists the available engine versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.list_engine_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#list_engine_versions)
        """
    def list_environments(
        self,
        *,
        engineType: EngineTypeType = None,
        maxResults: int = None,
        names: List[str] = None,
        nextToken: str = None
    ) -> ListEnvironmentsResponseTypeDef:
        """
        Lists the runtime environments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.list_environments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#list_environments)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#list_tags_for_resource)
        """
    def start_application(self, *, applicationId: str) -> Dict[str, Any]:
        """
        Starts an application that is currently stopped.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.start_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#start_application)
        """
    def start_batch_job(
        self,
        *,
        applicationId: str,
        batchJobIdentifier: "BatchJobIdentifierTypeDef",
        jobParams: Dict[str, str] = None
    ) -> StartBatchJobResponseTypeDef:
        """
        Starts a batch job and returns the unique identifier of this execution of the
        batch job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.start_batch_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#start_batch_job)
        """
    def stop_application(self, *, applicationId: str, forceStop: bool = None) -> Dict[str, Any]:
        """
        Stops a running application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.stop_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#stop_application)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds one or more tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#untag_resource)
        """
    def update_application(
        self,
        *,
        applicationId: str,
        currentApplicationVersion: int,
        definition: "DefinitionTypeDef" = None,
        description: str = None
    ) -> UpdateApplicationResponseTypeDef:
        """
        Updates an application and creates a new version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.update_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#update_application)
        """
    def update_environment(
        self,
        *,
        environmentId: str,
        applyDuringMaintenanceWindow: bool = None,
        desiredCapacity: int = None,
        engineVersion: str = None,
        instanceType: str = None,
        preferredMaintenanceWindow: str = None
    ) -> UpdateEnvironmentResponseTypeDef:
        """
        Updates the configuration details for a specific runtime environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Client.update_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/client.html#update_environment)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_versions"]
    ) -> ListApplicationVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Paginator.ListApplicationVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listapplicationversionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Paginator.ListApplications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listapplicationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_batch_job_definitions"]
    ) -> ListBatchJobDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Paginator.ListBatchJobDefinitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listbatchjobdefinitionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_batch_job_executions"]
    ) -> ListBatchJobExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Paginator.ListBatchJobExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listbatchjobexecutionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_set_import_history"]
    ) -> ListDataSetImportHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Paginator.ListDataSetImportHistory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listdatasetimporthistorypaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_data_sets"]) -> ListDataSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Paginator.ListDataSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listdatasetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployments"]
    ) -> ListDeploymentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Paginator.ListDeployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listdeploymentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_engine_versions"]
    ) -> ListEngineVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Paginator.ListEngineVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listengineversionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_environments"]
    ) -> ListEnvironmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/m2.html#MainframeModernization.Paginator.ListEnvironments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listenvironmentspaginator)
        """
