"""
Type annotations for iottwinmaker service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iottwinmaker import IoTTwinMakerClient

    client: IoTTwinMakerClient = boto3.client("iottwinmaker")
    ```
"""

from datetime import datetime
from typing import Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta

from .literals import DestinationTypeType, OrderByTimeType, PricingModeType, SourceTypeType
from .type_defs import (
    BatchPutPropertyValuesResponseTypeDef,
    CancelMetadataTransferJobResponseTypeDef,
    ComponentRequestTypeDef,
    ComponentUpdateRequestTypeDef,
    CompositeComponentRequestTypeDef,
    CompositeComponentTypeRequestTypeDef,
    CompositeComponentUpdateRequestTypeDef,
    CreateComponentTypeResponseTypeDef,
    CreateEntityResponseTypeDef,
    CreateMetadataTransferJobResponseTypeDef,
    CreateSceneResponseTypeDef,
    CreateSyncJobResponseTypeDef,
    CreateWorkspaceResponseTypeDef,
    DeleteComponentTypeResponseTypeDef,
    DeleteEntityResponseTypeDef,
    DeleteSyncJobResponseTypeDef,
    DeleteWorkspaceResponseTypeDef,
    DestinationConfigurationTypeDef,
    ExecuteQueryResponseTypeDef,
    FunctionRequestTypeDef,
    GetComponentTypeResponseTypeDef,
    GetEntityResponseTypeDef,
    GetMetadataTransferJobResponseTypeDef,
    GetPricingPlanResponseTypeDef,
    GetPropertyValueHistoryResponseTypeDef,
    GetPropertyValueResponseTypeDef,
    GetSceneResponseTypeDef,
    GetSyncJobResponseTypeDef,
    GetWorkspaceResponseTypeDef,
    InterpolationParametersTypeDef,
    ListComponentsResponseTypeDef,
    ListComponentTypesFilterTypeDef,
    ListComponentTypesResponseTypeDef,
    ListEntitiesFilterTypeDef,
    ListEntitiesResponseTypeDef,
    ListMetadataTransferJobsFilterTypeDef,
    ListMetadataTransferJobsResponseTypeDef,
    ListPropertiesResponseTypeDef,
    ListScenesResponseTypeDef,
    ListSyncJobsResponseTypeDef,
    ListSyncResourcesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWorkspacesResponseTypeDef,
    ParentEntityUpdateRequestTypeDef,
    PropertyDefinitionRequestTypeDef,
    PropertyFilterTypeDef,
    PropertyGroupRequestTypeDef,
    PropertyValueEntryTypeDef,
    SourceConfigurationTypeDef,
    SyncResourceFilterTypeDef,
    TabularConditionsTypeDef,
    UpdateComponentTypeResponseTypeDef,
    UpdateEntityResponseTypeDef,
    UpdatePricingPlanResponseTypeDef,
    UpdateSceneResponseTypeDef,
    UpdateWorkspaceResponseTypeDef,
)

