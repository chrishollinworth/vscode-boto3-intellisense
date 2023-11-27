"""
Type annotations for resource-explorer-2 service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_resource_explorer_2 import ResourceExplorerClient
    from mypy_boto3_resource_explorer_2.paginator import (
        ListIndexesPaginator,
        ListIndexesForMembersPaginator,
        ListSupportedResourceTypesPaginator,
        ListViewsPaginator,
        SearchPaginator,
    )

    client: ResourceExplorerClient = boto3.client("resource-explorer-2")

    list_indexes_paginator: ListIndexesPaginator = client.get_paginator("list_indexes")
    list_indexes_for_members_paginator: ListIndexesForMembersPaginator = client.get_paginator("list_indexes_for_members")
    list_supported_resource_types_paginator: ListSupportedResourceTypesPaginator = client.get_paginator("list_supported_resource_types")
    list_views_paginator: ListViewsPaginator = client.get_paginator("list_views")
    search_paginator: SearchPaginator = client.get_paginator("search")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import IndexTypeType
from .type_defs import (
    ListIndexesForMembersOutputTypeDef,
    ListIndexesOutputTypeDef,
    ListSupportedResourceTypesOutputTypeDef,
    ListViewsOutputTypeDef,
    PaginatorConfigTypeDef,
    SearchOutputTypeDef,
)

__all__ = (
    "ListIndexesPaginator",
    "ListIndexesForMembersPaginator",
    "ListSupportedResourceTypesPaginator",
    "ListViewsPaginator",
    "SearchPaginator",
)

class ListIndexesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/resource-explorer-2.html#ResourceExplorer.Paginator.ListIndexes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators.html#listindexespaginator)
    """

    def paginate(
        self,
        *,
        Regions: List[str] = None,
        Type: IndexTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIndexesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/resource-explorer-2.html#ResourceExplorer.Paginator.ListIndexes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators.html#listindexespaginator)
        """

class ListIndexesForMembersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/resource-explorer-2.html#ResourceExplorer.Paginator.ListIndexesForMembers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators.html#listindexesformemberspaginator)
    """

    def paginate(
        self, *, AccountIdList: List[str], PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIndexesForMembersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/resource-explorer-2.html#ResourceExplorer.Paginator.ListIndexesForMembers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators.html#listindexesformemberspaginator)
        """

class ListSupportedResourceTypesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/resource-explorer-2.html#ResourceExplorer.Paginator.ListSupportedResourceTypes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators.html#listsupportedresourcetypespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSupportedResourceTypesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/resource-explorer-2.html#ResourceExplorer.Paginator.ListSupportedResourceTypes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators.html#listsupportedresourcetypespaginator)
        """

class ListViewsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/resource-explorer-2.html#ResourceExplorer.Paginator.ListViews)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators.html#listviewspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListViewsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/resource-explorer-2.html#ResourceExplorer.Paginator.ListViews.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators.html#listviewspaginator)
        """

class SearchPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/resource-explorer-2.html#ResourceExplorer.Paginator.Search)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators.html#searchpaginator)
    """

    def paginate(
        self,
        *,
        QueryString: str,
        ViewArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/resource-explorer-2.html#ResourceExplorer.Paginator.Search.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators.html#searchpaginator)
        """
