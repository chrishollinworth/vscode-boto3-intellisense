# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for discovery service client

Usage::

    ```python
    import boto3
    from mypy_boto3_discovery import ApplicationDiscoveryServiceClient

    client: ApplicationDiscoveryServiceClient = boto3.client("discovery")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_discovery.paginator import (
    DescribeAgentsPaginator,
    DescribeContinuousExportsPaginator,
    DescribeExportConfigurationsPaginator,
    DescribeExportTasksPaginator,
    DescribeTagsPaginator,
    ListConfigurationsPaginator,
)
from mypy_boto3_discovery.type_defs import (
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


class ApplicationDiscoveryServiceClient:
    """
    [ApplicationDiscoveryService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_configuration_items_to_application(
        self, applicationConfigurationId: str, configurationIds: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.associate_configuration_items_to_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.associate_configuration_items_to_application)
        """

    def batch_delete_import_data(
        self, importTaskIds: List[str]
    ) -> BatchDeleteImportDataResponseTypeDef:
        """
        [Client.batch_delete_import_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.batch_delete_import_data)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.can_paginate)
        """

    def create_application(
        self, name: str, description: str = None
    ) -> CreateApplicationResponseTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.create_application)
        """

    def create_tags(self, configurationIds: List[str], tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.create_tags)
        """

    def delete_applications(self, configurationIds: List[str]) -> Dict[str, Any]:
        """
        [Client.delete_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.delete_applications)
        """

    def delete_tags(
        self, configurationIds: List[str], tags: List[TagTypeDef] = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.delete_tags)
        """

    def describe_agents(
        self,
        agentIds: List[str] = None,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeAgentsResponseTypeDef:
        """
        [Client.describe_agents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_agents)
        """

    def describe_configurations(
        self, configurationIds: List[str]
    ) -> DescribeConfigurationsResponseTypeDef:
        """
        [Client.describe_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_configurations)
        """

    def describe_continuous_exports(
        self, exportIds: List[str] = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeContinuousExportsResponseTypeDef:
        """
        [Client.describe_continuous_exports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_continuous_exports)
        """

    def describe_export_configurations(
        self, exportIds: List[str] = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeExportConfigurationsResponseTypeDef:
        """
        [Client.describe_export_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_export_configurations)
        """

    def describe_export_tasks(
        self,
        exportIds: List[str] = None,
        filters: List[ExportFilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeExportTasksResponseTypeDef:
        """
        [Client.describe_export_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_export_tasks)
        """

    def describe_import_tasks(
        self,
        filters: List[ImportTaskFilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeImportTasksResponseTypeDef:
        """
        [Client.describe_import_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_import_tasks)
        """

    def describe_tags(
        self, filters: List[TagFilterTypeDef] = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeTagsResponseTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_tags)
        """

    def disassociate_configuration_items_from_application(
        self, applicationConfigurationId: str, configurationIds: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_configuration_items_from_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.disassociate_configuration_items_from_application)
        """

    def export_configurations(self) -> ExportConfigurationsResponseTypeDef:
        """
        [Client.export_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.export_configurations)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.generate_presigned_url)
        """

    def get_discovery_summary(self) -> GetDiscoverySummaryResponseTypeDef:
        """
        [Client.get_discovery_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.get_discovery_summary)
        """

    def list_configurations(
        self,
        configurationType: Literal["SERVER", "PROCESS", "CONNECTION", "APPLICATION"],
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
        orderBy: List[OrderByElementTypeDef] = None,
    ) -> ListConfigurationsResponseTypeDef:
        """
        [Client.list_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.list_configurations)
        """

    def list_server_neighbors(
        self,
        configurationId: str,
        portInformationNeeded: bool = None,
        neighborConfigurationIds: List[str] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListServerNeighborsResponseTypeDef:
        """
        [Client.list_server_neighbors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.list_server_neighbors)
        """

    def start_continuous_export(self) -> StartContinuousExportResponseTypeDef:
        """
        [Client.start_continuous_export documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_continuous_export)
        """

    def start_data_collection_by_agent_ids(
        self, agentIds: List[str]
    ) -> StartDataCollectionByAgentIdsResponseTypeDef:
        """
        [Client.start_data_collection_by_agent_ids documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_data_collection_by_agent_ids)
        """

    def start_export_task(
        self,
        exportDataFormat: List[Literal["CSV", "GRAPHML"]] = None,
        filters: List[ExportFilterTypeDef] = None,
        startTime: datetime = None,
        endTime: datetime = None,
    ) -> StartExportTaskResponseTypeDef:
        """
        [Client.start_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_export_task)
        """

    def start_import_task(
        self, name: str, importUrl: str, clientRequestToken: str = None
    ) -> StartImportTaskResponseTypeDef:
        """
        [Client.start_import_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_import_task)
        """

    def stop_continuous_export(self, exportId: str) -> StopContinuousExportResponseTypeDef:
        """
        [Client.stop_continuous_export documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.stop_continuous_export)
        """

    def stop_data_collection_by_agent_ids(
        self, agentIds: List[str]
    ) -> StopDataCollectionByAgentIdsResponseTypeDef:
        """
        [Client.stop_data_collection_by_agent_ids documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.stop_data_collection_by_agent_ids)
        """

    def update_application(
        self, configurationId: str, name: str = None, description: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Client.update_application)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_agents"]) -> DescribeAgentsPaginator:
        """
        [Paginator.DescribeAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeAgents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_continuous_exports"]
    ) -> DescribeContinuousExportsPaginator:
        """
        [Paginator.DescribeContinuousExports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeContinuousExports)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_configurations"]
    ) -> DescribeExportConfigurationsPaginator:
        """
        [Paginator.DescribeExportConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportConfigurations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_tasks"]
    ) -> DescribeExportTasksPaginator:
        """
        [Paginator.DescribeExportTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportTasks)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_tags"]) -> DescribeTagsPaginator:
        """
        [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeTags)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configurations"]
    ) -> ListConfigurationsPaginator:
        """
        [Paginator.ListConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.ListConfigurations)
        """
