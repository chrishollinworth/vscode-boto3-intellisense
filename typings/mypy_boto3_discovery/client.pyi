"""
Type annotations for discovery service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_discovery import ApplicationDiscoveryServiceClient

    client: ApplicationDiscoveryServiceClient = boto3.client("discovery")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ConfigurationItemTypeType, ExportDataFormatType
from .paginator import (
    DescribeAgentsPaginator,
    DescribeContinuousExportsPaginator,
    DescribeExportConfigurationsPaginator,
    DescribeExportTasksPaginator,
    DescribeTagsPaginator,
    ListConfigurationsPaginator,
)
from .type_defs import (
    BatchDeleteImportDataResponseTypeDef,
    CreateApplicationResponseTypeDef,
    DescribeAgentsResponseTypeDef,
    DescribeConfigurationsResponseTypeDef,
    DescribeContinuousExportsResponseTypeDef,
    DescribeExportConfigurationsResponseTypeDef,
    DescribeExportTasksResponseTypeDef,
    DescribeImportTasksResponseTypeDef,
    DescribeTagsResponseTypeDef,
    ExportConfigurationsResponseTypeDef,
    ExportFilterTypeDef,
    FilterTypeDef,
    GetDiscoverySummaryResponseTypeDef,
    ImportTaskFilterTypeDef,
    ListConfigurationsResponseTypeDef,
    ListServerNeighborsResponseTypeDef,
    OrderByElementTypeDef,
    StartContinuousExportResponseTypeDef,
    StartDataCollectionByAgentIdsResponseTypeDef,
    StartExportTaskResponseTypeDef,
    StartImportTaskResponseTypeDef,
    StopContinuousExportResponseTypeDef,
    StopDataCollectionByAgentIdsResponseTypeDef,
    TagFilterTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ApplicationDiscoveryServiceClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AuthorizationErrorException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictErrorException: Type[BotocoreClientError]
    HomeRegionNotSetException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    OperationNotPermittedException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServerInternalErrorException: Type[BotocoreClientError]

class ApplicationDiscoveryServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ApplicationDiscoveryServiceClient exceptions.
        """
    def associate_configuration_items_to_application(
        self, *, applicationConfigurationId: str, configurationIds: List[str]
    ) -> Dict[str, Any]:
        """
        Associates one or more configuration items with an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.associate_configuration_items_to_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#associate_configuration_items_to_application)
        """
    def batch_delete_import_data(
        self, *, importTaskIds: List[str]
    ) -> BatchDeleteImportDataResponseTypeDef:
        """
        Deletes one or more import tasks, each identified by their import ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.batch_delete_import_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#batch_delete_import_data)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#close)
        """
    def create_application(
        self, *, name: str, description: str = None
    ) -> CreateApplicationResponseTypeDef:
        """
        Creates an application with the given name and description.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.create_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#create_application)
        """
    def create_tags(
        self, *, configurationIds: List[str], tags: List["TagTypeDef"]
    ) -> Dict[str, Any]:
        """
        Creates one or more tags for configuration items.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#create_tags)
        """
    def delete_applications(self, *, configurationIds: List[str]) -> Dict[str, Any]:
        """
        Deletes a list of applications and their associations with configuration items.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.delete_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#delete_applications)
        """
    def delete_tags(
        self, *, configurationIds: List[str], tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Deletes the association between configuration items and one or more tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.delete_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#delete_tags)
        """
    def describe_agents(
        self,
        *,
        agentIds: List[str] = None,
        filters: List["FilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeAgentsResponseTypeDef:
        """
        Lists agents or connectors as specified by ID or other filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_agents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#describe_agents)
        """
    def describe_configurations(
        self, *, configurationIds: List[str]
    ) -> DescribeConfigurationsResponseTypeDef:
        """
        Retrieves attributes for a list of configuration item IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#describe_configurations)
        """
    def describe_continuous_exports(
        self, *, exportIds: List[str] = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeContinuousExportsResponseTypeDef:
        """
        Lists exports as specified by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_continuous_exports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#describe_continuous_exports)
        """
    def describe_export_configurations(
        self, *, exportIds: List[str] = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeExportConfigurationsResponseTypeDef:
        """
        `DescribeExportConfigurations` is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_export_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#describe_export_configurations)
        """
    def describe_export_tasks(
        self,
        *,
        exportIds: List[str] = None,
        filters: List["ExportFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeExportTasksResponseTypeDef:
        """
        Retrieve status of one or more export tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_export_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#describe_export_tasks)
        """
    def describe_import_tasks(
        self,
        *,
        filters: List["ImportTaskFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeImportTasksResponseTypeDef:
        """
        Returns an array of import tasks for your account, including status information,
        times, IDs, the Amazon S3 Object URL for the import file, and more.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_import_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#describe_import_tasks)
        """
    def describe_tags(
        self,
        *,
        filters: List["TagFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeTagsResponseTypeDef:
        """
        Retrieves a list of configuration items that have tags as specified by the key-
        value pairs, name and value, passed to the optional parameter `filters` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#describe_tags)
        """
    def disassociate_configuration_items_from_application(
        self, *, applicationConfigurationId: str, configurationIds: List[str]
    ) -> Dict[str, Any]:
        """
        Disassociates one or more configuration items from an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.disassociate_configuration_items_from_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#disassociate_configuration_items_from_application)
        """
    def export_configurations(self) -> ExportConfigurationsResponseTypeDef:
        """
        Deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.export_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#export_configurations)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#generate_presigned_url)
        """
    def get_discovery_summary(self) -> GetDiscoverySummaryResponseTypeDef:
        """
        Retrieves a short summary of discovered assets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.get_discovery_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#get_discovery_summary)
        """
    def list_configurations(
        self,
        *,
        configurationType: ConfigurationItemTypeType,
        filters: List["FilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None,
        orderBy: List["OrderByElementTypeDef"] = None
    ) -> ListConfigurationsResponseTypeDef:
        """
        Retrieves a list of configuration items as specified by the value passed to the
        required parameter `configurationType`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.list_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#list_configurations)
        """
    def list_server_neighbors(
        self,
        *,
        configurationId: str,
        portInformationNeeded: bool = None,
        neighborConfigurationIds: List[str] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListServerNeighborsResponseTypeDef:
        """
        Retrieves a list of servers that are one network hop away from a specified
        server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.list_server_neighbors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#list_server_neighbors)
        """
    def start_continuous_export(self) -> StartContinuousExportResponseTypeDef:
        """
        Start the continuous flow of agent's discovered data into Amazon Athena.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_continuous_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#start_continuous_export)
        """
    def start_data_collection_by_agent_ids(
        self, *, agentIds: List[str]
    ) -> StartDataCollectionByAgentIdsResponseTypeDef:
        """
        Instructs the specified agents or connectors to start collecting data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_data_collection_by_agent_ids)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#start_data_collection_by_agent_ids)
        """
    def start_export_task(
        self,
        *,
        exportDataFormat: List[ExportDataFormatType] = None,
        filters: List["ExportFilterTypeDef"] = None,
        startTime: Union[datetime, str] = None,
        endTime: Union[datetime, str] = None
    ) -> StartExportTaskResponseTypeDef:
        """
        Begins the export of discovered data to an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_export_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#start_export_task)
        """
    def start_import_task(
        self, *, name: str, importUrl: str, clientRequestToken: str = None
    ) -> StartImportTaskResponseTypeDef:
        """
        Starts an import task, which allows you to import details of your on-premises
        environment directly into Amazon Web Services Migration Hub without having to
        use the Application Discovery Service (ADS) tools such as the Discovery
        Connector or Discovery Agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_import_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#start_import_task)
        """
    def stop_continuous_export(self, *, exportId: str) -> StopContinuousExportResponseTypeDef:
        """
        Stop the continuous flow of agent's discovered data into Amazon Athena.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.stop_continuous_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#stop_continuous_export)
        """
    def stop_data_collection_by_agent_ids(
        self, *, agentIds: List[str]
    ) -> StopDataCollectionByAgentIdsResponseTypeDef:
        """
        Instructs the specified agents or connectors to stop collecting data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.stop_data_collection_by_agent_ids)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#stop_data_collection_by_agent_ids)
        """
    def update_application(
        self, *, configurationId: str, name: str = None, description: str = None
    ) -> Dict[str, Any]:
        """
        Updates metadata about an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Client.update_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/client.html#update_application)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_agents"]) -> DescribeAgentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeAgents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators.html#describeagentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_continuous_exports"]
    ) -> DescribeContinuousExportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeContinuousExports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators.html#describecontinuousexportspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_configurations"]
    ) -> DescribeExportConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators.html#describeexportconfigurationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_tasks"]
    ) -> DescribeExportTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators.html#describeexporttaskspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_tags"]) -> DescribeTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeTags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators.html#describetagspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_configurations"]
    ) -> ListConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.ListConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators.html#listconfigurationspaginator)
        """
