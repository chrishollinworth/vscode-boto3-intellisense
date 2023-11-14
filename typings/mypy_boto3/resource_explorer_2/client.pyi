"""
Type annotations for resource-explorer-2 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_resource_explorer_2 import ResourceExplorerClient

    client: ResourceExplorerClient = boto3.client("resource-explorer-2")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import IndexTypeType
from .paginator import (
    ListIndexesPaginator,
    ListSupportedResourceTypesPaginator,
    ListViewsPaginator,
    SearchPaginator,
)
from .type_defs import (
    AssociateDefaultViewOutputTypeDef,
    BatchGetViewOutputTypeDef,
    CreateIndexOutputTypeDef,
    CreateViewOutputTypeDef,
    DeleteIndexOutputTypeDef,
    DeleteViewOutputTypeDef,
    GetDefaultViewOutputTypeDef,
    GetIndexOutputTypeDef,
    GetViewOutputTypeDef,
    IncludedPropertyTypeDef,
    ListIndexesOutputTypeDef,
    ListSupportedResourceTypesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListViewsOutputTypeDef,
    SearchFilterTypeDef,
    SearchOutputTypeDef,
    UpdateIndexTypeOutputTypeDef,
    UpdateViewOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ResourceExplorerClient",)

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
    UnauthorizedException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ResourceExplorerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ResourceExplorerClient exceptions.
        """
    def associate_default_view(self, *, ViewArn: str) -> AssociateDefaultViewOutputTypeDef:
        """
        Sets the specified view as the default for the Amazon Web Services Region in
        which you call this operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.associate_default_view)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#associate_default_view)
        """
    def batch_get_view(self, *, ViewArns: List[str] = None) -> BatchGetViewOutputTypeDef:
        """
        Retrieves details about a list of views.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.batch_get_view)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#batch_get_view)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#close)
        """
    def create_index(
        self, *, ClientToken: str = None, Tags: Dict[str, str] = None
    ) -> CreateIndexOutputTypeDef:
        """
        Turns on Amazon Web Services Resource Explorer in the Amazon Web Services Region
        in which you called this operation by creating an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.create_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#create_index)
        """
    def create_view(
        self,
        *,
        ViewName: str,
        ClientToken: str = None,
        Filters: "SearchFilterTypeDef" = None,
        IncludedProperties: List["IncludedPropertyTypeDef"] = None,
        Tags: Dict[str, str] = None
    ) -> CreateViewOutputTypeDef:
        """
        Creates a view that users can query by using the  Search operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.create_view)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#create_view)
        """
    def delete_index(self, *, Arn: str) -> DeleteIndexOutputTypeDef:
        """
        Deletes the specified index and turns off Amazon Web Services Resource Explorer
        in the specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.delete_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#delete_index)
        """
    def delete_view(self, *, ViewArn: str) -> DeleteViewOutputTypeDef:
        """
        Deletes the specified view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.delete_view)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#delete_view)
        """
    def disassociate_default_view(self) -> None:
        """
        After you call this operation, the affected Amazon Web Services Region no longer
        has a default view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.disassociate_default_view)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#disassociate_default_view)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#generate_presigned_url)
        """
    def get_default_view(self) -> GetDefaultViewOutputTypeDef:
        """
        Retrieves the Amazon Resource Name (ARN) of the view that is the default for the
        Amazon Web Services Region in which you call this operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.get_default_view)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#get_default_view)
        """
    def get_index(self) -> GetIndexOutputTypeDef:
        """
        Retrieves details about the Amazon Web Services Resource Explorer index in the
        Amazon Web Services Region in which you invoked the operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.get_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#get_index)
        """
    def get_view(self, *, ViewArn: str) -> GetViewOutputTypeDef:
        """
        Retrieves details of the specified view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.get_view)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#get_view)
        """
    def list_indexes(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        Regions: List[str] = None,
        Type: IndexTypeType = None
    ) -> ListIndexesOutputTypeDef:
        """
        Retrieves a list of all of the indexes in Amazon Web Services Regions that are
        currently collecting resource information for Amazon Web Services Resource
        Explorer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.list_indexes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#list_indexes)
        """
    def list_supported_resource_types(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListSupportedResourceTypesOutputTypeDef:
        """
        Retrieves a list of all resource types currently supported by Amazon Web
        Services Resource Explorer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.list_supported_resource_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#list_supported_resource_types)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Lists the tags that are attached to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#list_tags_for_resource)
        """
    def list_views(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListViewsOutputTypeDef:
        """
        Lists the `Amazon resource names (ARNs)
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
        of the views available in the Amazon Web Services Region in which you call this
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.list_views)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#list_views)
        """
    def search(
        self,
        *,
        QueryString: str,
        MaxResults: int = None,
        NextToken: str = None,
        ViewArn: str = None
    ) -> SearchOutputTypeDef:
        """
        Searches for resources and displays details about all resources that match the
        specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.search)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#search)
        """
    def tag_resource(self, *, resourceArn: str, Tags: Dict[str, str] = None) -> Dict[str, Any]:
        """
        Adds one or more tag key and value pairs to an Amazon Web Services Resource
        Explorer view or index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tag key and value pairs from an Amazon Web Services Resource
        Explorer view or index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#untag_resource)
        """
    def update_index_type(self, *, Arn: str, Type: IndexTypeType) -> UpdateIndexTypeOutputTypeDef:
        """
        Changes the type of the index from one of the following types to the other.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.update_index_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#update_index_type)
        """
    def update_view(
        self,
        *,
        ViewArn: str,
        Filters: "SearchFilterTypeDef" = None,
        IncludedProperties: List["IncludedPropertyTypeDef"] = None
    ) -> UpdateViewOutputTypeDef:
        """
        Modifies some of the details of a view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Client.update_view)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client.html#update_view)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_indexes"]) -> ListIndexesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Paginator.ListIndexes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators.html#listindexespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_supported_resource_types"]
    ) -> ListSupportedResourceTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Paginator.ListSupportedResourceTypes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators.html#listsupportedresourcetypespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_views"]) -> ListViewsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Paginator.ListViews)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators.html#listviewspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["search"]) -> SearchPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-explorer-2.html#ResourceExplorer.Paginator.Search)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators.html#searchpaginator)
        """
