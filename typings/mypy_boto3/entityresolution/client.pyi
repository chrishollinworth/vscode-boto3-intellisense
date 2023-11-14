"""
Type annotations for entityresolution service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_entityresolution import EntityResolutionClient

    client: EntityResolutionClient = boto3.client("entityresolution")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListIdMappingJobsPaginator,
    ListIdMappingWorkflowsPaginator,
    ListMatchingJobsPaginator,
    ListMatchingWorkflowsPaginator,
    ListProviderServicesPaginator,
    ListSchemaMappingsPaginator,
)
from .type_defs import (
    CreateIdMappingWorkflowOutputTypeDef,
    CreateMatchingWorkflowOutputTypeDef,
    CreateSchemaMappingOutputTypeDef,
    DeleteIdMappingWorkflowOutputTypeDef,
    DeleteMatchingWorkflowOutputTypeDef,
    DeleteSchemaMappingOutputTypeDef,
    GetIdMappingJobOutputTypeDef,
    GetIdMappingWorkflowOutputTypeDef,
    GetMatchIdOutputTypeDef,
    GetMatchingJobOutputTypeDef,
    GetMatchingWorkflowOutputTypeDef,
    GetProviderServiceOutputTypeDef,
    GetSchemaMappingOutputTypeDef,
    IdMappingTechniquesTypeDef,
    IdMappingWorkflowInputSourceTypeDef,
    IdMappingWorkflowOutputSourceTypeDef,
    IncrementalRunConfigTypeDef,
    InputSourceTypeDef,
    ListIdMappingJobsOutputTypeDef,
    ListIdMappingWorkflowsOutputTypeDef,
    ListMatchingJobsOutputTypeDef,
    ListMatchingWorkflowsOutputTypeDef,
    ListProviderServicesOutputTypeDef,
    ListSchemaMappingsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    OutputSourceTypeDef,
    ResolutionTechniquesTypeDef,
    SchemaInputAttributeTypeDef,
    StartIdMappingJobOutputTypeDef,
    StartMatchingJobOutputTypeDef,
    UpdateIdMappingWorkflowOutputTypeDef,
    UpdateMatchingWorkflowOutputTypeDef,
    UpdateSchemaMappingOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("EntityResolutionClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ExceedsLimitException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class EntityResolutionClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EntityResolutionClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#close)
        """
    def create_id_mapping_workflow(
        self,
        *,
        idMappingTechniques: "IdMappingTechniquesTypeDef",
        inputSourceConfig: List["IdMappingWorkflowInputSourceTypeDef"],
        outputSourceConfig: List["IdMappingWorkflowOutputSourceTypeDef"],
        roleArn: str,
        workflowName: str,
        description: str = None,
        tags: Dict[str, str] = None
    ) -> CreateIdMappingWorkflowOutputTypeDef:
        """
        Creates an `IdMappingWorkflow` object which stores the configuration of the data
        processing job to be run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.create_id_mapping_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#create_id_mapping_workflow)
        """
    def create_matching_workflow(
        self,
        *,
        inputSourceConfig: List["InputSourceTypeDef"],
        outputSourceConfig: List["OutputSourceTypeDef"],
        resolutionTechniques: "ResolutionTechniquesTypeDef",
        roleArn: str,
        workflowName: str,
        description: str = None,
        incrementalRunConfig: "IncrementalRunConfigTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateMatchingWorkflowOutputTypeDef:
        """
        Creates a `MatchingWorkflow` object which stores the configuration of the data
        processing job to be run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.create_matching_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#create_matching_workflow)
        """
    def create_schema_mapping(
        self,
        *,
        mappedInputFields: List["SchemaInputAttributeTypeDef"],
        schemaName: str,
        description: str = None,
        tags: Dict[str, str] = None
    ) -> CreateSchemaMappingOutputTypeDef:
        """
        Creates a schema mapping, which defines the schema of the input customer records
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.create_schema_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#create_schema_mapping)
        """
    def delete_id_mapping_workflow(
        self, *, workflowName: str
    ) -> DeleteIdMappingWorkflowOutputTypeDef:
        """
        Deletes the `IdMappingWorkflow` with a given name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.delete_id_mapping_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#delete_id_mapping_workflow)
        """
    def delete_matching_workflow(self, *, workflowName: str) -> DeleteMatchingWorkflowOutputTypeDef:
        """
        Deletes the `MatchingWorkflow` with a given name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.delete_matching_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#delete_matching_workflow)
        """
    def delete_schema_mapping(self, *, schemaName: str) -> DeleteSchemaMappingOutputTypeDef:
        """
        Deletes the `SchemaMapping` with a given name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.delete_schema_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#delete_schema_mapping)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#generate_presigned_url)
        """
    def get_id_mapping_job(self, *, jobId: str, workflowName: str) -> GetIdMappingJobOutputTypeDef:
        """
        Gets the status, metrics, and errors (if there are any) that are associated with
        a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.get_id_mapping_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#get_id_mapping_job)
        """
    def get_id_mapping_workflow(self, *, workflowName: str) -> GetIdMappingWorkflowOutputTypeDef:
        """
        Returns the `IdMappingWorkflow` with a given name, if it exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.get_id_mapping_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#get_id_mapping_workflow)
        """
    def get_match_id(self, *, record: Dict[str, str], workflowName: str) -> GetMatchIdOutputTypeDef:
        """
        Returns the corresponding Match ID of a customer record if the record has been
        processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.get_match_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#get_match_id)
        """
    def get_matching_job(self, *, jobId: str, workflowName: str) -> GetMatchingJobOutputTypeDef:
        """
        Gets the status, metrics, and errors (if there are any) that are associated with
        a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.get_matching_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#get_matching_job)
        """
    def get_matching_workflow(self, *, workflowName: str) -> GetMatchingWorkflowOutputTypeDef:
        """
        Returns the `MatchingWorkflow` with a given name, if it exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.get_matching_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#get_matching_workflow)
        """
    def get_provider_service(
        self, *, providerName: str, providerServiceName: str
    ) -> GetProviderServiceOutputTypeDef:
        """
        Returns the `ProviderService` of a given name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.get_provider_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#get_provider_service)
        """
    def get_schema_mapping(self, *, schemaName: str) -> GetSchemaMappingOutputTypeDef:
        """
        Returns the SchemaMapping of a given name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.get_schema_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#get_schema_mapping)
        """
    def list_id_mapping_jobs(
        self, *, workflowName: str, maxResults: int = None, nextToken: str = None
    ) -> ListIdMappingJobsOutputTypeDef:
        """
        Lists all ID mapping jobs for a given workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.list_id_mapping_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#list_id_mapping_jobs)
        """
    def list_id_mapping_workflows(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListIdMappingWorkflowsOutputTypeDef:
        """
        Returns a list of all the `IdMappingWorkflows` that have been created for an
        Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.list_id_mapping_workflows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#list_id_mapping_workflows)
        """
    def list_matching_jobs(
        self, *, workflowName: str, maxResults: int = None, nextToken: str = None
    ) -> ListMatchingJobsOutputTypeDef:
        """
        Lists all jobs for a given workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.list_matching_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#list_matching_jobs)
        """
    def list_matching_workflows(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListMatchingWorkflowsOutputTypeDef:
        """
        Returns a list of all the `MatchingWorkflows` that have been created for an
        Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.list_matching_workflows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#list_matching_workflows)
        """
    def list_provider_services(
        self, *, maxResults: int = None, nextToken: str = None, providerName: str = None
    ) -> ListProviderServicesOutputTypeDef:
        """
        Returns a list of all the `ProviderServices` that are available in this Amazon
        Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.list_provider_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#list_provider_services)
        """
    def list_schema_mappings(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListSchemaMappingsOutputTypeDef:
        """
        Returns a list of all the `SchemaMappings` that have been created for an Amazon
        Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.list_schema_mappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#list_schema_mappings)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Displays the tags associated with an Entity Resolution resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#list_tags_for_resource)
        """
    def start_id_mapping_job(self, *, workflowName: str) -> StartIdMappingJobOutputTypeDef:
        """
        Starts the `IdMappingJob` of a workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.start_id_mapping_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#start_id_mapping_job)
        """
    def start_matching_job(self, *, workflowName: str) -> StartMatchingJobOutputTypeDef:
        """
        Starts the `MatchingJob` of a workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.start_matching_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#start_matching_job)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified Entity Resolution
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified Entity Resolution resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#untag_resource)
        """
    def update_id_mapping_workflow(
        self,
        *,
        idMappingTechniques: "IdMappingTechniquesTypeDef",
        inputSourceConfig: List["IdMappingWorkflowInputSourceTypeDef"],
        outputSourceConfig: List["IdMappingWorkflowOutputSourceTypeDef"],
        roleArn: str,
        workflowName: str,
        description: str = None
    ) -> UpdateIdMappingWorkflowOutputTypeDef:
        """
        Updates an existing `IdMappingWorkflow`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.update_id_mapping_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#update_id_mapping_workflow)
        """
    def update_matching_workflow(
        self,
        *,
        inputSourceConfig: List["InputSourceTypeDef"],
        outputSourceConfig: List["OutputSourceTypeDef"],
        resolutionTechniques: "ResolutionTechniquesTypeDef",
        roleArn: str,
        workflowName: str,
        description: str = None,
        incrementalRunConfig: "IncrementalRunConfigTypeDef" = None
    ) -> UpdateMatchingWorkflowOutputTypeDef:
        """
        Updates an existing `MatchingWorkflow`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.update_matching_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#update_matching_workflow)
        """
    def update_schema_mapping(
        self,
        *,
        mappedInputFields: List["SchemaInputAttributeTypeDef"],
        schemaName: str,
        description: str = None
    ) -> UpdateSchemaMappingOutputTypeDef:
        """
        Updates a schema mapping.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Client.update_schema_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/client.html#update_schema_mapping)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_id_mapping_jobs"]
    ) -> ListIdMappingJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Paginator.ListIdMappingJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listidmappingjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_id_mapping_workflows"]
    ) -> ListIdMappingWorkflowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Paginator.ListIdMappingWorkflows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listidmappingworkflowspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_matching_jobs"]
    ) -> ListMatchingJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Paginator.ListMatchingJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listmatchingjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_matching_workflows"]
    ) -> ListMatchingWorkflowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Paginator.ListMatchingWorkflows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listmatchingworkflowspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_provider_services"]
    ) -> ListProviderServicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Paginator.ListProviderServices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listproviderservicespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_schema_mappings"]
    ) -> ListSchemaMappingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/entityresolution.html#EntityResolution.Paginator.ListSchemaMappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listschemamappingspaginator)
        """