__all__ = ("IoTTwinMakerClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ConnectorFailureException: Type[BotocoreClientError]
    ConnectorTimeoutException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    QueryTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class IoTTwinMakerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IoTTwinMakerClient exceptions.
        """

    def batch_put_property_values(
        self, *, workspaceId: str, entries: List["PropertyValueEntryTypeDef"]
    ) -> BatchPutPropertyValuesResponseTypeDef:
        """
        Sets values for multiple time series properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.batch_put_property_values)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#batch_put_property_values)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#can_paginate)
        """

    def cancel_metadata_transfer_job(
        self, *, metadataTransferJobId: str
    ) -> CancelMetadataTransferJobResponseTypeDef:
        """
        Cancels the metadata transfer job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.cancel_metadata_transfer_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#cancel_metadata_transfer_job)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#close)
        """

    def create_component_type(
        self,
        *,
        workspaceId: str,
        componentTypeId: str,
        isSingleton: bool = None,
        description: str = None,
        propertyDefinitions: Dict[str, "PropertyDefinitionRequestTypeDef"] = None,
        extendsFrom: List[str] = None,
        functions: Dict[str, "FunctionRequestTypeDef"] = None,
        tags: Dict[str, str] = None,
        propertyGroups: Dict[str, "PropertyGroupRequestTypeDef"] = None,
        componentTypeName: str = None,
        compositeComponentTypes: Dict[str, "CompositeComponentTypeRequestTypeDef"] = None
    ) -> CreateComponentTypeResponseTypeDef:
        """
        Creates a component type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.create_component_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#create_component_type)
        """

    def create_entity(
        self,
        *,
        workspaceId: str,
        entityName: str,
        entityId: str = None,
        description: str = None,
        components: Dict[str, "ComponentRequestTypeDef"] = None,
        compositeComponents: Dict[str, "CompositeComponentRequestTypeDef"] = None,
        parentEntityId: str = None,
        tags: Dict[str, str] = None
    ) -> CreateEntityResponseTypeDef:
        """
        Creates an entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.create_entity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#create_entity)
        """

    def create_metadata_transfer_job(
        self,
        *,
        sources: List["SourceConfigurationTypeDef"],
        destination: "DestinationConfigurationTypeDef",
        metadataTransferJobId: str = None,
        description: str = None
    ) -> CreateMetadataTransferJobResponseTypeDef:
        """
        Creates a new metadata transfer job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.create_metadata_transfer_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#create_metadata_transfer_job)
        """

    def create_scene(
        self,
        *,
        workspaceId: str,
        sceneId: str,
        contentLocation: str,
        description: str = None,
        capabilities: List[str] = None,
        tags: Dict[str, str] = None,
        sceneMetadata: Dict[str, str] = None
    ) -> CreateSceneResponseTypeDef:
        """
        Creates a scene.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.create_scene)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#create_scene)
        """

    def create_sync_job(
        self, *, workspaceId: str, syncSource: str, syncRole: str, tags: Dict[str, str] = None
    ) -> CreateSyncJobResponseTypeDef:
        """
        This action creates a SyncJob.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.create_sync_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#create_sync_job)
        """

    def create_workspace(
        self,
        *,
        workspaceId: str,
        description: str = None,
        s3Location: str = None,
        role: str = None,
        tags: Dict[str, str] = None
    ) -> CreateWorkspaceResponseTypeDef:
        """
        Creates a workplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.create_workspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#create_workspace)
        """

    def delete_component_type(
        self, *, workspaceId: str, componentTypeId: str
    ) -> DeleteComponentTypeResponseTypeDef:
        """
        Deletes a component type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.delete_component_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#delete_component_type)
        """

    def delete_entity(
        self, *, workspaceId: str, entityId: str, isRecursive: bool = None
    ) -> DeleteEntityResponseTypeDef:
        """
        Deletes an entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.delete_entity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#delete_entity)
        """

    def delete_scene(self, *, workspaceId: str, sceneId: str) -> Dict[str, Any]:
        """
        Deletes a scene.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.delete_scene)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#delete_scene)
        """

    def delete_sync_job(self, *, workspaceId: str, syncSource: str) -> DeleteSyncJobResponseTypeDef:
        """
        Delete the SyncJob.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.delete_sync_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#delete_sync_job)
        """

    def delete_workspace(self, *, workspaceId: str) -> DeleteWorkspaceResponseTypeDef:
        """
        Deletes a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.delete_workspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#delete_workspace)
        """

    def execute_query(
        self,
        *,
        workspaceId: str,
        queryStatement: str,
        maxResults: int = None,
        nextToken: str = None
    ) -> ExecuteQueryResponseTypeDef:
        """
        Run queries to access information from your knowledge graph of entities within
        individual workspaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.execute_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#execute_query)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#generate_presigned_url)
        """

    def get_component_type(
        self, *, workspaceId: str, componentTypeId: str
    ) -> GetComponentTypeResponseTypeDef:
        """
        Retrieves information about a component type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.get_component_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#get_component_type)
        """

    def get_entity(self, *, workspaceId: str, entityId: str) -> GetEntityResponseTypeDef:
        """
        Retrieves information about an entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.get_entity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#get_entity)
        """

    def get_metadata_transfer_job(
        self, *, metadataTransferJobId: str
    ) -> GetMetadataTransferJobResponseTypeDef:
        """
        Gets a nmetadata transfer job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.get_metadata_transfer_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#get_metadata_transfer_job)
        """

    def get_pricing_plan(self) -> GetPricingPlanResponseTypeDef:
        """
        Gets the pricing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.get_pricing_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#get_pricing_plan)
        """

    def get_property_value(
        self,
        *,
        selectedProperties: List[str],
        workspaceId: str,
        componentName: str = None,
        componentPath: str = None,
        componentTypeId: str = None,
        entityId: str = None,
        maxResults: int = None,
        nextToken: str = None,
        propertyGroupName: str = None,
        tabularConditions: "TabularConditionsTypeDef" = None
    ) -> GetPropertyValueResponseTypeDef:
        """
        Gets the property values for a component, component type, entity, or workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.get_property_value)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#get_property_value)
        """

    def get_property_value_history(
        self,
        *,
        workspaceId: str,
        selectedProperties: List[str],
        entityId: str = None,
        componentName: str = None,
        componentPath: str = None,
        componentTypeId: str = None,
        propertyFilters: List["PropertyFilterTypeDef"] = None,
        startDateTime: Union[datetime, str] = None,
        endDateTime: Union[datetime, str] = None,
        interpolation: "InterpolationParametersTypeDef" = None,
        nextToken: str = None,
        maxResults: int = None,
        orderByTime: OrderByTimeType = None,
        startTime: str = None,
        endTime: str = None
    ) -> GetPropertyValueHistoryResponseTypeDef:
        """
        Retrieves information about the history of a time series property value for a
        component, component type, entity, or workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.get_property_value_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#get_property_value_history)
        """

    def get_scene(self, *, workspaceId: str, sceneId: str) -> GetSceneResponseTypeDef:
        """
        Retrieves information about a scene.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.get_scene)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#get_scene)
        """

    def get_sync_job(
        self, *, syncSource: str, workspaceId: str = None
    ) -> GetSyncJobResponseTypeDef:
        """
        Gets the SyncJob.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.get_sync_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#get_sync_job)
        """

    def get_workspace(self, *, workspaceId: str) -> GetWorkspaceResponseTypeDef:
        """
        Retrieves information about a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.get_workspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#get_workspace)
        """

    def list_component_types(
        self,
        *,
        workspaceId: str,
        filters: List["ListComponentTypesFilterTypeDef"] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListComponentTypesResponseTypeDef:
        """
        Lists all component types in a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.list_component_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#list_component_types)
        """

    def list_components(
        self,
        *,
        workspaceId: str,
        entityId: str,
        componentPath: str = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListComponentsResponseTypeDef:
        """
        This API lists the components of an entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.list_components)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#list_components)
        """

    def list_entities(
        self,
        *,
        workspaceId: str,
        filters: List["ListEntitiesFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListEntitiesResponseTypeDef:
        """
        Lists all entities in a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.list_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#list_entities)
        """

    def list_metadata_transfer_jobs(
        self,
        *,
        sourceType: SourceTypeType,
        destinationType: DestinationTypeType,
        filters: List["ListMetadataTransferJobsFilterTypeDef"] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListMetadataTransferJobsResponseTypeDef:
        """
        Lists the metadata transfer jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.list_metadata_transfer_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#list_metadata_transfer_jobs)
        """

    def list_properties(
        self,
        *,
        workspaceId: str,
        entityId: str,
        componentName: str = None,
        componentPath: str = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListPropertiesResponseTypeDef:
        """
        This API lists the properties of a component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.list_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#list_properties)
        """

    def list_scenes(
        self, *, workspaceId: str, maxResults: int = None, nextToken: str = None
    ) -> ListScenesResponseTypeDef:
        """
        Lists all scenes in a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.list_scenes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#list_scenes)
        """

    def list_sync_jobs(
        self, *, workspaceId: str, maxResults: int = None, nextToken: str = None
    ) -> ListSyncJobsResponseTypeDef:
        """
        List all SyncJobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.list_sync_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#list_sync_jobs)
        """

    def list_sync_resources(
        self,
        *,
        workspaceId: str,
        syncSource: str,
        filters: List["SyncResourceFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListSyncResourcesResponseTypeDef:
        """
        Lists the sync resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.list_sync_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#list_sync_resources)
        """

    def list_tags_for_resource(
        self, *, resourceARN: str, maxResults: int = None, nextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags associated with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#list_tags_for_resource)
        """

    def list_workspaces(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListWorkspacesResponseTypeDef:
        """
        Retrieves information about workspaces in the current account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.list_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#list_workspaces)
        """

    def tag_resource(self, *, resourceARN: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceARN: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#untag_resource)
        """

    def update_component_type(
        self,
        *,
        workspaceId: str,
        componentTypeId: str,
        isSingleton: bool = None,
        description: str = None,
        propertyDefinitions: Dict[str, "PropertyDefinitionRequestTypeDef"] = None,
        extendsFrom: List[str] = None,
        functions: Dict[str, "FunctionRequestTypeDef"] = None,
        propertyGroups: Dict[str, "PropertyGroupRequestTypeDef"] = None,
        componentTypeName: str = None,
        compositeComponentTypes: Dict[str, "CompositeComponentTypeRequestTypeDef"] = None
    ) -> UpdateComponentTypeResponseTypeDef:
        """
        Updates information in a component type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.update_component_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#update_component_type)
        """

    def update_entity(
        self,
        *,
        workspaceId: str,
        entityId: str,
        entityName: str = None,
        description: str = None,
        componentUpdates: Dict[str, "ComponentUpdateRequestTypeDef"] = None,
        compositeComponentUpdates: Dict[str, "CompositeComponentUpdateRequestTypeDef"] = None,
        parentEntityUpdate: "ParentEntityUpdateRequestTypeDef" = None
    ) -> UpdateEntityResponseTypeDef:
        """
        Updates an entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.update_entity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#update_entity)
        """

    def update_pricing_plan(
        self, *, pricingMode: PricingModeType, bundleNames: List[str] = None
    ) -> UpdatePricingPlanResponseTypeDef:
        """
        Update the pricing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.update_pricing_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#update_pricing_plan)
        """

    def update_scene(
        self,
        *,
        workspaceId: str,
        sceneId: str,
        contentLocation: str = None,
        description: str = None,
        capabilities: List[str] = None,
        sceneMetadata: Dict[str, str] = None
    ) -> UpdateSceneResponseTypeDef:
        """
        Updates a scene.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.update_scene)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#update_scene)
        """

    def update_workspace(
        self, *, workspaceId: str, description: str = None, role: str = None, s3Location: str = None
    ) -> UpdateWorkspaceResponseTypeDef:
        """
        Updates a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/iottwinmaker.html#IoTTwinMaker.Client.update_workspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/client.html#update_workspace)
        """
