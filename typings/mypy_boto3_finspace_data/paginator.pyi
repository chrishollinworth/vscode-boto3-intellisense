"""
Type annotations for finspace-data service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_finspace_data.client import FinSpaceDataClient
    from mypy_boto3_finspace_data.paginator import (
        ListChangesetsPaginator,
        ListDataViewsPaginator,
        ListDatasetsPaginator,
        ListPermissionGroupsPaginator,
        ListUsersPaginator,
    )

    session = Session()
    client: FinSpaceDataClient = session.client("finspace-data")

    list_changesets_paginator: ListChangesetsPaginator = client.get_paginator("list_changesets")
    list_data_views_paginator: ListDataViewsPaginator = client.get_paginator("list_data_views")
    list_datasets_paginator: ListDatasetsPaginator = client.get_paginator("list_datasets")
    list_permission_groups_paginator: ListPermissionGroupsPaginator = client.get_paginator("list_permission_groups")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListChangesetsRequestPaginateTypeDef,
    ListChangesetsResponseTypeDef,
    ListDatasetsRequestPaginateTypeDef,
    ListDatasetsResponseTypeDef,
    ListDataViewsRequestPaginateTypeDef,
    ListDataViewsResponseTypeDef,
    ListPermissionGroupsRequestPaginateTypeDef,
    ListPermissionGroupsResponseTypeDef,
    ListUsersRequestPaginateTypeDef,
    ListUsersResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListChangesetsPaginator",
    "ListDataViewsPaginator",
    "ListDatasetsPaginator",
    "ListPermissionGroupsPaginator",
    "ListUsersPaginator",
)

if TYPE_CHECKING:
    _ListChangesetsPaginatorBase = Paginator[ListChangesetsResponseTypeDef]
else:
    _ListChangesetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListChangesetsPaginator(_ListChangesetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace-data/paginator/ListChangesets.html#FinSpaceData.Paginator.ListChangesets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators/#listchangesetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListChangesetsRequestPaginateTypeDef]
    ) -> PageIterator[ListChangesetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace-data/paginator/ListChangesets.html#FinSpaceData.Paginator.ListChangesets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators/#listchangesetspaginator)
        """

if TYPE_CHECKING:
    _ListDataViewsPaginatorBase = Paginator[ListDataViewsResponseTypeDef]
else:
    _ListDataViewsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataViewsPaginator(_ListDataViewsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace-data/paginator/ListDataViews.html#FinSpaceData.Paginator.ListDataViews)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators/#listdataviewspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataViewsRequestPaginateTypeDef]
    ) -> PageIterator[ListDataViewsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace-data/paginator/ListDataViews.html#FinSpaceData.Paginator.ListDataViews.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators/#listdataviewspaginator)
        """

if TYPE_CHECKING:
    _ListDatasetsPaginatorBase = Paginator[ListDatasetsResponseTypeDef]
else:
    _ListDatasetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatasetsPaginator(_ListDatasetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace-data/paginator/ListDatasets.html#FinSpaceData.Paginator.ListDatasets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators/#listdatasetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatasetsRequestPaginateTypeDef]
    ) -> PageIterator[ListDatasetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace-data/paginator/ListDatasets.html#FinSpaceData.Paginator.ListDatasets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators/#listdatasetspaginator)
        """

if TYPE_CHECKING:
    _ListPermissionGroupsPaginatorBase = Paginator[ListPermissionGroupsResponseTypeDef]
else:
    _ListPermissionGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPermissionGroupsPaginator(_ListPermissionGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace-data/paginator/ListPermissionGroups.html#FinSpaceData.Paginator.ListPermissionGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators/#listpermissiongroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPermissionGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListPermissionGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace-data/paginator/ListPermissionGroups.html#FinSpaceData.Paginator.ListPermissionGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators/#listpermissiongroupspaginator)
        """

if TYPE_CHECKING:
    _ListUsersPaginatorBase = Paginator[ListUsersResponseTypeDef]
else:
    _ListUsersPaginatorBase = Paginator  # type: ignore[assignment]

class ListUsersPaginator(_ListUsersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace-data/paginator/ListUsers.html#FinSpaceData.Paginator.ListUsers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators/#listuserspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUsersRequestPaginateTypeDef]
    ) -> PageIterator[ListUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace-data/paginator/ListUsers.html#FinSpaceData.Paginator.ListUsers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators/#listuserspaginator)
        """
