"""
Type annotations for keyspaces service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_keyspaces.client import KeyspacesClient
    from mypy_boto3_keyspaces.paginator import (
        ListKeyspacesPaginator,
        ListTablesPaginator,
        ListTagsForResourcePaginator,
        ListTypesPaginator,
    )

    session = Session()
    client: KeyspacesClient = session.client("keyspaces")

    list_keyspaces_paginator: ListKeyspacesPaginator = client.get_paginator("list_keyspaces")
    list_tables_paginator: ListTablesPaginator = client.get_paginator("list_tables")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_types_paginator: ListTypesPaginator = client.get_paginator("list_types")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListKeyspacesRequestPaginateTypeDef,
    ListKeyspacesResponseTypeDef,
    ListTablesRequestPaginateTypeDef,
    ListTablesResponseTypeDef,
    ListTagsForResourceRequestPaginateTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTypesRequestPaginateTypeDef,
    ListTypesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListKeyspacesPaginator",
    "ListTablesPaginator",
    "ListTagsForResourcePaginator",
    "ListTypesPaginator",
)

if TYPE_CHECKING:
    _ListKeyspacesPaginatorBase = Paginator[ListKeyspacesResponseTypeDef]
else:
    _ListKeyspacesPaginatorBase = Paginator  # type: ignore[assignment]

class ListKeyspacesPaginator(_ListKeyspacesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspaces/paginator/ListKeyspaces.html#Keyspaces.Paginator.ListKeyspaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/paginators/#listkeyspacespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListKeyspacesRequestPaginateTypeDef]
    ) -> PageIterator[ListKeyspacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspaces/paginator/ListKeyspaces.html#Keyspaces.Paginator.ListKeyspaces.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/paginators/#listkeyspacespaginator)
        """

if TYPE_CHECKING:
    _ListTablesPaginatorBase = Paginator[ListTablesResponseTypeDef]
else:
    _ListTablesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTablesPaginator(_ListTablesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspaces/paginator/ListTables.html#Keyspaces.Paginator.ListTables)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/paginators/#listtablespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTablesRequestPaginateTypeDef]
    ) -> PageIterator[ListTablesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspaces/paginator/ListTables.html#Keyspaces.Paginator.ListTables.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/paginators/#listtablespaginator)
        """

if TYPE_CHECKING:
    _ListTagsForResourcePaginatorBase = Paginator[ListTagsForResourceResponseTypeDef]
else:
    _ListTagsForResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsForResourcePaginator(_ListTagsForResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspaces/paginator/ListTagsForResource.html#Keyspaces.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/paginators/#listtagsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsForResourceRequestPaginateTypeDef]
    ) -> PageIterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspaces/paginator/ListTagsForResource.html#Keyspaces.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/paginators/#listtagsforresourcepaginator)
        """

if TYPE_CHECKING:
    _ListTypesPaginatorBase = Paginator[ListTypesResponseTypeDef]
else:
    _ListTypesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTypesPaginator(_ListTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspaces/paginator/ListTypes.html#Keyspaces.Paginator.ListTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/paginators/#listtypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTypesRequestPaginateTypeDef]
    ) -> PageIterator[ListTypesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspaces/paginator/ListTypes.html#Keyspaces.Paginator.ListTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/paginators/#listtypespaginator)
        """
