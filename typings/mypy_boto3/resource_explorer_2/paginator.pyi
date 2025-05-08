"""
Type annotations for resource-explorer-2 service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_resource_explorer_2.client import ResourceExplorerClient
    from mypy_boto3_resource_explorer_2.paginator import (
        ListIndexesForMembersPaginator,
        ListIndexesPaginator,
        ListManagedViewsPaginator,
        ListResourcesPaginator,
        ListSupportedResourceTypesPaginator,
        ListViewsPaginator,
        SearchPaginator,
    )

    session = Session()
    client: ResourceExplorerClient = session.client("resource-explorer-2")

    list_indexes_for_members_paginator: ListIndexesForMembersPaginator = client.get_paginator("list_indexes_for_members")
    list_indexes_paginator: ListIndexesPaginator = client.get_paginator("list_indexes")
    list_managed_views_paginator: ListManagedViewsPaginator = client.get_paginator("list_managed_views")
    list_resources_paginator: ListResourcesPaginator = client.get_paginator("list_resources")
    list_supported_resource_types_paginator: ListSupportedResourceTypesPaginator = client.get_paginator("list_supported_resource_types")
    list_views_paginator: ListViewsPaginator = client.get_paginator("list_views")
    search_paginator: SearchPaginator = client.get_paginator("search")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListIndexesForMembersInputPaginateTypeDef,
    ListIndexesForMembersOutputTypeDef,
    ListIndexesInputPaginateTypeDef,
    ListIndexesOutputTypeDef,
    ListManagedViewsInputPaginateTypeDef,
    ListManagedViewsOutputTypeDef,
    ListResourcesInputPaginateTypeDef,
    ListResourcesOutputTypeDef,
    ListSupportedResourceTypesInputPaginateTypeDef,
    ListSupportedResourceTypesOutputTypeDef,
    ListViewsInputPaginateTypeDef,
    ListViewsOutputTypeDef,
    SearchInputPaginateTypeDef,
    SearchOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListIndexesForMembersPaginator",
    "ListIndexesPaginator",
    "ListManagedViewsPaginator",
    "ListResourcesPaginator",
    "ListSupportedResourceTypesPaginator",
    "ListViewsPaginator",
    "SearchPaginator",
)

if TYPE_CHECKING:
    _ListIndexesForMembersPaginatorBase = Paginator[ListIndexesForMembersOutputTypeDef]
else:
    _ListIndexesForMembersPaginatorBase = Paginator  # type: ignore[assignment]

class ListIndexesForMembersPaginator(_ListIndexesForMembersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/ListIndexesForMembers.html#ResourceExplorer.Paginator.ListIndexesForMembers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#listindexesformemberspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIndexesForMembersInputPaginateTypeDef]
    ) -> PageIterator[ListIndexesForMembersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/ListIndexesForMembers.html#ResourceExplorer.Paginator.ListIndexesForMembers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#listindexesformemberspaginator)
        """

if TYPE_CHECKING:
    _ListIndexesPaginatorBase = Paginator[ListIndexesOutputTypeDef]
else:
    _ListIndexesPaginatorBase = Paginator  # type: ignore[assignment]

class ListIndexesPaginator(_ListIndexesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/ListIndexes.html#ResourceExplorer.Paginator.ListIndexes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#listindexespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIndexesInputPaginateTypeDef]
    ) -> PageIterator[ListIndexesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/ListIndexes.html#ResourceExplorer.Paginator.ListIndexes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#listindexespaginator)
        """

if TYPE_CHECKING:
    _ListManagedViewsPaginatorBase = Paginator[ListManagedViewsOutputTypeDef]
else:
    _ListManagedViewsPaginatorBase = Paginator  # type: ignore[assignment]

class ListManagedViewsPaginator(_ListManagedViewsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/ListManagedViews.html#ResourceExplorer.Paginator.ListManagedViews)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#listmanagedviewspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListManagedViewsInputPaginateTypeDef]
    ) -> PageIterator[ListManagedViewsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/ListManagedViews.html#ResourceExplorer.Paginator.ListManagedViews.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#listmanagedviewspaginator)
        """

if TYPE_CHECKING:
    _ListResourcesPaginatorBase = Paginator[ListResourcesOutputTypeDef]
else:
    _ListResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourcesPaginator(_ListResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/ListResources.html#ResourceExplorer.Paginator.ListResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#listresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourcesInputPaginateTypeDef]
    ) -> PageIterator[ListResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/ListResources.html#ResourceExplorer.Paginator.ListResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#listresourcespaginator)
        """

if TYPE_CHECKING:
    _ListSupportedResourceTypesPaginatorBase = Paginator[ListSupportedResourceTypesOutputTypeDef]
else:
    _ListSupportedResourceTypesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSupportedResourceTypesPaginator(_ListSupportedResourceTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/ListSupportedResourceTypes.html#ResourceExplorer.Paginator.ListSupportedResourceTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#listsupportedresourcetypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSupportedResourceTypesInputPaginateTypeDef]
    ) -> PageIterator[ListSupportedResourceTypesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/ListSupportedResourceTypes.html#ResourceExplorer.Paginator.ListSupportedResourceTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#listsupportedresourcetypespaginator)
        """

if TYPE_CHECKING:
    _ListViewsPaginatorBase = Paginator[ListViewsOutputTypeDef]
else:
    _ListViewsPaginatorBase = Paginator  # type: ignore[assignment]

class ListViewsPaginator(_ListViewsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/ListViews.html#ResourceExplorer.Paginator.ListViews)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#listviewspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListViewsInputPaginateTypeDef]
    ) -> PageIterator[ListViewsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/ListViews.html#ResourceExplorer.Paginator.ListViews.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#listviewspaginator)
        """

if TYPE_CHECKING:
    _SearchPaginatorBase = Paginator[SearchOutputTypeDef]
else:
    _SearchPaginatorBase = Paginator  # type: ignore[assignment]

class SearchPaginator(_SearchPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/Search.html#ResourceExplorer.Paginator.Search)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#searchpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchInputPaginateTypeDef]
    ) -> PageIterator[SearchOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/Search.html#ResourceExplorer.Paginator.Search.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#searchpaginator)
        """
