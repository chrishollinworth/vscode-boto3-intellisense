"""
Type annotations for resource-explorer-2 service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_resource_explorer_2.client import ResourceExplorerClient
    from mypy_boto3_resource_explorer_2.paginator import (
        GetResourceExplorerSetupPaginator,
        ListIndexesForMembersPaginator,
        ListIndexesPaginator,
        ListManagedViewsPaginator,
        ListResourcesPaginator,
        ListServiceIndexesPaginator,
        ListServiceViewsPaginator,
        ListStreamingAccessForServicesPaginator,
        ListSupportedResourceTypesPaginator,
        ListViewsPaginator,
        SearchPaginator,
    )

    session = Session()
    client: ResourceExplorerClient = session.client("resource-explorer-2")

    get_resource_explorer_setup_paginator: GetResourceExplorerSetupPaginator = client.get_paginator("get_resource_explorer_setup")
    list_indexes_for_members_paginator: ListIndexesForMembersPaginator = client.get_paginator("list_indexes_for_members")
    list_indexes_paginator: ListIndexesPaginator = client.get_paginator("list_indexes")
    list_managed_views_paginator: ListManagedViewsPaginator = client.get_paginator("list_managed_views")
    list_resources_paginator: ListResourcesPaginator = client.get_paginator("list_resources")
    list_service_indexes_paginator: ListServiceIndexesPaginator = client.get_paginator("list_service_indexes")
    list_service_views_paginator: ListServiceViewsPaginator = client.get_paginator("list_service_views")
    list_streaming_access_for_services_paginator: ListStreamingAccessForServicesPaginator = client.get_paginator("list_streaming_access_for_services")
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
    GetResourceExplorerSetupInputPaginateTypeDef,
    GetResourceExplorerSetupOutputTypeDef,
    ListIndexesForMembersInputPaginateTypeDef,
    ListIndexesForMembersOutputTypeDef,
    ListIndexesInputPaginateTypeDef,
    ListIndexesOutputTypeDef,
    ListManagedViewsInputPaginateTypeDef,
    ListManagedViewsOutputTypeDef,
    ListResourcesInputPaginateTypeDef,
    ListResourcesOutputTypeDef,
    ListServiceIndexesInputPaginateTypeDef,
    ListServiceIndexesOutputTypeDef,
    ListServiceViewsInputPaginateTypeDef,
    ListServiceViewsOutputTypeDef,
    ListStreamingAccessForServicesInputPaginateTypeDef,
    ListStreamingAccessForServicesOutputTypeDef,
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
    "GetResourceExplorerSetupPaginator",
    "ListIndexesForMembersPaginator",
    "ListIndexesPaginator",
    "ListManagedViewsPaginator",
    "ListResourcesPaginator",
    "ListServiceIndexesPaginator",
    "ListServiceViewsPaginator",
    "ListStreamingAccessForServicesPaginator",
    "ListSupportedResourceTypesPaginator",
    "ListViewsPaginator",
    "SearchPaginator",
)

if TYPE_CHECKING:
    _GetResourceExplorerSetupPaginatorBase = Paginator[GetResourceExplorerSetupOutputTypeDef]
else:
    _GetResourceExplorerSetupPaginatorBase = Paginator  # type: ignore[assignment]

class GetResourceExplorerSetupPaginator(_GetResourceExplorerSetupPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/GetResourceExplorerSetup.html#ResourceExplorer.Paginator.GetResourceExplorerSetup)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#getresourceexplorersetuppaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetResourceExplorerSetupInputPaginateTypeDef]
    ) -> PageIterator[GetResourceExplorerSetupOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/GetResourceExplorerSetup.html#ResourceExplorer.Paginator.GetResourceExplorerSetup.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#getresourceexplorersetuppaginator)
        """

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
    _ListServiceIndexesPaginatorBase = Paginator[ListServiceIndexesOutputTypeDef]
else:
    _ListServiceIndexesPaginatorBase = Paginator  # type: ignore[assignment]

class ListServiceIndexesPaginator(_ListServiceIndexesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/ListServiceIndexes.html#ResourceExplorer.Paginator.ListServiceIndexes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#listserviceindexespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServiceIndexesInputPaginateTypeDef]
    ) -> PageIterator[ListServiceIndexesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/ListServiceIndexes.html#ResourceExplorer.Paginator.ListServiceIndexes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#listserviceindexespaginator)
        """

if TYPE_CHECKING:
    _ListServiceViewsPaginatorBase = Paginator[ListServiceViewsOutputTypeDef]
else:
    _ListServiceViewsPaginatorBase = Paginator  # type: ignore[assignment]

class ListServiceViewsPaginator(_ListServiceViewsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/ListServiceViews.html#ResourceExplorer.Paginator.ListServiceViews)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#listserviceviewspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServiceViewsInputPaginateTypeDef]
    ) -> PageIterator[ListServiceViewsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/ListServiceViews.html#ResourceExplorer.Paginator.ListServiceViews.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#listserviceviewspaginator)
        """

if TYPE_CHECKING:
    _ListStreamingAccessForServicesPaginatorBase = Paginator[
        ListStreamingAccessForServicesOutputTypeDef
    ]
else:
    _ListStreamingAccessForServicesPaginatorBase = Paginator  # type: ignore[assignment]

class ListStreamingAccessForServicesPaginator(_ListStreamingAccessForServicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/ListStreamingAccessForServices.html#ResourceExplorer.Paginator.ListStreamingAccessForServices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#liststreamingaccessforservicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStreamingAccessForServicesInputPaginateTypeDef]
    ) -> PageIterator[ListStreamingAccessForServicesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/paginator/ListStreamingAccessForServices.html#ResourceExplorer.Paginator.ListStreamingAccessForServices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/paginators/#liststreamingaccessforservicespaginator)
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
