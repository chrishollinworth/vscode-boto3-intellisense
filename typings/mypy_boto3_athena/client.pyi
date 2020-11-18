# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for athena service client

Usage::

    ```python
    import boto3
    from mypy_boto3_athena import AthenaClient

    client: AthenaClient = boto3.client("athena")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_athena.paginator import (
    GetQueryResultsPaginator,
    ListDatabasesPaginator,
    ListDataCatalogsPaginator,
    ListNamedQueriesPaginator,
    ListQueryExecutionsPaginator,
    ListTableMetadataPaginator,
    ListTagsForResourcePaginator,
)
from mypy_boto3_athena.type_defs import (
    BatchGetNamedQueryOutputTypeDef,
    BatchGetQueryExecutionOutputTypeDef,
    CreateNamedQueryOutputTypeDef,
    GetDatabaseOutputTypeDef,
    GetDataCatalogOutputTypeDef,
    GetNamedQueryOutputTypeDef,
    GetQueryExecutionOutputTypeDef,
    GetQueryResultsOutputTypeDef,
    GetTableMetadataOutputTypeDef,
    GetWorkGroupOutputTypeDef,
    ListDatabasesOutputTypeDef,
    ListDataCatalogsOutputTypeDef,
    ListNamedQueriesOutputTypeDef,
    ListQueryExecutionsOutputTypeDef,
    ListTableMetadataOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListWorkGroupsOutputTypeDef,
    QueryExecutionContextTypeDef,
    ResultConfigurationTypeDef,
    StartQueryExecutionOutputTypeDef,
    TagTypeDef,
    WorkGroupConfigurationTypeDef,
    WorkGroupConfigurationUpdatesTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AthenaClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    MetadataException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]


class AthenaClient:
    """
    [Athena.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_get_named_query(self, NamedQueryIds: List[str]) -> BatchGetNamedQueryOutputTypeDef:
        """
        [Client.batch_get_named_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.batch_get_named_query)
        """

    def batch_get_query_execution(
        self, QueryExecutionIds: List[str]
    ) -> BatchGetQueryExecutionOutputTypeDef:
        """
        [Client.batch_get_query_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.batch_get_query_execution)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.can_paginate)
        """

    def create_data_catalog(
        self,
        Name: str,
        Type: Literal["LAMBDA", "GLUE", "HIVE"],
        Description: str = None,
        Parameters: Dict[str, str] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_data_catalog documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.create_data_catalog)
        """

    def create_named_query(
        self,
        Name: str,
        Database: str,
        QueryString: str,
        Description: str = None,
        ClientRequestToken: str = None,
        WorkGroup: str = None,
    ) -> CreateNamedQueryOutputTypeDef:
        """
        [Client.create_named_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.create_named_query)
        """

    def create_work_group(
        self,
        Name: str,
        Configuration: "WorkGroupConfigurationTypeDef" = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_work_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.create_work_group)
        """

    def delete_data_catalog(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_data_catalog documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.delete_data_catalog)
        """

    def delete_named_query(self, NamedQueryId: str) -> Dict[str, Any]:
        """
        [Client.delete_named_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.delete_named_query)
        """

    def delete_work_group(
        self, WorkGroup: str, RecursiveDeleteOption: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_work_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.delete_work_group)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.generate_presigned_url)
        """

    def get_data_catalog(self, Name: str) -> GetDataCatalogOutputTypeDef:
        """
        [Client.get_data_catalog documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.get_data_catalog)
        """

    def get_database(self, CatalogName: str, DatabaseName: str) -> GetDatabaseOutputTypeDef:
        """
        [Client.get_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.get_database)
        """

    def get_named_query(self, NamedQueryId: str) -> GetNamedQueryOutputTypeDef:
        """
        [Client.get_named_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.get_named_query)
        """

    def get_query_execution(self, QueryExecutionId: str) -> GetQueryExecutionOutputTypeDef:
        """
        [Client.get_query_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.get_query_execution)
        """

    def get_query_results(
        self, QueryExecutionId: str, NextToken: str = None, MaxResults: int = None
    ) -> GetQueryResultsOutputTypeDef:
        """
        [Client.get_query_results documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.get_query_results)
        """

    def get_table_metadata(
        self, CatalogName: str, DatabaseName: str, TableName: str
    ) -> GetTableMetadataOutputTypeDef:
        """
        [Client.get_table_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.get_table_metadata)
        """

    def get_work_group(self, WorkGroup: str) -> GetWorkGroupOutputTypeDef:
        """
        [Client.get_work_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.get_work_group)
        """

    def list_data_catalogs(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListDataCatalogsOutputTypeDef:
        """
        [Client.list_data_catalogs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.list_data_catalogs)
        """

    def list_databases(
        self, CatalogName: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDatabasesOutputTypeDef:
        """
        [Client.list_databases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.list_databases)
        """

    def list_named_queries(
        self, NextToken: str = None, MaxResults: int = None, WorkGroup: str = None
    ) -> ListNamedQueriesOutputTypeDef:
        """
        [Client.list_named_queries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.list_named_queries)
        """

    def list_query_executions(
        self, NextToken: str = None, MaxResults: int = None, WorkGroup: str = None
    ) -> ListQueryExecutionsOutputTypeDef:
        """
        [Client.list_query_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.list_query_executions)
        """

    def list_table_metadata(
        self,
        CatalogName: str,
        DatabaseName: str,
        Expression: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListTableMetadataOutputTypeDef:
        """
        [Client.list_table_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.list_table_metadata)
        """

    def list_tags_for_resource(
        self, ResourceARN: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.list_tags_for_resource)
        """

    def list_work_groups(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListWorkGroupsOutputTypeDef:
        """
        [Client.list_work_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.list_work_groups)
        """

    def start_query_execution(
        self,
        QueryString: str,
        ClientRequestToken: str = None,
        QueryExecutionContext: "QueryExecutionContextTypeDef" = None,
        ResultConfiguration: "ResultConfigurationTypeDef" = None,
        WorkGroup: str = None,
    ) -> StartQueryExecutionOutputTypeDef:
        """
        [Client.start_query_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.start_query_execution)
        """

    def stop_query_execution(self, QueryExecutionId: str) -> Dict[str, Any]:
        """
        [Client.stop_query_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.stop_query_execution)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.untag_resource)
        """

    def update_data_catalog(
        self,
        Name: str,
        Type: Literal["LAMBDA", "GLUE", "HIVE"],
        Description: str = None,
        Parameters: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_data_catalog documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.update_data_catalog)
        """

    def update_work_group(
        self,
        WorkGroup: str,
        Description: str = None,
        ConfigurationUpdates: WorkGroupConfigurationUpdatesTypeDef = None,
        State: Literal["ENABLED", "DISABLED"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_work_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Client.update_work_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_query_results"]
    ) -> GetQueryResultsPaginator:
        """
        [Paginator.GetQueryResults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.GetQueryResults)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_catalogs"]
    ) -> ListDataCatalogsPaginator:
        """
        [Paginator.ListDataCatalogs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.ListDataCatalogs)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_databases"]) -> ListDatabasesPaginator:
        """
        [Paginator.ListDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.ListDatabases)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_named_queries"]
    ) -> ListNamedQueriesPaginator:
        """
        [Paginator.ListNamedQueries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.ListNamedQueries)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_query_executions"]
    ) -> ListQueryExecutionsPaginator:
        """
        [Paginator.ListQueryExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.ListQueryExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_table_metadata"]
    ) -> ListTableMetadataPaginator:
        """
        [Paginator.ListTableMetadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.ListTableMetadata)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.ListTagsForResource)
        """
